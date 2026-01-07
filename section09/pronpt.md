```
Python で ROBOKO というプログラムを作りたいです。
以下の仕様を満たすコードを作成してください。

【仕様】
1. roboko.csv が存在する場合
   - CSV を DictReader で読み込み、rows（辞書のリスト）に格納する
   - count を整数として扱い、降順にソートする
   - ソートした rows を使って、shop_name を 1 件ずつユーザーに提示し、
     「このレストランは好きですか？(Yes/No)」と質問する
   - Yes/No の回答は count 更新には使わない（提示だけ）

2. roboko.csv が存在しない場合
   - rows は空のリストとして扱う

3. 最後にユーザーに好きなレストラン名を入力させる
   - rows の中に同じ shop_name があれば count を +1 する
   - 存在しなければ {"shop_name": 入力値, "count": "1"} を追加する

4. 最終的に rows 全体を roboko.csv に上書き保存する
   - ヘッダー（shop_name, count）を書き込む
   - writerows(rows) で全行を書き込む

【条件】
- CSV の count は文字列で保存する
- 大文字小文字の違いは無視して比較する
- 日本語の店名も扱えるようにする
- コードは 1 ファイルで完結させる
- termcolor を使って colored() でメッセージを色付けする
以上を満たす Python コードを作成してください。
```

