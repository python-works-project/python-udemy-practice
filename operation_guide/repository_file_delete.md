## 📝 作業手順：GitHubリポジトリからファイル削除

不要なファイルを削除する際に、GitHub上で削除できなかったため、ローカル環境にて行いました。  
再現できるように、手順とコマンドを一つのドキュメントにまとめます。

---
#### 対象ファイル
- リポジトリ: chie-works
- フォルダ: section04
- ファイル: section03_code.py
---

#### 手順1： リポジトリのルートへ移動
```bash
cd section04
$ dir
```
#### 手順2： ファイルを削除してステージング
```bash
git rm section04/section03_code.py
```
※もし単純に削除した場合は rm section04/section03_code.py → git add -u でステージング。
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
