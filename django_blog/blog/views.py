from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm


from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Post, Comment
from .forms import CommentForm

# --- Existing PostDetailView upgraded to handle comment creation inline ---
class PostDetailView(FormMixin, DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.select_related('author')
        # if form was posted and invalid, self.object is already set; use provided form else blank
        context['comment_form'] = kwargs.get('form') or self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        # allow viewing when not logged in, but only allow posting if authenticated
        self.object = self.get_object()  # sets self.object for get_success_url
        if not request.user.is_authenticated:
            # Redirect to login preserving return URL
            login_url = reverse('login')
            return redirect(f"{login_url}?next={self.get_success_url()}")

        form = self.get_form()
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.author = request.user
            comment.save()
            return redirect(self.get_success_url())
        # Re-render the detail page with form errors
        return self.render_to_response(self.get_context_data(form=form))

# --- Comment edit ---
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def test_func(self):
        return self.request.user == self.get_object().author

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.get_object().post.pk})

# --- Comment delete ---
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def test_func(self):
        return self.request.user == self.get_object().author

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.get_object().post.pk})



# List all posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']

# Show one post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

# Create a post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Update a post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().author

# Delete a post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        return self.request.user == self.get_object().author
