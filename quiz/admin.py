from django.contrib import admin
from .models import Quiz, Question, Option

class OptionInline(admin.TabularInline):
    model = Option
    extra = 4  # Number of extra option fields to display

class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created_by', 'created_at']
    search_fields = ['title', 'description']
    list_filter = ['created_by', 'created_at']
    date_hierarchy = 'created_at'

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'quiz', 'created_at']
    search_fields = ['text', 'quiz__title']
    list_filter = ['quiz', 'created_at']
    date_hierarchy = 'created_at'
    inlines = [OptionInline]

@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ['text', 'question', 'is_correct']
    search_fields = ['text', 'question__text']
    list_filter = ['question__quiz', 'is_correct']
