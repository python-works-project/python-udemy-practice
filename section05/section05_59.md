## 59. ジェネレーター
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section5">READMEに戻る</a>
</div>

```python
l = ['Good morning', 'Good afternoon', 'Good night']

# リストの要素を順に出力
for i in l:
    print(i)
```
```python
# ジェネレータ関数の定義
def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'

# ジェネレータをfor文で展開
for g in greeting():
    print(g)
```
```python
# ジェネレータをnext()で逐次取得
def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'

g = greeting()
print(next(g))   # 1つ目の要素
print('@@@@')    # 途中で別の処理を挟める
print(next(g))   # 2つ目の要素
print('@@@@')    # 途中で別の処理を挟める
print(next(g))   # 3つ目の要素
```
```python
# カウンタ用ジェネレータ
def counter(num=10):
    for _ in range(num):
        yield 'run'

def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'

g = greeting()
c = counter()

print(next(g))   # Good morning
print(next(c))   # run1
print(next(c))   # run2
print(next(c))   # run3
print(next(c))   # run4
print(next(c))   # run5

print(next(g))   # Good afternoon
print(next(c))   # run6
print(next(c))   # run7
print(next(c))   # run8

print(next(g))   # Good night
print(next(g))   # StopIteration発生（要素が尽きる）

```
## ✨ 学習のまとめ
- 

<div align="right">
  <a href="../README.md#section5">READMEに戻る</a>
</div>


