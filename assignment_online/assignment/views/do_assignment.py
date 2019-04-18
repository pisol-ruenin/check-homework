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
        print( context['questions'])
        return context

class DoChoice(generic.TemplateView):
    template_name = 'student/choice.html'
    def get_context_data(self, **kwargs):
        context = super( DoChoice, self).get_context_data(**kwargs)
        sub = self.kwargs['subject']
        ass_id = self.kwargs['id']
        no_id = self.kwargs['no']
        # print(no_id)
        context['choice'] = Choice.objects.filter( question__assignment = ass_id ,question__no = no_id)
        return context

class DoMatching(generic.TemplateView):
    template_name = 'student/matching.html'
    def get_context_data(self, **kwargs):
        context = super( DoMatching, self).get_context_data(**kwargs)
        # result = list()
        # sub = self.kwargs['subject']
        # ass_id = self.kwargs['id']
        # no_id = self.kwargs['no']
        # question = Question.objects.filter(assignment__subject__subject_code = sub , assignment = ass_id )
        # context['question'] = question
        # for i in question:
        #     if i.qtype == 'M':
        #         item = Matching.objects.filter(question=i)
        #         choice = MatchingChoice.objects.filter(question=i)
        #         result.append([item,choice])
        #     context['result'] = result
        # question = Question.objects.filter(assignment__subject__subject_code=self.kwargs['subject'],assignment=self.kwargs['assignment'])
        # context['question'] = question
        # for i in question:
        # sub = self.kwargs['subject']
        # ass_id = self.kwargs['id']
        # no_id = self.kwargs['no']
        # item = Matching.objects.filter(question__assignment = ass_id ,question__no = no_id)
        # choice = MatchingChoice.objects.filter(question__assignment = ass_id ,question__no = no_id)
        # result.append([item,choice])
        # context['result'] = result
        
        
        return context




class DoOpenended(generic.TemplateView):
    template_name = 'student/openended.html'
    def get_context_data(self, **kwargs):
        context = super( DoOpenended, self).get_context_data(**kwargs)
        code = self.kwargs['subject']
        ass_id = self.kwargs['id']
        no_id = self.kwargs['no']
        context['questions'] = Question.objects.filter(assignment = ass_id,no = no_id )
        return context

    



def create_assignment(request):
    return render(request, 'teacher/create-assignment.html')

def teacher_dashboard(request):
    return render(request, 'teacher/teacher-dashboard.html')