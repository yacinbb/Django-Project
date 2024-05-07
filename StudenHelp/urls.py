from django.urls import path,include
from . import views 
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

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
    path('evenemnt/', views.evenemnt, name='evenmnt'),
    path('post/' , views.post , name='post')
 ] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)