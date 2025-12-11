## 101. tempfile
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section8">◀️READMEに戻る</a>
</div>

**使用ライブラリ**
```python
import tempfile
```

**一時ファイル（TemporaryFile）**
```python
with tempfile.TemporaryFile(mode='w+') as t:
    t.write('hello')         # 一時ファイルに文字列を書き込み
    t.seek(0)
    print(t.read())
    # このファイルは with ブロックを抜けると自動的に削除される
```

**名前付き一時ファイル（NamedTemporaryFile）**
```python
with tempfile.NamedTemporaryFile(delete=False) as t:
    print('t.name = ', t.name)  # 一時ファイルのパスを表示（通常は OS の temp フォルダ内）
    with open(t.name, 'w+') as f:
        f.write('***test***\n')
        f.seek(0)
        print(f.read())
    # delete=False にしているので、with を抜けてもファイルは残る
```

**一時ディレクトリ（TemporaryDirectory）**
```python
with tempfile.TemporaryDirectory() as td:
    print(td)  # 一時ディレクトリのパスを表示
    # with を抜けるとディレクトリは自動的に削除される
```

**一時ディレクトリ（mkdtemp）**
```python
temp_dir = tempfile.mkdtemp()
print(temp_dir)
# mkdtemp は一時ディレクトリを作成してパスを返すが、自動削除はされない
```
## ✨ 学習のまとめ
**` TemporaryFile `**
- ` 匿名 `の一時ファイルを作成
- ` with `ブロック終了時に自動削除
**` NamedTemporaryFile `**
- ` 名前付き `の一時ファイルを作成
- ` delete=False `を指定すると終了後も残る
- ` t.name `でファイルパスを取得できる
**` TemporaryDirectory `**
- 一時ディレクトリを作成
- ` with `ブロック終了時に自動削除
**` mkdtemp `**
- 一時ディレクトリを作成してパスを返す
- 自動削除されないので、不要になったら手動で削除が必要


<div align="right">
  <a href="../README.md#section8">◀️READMEに戻る<a>
</div>




