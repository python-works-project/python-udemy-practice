## 60. リスト内包表記
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section5">READMEに戻る</a>
</div>

```python
t = (1, 2, 3, 4, 5)
t2 = (5, 6, 7, 8, 9)
```
```python
r = []
for i in t:
    r.append(i)
print(r)   # [1, 2, 3, 4, 5]
```
```python
# リスト内包表記
r = [i for i in t]
print(r)   # [1, 2, 3, 4, 5]
```
```python
r = []
for i in t:
    if i % 2 == 0:
        r.append(i)
print(r)   # [2, 4]
```
```python
# リスト内包表記
r = [i for i in t if i % 2 == 0]
print(r)   # [2, 4]
``````python
r = []
for i in t:
    for j in t2:
        r.append(i * j)
print(r)   # [5,6,7,8,9,10,...,45]
```
```python
# リスト内包表記
r = [i * j for i in t for j in t2]
print(r)   # [5,6,7,8,9,10,...,45]
```
## ✨ 学習のまとめ
- Pythonで 新しいリストを簡潔に作るための構文  
  通常の for 文＋append を使うよりも、短く読みやすく書ける

```python
# 基本構文
[式 for 変数 in イテラブル if 条件]

# 1. 単純コピー
r = [i for i in (1, 2, 3)]
# → [1, 2, 3]

# 2. 値を加工して追加
r = [i * 2 for i in (1, 2, 3)]
# → [2, 4, 6]

# 3. 条件付きで抽出
r = [i for i in range(10) if i % 2 == 0]
# → [0, 2, 4, 6, 8]

# 4. 二重ループも書ける
r = [i * j for i in (1, 2, 3) for j in (4, 5)]
# → [4, 5, 8, 10, 12, 15]
```


<div align="right">
  <a href="../README.md#section5">READMEに戻る</a>
</div>
