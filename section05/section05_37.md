## 37. 値が入っていない判定をするテクニック
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section5">◀️READMEに戻る</a>
</div>

```python
# 文字列は空でなければ True
is_ok = 'True'
if is_ok:
    print('True')
else:
    print('False')

# 空文字列は False
is_ok = ''
if is_ok:
    print('True')
else:
    print('False')

# 数値 1 は True
is_ok = 1
if is_ok:
    print('OK!')
else:
    print('NO!')

# 数値 0 は False
is_ok = 0
if is_ok:
    print('OK!')
else:
    print('NO!')

# 数値 10 は True
is_ok = 10
if is_ok:
    print('OK!')
else:
    print('NO!')

# 空文字列は False
is_ok = ''
if is_ok:
    print('True')
else:
    print('False')

# 空リストは False
is_ok = []
if is_ok:
    print('True')
else:
    print('False')

# 要素ありリストは True
is_ok = [1, 2, 3, 4]
if is_ok:
    print('True')
else:
    print('False')

# 空辞書は False
is_ok = {}
if is_ok:
    print('True')
else:
    print('False')
```

<div align="right">
  <a href="../README.md#section5">◀️READMEに戻る</a>
</div>
