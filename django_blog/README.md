# Blog Post CRUD – django_blog

## Features
- View all posts
- View single post details
- Create new posts (login required)
- Edit & delete only own posts
- Secure permissions with LoginRequiredMixin and UserPassesTestMixin

## URL Patterns
- `/` → List all posts
- `/posts/<id>/` → View details
- `/posts/new/` → Create post
- `/posts/<id>/edit/` → Edit post
- `/posts/<id>/delete/` → Delete post




## Comments

### Features
- Inline comment creation on post detail page
- Edit/Delete limited to comment author
- CSRF protection on all forms
- Server-side validation (minimum length)

### URLs
- `posts/<id>/` – View post + comments and add a new comment
- `comments/<id>/edit/` – Edit own comment (login required)
- `comments/<id>/delete/` – Delete own comment (login required)

### How to Use
1. Log in, open any post, write a comment, and submit.
2. To edit/delete, use the links shown below your own comment.
3. Unauthorized users cannot modify others’ comments.

