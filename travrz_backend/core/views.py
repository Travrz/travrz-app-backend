"""
Core views for app.
"""

from rest_framework.response import Response
from rest_framework import generics


class HealthCheckView(generics.GenericAPIView):
    """Returns successful response."""

    def get(self, request):
        return Response({"healthy": True})
