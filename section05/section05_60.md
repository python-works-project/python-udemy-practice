## 60. リスト内包表記
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section5">READMEに戻る</a>
</div>

```python
t = (1, 2, 3, 4, 5)      # 元のタプル
t2 = (5, 6, 7, 8, 9)     # 掛け算用のタプル

# --- タプルの要素をリストにコピー ---
r = []
for i in t:              # tの要素を順に取り出す
    r.append(i)          # リストに追加
print(r)   # [1, 2, 3, 4, 5]

# リスト内包表記で同じ処理
r = [i for i in t]       # tの要素をそのままリスト化
print(r)   # [1, 2, 3, 4, 5]


# --- 偶数だけ抽出 ---
r = []
for i in t:              # tの要素を順に取り出す
    if i % 2 == 0:       # 偶数なら追加
        r.append(i)
print(r)   # [2, 4]

# リスト内包表記で同じ処理
r = [i for i in t if i % 2 == 0]   # 偶数のみリスト化
print(r)   # [2, 4]


# --- 2つのタプルの全組み合わせで掛け算 ---
r = []
for i in t:              # tの要素を順に取り出す
    for j in t2:         # t2の要素を順に取り出す
        r.append(i * j)  # 掛け算結果を追加
print(r)   # [5,6,7,8,9,10,...,45]

# リスト内包表記で同じ処理
r = [i * j for i in t for j in t2]   # 全組み合わせの積をリスト化
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
