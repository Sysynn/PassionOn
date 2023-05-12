from django.urls import path
from . import views


app_name = 'reviews'
urlpatterns = [
    path('cloth/<int:cloth_pk>/review/create/', views.review_create, name='review_create'), 
    path('cloth/<int:cloth_pk>/review/<int:review_pk>/update/', views.review_update, name='review_update'),
    path('cloth/<int:cloth_pk>/review/<int:review_pk>/delete/', views.review_delete, name='review_delete'),
]