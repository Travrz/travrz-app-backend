"""
Views for the climb api
"""

from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
    OpenApiParameter,
    OpenApiTypes,
)

from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db import models
from core.models import Climb, Tag
from climb import serializers


@extend_schema_view(
    list=extend_schema(
        description="List of climbs",
        parameters=[
            OpenApiParameter(
                name="tags",
                type=OpenApiTypes.STR,
                description="Comma separated list of tag IDs to filter by",
            ),
            OpenApiParameter(
                name="grades",
                type=OpenApiTypes.STR,
                description="Comma separated list of grades to filter by",
            ),
            OpenApiParameter(
                name="locations",
                type=OpenApiTypes.STR,
                description="Comma separated list of locations to filter by",
            ),
        ],
    )
)
class ClimbViewSet(viewsets.ModelViewSet):
    """View for manage climb objects."""

    serializer_class = serializers.ClimbDetailSerializer
    queryset = Climb.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def _params_to_ints(self, qs):
        """Convert a list of string IDs to a list of integers."""
        return [int(str_id) for str_id in qs.split(",")]

    def get_queryset(self):
        """Return objects for the current authenticated user only."""
        tags = self.request.query_params.get("tags")
        grade = self.request.query_params.get("grades")
        location = self.request.query_params.get("locations")
        queryset = self.queryset

        # first check if private
        queryset = queryset.filter(
            models.Q(private=False) | models.Q(user=self.request.user)
        )

        if tags:
            tag_ids = self._params_to_ints(tags)
            queryset = queryset.filter(tags__id__in=tag_ids)

        if grade:
            queryset = queryset.filter(grade=grade)

        if location:
            queryset = queryset.filter(location=location)

        return queryset.distinct()

    def get_serializer_class(self):
        """Return the serializer class for the view."""
        if self.action == "list":
            return serializers.ClimbSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new climb."""
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        """Delete a climb if and only if the user is the owner."""
        climb = self.get_object()
        if climb.user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """Update a climb if and only if the user is the owner."""
        climb = self.get_object()
        if climb.user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)


@extend_schema_view(
    list=extend_schema(
        description="List of tags",
        parameters=[
            OpenApiParameter(
                name="assigned_only",
                type=OpenApiTypes.INT,
                enum=[0, 1],
                description="Return only tags assigned to climbs",
            ),
        ],
    )
)
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
        assigned_only = bool(self.request.query_params.get("assigned_only", 0))
        queryset = self.queryset
        if assigned_only:
            queryset = queryset.filter(climbs__isnull=False)

        return queryset.order_by("-name").distinct()
