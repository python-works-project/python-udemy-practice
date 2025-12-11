## 99. tarfileの圧縮展開
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section8">◀️READMEに戻る</a>
</div>

**圧縮ファイルを作成**
```python
with tarfile.open('test.tar.gz', 'w:gz') as tr:
    tr.add('test_dir')   # ディレクトリ test_dir を丸ごと追加 → test.tar.gz に保存
```

**圧縮ファイルを展開**
```pyton
with tarfile.open('test.tar.gz', 'r:gz') as tr:
    tr.extractall(path='test_tar')   # test_tar ディレクトリに展開

    # 展開せずに直接ファイルを読み込む場合
    with tr.extractfile('test_dir/sub_dir/sub_test.txt') as f:
        print(f.read())
```

## ✨ 学習のまとめ

**` tarfile.open(mode) `**
- ` w:gz ` ： gzip圧縮で書き込み
- ` r:gz ` ： gzip圧縮を読み込み

**` extractall() `**
- アーカイブ全体を展開する
- 展開先を path で指定可能

**` extractfile() `**
- 展開せずにアーカイブ内の特定ファイルを直接読み込める
- 戻り値はファイルオブジェクトなので read() で内容を取得


<div align="right">
  <a href="../README.md#section8">◀️READMEに戻る<a>
</div>




