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
        self.run(3)

    # run メソッドの定義
    def run(self, num):
        print('run' * num)

# Person クラスからインスタンスを生成（name に 'Mike' を渡す）
person = Person('Mike')

# インスタンスのメソッドを呼び出し
person.say_something()
# 出力例：
# I am Mike. hello
# runrunrun
```
## ✨ 学習のまとめ
**コンストラクタ**
- Python では` __init__ `がコンストラクタにあたる
- インスタンス生成時に自動で呼ばれる
- 主な役割は インスタンス変数の初期化 や 準備処理

**インスタンスメソッド**
- クラスの中で` def `で定義され、第一引数に` self `を取る
- ` self `は「そのインスタンス自身」を指す
- インスタンス変数を使った処理を記述できる

**インスタンス変数**
- クラスから作られたインスタンスが 個別に持つデータ
- ` self.変数名 `の形で定義される
- インスタンスごとに値が保持される（同じクラスでも別々の値を持てる）
- よくコンストラクタ` __init__ `の中で初期化される

```python
class Person:                  # クラス
    def __init__(self, name):  # コンストラクタ
        self.name = name       # インスタンス変数

    def say_hello(self):       # インスタンスメソッド
        print(f"Hello, I am {self.name}.")

# インスタンスを作成
p1 = Person("Mike")
p2 = Person("Nancy")

# インスタンスごとにメソッドを呼び出す
p1.say_hello()   # → Hello, I am Mike.
p2.say_hello()   # → Hello, I am Nancy.
```


<div align="right">
  <a href="../README.md#section7">◀️READMEに戻る<a>
</div>

