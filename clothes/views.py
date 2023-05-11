from django.shortcuts import render, redirect
from django.conf import settings
from .models import Cloth, ClothImage
from .forms import ClothForm, ClothImageForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.db.models import Q
from taggit.models import Tag

# Create your views here.
def index(request):
    clothes = Cloth.objects.all()
    context = {
        'clothes': clothes,
    }
    return render(request, 'clothes/index.html', context)


def detail(request, cloth_pk):
    cloth = Cloth.objects.get(pk=cloth_pk)
    cloth_images = ClothImage.objects.filter(cloth=cloth)

    tags = cloth.tags.all()

    session_key = 'cloth_{}_hits'.format(cloth_pk)
    if not request.session.get(session_key):
        cloth.hits += 1
        cloth.save()
        request.session[session_key] = True

    context = {
        'cloth': cloth,
        'cloth_images': cloth_images,
        'tags': tags,
    }
    return render(request, 'clothes/detail.html', context)


def create(request):
    if request.method == 'POST':
        cloth_form = ClothForm(request.POST, request.FILES)
        cloth_image_form = ClothImageForm(request.POST, request.FILES)
        files = request.FILES.getlist('image')
        tags = request.POST.get('tags').split(',')
        
        if cloth_form.is_valid() and cloth_image_form.is_valid():
            cloth = cloth_form.save(commit=False)
            cloth.user = request.user
            cloth.save()

            for tag in tags:
                cloth.tags.add(tag.strip())

            for file in files:
                ClothImage.objects.create(cloth=cloth, image=file)

            return redirect('clothes:detail', cloth.pk)
    else:
        cloth_form = ClothForm()
        cloth_image_form = ClothImageForm()
    context = {
        'cloth_form': cloth_form,
        'cloth_image_form': cloth_image_form,
    }
    return render(request, 'clothes/create.html', context)


def update(request, cloth_pk):
    cloth = Cloth.objects.get(pk=cloth_pk)
    cloth_image = ClothImage.objects.filter(cloth=cloth)
    if request.method == 'POST':
        cloth_form = ClothForm(request.POST, request.FILES, instance=cloth)
        cloth_image_form = ClothImageForm(request.POST, request.FILES)
        files = request.FILES.getlist('image')
        if cloth_form.is_valid() and cloth_image_form.is_valid():
            cloth = cloth_form.save(commit=False)
            cloth.user = request.user
            cloth.save()
            cloth.tags.clear()
            tags = request.POST.get('tags').split(',')

            for tag in tags:
                cloth.tags.add(tag.strip())

            for file in files:
                ClothImage.objects.create(cloth=cloth, image=file)
            
            return redirect('clothes:detail', cloth.pk)
    else:
        cloth_form = ClothForm(instance=cloth)
        cloth_image_form = ClothImageForm()
    context = {
        'cloth_form': cloth_form,
        'cloth_image_form': cloth_image_form,
        'cloth': cloth,
    }
    return render(request, 'clothes/update.html', context)


def delete(request, cloth_pk):
    cloth = Cloth.objects.get(pk=cloth_pk)
    cloth_images = cloth.clothimage_set.all()
    for cloth_image in cloth_images:
        cloth_image.delete()
    cloth.delete()
    return redirect('clothes:index')


def search(request):
    query = None
    search_list = None

    if 'q' in request.GET:
        query = request.GET.get('q')
        search_list = Cloth.objects.filter(
            Q(brand__icontains=query) | Q(name__icontains=query)
        ).distinct()
    context = {
        'query': query,
        'search_list': search_list,
    }
    return render(request, 'clothes/index.html', context)


# 일단은 보류(tag에 따라 분류할 것인가?)
# def tagged_clothes(request, tag_pk):
#     tag = Tag.objects.get(pk=tag_pk)
#     clothes = Cloth.objects.filter(tags=tag)
#     context = {
#         'tag': tag,
#         'clothes': clothes,
#     }
#     return render(request, 'clothes/tagged.html', context)


def likes(request, cloth_pk):
    cloth = Cloth.objects.get(pk=cloth_pk)
    if request.user in cloth.like_users.all():
        cloth.like_users.remove(request.user)
        is_liked = False
    else:
        cloth.like_users.add(request.user)
        is_liked = True
    context = {
        'is_liked': is_liked,
        'likes_count': cloth.like_users.count(),
    }
    return JsonResponse(context)


def category(request, subject):
    clothes = Cloth.objects.filter(category=subject)
    context = {
        'clothes': clothes,
        'category_subject': subject,
    }
    return render(request, 'clothes/category.html', context)