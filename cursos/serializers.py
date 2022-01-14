from rest_framework import serializers
from .models import Course, Avaliation

class AvaliationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliation
        extra_kwargs = {
            'email': {'write_only': True}
        }
        fields = (
            'id',
            'name',
            'email',
            'comment',
            'rate',
            'course',
            'active',
            'created_at',
            'updated_at',
        )

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'url',
            'active',
            'created_at',
            'updated_at',
            'avaliations',
        )

