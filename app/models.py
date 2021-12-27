from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Student(models.Model):
    course_year_choices = [("puc", "PUC"),
                           ("cse", "CSE"),
                           ("ece", "ECE"),
                           ("chem", "CHEM"),
                           ("mech", "MECH"),
                           ("civil", "CIVIL")
                           ]
    gender_choices = [("male", "Male"), ("female", "Female")]
    user = models.OneToOneField(User, unique=True, related_name='profile', on_delete=models.CASCADE)
    id_no = models.CharField(max_length=7)
    name = models.CharField(max_length=30, null=False, blank=False)
    year = models.IntegerField(default=1)
    course = models.CharField(max_length=10, null=False, blank=False, choices=course_year_choices)
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=gender_choices, default="male")
    category = models.CharField(max_length=5)
    ph_category = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    email = models.EmailField()

class StudentAbout(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_about')
    education = models.CharField(max_length=20)
    father_name = models.CharField(max_length=50)
    address = models.TextField()
    hostel = models.CharField(max_length=20)
    mess = models.CharField(max_length=20)
    aadhaar = models.CharField(max_length=12)
    laptop_serial_number = models.CharField(max_length=100)

class Notification(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField()
    media = models.FileField(blank=True, null=True)
    created_date = models.DateTimeField(default=datetime.now())

    def save(self, *args, **kwargs):
        self.created_date = datetime.now()
        super(Notification, self).save(*args, **kwargs)

class Grievence(models.Model):
    statuses = [
        ("under_processing", "Under Processing"),
        ("solved", "Solved"),
        ("visit_office", "Visit Office")
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student')
    title = models.CharField(max_length=30, default="")
    description = models.TextField()
    status = models.CharField(max_length=100, default="under_processing", choices=statuses)
    media = models.FileField(blank=True, null=True)

class FacultyFeedback(models.Model):
    year_choices = [
        ("puc-1", "PUC-1"),
        ("puc-2", "PUC-2"),
        ("Engineering-1", "Engineering-1"),
        ("Engineering-2", "Engineering-2"),
        ("Engineering-3", "Engineering-3"),
        ("Engineering-4", "Engineering-4"),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_feedback')
    faculty_name = models.CharField(max_length=100)
    feedback = models.TextField()
    year = models.CharField(max_length=50, choices=year_choices)


class TimeTable(models.Model):
    year_choices = [
        ("puc-1", "PUC-1"),
        ("puc-2", "PUC-2"),
        ("Engineering-1", "Engineering-1"),
        ("Engineering-2", "Engineering-2"),
        ("Engineering-3", "Engineering-3"),
        ("Engineering-4", "Engineering-4"),
    ]
    year = models.CharField(max_length=50, choices=year_choices)
    file = models.FileField()

class AcademicCalender(models.Model):
    file = models.FileField()