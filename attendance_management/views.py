from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Attendance, Student, Subject
import datetime
def index(request):
    return render(request, 'attendance_management/index.html')
@csrf_exempt  # 簡易的対応、実運用ではCSRFトークン必須
def mark_attendance(request):
    if request.method == 'POST':
        # POSTデータを取得
        date = request.POST.get('date')
        student_id = request.POST.get('student_id')
        subject_id = request.POST.get('subject_id')
        status = request.POST.get('status')

        # ここで出席データ保存処理を実装する（DB保存など）
        # 例: Attendance.objects.create(...)

        return JsonResponse({'status': 'ok'})
    return JsonResponse({'error': 'Invalid method'}, status=400)
def help(request):
    return render(request, 'attendance_management/help.html')
# Create your views here.