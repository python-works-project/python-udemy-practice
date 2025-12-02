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
**コンストラクタ**：Python では` __init__ `がコンストラクタにあたる
- 初期化処理を行う  
  →` obj = ClassName(...) `とした瞬間に` __init__ `が実行される  
  → 主な使い所は「インスタンス変数の初期化」「準備処理」

**インスタンスのメソッド**：クラスの中で` def `で定義され、第一引数に` self `を取る
```python
class Person:
    def __init__(self, name):
        self.name = name   # インスタンス変数

    def say_hello(self):   # インスタンスメソッド
        print(f"Hello, I am {self.name}.")

# インスタンスを作成
p1 = Person("Mike")
p2 = Person("Nancy")

# インスタンスごとにメソッドを呼び出す
p1.say_hello()   # → Hello, I am Mike.
p2.say_hello()   # → Hello, I am Nancy.
```
**インスタンス変数**：クラスから作られたインスタンス（オブジェクト）が個別に持つデータ
- クラスの中で self.変数名 の形で定義される
- インスタンスごとに値が保持される（同じクラスでも別々の値を持てる）
- コンストラクタ __init__ の中でよく初期化される


<div align="right">
  <a href="../README.md#section7">◀️READMEに戻る<a>
</div>

