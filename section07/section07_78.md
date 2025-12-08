## 78. クラスの定義
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section7">◀️READMEに戻る</a>
</div>


```python
# class Person():      # Python2の古い書き方（継承先を明示していない）
# class Person:        # Python3以降では () を省略して書ける（object を暗黙的に継承する）
class Person(object):  # 明示的に object を継承する書き方（Python2 ではこれが推奨されていた）
    def say_something(self):     # インスタンスメソッドの定義
        print('hello') 

person = Person()        # Person クラスからインスタンスを生成

person.say_something()   # インスタンスのメソッドを呼び出し
```
## ✨ 学習のまとめ
**Python クラスの基本構造**
```python
class クラス名:
    # クラス変数（全インスタンスで共有）
    クラス変数 = 値

    def __init__(self, 引数1, 引数2, ...):
        # インスタンス変数（インスタンスごとに独立）
        self.変数1 = 引数1
        self.変数2 = 引数2

    # メソッド（インスタンス専用の処理）
    def メソッド名(self, 引数...):
        # self を通じてインスタンス変数にアクセス
        return self.変数1
```
**使い方**
1. インスタンス生成
```
インスタンス = クラス名(初期化引数...)
```
2. インスタンス変数の利用
```
クラス変数の利用
```
3. メソッドの呼び出し
```
インスタンス.メソッド名(引数...)
```
4. クラス変数の利用
```
クラス名.変数名
```
