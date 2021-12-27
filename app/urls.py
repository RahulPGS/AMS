from django.urls import path, include, re_path
from .views import *
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static

urlpatterns = [
    path("", home, name="home"),
    path("register", register, name="register"),
    path("student", student, name="student"),
    path("admin", admin, name="admin"),
    path("post-notification", post_notification, name="post_notification"),
    path("raise-grievence", raise_grievence, name="raise_grievence"),
    path("grievences", grivences, name="grievences"),
    path("change-grievence-status", change_grievence_status, name="change_grievence_status"),
    path('profile', profile, name='profile'),
    path('edit-profile', edit_profile, name='edit_profile'),
    path("faculty-feedback", faculty_feedback, name="faculty_feedback"),
    path("feedbacks", feedbacks, name="feedbacks"),
    path("update-time-table", update_time_table, name="update_time_table"),
    path("time-table", time_table, name="time_table"),
    path('academic-calender', academic_calender, name="academic_calender"),
    path("upload-academic-calender", upload_academic_calender, name="upload_academic_calender"),
    path("laptop-details", laptop_details, name="laptop_details"),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    ] + static(settings.STATIC_URL, doucument_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)