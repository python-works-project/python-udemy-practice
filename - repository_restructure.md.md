# 🗂️ GitHubリポジトリのクローンとフォルダ構成整理

学習ログの途中で、フォルダ構成とファイル名を整理しました。
再現できるように、手順とコマンドを一つのドキュメントにまとめます。

---

## 手順1： GitHubからリポジトリURLを取得
- **対象リポジトリ:** `chie-works/python_study`
- **操作:** 「Code」ボタン → 「HTTPS」タブ → URLをコピー
- **コピーしたURL:** https://github.com/chie-works/python_study.git

## 手順2： Git Bashでローカルにクローン
```bash
cd /c/Users/XXXX/Desktop/作業用
git clone https://github.com/chie-works/python_study.git
cd python_study
```
## 手順3： フォルダ名の変更
```bash
mv logs section03
mv src section04
```

## 手順4： ファイルの移動
```bash
mv section03/section04_16.md section04/
mv section03/section04_17.md section04/
```

## 手順5： Gitユーザー情報の設定（初回のみ）
```bash
git config --global user.name "Chie Works"
git config --global user.email "chie@example.com"
```
## 手順6： Gitへの反映（コミット＆プッシュ）
```bash
git add -A
git commit -m "Restructure folders: logs→section03, src→section04, moved section04 files"
git push origin main
```

## 手順7： 結果確認
GitHub上の python_study リポジトリにて、以下の構成に変更されていることを確認：
```bash
python_study/
 ├─ section03/
 │   ├─ section03_14.md
 │   └─ section03_15.md
 └─ section04/
     ├─ section04_16.md
     └─ section04_17.md
```
