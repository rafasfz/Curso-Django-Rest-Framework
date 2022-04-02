from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

from cursos.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('api/v1/', include('cursos.urls')),
    path('api/v1/auth/', views.obtain_auth_token),
    path('api/v2/', include(router.urls))
]
