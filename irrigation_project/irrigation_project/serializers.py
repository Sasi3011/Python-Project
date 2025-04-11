from rest_framework import serializers
from .models import Plant, UserInput

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'

class UserInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInput
        fields = '__all__'
