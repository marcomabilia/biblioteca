from rest_framework import serializers
from obras import models

class ObrasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Obras
        fields = '__all__'