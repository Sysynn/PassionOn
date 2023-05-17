from django import forms
from .models import Cloth, ClothImage, Recommend, RecommendImage, Comment, ClothDescriptionImage
from taggit.managers import TaggableManager
from taggit.forms import TagField, TagWidget

class ClothForm(forms.ModelForm):
    brand = forms.CharField(label='브랜드', widget=forms.TextInput(attrs={'class': 'form-control',}))
    name = forms.CharField(label='상품명', widget=forms.TextInput(attrs={'class': 'form-control',}))
    gender = forms.ChoiceField(label='성별', choices=Cloth.gender_choices, widget=forms.Select(attrs={'class': 'form-select',}))
    # category = forms.ChoiceField(label='분류', widget=forms.Select(attrs={'class': 'form-select',}))
    category = forms.ChoiceField(label='분류', choices=Cloth.category_choices, widget=forms.Select(attrs={'class': 'form-select'}),)
    size = forms.ChoiceField(label='사이즈', choices=Cloth.size_choices, widget=forms.Select(attrs={'class': 'form-select',}))
    price = forms.IntegerField(label='가격', widget=forms.NumberInput(attrs={'class': 'form-control',}))
    tags = forms.CharField(label='태그', widget=TagWidget(attrs={'class': 'form-control',}))
    thumbnail = forms.ImageField(label='썸네일 이미지', widget=forms.ClearableFileInput(attrs={'class': 'form-control'})),

    class Meta:
        model = Cloth
        fields = ('brand', 'name', 'gender', 'category', 'size', 'price', 'tags', 'thumbnail',)


class ClothImageForm(forms.ModelForm):
    image = forms.ImageField(label='상품 이미지 업로드', widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'multiple': True,},), required=False,)

    class Meta:
        model = ClothImage
        fields = ('image', )


class RecommendForm(forms.ModelForm):
    title = forms.CharField(
        label='코디명',
        widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 700px'}),
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'width: 700px; height: 200px'}),
    )
    tags = forms.CharField(
        label='코디 태그',
        widget=TagWidget(attrs={'class': 'form-control', 'style': 'width: 700px'}),
    )
    clothes = forms.ModelMultipleChoiceField(
        queryset=Cloth.objects.all(),
        label='상품 정보',
        widget=forms.CheckboxSelectMultiple(),
    )

    class Meta:
        model = Recommend
        fields = ('title', 'content', 'tags', 'clothes',)


class RecommendImageForm(forms.ModelForm):
    image = forms.ImageField(
        label='스타일 이미지 업로드',
        widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'style': 'width: 700px;'}),
        required=False,
    )
    
    class Meta:
        model = RecommendImage
        fields = ('image',)


class ClothDescriptionImageForm(forms.ModelForm):
    description_image = forms.ImageField(label='상품 설명 이미지 업로드', widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'multiple': True,},), required=False,)

    class Meta:
        model = ClothDescriptionImage
        fields = ('description_image', )
        

class CommentForm(forms.ModelForm):
    content = forms.CharField(label='댓글', widget=forms.TextInput(attrs={'class': 'form-control',}))

    class Meta:
        model = Comment
        fields = ('content',)
