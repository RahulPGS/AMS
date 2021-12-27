from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.contrib.auth.decorators import login_required


def home(response):
    if isinstance(response.user, User):
        if response.user.is_superuser:
            return redirect('logout')
        return redirect('/student')
    return redirect('login')

def register(req):
    if req.method == 'POST':
        data = req.POST
        user = User.objects.get_or_create(username=data["username"], email=f"{data['id_no']}@rguktsklm.ac.in")[0]
        user.set_password(data["password1"])
        user.save()
        student = Student(user=user)
        student.id_no = data["id_no"]
        student.course = data["course"]
        student.email = data["email"]
        student.category = data["category"]
        student.dob = data["dob"]
        student.ph_category = data["ph_category"]
        student.name = data["name"]
        student.year = data["year"]
        student.phone = data["phone"]
        student.save()
        sa = StudentAbout()
        sa.student = student
        sa.save()
        return HttpResponse("Registration success, You can login now.")

    return render(req, 'stu_register.html', {"stu_form": StudentForm, "user_form": UserForm})

@login_required()
def student(req):
    if req.user.is_superuser: return redirect('admin')
    stu = Student.objects.get(user=req.user)
    name = stu.name
    id = stu.id_no
    notifications = Notification.objects.all().order_by('-id')[:5]
    return render(req, 'stu_dash.html', {"name": name, "id_no": id, "notifications": notifications})

@login_required()
def admin(req):
    if not req.user.is_superuser: return redirect('student')
    return render(req, "admin.html", {})

@login_required()
def post_notification(req):
    if not req.user.is_superuser: return redirect('student')
    if req.method == 'POST':
        form = NotificationForm(req.POST, req.FILES)
        form.save()
        return redirect("post_notification")
    return render(req, "post_notification.html", {"form": NotificationForm})

@login_required()
def raise_grievence(req):
    if req.method == 'POST':
        form = GrievenceForm(req.POST, req.FILES)
        obj = form.save(commit=False)
        obj.student = req.user.profile
        obj.save()
        return redirect("raise_grievence")
    return render(req, "raise_grievence.html", {"form": GrievenceForm, "grivences": Grievence.objects.all().order_by("-id")})

@login_required()
def grivences(req):
    if not req.user.is_superuser: return redirect('student')
    return render(req, "grivences.html", {"grivences": Grievence.objects.all().order_by("-id")})

@login_required(login_url='login')
def change_grievence_status(req):
    if not req.user.is_superuser: return redirect('student')
    params = req.GET
    g = Grievence.objects.get(id=int(params['id']))
    g.status = params['status']
    g.save()
    return redirect("grievences")

@login_required(login_url='/login')
def profile(req):
    if req.user.is_superuser: return redirect('admin')
    return render(req, 'profile.html', {'stu': req.user.profile,
                                        'about': StudentAbout.objects.get(student=req.user.profile)})

def edit_profile(req):
    if req.user.is_superuser: return redirect('admin')
    if req.method == 'POST':
        form = StudentAboutForm(req.POST, instance=StudentAbout.objects.get(student=req.user.profile))
        o = form.save(commit=False)
        o.student = req.user.profile
        o.save()
        return redirect("edit_profile")
    return render(req, "about_form.html", {"form": StudentAboutForm})

def faculty_feedback(req):
    if req.user.is_superuser: return redirect("feedbacks")
    if req.method == 'POST':
        form = FacultyFeedbackForm(req.POST)
        s = form.save(commit=False)
        s.student = req.user.profile
        s.save()
        return redirect("faculty_feedback")
    return render(req, "faculty_feedback.html", {"form": FacultyFeedbackForm})

def feedbacks(req):
    if not req.user.is_superuser: return redirect("faculty-feedback")
    year = "puc-1"
    try:
        year = req.GET["year"]
    except:
        pass
    return render(req, "feedbacks.html", {"feedbacks": FacultyFeedback.objects.filter(year=year).order_by("-id"), "year": year})

def update_time_table(req):
    if not req.user.is_superuser: return redirect("time-table")
    if req.method == 'POST':
        form = TimeTableForm(req.POST, req.FILES, instance=TimeTable.objects.get(year=req.POST['year']))
        form.save()
        return redirect("update_time_table")
    return render(req, 'update-time-table.html', {"timetables": TimeTable.objects.all(), "form": TimeTableForm()})

def time_table(req):
    return render(req, 'time-table.html', {"timetables": TimeTable.objects.all()})

def academic_calender(req):
    return render(req, 'academic-calender.html', {"cal": AcademicCalender.objects.first()})

def upload_academic_calender(req):
    if req.method == 'POST':
        form = AcademicCalenderForm(req.POST, req.FILES, instance=AcademicCalender.objects.first())
        form.save()
        return redirect("upload_academic_calender")
    return render(req, 'upload-calender.html', {"cal": AcademicCalender.objects.first(), "form": AcademicCalenderForm()})\

def laptop_details(req):
    return render(req, 'laptop-details.html', {"stu": req.user.profile, "lsn": StudentAbout.objects.get(student=req.user.profile).laptop_serial_number})