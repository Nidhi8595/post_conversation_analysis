# Registering models for admin interface
from django.contrib import admin
from .models import Conversation, Message, ConversationAnalysis

class MessageInline(admin.TabularInline):
    model = Message
    extra = 0

class ConversationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    inlines = [MessageInline]

class ConversationAnalysisAdmin(admin.ModelAdmin):
    list_display = ('conversation', 'clarity_score', 'relevance_score', 'overall_score', 'created_at')

admin.site.register(Conversation, ConversationAdmin)
admin.site.register(Message)
admin.site.register(ConversationAnalysis, ConversationAnalysisAdmin)
