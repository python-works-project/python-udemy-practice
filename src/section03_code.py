
# --- 文字列のクォートの使い方 ---
print("I don't know")              # ダブルクォートで囲めば、内部のシングルクォートをそのまま使える
print('say "I don\'t know"')       # シングルクォートで囲み、内部のシングルクォートはエスケープ
print("say \"I don't know\"")      # ダブルクォート内のダブルクォートはエスケープ

# --- 改行やエスケープシーケンス ---
print('Hello. \nHow are you?')     # \n で改行
print(r'c:\name\name')             # r'' で「raw文字列」→ エスケープを無効化

# --- 複数行文字列 ---
print("""\
line1
line2
line3\
""")                               # """...""" で複数行文字列を表現

# --- 文字列の結合と繰り返し ---
print('Hi.' * 3 + 'Mike')          # 'Hi.' を3回繰り返して 'Mike' を結合
print('Py' + 'thon')               # 文字列の結合 → 'Python'
print('Py''thon')                  # 隣接文字列は自動結合 → 'Python'
prefix = 'Py'
print(prefix + 'thon')             # 変数と文字列の結合

# --- 長い文字列の分割記述 ---
s = ('aaaaaaaaaaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbbbbbbbbbb')  # () 内の隣接文字列は自動結合
print(s)

ss = 'aaaaaaaaaaaaaaaaaaaaaaaa' \
     'bbbbbbbbbbbbbbbbbbbbbbbb'   # バックスラッシュで改行を継続
print(ss)

# --- インデックスとスライス ---
word = 'python'
print(word[3])     # インデックス3 → 'h'
print(word[-1])    # インデックス-1 → 最後の文字 'n'

print(word[0:2])   # 0〜1 → 'py'
print(word[:2])    # 先頭から2文字 → 'py'
print(word[2:])    # 2文字目以降 → 'thon'
print(word[2:5])   # 2〜4 → 'tho'

word = 'j' + word[1:]  # 先頭を 'j' に置き換え → 'jython'
print(word)
print(word[:])     # 全体をスライス → 'jython'

print(len(word))   # 文字列の長さ → 6

# --- 文字列メソッド ---
s = 'My name is Mike. Hi Mike.'
print(s)

is_start = s.startswith('My')   # 'My' で始まるか → True
print(is_start)

is_start = s.startswith('XX')   # 'XX' で始まるか → False
print(is_start)

print(s.find('Mike'))           # 最初の 'Mike' の位置 → 11
print(s.rfind('Mike'))          # 最後の 'Mike' の位置 → 19
print(s.count('Mike'))          # 'Mike' の出現回数 → 2

print(s.capitalize())           # 先頭を大文字に → 'My name is mike. hi mike.'
print(s.title())                # 単語ごとに先頭大文字 → 'My Name Is Mike. Hi Mike.'
print(s.upper())                # 全て大文字 → 'MY NAME IS MIKE. HI MIKE.'
print(s.lower())                # 全て小文字 → 'my name is mike. hi mike.'
print(s.replace('Mike','Nancy'))# 'Mike' を 'Nancy' に置換
