## 74. 標準ライブラリ
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section6">◀️READMEに戻る</a>
</div>

**文字列を用意**
```python
s = "aaabbcccccdde"
```
**方法1: if文で初期化してカウント**
```python
d = {}
for c in s:
    if c not in d:      # 初めて出てきた文字ならキーを作って0で初期化
        d[c] = 0
    d[c] += 1           # 既存なら値を1増やす

print(d)  # {'a': 3, 'b': 2, 'c': 5, 'd': 2, 'e': 1}
```

**方法2: ` setdefault() `**
```python
d = {}
for c in s:
    if c not in d:              # キーがなければ setdefault で初期値を設定
        d.setdefault(c, 0)
        d[c] += 1               # 値を1増やす

print(d)  # {'a': 3, 'b': 2, 'c': 5, 'd': 2, 'e': 1}
```

**方法3: ` collections.defaultdict `**
```python
from collections import defaultdict

d = defaultdict(int)    # 新しいキーが出てきたら自動的に 0 で初期化される辞書

for c in s:
    d[c] += 1           # そのまま加算できる（初期化不要）

print(d)  # defaultdict(<class 'int'>, {'a': 3, 'b': 2, 'c': 5, 'd': 2, 'e': 1})
```
**特定のキーの値を参照**
```python
print(d['b'])  # → 2
```

## ✨ 学習のまとめ
**` setdefault `**
- 対象: 通常の辞書` （dict）`に使うメソッド
- 役割: 指定したキーが存在しなければ「デフォルト値」を代入し、その値を返す
```python
d = {}
d.setdefault("x", 0)   # キー "x" がなければ 0 を代入
d["x"] += 1
print(d)  # → {'x': 1}
```

**` defaultdict `**
- 対象:` collections `モジュールが提供する「辞書の派生クラス」
- 役割: 存在しないキーにアクセスしたとき、自動で「デフォルト値」を生成して登録する
```python
from collections import defaultdict

d = defaultdict(int)   # 未登録キーは自動で int() → 0 に初期化
d["x"] += 1
print(d)  # → {'x': 1}
```

<div align="right">
  <a href="../README.md#section6">◀️READMEに戻る<a>
</div>
