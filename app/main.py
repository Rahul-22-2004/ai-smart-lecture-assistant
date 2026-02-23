from fastapi import FastAPI, UploadFile, File
import os
import shutil
from app.speech import transcribe_audio
# from app.llm import generate_notes
from app.llm import generate_notes, generate_quiz, generate_flashcards

app = FastAPI()

UPLOAD_FOLDER = "uploads"

@app.get("/")
def home():
    return {"message": "AI Smart Lecture Assistant is running 🚀"}

@app.post("/upload")
async def upload_audio(file: UploadFile = File(...)):
    try:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # 🎤 Transcription
        transcript = transcribe_audio(file_path)

        # 🧠 AI generation
        notes = generate_notes(transcript)
        quiz = generate_quiz(transcript)
        flashcards = generate_flashcards(transcript)

        return {
            "filename": file.filename,
            "transcript": transcript,
            "notes": notes,
            "quiz": quiz,
            "flashcards": flashcards
        }

    except Exception as e:
        return {"error": str(e)}