from django.urls import path,include
from . import views 
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),  
    path('register/', views.register, name='register'),
    path('choix/', views.choix, name='choix'),
    path('eventClub/', views.eventClub, name='eventClub'),
    path('eventSocial/', views.eventSocial, name='eventSocial'),
    path('stage/', views.stage, name='stage'),
    path('logement/', views.logement, name='logement'),
    path('transport/', views.transport, name='transport'),
    path('recommandation/', views.recommandation, name='recommandation'),
 ]