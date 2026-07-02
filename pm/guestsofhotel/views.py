from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from guestsofhotel.forms import GuestForm 
from guestsofhotel.models import Guest

class GuestUpdateView(SuccessMessageMixin, UpdateView):
    model = Guest
    form_class = GuestForm
    success_url = reverse_lazy("home") # или укажи нужный URL
    success_message = "Информация о госте сохранена"

class GuestCreateView(SuccessMessageMixin, CreateView):
    model = Guest
    form_class = GuestForm
    success_url = reverse_lazy("home")
    success_message = "Гость добавлен"