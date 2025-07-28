from django import forms
from django.contrib.auth.models import User
from attendance_management.models import Student
from django.db import transaction
class SignUpForm(forms.ModelForm):
    student_number = forms.CharField(label='学籍番号')
    name = forms.CharField(label='名前')
    course = forms.CharField(label='コース')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
    def clean_student_number(self):
        student_number = self.cleaned_data.get('student_number')
        if Student.objects.filter(student_number=student_number).exists():
            raise forms.ValidationError("この学籍番号はすでに登録されています。")
        return student_number
    def save(self, commit=True):
        with transaction.atomic():
            user = super().save(commit=False)
            user.set_password(self.cleaned_data['password'])
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
                Student.objects.create(
                    user=user,
                    student_number=self.cleaned_data['student_number'],
                    name=self.cleaned_data['name'],
                    email=self.cleaned_data["email"],
                    course=self.cleaned_data['course'],
                )
                print("Studentレコード作成完了")
            return user