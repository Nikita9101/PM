from django.views.generic import ListView
from history.models import History

class HomeView(ListView):
    """
    Главная страница со списком истории заселений.
    """
    template_name = "home/home.html"
    model = History  