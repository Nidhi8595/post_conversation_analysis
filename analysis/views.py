from rest_framework import generics
from .models import Conversation, Message, ConversationAnalysis
from .serializers import ConversationSerializer, MessageSerializer, ConversationAnalysisSerializer

class ConversationListCreateView(generics.ListCreateAPIView):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

class MessageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class ConversationAnalysisListCreateView(generics.ListCreateAPIView):
    queryset = ConversationAnalysis.objects.all()
    serializer_class = ConversationAnalysisSerializer
