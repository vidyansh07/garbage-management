from rest_framework import serializers
from .models import CustomUser
from collectors.models import Collector

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password', 'is_collector')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

class CollectorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Collector
        fields = ('id', 'user', 'employee_id')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_data['is_collector'] = True
        user = CustomUser.objects.create_user(**user_data)
        collector = Collector.objects.create(user=user, **validated_data)
        return collector