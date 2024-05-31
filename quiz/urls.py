from django.urls import path
from .views import QuizListCreateView, QuizDetailView, QuizPlayView

urlpatterns = [
    path('', QuizListCreateView.as_view(), name='quiz-list-create'),
    path('<int:pk>/', QuizDetailView.as_view(), name='quiz-detail'),
    path('<int:pk>/play/', QuizPlayView.as_view(), name='quiz-play'),
]
