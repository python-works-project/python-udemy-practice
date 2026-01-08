<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8" />
  <title>コード比較（左右に並べて表示）</title>
  <style>
    body {
      font-family: "Segoe UI", system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
      margin: 0;
      padding: 16px;
      box-sizing: border-box;
      background-color: #f5f5f5;
    }
    .container {
      display: flex;
      gap: 16px;
      align-items: flex-start;
    }
    .column {
      flex: 1;
      min-width: 0;
      background: #ffffff;
      border: 1px solid #ddd;
      border-radius: 4px;
      padding: 12px;
      box-sizing: border-box;
    }
    .column h2 {
      margin-top: 0;
      font-size: 16px;
      margin-bottom: 8px;
      border-bottom: 1px solid #eee;
      padding-bottom: 4px;
    }
    pre {
      margin: 0;
      overflow: auto;
      background-color: #272822;
      color: #f8f8f2;
      padding: 10px;
      border-radius: 4px;
      font-size: 13px;
      line-height: 1.5;
    }
    code {
      font-family: Consolas, "Courier New", monospace;
      white-space: pre;
    }
    /* 必要ならスマホ用に縦並びにする */
    @media (max-width: 800px) {
      .container {
        flex-direction: column;
      }
    }
  </style>
</head>
<body>
  <div class="container">
    <!-- 左カラム：自分で作成したコード -->
    <div class="column">
      <h2>自分で作成したコード</h2>
      <pre><code>import csv
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

print(colored(msg3.format(user_name), color))</code></pre>
    </div>

    <!-- 右カラム：生成したコード -->
    <div class="column">
      <h2>プロンプトをもとに生成したコード</h2>
      <pre><code>import csv
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
    main()</code></pre>
    </div>
  </div>
</body>
</html>
