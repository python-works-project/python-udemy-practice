## 19. リストのコピー
#### 📝 VSCodeで実行
<div align="right">
  <a href="../README.md#section4">READMEに戻る</a>
</div>

```python
# リストを代入すると「参照」が渡される
i = [1,2,3,4,5]
j = i              # jはiと同じリストを参照
j[0] = 100         # jを変更するとiも変更される
print('i = ', i)   # i = [100, 2, 3, 4, 5]
print('j = ', j)   # j = [100, 2, 3, 4, 5]

# copy()やスライスで「浅いコピー」を作ると別オブジェクトになる
x = [1,2,3,4,5]
y = x.copy()       # y = x[:] と同じ意味
y[0] = 100         # yを変更してもxには影響しない
print('x = ' , x)  # x = [1, 2, 3, 4, 5]
print('y = ' , y)  # y = [100, 2, 3, 4, 5]

# 整数はイミュータブル（変更不可）なので代入すると新しいオブジェクトになる
x = 20
y = x              # yはxと同じ値を参照
y = 5              # yに新しい値を代入 → xには影響なし
print(id(x))       # xのオブジェクトID
print(id(y))       # yのオブジェクトID（別物）
print('X = ', x)   # X = 20
print('y = ', y)   # y = 5

# リストはミュータブル（変更可能）なので参照を共有すると両方に影響する
x = ['a', 'b']
y = x              # yはxと同じリストを参照
y[0] = 'A'         # yを変更するとxも変更される
print(id(x))       # xとyのIDは同じ
print(id(y))       # 同じリストを参照している
print('X = ', x)   # X = ['A', 'b']
print('y = ', y)   # y = ['A', 'b']
```

## 📝 学習のまとめ
- Pythonは「オブジェクト参照渡し」
- intやstrはイミュータブル（変更不可） → 値を変更しても元に影響なし
- listやdictはミュータブル（変更不可） → 参照を共有すると変更が伝わる
- 独立コピーには copy() や deepcopy() を使う
```bash
j = i.copy()        # シャローコピー（浅いコピー）
j = list(i)         # 同じく浅いコピー
import copy
j = copy.deepcopy(i) # ネストしたリストまで完全コピー
```
- 
<div align="right">
  <a href="../README.md#section4">READMEに戻る</a>
</div>
