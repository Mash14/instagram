from django.test import TestCase
from .models import Image, Profile, Comment
from django.contrib.auth.models import User

# Create your tests here.

class ProfileTestClass(TestCase):
    
    def setUp(self):
        self.user = User(username = 'mash', email = 'mash@gmail.com', password = 'test')
        self.user.save()

        self.new_profile = Profile(profile_photo = 'image3.jpg', bio = 'G.O.A.T',profile_user = self.user)
        self.new_profile.save()

    def tearDown(self):
        Profile.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))

    def test_save_method(self):
        self.new_profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)>0)

    def test_delete_method(self):
        self.new_profile.save_profile()
        self.new_profile.delete_profile(id = self.new_profile.id)
        profile = Profile.objects.all()
        self.assertTrue(len(profile) == 0)

    def test_update_method(self):
        self.new_profile.save_profile()
        profile_id = self.new_profile.id
        Profile.update_profile(profile_id,'CR7')
        self.new_profile.refresh_from_db()
        self.assertEquals(self.new_profile.bio,'CR7')

class ImageTestClass(TestCase):

    def setUp(self):
        self.user = User(username = 'mash', email = 'mash@gmail.com', password = 'test')
        self.user.save()

        
        
