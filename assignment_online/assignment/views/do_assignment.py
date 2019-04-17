from django.shortcuts import render
from django.views import generic
from ..models import *
from django.http import JsonResponse
from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.response import Response

class StudentDashboard(generic.TemplateView):
    template_name = 'student/student-dashboard.html'
    def get_context_data(self, **kwargs):
        context = super( StudentDashboard, self).get_context_data(**kwargs)
        context['subject'] = MemberSection.objects.filter(student__user=self.request.user)
        print(context['subject'])
        # context['assignment'] = Assignment.objects.get(pk=self.kwargs['assignment'])
        # context['subject'] = Subject.objects.get(pk=self.kwargs['subject'])

        return context

# class StudentDashboard(generic.View):
#     template_
class StudentSubject(generic.TemplateView):
    template_name = 'student/student-subject.html'
    def get_context_data(self, **kwargs):
        context = super( StudentSubject, self).get_context_data(**kwargs)
        code = self.kwargs['subject']
        context['sub'] = Subject.objects.get(subject_code = code )
   
        context['subject'] = Assignment.objects.filter(subject__subject_code = code)
        m = MemberSection.objects.get(student__user=self.request.user,subject__subject_code=self.kwargs['subject'])
        assignment=list()
        for i in context['subject']:
            if i.subject.subject_code == m.subject.subject_code:
                assignment.append(i)
        context['assignment'] = assignment
        # context['assignment'] = Assignment.objects.get(pk=self.kwargs['assignment'])
        # context['subject'] = Subject.objects.get(pk=self.kwargs['subject'])

        return context

class DoAssignment(generic.TemplateView):
    template_name = 'student/do-assignment.html'
    def get_context_data(self, **kwargs):
        context = super( DoAssignment, self).get_context_data(**kwargs)
        code = self.kwargs['subject']
        ass_id = self.kwargs['id']
        context['questions'] = Question.objects.filter(assignment = ass_id)
        return context
        # code = self.kwargs['subject']
        # context['sub'] = Subject.objects.get(subject_code = code )
   
        # context['subject'] = Assignment.objects.filter(subject__subject_code = code)
        # m = MemberSection.objects.get(student__user=self.request.user,subject__subject_code=self.kwargs['subject'])
        # assignment=list()
        # for i in context['subject']:
        #     if i.subject.subject_code == m.subject.subject_code:
        #         assignment.append(i)
        # context['assignment'] = assignment

# def do_assignment(request):
#     return render(request, 'student/do-assignment.html')

def create_assignment(request):
    return render(request, 'teacher/create-assignment.html')

def teacher_dashboard(request):
    return render(request, 'teacher/teacher-dashboard.html')