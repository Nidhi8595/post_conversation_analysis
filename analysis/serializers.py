from rest_framework import serializers
from .models import Conversation, Message, ConversationAnalysis

class MessageSerializer(serializers.ModelSerializer):
    conversation = serializers.PrimaryKeyRelatedField(queryset=Conversation.objects.all())
    class Meta:
        model = Message
        fields = ['id', 'conversation', 'sender', 'text']

class ConversationSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ['id', 'title', 'created_at', 'messages']

class ConversationAnalysisSerializer(serializers.ModelSerializer):
    conversation = serializers.PrimaryKeyRelatedField(queryset=Conversation.objects.all())

    class Meta:
        model = ConversationAnalysis
        fields = [
            'conversation', 'clarity_score', 'relevance_score', 'accuracy_score',
            'completeness_score', 'sentiment', 'empathy_score', 'response_time',
            'resolution', 'escalation_needed', 'fallback_count', 'overall_score', 'created_at'
        ]
