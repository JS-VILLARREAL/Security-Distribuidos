from rest_framework import serializers
from security.models import ViewModule

class ModuleViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewModule
        fields = '__all__'

class ModuleViewPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewModule
        fields = (
            'id',
            'module',
            'view',
        )