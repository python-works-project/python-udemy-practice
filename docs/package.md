## Pythonパッケージ配布手順
<div align="right"><a href="../README.md#section5">◀️READMEに戻る</a></div>

### 1. VSCodeでパッケージ作成
- 各フォルダに ` __init__.py ` の用意
- setup.py を作成
```python
from setuptools import setup, find_packages

setup(
    name='lesson_package',
    version='1.0.0',
    packages=find_packages(),
    url='https://github.com/chie-works/python_study/',
    license='MIT',
    author='chie',
    author_email='',
    description='sample package'
)
```
- ' README.md ' を作成
- ` LISENCE ` を作成
```bash
lesson_package_project/        ← プロジェクト全体のルートフォルダ（任意の名前）
├── lesson_package/            ← 実際のパッケージ本体
│   ├── __init__.py
│   ├── talk/
│   │   ├── __init__.py
│   │   ├── animal.py
│   │   └── human.py
│   └── tools/
│       ├── __init__.py
│       └── utils.py
├── setup.py                   ← パッケージ定義ファイル
├── README.md                  ← 説明文（GitHubやPyPIに表示される）
├── LICENSE                    ← ライセンス（MITなど）
```
### 2. Githubにパッケージ用のリポジトリを用意し、ローカルのパッケージをpush
- このフォルダを Git管理対象にする（初期化）
```bash
git init
```
- このフォルダ内のすべてのファイルをステージング
```bash
git add .
```
- ステージングされたファイルを 履歴として保存（＝「最初のスナップショット」）
- "initial commit" は履歴のメモ
```bash
git commit -m "initial commit"
```

- 現在のブランチ名を main に変更（GitHubの標準に合わせる）
```bash
git branch -M main
```

- GitHubのリポジトリと紐付ける
```bash
git remote add origin https://github.com/chie-works/lesson_package.git
```

- ローカルの履歴を GitHubに送る（push）
```bash
git push -u origin main
```

### 3. 動作確認
- GithubにあげたパッケージをローカルのPython環境にインストールし、動作確認をする
```bash
pip install -e .
```
- Python REPLを起動して確認
```bash
>>> import lesson_package
>>> lesson_package.__doc__
```

## 7. importテストで動作確認
## 8. Gitで管理開始 (git init)
## 9. コミット (git add . → git commit)
## 10. GitHubに新しいリポジトリを作成
## 11. リモートを追加 (git remote add origin ...)
## 12. push (git push -u origin main)
## 13. GitHub上でREADMEとLICENSEを確認
## 14. （任意）python -m build で配布物を生成
## 15. （任意）PyPIにアップロード (twine upload dist/*)

<div align="right"><a href="../README.md#section5">◀️READMEに戻る</a></div>
