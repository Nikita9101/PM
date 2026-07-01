from django.db import models


class Guest(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="ФИО")
    birthday = models.DateField(verbose_name="Дата рождения")
    gender = models.ForeignKey('genders.Gender', on_delete=models.CASCADE, verbose_name="Пол")
    status = models.ForeignKey('statuses.Status', on_delete=models.CASCADE, verbose_name="Статус")

    def __str__(self):
        return self.full_name