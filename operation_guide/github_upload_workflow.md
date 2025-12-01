## GitHubアップロード手順

ローカルで作成したパッケージをGithubにアップロードする手順

---
<div align="right"><a href="../README.md#4-手順">◀️ READMEに戻る</a></div>

### 1. GitHubでリポジトリを作成
- New repository作成：リポジトリ名 ` mypackage `
- 公開範囲を Public に設定

### 2. ローカルでGit初期化
- ローカルで Git 管理を始める準備
- プロジェクトフォルダ（mypackage/）で以下を実行：
```bash
cd C:\Users\teruy\Desktop\Python\Udemy\mypackage
git init       # Gitリポジトリとして初期化
git add .      # すべてのファイルをステージング領域(次のコミットに含めるファイルを一時的に置く場所)に追加
git commit -m "Initial commit: mypackage demo"
               # ステージングされたファイルをコミット（履歴として保存）
```

### 3. GitHubリポジトリと接続
- GitHubで作成したリポジトリのURLをコピーして、以下を実行：
```bash
git remote add origin https://github.com/chie-works/mypackage.git
                          # ローカルの Git リポジトリと GitHub 上のリポジトリを接続する
git branch -M main        # ローカルのブランチ名を「main」に変更する
git push -u origin main   # ローカルの変更を GitHub にアップロードする → Github上にローカルの内容が反映される
```

### 4. 公開後の確認
- ファイル一覧が表示されているか確認
- ` README.md `の確認
- コミット履歴の確認：` Initial commit: mypackage demo `が履歴に残っているか確認
- ブランチが` main `であることの確認
- 公開状態` Public `の確認
- 動作確認
```bash
import mypackage   # または import mypackage_copy
print(mypackage.hello())          # → Hello, world!
```
<div align="right"><a href="../README.md#4-手順">◀️ READMEに戻る</a></div>

