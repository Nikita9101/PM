from django.db import models
from django.urls import reverse_lazy


class Guest(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="ФИО")
    birthday = models.DateField(verbose_name="Дата рождения")

    gender = models.ForeignKey('genders.Gender', on_delete=models.CASCADE, verbose_name="Пол")
    status = models.ForeignKey('statuses.Status', on_delete=models.CASCADE, verbose_name="Статус")

    def __str__(self):
        return self.full_name

    def get_stay_count(self):
        """
        Считает, сколько раз гость останавливался в отеле (аналог цикла из методички)
        """

        records = self.history_set.all()
        count = 0
        for record in records:
            count += 1
        return count

    def get_update_url(self):
        return reverse_lazy("quest-update", kwargs={"pk": self.pk})

    def get_history_url(self):
        return reverse_lazy("quest-history", kwargs={"pk": self.pk})

    class Meta:
        ordering=["full_name"]