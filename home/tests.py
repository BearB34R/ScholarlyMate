from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class LoginViewTestCase(TestCase):
    def test_login_view(self):
        # Get URL for login view
        url = reverse('login')

        # GET request to login view
        response = self.client.get(url)

        # Check if the view returns a status code of 200
        self.assertEqual(response.status_code, 200)

        # Check if the correct template is used
        self.assertTemplateUsed(response, 'accounts/login.html')