from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Image,Comment,Profile
from .forms import NewPostForm

# Create your views here.

@login_required(login_url='/accounts/login/')
def home(request):
    photos = Image.objects.all()

    title = 'Home' 
    return render(request, 'gram/index.html',{"photos":photos,"title":title})

@login_required(login_url='/accounts/login/')
def post_image(request):
    current_user = request.user
    userProfile = Profile.objects.filter(profile_user = current_user).first()

    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.image_profile = userProfile
            image.save()
            return redirect('/home')
    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {'form':form})        