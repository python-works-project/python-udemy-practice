## 11. 文字列
#### 📝 VSCodeで実行
<div align="right">
  <a href="../README.md">READMEへ戻る</a>
</div>

```bash
# --- 文字列のクォートの使い方 ---
print("I don't know")              # ダブルクォートで囲めば、内部のシングルクォートをそのまま使える
print('say "I don\'t know"')       # シングルクォートで囲み、内部のシングルクォートはエスケープ
print("say \"I don't know\"")      # ダブルクォート内のダブルクォートはエスケープ

# --- 改行やエスケープシーケンス ---
print('Hello. \nHow are you?')     # \n で改行
print(r'c:\name\name')             # r'' で「raw文字列」→ エスケープを無効化

# --- 複数行文字列 ---
print("""\
line1
line2
line3\
""")                               # """...""" で複数行文字列を表現

# --- 文字列の結合と繰り返し ---
print('Hi.' * 3 + 'Mike')          # 'Hi.' を3回繰り返して 'Mike' を結合
print('Py' + 'thon')               # 文字列の結合 → 'Python'
print('Py''thon')                  # 隣接文字列は自動結合 → 'Python'
prefix = 'Py'
print(prefix + 'thon')             # 変数と文字列の結合

# --- 長い文字列の分割記述 ---
s = ('aaaaaaaaaaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbbbbbbbbbb')  # () 内の隣接文字列は自動結合
print(s)

ss = 'aaaaaaaaaaaaaaaaaaaaaaaa' \
     'bbbbbbbbbbbbbbbbbbbbbbbb'   # バックスラッシュで改行を継続
print(s)
```
<div align="right">
  <a href="../README.md">READMEへ戻る</a>
</div>
