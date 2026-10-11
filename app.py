
from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the improved sentiment-analysis model
MODEL_PATH = "model/sentiment_model_experiment.pkl"
model = joblib.load(MODEL_PATH)

MAX_TEXT_LENGTH = 500

SENTIMENT_INFO = {
    "positive": {
        "label": "Positive",
        "emoji": "😊",
        "color": "positive"
    },
    "neutral": {
        "label": "Neutral",
        "emoji": "😐",
        "color": "neutral"
    },
    "negative": {
        "label": "Negative",
        "emoji": "😞",
        "color": "negative"
    }
}


def generate_insight(sentiment, probability):
    """Generate a cautious, rule-based explanation."""

    if probability < 0.50:
        return (
            "The model is uncertain about this text. "
            "Review the probability breakdown before relying "
            "on the predicted sentiment."
        )

    if sentiment == "positive":
        return (
            "The model identifies a positive sentiment in this text. "
            "It may express satisfaction, appreciation, or enthusiasm."
        )

    if sentiment == "negative":
        return (
            "The model identifies a negative sentiment in this text. "
            "It may express dissatisfaction, criticism, or frustration."
        )

    return (
        "The model identifies a neutral sentiment in this text. "
        "The wording may be mainly factual or may express mixed "
        "or weak emotional signals."
    )


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    text = request.form.get("text", "").strip()

    if not text:
        return render_template(
            "index.html",
            error="Please enter some text to analyze.",
            input_text=""
        )

    if len(text) > MAX_TEXT_LENGTH:
        return render_template(
            "index.html",
            error=f"Please keep your text within {MAX_TEXT_LENGTH} characters.",
            input_text=text[:MAX_TEXT_LENGTH]
        )

    # Predict the sentiment
    predicted_sentiment = str(model.predict([text])[0]).lower()

    # Obtain probabilities for all model classes
    raw_probabilities = model.predict_proba([text])[0]
    class_probabilities = {
        str(label).lower(): float(probability)
        for label, probability in zip(
            model.classes_,
            raw_probabilities
        )
    }

    # Find the probability associated with the predicted class
    confidence = class_probabilities[predicted_sentiment]
    confidence_percentage = round(confidence * 100, 2)

    # Prepare the probability breakdown for the result page
    probability_breakdown = [
        {
            "name": SENTIMENT_INFO[sentiment]["label"],
            "key": sentiment,
            "emoji": SENTIMENT_INFO[sentiment]["emoji"],
            "probability": round(
                class_probabilities.get(sentiment, 0.0) * 100, 2
            )
        }
        for sentiment in ["positive", "neutral", "negative"]
    ]

    sentiment_info = SENTIMENT_INFO.get(
        predicted_sentiment,
        SENTIMENT_INFO["neutral"]
    )

    insight = generate_insight(
        predicted_sentiment,
        confidence
    )

    uncertain = confidence < 0.50

    return render_template(
        "result.html",
        text=text,
        sentiment=sentiment_info["label"],
        sentiment_key=predicted_sentiment,
        sentiment_emoji=sentiment_info["emoji"],
        sentiment_class=sentiment_info["color"],
        confidence=confidence_percentage,
        probabilities=probability_breakdown,
        insight=insight,
        uncertain=uncertain
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
