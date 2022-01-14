from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Course, Avaliation
from .serializers import CourseSerializer, AvaliationSerializer

class CourseAPIView(APIView):

    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    

class AvaliationAPIView(APIView):

    def get(self, request):
        avaliations = Avaliation.objects.all().select_related('course')
        print(request.data)
        serializer = AvaliationSerializer(avaliations, many=True)
        return Response(serializer.data)
