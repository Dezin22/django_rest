from rest_framework import serializers
from .models import Courses, Register
from students.serializers import StudentSerializer
class CoursesSerializer(serializers.ModelSerializer):
   student = StudentSerializer(many=True)
   class Meta:
        model = Courses
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    course = serializers.StringRelatedField()

    class Meta:
        model = Register
        fields = ['student', 'course', 'date_register']