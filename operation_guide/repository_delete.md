# 学習ログ：GitHubリポジトリからファイル削除

## 対象ファイル
- リポジトリ: chie-works
- フォルダ: section04
- ファイル: section03_code.py

---

## 手順（ターミナル）

1. リポジトリのルートへ移動
```bash
cd chie-works
```
2. ファイルを削除してステージング
```bash
git rm section04/section03_code.py
```
- ※もし単純に削除した場合は rm section04/section03_code.py → git add -u でステージング。
3. コミット
```bash
git commit -m "Remove section03_code.py from section04"
```
4. リモートへプッシュ
```bash
git push origin main
```

## 補足
- 誤って削除した場合は復元可能：
```bash 
git checkout HEAD -- section04/section03_code.py
```
