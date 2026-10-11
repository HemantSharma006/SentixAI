# SentixAI — Sentiment Analysis Web App

SentixAI is a machine learning-powered web application that analyzes text and classifies its sentiment as **Positive, Neutral, or Negative**.

## Features

- Sentiment prediction using a trained machine learning pipeline
- Probability breakdown for all three sentiment classes
- Confidence-based insights
- Interactive and responsive web interface
- Input validation for empty and oversized text
- Flask backend with HTML, CSS, and JavaScript frontend

## Tech Stack

- **Language:** Python
- **Machine Learning:** scikit-learn, TF-IDF, Logistic Regression
- **Backend:** Flask
- **Frontend:** HTML, CSS, JavaScript
- **Model Storage:** Joblib
- **Deployment:** Render

## Project Structure

```text
Sentiment-Analysis/
├── app.py
├── requirements.txt
├── .python-version
├── model/
│   └── sentiment_model_experiment.pkl
├── templates/
├── static/
└── README.md
```

## Run Locally

1. Clone this repository.
2. Create and activate a Python virtual environment.
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the application:

   ```bash
   python app.py
   ```

5. Open `http://127.0.0.1:5000` in your browser.

## Model Evaluation

On the held-out test set, the selected model achieved approximately:

- **Accuracy:** 62%
- **Macro F1-score:** 0.62

Performance varies depending on the input text. Sarcasm, irony, and ambiguous statements may be classified incorrectly.

The small, manually labeled challenge set is exploratory and should not be treated as an official benchmark.

## Limitations

The model was trained on social-media-style text. Its performance on customer reviews, formal writing, and other domains may differ. Predicted probabilities are model estimates, not guarantees of correctness.

## Future Improvements

- Improve sarcasm and context detection
- Evaluate on additional labeled datasets
- Add a larger evaluation dashboard
- Expand support for different text domains

## Author

Hemant Sharma