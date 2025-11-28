## 67. コマンドライン引数
#### 🖥 VSCode／ターミナル／lanch.jsonで実行
<div align="right">
  <a href="../README.md#section5">◀️READMEに戻る</a>
</div>

## ✨ 学習のまとめ
**コマンドライン引数とは**
- プログラムを実行するときに、コマンドライン（ターミナルやコマンドプロンプト）から渡す追加の情報のこと
- Pythonでは `sys.argv` というリストに格納され、スクリプト内で利用できる
- すべて文字列として渡されるので、数値として使いたい場合は `int()` や `float()` に変換する必要がある

**lanch.jsonの`args`**
- 対象: VSCodeの`「Run and Debug」`機能で実行したときのみ有効
- 仕組み: VSCodeのデバッガー (debugpy) が起動し、`launch.json` に書かれた `args` を `sys.argv` に渡す
- デバッグ環境でのみ反映される
- env や cwd など他の設定も同時に適用される

**ターミナルで引数指定**
- 対象: VSCodeの統合ターミナルや外部のシェルから直接 `python main.py arg1 arg2` のように実行した場合
- 仕組み: OSのシェルがそのまま Python に引数を渡し、`sys.argv` に格納される
- launch.json の設定は無視される
- デバッグ機能は使えない
