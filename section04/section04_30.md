## 30. 集合型の使い所
#### 📝 VSCodeで実行
<div align="right">
  <a href="../README.md#30-集合型の使い所">READMEに戻る</a>
</div>


```bash
# 自分の友達の集合
my_frienda = {'A', 'B', 'C'}

# Aさんの友達の集合
A_frienda = {'B', 'D', 'E', 'F'}

# 共通部分（積集合）を求める → 両方にいる友達
print(my_frienda & A_frienda)  # {'B'}


# リストを作成（同じ要素が重複している）
f = ['apple', 'banana', 'apple', 'banana']
print(f)  # ['apple', 'banana', 'apple', 'banana']

# リストを集合に変換 → 重複が自動的に取り除かれる
kind = set(f)
print(kind)  # {'apple', 'banana'}
```

<div align="right">
  <a href="../README.md#30-集合型の使い所">READMEに戻る</a>
</div>


