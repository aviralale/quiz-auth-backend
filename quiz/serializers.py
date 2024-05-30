from rest_framework import serializers
from .models import Quiz, Question, Option
from accounts.models import QuizPerformance, UserQuizHistory

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'text', 'image', 'is_correct']  # Include 'image' field

class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'text', 'image', 'options']  # Include 'image' field

    def create(self, validated_data):
        options_data = validated_data.pop('options')
        question = Question.objects.create(**validated_data)
        for option_data in options_data:
            Option.objects.create(question=question, **option_data)
        return question

class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'thumbnail', 'questions', 'created_by', 'created_at']
        read_only_fields = ['created_by', 'created_at']

    def create(self, validated_data):
        questions_data = validated_data.pop('questions')
        quiz = Quiz.objects.create(**validated_data)
        for question_data in questions_data:
            options_data = question_data.pop('options')
            question = Question.objects.create(quiz=quiz, **question_data)
            for option_data in options_data:
                Option.objects.create(question=question, **option_data)
        
        # Create or update QuizPerformance
        quiz_performance, created = QuizPerformance.objects.get_or_create(quiz=quiz)
        if not created:
            # Update QuizPerformance attributes if needed
            pass  # Add your logic to update QuizPerformance attributes if needed

        return quiz
