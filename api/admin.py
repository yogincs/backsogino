from django.contrib import admin
from .models import Subscriber, Suggestion


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at')
    search_fields = ('email',)


@admin.register(Suggestion)
class SuggestionAdmin(admin.ModelAdmin):
    list_display = ('email', 'message', 'created_at')
    search_fields = ('email', 'message')
