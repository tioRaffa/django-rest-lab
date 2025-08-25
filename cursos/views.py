from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Course, Avaliação
from .serializer import CourseSerializer, AvaliacaoSerializer

class CourseAPIView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)

        return Response(serializer.data)
    

class AvaliacaoAPIView(APIView):
    def get(self, request):
        avaliacoes = Avaliação.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)

        return Response(serializer.data)