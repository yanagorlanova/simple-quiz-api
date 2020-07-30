from django.urls import path
from quiz import views

urlpatterns = [
    path('quizes/', views.QuizList.as_view(), name='quiz-list'),
    path('quizes/<int:pk>/', views.QuizDetail.as_view(), name='quiz-detail'),
    path('questions/<int:pk>/', views.QuestionDetail.as_view(), name='question-detail'),
]
