from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CoursesViewSet, RegisterViewSet

router = DefaultRouter()
router.register('courses', CoursesViewSet, basename='courses')
router.register('register', RegisterViewSet, basename='register')

urlpatterns = [
    path('', include(router.urls)),
]
