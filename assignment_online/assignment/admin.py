from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Subject)
admin.site.register(Lecturer)
admin.site.register(MemberSection)
admin.site.register(Assignment)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(ChoiceAnswer)
admin.site.register(OpenEndedKeywords)
admin.site.register(Matching)
admin.site.register(MatchingChoice)
admin.site.register(MatchingAnswer)
admin.site.register(StudentChoiceAnswer)
admin.site.register(StudentOpenEndedAnswer)
admin.site.register(StudentMatchingAnswer)
admin.site.register(StudentChoiceScore)
admin.site.register(StudentMatchingScore)
admin.site.register(StudentOpenEndedScore)