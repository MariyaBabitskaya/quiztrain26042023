from django.contrib import admin
from .models import Question, Answer


# admin.site.register(Result)
class AnswerInLine(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInLine]



admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)