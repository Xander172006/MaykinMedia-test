from django.db import models

# Create your models here.

class City(models.Model):
    city_code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Hotel(models.Model):
    city_code = models.ForeignKey(City, on_delete=models.CASCADE, related_name='hotels')
    hotel_code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name