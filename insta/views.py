from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Image,Comment,Profile
from .forms import NewPostForm,NewCommentForm,NewProfileForm
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

@login_required(login_url='/accounts/login/')
def home_page(request):
    photos = Image.objects.all()

    current_user = request.user
    userProfile = Profile.objects.filter(profile_user = current_user).first()
    image = Image.objects.filter()
    if request.method == 'POST':
        form = NewCommentForm(request.POST, request.FILES)
        if form.is_valid():
            comments = form.save(commit=False)
            image = Image.objects.filter(id=request.POST.get('post')).first()
            comments.user = userProfile
            comments.post = image
            comments.save_comment()

    else:
        form = NewCommentForm()

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
            return redirect('/')
    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {'form':form})  

@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user =  request.user 
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.image_profile = current_user
            profile.save()

    else:
        form = NewProfileForm()
    title = 'Update Profile'
    return render(request, 'update_profile.html',{'form':form,'title':title}) 

@login_required(login_url='/accounts/login/')
def profile_page(request):
    current_user =  request.user 
    userProfile = Profile.objects.filter(profile_user = current_user).first()
    photos = Image.objects.filter(image_profile = userProfile).all()

    return render(request, 'gram/profile.html',{'userProfile':userProfile,'photos':photos})

@login_required(login_url='/accounts/login/')
def single_view(request,image_id):

    images = Image.objects.get(id = image_id)

    try:
        comments = Comment.objects.filter(image_id = images.id).all()

    except ObjectDoesNotExist:
        raise Http404()

    title = 'Image'
    return render(request, 'gram/single.html', {'images':images,'comments':comments,'title':title})