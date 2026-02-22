import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
print("API KEY:", os.getenv("LLM_API_KEY"))

client = OpenAI(api_key=os.getenv("LLM_API_KEY"))



def generate_notes(transcript: str):
    """
    Generate summary and structured notes from transcript
    """

    prompt = f"""
    You are an academic lecture assistant.

    From the transcript below generate:

    1. Short summary (5 lines)
    2. Structured notes with headings and bullet points

    Transcript:
    {transcript}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",   # can change later
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content