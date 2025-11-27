## 27. 辞書型の使い所
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section4">READMEに戻る</a>
</div>

```python
# 辞書を作成（キーと値のペア）
fruits = {
    'apple': 100,
    'banana': 200,
    'orange': 300,
}

# キーを指定して値を取り出す
print(fruits['apple'])   # 100
print(fruits['banana'])  # 200
print(fruits['orange'])  # 300


# リストを作成（要素は ["果物名", 値] のペア）
l = [
    ['apple', 100],
    ['banana', 100],
    ['orange', 100],
]

# リストは「インデックス番号」でアクセスするため、キーのように文字列では指定できない
# print(l['apple'])  # ← エラーになる（TypeError: list indices must be integers or slices, not str）

# 正しいアクセス方法はインデックス番号を使う
print(l[0])       # ['apple', 100]
print(l[0][0])    # 'apple'
print(l[0][1])    # 100
```

<div align="right">
  <a href="../README.md#section4">READMEに戻る</a>
</div>


