---
source: "codefronts"
url: "https://codefronts.com/motion/css-spinner-designs/matrix-rain-column-spinner/"
title: "Matrix Rain Column Spinner"
section: "motion"
category: "css-spinner-designs"
category_name: "CSS Spinners"
description: "Five columns of katakana characters and binary digits cascade downward with a bright white leading character fading to dark green, evoking the iconic Matrix…"
has_js: "false"
---

Here's a working CSS Spinner from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Matrix Rain Column Spinner
Source: https://codefronts.com/motion/css-spinner-designs/matrix-rain-column-spinner/

Five columns of katakana characters and binary digits cascade downward with a bright white leading character fading to dark green, evoking the iconic Matrix digital rain effect.
## HTML
```html
<div class="sp-24">
  <div class="sp-24__cols">
    <div class="sp-24__col">
      <div class="sp-24__char" style="--i:0">ア</div>
      <div class="sp-24__char" style="--i:1">ク</div>
      <div class="sp-24__char" style="--i:2">セ</div>
      <div class="sp-24__char" style="--i:3">ス</div>
      <div class="sp-24__char" style="--i:4">1</div>
      <div class="sp-24__char" style="--i:5">0</div>
      <div class="sp-24__char" style="--i:6">0</div>
      <div class="sp-24__char" style="--i:7">1</div>
    </div>
    <div class="sp-24__col">
      <div class="sp-24__char" style="--i:0">テ</div>
      <div class="sp-24__char" style="--i:1">ス</div>
      <div class="sp-24__char" style="--i:2">ト</div>
      <div class="sp-24__char" style="--i:3">0</div>
      <div class="sp-24__char" style="--i:4">1</div>
      <div class="sp-24__char" style="--i:5">ネ</div>
      <div class="sp-24__char" style="--i:6">ッ</div>
      <div class="sp-24__char" style="--i:7">ト</div>
    </div>
    <div class="sp-24__col">
      <div class="sp-24__char" style="--i:0">1</div>
      <div class="sp-24__char" style="--i:1">0</div>
      <div class="sp-24__char" style="--i:2">ラ</div>
      <div class="sp-24__char" style="--i:3">イ</div>
      <div class="sp-24__char" style="--i:4">ン</div>
      <div class="sp-24__char" style="--i:5">コ</div>
      <div class="sp-24__char" style="--i:6">ー</div>
      <div class="sp-24__char" style="--i:7">ド</div>
    </div>
    <div class="sp-24__col">
      <div class="sp-24__char" style="--i:0">0</div>
      <div class="sp-24__char" style="--i:1">1</div>
      <div class="sp-24__char" style="--i:2">マ</div>
      <div class="sp-24__char" style="--i:3">ト</div>
      <div class="sp-24__char" style="--i:4">リ</div>
      <div class="sp-24__char" style="--i:5">ク</div>
      <div class="sp-24__char" style="--i:6">ス</div>
      <div class="sp-24__char" style="--i:7">1</div>
    </div>
    <div class="sp-24__col">
      <div class="sp-24__char" style="--i:0">ヲ</div>
      <div class="sp-24__char" style="--i:1">1</div>
      <div class="sp-24__char" style="--i:2">0</div>
      <div class="sp-24__char" style="--i:3">ル</div>
      <div class="sp-24__char" style="--i:4">ー</div>
      <div class="sp-24__char" style="--i:5">プ</div>
      <div class="sp-24__char" style="--i:6">0</div>
      <div class="sp-24__char" style="--i:7">1</div>
    </div>
  </div>
</div>
```
## CSS
```css
.sp-24,
.sp-24 *,
.sp-24 *::before,
.sp-24 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sp-24 {
  --bg: #000;
  --c: #00ff41;
  --dim: #003b10;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: var(--bg);
  font-family: 'Courier New',monospace;
}

.sp-24__cols {
  display: flex;
  gap: 6px;
  align-items: flex-start;
}

.sp-24__col {
  display: flex;
  flex-direction: column;
  gap: 0;
}

.sp-24__char {
  width: 16px;
  height: 18px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
  font-weight: bold;
  color: var(--dim);
  animation: sp-24-fall 1.5s linear infinite;
}

.sp-24__col:nth-child(1) .sp-24__char {
  animation-delay: calc(var(--i,0) * -0.1s);
}

.sp-24__col:nth-child(2) .sp-24__char {
  animation-delay: calc(var(--i,0) * -0.1s - 0.3s);
}

.sp-24__col:nth-child(3) .sp-24__char {
  animation-delay: calc(var(--i,0) * -0.1s - 0.6s);
}

.sp-24__col:nth-child(4) .sp-24__char {
  animation-delay: calc(var(--i,0) * -0.1s - 0.9s);
}

.sp-24__col:nth-child(5) .sp-24__char {
  animation-delay: calc(var(--i,0) * -0.1s - 1.2s);
}
/* Head char bright white-green */

.sp-24__col:nth-child(1) .sp-24__char:nth-child(1),
.sp-24__col:nth-child(2) .sp-24__char:nth-child(1),
.sp-24__col:nth-child(3) .sp-24__char:nth-child(1),
.sp-24__col:nth-child(4) .sp-24__char:nth-child(1),
.sp-24__col:nth-child(5) .sp-24__char:nth-child(1) {
  color: #fff;
  text-shadow: 0 0 8px var(--c),0 0 16px var(--c);
}

@keyframes sp-24-fall {
  0% {
    color: #fff;
    text-shadow: 0 0 8px var(--c);
  }

  10% {
    color: var(--c);
    text-shadow: 0 0 4px var(--c);
  }

  60% {
    color: rgba(0,255,65,0.4);
    text-shadow: none;
  }

  100% {
    color: var(--dim);
    text-shadow: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sp-24__char {
    animation: none;
    color: var(--c);
  }
}
```
