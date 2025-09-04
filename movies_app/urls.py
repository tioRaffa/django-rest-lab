from django.urls import path

urlpatterns = [
    path('moives/', ..., name='movies'),
    path('movie/<int:pk>/', ...,name='movie')
]