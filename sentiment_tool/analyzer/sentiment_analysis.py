from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LinearRegression
import numpy as np

vectorizer = CountVectorizer()
regressor = LinearRegression()

# TODO: We're re-training the model every time we run the program, use joblib to save the model and load it
# TODO: Improve training data
# Function to train a basic model on sample data
def train():
    sample_texts = [
        "I absolutely hate this!", "This is terrible.", "I dislike it.",
        "It's not great.", "It's okay.", "Not bad.",
        "I like it.", "This is good.", "I love this!", "This is amazing!"
    ]
    sample_scores = [-1.0, -0.8, -0.6, -0.3, 0.0, 0.2, 0.5, 0.7, 0.9, 1.0]
    
    vectors = vectorizer.fit_transform(sample_texts)
    regressor.fit(vectors.toarray(), sample_scores)

# Function to predict sentiment score of new text
def predict_sentiment(text):
    vector = vectorizer.transform([text])
    score = regressor.predict(vector.toarray())[0]
    return max(min(score, 1.0), -1.0)  # Ensure the score is between -1 and 1
