from django import forms
from django.contrib.auth.models import User
from .models import *

# class ChoiceAnswer(forms.ModelForm):
#     CHOICES=[('select1','select 1'),
#          ('select2','select 2')]

#     answer = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
#     # answer = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea'}))
#     class Meta:
#         model =  StudentChoiceAnswer
#         fields = [
#             'answer'
#         ]
#     def save(self,commit=True):
#         ans = super(ChoiceAnswer, self).save(commit=False)   
#         ans.answer = self.cleaned_data['answer']
#         if commit:
#             ans.save()
        
#     return ans

class OpenEndedAnswer(forms.ModelForm):
    answer = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea'}))
    class Meta:
        model = StudentOpenEndedAnswer
        fields = [
            'answer'
        ]
    def save(self,commit=True):
        ans = super(OpenEndedAnswer, self).save(commit=False)   
        ans.answer = self.cleaned_data['answer']
        if commit:
            ans.save()
        
        return ans


