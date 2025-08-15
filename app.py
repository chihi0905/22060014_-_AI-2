# app.py
from logic import fetch_cat_fact, fetch_multiple_cat_facts

def main():
    print("🐱 猫トリビアアプリ 🐱")
    print("1: ランダムな猫トリビアを取得")
    print("2: 複数の猫トリビアを取得")
    choice = input("選択してください (1 or 2): ")

    if choice == "1":
        fact = fetch_cat_fact()
        print("\n✨ 猫トリビア ✨")
        print(fact)

    elif choice == "2":
        count = input("いくつ取得しますか？（数字）: ")
        if not count.isdigit():
            print("⚠ 数字を入力してください")
            return
        facts = fetch_multiple_cat_facts(int(count))
        print("\n✨ 猫トリビア ✨")
        for i, f in enumerate(facts, 1):
            print(f"{i}. {f}")
    else:
        print("⚠ 無効な選択です")

if __name__ == "__main__":
    main()
