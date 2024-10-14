from .models import AppUser
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

class AppUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = AppUser
        fields = ('username', 'email')
        
class AppUserChangeForm(UserChangeForm):
    class Meta:
        model = AppUser
        fields = ('username', 'email')