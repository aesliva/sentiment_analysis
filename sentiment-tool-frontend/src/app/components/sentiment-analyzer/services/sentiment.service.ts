import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../../../environments/environment';
import { SentimentResponse } from '../models/sentiment.interface';

@Injectable({
  providedIn: 'root'
})
export class SentimentService {
  private apiUrl = `${environment.apiUrl}/sentiment/analyze/`;

  constructor(private http: HttpClient) {}

  analyzeSentiment(feedback: string): Observable<SentimentResponse> {
    return this.http.get<SentimentResponse>(`${this.apiUrl}?feedback=${encodeURIComponent(feedback)}`);
  }
}