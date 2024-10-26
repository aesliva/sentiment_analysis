from django.shortcuts import render

from django.http import JsonResponse
from .sentiment_analysis import predict_sentiment, train

# train the model separately and save it
train()

def analyze(request):
    if request.method == "GET":
        user_text = request.GET.get("feedback")
        if user_text:
            sentiment_score = predict_sentiment(user_text)
            response = {
                "feedback": user_text,
                "sentiment_score": round(sentiment_score, 2),
                "sentiment": get_sentiment_label(sentiment_score)
            }
            return JsonResponse(response)
        return JsonResponse({"error": "No feedback provided"}, status=400)

def index(request):
    return render(request, 'analyzer/index.html')

def get_sentiment_label(score):
    if score < -0.6:
        return "Very Negative"
    elif score < -0.2:
        return "Negative"
    elif score < 0.2:
        return "Neutral"
    elif score < 0.6:
        return "Positive"
    else:
        return "Very Positive"
