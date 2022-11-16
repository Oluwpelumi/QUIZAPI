from sre_constants import CATEGORY_UNI_DIGIT
from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Category)

  
# admin.site.register(Quizzes)
@admin.register(Quizzes)
class QuizAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title'
    ]



# admin.site.register(Questions)
class AnswerInlineModel(admin.TabularInline):
    model = Answers


@admin.register(Questions)
class QuestionAdmin(admin.ModelAdmin):

    list_display = [
        'title',
        'quiz',
        'date_created',
        'date_updated'
    ]

    inlines = [
        AnswerInlineModel,
        ]



# admin.site.register(Answers)
@admin.register(Answers)
class AnswerAdmin(admin.ModelAdmin):
        list_display = [
        'question',
        'answer_text',
        'is_correct',
    ]