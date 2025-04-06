# Swasthya Setu

A lightweight, modular healthcare information system designed for **low-resource environments** and **rural communities**, supporting **multilingual voice, text, and image inputs** to deliver clear, easy-to-understand medical guidance.

---

## 🚀 Features

- 🔊 **Voice, Text & Image Inputs**  
  Supports user queries via speech (Hindi/English), plain text, or medical document images.

- 🧠 **AI Language Processing**  
  Translates, simplifies, and summarizes medical language for low-literacy users using IndicBERT and mBART.

- 🔍 **Smart Information Retrieval**  
  Retrieves relevant advice from trusted medical databases (WHO, PMJAY, MedlinePlus) using intent-matching NLP models.

- 🗣️ **Accessible Outputs**  
  Converts responses into local language speech (TTS) and simple visuals (charts, dosage icons, etc.).

- 🌐 **Multilingual & Offline-First**  
  Designed to run efficiently in low-bandwidth or disconnected settings with multilingual capabilities.

---

## 📦 Project Structure

```bash
📁 backend/
├── app.py               # FastAPI or Flask server
├── bot_engine.py        # Query processor and retrieval logic
├── bot_data.pkl         # Precomputed embeddings and dataset

📁 frontend/
├── app.py               # Streamlit frontend

📁 model/
├── whisper/             # Speech-to-text
├── yolov5/              # Image processing
├── clip/                # Visual understanding

📁 utils/
├── nlp_utils.py         # Translation & summarization helpers
