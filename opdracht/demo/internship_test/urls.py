from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.city_hotel_view, name='city_hotel_view'),
    path('autocomplete/', views.autocomplete_city, name='autocomplete_city'),
]
