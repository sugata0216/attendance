from django.apps import AppConfig


class AttendanceManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'attendance_management'
# class AttendanceManagementConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'attendance_management'
#     def ready(self):
#         import attendance_management.signals
