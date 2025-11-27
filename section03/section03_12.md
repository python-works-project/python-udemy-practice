## 12. 文字列のインデックスとスライス
#### 📝 VSCodeで実行
<div align="right">
  <a href="../README.md#section3">◀️READMEに戻る</a>
</div>

```python
# --- インデックスとスライス ---
word = 'python'
print(word[3])     # インデックス3 → 'h'
print(word[-1])    # インデックス-1 → 最後の文字 'n'

print(word[0:2])   # 0〜1 → 'py'
print(word[:2])    # 先頭から2文字 → 'py'
print(word[2:])    # 2文字目以降 → 'thon'
print(word[2:5])   # 2〜4 → 'tho'

word = 'j' + word[1:]  # 先頭を 'j' に置き換え → 'jython'
print(word)
print(word[:])     # 全体をスライス → 'jython'

print(len(word))   # 文字列の長さ → 6
```
