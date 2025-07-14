from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('mark_attendance/', views.mark_attendance, name='mark_attendance'),
    path('help/', views.help, name='help')
]