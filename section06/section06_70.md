## 70. アスタリスクのImportと__init__.pyと__all__の意味
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section5">◀️READMEに戻る</a>
</div>

**フォルダ構成**
```python
lesson_pakkege/             # パッケージフォルダ
    └── talk/               # サブパッケージ
         ├── __init__.py
         └── animal.py
         └── human.py
section06.py                # メインの実行ファイル
```
**__init__.pyの中身**
```python
__all__ = ['animal']
```

**section06.pyの中身**
```Python
# パッケージの __init__.py で定義された公開モジュールをすべて読み込む
from lesson_pakkege.talk import *

# __init__.pyに記述してあるのでエラーにならない
print(animal.sing())
print(animal.cry())

# __init__.pyに記述してないでエラーになる
print(human.sing())
print(human.cry())
```

<div align="right">
  <a href="../README.md#section5">◀️READMEに戻る<a>
</div>
