from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

#this function will be used to get list of cocktails for a selected category
def get_cocktails_list(request):
    category = request.GET.get('sel1')
    url = f'https://www.thecocktaildb.com/api/json/v1/1/filter.php?c={category}'
    response = requests.get(url)
    data = response.json()
    drinks=data['drinks']
    rep={
        'drinks' : drinks
    }
    return HttpResponse(json.dumps(rep))

#this function will be used to get list of meals for a selected category
def get_meals_list(request):
    category = request.GET.get('sel1')
    url = f'https://www.themealdb.com/api/json/v1/1/filter.php?c={category}'
    response = requests.get(url)
    data = response.json()
    meals=data['meals']
    rep={
        'meals' : meals
    }
    return HttpResponse(json.dumps(rep))


def index(request):
    if request.method == 'POST':
        #Getting the selected options
        selected_meal = request.POST.get('meals')
        selected_cocktail = request.POST.get('cocktails')

        #calling the endpoints and saving the responses
        url1 = f'https://www.themealdb.com/api/json/v1/1/lookup.php?i={selected_meal}'
        url2 = f'https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={selected_cocktail}'
        
        response1 = requests.get(url1)
        response2 = requests.get(url2)
        data1 = response1.json()
        data2 = response2.json()
        meals = data1['meals']
        drinks = data2['drinks']
        context = {
            'meals' : meals,
            'drinks' : drinks
        }
    else:
        context={}
    return render(request, 'foodapp/index.html', context)