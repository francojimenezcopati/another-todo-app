from django.shortcuts import redirect
from .serializer import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task


# Create your views here.

# @api_view(['GET'])
# def endpoints(request):
#     urls = ['/api/tasks', '/api/tasks/<id>']
#     return 0


@api_view(['GET', 'POST'])
def listTasks(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
    else:
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
    
    return Response(serializer.data)




@api_view(['GET', 'PUT', 'DELETE'])
def taskDetails(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'GET':
        serializer = TaskSerializer(task, many=False)
    elif request.method == 'PUT':
        data = request.data
        serializer = TaskSerializer(task, data, many=False)
        if serializer.is_valid():
            serializer.save()
    else:
        task.delete()
        return Response('Task deleted successfully!')
    
    return Response(serializer.data)