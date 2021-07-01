from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Location,CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.utils.translation import ugettext_lazy


class CustomUserAdmin(UserAdmin):
    
    admin.site.site_header = 'Geolocalisation System'
    admin.site.index_title = "Geolocalisation System"
    admin.site.site_title = "Geolocalisation System"
    admin.site.site_url = "/"
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
    

    
    #def login(self, request, extra_context=None):
    #    """
    #    Displays the login form for the given HttpRequest.
    #    """
    #    from django.contrib.auth.views import login
    #    context = {
    #        'title': _('Log in'),
    #        'app_path': request.get_full_path(),
    #        REDIRECT_FIELD_NAME: settings.ADMIN_LOGIN_REDIRECT_URL,
    #    }
    #    context.update(extra_context or {})
#
    #    defaults = {
    #        'extra_context': context,
    #        'current_app': self.name,
    #        'authentication_form': self.login_form or AdminAuthenticationForm,
    #        'template_name': self.login_template or 'admin/login.html',
    #    }
    #    return login(request, **defaults) 
    



admin.site.register(Location)
admin.site.register(CustomUser,CustomUserAdmin)