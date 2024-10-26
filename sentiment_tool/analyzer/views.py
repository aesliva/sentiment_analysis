from django.shortcuts import render

from django.http import JsonResponse
from .sentiment_analysis import predict_sentiment, train

# train the model separately and save it
train()

def analyze(request):
    if request.method == "GET":
        user_text = request.GET.get("feedback")
        if user_text:
            sentiment = predict_sentiment(user_text)
            response = {
                "feedback": user_text,
                "sentiment": "positive" if sentiment[0] == 1 else "negative"
            }
            return JsonResponse(response)
        return JsonResponse({"error": "No feedback provided"}, status=400)

def index(request):
    return render(request, 'analyzer/index.html')
