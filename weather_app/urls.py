from django.urls import path
from weather_app.views import WeatherOnCityAPIView

urlpatterns = [
    path('clima/', WeatherOnCityAPIView.as_view(), name='weather'),
]