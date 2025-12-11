## 96. テンプレート
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section8">◀️READMEに戻る</a>
</div>

```python
import string

# テンプレート文字列を定義
s = """\
Hi $name.

$contents

Have a good day
"""

# Templateオブジェクトを作成
t = string.Template(s)

# substitute() でプレースホルダを置換
contents = t.substitute(name='Mike', contents='How are you')
print(contents)
# 出力:
# Hi Mike.
#
# How are you
#
# Have a good day
```
**外部ファイルからテンプレートを読み込む場合**
```
# 外部ファイル：design/template.txtの中身
Hi $name.

$contents

Have a good day
```
```python
with open('design/template.txt') as f:
    # ファイルの内容をテンプレートとして読み込む
    t = string.Template(f.read())

# substitute() でプレースホルダを置換
contents = t.substitute(name='Nancy', contents='Good morning')
print(contents)
# 出力例
# Hi Nancy.
#
# Good morning
#
# Have a good day
```
## ✨ 学習のまとめ
**` string.Template `**
- ` $変数名 `の形式でプレースホルダを定義できる。
- ` substitute() `で辞書やキーワード引数を渡すと置換される。
**` substitute() `と` safe_substitute() `の違い**
- ` substitute() `： プレースホルダが不足するとエラー。
- ` safe_substitute() `： プレースホルダが不足してもそのまま残す。

<div align="right">
  <a href="../README.md#section8">◀️READMEに戻る<a>
</div>




