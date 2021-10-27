from django import forms
from .models import Profile,Image,Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    email = forms.EmailField

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
class NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['image_profile','pub_date','likes','comments','user'] 

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post','user','date']

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['profile_user']