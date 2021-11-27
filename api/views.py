from django.http import response
from django.shortcuts import render
from quiz.models import Quiz, Question, Category, Choice
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import QuestionSerializer,QuizSerializer,CategorySerializer,ChoiceSerializer
# Create your views here.


class QuizApiView(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class CategoryApiView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class QuestionApiView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ChoiceApiView(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

class QuizCategoryApi(APIView):
    def get(self,request,format=None,**kwargs):
        quizzes = Quiz.objects.filter(category__id=kwargs['id'])
        serializer = QuizSerializer(quizzes, many=True)
        return Response(serializer.data)

class QuizDetail(generics.RetrieveAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuestionCategory(APIView):
    def get(self,request,format=None,**kwargs):
        questions = Question.objects.filter(quiz__category=kwargs['id'])
        serializer = QuestionSerializer(questions,many=True)
        return Response(serializer.data)


class QuestionDetial(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer 
