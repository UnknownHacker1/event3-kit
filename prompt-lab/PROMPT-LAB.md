# Prompt lab (20 minutes)

You need any free AI chat: Gemini, ChatGPT, or Claude. No coding.

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

Read the answer. Is it useful? Is it too long? Did it make anything up?

## Round 2: check its math (5 minutes)

In the same chat, ask these. Then compare with the answer key below.

1. What's the total I spent?
2. How much did I spend on Dining?
3. What was my biggest single purchase?

## Round 3: the five-part prompt (10 minutes)

Start a **new chat** and fill in this template. Paste the same table under CONTEXT.

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
- **LIMITS:** only use these transactions, don't give investment advice, say "I don't know" if the answer isn't here

Did the answer get better? Change one part at a time and see what moves.

## Answer key (worked out by Python, not AI)

| Question | Right answer |
|---|---|
| Total spent | **$984.49** (16 purchases) |
| Spent on Dining | **$247.06** (6 purchases) |
| Biggest single purchase | **ElectroMart, $489.99** on Oct 27 |
| Unusual charges | **ElectroMart $489.99** and **The Capital Grille $186.40**, each way above normal for its category |

If the AI got a number wrong, that's the lesson: **Python does the math, AI does the talking.**

## Share out (2 minutes)

Each team: read your best prompt out loud, and say one thing the AI got wrong.
