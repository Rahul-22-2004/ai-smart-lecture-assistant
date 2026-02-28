import requests
import os
import mimetypes

SARVAM_API_KEY = os.getenv("LLM_API_KEY")

def transcribe_audio(file_path):

    url = "https://api.sarvam.ai/v1/speech-to-text"

    headers = {
        "Authorization": f"Bearer {SARVAM_API_KEY}"
    }

    # Detect MIME type properly
    mime_type, _ = mimetypes.guess_type(file_path)

    if mime_type is None:
        mime_type = "audio/mpeg"  # fallback

    with open(file_path, "rb") as audio_file:
        files = {
            "file": (os.path.basename(file_path), audio_file, mime_type)
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