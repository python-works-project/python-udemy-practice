## 18. リストのメソッド
#### 📝 VSCodeで実行
<div align="right">
  <a href="../README.md#section4">READMEに戻る</a>
</div>

```bash
# リストを作成
r = [1,2,3,4,5,1,2,3]

# index(): 指定した値が最初に出現する位置を返す
print(r.index(3))       # → 最初の3の位置（インデックス2）
print(r.index(3, 3))    # → インデックス3以降で最初に出現する3の位置（インデックス7）

# count(): 指定した値がリストにいくつあるか数える
print(r.count(3))       # → 3は2回出現

# in演算子: 要素が存在するか確認
if 5 in r:
    print('exist')      # → 5が存在するので表示される

# sort(): 昇順に並べ替え
r.sort()
print(r)                # → [1,1,2,2,3,3,4,5]

# sort(reverse=True): 降順に並べ替え
r.sort(reverse=True)
print(r)                # → [5,4,3,3,2,2,1,1]

# reverse(): リストを逆順にする
r.reverse()
print(r)                # → [1,1,2,2,3,3,4,5]

# 文字列の分割 split()
s = 'My name is Mike'
to_split = s.split(' ')
print(to_split)         # → ['My', 'name', 'is', 'Mike']

# join(): リストを文字列に結合
x = ' '.join(to_split)
print(x)                # → "My name is Mike"

# listクラスのヘルプを表示
print(help(list))

```
<div align="right">
  <a href="../README.md#section4">READMEに戻る</a>
</div>
