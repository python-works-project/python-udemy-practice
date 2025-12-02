## 79. クラスの初期化とクラス変数
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section7">◀️READMEに戻る</a>
</div>

```python
class Person(object):
    # コンストラクタ（インスタンス生成時に呼ばれる）
    def __init__(self, name):
        # インスタンス変数 name に引数を代入
        self.name = name
        print('First:', self.name)

    # インスタンスメソッドの定義
    def say_something(self):
        # インスタンス変数 self.name を使って文字列を出力
        print('I am {}. hello'.format(self.name))
        # run メソッドを呼び出し、引数 3 を渡す
        self.run(3)

    # run メソッドの定義
    def run(self, num):
        # 'run' を num 回繰り返して出力
        print('run' * num)

# Person クラスからインスタンスを生成（name に 'Mike' を渡す）
person = Person('Mike')

# インスタンスのメソッドを呼び出し
person.say_something()
# 出力例：
# I am Mike. hello
# runrunrun
```
