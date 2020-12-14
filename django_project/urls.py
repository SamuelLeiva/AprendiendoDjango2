"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views #views para logout y login
from django.urls import path, include
#objetos para trabajar con static files segun docs de django
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views #importamos las views de users de django

urlpatterns = [
    path('admin/', admin.site.urls), #ruta /admin
    path('register/', user_views.register, name='register'),#mapeo haci registrar usuario
    path('profile/', user_views.profile, name='profile'), #ruta de userprofile
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),#mapeo haci registrar usuario
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/', 
    auth_views.PasswordResetView.as_view(#3 rutas para el reinicio de contrase;as
        template_name='users/password_reset.html'
        ), 
        name='password_reset'),
    path('password-reset/done/', 
    auth_views.PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'
        ), 
        name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', #parametros que django pide obligatoriamente ( id del usuario encriptado en base 64/token que chequea si el password es valido )
    auth_views.PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html'
        ), 
        name='password_reset_confirm'),
    path('password-reset-complete/', #parametros que django pide obligatoriamente ( id del usuario encriptado en base 64/token que chequea si el password es valido )
    auth_views.PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'
        ), 
        name='password_reset_complete'),
    path('', include('blog.urls')), #mapeo hacia las urls de blog ruta /blog
]

#si estamos en DEBUG mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
