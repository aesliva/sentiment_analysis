from django.shortcuts import render

from django.http import JsonResponse
from .sentiment_analysis import predict_sentiment, train, get_overall_sentiment, aspects

# TODO: train the model separately and save it
train()

def analyze(request):
    if request.method == "GET":
        user_text = request.GET.get("feedback")
        if user_text:
            sentiment_scores = predict_sentiment(user_text)
            overall_score = get_overall_sentiment(sentiment_scores)
            response = {
                "feedback": user_text,
                "overall_score": round(overall_score, 2),
                "overall_sentiment": get_sentiment_label(overall_score),
                "aspect_scores": {aspect: round(score, 2) for aspect, score in sentiment_scores.items()},
                "aspect_sentiments": {aspect: get_sentiment_label(score) for aspect, score in sentiment_scores.items()}
            }
            return JsonResponse(response)
        return JsonResponse({"error": "No feedback provided"}, status=400)

def index(request):
    return render(request, 'analyzer/index.html', {'aspects': aspects})

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
