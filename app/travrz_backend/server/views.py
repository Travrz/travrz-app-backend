from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer


def hello_world(request):
    return HttpResponse("Hello, World!")


def get_hello_world(request):
    return Response("Hello, World!")
