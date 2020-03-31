
from django.test import TestCase
from .models import Neighbourhood,Profile,Post,Users,Business


class NeighbourhoodTest(TestCase):

    def setUp(self):
        self.neighbourhood=Neighbourhood(name="fff",location="VV",occupants=3,pub_date="DD")


    def test_instance(self):
        self.assertTrue(isinstance(self.neighbourhood,Neighbourhood))

class ProfileTest(TestCase):

    def setUp(self):
        self.profile=Profile(bio="profile",profile_photo="profile.jpg")


    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

class PostTest(TestCase):

    def setUp(self):
        self.post=Post(image="images.png",updates="post")


    def test_instance(self):
        self.assertTrue(isinstance(self.post,Post))



class UserTest(TestCase):

    def setUp(self):
        self.user=Users(name="user",email="user@gmail.com",status="updates")


    def test_instance(self):
        self.assertTrue(isinstance(self.user,Users))


class BusinessTest(TestCase):

    def setUp(self):
        self.business=Business(name="business name",email="business@gmail.com")


    def test_instance(self):
        self.assertTrue(isinstance(self.business,Business))




# Create your tests here.
