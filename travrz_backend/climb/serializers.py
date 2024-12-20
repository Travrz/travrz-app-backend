"""
Serializers for the climb API.
"""

from rest_framework import serializers

from core.models import Climb, Tag


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag objects."""

    class Meta:
        model = Tag
        fields = [
            "id",
            "name",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]


class ClimbSerializer(serializers.ModelSerializer):
    """Serializer for climb objects. mainly list view"""

    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = Climb
        fields = [
            "id",
            "climb_name",
            "grade",
            "location",
            "tags",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]

    def create(self, validated_data):
        tags = validated_data.pop("tags", [])
        climb = Climb.objects.create(**validated_data)
        for tag in tags:
            tag_obj, _ = Tag.objects.get_or_create(name=tag["name"])
            climb.tags.add(tag_obj)

        return climb

    def update(self, instance, validated_data):
        tags = validated_data.pop("tags", [])
        climb = super().update(instance, validated_data)
        climb.tags.clear()
        for tag in tags:
            tag_obj, _ = Tag.objects.get_or_create(name=tag["name"])
            climb.tags.add(tag_obj)

        return climb


class ClimbDetailSerializer(ClimbSerializer):
    """Serializer for climb detail objects"""

    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())

    class Meta(ClimbSerializer.Meta):
        fields = ClimbSerializer.Meta.fields + [
            "description",
            "media_url",
            "rating",
        ]
        read_only_fields = ClimbSerializer.Meta.read_only_fields + [
            "rating",  # rating is avgd from all ratings
        ]
