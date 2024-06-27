from django.urls import path
from . import views

"""
    URL patterns for the application
    The autocomplete URL is used to fetch the city names for the autocomplete feature.
"""

urlpatterns = [
    path('', views.city_hotel_view, name='city_hotel_view'),
    path('autocomplete/', views.autocomplete_city, name='autocomplete_city'),
]
