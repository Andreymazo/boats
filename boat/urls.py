from django.urls import path

from boat.apps import BoatConfig
from boat.views import HomePageView

app_name = BoatConfig.name

urlpatterns = [
    path('', HomePageView.as_view(), name='list')
]
