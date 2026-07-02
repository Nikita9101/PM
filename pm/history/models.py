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

    def get_duration(self):
        """
        Возвращает количество дней между заездом и выездом
        """
        if self.check_in and self.check_out:
            delta = self.check_out - self.check_in
            return f"{delta.days} дн."
        return "Нет данных"

    class Meta:
        ordering = ["check_in"]