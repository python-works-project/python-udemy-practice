## 75. サードパーティのライブラリ
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section5">◀️READMEに戻る</a>
</div>

**pypiにある関数をインストール**
```bash
pip install termcolor
```
**インストールした関数を使用**
```python
from termcolor import colored

print('test')

print(colored('test', 'red'))

print(help(colored))
```
