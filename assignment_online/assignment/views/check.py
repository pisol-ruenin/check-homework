from django.shortcuts import render
from django.views import generic
from ..models import *


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
        question = Question.objects.filter(
            assignment__subject__subject_code=self.kwargs['subject'],assignment=self.kwargs['assignment'])
        context['question'] = question
        for i in question:
            if i.qtype == 'O':
                answer = StudentOpenEndedAnswer.objects.get(question=i, student__user=self.request.user)
                real_answer = OpenEndedKeywords.objects.filter(question=i)
                result.append([i,answer,real_answer])
            elif i.qtype == 'C':
                answer = StudentChoiceAnswer.objects.get(question=i, student__user=self.request.user)
                choice = Choice.objects.filter(question=i)
                real_answer = ChoiceAnswer.objects.get(question=i)
                result.append([i,answer,choice,real_answer])
            elif i.qtype == 'M':
                answer = StudentMatchingAnswer.objects.filter(question=i, student__user=self.request.user)
                item = Matching.objects.filter(question=i)
                choice = MatchingChoice.objects.filter(question=i)
                real_answer = MatchingAnswer.objects.filter(question=i)
                result.append([i,answer,item,choice,real_answer])
        context['result'] = result
        context['assignment'] = Assignment.objects.get(pk=self.kwargs['assignment'])
        score_choice = StudentChoiceScore.objects.filter(question__assignment=self.kwargs['assignment'])
        score_matching = StudentMatchingScore.objects.filter(question__assignment=self.kwargs['assignment'])
        score_open = StudentOpenEndedScore.objects.filter(question__assignment=self.kwargs['assignment'])
        score = sum([i.score for i in score_choice])
        score += sum([i.score for i in score_matching])
        score += sum([i.score for i in score_open])
        print(score)
        context['score'] = score
        context['full_score'] = sum([i.score for i in question])
        return context




# class Test(generic.DeleteView):
#     def dispatch(self,*args,**kwargs):
#         answer = StudentChoiceAnswer.objects.filter(question__assignment__end_date='2019-04-17')
#         if len(answer):
#             for i in answer:
#                 real_answer = ChoiceAnswer.objects.get(question=i.question)
#                 if i.answer == real_answer.no:
#                     print(i.answer)
