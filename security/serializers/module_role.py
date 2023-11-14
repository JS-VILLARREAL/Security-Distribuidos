from rest_framework import serializers
from security.models import ModuleRole

class ModuleRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModuleRole
        fields = '__all__'

class ModuleRolePublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModuleRole
        fields = (
            'id',
            'module',
            'role',
        )