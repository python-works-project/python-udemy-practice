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

# 変数に数値を代入
>>> x = 1

# 数値を文字列に変換
>>> x = str(1)

# 型を確認
>>> type(x)
<class 'str'>
