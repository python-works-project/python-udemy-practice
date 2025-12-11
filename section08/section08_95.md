## 95. 書き込み読み込みモード
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section8">◀️READMEに戻る</a>
</div>

```python
# 複数行の文字列を準備
s = """\
AAA
BBB
CCC
DDD
EEE
"""

# 'w' モード：新規作成／上書き
with open('test.txt', 'w') as f:
    f.write(s)
    # print(f.read())              # 'w' モードは書き込み専用なので読み込み不可(エラー)

# 'r' モード：読み込み専用
with open('test.txt', 'r') as f:
    print(f.read())                # ファイル全体を読み込んで表示

# 'w+' モード：書き込み＋読み込み（既存内容は消える）
with open('test.txt', 'w+') as f:
    f.write(s)                     # 書き込み
    f.seek(0)                      # ポインタを先頭に戻す
    print(f.read())                # 書き込んだ内容を読み込んで表示

# 'w+'：開いた直後に読み込み
with open('test.txt', 'w+') as f:
    print(f.read())                # 開いた時点で内容は消えているので空文字列が返る

# 'r+' モード：読み込み＋書き込み（既存内容を保持）
with open('test2.txt', 'r+') as f:
    print(f.read())                # test2.txt が存在しない場合は FileNotFoundError になる

# 'r+' モードで test.txt を開く
with open('test.txt', 'r+') as f:
    print(f.read())                # 既存の内容を読み込む
    f.seek(0)                      # ポインタを先頭に戻す
    f.write(s)                     # 内容を上書き（先頭から書き込む）
```
## ✨ 学習のまとめ
- ` w ` : 書き込み専用。既存ファイルは内容が消える。読み込み不可。
- ` r ` : 読み込み専用。ファイルが存在しないとエラー。
- ` w+ ` : 書き込み＋読み込み。既存内容は消える。
- ` r+ ` : 読み込み＋書き込み。既存内容を保持。ファイルが存在しないとエラー。


<div align="right">
  <a href="../README.md#section8">◀️READMEに戻る<a>
</div>




