## 23. タプルの使い所
#### 📝 VSCodeで実行
<div align="right">
  <a href="../README.md#section4">READMEに戻る</a>
</div>

```python
# タプルの定義（イミュータブル：変更不可）
chose_from_two = ('A', 'B', 'C')

# 回答を格納するためのリスト（ミュータブル：変更可能）
answer = []
answer.append('A')   # リストに 'A' を追加
answer.append('C')   # リストに 'C' を追加

# タプルは変更不可なので append() は使えない
# chose_from_two = ['A', 'B', 'C']   # リストなら append() が可能
# chose_from_two.append('A')
# chose_from_two.append('C')

# 出力確認
print(chose_from_two)   # ('A', 'B', 'C') → タプルのまま
print(answer)           # ['A', 'c'] → リストに追加された結果
```

## 📝 学習のまとめ
- 要素を後から変更したくないときに使う
- データを固定して安全に保持したい場面に適している

<div align="right">
  <a href="../README.md#section4">READMEに戻る</a>
</div>


