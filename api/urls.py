from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WidgetViewSet, CogViewSet, version_view

router = DefaultRouter()
router.register(r'widgets', WidgetViewSet)
router.register(r'cogs', CogViewSet)

urlpatterns = [
    path('version/', version_view, name='api-version'),
    path('', include(router.urls)),
]

