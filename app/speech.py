import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("LLM_API_KEY"),
    base_url="https://api.sarvam.ai/v1"
)

def transcribe_audio(file_path: str):

    try:
        with open(file_path, "rb") as audio_file:

            transcription = client.audio.transcriptions.create(
                file=audio_file,
                model="whisper-1"   # IMPORTANT
            )

        return transcription.text

    except Exception as e:
        raise Exception(f"Sarvam Transcription Error: {str(e)}")