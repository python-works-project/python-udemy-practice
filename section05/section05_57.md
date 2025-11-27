## 57. デコレーター
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section5">◀️READMEに戻る</a>
</div>

```python
# --- 基本の関数 ---
def add_num(a, b):
    return a + b

print('start')
r = add_num(10, 20)   # 普通に関数を呼び出す
print('end')

print(r)              # → 30


# --- デコレータ関数を手動で適用 ---
def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')                 # 前処理
        result = func(*args, **kwargs) # 元の関数を実行
        print('end')                   # 後処理
        return result
    return wrapper

def add_num(a, b):
    return a + b

f = print_info(add_num)   # add_num をラップした関数を返す
r = f(10, 20)             # wrapper が呼ばれる
print(r)                  # → 30


# --- デコレータ構文 @ を使う ---
def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

@print_info               # add_num = print_info(add_num) と同じ意味
def add_num(a, b):
    return a + b

r = add_num(10, 20)       # wrapper が呼ばれる
print(r)                  # → 30

@print_info
def sub_num(a, b):
    return a - b

r = sub_num(100, 20)      # wrapper が呼ばれる
print(r)                  # → 80


# --- デコレータを2つ重ねる ---
def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)  # 関数名を表示
        print('args:', args)           # 引数を表示
        print('kwargs:', kwargs)       # キーワード引数を表示
        result = func(*args, **kwargs)
        print('result:', result)       # 戻り値を表示
        return result
    return wrapper

def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

@print_info
@print_more
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)
# 実行順序：
#   add_num → print_more でラップ → print_info でさらにラップ
# 出力は start → func情報 → result → end → 戻り値


# --- デコレータを手動でネスト ---
def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result
    return wrapper

def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

def add_num(a, b):
    return a + b

# add_num を print_more でラップ → さらに print_info でラップ
f = print_info(print_more(add_num))
r = f(1000, 2000)
print(r)

```
## ✨ 学習のまとめ
- デコレーターとは、関数を受け取り、関数を返す関数のこと
- `@デコレーター名` と書くと、その関数に自動的にラップ処理が適用される
```python
# 基本の流れ
def decorator(func):
    def wrapper(*args, **kwargs):
        # 前処理
        print("start")
        result = func(*args, **kwargs)  # 元の関数を実行
        # 後処理
        print("end")
        return result
    return wrapper

@decorator
def add_num(a, b):
    return a + b

print(add_num(10, 20))
```
**処理順**
- `@decorator` が付いた時点で  
→ add_num = decorator(add_num) に置き換えられる
- add_num(10, 20) を呼ぶと  
→ 実際には wrapper(10, 20) が呼ばれる
- wrapper の中で「前処理 → 元の関数 → 後処理」が実行される



<div align="right">
  <a href="../README.md#section5">◀️READMEに戻る</a>
</div>


