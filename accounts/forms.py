from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label = 'ID',
        widget = forms.TextInput(
            attrs = {}
        )
    )
    password = forms.CharField(
        label = 'pwd',
        widget = forms.PasswordInput(
            attrs = {}
        )
    )


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'profile_image',)
        
        
class CustomUserChangeForm(UserChangeForm):
    password = None
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'profile_image',)
        
        
class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = get_user_model()
        fields = '__all__'