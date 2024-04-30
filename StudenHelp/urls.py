from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from .views import home
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),  # Utilisation de la vue logout_view
    path('register/', views.register, name='register'),
    path('choix/', views.choix, name='choix'),
    path('eventClub/', views.eventClub, name='eventClub'),
]