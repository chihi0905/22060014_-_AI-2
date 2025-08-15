# logic.py
import requests
import pandas as pd

def get_cat_fact():
    """ランダムな猫の豆知識を1つ取得"""
    url = "https://catfact.ninja/fact"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("fact", "猫の情報が取得できませんでした")
    else:
        return "APIリクエストに失敗しました"

def get_multiple_cat_facts(count):
    """複数の猫の豆知識を取得"""
    facts = []
    for _ in range(count):
        facts.append(get_cat_fact())
    return facts

def save_facts_to_csv(facts, filename="cat_facts.csv"):
    """猫の豆知識をCSVとして保存"""
    df = pd.DataFrame(facts, columns=["Cat Fact"])
    df.to_csv(filename, index=False, encoding="utf-8")
    return filename

from googletrans import Translator

translator = Translator()

def translate_to_japanese(text):
    """英語のテキストを日本語に翻訳"""
    result = translator.translate(text, src='en', dest='ja')
    return result.text

