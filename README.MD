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

sentiment_api/
├── api/ # Django app for sentiment API
│ ├── views.py # View handling sentiment logic
│ ├── serializers.py # Input/Output validation
│ ├── urls.py # Route config
├── sentiment_api/ # Project settings
├── requirements.txt # Python dependencies
├── Dockerfile # Docker setup
├── .gitignore
├── .env
└── manage.py


---

## 📥 Installation & Usage

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
