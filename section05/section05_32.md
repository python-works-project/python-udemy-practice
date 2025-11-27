## 32. 1行が長くなる時
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section5">READMEに戻る</a>
</div>

```python
# 文字列を + 演算子で連結
s = 'aaaaaaaaaaaaa' + 'bbbbbbbbbbbbbbbbbb'
print(s)  # → 'aaaaaaaaaaaaabbbbbbbbbbbbbbbbbb'

# この場合はエラーとなる
# s = 'aaaaaaaaaaaaa'
# + 'bbbbbbbbbbbbbbbbbb'

# バックスラッシュ（\）を使って行を継続
s2 = 'aaaaaaaaaaaaa' \
+ 'bbbbbbbbbbbbbbbbbb'
print(s2)  # → 'aaaaaaaaaaaaabbbbbbbbbbbbbbbbbb'

# 数字の足し算を複数行に分けて書いた例
s3 = 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 \
  + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1
print(s3)  # → 20

# () で括ると改行しても式が継続できる
s4 = (1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1
  + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1)
print(s4)  # → 20
```

<div align="right">
  <a href="../README.md#section5">READMEに戻る</a>
</div>
