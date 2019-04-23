from django.conf.urls import url, include
from django.urls import path
from . import views
app_name = "assignment"
urlpatterns = [

    url(r'^create_assignment$', views.create_assignment, name='create_assignment'),
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
     
    path('subject/',views.StudentDashboard.as_view(), name='student_dashboard'),
    path('subject/<int:subject>/',views.StudentSubject.as_view(), name='student_subject'),
    path('subject/<int:subject>/<int:id>/',views.DoAssignment.as_view(), name='do_assignment'),
#     path('subject/<int:subject>/<int:id>/',views.EditDoAssignment.as_view(), name='edit_do_assignment'),
    path('subject1/<int:subject>/<int:id>/<int:no>/',views.DoChoice.as_view(), name='choice'),
    path('subject2/<int:subject>/<int:id>/<int:no>/',views.DoMatching.as_view(), name='matching'),
    path('subject3/<int:subject>/<int:id>/<int:no>/',views.DoOpenended.as_view(), name='openended'),
#     path('subject3/<int:subject>/<int:id>/<int:no>/',views.EditOpenended.as_view(), name='editopenended'),
]
