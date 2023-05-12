from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login, logout as auth_logout, update_session_auth_hash
from .forms import CustomAuthenticationForm, CustomUserCreationForm, CustomUserChangeForm, CustomPasswordChangeForm
from clothes.models import Cloth
from .models import Cart, PurchaseLog
from django.db.models import Count, Sum

# Create your views here.
def temp(request):
    context = {
        'persons': get_user_model().objects.all()
    }
    return render(request, 'accounts/temp.html', context)


def profile(request, username: str):
    User = get_user_model()
    person = User.objects.get(username=username)
    carts = Cart.objects.filter(user=person)
    purchases = PurchaseLog.objects.filter(user=person)
    
    context = {
        'person': person,   
        'carts': carts,
        'purchase_logs': purchases,
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


@login_required
def delete(request, user_pk: int):
    person = get_user_model().objects.get(pk=user_pk)
    if request.user == person:
        person.delete()
        auth_logout(request)
        
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


@login_required
def add_cart(request, username: str, cloth_pk: int):
    me = request.user
    cloth = Cloth.objects.get(pk=cloth_pk)
    quantity = request.POST.get('quantity')
    if quantity:
        Cart.objects.create(user=me, cloth=cloth, quantity=quantity)
    else:
        Cart.objects.create(user=me, cloth=cloth)
        
    # return redirect('clothes:detail', cloth_pk)
    return redirect('accounts:temp')


@login_required
def purchase(request, username: str, cloth_pk: int):
    me = request.user
    cloth = Cloth.objects.get(pk=cloth_pk)
    quantity = request.POST.get('quantity')
    if quantity:
        PurchaseLog.objects.create(user=me, cloth=cloth, quantity=quantity)
    else:
        PurchaseLog.objects.create(user=me, cloth=cloth)
    
    # 물건을 구매하고 결제한 후에 이동할 창 구체적인 명세 필요
    # return redirect('clothes:index')
    return redirect('accounts:temp')


@login_required
def delete_cart_item(request, username: str, cart_pk: int):
    person = get_user_model().objects.get(username=username)
    if request.user == person:
        cart = Cart.objects.get(pk=cart_pk)
        cart.delete()
        
    return redirect('accounts:profile', request.user)


@login_required
def delete_purchase_log(request, username: str, purchase_pk: int):
    person = get_user_model().objects.get(username=username)
    if request.user == person:
        purchase = PurchaseLog.objects.get(pk=purchase_pk)
        purchase.delete()
        
    return redirect('accounts:profile', request.user)