from django.db import models

# Create your models here.

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'posts/', blank = True)
    bio = models.CharField(max_length=150)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def update_profile(cls,id,new_photo,new_bio):
        cls.objects.filter(id = id).update(profile_photo = new_photo,bio = new_bio)
    
    def __str__(self):
        return self.bio