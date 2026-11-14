---
source: "codefronts"
url: "https://codefronts.com/motion/css-typewriter-effect/css-typewriter-code-editor-syntax/"
title: "CSS Typewriter Code Editor Syntax"
section: "motion"
category: "css-typewriter-effect"
category_name: "CSS Typewriter Effect Designs"
description: "A realistic VS Code-style editor types out syntax-highlighted code line by line, with a live line-number gutter, blinking cursor, and language-aware coloring…"
has_js: "false"
---

Here's a working CSS Typewriter Effect Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Typewriter Code Editor Syntax
Source: https://codefronts.com/motion/css-typewriter-effect/css-typewriter-code-editor-syntax/

A realistic VS Code-style editor types out syntax-highlighted code line by line, with a live line-number gutter, blinking cursor, and language-aware coloring — all orchestrated by JS.
## HTML
```html
<div class="tw-13">
  <div class="tw-13__editor">
    <div class="tw-13__topbar">
      <span class="tw-13__dot tw-13__dot--r"></span>
      <span class="tw-13__dot tw-13__dot--y"></span>
      <span class="tw-13__dot tw-13__dot--g"></span>
      <span class="tw-13__filename">app.ts &nbsp;×</span>
    </div>
    <div class="tw-13__body">
      <div class="tw-13__gutter" id="tw-13-gutter"></div>
      <div class="tw-13__code" id="tw-13-code" aria-label="Typescript code demo" aria-live="polite"></div>
    </div>
  </div>
</div>
```
## CSS
```css
.tw-13,
.tw-13 *,
.tw-13 *::before,
.tw-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tw-13 ::selection {
  background: #264f78;
  color: #d4d4d4;
}

.tw-13 {
  --bg: #1e1e1e;
  --surface: #252526;
  --border: #3e3e42;
  --text: #d4d4d4;
  font-family: 'Courier New', 'Fira Code', monospace;
  background: #111;
  min-height: 340px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px 16px;
}

.tw-13__editor {
  width: 100%;
  max-width: 540px;
  border-radius: 10px;
  border: 1px solid var(--border);
  box-shadow: 0 24px 60px rgba(0,0,0,0.6);
  overflow: hidden;
}

.tw-13__topbar {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 14px;
  background: var(--surface);
  border-bottom: 1px solid var(--border);
}

.tw-13__dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
}

.tw-13__dot--r {
  background: #ff5f57;
}

.tw-13__dot--y {
  background: #febc2e;
}

.tw-13__dot--g {
  background: #28c840;
}

.tw-13__filename {
  margin-left: 8px;
  font-size: 0.78rem;
  color: #9d9d9d;
  font-family: inherit;
}

.tw-13__body {
  display: flex;
  padding: 16px 0;
}

.tw-13__gutter {
  padding: 0 16px;
  border-right: 1px solid var(--border);
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 2px;
  min-width: 44px;
  color: #495c73;
  font-size: 0.82rem;
  line-height: 1.7;
  user-select: none;
}

.tw-13__code {
  padding: 0 16px;
  flex: 1;
  font-size: 0.82rem;
  line-height: 1.7;
  color: var(--text);
  display: flex;
  flex-direction: column;
  gap: 0;
  min-height: 200px;
  position: relative;
  overflow: hidden;
}

.tw-13__code .ln {
  display: block;
  min-height: 1.7em;
  white-space: pre;
}

.tw-13__code .kw {
  color: #569cd6;
}

.tw-13__code .fn {
  color: #dcdcaa;
}

.tw-13__code .str {
  color: #ce9178;
}

.tw-13__code .num {
  color: #b5cea8;
}

.tw-13__code .cm {
  color: #6a9955;
}

.tw-13__code .tp {
  color: #4ec9b0;
}

.tw-13__code .op {
  color: #d4d4d4;
}

.tw-13__cursor {
  display: inline-block;
  width: 2px;
  height: 1em;
  background: #aeafad;
  vertical-align: middle;
  animation: tw-13-blink 0.9s steps(2) infinite;
}

@keyframes tw-13-blink {
  0%,
    100% {
    opacity: 1;
  }

  50% {
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tw-13__cursor {
    animation: none;
    opacity: 1;
  }
}
```

## JavaScript
```js
(function() {
  const codeEl = document.getElementById('tw-13-code');
  const gutterEl = document.getElementById('tw-13-gutter');
  if (!codeEl) return;

  // Pre-tokenised lines (HTML strings)
  const LINES = [
    '<span class="cm">// Typewriter code editor demo</span>',
    '<span class="kw">interface</span> <span class="tp">User</span> {',
    '  id<span class="op">:</span> <span class="tp">number</span>;',
    '  name<span class="op">:</span> <span class="tp">string</span>;',
    '  role<span class="op">:</span> <span class="str">"admin"</span> <span class="op">|</span> <span class="str">"user"</span>;',
    '}',
    '',
    '<span class="kw">async function</span> <span class="fn">fetchUser</span>(id<span class="op">:</span> <span class="tp">number</span>) {',
    '  <span class="kw">const</span> res <span class="op">=</span> <span class="kw">await</span> <span class="fn">fetch</span>(<span class="str">`/api/users/${id}`</span>);',
    '  <span class="kw">return</span> res.<span class="fn">json</span>()<span class="op"> as</span> <span class="tp">User</span>;',
    '}',
  ];

  let lineIdx = 0, timer = null;

  function addGutterLine(n) {
    const span = document.createElement('span');
    span.textContent = n;
    gutterEl.appendChild(span);
  }

  function typeLine(html, lineEl, callback) {
    // Extract plain text length for speed calculation
    const tmp = document.createElement('div');
    tmp.innerHTML = html;
    const plain = tmp.textContent;
    let i = 0;

    // We reveal character-by-character by tracking text position through HTML
    function tick() {
      i++;
      // Slice HTML to show first i plain-text characters
      let visible = 0;
      let result = '';
      let inTag = false;
      for (let ci = 0; ci < html.length; ci++) {
        const ch = html[ci];
        if (ch === '<') { inTag = true; result += ch; continue; }
        if (ch === '>') { inTag = false; result += ch; continue; }
        if (inTag) { result += ch; continue; }
        if (visible < i) { result += ch; visible++; }
        else break;
      }
      // Close any open tags
      lineEl.innerHTML = result + '<span class="tw-13__cursor"></span>';
      if (i <= plain.length) {
        timer = setTimeout(tick, plain[i-1] === ' ' ? 30 : 55 + Math.random() * 20);
      } else {
        lineEl.innerHTML = html;
        callback();
      }
    }
    tick();
  }

  function typeNextLine() {
    if (lineIdx >= LINES.length) return;
    addGutterLine(lineIdx + 1);
    const lineEl = document.createElement('span');
    lineEl.className = 'ln';
    codeEl.appendChild(lineEl);
    const html = LINES[lineIdx];
    lineIdx++;
    typeLine(html, lineEl, () => {
      timer = setTimeout(typeNextLine, 120);
    });
  }

  typeNextLine();
})();
```
