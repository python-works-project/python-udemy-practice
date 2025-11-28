## 64. 名前空間とスコープ
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section5">◀️READMEに戻る</a>
</div>

```python
"""main func doc"""

# グローバル変数
animal = 'cat'

def f():
    # ローカル変数を定義すると、同名のグローバル変数は隠れる
    animal = "dog"
    print('local:', animal)

print('global:', animal)  # → cat （グローバル変数）
f()                       # → dog （ローカル変数）


# global 宣言を使うと、関数内からグローバル変数を書き換え可能
animal = 'cat'

def f():
    global animal
    animal = "dog"        # グローバル変数を直接変更
    print('local:', animal)

print('global:', animal)  # → cat （変更前）
f()                       # → dog （変更後）
print('global after f():', animal)  # → dog （書き換え済み）


# ❌ エラーになるパターン
# グローバル変数を参照しつつ、同じ関数内で代入しようとすると
# 「UnboundLocalError: local variable 'animal' referenced before assignment」
# が発生する
animal = 'cat'

def f():
    print('before:', animal)  # ここでグローバルを参照しようとする
    animal = "dog"            # しかし代入があるため、animalはローカル扱いになる
    print('after:', animal)

# f()  # 実行すると UnboundLocalError


# 関数オブジェクトの属性（名前とdocstring）
def f():
    """test func doc"""
    print(f.__name__)  # 関数名
    print(f.__doc__)   # docstring

print(__name__)  # 現在のモジュール名（スクリプトなら "__main__"）
f()


# locals() と globals() の確認
def f():
    print('locals:', locals())  # 関数内のローカル名前空間を辞書で返す

f()
print('globals:', globals())    # モジュール全体のグローバル名前空間を辞書で返す
```
## ✨ 学習のまとめ
- global 宣言でグローバル変数を直接操作できる
- `__name__`,` __doc__` で関数やモジュールの属性を確認できる
- locals() / globals() で名前空間を辞書として確認できる


<div align="right">
  <a href="../README.md#section5">◀️READMEに戻る</a>
</div>
