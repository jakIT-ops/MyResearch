from django.shortcuts import render
import ticketmaster.my_formatter
import requests


api_key = '{{API_KEY}}'
discovery_url = 'https://app.ticketmaster.com/discovery/v2/'
inventory_url = 'https://app.ticketmaster.com/inventory-status/v1/availability/'


def home(request):
    data = requests.get(discovery_url + 'suggest', params = {
        'apikey'    : api_key,
        'resource'  : ['events','attractions','venues'],
        'size'      : 3
    }).json()

    events = data['_embedded']['events']
    attractions = data['_embedded']['attractions']
    venues = data['_embedded']['venues']

    # formatting the data to be rendered to the page
    formatted_data = ticketmaster.my_formatter.format_home(events, attractions, venues)

    return render(request, 'ticketmaster/home.html', formatted_data)


def events(request):
    data = requests.get(discovery_url + 'events', params = {
        'apikey' : api_key
    }).json()
    
    events = data['_embedded']['events']

    # formatting the data to be rendered to the page
    events = ticketmaster.my_formatter.format_events(events)

    return render(request, 'ticketmaster/events.html', {
        'events' : events
    })


def attractions(request):
    data = requests.get(discovery_url + 'attractions', params = {
        'apikey' : api_key
    }).json()
    
    attractions = data['_embedded']['attractions']

    # formatting the data to be rendered to the page
    attractions = ticketmaster.my_formatter.format_attractions(attractions)

    return render(request, 'ticketmaster/attractions.html', {
        'attractions' : attractions
    })


def venues(request):
    data = requests.get(discovery_url + 'venues', params = {
        'apikey' : api_key
    }).json()
    
    venues = data['_embedded']['venues']

    # formatting the data to be rendered to the page
    venues = ticketmaster.my_formatter.format_venues(venues)

    return render(request, 'ticketmaster/venues.html', {
        'venues' : venues
    })


def search(request):
    keyword = request.GET.get('keyword')
    type = request.GET.get('type')
    is_empty = False

    data = requests.get(discovery_url + type, params = {
        'apikey'  : api_key,
        'keyword' : keyword
    }).json()
    
    # if no results were returned, we set is_empty to true
    if data['page']['totalElements'] == 0:
        is_empty = True
    # otherwise, we format the data to be rendered
    else:
        data = ticketmaster.my_formatter.format_searches(data['_embedded'][type])

    return render(request, 'ticketmaster/results.html', {
        'results'     : data,
        'search_term' : keyword,
        'type'        : type,
        'empty'       : is_empty
    })


def event_detail(request, event_id):
    data = requests.get(discovery_url + 'events/' + event_id, params = {
        'apikey' : api_key
    }).json()
    
    inventory = requests.get(inventory_url, params = {
        'apikey' : api_key,
        'events' : [event_id]
    }).json()

    attractions = data['_embedded']['attractions']
    venues = data['_embedded']['venues']
    inventory = inventory[0]['status']

    # formatting the data to be rendered to the page
    formatted_data = ticketmaster.my_formatter.format_event_detail(data, attractions, venues)
    formatted_data['inventory'] = inventory

    return render(request, 'ticketmaster/event_detail.html', formatted_data)


def attraction_detail(request, attraction_id):
    data = requests.get(discovery_url + 'attractions/' + attraction_id, params = {
        'apikey' : api_key
    }).json()

    # formatting the data to be rendered to the page
    data = ticketmaster.my_formatter.format_attraction_detail(data)

    return render(request, 'ticketmaster/attraction_detail.html', {
        'details' : data
    })


def venue_detail(request, venue_id):
    data = requests.get(discovery_url + 'venues/' + venue_id, params = {
        'apikey' : api_key
    }).json()

    # formatting the data to be rendered to the page
    data = ticketmaster.my_formatter.format_venue_detail(data)
    
    return render(request, 'ticketmaster/venue_detail.html', {
        'details' : data
    })