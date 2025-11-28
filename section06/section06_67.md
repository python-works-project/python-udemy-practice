## 67. コマンドライン引数
#### 🖥 VSCode／ターミナル／lanch.jsonで実行
<div align="right">
  <a href="../README.md#section5">◀️READMEに戻る</a>
</div>

**` launch.json ` に ` args ` を追加してデバッグ実行
```python
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python デバッガー: 現在のファイル",
            "type": "debugpy",
            "request": "launch",
            "program": "${file}",
            "args": ["arg1", "arg2"],   // ← ここで引数を指定
            "console": "internalConsole"
        }
    ]
}
```
- VSCodeの「Run and Debug」で実行すると、` sys.argv ` に ` ["ファイル名", "arg1", "arg2"] `が入る
- デバッグ環境専用の設定（ブレークポイントやステップ実行が可能）

**Pythonコード例**
```python
# Pythonの標準ライブラリsysをインポート（コマンドライン引数などを扱える）
import sys

# コマンドライン引数をリスト形式で表示
print(sys.argv)     # sys.argv[0] はスクリプト名、それ以降が渡された引数

# sys.argvの各要素を順番に取り出すループ
for i in sys.argv:
    print(i)
```

**ターミナルからの実行コマンド**
```bach
PS C:\Users\XXXX\Desktop\Python\Udemy> python section06.py option1 option2
```
- Pythonインタプリタを起動し、section06.py を実行
- ` option1 ` と ` option2 ` がコマンドライン引数として渡される
- ` sys.argv ` の中身は` ["section06.py", "option1", "option2"] `

## ✨ 学習のまとめ
**コマンドライン引数とは**
- プログラムを実行するときに、コマンドライン（ターミナルやコマンドプロンプト）から渡す追加の情報のこと
- Pythonでは `sys.argv` というリストに格納され、スクリプト内で利用できる
- すべて文字列として渡されるので、数値として使いたい場合は `int()` や `float()` に変換する必要がある

**【 lanch.jsonの`args` 】**
- VSCodeの`「Run and Debug」`機能で実行したときのみ有効
- VSCodeのデバッガー (debugpy) が起動し、`launch.json` に書かれた `args` を `sys.argv` に渡す
- デバッグ環境でのみ反映される
- env や cwd など他の設定も同時に適用される

**【 ターミナルで引数指定 】**
- VSCodeの統合ターミナルや外部のシェルから直接 `python main.py arg1 arg2` のように実行した場合
- OSのシェルがそのまま Python に引数を渡し、`sys.argv` に格納される
- launch.json の設定は無視される
- デバッグ機能は使えない
