from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login, logout as auth_logout, update_session_auth_hash
from .forms import CustomAuthenticationForm, CustomUserCreationForm, CustomUserChangeForm, CustomPasswordChangeForm
from clothes.models import Cloth
from .models import Cart, PurchaseLog
from django.db.models import Count, Sum

# Create your views here.
# def temp(request):
#     context = {
#         'persons': get_user_model().objects.all()
#     }
#     return render(request, 'accounts/temp.html', context)


def profile(request, username: str):
    User = get_user_model()
    person = User.objects.get(username=username)
    carts = Cart.objects.filter(user=person)
    purchases = PurchaseLog.objects.filter(user=person)
    
    change_form = CustomUserChangeForm()
    if request.user == person:
        change_form = CustomUserChangeForm(instance=request.user)

    context = {
        'person': person,   
        'carts': carts,
        'purchase_logs': purchases,
        'form' : change_form,
    }
    return render(request, 'accounts/profile.html', context)
    
    
def login(request):
    if request.user.is_authenticated:
        return redirect('clothes:index')
    
    if request.method == 'POST':
        login_form = CustomAuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            
            prev_url = request.session.get('prev_url')
            # 이전 페이지의 URL 정보가 있으면 해당 URL로 리다이렉트합니다.
            if prev_url:
                # 이전 페이지의 URL 정보를 삭제합니다.
                del request.session['prev_url']
                return redirect(prev_url)
            
            return redirect('clothes:index')
    else:
        login_form = CustomAuthenticationForm()
    
    request.session['prev_url'] = request.META.get('HTTP_REFERER')
    
    context = {
        'form': login_form,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    if request.user:
        auth_logout(request)
        
        request.session['prev_url'] = request.META.get('HTTP_REFERER')
        
        prev_url = request.session.get('prev_url')
        # 이전 페이지의 URL 정보가 있으면 해당 URL로 리다이렉트합니다.
        if prev_url:
            # 이전 페이지의 URL 정보를 삭제합니다.
            del request.session['prev_url']
            return redirect(prev_url)
    
    return redirect('clothes:index')


def signup(request):
    if request.user.is_authenticated:
        return redirect('clothes:index')
        
    if request.method == 'POST':
        register_form = CustomUserCreationForm(data=request.POST, files=request.FILES)
        if register_form.is_valid():
            user = register_form.save()
            auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            
            prev_url = request.session.get('prev_url')
            # 이전 페이지의 URL 정보가 있으면 해당 URL로 리다이렉트합니다.
            if prev_url:
                # 이전 페이지의 URL 정보를 삭제합니다.
                del request.session['prev_url']
                return redirect(prev_url)
            
            return redirect('clothes:index')
    else:
        register_form = CustomUserCreationForm()
    
    request.session['prev_url'] = request.META.get('HTTP_REFERER')
    
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
        
    return redirect('clothes:index')


@login_required
def update(request):
    me = request.user
    if request.method == 'POST':
        print(request.FILES)
        change_form = CustomUserChangeForm(instance=me, data=request.POST, files=request.FILES)
        if change_form.is_valid():
            change_form.save()
            return redirect('accounts:profile', request.user)
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
            return redirect('accounts:profile', request.user)
    else:
        change_pwd_form = CustomPasswordChangeForm(user=me)
        
    context = {
        'form': change_pwd_form,
    }
    return render(request, 'accounts/change_password.html', context)


@login_required
def add_cart(request, cloth_pk: int):
    me = request.user
    cloth = Cloth.objects.get(pk=cloth_pk)
    cloth_quantity = request.POST.get('quantity')
    # cloth_size = request.POST.get('size')
    if cloth_quantity:
        Cart.objects.create(user=me, cloth=cloth, quantity=cloth_quantity)
        # Cart.objects.create(user=me, cloth=cloth, quantity=cloth_quantity, size=cloth_size)
    else:
        Cart.objects.create(user=me, cloth=cloth)
    
    return redirect('accounts:profile', request.user)


@login_required
def purchase(request, cloth_pk: int):
    me = request.user
    cloth = Cloth.objects.get(pk=cloth_pk)
    cloth_quantity = request.POST.get('quantity')
    # cloth_size = request.POST.get('size')
    if cloth_quantity:
        PurchaseLog.objects.create(user=me, cloth=cloth, quantity=cloth_quantity)
        # PurchaseLog.objects.create(user=me, cloth=cloth, quantity=cloth_quantity, size=cloth_size)
    else:
        PurchaseLog.objects.create(user=me, cloth=cloth)
    
    return redirect('clothes:index')


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