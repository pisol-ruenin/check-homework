from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from ..models import *
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from ..models import *
from ..forms import *

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
        result = list()
        code = self.kwargs['subject']
        context['sub'] = Subject.objects.get(subject_code = code )
        context['subject'] = Assignment.objects.filter(subject__subject_code = code)
       
        m = MemberSection.objects.get(student__user=self.request.user,subject__subject_code=self.kwargs['subject'])

        context['c'] = StudentDoAssignment.objects.filter(student__user=self.request.user)
        print(self.request.user)
        for i in context['subject']:
            if i.subject.subject_code == m.subject.subject_code:
                if context['c'] :
                    checked = StudentDoAssignment.objects.get(student__user=self.request.user,assignment__name = i.name)
                    print(checked)
                    result.append([i,checked])
                else:
                    checked = 0 
                    result.append([i,checked])
        
         
        context['result'] = result

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


# class EditDoAssignment(generic.TemplateView):
#     template_name = 'student/edit_do_assignment.html'
#     def get_context_data(self, **kwargs):
#         context = super( EditDoAssignment, self).get_context_data(**kwargs)
#         code = self.kwargs['subject']
#         ass_id = self.kwargs['id']
#         context['questions'] = Question.objects.filter(assignment = ass_id)
#         print( context['questions'])
#         return context

class DoChoice(generic.TemplateView):
    template_name = 'student/choice.html'
    form_class = ChoiceAnswer
    model = StudentChoiceAnswer
    def get_context_data(self, **kwargs):
        context = super( DoChoice, self).get_context_data(**kwargs)
        sub = self.kwargs['subject']
        ass_id = self.kwargs['id']
        no_id = self.kwargs['no']
        # print(no_id)
        context['choice'] = Choice.objects.filter( question__assignment = ass_id ,question__no = no_id)
        return context

    # def get_success_url(self, *arg, **kwargs):
    #     code = self.kwargs['subject']
    #     ass_id = self.kwargs['id']
    #     no_id = self.kwargs['no']
    #     return reverse_lazy('assignment:do_assignment',kwargs={'subject': code,'id': ass_id})

    # def form_valid(self, form):
    #     code = self.kwargs['subject']
    #     ass_id = self.kwargs['id']
    #     no_id = self.kwargs['no']
    #     user = self.request.user
    #     # print(user)
    #     form.instance.student =  Student.objects.get(code = user)
    #     form.instance.question =  Question.objects.get(assignment = ass_id,no = no_id )
    #     return super(DoChoice, self).form_valid(form)

class DoMatching(generic.TemplateView):
    template_name = 'student/matching.html'
    def get_context_data(self, **kwargs):
        context = super( DoMatching, self).get_context_data(**kwargs)
        result = list()
        sub = self.kwargs['subject']
        ass_id = self.kwargs['id']
        no_id = self.kwargs['no']
        
        question = Question.objects.get(assignment__subject__subject_code = sub , assignment = ass_id ,no = no_id)
        context['question'] = question
        item = Matching.objects.filter(question__no = no_id)
        context['item'] = item
        for i in item:
            choice = MatchingChoice.objects.get(no = i.no)
            result.append([i,choice])
        context['result'] = result    
        return context

class DoOpenended(generic.CreateView):
    template_name = 'student/openended.html'
    form_class = OpenEndedAnswer
    model = StudentOpenEndedAnswer
    def get_context_data(self, **kwargs):
        context = super( DoOpenended, self).get_context_data(**kwargs)
        code = self.kwargs['subject']
        ass_id = self.kwargs['id']
        no_id = self.kwargs['no']
        context['questions'] = Question.objects.filter(assignment = ass_id,no = no_id )
        return context
    def get_success_url(self, *arg, **kwargs):
        code = self.kwargs['subject']
        ass_id = self.kwargs['id']
        no_id = self.kwargs['no']
        return reverse_lazy('assignment:do_assignment',kwargs={'subject': code,'id': ass_id})


    def form_valid(self, form):
        code = self.kwargs['subject']
        ass_id = self.kwargs['id']
        no_id = self.kwargs['no']
        user = self.request.user
        # print(user)
        form.instance.student =  Student.objects.get(code = user)
        form.instance.question =  Question.objects.get(assignment = ass_id,no = no_id )
        return super(DoOpenended, self).form_valid(form)

    
# class EditOpenended(generic.UpdateView):
#     template_name = 'student/editopenended.html'
#     # form_class = OpenEndedAnswer
#     model = StudentOpenEndedAnswer
#     def get_context_data(self, **kwargs):
#         context = super( DoOpenended, self).get_context_data(**kwargs)
#         code = self.kwargs['subject']
#         ass_id = self.kwargs['id']
#         no_id = self.kwargs['no']
#         context['questions'] = Question.objects.filter(assignment = ass_id,no = no_id )
#         return context


def create_assignment(request):
    return render(request, 'teacher/create-assignment.html')

def teacher_dashboard(request):
    return render(request, 'teacher/teacher-dashboard.html')