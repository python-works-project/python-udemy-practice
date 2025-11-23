# Chapter 1: Python基礎

## ターミナル実行ログ
```python
>>> 'a is {}'.format('a')
'a is a'
>>> 'a is {}'.format('test')
'a is test'
>>> 'a is {} {} {}'.format(1,2,3)
'a is 1 2 3'
>>> 'a is {0} {1} {2}'.format(1,2,3)
'a is 1 2 3'
>>> 'My name is {0} {1}.Watashiwa {1} {0} desu'.format('aaa','bbb')
'My name is aaa bbb.Watashiwa bbb aaa desu'
>>> 'My name is {name} {family}. Watashiwa {family} {name} desu'.format(name='aaa',family='bbb') 
'My name is aaa bbb. Watashiwa bbb aaa desu'
