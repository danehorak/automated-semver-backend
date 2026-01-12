from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Widget, Cog
from .serializers import WidgetSerializer, CogSerializer
from . import __version__


class WidgetViewSet(viewsets.ModelViewSet):
    """ViewSet for Widget CRUD operations."""
    queryset = Widget.objects.all()
    serializer_class = WidgetSerializer


class CogViewSet(viewsets.ModelViewSet):
    """ViewSet for Cog CRUD operations."""
    queryset = Cog.objects.all()
    serializer_class = CogSerializer


@api_view(['GET'])
def version_view(request):
    """Return the API version with CORS support."""
    return Response({
        'version': __version__,
        'api': 'automated-semver-backend'
    })
