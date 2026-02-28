import requests
import os

API_KEY = os.getenv("LLM_API_KEY")

def transcribe_audio(file_path):
    url = "https://api.openai.com/v1/audio/transcriptions"

    with open(file_path, "rb") as audio:
        response = requests.post(
            url,
            headers={
                "Authorization": f"Bearer {API_KEY}"
            },
            files={
                "file": audio
            },
            data={
                "model": "whisper-1"
            }
        )

    return response.json()["text"]