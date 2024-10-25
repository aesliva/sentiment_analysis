from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

vectorizer = CountVectorizer()
classifier = MultinomialNB()

# Placeholder function to train a basic model on some sample data
def train():
    sample_texts = ["I love this game!", "This game is terrible.", "It's okay."]
    sample_labels = [1, 0, 1]
    vectors = vectorizer.fit_transform(sample_texts)
    classifier.fit(vectors, sample_labels)

# Function to predict sentiment of new text
def predict_sentiment(text):
    vector = vectorizer.transform([text])
    return classifier.predict(vector)
