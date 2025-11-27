## 53. キーワード引数の辞書化
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section5">READMEに戻る</a>
</div>

```python
# --- デフォルト引数 ---
def menu(entree='pizza', drink='wine'):
    print(entree, drink)

menu()  # 引数を省略するとデフォルト値が使われる → pizza wine
menu(entree='cake', drink='coffee')  # 指定すれば上書きされる → cake coffee

# --- キーワード引数をまとめて受け取る（**kwargs） ---
def menu(**kwargs):
    print(kwargs)  # 辞書として受け取る
    for k, v in kwargs.items():
        print(k, v)

menu(entree='cake', drink='coffee')

# --- 辞書をアンパックして渡す ---
def menu(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)

d = {
    'entree': 'pizza',
    'drink': 'beer',
    'dessert': 'ice'
}
menu(**d)  # 辞書を展開して渡す → entree pizza / drink beer / dessert ice

# --- 位置引数 + 可変長引数(*args) + キーワード引数(**kwargs) ---
def menu(food, *args, **kwargs):
    print(food)    # 最初の引数
    print(args)    # 残りの位置引数（タプル）
    print(kwargs)  # キーワード引数（辞書）

menu('apple', 'banana', 'orange', entree='cake', drink='coffee')
# food = 'apple'
# args = ('banana', 'orange')
# kwargs = {'entree': 'cake', 'drink': 'coffee'}

# --- 引数の順序は「*args → **kwargs」でなければならない ---
# 以下は構文エラーになる例
def menu(food, **kwargs, *args):  # ❌ 順序が逆なのでエラー
    print(food)
    print(args)
    print(kwargs)
```
## ✨ 学習のまとめ
- 

<div align="right">
  <a href="../README.md#section5">READMEに戻る</a>
</div>
