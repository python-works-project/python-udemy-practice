## 71. ImportErrorの使い所
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section5">◀️READMEに戻る</a>
</div>

```python
try:
    from lesson_pakkege import utils
except ImportError: 
    from lesson_pakkege.tools import utils

utils.say_twaice('word')
```
## ✨ 学習のまとめ
- パッケージのバージョンの切り分けをする際に使用する 
