
# リストの準備
r = [1,2,3,4,5,1,2,3]

# index(): 最初に見つかった要素の位置
print(r.index(3))      # 出力: 2

# index(start): 指定位置から検索
print(r.index(3, 3))   # 出力: 7

# count(): 要素の出現回数
print(r.count(3))      # 出力: 2

# in演算子: 要素の存在確認
if 5 in r:
    print('exist')

# sort(): 昇順に並べ替え
r.sort()
print(r)               # 出力: [1, 1, 2, 2, 3, 3, 4, 5]
