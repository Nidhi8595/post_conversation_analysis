from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Post-Conversation Analysis API")

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

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class AnalyzeConversationView(APIView):

    def post(self, request, pk):
        try:
            conversation = Conversation.objects.get(pk=pk)
        except Conversation.DoesNotExist:
            return Response({"error": "Conversation not found"}, status=status.HTTP_404_NOT_FOUND)

        analysis_data = conversation.analyze()

        # Save or update ConversationAnalysis
        analysis_obj, created = ConversationAnalysis.objects.update_or_create(
            conversation=conversation,
            defaults=analysis_data
        )

        serializer = ConversationAnalysisSerializer(analysis_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
