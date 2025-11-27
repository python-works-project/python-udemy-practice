## 💡Python補足メモ

このページでは、Python学習の中で出てきた補足事項やVSCodeの操作方法など、<br>
理解を深めるためのポイントを簡潔にまとめています。


<div align="right">
  <a href="../README.md#４-その他">◀️READMEに戻る</a>
</div>

---

## 目次

- [リスト/タプル/辞書/集合](#リストタプル辞書集合)
- [type() と help() の使い分け](#type-と-help-の使い分け)
- [is not と != の使い分け](#is-not-と--の使い分け)
- [VSCodeの全画面表示解除](#vscodeの全画面表示解除)
- [d['x'] と d.get('x') の使い分け](#dx-と-dgetx-の使い分け)
- [各 内包表記](#各-内包表記)



---

### リスト/タプル/辞書/集合
**リスト (list)**
```
- `[]` で表記
- 順序あり / 重複可 / 変更可能 (mutable)
- 例: `lst = [1, 2, 3]`
```

**タプル (tuple)**
```
- `()` で表記
- 順序あり / 重複可 / 変更不可 (immutable)
- 例: `tpl = (1, 2, 3)`
```
<div align="right"><a href="#python補足メモ">🔼 TOPに戻る</a></div>

**辞書 (dict)**
```
- `{キー: 値}` で表記
- キーと値のペアを保持 / キーは重複不可
- 例: `d = {'a': 1, 'b': 2}`
```
<div align="right"><a href="#python補足メモ">🔼 TOPに戻る</a></div>

**集合 (set)**
```
- `{}` または `set()` で表記
- 順序なし / 重複不可
- 例: `s = {1, 2, 3}`
```
<div align="right"><a href="#python補足メモ">🔼 TOPに戻る</a></div>

### type() と help() の使い分け
```
- `type(obj)` → 型を返す（例: `<class 'NoneType'>`）：型を調べたいとき  
- `help(obj)` → 型やオブジェクトのドキュメントを表示：詳しい説明やメソッド一覧を知りたいとき  
```
<div align="right"><a href="#python補足メモ">🔼 TOPに戻る</a></div>

### is not と != の使い分け
```
- `!=` → 値が等しくないかどうかを判定  
  例: `1 != 2` → True（値が異なる）  
- `is not` → 同じオブジェクトではないかどうかを判定  
  例: `[] is not []` → True（別々に作られたリストなので同一オブジェクトではない）  
```
<div align="right"><a href="#python補足メモ">🔼 TOPに戻る</a></div>

### VSCodeの全画面表示解除
```
- フルスクリーン解除：**F11** キーを押下する
```
<div align="right"><a href="#python補足メモ">🔼 TOPに戻る</a></div>

### d['x'] と d.get('x') の使い分け
```
- `d['x']` → キーが無いと **KeyError**。キーが必ず存在する前提で使う  
- `d.get('x')` → キーが無くてもエラーにならない。デフォルト値も指定できる（例：`d.get('x', 0)`）
```
<div align="right"><a href="#python補足メモ">🔼 TOPに戻る</a></div>

### 各 内包表記
```
- リスト内包表記：`[式 for 変数 in イテラブル if 条件]`
- 集合内包表記：`{式 for 変数 in イテラブル if 条件}`
- 辞書内包表記：`{キー: 値 for 変数 in イテラブル if 条件}`
```
<div align="right"><a href="#python補足メモ">🔼 TOPに戻る</a></div>



---

<div align="right">
  <a href="../README.md#４-その他">READMEに戻る</a>
</div>
