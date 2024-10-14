from django.contrib import admin
from .models import AppUser
from django.contrib.auth.admin import UserAdmin
from .forms import AppUserChangeForm, AppUserCreationForm

class CustomUserAdmin(UserAdmin):
    
    add_form = AppUserCreationForm
    form = AppUserChangeForm
    model = AppUser
    
    list_display = ('username', 'email', 'is_staff')
    

admin.site.register(AppUser, CustomUserAdmin)
