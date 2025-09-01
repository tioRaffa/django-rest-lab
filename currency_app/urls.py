from django.urls import path
from .views import CurrencyConvertAPIView

urlpatterns = [
    path('conversor/', CurrencyConvertAPIView.as_view(), name='conversions')
]