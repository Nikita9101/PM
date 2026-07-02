from django.shortcuts import render

from django.views.generic import ListView


from history.models import History

class HistoryListView(ListView):
    model = History

    def get_queryset(self):
        queryset=History.objects.filter(quest__pk=self.kwargs.get("pk"))
        return queryset
