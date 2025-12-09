## 87. 多重継承
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section7">◀️READMEに戻る</a>
</div>

```python
# 親クラス Person
class Person(object):
    def talk(self):               # Person固有のメソッド
        print('talk')

    def run(self):                # Personのrunメソッド
        print('person run')


# 親クラス Car
class Car(object):
    def run(self):                # Carのrunメソッド
        print('run')


# 多重継承クラス
# class PersonCarRobot(Person, Car):   # ← この場合はPerson優先
class PersonCarRobot(Car, Person):     # ← この場合はCar優先
    def fly(self):                     # 独自メソッド
        print('fly')


# インスタンス生成
person_car_robot = PersonCarRobot()

person_car_robot.talk()   # → 'talk'
person_car_robot.run()    # → 'run'　：runメソッドはCarが先に継承されているため、Carのrunが呼ばれる
person_car_robot.fly()    # → 'fly'
```
## ✨ 学習のまとめ
- ` PersonCarRobot(Car, Person) `のように複数の親クラスを指定できる
- ` Python `は左から順に親クラスを探索する
- 継承順序を変えるだけで呼ばれるメソッドが変わるため、設計時には注意が必要
- 実務では「ダイヤモンド継承問題」を避けるために、` super() `を正しく使うことが推奨されます





<div align="right">
  <a href="../README.md#section7">◀️READMEに戻る<a>
</div>




