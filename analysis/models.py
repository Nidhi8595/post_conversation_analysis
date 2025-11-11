from django.db import models

# Models

class Conversation(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def analyze(self):
        messages = self.messages.all()
        # Dummy example: set scores based on message counts and simple analysis

        clarity_score = 4.5
        relevance_score = 4.5
        accuracy_score = 5.0
        completeness_score = 4.0
        sentiment = "positive"
        empathy_score = 4.0
        response_time = 2.5
        resolution = True
        escalation_needed = False
        fallback_count = 0
        overall_score = (clarity_score + relevance_score + accuracy_score + completeness_score) / 4

        return {
            'clarity_score': clarity_score,
            'relevance_score': relevance_score,
            'accuracy_score': accuracy_score,
            'completeness_score': completeness_score,
            'sentiment': sentiment,
            'empathy_score': empathy_score,
            'response_time': response_time,
            'resolution': resolution,
            'escalation_needed': escalation_needed,
            'fallback_count': fallback_count,
            'overall_score': overall_score,
        }


class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.CharField(max_length=20)  # 'user' or 'ai'
    text = models.TextField()

    def __str__(self):
        return f"{self.sender}: {self.text[:50]}"

class ConversationAnalysis(models.Model):
    conversation = models.OneToOneField(Conversation, on_delete=models.CASCADE, related_name='analysis')
    clarity_score = models.FloatField()
    relevance_score = models.FloatField()
    accuracy_score = models.FloatField()
    completeness_score = models.FloatField()
    sentiment = models.CharField(max_length=20)
    empathy_score = models.FloatField()
    response_time = models.FloatField()
    resolution = models.BooleanField()
    escalation_needed = models.BooleanField()
    fallback_count = models.IntegerField()
    overall_score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Analysis for Conversation {self.conversation_id}"
