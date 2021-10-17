from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Image,Comment,Profile

# Create your views here.

@login_required(login_url='/accounts/login/')
def home(request):
    photos = Image.objects.all()

    title = 'Home' 
    return render(request, 'gram/index.html',{"photos":photos,"title":title})
