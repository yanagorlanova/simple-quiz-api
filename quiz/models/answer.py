from django.db import models

from quiz.models import Question


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_id = models.IntegerField()
    answer_text = models.TextField()

    def __str__(self):
        return self.question.question_text + ' ' + self.answer_text
