from rest_framework import serializers
from quiz.models import Question,Category,Quiz, Choice


class CategorySerializer(serializers.ModelSerializer):
    class Meta:    
        model = Category
        fields = ('title',)


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('choice_text','is_correct')

class QuestionSerializer(serializers.ModelSerializer):
    choice = ChoiceSerializer(many=True,read_only=True)
    class Meta:
        model = Question
        fields = ('quiz','question_text','choice')

class QuizSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(many=True,read_only=True)
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Quiz
        fields = ('title','category','date_created','question')