from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import Cart, PurchaseLog


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
    password1 = forms.CharField(
        # label='', 
        widget=forms.PasswordInput(attrs={'class' : 'form-control'}),
        help_text=password_validation.password_validators_help_text_html(),
        )
    password2 = forms.CharField(
        # label='', 
        widget=forms.PasswordInput(attrs={'class' : 'form-control'}),
        )
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'password1', 'password2',)
        labels = {
            'username': 'ID',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
        
class CustomUserChangeForm(UserChangeForm):
    password = None
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'profile_image',)
        labels = {
            'first_name': '이름',
            'last_name': '성',
            'email': '이메일',
            'profile_image': '프로필 사진',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_image': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }
        
        
class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        # label='', 
        widget=forms.PasswordInput(attrs={'class' : 'form-control'}),
        )
    new_password1 = forms.CharField(
        # label='', 
        widget=forms.PasswordInput(attrs={'class' : 'form-control'}),
        help_text=password_validation.password_validators_help_text_html(),
        )
    new_password2 = forms.CharField(
        # label='', 
        widget=forms.PasswordInput(attrs={'class' : 'form-control'}),
        )
    
    class Meta:
        model = get_user_model()
        fields = '__all__'