from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = {"user"}

class StudentAboutForm(forms.ModelForm):
    class Meta:
        model = StudentAbout
        exclude = {"student"}

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        exclude = {'created_date'}

class GrievenceForm(forms.ModelForm):
    class Meta:
        model = Grievence
        exclude = {'student', 'status'}

class FacultyFeedbackForm(forms.ModelForm):
    class Meta:
        model = FacultyFeedback
        exclude = {"student"}

class TimeTableForm(forms.ModelForm):
    class Meta:
        model = TimeTable
        exclude = {}

class AcademicCalenderForm(forms.ModelForm):
    class Meta:
        model = AcademicCalender
        exclude = {}
