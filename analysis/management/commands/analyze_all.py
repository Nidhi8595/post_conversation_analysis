from django.core.management.base import BaseCommand
from analysis.models import Conversation, ConversationAnalysis

class Command(BaseCommand):
    help = 'Analyze all conversations without analysis or with outdated analysis'

    def handle(self, *args, **kwargs):
        conversations = Conversation.objects.all()
        for convo in conversations:
            analysis_result = convo.analyze()
            ConversationAnalysis.objects.update_or_create(
                conversation=convo,
                defaults=analysis_result
            )
            self.stdout.write(self.style.SUCCESS(f"Analyzed Conversation ID {convo.id}"))
