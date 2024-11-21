export interface SentimentResponse {
    feedback: string;
    overall_score: number;
    overall_sentiment: string;
    aspect_scores: {
      [key: string]: number;
    };
    aspect_sentiments: {
      [key: string]: string;
    };
  }
  
  export interface AspectScore {
    aspect: string;
    score: number;
    sentiment: string;
  }