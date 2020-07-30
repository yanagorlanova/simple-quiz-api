import datetime

from rest_framework import generics
from quiz.models import Quiz, Question
from quiz.permissions import IsAdminUserOrRestricted
from quiz.serializers import QuizSerializer, QuestionSerializer


class QuizList(generics.ListCreateAPIView):
    """
        Get the list of active quizes (end date is today or in the future) and create quiz.
    """
    permission_classes = [IsAdminUserOrRestricted]
    queryset = Quiz.objects.filter(end_date__gte=datetime.date.today(), start_date__lte=datetime.date.today())
    serializer_class = QuizSerializer


class QuizDetail(generics.RetrieveUpdateDestroyAPIView):
    """
        Retrieve, update or delete a quiz.
    """
    permission_classes = [IsAdminUserOrRestricted]
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    """
        Retrieve, update or delete a single question.
    """
    permission_classes = [IsAdminUserOrRestricted]
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
