from dataclasses import field
from rest_framework import serializers

from .models import Answer, Category, Question, Quiz

class AnswerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Answer
        fields = ("answerText","isRight",)

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True,read_only=True)
    class Meta:
        model = Question
        fields =("title","answers","difficulty",)


class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    question_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Quiz
        fields = ('title', 'questions', 'question_count',)

    def get_question_count(self, obj):
        return obj.questions.count()


class CategorySerializer(serializers.ModelSerializer):
    quizzes = QuizSerializer(many=True, write_only=True)
    quiz_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'quizzes', 'quiz_count',)

    def get_quiz_count(self, obj):
        return obj.quizzes.count()
