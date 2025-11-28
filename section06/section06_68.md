## 68. Import文とAS
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section5">◀️READMEに戻る</a>
</div>

**パッケージフォルダ準備**
```
lesson_pakkege/         # パッケージフォルダ
  ├── init.py           # パッケージ初期化ファイル
  └── utils.py          # ユーティリティ関数を定義するモジュール
section06.py            # メインの実行ファイル
```

**パッケージ全体をインポート**
```python
import lesson_pakkege.utils
r = lesson_pakkege.utils.say_twaice('hello') 
```

**パッケージから特定のモジュールをインポート**
```python
from lesson_pakkege import utils
r = utils.say_twaice('Good morning')  
```

**モジュールから特定の関数だけを直接インポートする方法**
```python
from lesson_pakkege.utils import say_twaice
r = say_twaice('Goodbay') 
```

**モジュールに別名（エイリアス）をつけてインポートする方法**
```python
from lesson_pakkege import utils as u
r = u.say_twaice('Good morning')
```

<div align="right">
  <a href="../README.md#section5">◀️READMEに戻る<a>
</div>
