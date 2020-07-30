import pdb

from django.contrib.auth.models import User
from rest_framework import serializers

from quiz.models import Quiz, Question, QUESTION_TYPES, Answer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class QuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    question_text = serializers.CharField()
    question_type = serializers.ChoiceField(choices=QUESTION_TYPES)
    answer_variants = serializers.CharField()
    quiz = serializers.StringRelatedField(read_only=True)

    def create(self, validated_data):
        return Question.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.question_text = validated_data.get('question_text', instance.question_text)
        instance.question_type = validated_data.get('question_type', instance.question_type)
        instance.save()
        return instance


class QuizSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    start_date = serializers.DateTimeField(read_only=True)
    end_date = serializers.DateTimeField()
    description = serializers.CharField()
    questions = QuestionSerializer(many=True)

    def create(self, validated_data):
        return Quiz.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class AnswerSerializer(serializers.Serializer):
    answer_text = serializers.CharField()
    user_id = serializers.IntegerField()
    question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all())

    def create(self, validated_data):
        return Answer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass

    def to_representation(self, instance):
        return {
            'question': instance.question.question_text,
            'answer': instance.answer_text
        }
