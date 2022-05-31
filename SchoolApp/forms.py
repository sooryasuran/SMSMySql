import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from SchoolApp.models import Login, Teacher, Student, TimeTable, Circular, Feedback, Attendance


def phone_number_validator(value):
    if not re.compile(r'^[7-9]\d{9}$').match(value):
        raise ValidationError('This is Not a Valid Phone Number')
class DateInput(forms.DateInput):
    input_type = 'date'
class LoginForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='Password', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Confirm password', widget=forms.PasswordInput)
    class Meta:
        model= Login
        fields = ('username','password1','password2')
class TeacherForm(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validator])
    class Meta:
        model = Teacher
        exclude = ('user',)
class StudentForm(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validator])
    class Meta:
        model = Student
        exclude= ('user',)
class TimeTableForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model = TimeTable
        fields = '__all__'
class CircularForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model = Circular
        fields = '__all__'
class FeedbackForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model = Feedback
        fields=('name','subject','description','date')
class AddAttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ('student','attendance')

