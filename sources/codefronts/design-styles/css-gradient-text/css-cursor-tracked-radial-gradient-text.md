---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-gradient-text/css-cursor-tracked-radial-gradient-text/"
title: "CSS Cursor-Tracked Radial Gradient Text"
section: "design-styles"
category: "css-gradient-text"
category_name: "CSS Gradient Text Designs"
description: "A radial gradient spotlight follows the cursor position inside the demo, illuminating text from the exact point the mouse hovers, driven by CSS custom…"
has_js: "true"
---

Here's a working CSS Gradient Text Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Cursor-Tracked Radial Gradient Text
Source: https://codefronts.com/design-styles/css-gradient-text/css-cursor-tracked-radial-gradient-text/

A radial gradient spotlight follows the cursor position inside the demo, illuminating text from the exact point the mouse hovers, driven by CSS custom properties updated in JavaScript.
## HTML
```html
<div class="gt-17" id="gt-17-root">
  <div class="gt-17__cursor" id="gt-17-cursor"></div>
  <span class="gt-17__label">Cursor-tracked gradient</span>
  <h1 class="gt-17__main" id="gt-17-main">FOLLOW</h1>
  <p class="gt-17__sub" id="gt-17-sub">Move your cursor</p>
  <div class="gt-17__grid">
    <span class="gt-17__cell">TRACK</span>
    <span class="gt-17__cell">LIGHT</span>
    <span class="gt-17__cell">FOCUS</span>
  </div>
</div>
```
## CSS
```css
.gt-17,
.gt-17 *,
.gt-17 *::before,
.gt-17 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.gt-17 {
  --bg: #08080e;
  --cx: 50%;
  --cy: 50%;
  font-family: 'Space Grotesk', sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 2.5rem;
  padding: 3rem 2rem;
  cursor: none;
}

.gt-17__cursor {
  position: fixed;
  top: 0;
  left: 0;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: white;
  mix-blend-mode: exclusion;
  pointer-events: none;
  transform: translate(-50%, -50%);
  transition: transform .1s;
  z-index: 9999;
}

.gt-17__label {
  font-size: .7rem;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: #333;
}

.gt-17__main {
  font-size: clamp(3rem, 12vw, 8rem);
  font-weight: 800;
  line-height: 1;
  letter-spacing: -.01em;
  background: radial-gradient(
      circle at var(--cx) var(--cy),
      #a855f7 0%,
      #ec4899 25%,
      #f43f5e 50%,
      #fb923c 75%,
      #fbbf24 100%
    );
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  transition: --cx .05s, --cy .05s;
}

.gt-17__sub {
  font-size: clamp(.9rem, 2.5vw, 1.3rem);
  font-weight: 700;
  background: radial-gradient(
      circle at var(--cx) var(--cy),
      #00f5a0 0%,
      #00d9f5 50%,
      #4d96ff 100%
    );
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  letter-spacing: .1em;
}

.gt-17__grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
}

.gt-17__cell {
  font-size: clamp(1rem, 3vw, 1.6rem);
  font-weight: 800;
  padding: .6em 1em;
  text-align: center;
  border: 1px solid #ffffff0d;
  border-radius: 8px;
  background: radial-gradient(
      circle at var(--cx) var(--cy),
      #a855f720 0%,
      transparent 70%
    );
  color: #333;
  background-clip: padding-box;
  -webkit-text-fill-color: transparent;
  background-image: radial-gradient(
      circle at var(--cx) var(--cy),
      #a855f7 0%,
      #ec4899 40%,
      #4d96ff 80%,
      #00f5a0 100%
    );
  -webkit-background-clip: text;
}

@media (prefers-reduced-motion: reduce) {
  .gt-17__cursor {
    display: none;
  }
}
```

## JavaScript
```js
(function() {
  const root = document.getElementById('gt-17-root');
  const cursor = document.getElementById('gt-17-cursor');
  if (!root) return;
  root.addEventListener('mousemove', (e) => {
    const rect = root.getBoundingClientRect();
    const x = ((e.clientX - rect.left) / rect.width * 100).toFixed(1) + '%';
    const y = ((e.clientY - rect.top) / rect.height * 100).toFixed(1) + '%';
    root.style.setProperty('--cx', x);
    root.style.setProperty('--cy', y);
    cursor.style.left = e.clientX + 'px';
    cursor.style.top = e.clientY + 'px';
  });
})();
```
