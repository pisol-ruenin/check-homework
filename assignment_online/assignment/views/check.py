from django.shortcuts import render
from django.views import generic
from ..models import *
from django.http import JsonResponse
from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.response import Response
from math import floor
import numpy as np

User = get_user_model()

class AssignmentScore(generic.TemplateView):
    template_name = 'student/assignment_score.html'

    def get_context_data(self, **kwargs):
        context = super(AssignmentScore, self).get_context_data(**kwargs)
        result = list()
        do = StudentDoAssignment.objects.get(student__user=self.request.user,assignment=self.kwargs['assignment'])
        question = Question.objects.filter(
            assignment__subject__subject_code=self.kwargs['subject'],assignment=self.kwargs['assignment'])
        context['question'] = question
        for i in question:
            if i.qtype == 'O':
                answer = None
                if do.finish:
                    answer = StudentOpenEndedAnswer.objects.get(question=i, student__user=self.request.user)
                real_answer = OpenEndedKeywords.objects.filter(question=i)
                result.append([i,answer,real_answer])
            elif i.qtype == 'C':
                answer = None
                if do.finish:
                    answer = StudentChoiceAnswer.objects.get(question=i, student__user=self.request.user)
                choice = Choice.objects.filter(question=i)
                real_answer = ChoiceAnswer.objects.get(question=i)
                result.append([i,answer,choice,real_answer])
            elif i.qtype == 'M':
                answer = None
                if do.finish:
                    answer = StudentMatchingAnswer.objects.filter(question=i, student__user=self.request.user)
                item = Matching.objects.filter(question=i)
                choice = MatchingChoice.objects.filter(question=i)
                real_answer = MatchingAnswer.objects.filter(question=i)
                result.append([i,answer,item,choice,real_answer])
            context['result'] = result

            if do.finish:
                score_choice = StudentChoiceScore.objects.filter(question__assignment=self.kwargs['assignment'])
                score_matching = StudentMatchingScore.objects.filter(question__assignment=self.kwargs['assignment'])
                score_open = StudentOpenEndedScore.objects.filter(question__assignment=self.kwargs['assignment'])
                score = sum([i.score for i in score_choice])
                score += sum([i.score for i in score_matching])
                score += sum([i.score for i in score_open])
            else:
                score = 0

            
        context['assignment'] = Assignment.objects.get(pk=self.kwargs['assignment'])
        
        print(score)
        context['score'] = score
        context['full_score'] = sum([i.score for i in question])
        return context

class StudentAssignmentScore(generic.TemplateView):
    template_name = 'teacher/student_assignment_score.html'

    def get_context_data(self, **kwargs):
        context = super(StudentAssignmentScore, self).get_context_data(**kwargs)
        result = list()
        do = StudentDoAssignment.objects.get(student__code=self.kwargs['std_code'],assignment=self.kwargs['assignment'])
        question = Question.objects.filter(
            assignment__subject__subject_code=self.kwargs['subject'],assignment=self.kwargs['assignment'])
        context['question'] = question
        for i in question:
            if i.qtype == 'O':
                answer = None
                s = 0
                if do.finish:
                    answer = StudentOpenEndedAnswer.objects.get(question=i, student__code=self.kwargs['std_code'])
                    s = StudentOpenEndedScore.objects.get(question=i,student__code=self.kwargs['std_code'])
                real_answer = OpenEndedKeywords.objects.filter(question=i)
                result.append([i,answer,real_answer,s])
            elif i.qtype == 'C':
                answer = None
                s = 0
                if do.finish:
                    answer = StudentChoiceAnswer.objects.get(question=i, student__code=self.kwargs['std_code'])
                    s = StudentChoiceScore.objects.get(question=i,student__code=self.kwargs['std_code'])
                choice = Choice.objects.filter(question=i)
                real_answer = ChoiceAnswer.objects.get(question=i)
                
                result.append([i,answer,choice,real_answer,s])
            elif i.qtype == 'M':
                answer = None
                s = 0
                if do.finish:
                    answer = StudentMatchingAnswer.objects.filter(question=i, student__code=self.kwargs['std_code'])
                    s = StudentMatchingScore.objects.filter(question=i,student__code=self.kwargs['std_code'])
                item = Matching.objects.filter(question=i)
                choice = MatchingChoice.objects.filter(question=i)
                real_answer = MatchingAnswer.objects.filter(question=i)
                result.append([i,answer,item,choice,real_answer,s])
            context['result'] = result

            if do.finish:
                score_choice = StudentChoiceScore.objects.filter(question__assignment=self.kwargs['assignment'])
                context['score_choice'] = score_choice
                score_matching = StudentMatchingScore.objects.filter(question__assignment=self.kwargs['assignment'])
                score_open = StudentOpenEndedScore.objects.filter(question__assignment=self.kwargs['assignment'])
                score = sum([i.score for i in score_choice])
                score += sum([i.score for i in score_matching])
                score += sum([i.score for i in score_open])
            else:
                score = 0

            
        context['assignment'] = Assignment.objects.get(pk=self.kwargs['assignment'])
        
        print(score)
        context['score'] = score
        context['full_score'] = sum([i.score for i in question])
        return context

