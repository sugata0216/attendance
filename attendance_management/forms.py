from django import forms
from .models import Attendance
class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        exclude = ['student', 'date', 'time_limit']
        widgets = {
            'reason': forms.Textarea(attrs={'rows': 3, 'placeholder': '理由を入力してください'}),
            'status': forms.Select(attrs={'id': 'id_status'}),
        }