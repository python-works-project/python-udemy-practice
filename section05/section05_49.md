## 49. 関数の引数と返り値の宣言
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section5">◀️READMEに戻る</a>
</div>

```python
# Python3.6 以降は「型ヒント（type hints）」が使える
num: int = 10   # num は int 型であることを示す（動作には影響しない）

# --- 数値を足し算する関数（型ヒント付き） ---
def add_num(a: int, b: int) -> int:
    return a + b

r = add_num(10, 20)
print(r)  # 30

# --- 文字列を結合する関数（型ヒント付き） ---
def add_str(a: str, b: str) -> str:
    return a + b

r = add_str('a', 'b')
print(r)  # 'ab'

# --- 型ヒントは「動作を強制しない」例 ---
def add_num(a: int, b: int) -> int:
    return a + b

# 本来は数値を渡すべきだが、文字列を渡しても Python はエラーにしない
r = add_num('a', 'b')
print(r)  # 'ab'（文字列連結になる）
```
 

<div align="right">
  <a href="../README.md#section5">◀️READMEに戻る</a>
</div>
