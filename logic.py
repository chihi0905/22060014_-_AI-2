# logic.py
import requests

def fetch_cat_fact(api_url="https://catfact.ninja/fact"):
    """ランダムな猫のトリビアを取得"""
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return data.get("fact", "No fact found.")
    else:
        return f"Error: {response.status_code}"

def fetch_multiple_cat_facts(count=3):
    """複数の猫トリビアを取得"""
    api_url = f"https://meowfacts.herokuapp.com/?count={count}"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return data.get("data", [])
    else:
        return [f"Error: {response.status_code}"]
