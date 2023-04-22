from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view
import io
from rest_framework import status
from todos.models import Task
from .serializers import TaskSerializer


@api_view(['GET'])
def get_task_list(request):
    tasks = Task.objects.all()
    # print('>>> tasks : ',tasks)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_task_detail(request, pk):
    task = Task.objects.get(pk=pk)
    serializer = TaskSerializer(task)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data, context={'request':request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT', 'PATCH'])
def update_task(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)