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

    # Nested Relationship
    avaliations = AvaliationSerializer(many=True, read_only=True)

    # HyperLinked Related Field
    # avaliations = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliation-detail')

    # Primary Key Related Field
    # avaliations = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'url',
            'active',
            'avaliations',
            'created_at',
            'updated_at',
        )

