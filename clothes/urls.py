from django.urls import path
from . import views


app_name = 'clothes'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:cloth_pk>/', views.detail, name='detail'),
    path('<int:cloth_pk>/delete/', views.delete, name='delete'),
    path('<int:cloth_pk>/update/', views.update, name='update'),
    path('search/', views.search, name='search'),
    # path('tags/<int:tag_pk>/', views.tagged_clothes, name='tagged_clothes'),
    path('<int:cloth_pk>/likes/', views.likes, name='likes'),
    path('category/<str:subject>/', views.category, name='category')
]