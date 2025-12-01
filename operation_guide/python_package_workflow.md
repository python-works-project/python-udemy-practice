## 📝 Pythonパッケージ作成と動作確認手順

このドキュメントは、Pythonパッケージを最小構成で作成し、
ビルド・インストール・動作確認・クリーンアップまでの流れをまとめたものです。

- プロジェクトフォルダとパッケージ本体の準備
- `setup.py`/`README.md`/`LICENSE` の作成
- `python -m build` による配布物の生成
- `pip install` でのローカルインストールと動作確認
- 不要になったビルド成果物やインストール済みパッケージの削除

---
<div align="right"><a href="../README.md#4-手順">◀️ READMEに戻る</a></div>

### 1. プロジェクトフォルダの作成
```bash
mkdir mypackage
cd mypackage
```
### 2. パッケージ本体の作成
- フォルダ構成
```
mypackage/                 # プロジェクトフォルダ（全体の管理用）
 └── mypackage/            # パッケージ本体フォルダ
      ├── __init__.py      # パッケージの初期化ファイル（helloを公開）
      └── hello.py         # 実際の処理を記述するモジュール
```
- ` __init__.py `の中身
```python
from .hello import hello   # この記述で mypackage.hello() が直接呼べるようになる
```
- ` hello.py `の中身
```python
def hello(name="World"):
    return f"Hello, {name}!"
```
### 3. setup.py の作成
- ` setuptools `：Pythonの標準的なパッケージ配布ツール  
  パッケージをビルドしたり、インストール可能な形式（wheelやtar.gz）に変換するために使う
- ` setup `：パッケージのメタ情報を定義する関数  
  この情報が pip install や PyPI公開 の際に利用される
- ` find_packages `：パッケージフォルダを自動検出する関数  
  プロジェクトフォルダ内の` __init__.py `を含むディレクトリを探して、パッケージとして登録
```python
from setuptools import setup, find_packages

setup(
    name="mypackage",                          # パッケージ名（PyPI上での公開名）
    version="0.1.0",                           # バージョン番号（更新時に変更）
    packages=find_packages(),                  # パッケージとして含めるフォルダを自動検出
    author="Chie",                             # 作者名
    description="A simple demo package with hello()",  # 短い説明文
    license="MIT",                             # ライセンス種別
    long_description=open("README.md").read()  # PyPI公開時にREADMEが説明文に反映される
)
```

### 4. README.md と LICENSE の作成
- README.md
```python
# mypackage
A simple demo package that provides `hello(name)`.

## Usage
import mypackage
print(mypackage.hello("XXX"))
```

- LICENSE
```
MIT License

Copyright (c) 2025 chie

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 5. ビルド
- ` dist/ `フォルダに` .whl `と` .tar.gz `が生成される
```bash
pip install build  # 初回のみ
python -m build
```

### 6. ローカルインストールと動作確認
```bash
pip install dist/mypackage-0.1.0-py3-none-any.whl
```
```python
import mypackage
print(mypackage.hello("XXX"))
# 出力: Hello, XXX!
```

### 7. クリーンアップ（任意）
```bash
Remove-Item build, dist, *.egg-info -Recurse -Force
pip uninstall mypackage -y
```

<div align="right"><a href="../README.md#4-手順">◀️ READMEに戻る</a></div>

