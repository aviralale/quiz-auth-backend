from django.db import models
from accounts.models import CustomUser

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='quiz_thumbnails/', blank=True, null=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    performance = models.OneToOneField('accounts.QuizPerformance', related_name='related_quiz', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    QUESTION_TYPES = (
        ('text', 'Text'),
        ('image', 'Image'),
    )
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)  # For text-based question
    image = models.ImageField(upload_to='question_images/', blank=True, null=True)  # For image-based question
    question_type = models.CharField(max_length=10, choices=QUESTION_TYPES, default='text')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text if self.text else "Question"

class Option(models.Model):
    OPTION_TYPES = (
        ('text', 'Text'),
        ('image', 'Image'),
    )
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    text = models.CharField(max_length=255, blank=True, null=True)  # For text-based option
    image = models.ImageField(upload_to='option_images/', blank=True, null=True)  # For image-based option
    option_type = models.CharField(max_length=10, choices=OPTION_TYPES, default='text')
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text if self.text else "Option"
