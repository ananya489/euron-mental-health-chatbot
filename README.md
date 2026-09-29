Euron – AI-Powered Mental Health Chatbot



Euron is an AI-driven mental health support chatbot designed to analyze user emotions and stress levels using state-of-the-art Natural Language Processing (NLP) models. It provides empathetic, personalized responses through a clean and interactive web interface.

The system leverages Transformer-based deep learning models to understand emotional context and deliver supportive feedback, making it a powerful tool for early mental health screening and emotional well-being support.

🚀 Key Features

Emotion classification using HuggingFace Transformer models

Stress detection via sentiment analysis

Empathetic and personalized AI responses

RESTful Flask backend

Responsive web-based chat interface

🛠 Technology Stack

Backend: Python, Flask

AI / NLP: HuggingFace Transformers, PyTorch

Frontend: HTML, CSS, JavaScript

Modeling: Emotion classification & sentiment analysis pipelines

⚙️ How It Works

User enters a message through the web interface

The backend processes the text using Transformer-based NLP models

The system detects the user’s emotion and stress level

A supportive response is generated and displayed to the user

📦 Installation & Setup
git clone https://github.com/ananya489/euron-mental-health-chatbot.git
cd euron-mental-health-chatbot

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install flask torch transformers

# Run the application
python app.py


Open in your browser:

http://127.0.0.1:5000
Example

User:

I feel stressed and lonely

Euron:

Detects sadness and high stress and responds with empathetic, supportive guidance.
