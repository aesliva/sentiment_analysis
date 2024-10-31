from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LinearRegression
import numpy as np
import re

vectorizer = CountVectorizer()
regressors = {aspect: LinearRegression() for aspect in ['graphics', 'music', 'terrain', 'combat', 'gameplay']}
overall_regressor = LinearRegression()

aspects = ['graphics', 'music', 'terrain', 'combat', 'gameplay']

# Dictionary of keywords associated with each aspect
aspect_keywords = {
    'graphics': ['graphics', 'visual', 'look', 'texture', 'vibe', 'aesthetic', 'shader'],
    'music': ['music', 'sound', 'audio', 'soundtrack', 'song', 'ost'],
    'terrain': ['terrain', 'landscape', 'map', 'world', 'environment', 'scenery', 'generation', 'region', 'biome'],
    'combat': ['combat', 'enemy', 'difficulty', 'boss', 'mob'],
    'gameplay': ['gameplay', 'mechanic', 'control', 'feature', 'system']
}

#TODO: need more sample data
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
    
    # Overall sentiment scores
    overall_scores = [0.3, 0.0, 0.6, -0.2, 0.3]
    
    vectors = vectorizer.fit_transform(sample_texts)
    
    for aspect in aspects:
        aspect_scores = [score[aspect] for score in sample_scores]
        regressors[aspect].fit(vectors.toarray(), aspect_scores)

    overall_regressor.fit(vectors.toarray(), overall_scores)

# Function to check if a text contains keywords related toaspect
def contains_aspect_keywords(text, aspect):
    text = text.lower()
    return any(keyword in text for keyword in aspect_keywords[aspect])

# Function to predict sentiment scores for all aspects
def predict_sentiment(text):
    vector = vectorizer.transform([text])
    scores = {}
    
    for aspect in aspects:
        # Only predict sentiment if aspect / related keywords mentioned
        if contains_aspect_keywords(text, aspect):
            score = regressors[aspect].predict(vector.toarray())[0]
            scores[aspect] = max(min(score, 1.0), -1.0)
        else:
            scores[aspect] = 0.0  # 0 if not mentioned
            
    return scores

def get_overall_sentiment(text):
    """Calculate overall sentiment using ML prediction"""
    vector = vectorizer.transform([text])
    score = overall_regressor.predict(vector.toarray())[0]
    return max(min(score, 1.0), -1.0)
