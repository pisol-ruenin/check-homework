from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from ..models import *
# from django.template import loader


def student_dashboard(request):

    all_subjects = Subject.objects.all() 
    member =  MemberSection.objects.all() 
    # Subject
    # template = loader.get_template('student/student-dashboard.html')
    context = {'all_subjects':all_subjects,'member':member
    }
    # return HttpResponse(template.render(context,request))
    return render(request, 'student/student-dashboard.html',context)

def student_subject(request):
    all_assignment = Assignment.objects.all()
    context = {'all_assignment':all_assignment}
    return render(request, 'student/student-subject.html',context)

def do_assignment(request):
    return render(request, 'student/do-assignment.html')

def create_assignment(request):
    return render(request, 'teacher/create-assignment.html')

def teacher_dashboard(request):
    return render(request, 'teacher/teacher-dashboard.html')