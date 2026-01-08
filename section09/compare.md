<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8" />
  <title>コード比較（左右並列）</title>
  <style>
    body {
      margin: 0;
      padding: 20px;
      background: #f5f5f5;
      font-family: "Segoe UI", sans-serif;
    }

    .grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
    }

    .box {
      background: #fff;
      border: 1px solid #ddd;
      border-radius: 6px;
      padding: 12px;
      box-sizing: border-box;
    }

    h2 {
      margin-top: 0;
      font-size: 16px;
      border-bottom: 1px solid #eee;
      padding-bottom: 6px;
    }

    pre {
      background: #272822;
      color: #f8f8f2;
      padding: 12px;
      border-radius: 4px;
      overflow-x: auto;
      font-size: 13px;
      line-height: 1.5;
      margin: 0;
    }

    code {
      font-family: Consolas, "Courier New", monospace;
      white-space: pre;
    }

    /* スマホでは縦並び */
    @media (max-width: 900px) {
      .grid {
        grid-template-columns: 1fr;
      }
    }
  </style>
</head>
<body>

  <div class="grid">
    <!-- 左 -->
    <div class="box">
      <h2>自分で作成したコード</h2>
      <pre><code>（ここに左側のコードを貼る）</code></pre>
    </div>

    <!-- 右 -->
    <div class="box">
      <h2>生成したコード</h2>
      <pre><code>（ここに右側のコードを貼る）</code></pre>
    </div>
  </div>

</body>
</html>
