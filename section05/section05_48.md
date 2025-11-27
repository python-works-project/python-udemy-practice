## 48. 関数定義
#### 📝 VSCodeで実行
<div align="right">
  <a href="../README.md#section5">READMEに戻る</a>
</div>

```python
# --- 基本的な関数定義と呼び出し ---
def say_something():
    print('Hi')

say_something()  # 関数を呼び出す

# --- 関数は定義より前に呼び出すとエラーになる例 ---
# say_something_NG()      # ← ここで呼ぶと未定義なのでエラー
# def say_something_NG():
#     print('Hi')

# --- 関数そのものは「オブジェクト」なので type() で確認できる ---
print(type(say_something))  # <class 'function'>

# --- 関数を変数に代入して呼び出すこともできる ---
f = say_something
f()  # say_something() と同じ動作

# --- return を使って値を返す関数 ---
def say_something2():
    s = 'Hello'
    return s

result = say_something2()
print(result)  # 'Hello'

# --- 引数によって処理を分岐する関数 ---
def what_is_this(color):
    if color == 'red':
        print('tomato')
    elif color == 'green':
        print('green pepper')
    else:
        return "I don't know"

# 関数の呼び出し例
result = what_is_this('red')    # tomato（print）
result = what_is_this('green')  # green pepper（print）
result = what_is_this('pink')   # return される
print(result)  # "I don't know"
```

<div align="right">
  <a href="../README.md#section5">READMEに戻る</a>
</div>
