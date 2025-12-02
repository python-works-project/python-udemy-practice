## 82. メソッドのオーバーライドとsuperによる親のメソッド呼び出し
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section7">◀️READMEに戻る</a>
</div>

**メソッドのオーバーライド**
```python
# 親クラス Car の定義
class Car(object):
    def run(self):
        print('run')         # Car クラスの基本動作

# Car を継承した ToyotaCar クラス
class ToyotaCar(Car):
    def run(self):
        print('fast')        # 親クラスの run をオーバーライド

# Car を継承した TeslaCar クラス
class TeslaCar(Car):
    def run(self):
        print('super fast')  # 親クラスの run をオーバーライド

# インスタンス生成とメソッド呼び出し
car = Car()
car.run()                    # → "run"

toyota_Car = ToyotaCar()
toyota_Car.run()             # → "fast" （オーバーライドされたメソッド）

tesla_Car = TeslaCar()
tesla_Car.run()              # → "super fast" （オーバーライドされたメソッド）
```

**superによる親のメソッド呼び出し**
```python
# 親クラス Car の定義
class Car(object):
    def __init__(self, model=None):
        self.model = model               # インスタンス変数 model を初期化
    def run(self):
        print('run')                     # Car の基本動作

# Car を継承した TeslaCar クラス
class TeslaCar(Car):
    def __init__(self, model='Model S'):
        super().__init__(model)          # 親クラスのコンストラクタを呼び出して model を初期化

# 動作確認
tesla_Car = TeslaCar('Model S')
print(tesla_Car.model)                   # → "Model S" （super() で親の __init__ を呼び出した）
```

## ✨ 学習のまとめ
- オーバーライド：親と同じ名前のメソッドを子クラスで定義すると、親の処理を上書きできる。
- 独自メソッド：子クラスに新しいメソッドを追加すれば、そのクラスだけの機能を持たせられる。
- コンストラクタのオーバーライド：
  子クラスで` __init__ `を定義すると親の初期化処理は呼ばれない
   → ` super().__init__() `で呼び出す必要がある。

<div align="right">
  <a href="../README.md#section7">◀️READMEに戻る<a>
</div>




