from rest_framework import serializers
from security.models import Person, User

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class PersonPublicSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = (
            'id',
            'full_name',
            'address',
            'phone',
            'mail',
            'state',
            'username',
        )

    def get_username(self, obj):
        user_instance = User.objects.filter(person=obj.id).first()
        if user_instance:
            return {
                'id': user_instance.id,
                'username': user_instance.username,
                'password': user_instance.password,
                'state': user_instance.state,
            }
        return None
