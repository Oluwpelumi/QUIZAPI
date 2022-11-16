from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from quizapp.models import Answers, Quizzes, Questions
from .serializers import AnswerSerializer, QuizSerializer, RandomQuestionSerializer, QuizQuestionSerializer
from rest_framework.views import APIView




# Create your views here.

class Quiz(generics.ListCreateAPIView):
    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()


class Answer(generics.ListCreateAPIView):
    serializer_class = AnswerSerializer
    queryset = Answers.objects.all()


class RandomQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        question = Questions.objects.filter(quiz__title=kwargs['topic']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)


class QuizQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        quiz = Questions.objects.filter(quiz__title=kwargs['topic']).order_by('?')
        serializer = QuizQuestionSerializer(quiz, many=True)
        return Response(serializer.data)
