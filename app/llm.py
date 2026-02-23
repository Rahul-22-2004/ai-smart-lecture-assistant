import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(
    api_key=os.getenv("LLM_API_KEY"),
    base_url="https://api.sarvam.ai/v1" # Sarvam API endpoint
)


def generate_notes(transcript: str):

    prompt = f"""
    You are an academic lecture assistant.

    From the transcript below generate:

    1. Short summary (5 lines)
    2. Structured notes with headings and bullet points

    Transcript:
    {transcript}
    """

    response = client.chat.completions.create(
        model="sarvam-m",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content

def generate_quiz(transcript: str):
    prompt = f"""
    Generate 5 MCQ questions from this lecture transcript.

    Each question must include:
    - Question
    - 4 options (A,B,C,D)
    - Correct answer
    - Short explanation

    Transcript:
    {transcript}
    """

    response = client.chat.completions.create(
        model="sarvam-m",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )

    return response.choices[0].message.content

def generate_flashcards(transcript: str):
    prompt = f"""
    Generate 5 study flashcards from this lecture.

    Format:
    Q:
    A:

    Transcript:
    {transcript}
    """

    response = client.chat.completions.create(
        model="sarvam-m",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )

    return response.choices[0].message.content