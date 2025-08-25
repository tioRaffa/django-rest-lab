from django.urls import path
from .views import CourseAPIView, AvaliacaoAPIView, CoursePKview

urlpatterns = [
    path('cursos/', CourseAPIView.as_view(), name='cursos'),
    path('curso/<int:pk>/', CoursePKview.as_view(), name='curso'),
    path('avaliações/', AvaliacaoAPIView.as_view(), name='avaliações')
]