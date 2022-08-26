from django.shortcuts import render
from datetime import date
import requests


API_KEY = '{{API_KEY}}'

def index(request):
    url = 'https://api.nasa.gov/planetary/apod'
    headers={
       'api_key': API_KEY
    }
    response = requests.get(url, headers)
    context={
        'picture': response.json()
    }
    return render(request, 'nasapp/index.html', context)

def events(request):
    url = 'https://eonet.gsfc.nasa.gov/api/v3/categories'
    headers={
        'api_key': API_KEY
    }
    response = requests.get(url, headers)
    context={
        'all_categories': response.json()['categories'],
        'selected_categories': ['Sea and Lake Ice', 'Severe Storms', 'Drought', 'Volcanoes', 'Wildfires', 'Earthquakes']
    }
    return render(request, 'nasapp/events.html', context)

def event(request, id):
    url = 'https://eonet.gsfc.nasa.gov/api/v3/events'
    headers={
       'api_key': API_KEY,
       'category': id
    }
    response = requests.get(url, headers)
    context={
        'events': response.json()['events']
    }
    return render(request, 'nasapp/event.html', context)

def asteroids(request):
    start_date = date.today().strftime("%Y-%m-%d")
    url = 'https://api.nasa.gov/neo/rest/v1/feed'
    headers={
        'api_key': API_KEY,
        'start_date': start_date,
        'end_date': start_date
    }
    response = requests.get(url, headers)
    context={
        'asteroids': response.json()['near_earth_objects'][start_date]
    }
    return render(request, 'nasapp/asteroids.html', context)

def mars(request):
    rover = 'Spirit'
    camera = 'navcam'

    if request.method == 'POST':
        rover = request.POST.get('rover')
        camera = request.POST.get('camera')

    url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/'+rover+'/photos?'
    headers={
        'api_key': API_KEY,
        'sol': 45,
        'camera': camera
    }
    response = requests.get(url, headers)
    context={
        'photos': response.json()['photos'],
        'selected_rover': rover,
        'selected_camera': camera
    }
    return render(request, 'nasapp/mars.html', context)

