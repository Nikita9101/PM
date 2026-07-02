from django.db import models

class Gender(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название пола")

    def __str__(self):
        return self.name