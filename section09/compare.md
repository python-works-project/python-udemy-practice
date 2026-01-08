<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title>左右コード比較サンプル</title>
<style>
  .container {
    display: flex;
    gap: 20px;
  }
  .code-box {
    flex: 1;
    background: #f0f0f0;
    padding: 10px;
    border-radius: 6px;
  }
  pre {
    background: #272822;
    color: #f8f8f2;
    padding: 10px;
    border-radius: 4px;
    overflow-x: auto;
    margin: 0;
  }
  code {
    white-space: pre;
    font-family: Consolas, monospace;
  }
</style>
</head>
<body>

<div class="container">

  <div class="code-box">
    <h3>左側のコード</h3>
    <pre><code>def hello():
    print("Hello from left")

for i in range(3):
    hello()</code></pre>
  </div>

  <div class="code-box">
    <h3>右側のコード</h3>
    <pre><code>def greet():
    print("Hello from right")

for i in range(3):
    greet()</code></pre>
  </div>

</div>

</body>
</html>
