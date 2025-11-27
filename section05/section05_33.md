## 33. If文
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section5">◀️READMEに戻る</a>
</div>

```python
# if 文で条件分岐
x = -10
if x < 0:
    print('negative')

# x = 0
x = 10  # 今回は 10 を代入
if x < 0:
    print('negative')
elif x == 0:
    print('zero')
elif x == 10:
    print('10')
else:
    print('positive')

# ネストした if 文の例
a = 5
b = 10
if a > 0:
    print('a = positive')
    if b > 0:
        print('b = positive')
```
## ✨ 学習のまとめ
- Pythonでは、インデント（字下げ）が正しく揃っていないと構文エラーになる

<div align="right">
  <a href="../README.md#section5">◀️READMEに戻る</a>
</div>
