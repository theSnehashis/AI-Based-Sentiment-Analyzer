AI-Based Sentiment Analyzer

A simple and powerful NLP web application that analyzes user text and classifies sentiment as Positive, Negative, or Neutral using Hugging Face Transformers (DistilBERT).

🚀 Features

✔ Transformer-powered sentiment analysis (DistilBERT)

✔ Flask-based web interface

✔ Real-time text prediction

✔ Stores user predictions in SQLite database

✔ Clean, modern UI

✔ Easy to run locally

✔ Lightweight & fast

🧠 Tech Stack

Python 3.11

Flask

Hugging Face Transformers

Torch (CPU)

SQLite (SQLAlchemy ORM)

HTML, CSS, Jinja Templates

📂 Project Structure
AI-Based-Sentiment-Analyzer/
│
├── app.py
├── requirements.txt
├── db.sqlite3  (auto-created, NOT uploaded to GitHub)
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── result.html
│   └── history.html
│
└── static/
    └── style.css

⚙️ Installation & Setup
1️⃣ Clone the repository
git clone <repo-link>
cd AI-Based-Sentiment-Analyzer

2️⃣ Create a virtual environment
python -m venv venv
source venv/bin/activate   # For Windows: venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the app
python app.py

5️⃣ Open in browser
http://127.0.0.1:5000/

📊 How It Works

User enters text

Model tokenizes and processes using DistilBERT

Output label returned as Positive / Negative / Neutral

Prediction saved in SQLite database

User can view prediction history

📝 Future Improvements

Add API endpoint for mobile integration

Improve UI design

Add sentiment confidence graph

Dockerize the project

👨‍💻 Author

Snehashis Dalui
Python Developer Intern
Codec Technologies
