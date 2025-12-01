## 73. 組み込み関数
#### 🖥 VSCodeで実行
<div align="right">
  <a href="../README.md#section5">◀️READMEに戻る</a>
</div>

```python
# Pythonの組み込みモジュール builtins をインポート
import builtins

ranking = {
    'A': 100,
    'B': 85,
    'C': 95
}

# 辞書のキーを順に取り出して表示
for key in ranking:
    print(key)   # → A, B, C が順に出力される

# 辞書を値でソート（昇順）。キーのリストが返る
print(sorted(ranking, key=ranking.get))  
# → ['B', 'C', 'A'] （85,95,100 の順）

# 辞書を値でソート（降順）。キーのリストが返る
print(sorted(ranking, key=ranking.get, reverse=True))  
# → ['A', 'C', 'B'] （100,95,85 の順）
```
