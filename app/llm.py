import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

SARVAM_API_KEY = os.getenv("LLM_API_KEY")

client = OpenAI(
    api_key=SARVAM_API_KEY,
    base_url="https://api.sarvam.ai/v1"
)


def safe_chat_completion(prompt: str, temperature: float = 0.2):
    try:
        response = client.chat.completions.create(
            model="sarvam-m",
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        raise Exception(f"Sarvam LLM Error: {str(e)}")


# ---------------- NOTES ---------------- #

def generate_notes(transcript: str):

    prompt = f"""
You are an academic lecture assistant.

Return ONLY this structure:

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

    return safe_chat_completion(prompt, temperature=0.2)


# ---------------- QUIZ ---------------- #

def generate_quiz(transcript: str):

    prompt = f"""
Generate 5 MCQs in STRICT JSON format.

Return ONLY a JSON list like:

[
{{
"question": "",
"options": ["","","",""],
"answer": "",
"explanation": ""
}}
]

Do NOT add markdown.
Do NOT add text before or after JSON.

Transcript:
{transcript}
"""

    result = safe_chat_completion(prompt, temperature=0.3)

    # Ensure valid JSON
    try:
        quiz_json = json.loads(result)
        return quiz_json
    except:
        raise Exception(f"Invalid Quiz JSON from Sarvam: {result}")


# ---------------- FLASHCARDS ---------------- #

def generate_flashcards(transcript: str):

    prompt = f"""
Generate exactly 5 flashcards.

Return ONLY in this format:

Q: question
A: answer

No introductions.
No markdown.
No extra text.

Transcript:
{transcript}
"""

    return safe_chat_completion(prompt, temperature=0.3)