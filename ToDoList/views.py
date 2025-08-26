from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ToDoList.models import TaskModel
from ToDoList.serializer import TaskSerializer
from django.shortcuts import get_object_or_404


class TasksAPIView(APIView):
    def get(self, request):
        tasks = TaskModel.objects.all()

        done = request.query_params.get('done')
        if done is not None:
            if done.lower() == 'true':
                tasks = tasks.filter(done=True)
            elif done.lower() == 'false':
                tasks = tasks.filter(done=False)

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
    

class TaskAPIView(APIView):
    def get(self, request, pk):
        task = get_object_or_404(TaskModel, pk=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request, pk):
        task = get_object_or_404(TaskModel, pk=pk)
        serializer = TaskSerializer(task, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)