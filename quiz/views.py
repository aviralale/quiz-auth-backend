from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Quiz
from accounts.models import UserQuizHistory, QuizPerformance
from .serializers import QuizSerializer

class QuizListCreateView(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        quiz = serializer.save(created_by=self.request.user)
        # Create or update QuizPerformance
        quiz_performance, created = QuizPerformance.objects.get_or_create(quiz=quiz)
        if not created:
            # Update QuizPerformance attributes
            pass  # Add logic to update QuizPerformance attributes

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class QuizDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        quiz_instance = self.get_object()
        score = request.data.get('score', None)
        if score is not None:
            # Create UserQuizHistory
            UserQuizHistory.objects.create(user=request.user, quiz=quiz_instance, score=score)
            return Response({'message': 'Quiz completed successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Score is required'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
