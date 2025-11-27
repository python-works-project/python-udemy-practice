## 38. Noneを判定する場合
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section5">◀️READMEに戻る</a>
</div>

```python
is_empty = None
# print(is_empty)        # None を表示
# print(help(is_empty))  # NoneType の説明を表示

# == で None 判定
if is_empty == None:
    print('None!')

# is で None 判定（推奨）
if is_empty is None:
    print('None!')

# is not で None 以外を判定
if is_empty is not None:
    print('None!')

# 値の比較（1 == True → True）
print(1 == True)

# オブジェクトの同一性比較（1 is True → False）
print(1 is True)

# None 同士の同一性比較（常に True）
print(None is None)
```

<div align="right">
  <a href="../README.md#section5">◀️READMEに戻る</a>
</div>
