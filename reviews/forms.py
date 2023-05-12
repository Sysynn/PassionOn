from django import forms
from .models import Review, ReviewImage

class ReviewForm(forms.ModelForm):
    title = forms.CharField(label='제목', widget=forms.TextInput(attrs={'class' : 'form-control',}))
    content = forms.CharField(label='내용', widget=forms.TextInput(attrs={'class' : 'form-control',}))
    
    CHOICES = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5),]
    rating = forms.ChoiceField(label='평점', widget=forms.Select(attrs={'class' : 'form-select',}), choices=CHOICES,)
    
    class Meta:
        model = Review
        fields = ('title', 'content', 'rating',)
        

class ReviewImageForm(forms.ModelForm):
    image = forms.ImageField(label='리뷰 이미지 업로드', widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'multiple': True,},), required=False,)

    class Meta:
        model = ReviewImage
        fields = ('image', )