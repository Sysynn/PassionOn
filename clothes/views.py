from django.shortcuts import render, redirect
from django.conf import settings
from .models import Cloth, ClothImage
from .forms import ClothForm, ClothImageForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator
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
    context = {
        'cloth': cloth,
        'cloth_images': cloth_images,
    }
    return render(request, 'clothes/detail.html', context)


def create(request):
    if request.method == 'POST':
        cloth_form = ClothForm(request.POST, request.FILES)
        cloth_image_form = ClothImageForm(request.POST, request.FILES)
        files = request.FILES.getlist('image')
        
        if cloth_form.is_valid() and cloth_image_form.is_valid():
            cloth = cloth_form.save(commit=False)
            cloth.user = request.user
            cloth.save()

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