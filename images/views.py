from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Image
from decouple import config,Csv

# Create your views here.

def images(request):

    images=Image.objects.all()
    # ALLOWED_HOSTS = config('ALLOWED_HOSTS')

    return render(request,'images.html',{"images":images})

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_categories(search_term)
        message = f"{search_term}"  

        return render(request,'search.html', {"message":message,"images":searched_images}) 

    else:
        message = "You havent searched for any term"
        return render(request,'search.html',{"message":message})     
    

def single_image(request,image_id):
    try:
        image = Image.objects.get(id=image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,'single_image.html',{"image":image})