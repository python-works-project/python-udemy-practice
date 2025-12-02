## 69. 絶対パスと相対パスのImport
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section6">◀️READMEに戻る</a>
</div>


**フォルダ構成**
```python
lesson_pakkege/             # パッケージフォルダ
    ├── talk/               # サブパッケージ
    │    ├── __init__.py
    │    └── human.py
    └── tools/              # サブパッケージ
        ├── __init__.py
        └── utils.py
section06.py                # メインの実行ファイル
```
**utils.py の中身**
```python
def say_twaice(word):
    return (word + '!') * 2
```
**human.py の中身**
```python
# 絶対パスの場合
from lesson_pakkege.tools import utils

# 相対パスの場合
from ..tools import utils

def sing():
    return 'sing'

def cry():
    # tools.utils の say_twaice 関数を呼び出し
    return utils.say_twaice('cry')
```
**section06.pyの中身**
```Python
from lesson_pakkege.talk import human

print(human.sing())
print(human.cry())
# 出力
# sing
# cry!cry!
```


<div align="right">
  <a href="../README.md#section6">◀️READMEに戻る<a>
</div>
