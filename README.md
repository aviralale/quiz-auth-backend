# Django Quiz App

A Django-based web application that allows users to create, play, and manage quizzes. Users can create quizzes with multiple questions, each having up to four options. The app also tracks user activity, including the quizzes created and played by users, and calculates the average scores.

## Features

- User authentication and registration
- Create, update, delete, and list quizzes
- Add multiple questions and options to each quiz
- Image support for questions and options
- Track user activity: quizzes created and played
- Calculate average scores for quizzes

## Tech Stack

- Python 3.12.1
- Django 5.0.6
- Django REST Framework
- SQLite (default) or PostgreSQL
- JavaScript / ReactJS + Vite (for frontend interaction)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/django-quiz-app.git
    cd django-quiz-app
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv env
    source env/bin/activate   # On Windows: env\Scripts\activate
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

    The application will be available at `http://127.0.0.1:8000/`.

## API Endpoints

The application provides RESTful API endpoints for managing quizzes, questions, options, and user activities. Here are some of the main endpoints:

- `GET /api/quizzes/`: List all quizzes
- `POST /api/quizzes/`: Create a new quiz
- `GET /api/quizzes/{id}/`: Retrieve a quiz by ID
- `PUT /api/quizzes/{id}/`: Update a quiz by ID
- `DELETE /api/quizzes/{id}/`: Delete a quiz by ID
- `POST /api/quizzes/{id}/play/`: Play a quiz

## Models

### Quiz

- `title`: CharField
- `description`: TextField
- `thumbnail`: ImageField
- `created_by`: ForeignKey (CustomUser)
- `created_at`: DateTimeField

### Question

- `quiz`: ForeignKey (Quiz)
- `text`: TextField
- `image`: ImageField
- `created_at`: DateTimeField

### Option

- `question`: ForeignKey (Question)
- `text`: CharField
- `image`: ImageField
- `is_correct`: BooleanField

### UserQuizHistory

- `user`: ForeignKey (CustomUser)
- `quiz`: ForeignKey (Quiz)
- `score`: IntegerField
- `completed_at`: DateTimeField

### QuizPerformance

- `quiz`: OneToOneField (Quiz)
- `total_players`: IntegerField
- `average_score`: FloatField

## Running Tests

To run the tests, use the following command:

```bash
python manage.py test
