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

    # 1️⃣ Upload audio
    with open(file_path, "rb") as f:
        upload_response = requests.post(
            UPLOAD_URL,
            headers=headers,
            data=f
        )

    upload_json = upload_response.json()

    if "upload_url" not in upload_json:
        raise Exception(f"AssemblyAI Upload Error: {upload_json}")

    audio_url = upload_json["upload_url"]

    # 2️⃣ Request transcription
    transcript_response = requests.post(
        TRANSCRIPT_URL,
        json={"audio_url": audio_url},
        headers=headers
    )

    transcript_json = transcript_response.json()

    if "id" not in transcript_json:
        raise Exception(f"AssemblyAI Transcript Request Error: {transcript_json}")

    transcript_id = transcript_json["id"]

    # 3️⃣ Poll until complete
    while True:
        polling = requests.get(
            f"{TRANSCRIPT_URL}/{transcript_id}",
            headers=headers
        ).json()

        if polling["status"] == "completed":
            return polling["text"]

        if polling["status"] == "error":
            raise Exception(f"AssemblyAI Processing Error: {polling}")

        time.sleep(2)