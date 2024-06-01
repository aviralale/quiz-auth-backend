from rest_framework import serializers
from .models import CustomUser, UserQuizHistory, QuizPerformance
import uuid
from quiz.models import Quiz

class UserQuizHistorySerializer(serializers.ModelSerializer):
    quiz = serializers.SerializerMethodField()
    class Meta:
        model = UserQuizHistory
        fields = ['id', 'quiz', 'score', 'played_at']
    def get_quiz(self, obj):
        return obj.quiz.title
        

class QuizPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizPerformance
        fields = ['id', 'quiz', 'total_players', 'average_score']

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'is_active', 'is_staff', 'created_at', 'pfp', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, value):
        if not value:
            raise serializers.ValidationError("Password is required.")
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser(
            email=validated_data['email'],
            username=validated_data.get('username', str(uuid.uuid4())),
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            pfp=validated_data.get('pfp', 'user_avatar/default.jpg')
        )
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        instance.pfp = validated_data.get('pfp', instance.pfp)
        instance.save()
        return instance
