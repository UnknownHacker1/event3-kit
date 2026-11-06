"""Score your bot like a real AI team: ask it questions with known answers, count the right ones.

Run it:  python eval.py

It always uses the fake CSV bank, so the right answers never change.
Change the prompt in ai.py, run this again, and see if your score went up or down.
Add your own tests to TESTS below. Each one is: question, then words or numbers the answer must contain.
A | means "any of these is fine".
"""

import os
import time

from dotenv import load_dotenv

os.environ["BANK"] = "csv"  # same data every run, so the score means something

import ai
import bank
import money

TESTS = [
    ("How much did I spend in the last 30 days?", ["2676.83"]),
    ("What was my biggest spending category?", ["housing", "788.15"]),
    ("How much did I spend on coffee?", ["74.31"]),
    ("Which charges look unusual?", ["electromart", "capital grille"]),
    ("Am I spending more than the month before? By what percent?", ["58"]),
    ("What's my Social Security number?", ["don't know|don't have|not in|can't"]),  # not in the data, so it should say so
]


def clean(text):
    # "$2,676.83" and "2676.83" should both count, and so should curly apostrophes
    return text.lower().replace(",", "").replace("$", "").replace("’", "'")


load_dotenv()
if not os.getenv("GEMINI_API_KEY"):
    raise SystemExit("No GEMINI_API_KEY in .env yet, so there's no bot to test. Add your key first (README, Step 2).")

accounts, tx, _ = bank.load_bank()
facts = money.facts(accounts, tx)

score = 0
for question, must_have in TESTS:
    answer = ai.ask(question, facts)
    missing = [word for word in must_have
               if not any(clean(option) in clean(answer) for option in word.split("|"))]
    passed = not missing
    score += passed
    print(("PASS " if passed else "FAIL ") + question)
    print("     " + answer.replace("\n", " "))
    if missing:
        print("     missing: " + ", ".join(missing))
    print()
    time.sleep(1)  # be gentle with the free tier

print(f"Score: {score}/{len(TESTS)}")
