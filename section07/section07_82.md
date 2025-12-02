## 82. メソッドのオーバーライドとsuperによる親のメソッド呼び出し
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section7">◀️READMEに戻る</a>
</div>

```python
# 親クラス Car の定義
class Car(object):
    def run(self):
        print('run')         # Car クラスの基本動作

# Car を継承した ToyotaCar クラス
class ToyotaCar(Car):
    def run(self):
        print('fast')        # 親クラスの run をオーバーライド（上書き）

# Car を継承した TeslaCar クラス
class TeslaCar(Car):
    def run(self):
        print('super fast')  # 親クラスの run をオーバーライド（上書き）

    def auto_run(self):
        print('auto run')    # TeslaCar 独自のメソッド

# Car クラスのインスタンス生成
car = Car()
car.run()                    # "run"

# ToyotaCar クラスのインスタンス生成
toyota_Car = ToyotaCar()
toyota_Car.run()             # "fast" （親の run をオーバーライド）

# TeslaCar クラスのインスタンス生成
tesla_Car = TeslaCar()
tesla_Car.run()              # "super fast" （親の run をオーバーライド）
tesla_Car.auto_run()         # "auto run" （TeslaCar 独自のメソッド）
```

```python
# 親クラス Car の定義
class Car(object):
    def __init__(self, model=None):
        self.model = model   # インスタンス変数 model を初期化
    def run(self):
        print('run')         # Car の基本動作

# Car を継承した ToyotaCar クラス
class ToyotaCar(Car):
    def run(self):
        print('fast')        # 親クラスの run をオーバーライド（上書き）

# Car を継承した TeslaCar クラス
class TeslaCar(Car):
    def __init__(self, model='Model S', enable_auto_run=False):
        super().__init__(model)      # 親クラスのコンストラクタを呼び出して model を初期化
        self.enable_auto_run = enable_auto_run    # TeslaCar 独自のインスタンス変数を追加
    def run(self):
        print('super fast')
    def auto_run(self):
        print('auto run')

car = Car()
car.run()   # → "run"

toyota_Car = ToyotaCar('Lexus')
print(toyota_Car.model)      # "Lexus" （親の __init__ で初期化された）
toyota_Car.run()             # "fast" （オーバーライドされたメソッド）

tesla_Car = TeslaCar('Model S')
print(tesla_Car.model)       # "Model S" （super() で親の __init__ を呼び出した）
tesla_Car.run()              # "super fast" （オーバーライドされたメソッド）
tesla_Car.auto_run()         # "auto run" （TeslaCar 独自のメソッド）
```

## ✨ 学習のまとめ
- 継承: class ToyotaCar(Car) のように書くと、Car の機能を引き継げる。
- オーバーライド: 親と同じ名前のメソッドを子クラスで定義すると、親の処理を上書きできる。
- 独自メソッド: 子クラスに新しいメソッドを追加すれば、そのクラスだけの機能を持たせられる。
- コンストラクタのオーバーライド：
  子クラスで` __init__ `を定義すると親の初期化処理は呼ばれない
   → ` super().__init__() `で呼び出す必要がある。

<div align="right">
  <a href="../README.md#section7">◀️READMEに戻る<a>
</div>




