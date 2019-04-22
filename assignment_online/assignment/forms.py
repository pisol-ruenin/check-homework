from django import forms
from .models import Assignment

class CreateAssignment(forms.ModelForm):

    start_date = forms.DateField()
    end_date = forms.DateField()
    name = forms.CharField(max_length=50)
    publish = forms.BooleanField()
    check = forms.BooleanField()
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