## 98. ファイル操作
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section8">◀️READMEに戻る</a>
</div>

**使用するライブラリ**
```python
import os
import pathlib
import glob
import shutil
```

**ファイルやディレクトリの存在確認**
```python
print(os.path.exists('test.txt'))   # 'test.txt' が存在するかどうか（True/False）
print(os.path.isfile('test.txt'))   # 'test.txt' が「ファイル」かどうか
print(os.path.isdir('test.txt'))    # 'test.txt' が「ディレクトリ」かどうか
print(os.path.isdir('design'))      # 'design' がディレクトリかどうか
```

**ファイル操作**
```python
os.rename('test.txt', 'rename.txt')     # ファイル名を変更（test.txt → rename.txt）
os.symlink('rename.txt', 'symlink.txt') # シンボリックリンクを作成（rename.txt → symlink.txt）
```

**ディレクトリ作成と削除**
```python
os.mkdir('test_dir')    # ディレクトリを作成
os.rmdir('test_dir')    # 空のディレクトリを削除
```

**ファイル作成と削除**
```python
pathlib.Path('empty.txt').touch()  # 空ファイルを作成（存在しなければ新規作成）
os.remove('empty.txt')             # ファイルを削除
```

**ネストしたディレクトリ操作**
```Python
os.mkdir('test_dir')               # test_dir を作成
os.mkdir('test_dir/test_dir2')     # test_dir 内に test_dir2 を作成
print(os.listdir('test_dir'))      # test_dir 内の一覧を表示 → ['test_dir2']
```

**ファイルコピー**
```python
pathlib.Path('test_dir/test_dir2/empty.txt').touch()  # 空ファイルを作成
shutil.copy('test_dir/test_dir2/empty.txt',           # コピー元
            'test_dir/test_dir2/empty2.txt')          # コピー先
print(glob.glob('test_dir/test_dir2/*'))              # パターンに一致するファイル一覧を取得
```

**ディレクトリごと削除**
```python
shutil.rmtree('test_dir')          # test_dir 以下を再帰的に削除
```

**カレントディレクトリの表示**
```python
print(os.getcwd())                 # 現在の作業ディレクトリを表示
```
## ✨ 学習のまとめ
1. 存在確認
- ` os.path.exists(path) `： ファイル/ディレクトリが存在するか
- ` os.path.isfile(path) `： ファイルかどうか
- ` os.path.isdir(path) `： ディレクトリかどうか
2. ファイル操作
- ` os.rename(src, dst) `： ファイル名変更
- ` os.symlink(src, dst) `： シンボリックリンク作成（Windowsでは開発者モードが必要）
3. ディレクトリ操作
- ` os.mkdir(path) `： 新規ディレクトリ作成
- ` os.rmdir(path) `： 空ディレクトリ削除
- ` os.listdir(path) `： ディレクトリ内の一覧取得
4. ファイル作成・削除
- ` pathlib.Path(path).touch() `： 空ファイル作成（存在すれば更新日時変更）
- ` os.remove(path) `： ファイル削除
5. ネストしたディレクトリ
- ` os.mkdir('test_dir/test_dir2') `： 階層的に作成（親が存在している必要あり）
6. ファイルコピー
- ` shutil.copy(src, dst) `： ファイルをコピー
- ` glob.glob(pattern) `： パターンに一致するファイル一覧取得（例: *.txt）
7. ディレクトリごと削除
- ` shutil.rmtree(path) `： ディレクトリ以下を再帰的に削除（中身ごと削除）
8. カレントディレクトリ
- ` os.getcwd() `： 現在の作業ディレクトリを取得

<div align="right">
  <a href="../README.md#section8">◀️READMEに戻る<a>
</div>




