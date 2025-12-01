## 📝 GitHubリポジトリからファイル削除

不要なファイルを削除する際に、GitHub上で削除できなかったため、ローカル環境にて行いました。  
再現できるように、手順とコマンドを一つのドキュメントにまとめます。

---
#### 対象ファイル
- リポジトリ: chie-works
- フォルダ: section04
- ファイル: section03_code.py
---
#### 手順1： ローカルの状態を確認
```bash
# 未コミットの変更があるかどうかを確認
$ git status

# 結果: 未コミットの変更は一切なく、作業ツリーはクリーン
# 意味: ローカルの main ブランチはリモートと同期済みで最新状態
On branch main
Your branch is up to date with 'origin/main'.
nothing to commit, working tree clean
```
#### 手順2： ローカルを最新化
```bash
git pull origin main
```
#### 手順3： コミット
```bash
git commit -m "Remove section03_code.py from section04"
```
#### 手順4： リモートへプッシュ
```bash
git push origin main
```

### 補足
- 誤って削除した場合は復元可能：
```bash 
git checkout HEAD -- section04/section03_code.py
```
