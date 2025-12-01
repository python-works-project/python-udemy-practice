## GitHubアップロード手順

---
### 1. GitHubでリポジトリを作成
- New repository作成：リポジトリ名 ` mypackage `
- - 公開範囲を Public に設定


### 2. ローカルでGit初期化
- ローカルで Git 管理を始める準備
- プロジェクトフォルダ（mypackage/）で以下を実行：
```bash
git init       # Gitリポジトリとして初期化
git add .      # すべてのファイルをステージング領域(次のコミットに含めるファイルを一時的に置く場所)に追加
git commit -m "Initial commit: mypackage demo"
               # ステージングされたファイルをコミット（履歴として保存）
```

### 3. GitHubリポジトリと接続
- GitHubで作成したリポジトリのURLをコピーして、以下を実行：
```bash
git remote add origin https://github.com/chie-works/mypackage.git
git branch -M main
git push -u origin main
```

### 4. 公開後の確認
