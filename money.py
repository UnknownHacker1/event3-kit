"""Python does the math. Every number the AI talks about comes from here.

Amounts follow Plaid's rule: positive = money out, negative = money in.
"Last 30 days" means the 30 days up to the newest transaction in the data.
"""

import pandas as pd

UNUSUAL_TIMES = 3  # flag a charge this many times bigger than its category's average


def _dated(tx):
    tx = tx.copy()
    tx["date"] = pd.to_datetime(tx["date"])
    return tx


def window(tx, days=30, skip=0):
    """Transactions from a stretch of days. skip=30 gives the 30 days before the last 30."""
    tx = _dated(tx)
    end = tx["date"].max() - pd.Timedelta(days=skip)
    return tx[(tx["date"] > end - pd.Timedelta(days=days)) & (tx["date"] <= end)]


def by_category(tx):
    """Money out per category, biggest first."""
    out = tx[tx["amount"] > 0]
    return out.groupby("category")["amount"].sum().round(2).sort_values(ascending=False)


def summary(tx):
    now, before = window(tx), window(tx, skip=30)
    spent = round(now.loc[now["amount"] > 0, "amount"].sum(), 2)
    spent_before = round(before.loc[before["amount"] > 0, "amount"].sum(), 2)
    return {
        "start": now["date"].min(), "end": now["date"].max(),
        "spent": spent,
        "came_in": round(-now.loc[now["amount"] < 0, "amount"].sum(), 2),
        "spent_before": spent_before,
        "change_pct": round((spent - spent_before) / spent_before * 100) if spent_before else None,
    }


def unusual_charges(tx):
    """Any charge at least 3x the average charge in its category."""
    out = _dated(tx)
    out = out[out["amount"] > 0]
    average = out.groupby("category")["amount"].transform("mean")
    flagged = out[out["amount"] >= UNUSUAL_TIMES * average].copy()
    flagged["category_average"] = average[flagged.index].round(2)
    flagged["date"] = flagged["date"].dt.strftime("%Y-%m-%d")
    return flagged[["date", "merchant", "category", "amount", "category_average"]].reset_index(drop=True)


def facts(accounts, tx):
    """Everything the AI is allowed to know, as plain text. No account numbers, nothing personal."""
    s = summary(tx)
    lines = [f"Period: last 30 days, {s['start']:%b %d} to {s['end']:%b %d, %Y}",
             f"Total spent: ${s['spent']:,.2f}",
             f"Total money in: ${s['came_in']:,.2f}",
             f"Spent in the 30 days before that: ${s['spent_before']:,.2f}"]
    if s["change_pct"] is not None:
        lines.append(f"Change in spending: {s['change_pct']:+d}%")

    lines.append("\nSpending by category, last 30 days:")
    lines += [f"- {category}: ${amount:,.2f}" for category, amount in by_category(window(tx)).items()]

    alerts = unusual_charges(tx)
    lines.append(f"\nUnusual charges (at least {UNUSUAL_TIMES}x their category average):")
    lines += [f"- {a.date} {a.merchant} ({a.category}): ${a.amount:,.2f}, category average ${a.category_average:,.2f}"
              for a in alerts.itertuples()] or ["- none"]

    lines.append("\nAccounts:")
    lines += [f"- {a.name} ({a.type}): ${a.balance:,.2f}" for a in accounts.itertuples()]

    recent = _dated(tx).head(25)
    lines.append("\nNewest 25 transactions (positive = money out, negative = money in):")
    lines += [f"- {t.date:%Y-%m-%d} {t.merchant} ({t.category}): ${t.amount:,.2f}" for t in recent.itertuples()]
    return "\n".join(lines)
