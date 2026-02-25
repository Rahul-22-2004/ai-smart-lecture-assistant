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

    Return output ONLY in this format:

    SUMMARY:
    - bullet points

    NOTES:
    ### Heading
    - bullet points

    No greetings.
    No explanations.
    No extra text.

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
    Generate 5 MCQs.

    Format STRICTLY:

    Q:
    A)
    B)
    C)
    D)
    Answer:
    Explanation:

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
    Generate 5 flashcards.

    Format STRICTLY:

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