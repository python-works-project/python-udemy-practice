## 97. CSVファイルへの書き込みと読み込み
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section8">◀️READMEに戻る</a>
</div>

**CSVファイルへの書き込み**
```python
import csv

# CSVファイルを書き込みモードで開く
with open('test.csv', 'w', newline='') as csv_file:
    fieldnames = ['Name', 'Count']　　　　　　　　　　　　　　　　# CSVの列名（ヘッダー）を定義
    Writer = csv.DictWriter(csv_file, fieldnames=fieldnames)　 # DictWriter：辞書形式で行を追加

    Writer.writeheader()                        # ヘッダー行を書き込む（Name,Count）
    Writer.writerow({'Name': 'A', 'Count': 1})  # 1行目を書き込む
    Writer.writerow({'Name': 'B', 'Count': 2})  # 2行目を書き込む
```
**CSVファイルの読み込み**
```python
# CSVファイルを読み込みモードで開く
with open('test.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)      # DictReader：各行を辞書として読み込める

    # 行ごとにループして出力
    for row in reader:
        print(row['Name'], row['Count'])   # row は {'Name': 'A', 'Count': '1'} のような辞書
        # 出力結果:
        # A 1
        # B 2
```
## ✨ 学習のまとめ
- ` DictWriter ` ： 辞書を渡してCSVに書き込める。キーがヘッダー名に対応
- ` DictReader ` ： CSVを辞書として読み込める。列名をキーにしてアクセス可能
- ` writeheader() ` ： ヘッダー行を自動で書き込む
- ` newline='' ` ： Windows環境で余分な改行を防ぐために必須

<div align="right">
  <a href="../README.md#section8">◀️READMEに戻る<a>
</div>




