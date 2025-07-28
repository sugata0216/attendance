# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.contrib.auth.models import User
# from attendance_management.models import Student
# @receiver(post_save, sender=User)
# def create_student_for_new_user(sender, instance, created, **kwargs):
#     if created:
#         Student.objects.create(user=instance)
