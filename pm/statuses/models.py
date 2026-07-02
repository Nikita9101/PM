from django.db import models

class Status(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название статуса")

    def __str__(self):
        return self.name