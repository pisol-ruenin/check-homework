from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

def student_dashboard(request):
    return render(request, 'student/student-dashboard.html')

def student_subject(request):
    return render(request, 'student/student-subject.html')

def do_assignment(request):
    return render(request, 'student/do-assignment.html')

def create_assignment(request):
    return render(request, 'teacher/create_assignment.html')

def teacher_dashboard(request):
    return render(request, 'teacher/teacher_dashboard.html')

def signin(request):
    return render(request, 'signin.html')

def signup(request):
    return render(request, 'signup.html')