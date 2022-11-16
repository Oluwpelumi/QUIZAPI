from .models import *
from rest_framework import serializers


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quizzes
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = '__all__'


class RandomQuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Questions
        fields = ('id', 'title', 'answer')



class QuizQuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)
    quiz = QuizSerializer(read_only=True)

    class Meta:
        model = Questions
        fields = ('id', 'title', 'quiz', 'answer')