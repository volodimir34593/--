

from django.db import models

# Модель для вчителів
class Teacher(models.Model):
    name = models.CharField(max_length=100)

# Модель для студентів
class Student(models.Model):
    name = models.CharField(max_length=100)

# Модель для курсів
class Course(models.Model):
    name = models.CharField(max_length=100)

# Модель для керівників
class Supervisor(models.Model):
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)
    # додайте поля для керівника

# Модель для зв'язку багато до багатьох між курсами та студентами
class Enrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

# Create your models here.
