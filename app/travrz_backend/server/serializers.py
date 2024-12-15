from rest_framework import serializers
from .models import User
from .models import Climb

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ClimbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Climb
        fields = '__all__'