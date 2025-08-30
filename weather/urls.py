from django.urls import path
from weather.views import WeatherOnCityAPIView

urlpatterns = [
    path('clima/', WeatherOnCityAPIView.as_view(), name='weather'),
]