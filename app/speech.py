import requests
import os

SARVAM_API_KEY = os.getenv("LLM_API_KEY")

def transcribe_audio(file_path):
    url = "https://api.sarvam.ai/speech-to-text"

    headers = {
        "Authorization": f"Bearer {SARVAM_API_KEY}"
    }

    with open(file_path, "rb") as audio_file:
        files = {
            "file": audio_file
        }

        response = requests.post(url, headers=headers, files=files)

    if response.status_code != 200:
        raise Exception(f"Sarvam Transcription Error: {response.text}")

    result = response.json()

    # Safely extract transcript
    if "text" in result:
        return result["text"]

    if "transcript" in result:
        return result["transcript"]

    raise Exception(f"Unexpected Sarvam response: {result}")