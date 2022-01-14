from django.urls import path

from .views import CourseAPIView, AvaliationAPIView

urlpatterns = [
    path('courses/', CourseAPIView.as_view(), name='courses'),
    path('avaliations/', AvaliationAPIView.as_view(), name='avaliations'),
]
