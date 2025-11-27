## 50. 位置引数とキーワード引数とデフォルト引数
#### 📝 VSCodeで実行
<div align="right">
  <a href="../README.md#section5">READMEに戻る</a>
</div>

```python
# --- 位置引数で渡す例 ---
def menu(entree, drink, dessert):
    print(entree)
    print(drink)
    print(dessert)

menu('pizza', 'beer', 'ice')  # 引数を順番通りに渡す（positional arguments）

# --- キーワード引数を使う例 ---
def menu(entree, drink, dessert):
    print('entree = ', entree)
    print('drink = ', drink)
    print('dessert = ', dessert)

# キーワード引数なら順番を入れ替えてもOK
menu(entree='pizza', drink='beer', dessert='ice')
menu(drink='beer', entree='pizza', dessert='ice')

# 位置引数とキーワード引数を混在させることもできる
menu('pizza', drink='beer', dessert='ice')

# ただし位置引数の順番を間違えると意図しない結果になる
menu('beer', entree='pizza', dessert='ice')  # 'beer' が entree に入る

# --- デフォルト引数を持つ関数 ---
def menu2(entree='carry', drink='wine', dessert='cake'):
    print('entree = ', entree)
    print('drink = ', drink)
    print('dessert = ', dessert)

menu2()  # 引数を省略するとデフォルト値が使われる
menu2(entree='pizza', drink='beer', dessert='ice')  # 指定すれば上書きされる
```

<div align="right">
  <a href="../README.md#section5">READMEに戻る</a>
</div>
