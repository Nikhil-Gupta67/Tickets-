from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('search/', views.search_flight, name='search'),

    path('book/<int:id>/', views.book_flight, name='book'),

    path('success/', views.success, name='success'),

    path('login/', views.login_user, name='login'),

    path('register/', views.register, name='register'),
    
    path('logout/', views.logout_user, name='logout'),


]