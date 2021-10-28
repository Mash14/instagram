from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Image,Comment,Profile,Like
from .forms import SignUpForm,NewPostForm,NewCommentForm,NewProfileForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

# Create your views here.

def signUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
            user = User.objects.create_user(username = username,email = email,password = password)
        return HttpResponse('Thank you for registering with us')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration_form.html', {'form': form})

@login_required(login_url='/accounts/login/')
def home_page(request):
    photos = Image.objects.all()
    comments = Comment.objects.all()
    
    title = 'Home' 
    return render(request, 'gram/index.html',{"photos":photos,"title":title,'comments':comments})

@login_required(login_url='/accounts/login/')
def post_image(request):
    current_user = request.user
    userProfile = Profile.objects.filter(profile_user = current_user).first()

    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
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
            profile.profile_user = current_user
            profile.save()
            return redirect('profile_page')

    else:
        form = NewProfileForm()
    title = 'Update Profile'
    return render(request, 'update_profile.html',{'form':form,'title':title}) 

@login_required(login_url='/accounts/login/')
def profile_page(request):
    current_user =  request.user 
    userProfile = Profile.objects.filter(profile_user = current_user).first()
    photos = Image.objects.filter(user = current_user).all()

    return render(request, 'gram/profile.html',{'userProfile':userProfile,'photos':photos})

@login_required(login_url='/accounts/login/')
def single_view(request,id):

    images = Image.objects.get(id=id)

    try:
        comments = Comment.objects.filter(id = images.id).all()

    except ObjectDoesNotExist:
        raise Http404()

    title = 'Image'
    return render(request, 'gram/single.html', {'image':images,'comments':comments,'title':title})

@login_required(login_url='/accounts/login/')
def search_user(request):
    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get('username')
        searched_profiles = Profile.search_profile(search_term)
        message = f'{search_term}'

        return render(request, 'gram/search.html', {'message':message, 'username':searched_profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'gram/search.html',{'message':message})

@login_required(login_url='/accounts/login/')
def comment_create(request,id):
    post_comment = Comment.objects.filter(post= id)
    images = Image.objects.filter(id=id).all()
    current_user = request.user
    profile = request.GET.get("profile")
    image = get_object_or_404(Image, id=id)
    if request.method == 'POST':
        form = NewCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = image
            comment.user = profile
            comment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = NewCommentForm()

    return render(request,'gram/comment.html',{"form":form,"images":images,"comments":post_comment})

def like_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        posted = Image.objects.get(id=post_id)
        if user in posted.likes.all():
            posted.likes.remove(user)
        else:
            posted.likes.add(user)
        like, created = Like.objects.get_or_create(user=user, post_id = post_id)
        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        like.save()
    return redirect('imageIndex')