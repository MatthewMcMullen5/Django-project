from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import JsonResponse

from .serializers import ItemSerializer
from .serializers import TaskSerializer
from base.models import Item
from .models import Task


# App landing page
@api_view(['GET'])
def apioverview(request):
    api_urls = {
         'List Item': '/item-list/',
         'List Task': '/task-list/',
         'Item View': '/item-detail/<str:pk>/',
         'Task View': '/task-detail/<str:pk>/',
         'Create Item': '/add-item/',
         'Create Task': '/add-task/',
         'Update Item': '/update-item/<str:pk>/',
         'Update Task': '/update-task/<str:pk>/',
         'Delete Item': '/delete-item/<str:pk>/',
         'Delete Task': '/delete-task/<str:pk>/',
    }
    return Response(api_urls)


# Items
@api_view(['GET'])
def getitem(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def additem(request):
    serializer = ItemSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def itemlist(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def itemdetail(request, pk):
    items = Item.objects.get(id=pk)
    serializer = ItemSerializer(items, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def updateitem(request, pk):
    item = Item.objects.get(id=pk)
    serializer = TaskSerializer(instance=item, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteitem(request, pk):
    item = Item.objects.get(id=pk)
    item.delete()

    return Response()


# Tasks
@api_view(['GET'])
def gettask(request):
    task = Task.objects.all()
    serializer = TaskSerializer(task, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addtask(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def tasklist(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskdetail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def updatetask(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deletetask(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return Response()