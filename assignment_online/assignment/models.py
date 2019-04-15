from django.db import models
from django.contrib.auth.models import User
from member.models import Student, Teacher

# Create your models here.


class Subject(models.Model):
    subject_code = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=20)
    no_section = models.IntegerField()

    def __str__(self):
        return self.subject_code


class Lecturer(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("subject", "lecturer"))

    def __str__(self):
        return self.subject.subject_code + '-' + self.lecturer.user.firstname


class MemberSection(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("subject", "student"))

    def __str__(self):
        return self.subject.subject_code + '-' + self.student.code


class Assignment(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    name = models.CharField(max_length=50)
    publish = models.BooleanField(default=False)
    check = models.BooleanField(default=False)

    def __str__(self):
        return self.subject.subject_code + '-' + self.name


class Question(models.Model):
    matching = 'M'
    choice = 'C'
    open_ended = 'O'
    question_type = (
        (matching, 'Matching'),
        (choice, 'Choices'),
        (open_ended, 'Open-ended')
    )
    no = models.IntegerField()
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    qtype = models.CharField(max_length=1, choices=question_type)
    topic = models.CharField(max_length=50)
    score = models.FloatField()

    class Meta:
        unique_together = (("no", "assignment"))

    def __str__(self):
        return self.assignment.subject.subject_code + ' ' + self.assignment.name + ' ' + self.qtype + ' no.' + str(self.no)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    no = models.IntegerField()
    txt = models.CharField(max_length=50)

    class Meta:
        unique_together = (("no", "question"))

    def __str__(self):
        return self.question.topic + '-' + str(self.no)


class ChoiceAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    no = models.IntegerField()

    class Meta:
        unique_together = (("no", "question"))

    def __str__(self):
        return self.question.topic + '-' + str(self.no)


class OpenEndedKeywords(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=20)

    class Meta:
        unique_together = (("question", "keyword"))

    def __str__(self):
        return self.question.topic + '-' + self.keyword


class Matching(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    no = models.IntegerField()
    txt = models.CharField(max_length=50)

    class Meta:
        unique_together = (("no", "question"))

    def __str__(self):
        return self.question.topic + '-' + str(self.no)


class MatchingChoice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    no = models.IntegerField()
    txt = models.CharField(max_length=50)

    class Meta:
        unique_together = (("no", "question"))

    def __str__(self):
        return self.question.topic + '-' + str(self.no)


class MatchingAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    item_no = models.ForeignKey(Matching, on_delete=models.CASCADE)
    choice_no = models.ForeignKey(MatchingChoice, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("choice_no", "item_no", "question"))

    def __str__(self):
        return self.question.topic + '-' + str(self.item_no)


class StudentChoiceAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("question", "student"))

    def __str__(self):
        return self.student.code + '-' + self.question.topic


class StudentOpenEndedAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("question", "student"))

    def __str__(self):
        return self.student.code + '-' + self.question.topic


class StudentMatchingAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_item = models.IntegerField()
    answer_choice = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("question", "student", "answer_item"))

    def __str__(self):
        return self.student.code + '-' + self.question.topic


class StudentChoiceScore(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    score = models.FloatField()

    class Meta:
        unique_together = (("student", "question"))

    def __str__(self):
        return self.student.code + '-' + self.question.topic


class StudentMatchingScore(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    item_no = models.IntegerField()
    score = models.FloatField()

    class Meta:
        unique_together = (("student", "question", "item_no"))

    def __str__(self):
        return self.student.code + '-' + self.question.topic


class StudentOpenEndedScore(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    score = models.FloatField()

    class Meta:
        unique_together = (("student", "question"))

    def __str__(self):
        return self.student.code + '-' + self.question.topic
