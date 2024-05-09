# models.py
from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    FMV = models.FloatField()
    transfer_rate = models.FloatField()

class Deal(models.Model):
    name = models.CharField(max_length=100, unique=True)
    projects = models.ManyToManyField(Project)

# serializers.py
from rest_framework import serializers
from .models import Project, Deal

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'FMV', 'transfer_rate']

class DealSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Deal
        fields = ['id', 'name', 'projects']

# views.py
from rest_framework import viewsets
from .models import Project, Deal
from .serializers import ProjectSerializer, DealSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class DealViewSet(viewsets.ModelViewSet):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer

# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, DealViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'deals', DealViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# settings.py
INSTALLED_APPS = [
    ...
    'rest_framework',
    'your_app_name_here',
]

# DevOps, Containerization, Package Management, Formatter Usage, etc.
# - Use virtual environments for managing dependencies
# - Use Docker for containerization
# - Use Git for version control
# - Use Black for code formatting

# Ensure to configure Django settings, database settings, and other necessary configurations as per your project requirements.

