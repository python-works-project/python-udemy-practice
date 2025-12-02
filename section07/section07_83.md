## 83. プロパティを使った属性の設定
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section7">◀️READMEに戻る</a>
</div>

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
        print('fast')        # 親クラスの run をオーバーライド

# Car を継承した TeslaCar クラス
class TeslaCar(Car):
    def __init__(self, model='Model S', 
                 enable_auto_run=False,
                 passwd='123'):
        super().__init__(model)
        # self.enable_auto_run = enable_auto_run   # 直接公開属性として設定
        # self._enable_auto_run = enable_auto_run  # 慣習的に「非公開扱い」の属性
        self.__enable_auto_run = enable_auto_run   # 名前修飾（name mangling）される属性 → 外部から直接アクセス不可
        self.passwd = passwd                       # パスワード（setterでの制御に利用）

    # プロパティ getter
    @property
    def enable_auto_run(self):
        return self._enable_auto_run         # 外部から tesla_Car.enable_auto_run と呼ぶとこのメソッドが実行される

    # プロパティ setter
    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.passwd == '456':             # パスワードが正しい場合のみ値を設定できる
            self._enable_auto_run = is_enable
        else:
            raise ValueError                 # 不正なパスワードならエラー

    def run(self):
        print(self.__enable_auto_run)   # __enable_auto_run は「名前修飾」されているので外部から直接アクセスできない
        print('super fast')

    def auto_run(self):
        print('auto run')

# tesla_Car = TeslaCar('Model S', passwd='456')   # 正しいパスワードなら setter が使える
tesla_Car = TeslaCar('Model S', passwd='111')     # パスワードが違うので setter は失敗する
# tesla_Car.enable_auto_run = True                # setter 呼び出し → passwd が違うので ValueError
# print(tesla_Car.__enable_auto_run)              # __付きは外部から直接アクセスできない
tesla_Car.run()                                   # run 内部では __enable_auto_run にアクセス可能
```
## ✨ 学習のまとめ
**` _変数名 `（シングルアンダースコア）**
- 慣習的に「外部から直接触らないで(=内部用)」という意味
- Pythonでは強制されないので外部からアクセスできてしまうが、通常は直接使わずプロパティ経由で扱う

**`__変数名 `（ダブルアンダースコア）**
- ` 「名前修飾（name mangling）」`されて、クラス外からは直接アクセスできない。
- 内部では` self.__変数名 `として使える。

**` @property `**
- 属性アクセスをメソッド経由で制御できる仕組み。
- ` getter `と` setter `を定義することで、値の取得や設定に条件を付けられる。
```python
class TeslaCar:
    def __init__(self, passwd='123'):
        self._enable_auto_run = False
        self.passwd = passwd

    @property
    def enable_auto_run(self):
        return self._enable_auto_run      # getter: 値を返す

    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        
        if self.passwd == '456':          # setter: 値を設定する際に条件をチェック
            self._enable_auto_run = is_enable
        else:
            raise ValueError("パスワードが違います")
``` 

<div align="right">
  <a href="../README.md#section7">◀️READMEに戻る<a>
</div>




