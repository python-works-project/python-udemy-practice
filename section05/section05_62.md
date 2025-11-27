## 62. 集合内包表記
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section5">READMEに戻る</a>
</div>

```python
s = set()                     # 空の集合を作成

for i in range(10):           # 0〜9を順に取り出す
    s.add(i)                  # 集合に追加
print(s)   # {0,1,2,3,4,5,6,7,8,9}

# 集合内包表記で同じ処理
s = {i for i in range(10)}    # 0〜9を集合に追加
print(s)   # {0,1,2,3,4,5,6,7,8,9}
```
```python
s = set()                     # 空の集合を作成

for i in range(10):           # 0〜9を順に取り出す
    if i % 2 == 0:            # 偶数のみ追加
        s.add(i)
print(s)   # {0,2,4,6,8}

# 集合内包表記で同じ処理
s = {i for i in range(10) if i % 2 == 0}   # 偶数のみ集合に追加
print(s)   # {0,2,4,6,8}
```
## ✨ 学習のまとめ
-  基本構文：`{式 for 変数 in イテラブル if 条件}`

**単純な集合生成**
```python
s = {i for i in range(5)}
print(s)  # {0, 1, 2, 3, 4}
```

**値を加工して追加**
```python
s = {i * 2 for i in range(5)}
print(s)  # {0, 2, 4, 6, 8}
```

**条件付きで抽出**
```python
s = {i for i in range(10) if i % 2 == 0}
print(s)  # {0, 2, 4, 6, 8}
```

<div align="right">
  <a href="../README.md#section5">READMEに戻る</a>
</div>
