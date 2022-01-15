from gc import get_objects
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.generics import get_object_or_404

from .models import Course, Avaliation
from .serializers import AvaliationSerializer, CourseSerializer


class CoursesAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class AvaliationsAPIView(generics.ListCreateAPIView):
    queryset = Avaliation.objects.all()
    serializer_class = AvaliationSerializer

    def get_queryset(self):
        if self.kwargs.get('course_pk'):
            return self.queryset.filter(course_id=self.kwargs.get('course_pk'))
        return self.queryset.all()
        


class AvaliationAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliation.objects.all()
    serializer_class = AvaliationSerializer

    def get_object(self):
        course_pk = self.kwargs.get('course_pk')
        avaliation_pk = self.kwargs.get('avaliation_pk')
        if course_pk:
            return get_object_or_404(self.get_queryset(),
                                    course_id=course_pk,
                                    pk=avaliation_pk)
        return get_object_or_404(self.get_queryset(), pk=avaliation_pk)
