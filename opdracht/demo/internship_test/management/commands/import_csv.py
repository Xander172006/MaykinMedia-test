import io, os
import pandas as pd
import requests
from requests.auth import HTTPBasicAuth
from django.core.management.base import BaseCommand
from internship_test.models import City, Hotel
from dotenv import load_dotenv

load_dotenv()

class Command(BaseCommand):
    help = 'Import cities and hotels from CSV files'

    # function for authenticating urls
    def handle(self, *args, **kwargs):
        city_url = os.getenv('CITY_URL')
        hotel_url = os.getenv('HOTEL_URL')
        username = os.getenv('USERNAME')
        password = os.getenv('PASSWORD')
        self.import_cities(city_url, username, password)
        self.import_hotels(hotel_url, username, password)

    # import cities data
    def import_cities(self, url, username, password):
        response = requests.get(url, auth=HTTPBasicAuth(username, password))
        city_df = pd.read_csv(io.StringIO(response.text), delimiter=';', header=None, names=['city_code', 'name'])
        for index, row in city_df.iterrows():
            City.objects.get_or_create(city_code=row['city_code'], name=row['name'])
        self.stdout.write(self.style.SUCCESS('Successfully imported cities'))

    # import hotels data
    def import_hotels(self, url, username, password):
        response = requests.get(url, auth=HTTPBasicAuth(username, password))
        hotel_df = pd.read_csv(io.StringIO(response.text), delimiter=';', header=None, names=['city_code', 'hotel_code', 'hotel_name'])
        for index, row in hotel_df.iterrows():
            city = City.objects.get(city_code=row['city_code'])
            Hotel.objects.get_or_create(city_code=city, hotel_code=row['hotel_code'], hotel_name=row['hotel_name'])
        self.stdout.write(self.style.SUCCESS('Successfully imported hotels'))
