## 42. for文とbreak文とcontinue文
#### 📝 VSCodeで実行
<div align="right">
  <a href="../README.md#section5">READMEに戻る</a>
</div>

```python
# whileでリストを順に処理
some_list = [1, 2, 3, 4, 5]

i = 0
while i < len(some_list):
    print(some_list[i])
    i += 1

# forでリストを順に処理
for i in some_list:
    print(i)

# forで文字列を1文字ずつ処理
for s in 'abcde':
    print(s)

# forで単語リストを順に処理
for word in ['My', 'name', 'is', 'MIke']:
    print(word)

# for + break（'name'で終了）
for word in ['My', 'name', 'is', 'MIke']:
    if word == 'name':
        break
    print(word)

# for + continue（'name'をスキップ）
for word in ['My', 'name', 'is', 'MIke']:
    if word == 'name':
        continue
    print(word)
```

<div align="right">
  <a href="../README.md#section5">READMEに戻る</a>
</div>
