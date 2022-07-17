from rest_framework import serializers
from base.models import Item
from IBL.models import Greeting
from .models import Task
# can't natively handle complex data types like django model instances


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class GreetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Greeting
        fields = '__all__'
