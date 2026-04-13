from django.urls import path
from .views import email, SuggestionCreateView, submit_data

urlpatterns = [
    path('email/', email),
    path('suggestion/', SuggestionCreateView.as_view()),
    path('list/', list_data),
    path('submit/', submit_data),
]
