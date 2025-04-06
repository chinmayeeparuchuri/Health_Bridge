# 🩺 Accessible Healthcare Information Bot

A **multilingual (English + Hindi)** healthcare Q&A assistant built to help users—especially from rural and underserved areas—access clear, structured medical advice via a conversational interface.

### 🏗️ Built with:
- 🌐 Streamlit frontend  
- 🧠 Flask API backend  
- 🤖 Sentence-Transformer embeddings  
- 📊 Pandas + Scikit-learn for data handling and similarity search  

---

## 🔧 Project Structure

```
Health_Bridge/
├── backend/
│   ├── app.py                # Flask API serving query responses
├── model/
│   ├── bot_data.pkl      # Pickled tuple: (DataFrame, embeddings, model)
│   └── bot_engine.py     # Query embedding + similarity search
├── data/
│   └── healthcare_dataset.csv   # Input data (multilingual health topics)
├── frontend/
│   └── streamlit_app.py      # Streamlit interface for user queries
├── healthcare_bot.py         # Script to build bot_data.pkl
└── README.md                 # 📘 You're here
```

---

## 🚀 How It Works

1. Preprocess multilingual healthcare data and generate sentence embeddings.  
2. Save the data, model, and embeddings as a pickle file (`bot_data.pkl`).  
3. Flask backend loads this file and serves answers to health queries.  
4. Streamlit frontend sends user queries and displays bilingual answers.

---

## 🛠 Installation & Setup

### 1️⃣ Clone the repo
```bash
git clone https://github.com/chinmayeeparuchuri/SwasthyaSetu.git
cd SwasthyaSetu
```

### 2️⃣ Create a virtual environment (recommended)
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

---

## 📦 Generate `bot_data.pkl`
Run this to build the vectorized knowledge base:

```bash
python healthcare_bot.py
```

✔️ This will:
- Load the dataset from `data/`
- Generate embeddings with `paraphrase-multilingual-MiniLM-L12-v2`
- Save everything as `backend/model/bot_data.pkl`

---

## 🧠 Start the Backend (Flask API)
```bash
cd backend
python app.py
```
📍 API available at: `http://127.0.0.1:5000/query`

---

## 🌐 Start the Frontend (Streamlit)
In a **new terminal**:

```bash
cd frontend
streamlit run streamlit_app.py
```

🌍 Interface at: `http://localhost:8501`

---

## 💬 Example Query

> **Question:** When should children be vaccinated?

✅ **Response:** A bilingual list of advice on child vaccination schedules, importance, and nearby health tips.

---

## 🗃 Dataset Format

| topic       | category         | description_en         | advice_en            | description_hi       | advice_hi            |
|-------------|------------------|-------------------------|----------------------|----------------------|----------------------|
| Burns       | Emergency Advice | Pain and fever in burns | Use clean water...   | जलन और बुखार...     | साफ पानी का प्रयोग... |
| Vaccination | Maternal Health  | Children need vaccines  | Follow schedule...   | बच्चों को टीका...    | समय पर टीका...        |

🔍 All columns are merged into a `corpus` for semantic search.

---

## 🤝 Contributions

Have ideas for:
- More languages?  
- Better embedding models?  
- Additional health topics?

We’d love your help! Open a pull request or raise an issue 🚀

---

## 🧾 License

Licensed under the **MIT License**.  
Use freely, adapt thoughtfully — always verify medical info with professionals.

---

## 🙏 Acknowledgements

- [Sentence-Transformers](https://www.sbert.net/)  
- [Streamlit](https://streamlit.io/)  
- [Flask](https://flask.palletsprojects.com/)  
- [Scikit-learn](https://scikit-learn.org/)
