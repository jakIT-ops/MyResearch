from django.shortcuts import render
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
import json
import requests

TMDB_API_KEY = '{{API_KEY}}'

def index(request):
    data = requests.get(f"https://api.themoviedb.org/3/trending/all/day?api_key={TMDB_API_KEY}&language=en-US")
    
    return render(request, "movietv/index.html", {
        "data": data.json()})

def search(request):

    query = request.GET.get("query")
    print(query)

    if query:
        data = requests.get(f"https://api.themoviedb.org/3/search/{request.GET.get('type')}?api_key={TMDB_API_KEY}&language=en-US&page=1&include_adult=false&query={query}")

    else:
        data = requests.get(f"https://api.themoviedb.org/3/trending/all/day?api_key={TMDB_API_KEY}&language=en-US")
        return render(request, "movietv/index.html", {"data":data.json()})

    return render(request, 'movietv/results.html', {
        "data": data.json(),
        "type": request.GET.get("type")
    })

def movies(request):
    latest= requests.get(f"https://api.themoviedb.org/3/movie/latest?api_key={TMDB_API_KEY}&language=en-US")
    trending = requests.get(f"https://api.themoviedb.org/3/trending/movie/week?api_key={TMDB_API_KEY}&language=en-US")
    popular = requests.get(f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=en-US")
    top = requests.get(f"https://api.themoviedb.org/3/movie/top_rated?api_key={TMDB_API_KEY}&language=en-US")    
    upcoming = requests.get(f"https://api.themoviedb.org/3/movie/upcoming?api_key={TMDB_API_KEY}&language=en-US")
    now_playing = requests.get(f"https://api.themoviedb.org/3/movie/now_playing?api_key={TMDB_API_KEY}&language=en-US")

    return render(request, "movietv/movies.html", {
        "latest":latest.json(),
        "trending": trending.json(),
        "popular": popular.json(),
        "top":top.json(),
        "upcoming": upcoming.json(),
        "now": now_playing.json(),
    })

def tv(request):
    latest= requests.get(f"https://api.themoviedb.org/3/tv/latest?api_key={TMDB_API_KEY}&language=en-US")
    trending = requests.get(f"https://api.themoviedb.org/3/trending/tv/week?api_key={TMDB_API_KEY}&language=en-US")
    popular = requests.get(f"https://api.themoviedb.org/3/tv/popular?api_key={TMDB_API_KEY}&language=en-US")
    top = requests.get(f"https://api.themoviedb.org/3/tv/top_rated?api_key={TMDB_API_KEY}&language=en-US")    
    airtoday = requests.get(f"https://api.themoviedb.org/3/tv/airing_today?api_key={TMDB_API_KEY}&language=en-US")
    onair = requests.get(f"https://api.themoviedb.org/3/tv/on_the_air?api_key={TMDB_API_KEY}&language=en-US")
   
    return render(request, "movietv/tv.html", {
        "latest":latest.json(),
        "trending": trending.json(),
        "popular": popular.json(),
        "top":top.json(),
        "airtoday": airtoday.json(),
        "onair": onair.json(),
    })
    
def movie_detail(request, movie_id):
    data = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US")    
    recommendations = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key={TMDB_API_KEY}&language=en-US")
    credits = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={TMDB_API_KEY}&language=en-US")
    videos= requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={TMDB_API_KEY}&language=en-US")
    
    return render(request, "movietv/movie_detail.html", {
        "data": data.json(),
        "recommendations": recommendations.json(),
        "credits": credits.json(),
        "videos": videos.json(),
        "type": "movie",
    })

def tv_detail(request, tv_id):
    data = requests.get(f"https://api.themoviedb.org/3/tv/{tv_id}?api_key={TMDB_API_KEY}&language=en-US")    
    recommendations = requests.get(f"https://api.themoviedb.org/3/tv/{tv_id}/recommendations?api_key={TMDB_API_KEY}&language=en-US")
    credits = requests.get(f"https://api.themoviedb.org/3/tv/{tv_id}/credits?api_key={TMDB_API_KEY}&language=en-US")
    videos= requests.get(f"https://api.themoviedb.org/3/tv/{tv_id}/videos?api_key={TMDB_API_KEY}&language=en-US")
    
    return render(request, "movietv/tv_detail.html", {
        "data": data.json(),
        "recommendations": recommendations.json(),
        "credits": credits.json(),
        "videos": videos.json(),
        "type": "tv",
    })
    
def season_detail(request, tv_id, season_number):
    data = requests.get(f"https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}?api_key={TMDB_API_KEY}&language=en-US")    
   
    return render(request, "movietv/season_detail.html", {
        "data": data.json(),
        "tv_id":tv_id,
    })

def episode_detail(request, tv_id, season_number, episode_number):
    data = requests.get(f"https://api.themoviedb.org/3/tv/{tv_id}/season/{season_number}/episode/{episode_number}?api_key={TMDB_API_KEY}&language=en-US")    
   
    return render(request, "movietv/episode_detail.html", {
        "data": data.json(),
    })

def people_detail(request, person_id):
    person= requests.get(f"https://api.themoviedb.org/3/person/{person_id}?api_key={TMDB_API_KEY}&language=en-US")
    credit_details = requests.get(f"https://api.themoviedb.org/3/person/{person_id}/combined_credits?api_key={TMDB_API_KEY}")
    return render(request, "movietv/person.html", {
        "person":person.json(),
        "credit":credit_details.json()})

def people(request):
    popular= requests.get(f"https://api.themoviedb.org/3/person/popular?api_key={TMDB_API_KEY}&language=en-US")
    return render(request, "movietv/people.html", {
        "popular":popular.json()})