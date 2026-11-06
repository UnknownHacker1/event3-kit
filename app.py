"""Event 3 kit: your wallet, and an AI you can ask about it.

Run it:  python -m streamlit run app.py
"""

import streamlit as st

import ai
import bank
import money

TEAM_NAME = "Your team name"  # TEAM TODO: change this

st.set_page_config(page_title=TEAM_NAME, layout="wide")


@st.cache_data(ttl=600, show_spinner="Calling the bank...")
def load():
    return bank.load_bank()


accounts, tx, source = load()
summary = money.summary(tx)
alerts = money.unusual_charges(tx)
facts = money.facts(accounts, tx)

st.title(TEAM_NAME)
st.caption(f"Data source: {source} · All data is fake · Not financial advice")

# ---------- Python does the math ----------
change = summary["change_pct"]
tiles = st.columns(3)
tiles[0].metric("Spent, last 30 days", f"${summary['spent']:,.2f}",
                delta=None if change is None else f"{change:+d}% vs the 30 days before", delta_color="inverse")
tiles[1].metric("Money in, last 30 days", f"${summary['came_in']:,.2f}")
tiles[2].metric("Unusual charges", len(alerts))

left, right = st.columns(2)
with left:
    st.subheader("Where it went")
    st.bar_chart(money.by_category(money.window(tx)))
with right:
    st.subheader("Unusual charges")
    st.caption(f"Python flags any charge {money.UNUSUAL_TIMES}x its category's average. The AI only explains.")
    st.dataframe(alerts, hide_index=True)

# ---------- AI does the talking ----------
st.subheader("Ask your wallet")
examples = ["Summarize my last 30 days in two sentences.",
            "Where did most of my money go?",
            "Explain my unusual charges and what I should check."]
clicked = None
for column, example in zip(st.columns(len(examples)), examples):
    if column.button(example, use_container_width=True):
        clicked = example

with st.form("ask", clear_on_submit=True):
    typed = st.text_input("Your question", placeholder="How much did I spend on dining?")
    sent = st.form_submit_button("Ask")

question = clicked or (typed if sent and typed.strip() else None)
if question:
    with st.chat_message("user"):
        st.write(question)
    with st.chat_message("assistant"), st.spinner("Thinking..."):
        st.write(ai.ask(question, facts).replace("$", r"\$"))

with st.expander("What the AI sees (this is everything we send it)"):
    st.code(facts, language=None)

# SILVER QUEST: budget coach. Delete the # on the next 5 lines, then set your own limits.
# BUDGETS = {"Dining": 150, "Coffee": 40, "Shopping": 120}
# spent = money.by_category(money.window(tx))
# for category, limit in BUDGETS.items():
#     if spent.get(category, 0) > limit:
#         st.warning(f"Over budget on {category}: ${spent[category]:,.2f} of ${limit}".replace("$", r"\$"))
