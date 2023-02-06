from django.contrib import admin
from django.urls import path
from . import views

# Create your tests here.
urlpatterns = [
    path('', views.index),
    path('page_md/', views.page_md, name='page_md'),
    path('<int:pk>/', views.detail, name='detail'),
]