class AssignmentReport(generic.TemplateView):
    template_name = 'teacher/report_assignment.html'

    def get_context_data(self, **kwargs):
        context = super(AssignmentReport, self).get_context_data(**kwargs)
        context['subject'] = self.kwargs['subject']
        context['assignment'] = self.kwargs['assignment']
        assignment = Assignment.objects.get(pk=self.kwargs['assignment'])
        context['data'] = assignment
        do = StudentDoAssignment.objects.filter(assignment=self.kwargs['assignment'])
        all_score=list()
        for i in do:
            if i.finish:
                score_choice = StudentChoiceScore.objects.filter(question__assignment=self.kwargs['assignment'],student=i.student)
                score_matching = StudentMatchingScore.objects.filter(question__assignment=self.kwargs['assignment'],student=i.student)
                score_open = StudentOpenEndedScore.objects.filter(question__assignment=self.kwargs['assignment'],student=i.student)
                score = sum([i.score for i in score_choice])
                score += sum([i.score for i in score_matching])
                score += sum([i.score for i in score_open])
            else:
                score = 0
            all_score.append(score)
        all_score = np.array(all_score)
        context['mean'] = all_score.mean()
        context['std'] = all_score.std()
        context['max'] = all_score.max()
        context['min'] = all_score.min()
        
        return context

class ChartScoreAssignment(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, *args, **kwargs):
        do = StudentDoAssignment.objects.filter(assignment=self.kwargs['assignment'])
        a = Assignment.objects.get(pk=self.kwargs['assignment'])
        item = [0 for i in range(int(a.score))]
        for i in do:
            if i.finish:
                score_choice = StudentChoiceScore.objects.filter(question__assignment=self.kwargs['assignment'],student=i.student)
                score_matching = StudentMatchingScore.objects.filter(question__assignment=self.kwargs['assignment'],student=i.student)
                score_open = StudentOpenEndedScore.objects.filter(question__assignment=self.kwargs['assignment'],student=i.student)
                score = sum([i.score for i in score_choice])
                score += sum([i.score for i in score_matching])
                score += sum([i.score for i in score_open])
            else:
                score = 0
            item[floor(score)] += 1
        labels = [i for i in range(int(a.score)+1)]
        default_items = item
        did = len([i for i in do if i.finish==True])
        notdid = len(list(do))-did
        print(did,notdid)
        data = {
            "labels":labels,
            "default":default_items,
            "did":did,
            "notdid":notdid,
        }
        return Response(data)

class SubjectReport(generic.TemplateView):
    template_name = 'teacher/report_subject.html'

    def get_context_data(self, **kwargs):
        context = super(SubjectReport, self).get_context_data(**kwargs)
        context['subject'] = Subject.objects.get(subject_code=self.kwargs['subject'])
        do = StudentDoAssignment.objects.filter(assignment__subject__subject_code=self.kwargs['subject'])
        all_score=list()
        for i in do:
            if i.finish:
                score_choice = StudentChoiceScore.objects.filter(student=i.student)
                score_matching = StudentMatchingScore.objects.filter(student=i.student)
                score_open = StudentOpenEndedScore.objects.filter(student=i.student)
                score = sum([i.score for i in score_choice])
                score += sum([i.score for i in score_matching])
                score += sum([i.score for i in score_open])
            else:
                score = 0
            all_score.append(score)
        all_score = np.array(all_score)
        context['mean'] = all_score.mean()
        context['std'] = all_score.std()
        context['max'] = all_score.max()
        context['min'] = all_score.min()

        return context

class ChartScoreSubject(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, *args, **kwargs):
        do = StudentDoAssignment.objects.filter(assignment__subject__subject_code=self.kwargs['subject'])
        a = Assignment.objects.all()
        a_score = sum([i.score for i in a])
        item = [0 for i in range(int(a_score))]
        for i in do:
            if i.finish:
                score_choice = StudentChoiceScore.objects.filter(student=i.student)
                score_matching = StudentMatchingScore.objects.filter(student=i.student)
                score_open = StudentOpenEndedScore.objects.filter(student=i.student)
                score = sum([i.score for i in score_choice])
                score += sum([i.score for i in score_matching])
                score += sum([i.score for i in score_open])
            else:
                score = 0
            item[floor(score)] += 1
        labels = [i for i in range(int(a_score)+1)]
        default_items = item
        data = {
            "labels":labels,
            "default":default_items,
        }
        return Response(data)

class StudentReportList(generic.ListView):
    template_name = 'teacher/student_report_list.html'
    model = MemberSection

    def get_context_data(self,**kwargs):
        context = super(StudentReportList, self).get_context_data(**kwargs)
        do = StudentDoAssignment.objects.filter(assignment=self.kwargs['assignment'])
        context['data'] = do
        return context

class AssignmentReportList(generic.ListView):
    template_name = 'teacher/assignment_report_list.html'
    model = Assignment

    def get_context_data(self,**kwargs):
        context = super(AssignmentReportList,self).get_context_data(**kwargs)
        assignment = Assignment.objects.filter(subject=self.kwargs['subject'])
        context['assignment'] = assignment
        return context

class EditChoiceScore(generic.UpdateView):
    model = StudentChoiceScore
    template_name = 'teacher/edit_score.html'
    fields = ['score']

class EditMatchingScore(generic.UpdateView):
    model = StudentMatchingScore
    template_name = 'teacher/edit_score.html'
    fields = ['score']

class EditOpenEndedScore(generic.UpdateView):
    model = StudentOpenEndedScore
    template_name = 'teacher/edit_score.html'
    fields = ['score']
    