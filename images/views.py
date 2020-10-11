from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt
import .models import Image
from decouple import config,Csv

# Create your views here.
# def images(request):

def images(request):
    images = Image.objects.all()
    ALLOWED_HOSTS = config('ALLOWED_HOSTS')

    return render(request,'images.html',{"images":images, "ALLOWED_HOSTS":})

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_item = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"  

        return render(request,'search.html', {"message":message,"images":searched_images}) 

    else:
        message = "You havent searched for any term"
        return render(request,'search.html',{"message":message})     
    

