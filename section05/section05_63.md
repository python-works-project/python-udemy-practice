## 63. ジェネレーター内包表記
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section5">READMEに戻る</a>
</div>

```python
# ジェネレーター関数の定義
def g():
    for i in range(10):
        yield i   # yieldで値を1つずつ返す（ジェネレーターになる）

# 関数を呼び出してジェネレーターオブジェクトを作成
g = g()
print(type(g))       # <class 'generator'>
print(next(g))       # 0 （最初の値）
print(next(g))       # 1 （次の値）
print(next(g))       # 2 （さらに次の値）

# ジェネレーター式（内包表記のように書ける）
g = (i for i in range(10))
print(type(g))       # <class 'generator'>
print(next(g))       # 0
print(next(g))       # 1
print(next(g))       # 2

# 条件付きジェネレーター式（偶数だけ取り出す）
g = (i for i in range(10) if i % 2 == 0)
for x in g:
    print(x)         # 2, 4, 6, 8

# ジェネレーター式をtupleに変換（全要素をまとめてタプル化）
g = tuple(i for i in range(10))
print(type(g))       # <class 'tuple'>
print(g)             # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
```
## ✨ 学習のまとめ

- 基本構文：`式 for 変数 in イテラブル if 条件`
- リスト内包表記と似ているが、[] ではなく () を使う
- 結果は ジェネレーターオブジェクト（イテレータ）になる
- next() や for で値を順に取り出す
- メモリ効率が良く、大量データを扱うときに便利

**単純コピー**
```python
g = (i for i in (1, 2, 3))
print(type(g))  # <class 'generator'>
print(list(g))  # → [1, 2, 3]
```

**値を加工して追加**
```python
g = (i * 2 for i in (1, 2, 3))
print(list(g))  # → [2, 4, 6]
```

**条件付きで抽出**
```python
g = (i for i in range(10) if i % 2 == 0)
print(list(g))  # → [0, 2, 4, 6, 8]
```

**二重ループも書ける**
```python
g = (i * j for i in (1, 2, 3) for j in (4, 5))
print(list(g))  # → [4, 5, 8, 10, 12, 15]
``` 

<div align="right">
  <a href="../README.md#section5">READMEに戻る</a>
</div>
