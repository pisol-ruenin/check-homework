from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.http import HttpResponseRedirect
from django.shortcuts import redirect


def student_dashboard(request):
    return render(request, 'student/student_dashboard.html')