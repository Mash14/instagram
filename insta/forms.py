from django import forms
from .models import Profile,Image,Comment

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['image_profile','pub_date','likes','comments'] 

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post','user','date']