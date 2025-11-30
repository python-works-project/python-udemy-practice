## Pythonパッケージ配布手順
<div align="right"><a href="../README.md#section5">◀️READMEに戻る</a></div>

## 1. VSCodeでパッケージ作成
- 各フォルダに ` __init__.py ` の用意
- setup.py を作成
```python
# from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name='lesson_package',
    version='1.0.0',
    # packages=[
    #     'lesson_package',
    #     'lesson_package.talk',
    #     'lesson_package.tools',
    #           ],
    packages=find_packages(),
    url='https://github.com/chie-works/python_study/',
    # license='Free',
    license='MIT',
    author='chie',
    author_email='',
    description='sample package'
)
```
- ' README.md ' を作成
- ` LISENCE `はGithubで自動作成
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
## 2. Githubにパッケージ用のリポジトリを用意し、  
ローカルのパッケージをpush
- このフォルダを Git管理対象にする（初期化）
- これにより` .git ` という隠しフォルダが作られ、履歴管理が始まる
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

# 現在のブランチ名を` main `に変更（GitHubの標準に合わせる）
# ` -M ` は「強制的に変更する」という意味
git branch -M main

# GitHubのリポジトリと紐付ける
# ' origin 'はリモートの名前。通常はこれでOK
git remote add origin https://github.com/chie-works/lesson_package.git

# ローカルの履歴を GitHubに送る（push）
# '-u 'は「今後もこのリモートとブランチを使う」という設定
git push -u origin main
```

## 3. LICENSE を追加（MIT推奨、今回はGitHubで生成）
## 6. 開発モードでインストール (pip install -e .)
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
