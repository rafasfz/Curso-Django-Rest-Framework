from rest_framework import serializers
from .models import Course, Avaliation

class AvaliationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliation
        extra_kwargs = {
            'email': {'write_only': True}
        }
        optional_fields = ['comment',]
        fields = (
            'id',
            'name',
            'email',
            'rate',
            'course',
            'active',
            'created_at',
            'updated_at',
        )

    def validate_rate(self, value):
        if value < 0 or value > 5:
            raise serializers.ValidationError('Rate must be between 0 and 5')
        return value

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

