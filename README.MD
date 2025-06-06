<h1 align="center">🧠 Sentiment Analysis API</h1>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.11-blue.svg">
  <img src="https://img.shields.io/badge/Django-4.x-green">
  <img src="https://img.shields.io/badge/DRF-3.14-red">
  <img src="https://img.shields.io/badge/NLP-TextBlob-yellow">
</p>

<div align="center">
  <strong>A lightweight REST API for classifying text sentiment as Positive, Negative, or Neutral.</strong>
</div>

<br>

## 🚀 Features

- 🔍 Analyze text sentiment using TextBlob (pre-trained NLP)
- 🧱 Built with Django REST Framework (DRF)
- 🐳 Dockerized for easy deployment
- ⚡ Fast and lightweight
- ✅ Easy to extend with other ML models

---

## 📦 Project Structure

sentiment_api/ <br>
├── api/ # Django app for sentiment API <br>
│ ├── views.py # View handling sentiment logic<br>
│ ├── serializers.py # Input/Output validation<br>
│ ├── urls.py # Route config<br>
├── sentiment_api/ # Project settings<br>
├── requirements.txt # Python dependencies<br>
├── Dockerfile # Docker setup<br>
├── .gitignore<br>
├── .env<br>
└── manage.py<br>
<br>
---<br>

# 📥 Installation & Usage

## 🧠 Sentiment Model
Uses TextBlob for sentiment analysis.
Polarity Range: [-1.0, 1.0]

## Classification Logic:
> 0.1 → Positive
< -0.1 → Negative
Otherwise → Neutral

## 💡 Future Improvements
🔁 Replace TextBlob with fine-tuned BERT/DistilBERT

📊 Add confidence scores

🧾 Swagger/OpenAPI documentation

🧪 Unit & integration tests

## 🧑‍💻 Author
Made with ❤️ by Dhruv Sharma
<p align="center"> 
<img src="https://forthebadge.com/images/badges/built-with-love.svg"> 
<img src="https://forthebadge.com/images/badges/made-with-python.svg"> 
</p>

### 🔧 Local Setup

```bash
git clone repo_url
cd sentiment_api
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python -m textblob.download_corpora
python manage.py migrate
python manage.py runserver
