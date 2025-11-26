## 36. InとNotの使い所
#### 📝 VSCodeで実行
<div align="right">
  <a href="../README.md#section5">READMEに戻る</a>
</div>

```python
y = [1, 2, 3]

# x が y に含まれているかどうかを判定
x = 1
if x in y:
    print('in')

# x が y に含まれていないかどうかを判定
x = 4
if x not in y:
    print('not in')


a = 1
b = 2

# not 演算子
if not a == b:
    print('not equal')

# != 演算子
if a != b:
    print('not equal')


is_ok = True

# is_ok が True の場合
if is_ok:
    print('hello')

# is_ok が False の場合
if not is_ok:
    print('hello')
```

<div align="right">
  <a href="../README.md#section5">READMEに戻る</a>
</div>
