from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login, logout as auth_logout, update_session_auth_hash
from .forms import CustomAuthenticationForm, CustomUserCreationForm, CustomUserChangeForm, CustomPasswordChangeForm

# Create your views here.
def temp(request):
    context = {
        'persons': get_user_model().objects.all()
    }
    return render(request, 'accounts/temp.html', context)


def profile(request, username: str):
    User = get_user_model()
    person = User.objects.get(username=username)
    
    context = {
        'person': person,    
    }
    return render(request, 'accounts/profile.html', context)
    
    
def login(request):
    if request.user.is_authenticated:
        # return redirect('clothes:index')
        return redirect('accounts:temp')
    
    if request.method == 'POST':
        login_form = CustomAuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            # return redirect('clothes:index')
            return redirect('accounts:temp')
    else:
        login_form = CustomAuthenticationForm()
        
    context = {
        'form': login_form,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    if request.user:
        auth_logout(request)
    # return redirect('clothes:index')
    return redirect('accounts:temp')


def signup(request):
    if request.user.is_authenticated:
        # return redirect('clothes:index')
        return redirect('accounts:temp')
        
    if request.method == 'POST':
        register_form = CustomUserCreationForm(data=request.POST, files=request.FILES)
        if register_form.is_valid():
            user = register_form.save()
            # auth_login(request, user)
            # return redirect('clothes:index')
            return redirect('accounts:temp')
    else:
        register_form = CustomUserCreationForm()
        
    context = {
        'form': register_form,
    }
    return render(request, 'accounts/signup.html', context)


def delete(request, user_pk: int):
    person = get_user_model().objects.get(pk=user_pk)
    if request.user == person:
        pass
    return redirect('accounts:temp')


@login_required
def update(request):
    me = request.user
    if request.method == 'POST':
        print(request.FILES)
        change_form = CustomUserChangeForm(instance=me, data=request.POST, files=request.FILES)
        if change_form.is_valid():
            change_form.save()
            return redirect('accounts:temp')
    else:
        change_form = CustomUserChangeForm(instance=me)
    
    context = {
        'form': change_form,
    }
    return render(request, 'accounts/update.html', context)


@login_required
def change_password(request):
    me = request.user
    if request.method == 'POST':
        change_pwd_form = CustomPasswordChangeForm(user=me, data=request.POST)
        if change_pwd_form.is_valid():
            change_pwd_form.save()
            update_session_auth_hash(request, request.user)
            return redirect('accounts:temp')
    else:
        change_pwd_form = CustomPasswordChangeForm(user=me)
        
    context = {
        'form': change_pwd_form,
    }
    return render(request, 'accounts/change_password.html', context)