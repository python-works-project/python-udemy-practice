## 26. 辞書のコピー
#### 📝 VSCodeで実行
<div align="right">
  <a href="../README.md#section4">READMEに戻る</a>
</div>

```python
# 辞書を作成
x = {'a': 1}

# y に x を代入（同じオブジェクトを参照する）
y = x

# y を通じて 'a' の値を変更
y['a'] = 1000

# x と y は同じオブジェクトなので、両方とも変更されている
print(x)  # {'a': 1000}
print(y)  # {'a': 1000}


# 辞書を作成
x = {'a': 1}

# copy() で x のコピーを作成（別オブジェクトになる）
y = x.copy()

# y を通じて 'a' の値を変更
y['a'] = 1000

# x と y は別オブジェクトなので、x は変更されない
print(x)  # {'a': 1}
print(y)  # {'a': 1000}
```

<div align="right">
  <a href="../README.md#section4">READMEに戻る</a>
</div>


