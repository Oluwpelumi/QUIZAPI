from django.urls import path
from .views import *


urlpatterns = [
    path('', Quiz.as_view(), name='quiz'),
    path('answer/', Answer.as_view(), name='answer'),
    path('r/<str:topic>/', RandomQuestion.as_view(), name='random'),
    path('q/<str:topic>/', QuizQuestion.as_view(), name='quiz'),
]
