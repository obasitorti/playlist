from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is the Homepage")

def coding_playlist(request):
    playlist_list = {
        "song_details": {
            "Love Lies": {"artist": "Normani, Khalid", "album": "Love Lies",
                              "length":"3:21"},
            "Rise": {"artist": "Jack & Jack, Jonas Blue", "album": "Blue",
                              "length":"3:14"}
            
        }
    }
    return render(request, 'first_app/coding.html', context=playlist_list)

def car_playlist(request):
    playlist_list = {
        "song_details": {
            "thank u, next": {"artist": "Ariana Grande", "album": "thank u, next",
                              "length":"3:27"},
            "One Kiss, next": {"artist": "Dua Lipa, Calvin Harris", "album": "One Kiss",
                              "length":"3:34"},
            "Better Now": {"artist": "Post Malone", "album": "beerbongs & bentleys",
                              "length":"3:51"},
            "The Middle": {"artist": "Grey, Marren Morris, ZEDD", "album": "The Middle",
                              "length":"3:04"}
            
        }
    }
    return render(request, 'first_app/car.html', context=playlist_list)

# Create your views here.
