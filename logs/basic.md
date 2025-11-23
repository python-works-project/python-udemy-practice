# 📘 学習ログ：Basic

## 🗂️ 学習日・環境
- 日付：2025年11月23日
- 実行環境：VSCode + Python 3.11（venv使用）
- ファイル名：`format.py`
- 章リンク：[src/basic/format.py](../src/basic/format.py)

---

## 🧪 実行コマンドと出力結果

```bash
# 基本的な format の使い方
>>> 'a is {}'.format('a')
'a is a'

# {} に別の文字列を埋め込む
>>> 'a is {}'.format('test')
'a is test'

# 複数の値を埋め込む
>>> 'a is {} {} {}'.format(1,2,3)
'a is 1 2 3'

# インデックス指定
>>> 'a is {0} {1} {2}'.format(1,2,3)
'a is 1 2 3'

# インデックス指定の応用
>>> 'My name is {0} {1}.Watashiwa {1} {0} desu'.format('aaa','bbb')
'My name is aaa bbb.Watashiwa bbb aaa desu'

# キーワード引数を使った埋め込み
>>> 'My name is {name} {family}. Watashiwa {family} {name} desu'.format(name='aaa',family='bbb')
'My name is aaa bbb. Watashiwa bbb aaa desu'

# 数値そのものを表示
>>> 1
1

# 文字列として表示
>>> '2'
'2'

# 数値を文字列に変換し、型を確認
>>> x = 1
>>> x = str(1)
>>> type(x)
<class 'str'>
