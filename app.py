import streamlit as st
from logic import get_multiple_cat_facts, save_facts_to_db, load_db
import pandas as pd

st.title("🐱 ネコ豆知識app")

count = st.number_input("取得する猫の豆知識の数", min_value=1, max_value=10, value=3)

if st.button("取得！"):
    facts = get_multiple_cat_facts(count)
    st.write("取得した豆知識（日本語）:")
    for i, fact in enumerate(facts, start=1):
        st.markdown(f"**{i}.** {fact}")
    
    # データベースに保存
    db_file = save_facts_to_db(facts)
    st.success(f"{len(facts)}件をデータベースに保存しました: {db_file}")

if st.button("データベースを表示"):
    df_db = load_db()
    st.dataframe(df_db)

