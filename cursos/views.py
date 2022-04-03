from rest_framework import generics
from rest_framework.generics import get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import permissions

from .models import Course, Avaliation
from .serializers import AvaliationSerializer, CourseSerializer
from .permissions import isAdminOrReadOnly

# API V1

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


# API V2

class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = (isAdminOrReadOnly, )
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, methods=['get'])
    def avaliations(self, request, pk=None):
        self.pagination_class.page_size = 5
        avaliations = Avaliation.objects.filter(course_id=pk)
        page = self.paginate_queryset(avaliations)

        if page:
            serializer = AvaliationSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serailizer = AvaliationSerializer(avaliations, many=True)
        return Response(serailizer.data)

"""
class AvaliationViewSet(viewsets.ModelViewSet):
    queryset = Avaliation.objects.all()
    serializer_class = AvaliationSerializer
"""

class AvaliationViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
    ):
    
    queryset = Avaliation.objects.all()
    serializer_class = AvaliationSerializer
