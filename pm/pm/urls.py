"""
URL configuration for PM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

from django.contrib.auth.decorators import login_required

from django.urls import path, include
from django.conf import settings  # PREP
from django.conf.urls.static import static  # PREP


from guestsofhotel.views import GuestCreateView, GuestUpdateView
from history.views import HistoryListView

from home.views import HomeView

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),

    path("", HomeView.as_view(), name="home"),
    path("guest/new/", GuestCreateView.as_view(), name="new-guest"),
    path("admin/", admin.site.urls),
    path("guest/new/", GuestCreateView.as_view(), name="new-guest"),
    path("guest/<int:pk>/update/", GuestUpdateView.as_view(), name="guest-update"),
    path("guest/<int:pk>/history", HistoryListView.as_view(), name="guest-history"),
    path("admin/", admin.site.urls),
]

urlpatterns += i18n_patterns(

)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
