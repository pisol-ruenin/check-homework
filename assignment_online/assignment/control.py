from django_cron import CronJobBase, Schedule
from .models import *
from pythainlp import word_tokenize


class MyCronJob(CronJobBase):
    RUN_AT_TIMES = ['01:00']

    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'assignment.my_cron_job'    # a unique code

    def do(self):
        now = datetime.datetime.now().strftime('%Y-%m-%d')
        choice_answer = StudentChoiceAnswer.objects.filter(
            question__assignment__end_date=now)

        StudentDoAssignment.filter(assignment__end_date=now).update(finish=True)
        
        # chocie
        if len(choice_answer):
            for i in choice_answer:
                real_answer = ChoiceAnswer.objects.get(question=i.question)
                student_score = StudentChoiceScore()
                student_score.student = i.student
                student_score.question = i.question
                if i.answer == real_answer.no:
                    student_score.score = i.question.score
                else:
                    student_score.score = 0
                student_score.save()

        # matching
        matching_answer = StudentMatchingAnswer.objects.filter(
            question__assignment__end_date=now)

        if len(matching_answer):
            for i in matching_answer:
                real_answer = MatchingAnswer.objects.get(
                    question=i.question, item_no=i.answer_item)
                student_score = StudentMatchingScore()
                student_score.student = i.student
                student_score.question = i.question
                student_score.item_no = i.answer_item

                if i.answer_choice == real_answer.choice_no:
                    len_choice = len(
                        MatchingAnswer.objects.filter(question=i.question))
                    student_score.score = i.question.score / len_choice
                else:
                    student_score.score = 0
                    student_score.save()

        # open ended
        open_answer = StudentOpenEndedAnswer.objects.filter(
            question__assignment__end_date=now)

        if len(open_answer):
            for i in open_answer:
                keywords = OpenEndedKeywords.objects.fileter(
                    question=i.question)
                token = word_tokenize(i.answer)
                count = 0
                for j in keywords:
                    if j.keyword in token:
                        count += 1
                student_score = StudentOpenEndedScore()
                student_score.student = i.student
                student_score.question = i.question
                student_score.score = count * i.question.score/len(keywords)
                student_score.save()

        StudentDoAssignment.objects.filter(assignment__end_date=now).update(True)
