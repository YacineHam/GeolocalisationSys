from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Location,CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'is_staff', 'is_active','is_car')
    list_filter = ('username', 'is_staff', 'is_active',"is_car")

    fieldsets = (
        (None, {'fields': ('username', 'password', 'aes_key')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_car')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_staff', 'is_active','is_car')}
        ),
    )

    search_fields = ('username',)
    ordering = ('username',)


admin.site.register(Location)
admin.site.register(CustomUser,CustomUserAdmin)