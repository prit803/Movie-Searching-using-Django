from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
from .models import Movie

# Create your views here.

def home(request):
    searchTerm=request.GET.get('searchMovie')
    movies=Movie.objects.all()
    return render(request,'home.html',{'searchTerm':searchTerm,'movies':movies})
def about(request):
    return HttpResponse('we are here at about page!')
def signup(request):
 email = request.GET.get('email')
 return render(request, 'signup.html', {'email':email})