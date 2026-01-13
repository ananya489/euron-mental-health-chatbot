from transformers import pipeline


emotion_model = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=True
)

sentiment_model = pipeline("sentiment-analysis")

def analyze(text):
    emotions = emotion_model(text)[0]
    top_emotion = max(emotions, key=lambda x: x['score'])

    sentiment = sentiment_model(text)[0]

    if sentiment['label'] == "NEGATIVE" and sentiment['score'] > 0.7:
        stress = "High"
    elif sentiment['label'] == "NEGATIVE":
        stress = "Medium"
    else:
        stress = "Low"

    tips = {
        "sadness": "Try talking to someone you trust or journaling.",
        "anxiety": "Practice deep breathing and grounding.",
        "anger": "Do physical activity or take a break.",
        "joy": "Keep doing what makes you happy!"
    }

    print("\nEmotion:", top_emotion['label'])
    print("Confidence:", round(top_emotion['score'] * 100, 2), "%")
    print("Stress Level:", stress)
    print("Tip:", tips.get(top_emotion['label'], "Relax and take a deep breath."))

text = input("How are you feeling today? ")
analyze(text)
