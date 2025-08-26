from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ToDoList.models import TaskModel
from ToDoList.serializer import TaskSerializer



class TaskAPIView(APIView):
    def get(self, request):
        tasks = TaskModel.objects.all()

        done = request.query_params.get('done')
        if done is not None:
            tasks = tasks.filter(done=(done.lower() == 'true'))

        search = request.query_params.get('search')
        if search:
            tasks = tasks.filter(title__icontains=search)


        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)