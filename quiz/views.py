from unicodedata import category
from django.shortcuts import render
from rest_framework import generics

from .models import Category,Quiz,Question
from .serializers import CategorySerializer,QuizSerializer,QuestionSerializer
from django_filters.rest_framework import DjangoFilterBackend

# from rest_framework.permissions import IsAuthenticated
from .pagination import CurserPage

from .permissions import IsStaffUser

# Create your views here.


class QuizList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class QuizRead(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def get_queryset(self):
        category =self.kwargs['category'].capitalize()
        return Quiz.objects.filter(category__name =category)

class QuestionRead(generics.ListAPIView):
    queryset=Question.objects.all()
    serializer_class = QuestionSerializer
    # pagination_class =PageNumPage
    pagination_class =CurserPage
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = [ 'difficulty']
    # permission_classes = (IsAuthenticated,)
    permission_classes =(IsStaffUser,)

    def get_queryset(self):
        quiz =self.kwargs['quiz'].capitalize()
        return Question.objects.filter(quiz__title =quiz)