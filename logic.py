# logic.py
import requests
import pandas as pd
from translate import Translator
from pathlib import Path

translator = Translator(to_lang="ja")
DB_FILE = "cat_facts_db.csv"  # データベースとして使うCSV

def translate_to_japanese(text):
    try:
        return translator.translate(text)
    except Exception:
        return text

def get_cat_fact():
    url = "https://catfact.ninja/fact"
    response = requests.get(url)
    if response.status_code == 200:
        fact_en = response.json().get("fact", "猫の情報が取得できませんでした")
        return translate_to_japanese(fact_en)
    else:
        return "APIリクエストに失敗しました"

def get_multiple_cat_facts(count):
    facts = []
    for _ in range(count):
        facts.append(get_cat_fact())
    return facts

def save_facts_to_db(facts, db_file=DB_FILE):
    """CSVをデータベースとして追記保存"""
    df_new = pd.DataFrame(facts, columns=["Cat Fact"])
    
    # CSVが存在する場合は追記
    if Path(db_file).exists():
        df_existing = pd.read_csv(db_file)
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
        df_combined.to_csv(db_file, index=False, encoding="utf-8")
    else:
        df_new.to_csv(db_file, index=False, encoding="utf-8")
    
    return db_file

def load_db(db_file=DB_FILE):
    """CSVデータベースを読み込み"""
    if Path(db_file).exists():
        return pd.read_csv(db_file)
    else:
        return pd.DataFrame(columns=["Cat Fact"])
