from django.db import models
from django.contrib.auth.models import User
import datetime as dt

# Create your models here.

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'posts/', blank = True)
    bio = models.CharField(max_length=150)
    profile_user = models.ForeignKey(User,on_delete=models.CASCADE,default = '')

    def save_profile(self):
        self.save()

    @classmethod
    def delete_profile(cls,id):
        cls.objects.filter(id = id).delete()

    @classmethod
    def update_profile(cls,id,new_photo,new_bio):
        cls.objects.filter(id = id).update(profile_photo = new_photo,bio = new_bio)
    
    def __str__(self):
        return self.bio


class Image(models.Model):
    image = models.ImageField(upload_to = 'posts/')
    image_name = models.CharField(max_length=60)
    image_caption = models.CharField(max_length=300)
    image_profile = models.ForeignKey(Profile,null = True,on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    pub_date = models.DateField(auto_now_add=True)
    comments = models.CharField(max_length=300,blank=True)

    @property
    def total_likes(self):
        return self.likes.count()

    def save_image(self):
        self.save()

    @classmethod
    def update_caption(cls,id,new_name,new_caption):
        cls.objects.filter(id = id).update(image_name = new_name,image_caption = new_caption)

    @classmethod
    def delete_image(cls,id):
        cls.objects.filter(id = id).delete()

    def __str__(self):
        return self.image_name


class Comment(models.Model):
    comment = models.CharField(max_length=200)
    post= models.ForeignKey(Image, on_delete=models.CASCADE)
    user= models.ForeignKey(Profile, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def save_comment(self):
        self.save()

    @classmethod
    def delete_comment(cls,id):
        cls.objects.filter(id = id).delete()

    @classmethod
    def update_comment(cls,id,new_comment):
        cls.objects.filter(id = id).update(comment = new_comment)

    def __str__(self):
        return  self.comment  