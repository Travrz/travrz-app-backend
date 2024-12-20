"""
Views for the climb api
"""

from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Climb, Tag
from climb import serializers


class ClimbViewSet(viewsets.ModelViewSet):
    """View for manage climb objects."""

    serializer_class = serializers.ClimbDetailSerializer
    queryset = Climb.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Return objects for the current authenticated user only."""
        return self.queryset.filter(user=self.request.user).order_by("-id")

    def get_serializer_class(self):
        """Return the serializer class for the view."""
        if self.action == "list":
            return serializers.ClimbSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new climb."""
        serializer.save(user=self.request.user)


class TagViewSet(
    mixins.UpdateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    """View for manage tag objects."""

    serializer_class = serializers.TagSerializer
    queryset = Tag.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Return objects for the current authenticated user only."""
        return self.queryset.order_by("-name")
