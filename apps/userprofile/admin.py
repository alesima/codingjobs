from django.contrib.auth.admin import User, UserAdmin
from django.contrib import admin

from apps.models.UserProfile import UserProfile


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'profile'


class UserAdmin(UserAdmin):
    inlines = (UserProfileInline,)

    list_display = ['username', 'email', 'first_name', 'last_name']


admin.site.unregister(User)  # Re-register UserAdmin
admin.site.register(User, UserAdmin)
