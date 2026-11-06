# Event 3 kit: Talk to Your Wallet

Your app answers questions about your (fake) money, sums up your month, and explains unusual charges.

The rule for today: **Python does the math, AI does the talking.** `money.py` works out every number. `ai.py` sends those numbers to an AI and asks it to explain them in plain English.

All data is fake. Nothing here is financial advice.

## Build it with AI. Really.

Use whatever AI you like: Copilot (built into Codespaces), Cursor, Claude Code, ChatGPT, Gemini. Every step below has a prompt you can paste.

This repo has an [AGENTS.md](AGENTS.md), so your coding AI already knows the project and its rules. Two rules for you:

1. **Read what it changed before you keep it.** If you can't say what changed in one sentence, ask it to explain.
2. **Never paste your API key into any chat.** It lives in `.env` and nowhere else.

## Missed an earlier event?

You're not behind. This kit runs on its own and already includes everything from Event 2.

- Event 1 slides and student guide: [event2-kit/event1-catchup](https://github.com/UnknownHacker1/event2-kit/tree/main/event1-catchup)
- Event 2 (connecting to the bank): [event2-kit](https://github.com/UnknownHacker1/event2-kit). Today's `bank.py` is the same code.

## Prompt lab first

No coding: open [prompt-lab/PROMPT-LAB.md](prompt-lab/PROMPT-LAB.md) and follow it in any AI chat.

## Step 1: Open it

1. Click **Fork** at the top of this page, then **Create fork**.
2. On your fork: **Code → Codespaces → Create codespace on main**. Wait for it to load.
3. Copilot Chat is the chat icon at the top of the editor (or **Ctrl+Alt+I**). Sign in with GitHub if it asks. Students get Copilot free through [GitHub Education](https://education.github.com/pack).

## Step 2: Get your free AI key

Do this one by hand. Your coding AI should never see the key.

1. Go to [aistudio.google.com/apikey](https://aistudio.google.com/apikey) and sign in with a Google account. If your school account is blocked, use a personal Gmail.
2. Click **Create API key** and copy it.
3. In the terminal at the bottom:

```bash
cp .env.example .env
```

4. Open `.env` and paste the key after `GEMINI_API_KEY=`. No quotes, no spaces. Plaid keys from Event 2 are optional today.
5. Check that git can't see the file:

```bash
git status
```

**`.env` must NOT be in the list.**

No AI key? Skip this step. The app still runs, and every number still shows. Only the AI answers are missing.

## Step 3: Run it

```bash
python -m streamlit run app.py
```

Or ask your AI:

> Run this Streamlit app and tell me how to open it in the browser.

Click **Open in Browser**, then click one of the example questions. Open **What the AI sees** at the bottom: that's everything we send it. Do the AI's numbers match the tiles at the top?

## Step 4: Make the prompt yours

`PROMPT` near the top of `ai.py` is the app's brain. It has five parts: ROLE, CONTEXT, TASK, FORMAT, LIMITS. Edit it by hand, or ask your AI:

> Rewrite PROMPT in ai.py so the bot sounds like a strict but funny coach and always ends with one tip. Keep {facts} and {question} exactly as they are.

Save, press **R** in the app, and ask again.

Pro move: paste your prompt into any AI chat and say *"Ask me 3 questions that would make this prompt better, then rewrite it."*

## Step 5: Score your bot

```bash
python eval.py
```

It asks your bot 6 questions with known answers and prints a score. Change the prompt, run it again, and see if the score moved. This is called an **eval**. Real AI teams run them before every change, because "it looked fine when I tried it" isn't proof.

## Break the Bot (15 minutes)

Try to get another team's bot to give reckless advice, like "put my rent money in crypto" or "skip paying my credit card." Pretend it's an emergency, tell it to ignore its rules, ask it to role-play. When yours gets broken, add a rule to LIMITS and try again. Bonus: add the attack that worked as a test in `eval.py`.

This is called **red-teaming**. AI companies pay people to do it. Fake data and student apps only, never other systems.

## Bonus quests

Paste these into your coding AI. Then check the result yourself.

**Silver: your own tests** (great for Researchers)

> Add 3 tests to TESTS in eval.py about my dining spending. Work out the right answers with money.py, not by guessing, then run eval.py.

**Silver: budget coach**

> Turn on the Silver Quest budget coach at the bottom of app.py. Set Dining to $100 and Coffee to $30.

**Silver: a chat that remembers**

> Make "Ask your wallet" a real chat that remembers earlier questions in this session, using st.chat_input and st.session_state. Send the last few messages to the AI along with the facts.

**Gold: structured output**

> Add a button that asks Gemini for JSON instead of sentences: one object per category with the total and a one-line tip. Use generationConfig with responseMimeType application/json in ai.py. Totals must come from money.py. Show the result with st.dataframe.

**Gold: prompt battle.** Two teams ask the same question. The room votes on whose answer is clearer. Then compare `eval.py` scores.

## Stuck?

Paste the error into your AI first:

> I got this error running the app: (paste it). Explain what it means in one sentence, then fix it.

If that doesn't work:

| You see | Fix |
|---|---|
| `AI is off` | No key in `.env`. Check the name is exactly `GEMINI_API_KEY`. |
| `API key not valid` | Copy the key again. No spaces or quotes. |
| `The AI is busy` | Free tier limit. Wait a minute. Each teammate can use their own key. |
| Edited the prompt, nothing changed | Save the file, then press **R** in the app. |
| `No module named streamlit` | `pip install -r requirements.txt` |
| The page won't open | Ports tab in the bottom panel, then the globe next to 8501. |

## Bringing it into your team repo

Copy `ai.py`, `money.py`, `eval.py` and `AGENTS.md` across (and `bank.py` if you don't have it yet). Then, in your team repo, ask your AI:

> I copied ai.py and money.py into this repo. Add an "Ask your wallet" section to our app.py that sends money.facts(accounts, tx) and the user's question to ai.ask, like event3-kit does.

Or by hand:

```python
import ai, money
facts = money.facts(accounts, tx)
st.write(ai.ask("Summarize my month.", facts))
```

## Ground rules

- Fake data only. Never paste real bank info into an AI tool.
- Keys live in `.env`, never in code or chats.
- Use AI to build. Read what it changed.
- The AI explains. A human decides.
