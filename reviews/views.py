from django.shortcuts import render, redirect
from .models import Review, ReviewImage
from .forms import ReviewForm, ReviewImageForm
from clothes.models import Cloth
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.
def review_create(request, cloth_pk):
    cloth = Cloth.objects.get(pk=cloth_pk)
    
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        review_image_form = ReviewImageForm(request.POST, request.FILES)
        files = request.FILES.getlist('image')

        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.clothes_id = cloth_pk
            review.user = request.user
            review.cloth = cloth
            review.save()

            for file in files:
                ReviewImage.objects.create(review=review, image=file)

            return redirect('clothes:detail', cloth_pk)
    else:
        review_form = ReviewForm()
        review_image_form = ReviewImageForm()
    context = {
        'review_form': review_form,
        'review_image_form': review_image_form,
        'cloth': cloth,
    }
    return render(request, 'reviews/review_create.html', context)


def review_update(request, cloth_pk, review_pk):
    review = Review.objects.get(pk=review_pk, clothes__pk=cloth_pk)
    if request.user == review.user:
        if request.method == 'POST':
            review_form = ReviewForm(request.POST, instance=review)
            files = request.FILES.getlist('image')
            if review_form.is_valid():
                review_form.save()
                review_images = ReviewImage.objects.filter(review=review)
                for review_image in review_images:
                    review_image.delete()
                for file in files:
                    ReviewImage.objects.create(review=review, image=file)
                return redirect('clothes:detail', cloth_pk=cloth_pk)
        else:
            review_form = ReviewForm(instance=review)
            review_image_form = ReviewImageForm()
        context = {
            'review_form': review_form,
            'review_image_form': review_image_form,
            'review': review,
        }
        return render(request, 'reviews/review_update.html', context)
    else:
        return redirect('clothes:detail', cloth_pk=cloth_pk)
    

def review_delete(request, cloth_pk, review_pk):
    review = Review.objects.get(pk=review_pk, clothes__pk=cloth_pk)
    review_images = review.reviewimage_set.all()
    if review.user == review.user:
        for review_image in review_images:
            review_image.delete()
        review.delete()
    return redirect('clothes:detail', cloth_pk)
