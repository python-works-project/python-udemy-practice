## 46. zip関数
#### 📝 VSCodeで実行
<div align="right">
  <a href="../README.md#section5">READMEに戻る</a>
</div>

```python
# 曜日・果物・飲み物の3つのリストを並行して取り出し、対応する要素を1行にまとめて表示する処理
days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'bear']

# インデックスを使って3つのリストの同じ位置の要素を取り出して表示
for i in range(len(days)):
    print(days[i], fruits[i], drinks[i])

# zipを使って3つのリストを同時にループし、対応する要素を取り出して表示
for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)
```

<div align="right">
  <a href="../README.md#section5">READMEに戻る</a>
</div>
