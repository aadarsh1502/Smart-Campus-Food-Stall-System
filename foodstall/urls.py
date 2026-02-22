from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='foodstall/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('order/', views.place_order, name='place_order'),
    path('order-history/', views.order_history, name='order_history'),
    path('shopkeeper/orders/', views.shopkeeper_orders, name='shopkeeper_orders'),
]