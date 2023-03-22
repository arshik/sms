
from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
    path("admin/", admin.site.urls), #admin url
    path("", views.frontend, name='frontend'), 
    path("backend/", views.backend, name='backend'), 
    # Login / Logout
    path("login/", include('django.contrib.auth.urls')), 
]
