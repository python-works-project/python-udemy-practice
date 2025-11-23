print('********************************')
print('* 【引用符】')
print('********************************')
print("I don't know")
print('say "I don\'t know"')
print('saを使用してdon\'t know"')
print("say \"I don't know\"")

print('********************************')
print('* 【改行】')
print('********************************')
print('Hello. \nHow are you?')
print(r'c:\name\name')
# - 複数行の改行
print("""\
line1
line2
line3\
""")

print('********************************')
print('* 【文字列の連結】')
print('********************************')
print('Hi.' * 3 + 'Mike')
print('Py' + 'thon')
print('Py''thon')
prefix = 'Py'
print(prefix + 'thon')
s = ('aaaaaaaaaaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbbbbbbbbbb')
print(s)
ss = 'aaaaaaaaaaaaaaaaaaaaaaaa' \
     'bbbbbbbbbbbbbbbbbbbbbbbb'
print(ss)

print('********************************')
print('* 【インデックス】')
print('********************************')
word = 'python'
print(word[3])
print(word[-1])

print('********************************')
print('* 【スライス】')
print('********************************')
print(word[0:2])
print(word[:2])
print(word[2:])
print(word[2:5])
word = 'j' + word[1:]
print(word)
print(word[:])

print('********************************')
print('* 【文字長】')
print('********************************')
print(len(word))

print('********************************')
print('* 【文字列のメソッド】')
print('********************************')
s = 'My name is Mike. Hi Mike.'
print(s)
is_start = s.startswith('My')
print(is_start)
is_start = s.startswith('XX')
print(is_start)
print(s.find('Mike'))
print(s.rfind('Mike'))
print(s.count('Mike'))
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.replace('Mike','Nancy'))
