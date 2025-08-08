from django.contrib.auth.models import User
from django.db import models
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, null=True)
    student_number = models.CharField(max_length=7, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    course = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return f"{self.student_number} - {self.name}"
class Subject(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name
class Attendance(models.Model):
    STATUS_CHOICES = [
        ('present', '出席'),
        ('absent', '欠席'),
        ('late', '遅刻'),
        ('leave_early', '早退'),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField()
    TIME_LIMIT_CHOICES = [(1, "1限目"),
                          (2, "2限目"),
                          (3, "3限目"),
                          (4, "4限目"),
                          ]
    time_limit = models.IntegerField(choices=TIME_LIMIT_CHOICES)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    reason = models.TextField(blank=True, null=True)
    class Meta:
        unique_together = ('student', 'subject', 'date')  # 同一授業・同一日には一つだけ記録

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.status}"
# Create your models here.
