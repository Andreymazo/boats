from django.urls import path

from boat.apps import BoatConfig
from boat.views import HomePageView, BoatDetail, make_like_toggle

app_name = BoatConfig.name

urlpatterns = [
    path('', HomePageView.as_view(), name='list'),
    path('<int:pk>/', BoatDetail.as_view(), name='detail'),
    path('like/<int:pk>/', make_like_toggle, name='like_toggle'),
]
