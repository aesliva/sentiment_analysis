from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LinearRegression
import numpy as np

vectorizer = CountVectorizer()
regressors = {aspect: LinearRegression() for aspect in ['graphics', 'music', 'terrain', 'combat', 'gameplay']}

aspects = ['graphics', 'music', 'terrain', 'combat', 'gameplay']

# Function to train a basic model on sample data
def train():
    sample_texts = [
        "The graphics are stunning but the combat is lacking.",
        "Amazing music and terrain, but the gameplay is weak.",
        "Gameplay is fun, graphics are okay, music is great.",
        "Terrible combat system, but the terrain is engaging.",
        "The terrain is bland, but the gameplay is addictive.",
    ]
    sample_scores = [
        {'graphics': 0.9, 'music': 0.0, 'terrain': 0.0, 'combat': -0.6, 'gameplay': 0.0},
        {'graphics': 0.0, 'music': 0.8, 'terrain': 0.7, 'combat': 0.0, 'gameplay': -0.5},
        {'graphics': 0.2, 'music': 0.8, 'terrain': 0.0, 'combat': 0.0, 'gameplay': 0.7},
        {'graphics': 0.0, 'music': 0.0, 'terrain': 0.6, 'combat': -0.8, 'gameplay': 0.0},
        {'graphics': 0.0, 'music': 0.0, 'terrain': -0.5, 'combat': 0.0, 'gameplay': 0.8},
    ]
    
    vectors = vectorizer.fit_transform(sample_texts)
    
    for aspect in aspects:
        aspect_scores = [score[aspect] for score in sample_scores]
        regressors[aspect].fit(vectors.toarray(), aspect_scores)

# Function to predict sentiment scores for all aspects
def predict_sentiment(text):
    vector = vectorizer.transform([text])
    scores = {}
    for aspect in aspects:
        score = regressors[aspect].predict(vector.toarray())[0]
        scores[aspect] = max(min(score, 1.0), -1.0)  # Ensure the score is between -1 and 1
    return scores

# Function to get overall sentiment
def get_overall_sentiment(scores):
    return sum(scores.values()) / len(scores)
