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
