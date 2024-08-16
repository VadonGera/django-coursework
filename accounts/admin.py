from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm
from .models import User


# admin.site.register(User)

# @admin.register(User)
# class CustomUserAdmin(UserAdmin):  # (UserAdmin)
#     model = User
#     list_display = ('email', 'phone_number', 'is_admin',)
#     # list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_active',)
#     list_filter = ('is_admin', 'is_active',)
#     search_fields = ('email',)
#     ordering = ('email',)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm

    list_display = ('email', 'phone_number', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'phone_number',)}),
        ('Permissions', {'fields': ('is_admin', 'is_active',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'phone_number'),
        }),
    )
    ordering = ('email',)
    filter_horizontal = ()
#
#

# admin.site.register(User, CustomUserAdmin)
