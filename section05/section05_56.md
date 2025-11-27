## 56. クロージャ―
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section5">◀️READMEに戻る</a>
</div>

```python
# --- 関数を返す関数の基本 ---
def outer(a, b):

    # 内側関数 inner を定義
    def inner():
        return a + b
    
    # inner 関数そのものを返す（まだ実行はしない）
    return inner

# outer(1, 2) は inner 関数オブジェクトを返す
print(outer(1, 2))  
# → <function outer.<locals>.inner at 0x...> （関数オブジェクトの参照）


# --- 返された関数を実際に呼び出す ---
def outer(a, b):

    def inner():
        return a + b
    
    return inner

f = outer(1, 2)  # inner 関数が返され、f に代入される
r = f()          # f() を呼び出す → inner() 実行 → 1+2=3
print(r)         # → 3


# --- 応用例：円の面積を計算する関数を生成 ---
def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius
    return circle_area

# π=3.14 を固定した関数を生成
cal1 = circle_area_func(3.14)

# π=3.141592 を固定した関数を生成
cal2 = circle_area_func(3.141592)

# 半径10の円面積を計算
print(cal1(10))   # → 314.0
print(cal2(10))   # → 314.1592
```
## ✨ 学習のまとめ
- 外側関数の中で内側関数を定義し、その関数オブジェクトを返す
- 内側関数は外側の変数を「覚えている」ので、後から呼び出しても利用できる
- 例：
```python
def outer(a, b):
    def inner():
        return a + b
    return inner

f = outer(1, 2)
print(f())  # → 3
```

<div align="right">
  <a href="../README.md#section5">◀️READMEに戻る</a>
</div>


