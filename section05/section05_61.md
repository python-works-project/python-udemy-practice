## 61. 辞書内包表記
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section5">READMEに戻る</a>
</div>

```python
w = ['Mon', 'Tue', 'Wen']   # 曜日のリスト
f = ['coffee', 'Milk', 'Water']   # 飲み物のリスト

# --- for文 + zip で辞書を作成 ---
d = {}
for x, y in zip(w, f):      # wとfの対応する要素をペアに取り出す
    d[x] = y                # キーに曜日、値に飲み物を登録
print(d)                    # {'Mon': 'coffee', 'Tue': 'Milk', 'Wen': 'Water'}

# --- 辞書内包表記で同じ処理を簡潔に書く ---
d = {x: y for x, y in zip(w, f)}  # zipでペアを作り、キー:値の辞書を生成
print(d)                          # {'Mon': 'coffee', 'Tue': 'Milk', 'Wen': 'Water'}
```
## ✨ 学習のまとめ
- 基本構文 :`{key: value for key, value in iterable}`
- iterable から要素を取り出し、キーと値を対応付けて辞書を生成する。

**2つのリストを対応付け**
```python
w = ['Mon', 'Tue', 'Wed']
f = ['coffee', 'Milk', 'Water']

d = {x: y for x, y in zip(w, f)}
print(d)  # {'Mon': 'coffee', 'Tue': 'Milk', 'Wed': 'Water'}
```
**値を加工して登録**
```python
nums = [1, 2, 3]
d = {n: n**2 for n in nums}
print(d)  # {1: 1, 2: 4, 3: 9}
```
**条件付きで登録**
```python
nums = range(6)
d = {n: n*10 for n in nums if n % 2 == 0}
```

<div align="right">
  <a href="../README.md#section5">READMEに戻る</a>
</div>
