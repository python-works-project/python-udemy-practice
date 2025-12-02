## 68. Import文とAS
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section5">◀️READMEに戻る</a>
</div>

**パッケージフォルダ準備**
```
lesson_pakkege/         # パッケージフォルダ
  ├── __init__.py       # パッケージ初期化ファイル
  └── utils.py          # ユーティリティ関数を定義するモジュール
section06.py            # メインの実行ファイル
```
**utils.py の中身**
```python
def say_twaice(word):
    return (word + '!') * 2
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
## ✨ 学習のまとめ
- `__init__.py` があることで Python に「ここはパッケージだ」と認識させる
### ＜ importの基本形 ＞
**モジュール全体をインポート**
  - モジュール全体を読み込む
  - 呼び出すときは モジュール名.関数名
```python
import math
print(math.sqrt(16))   # → 4.0
```
**モジュールに別名をつける**
  - 長い名前を短くできる
  - 慣習的に numpy → np, pandas → pd など
```python
import numpy as np
print(np.array([1, 2, 3]))
```
**特定の関数やクラスだけをインポート**
  - 必要なものだけを直接使える
  - 呼び出しがシンプルになる
```python
from math import sqrt
print(sqrt(16))   # → 4.0
```
**複数まとめてインポート（推奨されない？）**
```python
from math import sqrt, pow
print(sqrt(9), pow(2, 3))
```
**ワイルドカード（推奨されない）**
  - 全部インポートするが、名前が衝突しやすく可読性が下がるため避ける
```python
from math import *
print(sqrt(16))
```



<div align="right">
  <a href="../README.md#section5">◀️READMEに戻る<a>
</div>
