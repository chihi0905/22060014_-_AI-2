# app.py
import streamlit as st
import pandas as pd
from logic import get_multiple_cat_facts

st.title("🐱 ネコ知識app")
st.write("猫の豆知識をランダムに表示します！")

count = st.number_input("取得する猫の豆知識の数", min_value=1, max_value=10, value=3)

# 表示用の変数
facts = []

if st.button("取得！"):
    st.write("猫の豆知識を取得中…")
    facts = get_multiple_cat_facts(count)
    for i, fact in enumerate(facts, start=1):
        st.markdown(f"**{i}.** {fact}")

# CSV保存機能
if facts:
    df = pd.DataFrame(facts, columns=["Cat Fact"])
    csv_data = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 CSVファイルとして保存",
        data=csv_data,
        file_name="cat_facts.csv",
        mime="text/csv",
    )
