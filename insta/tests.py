from django.test import TestCase
from .models import Image, Profile, Comment
from django.contrib.auth.models import User

# Create your tests here.

class ProfileTestClass(TestCase):
    
    def setUP(self):
        self.user = User(username = 'mash', email = 'mash@gmail.com', password = 'test')
        self.user.save()

         