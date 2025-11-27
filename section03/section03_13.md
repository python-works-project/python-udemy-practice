## 13. 文字のメソッド
#### 📝 VSCodeで実行
<div align="right">
  <a href="../README.md#section3">◀️READMEに戻る</a>
</div>

```python
# --- 文字列メソッド ---
s = 'My name is Mike. Hi Mike.'
print(s)

is_start = s.startswith('My')   # 'My' で始まるか → True
print(is_start)

is_start = s.startswith('XX')   # 'XX' で始まるか → False
print(is_start)

print(s.find('Mike'))           # 最初の 'Mike' の位置 → 11
print(s.rfind('Mike'))          # 最後の 'Mike' の位置 → 19
print(s.count('Mike'))          # 'Mike' の出現回数 → 2

print(s.capitalize())           # 先頭を大文字に → 'My name is mike. hi mike.'
print(s.title())                # 単語ごとに先頭大文字 → 'My Name Is Mike. Hi Mike.'
print(s.upper())                # 全て大文字 → 'MY NAME IS MIKE. HI MIKE.'
print(s.lower())                # 全て小文字 → 'my name is mike. hi mike.'
print(s.replace('Mike','Nancy'))# 'Mike' を 'Nancy' に置換
```
<div align="right">
  <a href="../README.md#section3">◀️READMEに戻る</a>
</div>
