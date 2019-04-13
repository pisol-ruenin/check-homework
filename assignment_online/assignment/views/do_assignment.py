from django.shortcuts import render

def student_dashboard(request):
    return render(request, 'student/student-dashboard.html')

def student_subject(request):
    return render(request, 'student/student-subject.html')

def do_assignment(request):
    return render(request, 'student/do-assignment.html')

def create_assignment(request):
    return render(request, 'teacher/create-assignment.html')

def teacher_dashboard(request):
    return render(request, 'teacher/teacher-dashboard.html')