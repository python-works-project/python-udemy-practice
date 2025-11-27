## 60. リスト内包表記
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section5">READMEに戻る</a>
</div>

```python
t = (1, 2, 3, 4, 5)
t2 = (5, 6, 7, 8, 9)

# ① for文でタプルの要素をリストにコピー
r = []
for i in t:
    r.append(i)
print(r)   # [1, 2, 3, 4, 5]

# ② リスト内包表記で同じ処理（コピー）
r = [i for i in t]
print(r)   # [1, 2, 3, 4, 5]

# ③ 偶数だけを抽出（for + if）
r = []
for i in t:
    if i % 2 == 0:
        r.append(i)
print(r)   # [2, 4]

# ④ リスト内包表記で偶数抽出
r = [i for i in t if i % 2 == 0]
print(r)   # [2, 4]

# ⑤ 二重ループで積を計算（全組み合わせ）
r = []
for i in t:
    for j in t2:
        r.append(i * j)
print(r)   # [5,6,7,8,9,10,...,45]

# ⑥ リスト内包表記で二重ループの積
r = [i * j for i in t for j in t2]
print(r)   # [5,6,7,8,9,10,...,45]
```
## ✨ 学習のまとめ
- Pythonで 新しいリストを簡潔に作るための構文  
  通常の for 文＋append を使うよりも、短く読みやすく書ける
**基本構文**
```python
[式 for 変数 in イテラブル if 条件]
```


<div align="right">
  <a href="../README.md#section5">READMEに戻る</a>
</div>
