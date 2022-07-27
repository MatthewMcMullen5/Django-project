from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.serializers import GreetingSerializer
from django.http import HttpResponse


def home(request):
    context = {
        'greeting': Greeting.objects.all()
    }
    return render(request, 'IBL/home.html', context)


@api_view(['GET'])
def getgreeting(request):
    greeting = Greeting.objects.all()
    serializer = GreetingSerializer(greeting, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addgreeting(request):
    serializer = GreetingSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def updategreeting(request):
    greeting = Greeting.ojbects.get(id=pk)
    serializer = GreetingSerializer(instance=greeting, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deletegreeting(request, pk):
    greeting = Greeting.objects.get(id=pk)
    greeting.delete()

    return Response()
