# Prompt lab (20 minutes)

You need any AI chat: Gemini, ChatGPT, Claude, Copilot. No coding.

**Fake data only.** Never paste your real bank statement, card numbers, or account numbers into any AI tool.

## Round 1: the lazy prompt (3 minutes)

Paste this into the chat, exactly as is:

```text
here's my spending how am I doing

date | merchant | category | amount
2026-10-21 | Aldi | Groceries | 75.45
2026-10-22 | Starbucks | Coffee | 6.93
2026-10-22 | Shell | Transport | 28.68
2026-10-24 | Bean There Cafe | Coffee | 5.67
2026-10-24 | Panda Express | Dining | 12.25
2026-10-24 | The Capital Grille | Dining | 186.40
2026-10-25 | Aldi | Groceries | 69.45
2026-10-25 | Taco Bell | Dining | 13.40
2026-10-26 | Starbucks | Coffee | 7.33
2026-10-27 | Cash App Pay - Food Truck | Dining | 10.14
2026-10-27 | ElectroMart | Shopping | 489.99
2026-10-28 | Publix | Groceries | 31.77
2026-10-29 | Starbucks | Coffee | 6.04
2026-10-29 | Taco Bell | Dining | 12.41
2026-10-29 | Steam | Entertainment | 16.12
2026-10-30 | Waffle House | Dining | 12.46
```

Read the answer. Is it useful, or is it a wall of generic advice? Did it guess things about you it can't know?

## Round 2: would you bet your rent on it? (5 minutes)

In the same chat, ask these, then check against the answer key at the bottom.

1. What's the total I spent?
2. How much did I spend on Dining?
3. What was my biggest single purchase?

Modern AIs often get these right. Some quietly write and run code to do it. Now try:

- Open **2 new chats** and ask "What's the total I spent?" with the table each time. Same number every time?
- Ask: *"Show me exactly how you got that total."* Could you prove it to someone?

A money app has to be right every time, for free, and provably. That's Python's job. The AI's job is explaining.

## Round 3: write a real brief (10 minutes)

Start a **new chat**. Write the prompt like a brief for a smart new coworker who knows nothing about you. Five parts help:

```text
ROLE: You are ...
CONTEXT: Here are my transactions: (paste the table)
TASK: ...
FORMAT: ...
LIMITS: ...
```

Ideas:

- **ROLE:** a friendly money coach for a college student
- **TASK:** point out the 2 charges that look unusual and say why
- **FORMAT:** 3 bullet points, under 50 words total
- **LIMITS:** only use these transactions, no investment advice, say "I don't know" if the answer isn't here

Then the pro move. Paste your prompt into a new chat and say:

```text
Here's a prompt I wrote. Ask me 3 questions that would make it better, then rewrite it.
```

Run the improved version. Better or worse than yours? Change one part at a time and see what moves.

## Answer key (worked out by Python)

| Question | Right answer |
|---|---|
| Total spent | **$984.49** (16 purchases) |
| Spent on Dining | **$247.06** (6 purchases) |
| Biggest single purchase | **ElectroMart, $489.99** on Oct 27 |
| Unusual charges | **ElectroMart $489.99** and **The Capital Grille $186.40**, each way above normal for its category |

## Share out (2 minutes)

Each team: read your best prompt out loud, and say one thing the AI got wrong or made up.
