"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path
from .views import index, mi_wiew, user_form, product_viev, success, total_in_db
from django.conf.urls.static import static



urlpatterns = [
    path('', index, name= 'index'),   
    path('mi_wiew/', mi_wiew, name= 'mi_wiew'),   
    path('user_form/', user_form, name= 'user_form'),   
    path('product_viev/', product_viev, name= 'product_viev'),   
    path('success/', success, name= 'success'),   
    path('total_in_db/', total_in_db, name= 'total_in_db'),   
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
