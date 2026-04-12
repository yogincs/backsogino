from django.urls import path
from .views import email, SuggestionCreateView

urlpatterns = [
    path('email/', email),
    path('suggestion/', SuggestionCreateView.as_view()),
]
