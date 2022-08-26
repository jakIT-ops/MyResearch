from django.urls import path
from .import views


app_name = 'nasapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('events', views.events, name='events'),
    path('events/<str:id>', views.event, name='event'),
    path('asteroids', views.asteroids, name='asteroids'),
    path('mars', views.mars, name='mars')
]
