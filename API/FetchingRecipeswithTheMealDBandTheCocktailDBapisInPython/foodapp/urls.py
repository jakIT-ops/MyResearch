from django.urls import path 
from .import views

urlpatterns = [
    path('', views.index, name='index'), 
    #path('yo/', views.yo, name='yo'),
    #path(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
    path('ajax/get_cocktails_list/', views.get_cocktails_list, name='get_cocktails_list'),
    path('ajax/get_meals_list/', views.get_meals_list, name='get_meals_list'),
    ]