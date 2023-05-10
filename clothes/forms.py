from django import forms
from .models import Cloth, ClothImage
from taggit.managers import TaggableManager
from taggit.forms import TagField, TagWidget

class ClothForm(forms.ModelForm):
    brand = forms.CharField(label='브랜드', widget=forms.TextInput(attrs={'class': 'form-control',}))
    name = forms.CharField(label='상품명', widget=forms.TextInput(attrs={'class': 'form-control',}))
    gender = forms.ChoiceField(label='성별', widget=forms.Select(attrs={'class': 'form-select',}))
    category = forms.ChoiceField(label='분류', widget=forms.Select(attrs={'class': 'form-select',}))
    size = forms.ChoiceField(label='사이즈', widget=forms.Select(attrs={'class': 'form-select',}))
    price = forms.IntegerField(label='가격', widget=forms.NumberInput(attrs={'class': 'form-control',}))
    tags = forms.CharField(label='태그', widget=TagWidget(attrs={'class': 'form-control',}))
    thumbnail = forms.ImageField(label='썸네일 이미지', widget=forms.ClearableFileInput , attrs={'class': 'form-control'}),

    class Meta:
        model = Cloth
        fields = ('brand', 'name', 'gender', 'category', 'size', 'price', 'tags', 'thumbnail',)


class ClothImageForm(forms.ModelForm):
    image = forms.ImageField(label='상품 이미지 업로드', widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'multiple': True,},), required=False,)

    class Meta:
        model = ClothImage
        fields = ('image', )