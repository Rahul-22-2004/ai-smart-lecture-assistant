import requests
import os

API_KEY = os.getenv("LLM_API_KEY")

def transcribe_audio(file_path):
    url = "https://api.openai.com/v1/audio/transcriptions"

    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    with open(file_path, "rb") as audio_file:
        response = requests.post(
            url,
            headers=headers,
            files={"file": audio_file},
            data={"model": "whisper-1"}
        )

    result = response.json()

    # Debug-safe parsing
    if response.status_code != 200:
        raise Exception(f"Transcription API Error: {result}")

    # Some APIs return "text"
    if "text" in result:
        return result["text"]

    # Fallback: print full result for debugging
    raise Exception(f"Unexpected transcription response: {result}")