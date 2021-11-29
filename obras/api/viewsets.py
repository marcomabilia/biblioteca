from obras import models
from rest_framework import viewsets
from obras.api import serializers

class ObrasViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ObrasSerializer
    queryset = models.Obras.objects.all()
