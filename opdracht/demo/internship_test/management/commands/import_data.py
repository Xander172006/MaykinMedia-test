import io, os
import pandas as pd
import requests
from requests.auth import HTTPBasicAuth
from django.core.management.base import BaseCommand
from internship_test.models import City, Hotel
from dotenv import load_dotenv

load_dotenv()

"""
    Command to import cities and hotels from CSV files
    The CSV files are fetched from the given URLs and stored in the database.
    The credentials are fetched from the environment variables.
"""

class Command(BaseCommand):
    help = 'Import cities and hotels from CSV files'

    # get credentials
    def handle(self, *args, **kwargs):
        city_url = os.getenv('CITY_URL')
        hotel_url = os.getenv('HOTEL_URL')
        username = os.getenv('USERNAME')
        password = os.getenv('PASSWORD')
        
        self.import_data(city_url, username, password, 'cities')
        self.import_data(hotel_url, username, password, 'hotels')

    # import data
    def import_data(self, url, username, password, data_type):
        response = requests.get(url, auth=HTTPBasicAuth(username, password))

        # store cities in database
        if data_type == 'cities':
            df = pd.read_csv(io.StringIO(response.text), delimiter=';', header=None, names=['city_code', 'name'])
            for _, row in df.iterrows():
                City.objects.get_or_create(city_code=row['city_code'], name=row['name'])

            self.stdout.write(self.style.SUCCESS('Successfully imported cities'))

        # store hotels in database
        elif data_type == 'hotels':
            df = pd.read_csv(io.StringIO(response.text), delimiter=';', header=None, names=['city_code', 'hotel_code', 'name'])
            for _, row in df.iterrows():
                city = City.objects.get(city_code=row['city_code'])
                Hotel.objects.get_or_create(city_code=city, hotel_code=row['hotel_code'], name=row['name'])
            self.stdout.write(self.style.SUCCESS('Successfully imported hotels'))