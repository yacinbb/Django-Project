from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from .views import home
urlpatterns = [
path('', views.index),
path('home/', views.home, name='home'),
path('accounts/', include('django.contrib.auth.urls')),
path('login/',auth_views.LoginView.as_view(template_name='registration/login.html'), name = 'login'),
path('logout/',auth_views.LogoutView.as_view(template_name='registration/logout.html'), name ='logout'),
path('register/',views.register, name = 'register'),
]