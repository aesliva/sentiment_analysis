# sentiment_tool/analyzer/urls.py
from django.urls import path
from .views import analyze, index

urlpatterns = [
    path('analyze/', analyze, name='analyze'),
    path('', index, name='index'),
]
