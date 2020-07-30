import datetime
import pdb

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from quiz.models import Quiz, Question, Answer
from quiz.permissions import IsAdminUserOrRestricted
from quiz.serializers import QuizSerializer, QuestionSerializer, AnswerSerializer


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


class AnswerSaveList(APIView):
    def post(self, request, format=None):
        user_id = request.data['user_id']
        data = []
        for answer in request.data['answers']:
            data.append({
                'answer_text': answer['answer_text'],
                'user_id': user_id,
                'question': answer['question_id'],
            })
        serializer = AnswerSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnswerList(APIView):
    def get(self, request, user_id, format=None):
        answers = Answer.objects.filter(user_id=user_id)
        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data)
