import { Component } from '@angular/core';
import { SentimentAnalyzerComponent } from './components/sentiment-analyzer/sentiment-analyzer.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  standalone: true,
  imports: [SentimentAnalyzerComponent]
})
export class AppComponent {
  title = 'Sentiment Analysis Tool';
}
