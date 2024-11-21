import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { MatCardModule } from '@angular/material/card';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { MatProgressBarModule } from '@angular/material/progress-bar';
import { MatTableModule } from '@angular/material/table';

import { SentimentService } from './components/sentiment-analyzer/services/sentiment.service';
import { SentimentResponse } from './components/sentiment-analyzer/models/sentiment.interface';

@Component({
  selector: 'app-sentiment-analyzer',
  templateUrl: './sentiment-analyzer.component.html',
  styleUrls: ['./sentiment-analyzer.component.scss'],
  standalone: true,
  imports: [
    CommonModule,
    ReactiveFormsModule,
    MatCardModule,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule,
    MatProgressBarModule,
    MatTableModule
  ]
})
export class SentimentAnalyzerComponent {
  analyzerForm: FormGroup;
  result: SentimentResponse | null = null;
  isLoading = false;
  error: string | null = null;

  constructor(
    private fb: FormBuilder,
    private sentimentService: SentimentService
  ) {
    this.analyzerForm = this.fb.group({
      feedback: ['', Validators.required]
    });
  }

  onSubmit(): void {
    if (this.analyzerForm.valid) {
      this.isLoading = true;
      this.error = null;
      
      this.sentimentService.analyzeSentiment(this.analyzerForm.value.feedback)
        .subscribe({
          next: (response) => {
            this.result = response;
            this.isLoading = false;
          },
          error: (error) => {
            this.error = 'An error occurred while analyzing sentiment';
            this.isLoading = false;
          }
        });
    }
  }
}