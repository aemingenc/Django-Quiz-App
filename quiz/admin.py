from django.contrib import admin
from django.contrib.admin import TabularInline, StackedInline, site
from super_inlines.admin import SuperInlineModelAdmin, SuperModelAdmin
from.models import Answer, Category,Quiz,Question,Quiz


class AnswerInline(SuperInlineModelAdmin,admin.TabularInline):
    model=Answer
#KAÇ TANE CEVAP SATIRI OLSUN
    extra = 4

class QuestionInline(SuperInlineModelAdmin,admin.StackedInline):
    model=Question
    extra = 1
    inlines = (AnswerInline,)

class QuizAdmin(SuperModelAdmin):
    model=Quiz
    inlines = (QuestionInline,)

admin.site.register(Category)
admin.site.register(Quiz,QuizAdmin)
admin.site.register(Question)
admin.site.register(Answer)