from django.db import models


class History(models.Model):

    guest = models.ForeignKey('guestsofhotel.Guest', on_delete=models.CASCADE, blank=True, null=True,
                              verbose_name="Гость")

    room = models.ForeignKey('rooms.Room', on_delete=models.CASCADE, blank=True, null=True, verbose_name="Комната")

    check_in = models.DateField(verbose_name="Дата заезда")

    check_out = models.DateField(verbose_name="Дата выезда")

    comment = models.TextField(blank=True, null=True, verbose_name="Комментарий")

    def __str__(self):
        return f"Заселение #{self.id}"