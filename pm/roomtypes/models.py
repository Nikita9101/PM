from django.db import models

class RoomType(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название типа")

    def __str__(self):
        return self.name