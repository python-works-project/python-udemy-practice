## 76. Importする際の記述の仕方
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section6">◀️READMEに戻る</a>
</div>

```python
# 標準ライブラリ
import collections
import os
import sys

# 外部ライブラリ（pip install termcolor で導入）
import termcolor

# 自作パッケージ
import mypackage.mypackage

# 自作モジュール
import config

# インポートの確認
print(collections.__file__)
print(termcolor.__file__)
print(mypackage.mypackage.__file__)
print(config.__file__)
```
## ✨ 学習のまとめ
- インポートの記述順

  1. 標準ライブラリ  
     例: import os, import sys, import math
  1. サードパーティライブラリ（pip install したもの）  
     例: import numpy, import pandas, import termcolor
  1. 自作モジュール  
     例: import mypackage
  1. ローカルパッケージ  
     例: import config

- 改行ルール
  - 各グループの間は 1 行空ける
  - 同じグループ内では改行しない（まとめて書く）
```python
import os
import sys

import numpy as np
import pandas as pd

import mypackage
import config
```
- アルファベット順に並べると見やすい（必須ではないが慣習的に多い）
- 不要な import は書かない（使わないなら削除）
- ワイルドカード import (from module import *) は避ける
- 名前空間が汚染されて可読性が下がるため

<div align="right">
  <a href="../README.md#section6">◀️READMEに戻る<a>
</div>
