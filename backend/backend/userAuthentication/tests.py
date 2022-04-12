from django.test import TestCase

from backend.backend import userAuthentication
from backend.backend.userAuthentication.models import UserProfile

# Create your tests here.

class UserTestCase(TestCase):
    def setUp(self):
        self.user = UserProfile.objects.create(
            email = "imanol@gmail.com",
            name = "imanol",
            password = "imanol"
            )
            
        
    def test_user_creation(self):
        self.assertEqual(self.user.is_active, True)
        self.assertEqual(self.user.is_staff, False)