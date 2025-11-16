from flask import Flask, render_template, request, redirect, url_for
from transformers import pipeline
from datetime import datetime
import os
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text
from sqlalchemy.orm import declarative_base, sessionmaker

# --- Config ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "db.sqlite3")
DATABASE_URL = f"sqlite:///{DB_PATH}"

# --- DB setup ---
engine = create_engine(DATABASE_URL, echo=False, future=True)
Base = declarative_base()

class Prediction(Base):
    __tablename__ = "predictions"
    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=False)
    label = Column(String(50), nullable=False)
    score = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)

# --- Model setup (load once) ---
print("Loading sentiment model (this may take a while)...")
sentiment = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
print("Model loaded.")

# --- Flask app ---
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    text = request.form.get("text", "").strip()
    if not text:
        return redirect(url_for("index"))
    # run model
    result = sentiment(text[:1000])  # limit length for safety
    label = result[0]["label"]
    score = result[0]["score"]
    # store in DB
    session = SessionLocal()
    pred = Prediction(text=text, label=label, score=str(score))
    session.add(pred)
    session.commit()
    session.close()
    return render_template("result.html", text=text, label=label, score=score)

@app.route("/history")
def history():
    session = SessionLocal()
    items = session.query(Prediction).order_by(Prediction.created_at.desc()).limit(100).all()
    session.close()
    return render_template("history.html", items=items)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
