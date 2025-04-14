from rest_framework import serializers
from TestForAbit.models import UserPasses, UserProgress

class UserPassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPasses
        fields = '__all__'

class UserProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProgress
        fields = '__all__'
