from django.contrib import admin

from .models import Question, Quiz


class QuestionInline(admin.StackedInline):
    model = Question


class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

    def get_readonly_fields(self, request, obj=None):
        return ['start_date'] if obj else []


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question)
