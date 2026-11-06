# Notes for AI coding assistants

This file is for Copilot, Cursor, Claude Code, Codex, or whatever AI tool a student is using. Read it before changing anything.

## What this project is

A student Streamlit app for a FinTech Club workshop. It loads fake bank data, Python works out the numbers, and an AI (Google Gemini) explains them in plain English. The people using you are college students, many new to coding. Explain what you change in one or two plain sentences.

## Files

- `app.py`: the Streamlit screen. Run with `python -m streamlit run app.py` (port 8501).
- `bank.py`: loads accounts and transactions from Plaid Sandbox, or from the CSV files when there are no Plaid keys or `BANK=csv` is in `.env`.
- `money.py`: all the math. Totals, categories, unusual charges, and `facts()`, the text block sent to the AI.
- `ai.py`: sends `PROMPT` plus the facts to Gemini over plain REST with `requests`. `ask(question, facts)` always returns a string, never raises.
- `eval.py`: asks the bot questions with known answers and prints a score. Run with `python eval.py`.
- `prompt-lab/PROMPT-LAB.md`: a no-code exercise, not part of the app.

## Rules

1. **Python does the math, the AI does the talking.** Never have the AI calculate totals, averages, or percentages. Add the math to `money.py` and pass the result to the AI as text inside `facts()`.
2. **Never read, print, log, or commit `.env`.** Keys live only there. Never hard-code a key, never put one in a URL, never show one on screen. If the student pastes a key into the chat, tell them to make a new one.
3. **Keep `{facts}` and `{question}` in `PROMPT`.** `ask()` replaces them. Don't switch to `str.format`, because students type curly braces.
4. **Fake data only.** Don't add code that asks for real bank logins, card numbers, or account numbers.
5. **Keep it beginner-sized.** Plain functions, no classes, no new frameworks. Only add a package to `requirements.txt` if there's no simple way without it.
6. **Escape dollar signs** before `st.write` or `st.markdown` (`.replace("$", r"\$")`), or Streamlit renders them as math.
7. **Not financial advice.** The bot can explain spending. It must not recommend investments, crypto, loans, or skipping bills.

## After a change

Run `python eval.py` if you touched `ai.py` or `money.py`, and tell the student the score. If you changed the Gemini request, keep the 429 and error handling in `ask()`.
