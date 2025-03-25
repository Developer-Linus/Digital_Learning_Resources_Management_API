from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Fields to be displayed in list view
    list_display = ['email', 'is_staff', 'is_active']
    # Fields for filtering
    list_filter = ['is_staff', 'is_active']
    # Fields for detail view- showing details of single user
    fieldsets = (
        # First fieldset contains email and password
        (None, {'fields': ('email', 'password')}),
        # Second fieldset contains permissions
        ('Permissions', ({'fields': ('is_staff', 'is_active')}))
    )
    
    # Fields to be displayed in add form
    add_fieldsets = (
        (None, {
            'classes': ('wide', ), # Make form fields wide
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )
    # Fields for searching users
    search_fields = ['email']
    # Fields for ordering users
    ordering = ['email']
# Register custom user in the admin interface
admin.site.register(CustomUser, CustomUserAdmin)
    
