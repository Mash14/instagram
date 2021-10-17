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

    def test_search_profile(self):
        self.new_profile.save_profile()
        username = 'mash'
        searched_profiles = self.new_profile.search_profile(username)
        self.assertTrue(len(searched_profiles)>0)

class ImageTestClass(TestCase):

    def setUp(self):
        self.user = User(username = 'mash', email = 'mash@gmail.com', password = 'test')
        self.user.save()

        self.new_profile = Profile(profile_photo = 'image3.jpg', bio = 'G.O.A.T',profile_user = self.user)
        self.new_profile.save()

        self.new_image = Image(image = 'image5.jpg',image_name = 'hitman',image_caption = 'Crown the King', image_profile = self.new_profile,comments = 'test comment')
        self.new_image.save_image()

    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()
        Image.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))

    def test_save_method(self):
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_update_method(self):
        self.new_image.save_image()
        image_id = self.new_image.id
        Image.update_caption(image_id,'Crown')
        self.new_image.refresh_from_db()
        self.assertEquals(self.new_image.image_caption,'Crown')

    def test_get_image_by_id(self):
        self.new_image.save_image()
        search_image = self.new_image.get_image_by_id(self.new_image.id)
        searched_image = Image.objects.filter(id=self.new_image.id)
        self.assertTrue(searched_image,search_image)
