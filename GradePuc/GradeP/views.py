from django.shortcuts import render
import requests


def home (request):
    results = requests.get("https://omdbapi.com/?apikey=38b4b85b&s=Batman&type=movie")
    results_json = results.json()
    movies = results_json["Search"]
    context = {
        "movies": movies
    }    
    return render(request, "ajuda.html", context)