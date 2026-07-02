from django.db import models

class Room(models.Model):
    room_number = models.CharField(max_length=10, verbose_name="Номер комнаты")
    hotel = models.ForeignKey('hotels.Hotel', on_delete=models.CASCADE, verbose_name="Отель")
    room_type = models.ForeignKey('roomtypes.RoomType', on_delete=models.CASCADE, verbose_name="Тип комнаты")

    def __str__(self):
        return f"Комната {self.room_number}"