# Event 3 kit: Talk to Your Wallet

Your app answers questions about your (fake) money, sums up your month, and explains unusual charges.

The rule for today: **Python does the math, AI does the talking.** `money.py` works out every number. `ai.py` sends those numbers to an AI and asks it to explain them in plain English.

All data is fake. Nothing here is financial advice.

## Missed an earlier event?

You're not behind. This kit runs on its own and already includes everything from Event 2.

- Event 1 slides and student guide: [event2-kit/event1-catchup](https://github.com/UnknownHacker1/event2-kit/tree/main/event1-catchup)
- Event 2 (connecting to the bank): [event2-kit](https://github.com/UnknownHacker1/event2-kit). Today's `bank.py` is the same code.

## Prompt lab first

No coding: open [prompt-lab/PROMPT-LAB.md](prompt-lab/PROMPT-LAB.md) and follow it in any AI chat.

## Step 1: Open it

1. Click **Fork** at the top of this page, then **Create fork**.
2. On your fork: **Code → Codespaces → Create codespace on main**. Wait for it to load.

## Step 2: Get your free AI key

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

Click **Open in Browser**, then click one of the example questions. Open **What the AI sees** at the bottom: that's everything we send it.

## Step 4: Make the prompt yours (AI Prompter)

Open `ai.py`. The `PROMPT` near the top has five parts: ROLE, CONTEXT, TASK, FORMAT, LIMITS. Change one, save the file, press **R** in the app, and ask again.

Keep `{facts}` and `{question}` exactly as they are. That's where Python drops in the numbers and the question.

## Break the Bot (15 minutes)

Try to get another team's assistant to give reckless advice, like "put my rent money in crypto" or "skip paying my credit card." When yours gets broken, add a rule to LIMITS in your prompt and try again.

Fake data only, and only student apps. No other systems.

## Bonus quests

**Silver: test set.** Put `BANK=csv` in `.env`, restart the app, and ask your bot these 5 questions. Score it out of 5.

| Question | Right answer |
|---|---|
| How much did I spend in the last 30 days? | $2,676.83 |
| What was my biggest spending category? | Housing, $788.15 |
| How much did I spend on coffee? | $74.31 |
| Which charges look unusual? | ElectroMart $489.99 and The Capital Grille $186.40 |
| Am I spending more than the month before? | Yes, up 58% (from $1,698.02) |

**Silver: budget coach.** In `app.py`, delete the `#` on the Silver Quest lines at the bottom. Change the limits to your own.

**Gold: structured output.** Make the AI return JSON (a list of categories and totals) instead of sentences, and show it with `st.dataframe`. Hint: add `"generationConfig": {"responseMimeType": "application/json"}` next to `"contents"` in `ai.py`, ask for the exact keys you want, then `json.loads` the answer.

**Gold: prompt battle.** Two teams ask the same question. The room votes on whose answer is clearer.

## Stuck?

| You see | Fix |
|---|---|
| `AI is off` | No key in `.env`. Check the name is exactly `GEMINI_API_KEY`. |
| `API key not valid` | Copy the key again. No spaces or quotes. |
| `The AI is busy` | Free tier limit. Wait a minute. |
| Edited the prompt, nothing changed | Save the file, then press **R** in the app. |
| `No module named streamlit` | `pip install -r requirements.txt` |
| The page won't open | Ports tab in the bottom panel, then the globe next to 8501. |

## Bringing it into your team repo

Copy `ai.py` and `money.py` across (and `bank.py` if you don't have it yet). Then:

```python
import ai, money
facts = money.facts(accounts, tx)
st.write(ai.ask("Summarize my month.", facts))
```

## Ground rules

- Fake data only. Never paste real bank info into an AI tool.
- Keys live in `.env`, never in code.
- The AI explains. A human decides.
