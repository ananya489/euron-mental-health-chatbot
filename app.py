from flask import Flask, request, jsonify, render_template
from transformers import pipeline

app = Flask(__name__)

# Load AI models
emotion_model = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=None
)

sentiment_model = pipeline("sentiment-analysis")

# Friendly responses
def get_tip(emotion):
    tips = {
        "sadness": "I’m here for you. Want to tell me what’s bothering you?",
        "anxiety": "Take a slow deep breath. You’re not alone.",
        "anger": "It’s okay to feel this way. Let’s slow down for a moment.",
        "joy": "That’s lovely to hear! Keep doing what makes you smile 💛"
    }
    return tips.get(emotion, "I’m here with you. Let’s talk.")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    text = data["message"]

    emotions = emotion_model(text)[0]
    top = max(emotions, key=lambda x: x["score"])

    sentiment = sentiment_model(text)[0]
    stress = "High" if sentiment["label"] == "NEGATIVE" else "Low"

    return jsonify({
        "emotion": top["label"],
        "stress": stress,
        "reply": get_tip(top["label"])
    })

app.run()
