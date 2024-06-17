from django.test import TestCase, Client
from django.urls import reverse
from .models import City, Hotel

"""
    Tests for the views	
    The tests are used to check if the views are working as expected.
"""

# Create your tests here.
class CityHotelViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.city = City.objects.create(name='Amsterdam')
        self.hotel = Hotel.objects.create(name='Hotel Amsterdam', city_code=self.city)

    def test_city_hotel_view(self):
        response = self.client.get(reverse('city_hotel_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'form.html')

    def test_city_hotel_view_post(self):
        response = self.client.post(reverse('city_hotel_view'), {'city': 'Amsterdam'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'form.html')
        self.assertEqual(response.context['selected_city'], self.city)
        self.assertEqual(list(response.context['hotels']), [self.hotel])