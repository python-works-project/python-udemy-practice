今回の演習では、まず自分でプログラムを作成し、そのコードをもとに  
Copilot にプロンプトのお手本を出してもらいました。  
以下に掲載しているのは、そのプロンプトと、  
プロンプトをもとに Copilot が生成したコードです。  

生成AIにとって分かりやすいプロンプトの書き方を理解するとともに、  
自分のコードとの違いや改善点を確認しました。  

# プロンプト（[自分のコード](code.md)）
```
Python で ROBOKO というプログラムを作りたいです。
以下の仕様を満たすコードを作成してください。

【仕様】
1. 起動するとユーザーに名前を尋ねる（termcolor の colored() を使って緑色表示）

2. roboko.csv が存在する場合
   - DictReader で読み込み、rows（辞書のリスト）に格納する
   - count を整数として扱い、降順にソートする
   - ソートした rows を使って、shop_name を 1 件ずつ
     「私のおすすめのお店は○○です。このレストランは好きですか？(Yes/No)」
     と質問する
   - Yes/No の回答は count 更新には使わない（提示だけ）

3. roboko.csv が存在しない場合
   - rows は空のリストとして扱う

4. 最後にユーザーに好きなレストラン名を入力させる
   - rows の中に同じ shop_name があれば count を +1 する
   - 存在しなければ {"shop_name": 入力値, "count": "1"} を追加する
   - 大文字小文字は無視して比較する（lower()）

5. 最終的に rows 全体を roboko.csv に上書き保存する
   - ヘッダー（shop_name, count）を書き込む
   - writerows(rows) で全行を書き込む
   - count は文字列で保存する

6. 最後に「ありがとうございました。良い一日を！」と colored() で緑色表示する

【条件】
- コードは 1 ファイルで完結させる
- 日本語の店名も扱えるようにする
- termcolor を使う
- 変数名や処理の流れは読みやすく書く

以上を満たす Python コードを作成してください。
```

# Python コード（上記のプロンプトをもとにCopilotが作成したコード）
```python
import csv
import os
from termcolor import colored

def main():
    # --- 1. ユーザー名を尋ねる ---
    user_name = input(colored("あなたの名前を教えてください：", "green")).strip()

    csv_file = "roboko.csv"
    rows = []

    # --- 2. CSV が存在する場合の読み込み ---
    if os.path.exists(csv_file):
        with open(csv_file, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # count を整数として扱う
                row["count"] = int(row["count"])
                rows.append(row)

        # count の降順でソート
        rows.sort(key=lambda x: x["count"], reverse=True)

        # ソートした rows を使って質問
        for row in rows:
            msg = f"私のおすすめのお店は {row['shop_name']} です。このレストランは好きですか？(Yes/No)："
            answer = input(msg).strip().lower()
            # Yes/No は count 更新に使わない（提示だけ）
    else:
        # --- 3. CSV が存在しない場合 ---
        rows = []

    # --- 4. ユーザーに好きなレストランを尋ねる ---
    favorite = input(colored(f"{user_name}さんの好きなレストランを教えてください：", "green")).strip()

    # 大文字小文字を無視して比較
    favorite_lower = favorite.lower()
    found = False

    for row in rows:
        if row["shop_name"].lower() == favorite_lower:
            row["count"] += 1
            found = True
            break

    if not found:
        rows.append({"shop_name": favorite, "count": 1})

    # --- 5. CSV に上書き保存 ---
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        fieldnames = ["shop_name", "count"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()

        # count は文字列で保存
        for row in rows:
            writer.writerow({
                "shop_name": row["shop_name"],
                "count": str(row["count"])
            })

    # --- 6. 終了メッセージ ---
    print(colored("ありがとうございました。良い一日を！", "green"))


if __name__ == "__main__":
    main()
```
