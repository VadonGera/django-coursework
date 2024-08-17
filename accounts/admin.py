from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm

    list_display = ('email', 'phone_number', 'first_name', 'last_name', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name', 'phone_number',)}),
        ('Permissions', {'fields': ('is_admin', 'is_active',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'phone_number'),
        }),
    )
    ordering = ('email',)
    filter_horizontal = ()
#
#

# admin.site.register(User, CustomUserAdmin)
