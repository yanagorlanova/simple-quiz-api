from django.db import models

from .quiz import Quiz

QUESTION_TYPES = [
    ('text_field', 'Text field'),
    ('checkbox', 'Single choice'),
    ('radio_button', 'Multiple choice'),
]


class Question(models.Model):

    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    question_type = models.CharField(max_length=100, choices=QUESTION_TYPES)
    answer_variants = models.TextField(blank=True)

    def __str__(self):
        return self.question_text
