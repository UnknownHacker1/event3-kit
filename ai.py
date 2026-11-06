"""Event 3: talk to an AI. Send text, get text back.

Python works out every number first (money.py). The AI only puts them into words.
The PROMPT below belongs to your team's AI Prompter. Edit it, save, and ask again.
"""

import os

import requests
from dotenv import load_dotenv

MODEL = "gemini-3.5-flash-lite"  # free tier. To change it, set GEMINI_MODEL in .env

# ---------- AI PROMPTER: this part is yours ----------
PROMPT = """ROLE: You are a friendly money coach for a college student.

CONTEXT: These are the student's numbers. Python already did all the math, so use these totals exactly and never calculate your own.
{facts}

TASK: {question}

FORMAT: 2 to 4 short sentences in plain English. Mention dollar amounts.

LIMITS: Only use the numbers above. If the answer is not in them, say you don't know.
"""
# -----------------------------------------------------


def ask(question, facts):
    """Returns the AI's answer, or a plain message saying why there isn't one."""
    load_dotenv()
    key = os.getenv("GEMINI_API_KEY")
    if not key:
        return "AI is off: there's no GEMINI_API_KEY in .env yet. Everything Python worked out still shows above."

    prompt = PROMPT.replace("{facts}", facts).replace("{question}", question)
    model = os.getenv("GEMINI_MODEL") or MODEL
    try:
        response = requests.post(
            f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent",
            headers={"x-goog-api-key": key},  # the key goes in a header, never in the URL
            json={"contents": [{"parts": [{"text": prompt}]}]},
            timeout=60,
        )
    except requests.RequestException:
        return "Couldn't reach the AI. Check the Wi-Fi and try again."

    if response.status_code == 429:
        return "The AI is busy (free tier limit). Wait a minute and try again."
    if not response.ok:
        try:
            reason = response.json()["error"]["message"]
        except (ValueError, KeyError):
            reason = f"HTTP {response.status_code}"
        return f"AI error: {reason}"

    try:
        parts = response.json()["candidates"][0]["content"]["parts"]
        return "".join(part.get("text", "") for part in parts).strip() or "The AI sent back nothing. Try rewording."
    except (ValueError, KeyError, IndexError):
        return "The AI didn't answer that one. Try rewording the question."
