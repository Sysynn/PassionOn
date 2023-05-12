from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('', views.temp, name='temp'),
    path('profile/<username>/', views.profile, name='profile'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('password/', views.change_password, name='change_password'),
    path('<username>/cart/<int:cloth_pk>/', views.add_cart, name='add_cart'),
    path('<username>/purchase/<int:cloth_pk>/', views.purchase, name='purchase'),
    
    # 아래 두 경로는 위 경로와 달리 cloth_pk가 아닌 cart_pk, purchase_pk임에 주의!!
    path('<username>/cart/<int:cart_pk>/delete/', views.delete_cart_item, name='delete_cart_item'),
    path('<username>/purchase/<int:purchase_pk>/delete/', views.delete_purchase_log, name='delete_purchase_log'),
]