from django.urls import path
from .views import CourseAPIView, AvaliacaoAPIView

urlpatterns = [
    path('cursos/', CourseAPIView.as_view(), name='cursos'),
    path('avaliações/', AvaliacaoAPIView.as_view(), name='avaliações')
]