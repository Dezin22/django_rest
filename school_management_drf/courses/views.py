from rest_framework import viewsets
from .models import Courses, Register
from .serializers import CoursesSerializer, RegisterSerializer

class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer

class RegisterViewSet(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer