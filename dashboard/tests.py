from django.test import TestCase
from django.urls import reverse

class CalendarViewTestCase(TestCase):
    def test_calendar_view(self):
        # Get URL for calendar view
        url = reverse('calendar')

        # GET request to calendar view
        response = self.client.get(url)

        # Check if the view returns a status code of 200
        self.assertEqual(response.status_code, 200)

        # Check if the correct template is used
        self.assertTemplateUsed(response, 'pages/calendar.html')

class IndexViewTestCase(TestCase):
    def test_index_view(self):
        # Send GET request to URL mapped to index view
        response = self.client.get(reverse('home'))

        # Verify status code is 200
        self.assertEqual(response.status_code, 200)

        # Assert correct template
        self.assertTemplateUsed(response, 'pages/index.html')