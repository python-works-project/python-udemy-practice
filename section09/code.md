## 演習
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section8">◀️READMEに戻る</a>
</div>

```python
import csv
import os
from termcolor import colored

# --- メッセージテンプレート ---
msg1 = """\
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
こんにちは！私はROBOKOです。あなたの名前は何ですか？
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
msg2 = """\
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{}さん、どこのレストランが好きですか？
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
msg2_2 = """\
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
私のおすすめのお店は{}です。
このレストランは好きですか？(Yes/No)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
msg3 = """\
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{}さん、ありがとうございました。
良い一日を！さようなら。
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

# --- 初期設定 ---
color = 'green'
csv_name = "roboko.csv"
data_exist = False
rows = []

# --- 質問1：ユーザー名の取得 ---
user_name = input(colored(msg1, color))

# --- CSV が存在する場合は読み込み ---
if os.path.exists(csv_name):
    # CSV を読み込み、辞書のリスト rows に格納
    with open(csv_name, newline="", encoding="cp932") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    # count を整数として扱い、降順にソート
    rows = sorted(rows, key=lambda x: int(x["count"]), reverse=True)

    # ソートした rows を使っておすすめ提示（YES/NO）
    for row in rows:
        answer = input(colored(msg2_2.format(row["shop_name"]), color)).strip().lower()
        if answer in ("yes", "y"):
            break

# --- 質問2：ユーザーが好きなレストラン名を取得 ---
shop_name = input(colored(msg2.format(user_name), color))

# --- 既存データに同じ店名があるかチェック ---
for row in rows:
    if shop_name.lower() == row["shop_name"].lower():
        # 既存店の場合は count を +1
        row["count"] = str(int(row["count"]) + 1)
        data_exist = True
        break

# --- 新規店名の場合は追加 ---
if not data_exist:
    rows.append({"shop_name": shop_name.capitalize(), "count": "1"})

# --- CSV に上書き保存（ヘッダー + 全行） ---
with open(csv_name, 'w', newline='') as f:
    fieldnames = ['shop_name', 'count']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

# --- 終了メッセージ ---
print(colored(msg3.format(user_name), color))
```
<div align="right">
  <a href="../README.md#section8">◀️READMEに戻る</a>
</div>
