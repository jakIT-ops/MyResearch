from django.urls import path 
from .import views

app_name = 'apis'

urlpatterns = [
path('', views.index, name='index'), 
path('ocr/', views.ocr, name='ocr'), 
path('imageanalysis/', views.imageanalysis, name='imageanalysis'), ]