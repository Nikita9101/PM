from django.db import models

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=255, verbose_name="Название отеля")

    def __str__(self):
        return self.hotel_name