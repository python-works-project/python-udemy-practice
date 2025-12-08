## 85. ダックタイピング
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section7">◀️READMEに戻る</a>
</div>

**基底クラス Person**
```python
class Person(object):
    def __init__(self, age=1):
        self.age = age

    def drive(self):
        if self.age >= 18:
            print('OK')
        else:
            print('NG')
```
**Baby クラス**
```python
# 18歳未満の人しかインスタンス化できないクラス
class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)   # Person の初期化を呼ぶ
        else:
            raise ValueError        # 18歳以上ならエラー
```

**Adult クラス**
```python
# 18歳以上の人しかインスタンス化できないクラス
class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)   # Person の初期化を呼ぶ
        else:
            raise ValueError        # 18歳未満ならエラー
```

**インスタンス生成**
```python
baby = Baby()     # age=1
adult = Adult()   # age=18
```

**Car クラス**
```python
class Car(object):
    def __init__(self):
        pass
    def ride(self, person):
        # ダックタイピングのポイント：
        # 渡されたオブジェクトが「drive() メソッド」を持っていれば呼び出せる
        # Person, Baby, Adult いずれも drive() を持つので問題なく動作する
        person.drive()
```

**Car に Baby と Adult を渡してみる**
```python
car = Car()
car.ride(baby)   # → baby.drive() が呼ばれる → 'NG' と表示
car.ride(adult)  # → adult.drive() が呼ばれる → 'OK' と表示
```

## ✨ 学習のまとめ
**ダックタイピングとは：**
- 型を意識せず「必要なメソッドを持っているか」で判断する柔軟な設計

**ダックタイピングの考え方**
- ` Car `クラス の` ride() `は「` 渡されたオブジェクトが drive() を持っているか `」だけを期待。
- ` Baby `でも` Adult `でも`、Person `を継承しているので` drive() `を持つ。
- 型チェックはしていない → 「アヒルのように鳴けばアヒル」 の考え方。
- 型よりも振る舞い（メソッドの有無）を重視するのがダックタイピング。

<div align="right">
  <a href="../README.md#section7">◀️READMEに戻る<a>
</div>




