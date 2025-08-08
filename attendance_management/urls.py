from django.urls import path
from . import views
app_name = 'attendance_management'
urlpatterns = [
    path('', views.index, name='index'),
    path('mark_attendance/', views.mark_attendance, name='mark_attendance'),
    path('help/', views.help, name='help'),
    path('create/<str:date>/<int:time_limit>/', views.create_or_update_attendance, name='create_or_update_attendance'),
    path('get_events/', views.get_events, name='get_events'),
    path('attendance/delete/<int:pk>/', views.attendance_delete, name='attendance_delete'),
    path('attendance/download/', views.export_attendance_csv, name='export_attendance_csv'),
    path('summary/', views.attendance_summary, name='attendance_summary'),
    path('summary_by_subject/', views.attendance_by_subject, name='attendance_by_subject'),
    path('pdf/', views.download_attendance_pdf, name='attendance_pdf'),
    path('history/', views.attendance_history, name='attendance_history'),
    path('export_excel/', views.export_attendance_excel, name='export_excel'),
]