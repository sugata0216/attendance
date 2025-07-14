from django.db import models
class Student(models.Model):
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
    time_limit = models.IntegerField(null=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'subject', 'date')  # 同一授業・同一日には一つだけ記録

    def __str__(self):
        return f"{self.date} - {self.student.name} - {self.get_status_display()}"
# Create your models here.
