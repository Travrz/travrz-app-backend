from django.urls import path
from server.views import hello_world

urlpatterns = [
    path('', hello_world),
]

