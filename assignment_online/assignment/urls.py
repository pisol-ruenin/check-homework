from django.conf.urls import url , include
from django.urls import path
from . import views
app_name = "assignment"
urlpatterns = [
    url(r'^student_dashboard$', views.student_dashboard, name='student_dashboard'),
    url(r'^student_subject$', views.student_subject, name='student_subject'),
    url(r'^do_assignment$', views.do_assignment, name='do_assignment'),
    url(r'^create_assignment$', views.create_assignment, name='create_assignment'),
    url(r'^teacher_dashboard$', views.teacher_dashboard, name='teacher_dashboard'),
    
]
