from rest_framework import serializers
from security.models import UserRole, User, Role

class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = '__all__'

class UserRolePublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = (
            'id',
            'user',
            'role',
        )