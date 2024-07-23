"""
URL configuration for DjangoCountries project.

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
from django.contrib import admin
from django.urls import path
from MainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.render_main),
    path('country-list/', views.render_country_list),
    path('country/<str:name>/', views.render_country_by_name, name='country'),
    path('countries_by_letter/<str:letter>/', views.render_countries_by_first_letter, name='letter'),
    path('countries_by_language/<str:language>/', views.render_countries_by_language, name='language'),
    path('languages/', views.render_languages, name='languages'),
]
