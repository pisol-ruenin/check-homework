from django.conf.urls import url, include
from django.urls import path
from . import views
app_name = "assignment"
urlpatterns = [
    url(r'^student_dashboard$', views.student_dashboard, name='student_dashboard'),
    url(r'^student_subject$', views.student_subject, name='student_subject'),
    url(r'^do_assignment$', views.do_assignment, name='do_assignment'),
    url(r'^create_assignment$', views.create_assignment.as_view(), name='create_assignment'),
    url(r'^teacher_dashboard$', views.teacher_dashboard, name='teacher_dashboard'),
    path('<int:subject>/score/<int:assignment>/',
         views.AssignmentScore.as_view(), name='assignment_score'),
    path('<int:subject>/score/<int:assignment>/list/<int:std_code>/',
         views.StudentAssignmentScore.as_view(), name='student_assignment_score'),
    path('api/score/<int:subject>/<int:assignment>/',
         views.ChartScoreAssignment.as_view(), name='assignment_report_api'),
    path('report/<int:subject>/list/<int:assignment>/',
         views.AssignmentReport.as_view(), name='assignment_report'),
    path('api/score/<int:subject>/',
         views.ChartScoreSubject.as_view(), name='subject_report_api'),
    path('report/<int:subject>/',
         views.SubjectReport.as_view(), name='subject_report'),
    path('<int:subject>/score/<int:assignment>/list/',
         views.StudentReportList.as_view(), name='student_report_list'),
    path('report/<int:subject>/list/',
         views.AssignmentReportList.as_view(), name='assignment_report_list'),
    path('score/<int:pk>/edit_choice/',
         views.EditChoiceScore.as_view(), name='edit_choice_score'),
    path('score/<int:pk>/edit_matching/',
         views.EditMatchingScore.as_view(), name='edit_matching_score'),
    path('score/<int:pk>/edit_open/',
         views.EditOpenEndedScore.as_view(), name='edit_open_score'),
]
