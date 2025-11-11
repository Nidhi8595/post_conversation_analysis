from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/conversations/', views.ConversationListCreateView.as_view(), name='conversation-list-create'),
    path('api/messages/', views.MessageListCreateView.as_view(), name='message-list-create'),
    path('api/analysis/', views.ConversationAnalysisListCreateView.as_view(), name='analysis-list-create'),
]
