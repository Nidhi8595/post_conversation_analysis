from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Post-Conversation Analysis API")
