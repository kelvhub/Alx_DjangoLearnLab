from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin.sites import AlreadyRegistered

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'date_of_birth', 'is_active', 'is_staff')
    search_fields = ('username', 'email')
    list_filter = ('is_active', 'is_staff')

fieldsets = (
        (None, {'fields': ()}),
)

add_fieldsets = UserAdmin.add_fieldsets + (
    (None, {'fields': ()}),
)

try:
    admin.site.register(CustomUser, CustomUserAdmin)
except AlreadyRegistered:
    pass