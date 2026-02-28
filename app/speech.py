import requests
import os
import mimetypes

SARVAM_API_KEY = os.getenv("LLM_API_KEY")

def transcribe_audio(file_path):

    url = "https://api.sarvam.ai/v1/audio/transcriptions"

    headers = {
        "Authorization": f"Bearer {SARVAM_API_KEY}"
    }

    mime_type, _ = mimetypes.guess_type(file_path)

    if mime_type is None:
        mime_type = "audio/mpeg"

    with open(file_path, "rb") as audio_file:
        files = {
            "file": (os.path.basename(file_path), audio_file, mime_type)
        }

        data = {
            "model": "sarvam-stt"
        }

        response = requests.post(
            url,
            headers=headers,
            files=files,
            data=data
        )

    if response.status_code != 200:
        raise Exception(f"Sarvam Transcription Error: {response.text}")

    result = response.json()

    if "text" in result:
        return result["text"]

    raise Exception(f"Unexpected Sarvam response: {result}")