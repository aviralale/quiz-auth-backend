# quiz/views.py
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Quiz, Question, Option
from accounts.models import UserQuizHistory, QuizPerformance
from .serializers import QuizSerializer, QuestionSerializer, OptionSerializer
from accounts.serializers import UserQuizHistorySerializer

class QuizListCreateView(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        quiz = serializer.save(created_by=self.request.user)
        QuizPerformance.objects.get_or_create(quiz=quiz)

class QuizDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [permissions.IsAuthenticated]

class QuizPlayView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        quiz = Quiz.objects.get(pk=pk)
        score = request.data.get('score', None)
        
        if score is not None:
            # Create UserQuizHistory
            user_history = UserQuizHistory.objects.create(user=request.user, quiz=quiz, score=score)
            
            # Update QuizPerformance
            quiz_performance, created = QuizPerformance.objects.get_or_create(quiz=quiz)
            if created:
                quiz_performance.total_players = 1
                quiz_performance.average_score = score
            else:
                total_players = quiz_performance.total_players + 1
                average_score = (quiz_performance.average_score * quiz_performance.total_players + score) / total_players
                quiz_performance.total_players = total_players
                quiz_performance.average_score = average_score
            quiz_performance.save()
            
            return Response({'message': 'Quiz completed successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Score is required'}, status=status.HTTP_400_BAD_REQUEST)
