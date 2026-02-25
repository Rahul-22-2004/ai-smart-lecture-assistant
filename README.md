# 🎓 AI Smart Lecture Assistant

An AI-powered lecture intelligence system that converts spoken lecture audio into structured learning material — including transcripts, summarized notes, quizzes, flashcards, and downloadable PDF study resources.

This project was developed as part of the **AICTE + Edunet Foundation AI/ML Internship** to demonstrate practical application of Speech Recognition, Natural Language Processing, and Generative AI in education technology.

---

## 🚀 Project Overview

Students often struggle to listen, understand, and take notes simultaneously during lectures. This system solves that problem by automatically transforming lecture audio into structured study content using AI.

### ✨ Key Capabilities

* 🎤 **Speech-to-Text Transcription** using Whisper
* 📝 **AI Lecture Summarization & Structured Notes**
* ❓ **Automatic MCQ Quiz Generation**
* 🧠 **Flashcard Creation for Revision**
* 📄 **Downloadable PDF Study Material**
* 🌐 **Interactive Streamlit Web Interface**
* 📦 **REST API Backend with FastAPI**

---

## 🏗 System Architecture

```
Streamlit UI
    ↓
FastAPI Backend
    ↓
Whisper (ASR)
    ↓
Sarvam LLM (NLP + Generation)
    ↓
PDF Generator
    ↓
User Output (Notes, Quiz, Flashcards)
```

---

## 🛠 Tech Stack

### 🔹 Backend

* Python
* FastAPI
* Whisper (OpenAI Speech Recognition)
* Sarvam AI (LLM)
* ReportLab (PDF generation)

### 🔹 Frontend

* Streamlit

### 🔹 Supporting Tools

* FFmpeg
* Requests
* Python-dotenv

---

## 📂 Project Structure

```
ai-lecture-assistant/
│
├── app/
│   ├── main.py           # FastAPI server
│   ├── speech.py         # Whisper transcription
│   ├── llm.py            # AI content generation
│   ├── pdf_utils.py      # PDF generation
│
├── uploads/              # Uploaded audio files
├── outputs/              # Generated PDFs
├── streamlit_app.py      # Streamlit UI
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Installation & Setup

### ✅ 1. Clone Repository

```bash
git clone https://github.com/<your-username>/ai-smart-lecture-assistant.git
cd ai-smart-lecture-assistant
```

---

### ✅ 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### ✅ 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### ✅ 4. Install FFmpeg

Download from:

👉 https://www.gyan.dev/ffmpeg/builds/

Add `ffmpeg/bin` to system PATH.

Verify:

```bash
ffmpeg -version
```

---

### ✅ 5. Add Environment Variables

Create `.env` file:

```
LLM_API_KEY=your_sarvam_api_key
```

---

## ▶️ Running the Application

### 🔹 Start Backend

```bash
uvicorn app.main:app --reload
```

Backend available at:

```
http://127.0.0.1:8000
```

---

### 🔹 Start Frontend

```bash
streamlit run streamlit_app.py
```

Frontend available at:

```
http://localhost:8501
```

---

## 🎯 How to Use

1. Upload lecture audio file
2. Click **Process Lecture**
3. View:

   * Transcript
   * Notes
   * Quiz
   * Flashcards
4. Download PDF study material

---

## 📊 Example Output

The system generates:

* Clean transcript
* Structured academic notes
* Conceptual MCQs
* Revision flashcards
* Printable study PDF

---

## 🔮 Future Enhancements

* Multi-language lecture translation
* Lecture title & keyword extraction
* Difficulty level estimation
* Session history & storage
* Real-time lecture recording
* Cloud deployment & scaling
* Vector search for lecture retrieval

---

## 🎓 Internship Context

This project was developed during the **AICTE + Edunet Foundation AI & ML Internship** to showcase:

* End-to-end AI pipeline development
* API-based microservice architecture
* Generative AI application design
* Real-world EdTech problem solving

---

## 👨‍💻 Author

**Rahul D Gowda**
Final Year Computer Science Engineering Student
AI/ML & Backend Development Enthusiast

---

## ⭐ Acknowledgements

* Edunet Foundation
* AICTE Internship Program
* Sarvam AI Platform
* OpenAI Whisper

---

## 📜 License

This project is intended for academic and demonstration purposes.

---

⭐ If you found this project interesting, consider giving it a star!
