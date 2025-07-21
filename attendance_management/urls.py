from django.urls import path
from . import views
app_name = 'attendance_management'
urlpatterns = [
    path('', views.index, name='index'),
    path('mark_attendance/', views.mark_attendance, name='mark_attendance'),
    path('help/', views.help, name='help'),
    path('create/<str:date>/<int:time_limit>/', views.create_or_update_attendance, name='create_or_update_attendance'),
    # path('<int:pk>/update/', views.UpdateView.as_view(), name="update")
    path('get_events/', views.get_events, name='get_events'),
]