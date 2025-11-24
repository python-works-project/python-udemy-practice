## 20. リストの使い所
#### 💻 ターミナルで実行
<div align="right">
  <a href="../README.md#20-リストの使い所">READMEに戻る</a>
</div>

```bash
# 座席を表すリストを初期化
seat = []
min = 0   # 座席数の下限
max = 5   # 座席数の上限

# 現在の座席数が下限以上かつ上限未満かを判定
min <= len(seat) < max   # len(seat) = 0 → True

# 1人追加
seat.append('p')         # seat = ['p']
min <= len(seat) < max   # len(seat) = 1 → True

# 2人目追加
seat.append('p')         # seat = ['p','p']
min <= len(seat) < max   # len(seat) = 2 → True

# 3人目・4人目追加
seat.append('p')         # seat = ['p','p','p']
seat.append('p')         # seat = ['p','p','p','p']
min <= len(seat) < max   # len(seat) = 4 → True

# 5人目追加 → 上限に達する
seat.append('p')         # seat = ['p','p','p','p','p']
min <= len(seat) < max   # len(seat) = 5 → False（満席）

# 先頭の座席を空ける（退席）
seat.pop(0)              # 'p' を削除 → seat = ['p','p','p','p']

# 再び条件判定 → 上限未満なので True
min <= len(seat) < max   # len(seat) = 4 → True
```

<div align="right">
  <a href="../README.md#20-リストの使い所">READMEに戻る</a>
</div>


