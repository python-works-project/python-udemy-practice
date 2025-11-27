## 51. デフォルト引数で気を付けること
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section5">READMEに戻る</a>
</div>

```python
# --- デフォルト引数にリストを使う例 ---
def test_func(x, l=[]):
    l.append(x)
    return l

# 既存のリスト y を渡すと、そのリストに要素が追加される
y = [1, 2, 3]
r = test_func(100, y)
print(r)  # [1, 2, 3, 100]

y = [1, 2, 3]
r = test_func(200, y)
print(r)  # [1, 2, 3, 200]

# 引数を省略すると、デフォルトのリストが使われる
r = test_func(100)
print(r)  # [100]

# もう一度呼ぶと、前回のリストが再利用される（新しく作られない）
r = test_func(100)
print(r)  # [100, 100] ← 前回の結果が残っている（デフォルト引数のリストは共有されるため）

# --- 安全な書き方（Noneを使って初期化） ---
def test_func(x, l=None):
    if l is None:
        l = []  # 呼び出しごとに新しいリストを作る
    l.append(x)
    return l

r = test_func(100)
print(r)  # [100]

r = test_func(100)
print(r)  # [100] ← 毎回新しいリストが作られるので安心
```
## ✨ 学習のまとめ
**デフォルト引数の注意点**
- デフォルトのリストは 関数定義時に一度だけ作られ、再利用される
- 呼び出しのたびに前回の結果が残る → バグの原因

```python
# 危険な例
def test_func(x, l=[]):  
    l.append(x)
    return l

# 安全な書き方
def test_func(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l
```

<div align="right">
  <a href="../README.md#section5">READMEに戻る</a>
</div>
