from django import forms
from .models import Assignment , Question

class CreateAssignment(forms.ModelForm):

    start_date = forms.DateField()
    end_date = forms.DateField()
    name = forms.CharField(max_length=50)
    publish = forms.BooleanField(required=False)
    check = forms.BooleanField(required=False)
    score = forms.FloatField()
    
    class Meta:
        model = Assignment
        fields = [
            'subject',
            'start_date',
            'end_date',
            'name',
            'publish',
            'check',
            'score',
        ]

class CreateQuestion(forms.ModelForm):
    no = forms.IntegerField()
    qtype = forms.CharField()
    topic = forms.CharField()
    score = forms.FloatField()
    class Meta:
        model = Question
        fields = [
            'assignment',
            'no',
            'qtype',
            'topic',
            'score',
        ]