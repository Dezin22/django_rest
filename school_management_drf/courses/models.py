from django.db import models
from students.models import Student

class Courses(models.Model):
    COURSE_CHOICES = [
        ('matematica', 'Matemática'),
        ('portugues', 'Português'),
        ('historia', 'História'),
        ('geografia', 'Geografia'),
        ('ciencias', 'Ciências'),
        ('ingles', 'Inglês'),
        ('ed_.fisica', 'Educação Física'),
        ('artes', 'Artes'),
        ('literatura', 'Literatura'),
        ('quimica', 'Química'),
        ('fisica', 'Física'),
        ('biologia', 'Biologia'),
    ]


    name = models.CharField(max_length=100, choices=COURSE_CHOICES, unique=True)
    description = models.CharField(max_length=200)
    students = models.ManyToManyField(Student, through='Register', related_name='courses')

    def __str__(self):
        return self.name
    
class Register(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    date_register = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.student.name} - {self.course.name}'