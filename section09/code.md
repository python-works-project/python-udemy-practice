```python
import csv
import os
from termcolor import colored

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
count = 1
color = 'green'
csv_name = "roboko.csv"
data_exist = False
rows = []

#  質問１→名前の取得
user_name = input(colored(msg1, color))

# CSV存在確認
if os.path.exists(csv_name):
    # 読み取り専用でファイルOPEN → rows に格納
    with open(csv_name, newline="", encoding="cp932") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    # count 降順ソート
    rows = sorted(rows, key=lambda x: int(x["count"]), reverse=True)
    # rows を使っておすすめ提示（YES/NO）
    for row in rows:
        answer = input(colored(msg2_2.format(row["shop_name"]), color)).strip().lower()
        if answer in ("yes", "y"):
            break

# 質問２→店名取得
shop_name = input(colored(msg2.format(user_name), color))

for row in rows:
    if shop_name.lower() == row["shop_name"].lower():
        row["count"] = str(int(row["count"]) + 1)
        data_exist = True
        break

if not data_exist:
    rows.append({"shop_name" : shop_name.capitalize(), "count" : "1"})

with open(csv_name, 'w', newline='') as f:
    fieldnames = ['shop_name', 'count']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(colored(msg3.format(user_name), color))
```
