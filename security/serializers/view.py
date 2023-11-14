from rest_framework import serializers
from security.models import View

class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = View
        fields = '__all__'

class ViewPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = View
        fields = (
            'id',
            'name',
            'description',
            'route',
            'state',
        )
