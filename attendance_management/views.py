from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Attendance, Student, Subject
import datetime
from django.views import generic
from .forms import AttendanceForm
from django.contrib.auth.decorators import login_required
def index(request):
    return render(request, 'attendance_management/index.html')
def help(request):
    return render(request, 'attendance_management/help.html')
def create_attendance(request, date):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance_management:index')
    else:
        form = AttendanceForm(initial={'date' : date})
    return render(request, 'attendance_management/create.html', {
        'form':form,
        'date':date,
        'object':None
        })
def update_attendance(request, date, time_limit):
    attendance = get_object_or_404(Attendance, date=date, time_limit=time_limit, student=request.user.student)
    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=attendance)
        if form.is_valid():
            form.save()
            return redirect('attendance_management:index')
    else:
        form = AttendanceForm(instance=attendance)
    return render(request, 'attendance_management/create.html', {
        'form':form,
        'date':date,
        'object':attendance
    })
@login_required
def create_or_update_attendance(request, date, time_limit):
    time_limit = int(time_limit)
    try:
        attendance = Attendance.objects.get(date=date, time_limit=time_limit, student=request.user.student)
        is_update = True
    except Attendance.DoesNotExist:
        attendance = None
        is_update = False
    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=attendance)
        if form.is_valid():
            new_attendance = form.save(commit=False)
            new_attendance.date = date
            new_attendance.time_limit = time_limit
            new_attendance.student = request.user.student
            new_attendance.save()
            return redirect('attendance_management:index')
    else:
        form = AttendanceForm(instance=attendance)
    return render(request, 'attendance_management/create.html', {
        'form' : form,
        'date' : date,
        'time_limit' : time_limit,
        'is_update' : is_update,
    })
@csrf_exempt
def mark_attendance(request):
    if request.method == 'POST':
        # POSTデータを取得
        date = request.POST.get('date')
        student_id = request.POST.get('student_id')
        subject_id = request.POST.get('subject_id')
        status = request.POST.get('status')

        return JsonResponse({'status': 'ok'})
    return JsonResponse({'error': 'Invalid method'}, status=400)
def get_events(request):
    if request.method == 'GET':
        events = []
        for attendance in Attendance.objects.all():
            events.append({
                'title': f"{attendance.subject.name}（{attendance.student.name}）",
                'start': attendance.date.strftime("%Y-%m-%dT%H:%M:%S"),
                'end': attendance.date.strftime("%Y-%m-%dT%H:%M:%S"),
            })
        return JsonResponse(events, safe=False)
# Create your views here.