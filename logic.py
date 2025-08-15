# logic.py
import requests
import pandas as pd
from googletrans import Translator

# 翻訳器の準備
translator = Translator()

def translate_to_japanese(text):
    """英語のテキストを日本語に翻訳"""
    result = translator.translate(text, src='en', dest='ja')
    return result.text

def get_cat_fact():
    """ランダムな猫の豆知識を1つ取得（日本語に翻訳済み）"""
    url = "https://catfact.ninja/fact"
    response = requests.get(url)
    if response.status_code == 200:
        fact_en = response.json().get("fact", "猫の情報が取得できませんでした")
        return translate_to_japanese(fact_en)
    else:
        return "APIリクエストに失敗しました"

def get_multiple_cat_facts(count):
    """複数の猫の豆知識を取得（日本語）"""
    facts = []
    for _ in range(count):
        facts.append(get_cat_fact())
    return facts

def save_facts_to_csv(facts, filename="cat_facts.csv"):
    """猫の豆知識をCSVとして保存"""
    df = pd.DataFrame(facts, columns=["Cat Fact"])
    df.to_csv(filename, index=False, encoding="utf-8")
    return filename
