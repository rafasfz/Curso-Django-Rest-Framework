from rest_framework import generics

from .models import Course, Avaliation
from .serializers import AvaliationSerializer, CourseSerializer


class CourseAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class AvaliationAPIView(generics.ListCreateAPIView):
    queryset = Avaliation.objects.all()
    serializer_class = AvaliationSerializer
