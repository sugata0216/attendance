from django.shortcuts import render
def index(request):
    return render(request, 'attendance_management/index.html')
# Create your views here.
