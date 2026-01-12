from rest_framework import serializers
from .models import Widget, Cog


class WidgetSerializer(serializers.ModelSerializer):
    """Serializer for Widget model."""
    
    class Meta:
        model = Widget
        fields = ['id', 'name', 'description', 'quantity', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class CogSerializer(serializers.ModelSerializer):
    """Serializer for Cog model."""
    
    class Meta:
        model = Cog
        fields = ['id', 'name', 'description', 'size', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

