import whisper
import os

# ⭐ Load once when app starts (important for performance)
print("Loading Whisper model...")
model = whisper.load_model("base")
print("Whisper model loaded ✅")


def transcribe_audio(file_path: str) -> str:
    """
    Convert audio file to text using Whisper
    """
    try:
        if not os.path.exists(file_path):
            return "File not found"

        result = model.transcribe(file_path)
        return result["text"]

    except Exception as e:
        return f"Error during transcription: {str(e)}"