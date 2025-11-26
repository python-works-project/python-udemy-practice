## 22. タプルのアンパッキング
#### 📝 VSCodeで実行
<div align="right">
  <a href="../README.md#section4">READMEに戻る</a>
</div>

```python
# タプルを作成
num_tuple = (10,20)
print(num_tuple)       # (10, 20)

# タプルのアンパッキング（複数の変数に展開）
x,y = num_tuple
print(x, y)            # 10 20

# タプルを直接アンパッキング
x, y = (10, 20)
print(x, y)            # 10 20

# カンマ区切りで書くとタプルとして扱われる
x, y = 10, 20
print(x, y)            # 10 20

# 変数名に複数代入（min, maxなど）
min, max = 0, 100
print(min, max)        # 0 100

# 変数の値を入れ替える（従来の方法）
i = 10
j = 20
print(i, j)            # 10 20
tmp  = i               # 一時変数に保存
i = j
j = tmp
print(i, j)            # 20 10

# Pythonらしい入れ替え（アンパッキングを利用）
a = 100
b = 200
print(a, b)            # 100 200
a, b = b, a            # 一時変数なしで入れ替え可能
print(a, b)            # 200 100
```

<div align="right">
  <a href="../README.md#section4">READMEに戻る</a>
</div>


