from django.http import JsonResponse
from django.shortcuts import render
import requests
import re

API_KEY = '{{API_KEY}}'

def getCurrentConditions(locationKey):
    url = 'http://dataservice.accuweather.com/currentconditions/v1/' + str(locationKey) + '?apikey=' + API_KEY + '&details=true'

    response = requests.get(url)

    currentConditions = dict()
    currentConditions['status'] = False

    if response.status_code == 200:
        data = response.json()[0]

        currentConditions['status'] = True
        currentConditions['currentTemperature'] = data['ApparentTemperature']['Imperial']['Value']
        currentConditions['weatherIcon'] = 'https://developer.accuweather.com/sites/default/files/' + str(data['WeatherIcon']).zfill(2) + '-s.png'
        currentConditions['weatherText'] = str(data['WeatherText'])
        currentConditions['wind'] = str(data['Wind']['Speed']['Imperial']['Value']) + ' ' + str(data['Wind']['Speed']['Imperial']['Unit']) + '-' + str(data['Wind']['Direction']['Degrees']) + ' ' + str(data['Wind']['Direction']['English'])
        currentConditions['cloudCover'] = str(data['CloudCover'])
        currentConditions['dewPoint'] = str(data['DewPoint']['Imperial']['Value'])
        currentConditions['humidity'] = str(data['RelativeHumidity'])
        currentConditions['uvIndex'] = str(data['UVIndex']) + ' - ' + str(data['UVIndexText'])
        currentConditions['realTemperature'] = str(data['RealFeelTemperature']['Imperial']['Value'])
        currentConditions['precipitation'] = str(data['HasPrecipitation'])

    else:
        currentConditions['message'] = f'{response.status_code}: {response.reason}'
    
    return currentConditions


def getHourlyForecasts(locationKey):
    url = 'http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/' + str(locationKey) + '?apikey=' + API_KEY + '&details=true'

    hourlyForecasts = dict()
    hourlyForecasts['status'] = False
    hourlyForecastsData = []

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        hourlyForecasts['status'] = True

        for i in data:
            hour = dict()
            
            hour['status'] = True
            hour['date'] = str(i['DateTime']).split('T')[0]
            hour['time'] = str(i['DateTime']).split('T')[1].split('+')[0]
            hour['weather'] = str(i['Temperature']['Value']) + '\N{DEGREE SIGN} F - ' + str(i['IconPhrase'])
            hour['rainProbability'] = str(i['RainProbability'])
            hour['weatherIcon'] = 'https://developer.accuweather.com/sites/default/files/' + str(i['WeatherIcon']).zfill(2) + '-s.png'
            
            hourlyForecastsData.append(hour)
        
        hourlyForecasts['data'] = hourlyForecastsData

    else:
        hourlyForecasts['message'] = f'{response.status_code}: {response.reason}'
    
    return hourlyForecasts


def getDailyForecasts(locationKey):
    url = 'http://dataservice.accuweather.com/forecasts/v1/daily/5day/' + str(locationKey) + '?apikey=' + API_KEY + '&details=true'

    dailyForecasts = dict()
    dailyForecasts['status'] = False
    dailyForecastsData = []

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        dailyForecasts['status'] = True

        for i in data['DailyForecasts']:
            day = dict()
            
            day['status'] = True
            day['date'] = str(i['Date']).split('T')[0]
            day['time'] = str(i['Date']).split('T')[1].split('+')[0]
            day['weather'] =   str(i['Temperature']['Maximum']['Value']) + '\N{DEGREE SIGN} F / ' + str(i['Temperature']['Minimum']['Value']) + '\N{DEGREE SIGN} F - ' + str(i['Day']['ShortPhrase'])
            day['rainProbability'] = str(i['Day']['RainProbability'])
            day['weatherIcon'] = 'https://developer.accuweather.com/sites/default/files/' + str(i['Day']['Icon']).zfill(2) + '-s.png'
            
            dailyForecastsData.append(day)
        
        dailyForecasts['data'] = dailyForecastsData

    else:
        dailyForecasts['message'] = f'{response.status_code}: {response.reason}'

    return dailyForecasts


def getLocationKey(location):
    locationData = dict()
    locationData['status'] = False

    if not re.match(r"[^\s,]+(?:\s*[^\s]+)*,\s[^\s,]+(?:\s*[^\s]+)*$", location):
        locationData['message'] = 'Invalid input format!'
        return locationData
    
    input = location.split()
    city = input[0][:-1]
    country = input[1].lstrip()

    url = 'http://dataservice.accuweather.com/locations/v1/cities/autocomplete?apikey=' + API_KEY + '&q=' + city
    
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        for i in data:
            if city.lower() == i['LocalizedName'].lower() and country.lower() == i['Country']['LocalizedName'].lower():
                locationData['location'] = i['LocalizedName'] + ', ' + i['Country']['LocalizedName']
                locationData['data'] = i['Key']
                locationData['status'] = True
        
        if locationData['status'] is False:
            locationData['message'] = 'Incorrect location entered!'

    else:
        locationData['message'] = f'{response.status_code}: {response.reason}'

    return locationData


def index(request):
    if 'term' in request.GET:
        url = 'http://dataservice.accuweather.com/locations/v1/cities/autocomplete' + '?apikey=' + API_KEY + '&q=' + request.GET.get('term')

        response = requests.get(url)
            
        locations = list()

        if response.status_code == 200:
            data = response.json()
            for i in data:
                locations.append(i['LocalizedName'] + ', ' + i['Country']['LocalizedName'])
        else:
            locations.append('No suggestions available!')

        return JsonResponse(locations, safe=False)
    
    elif request.method == 'POST':
        location = request.POST.get("location")
        locationKey = ''
        locationData = getLocationKey(location)
        status = False

        if locationData['status']:
            status = True
            location = locationData['location']
            locationKey = locationData['data']
            currentConditions = getCurrentConditions(locationKey)
            hourlyForecasts = getHourlyForecasts(locationKey)
            dailyForecasts = getDailyForecasts(locationKey)
            return render(request,'weatherapp/index.html', {'status': status, 'location': location, 'currentConditions': currentConditions, 'hourlyForecasts': hourlyForecasts, 'dailyForecasts': dailyForecasts})
        else:
            message = locationData['message']
            return render(request,'weatherapp/index.html', {'status': status, 'message': message})

    return render(request, 'weatherapp/index.html')
