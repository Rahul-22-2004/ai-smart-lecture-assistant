import requests
import os
import time

ASSEMBLYAI_API_KEY = os.getenv("ASSEMBLYAI_API_KEY")

UPLOAD_URL = "https://api.assemblyai.com/v2/upload"
TRANSCRIPT_URL = "https://api.assemblyai.com/v2/transcript"

headers = {
    "authorization": ASSEMBLYAI_API_KEY
}

def transcribe_audio(file_path):

    # Step 1: Upload file
    with open(file_path, "rb") as f:
        upload_response = requests.post(
            UPLOAD_URL,
            headers=headers,
            data=f
        )

    audio_url = upload_response.json()["upload_url"]

    # Step 2: Request transcription
    transcript_response = requests.post(
        TRANSCRIPT_URL,
        json={"audio_url": audio_url},
        headers=headers
    )

    transcript_id = transcript_response.json()["id"]

    # Step 3: Poll until done
    while True:
        polling = requests.get(
            f"{TRANSCRIPT_URL}/{transcript_id}",
            headers=headers
        ).json()

        if polling["status"] == "completed":
            return polling["text"]

        if polling["status"] == "error":
            raise Exception(f"AssemblyAI Error: {polling}")

        time.sleep(2)