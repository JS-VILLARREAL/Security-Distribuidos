from rest_framework import serializers
from security.models import Module

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'

class ModulePublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = (
            'id',
            'name',
            'description',
            'route',
            'state',
        )
