---
source: "codefronts"
url: "https://codefronts.com/snippets/css-dark-mode-toggle/the-modern-css-light-dark-function-boilerplate/"
title: "The Modern CSS light-dark() Function Boilerplate"
section: "snippets"
category: "css-dark-mode-toggle"
category_name: "CSS Dark Mode Toggles"
description: "A mock code editor showcasing the native CSS light-dark() function — single declarations that adapt both values simultaneously, eliminating duplicate @media…"
has_js: "true"
---

Here's a working CSS Dark Mode Toggle from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: The Modern CSS light-dark() Function Boilerplate
Source: https://codefronts.com/snippets/css-dark-mode-toggle/the-modern-css-light-dark-function-boilerplate/

A mock code editor showcasing the native CSS light-dark() function — single declarations that adapt both values simultaneously, eliminating duplicate @media blocks entirely.
## HTML
```html
<div class="dm-03" id="dm-03-root">
  <div class="dm-03__editor">
    <div class="dm-03__bar">
      <div class="dm-03__dots">
        <div class="dm-03__dot"></div>
        <div class="dm-03__dot"></div>
        <div class="dm-03__dot"></div>
      </div>
      <span class="dm-03__bar-title">theme.css — light-dark() boilerplate</span>
      <button class="dm-03__switcher" id="dm-03-btn" aria-label="Toggle color scheme">
        <span class="dm-03__switcher-icon" id="dm-03-icon">☀️</span>
        <span id="dm-03-label">Light</span>
      </button>
    </div>
    <div class="dm-03__code">
      <div class="dm-03__line"><span class="dm-03__ln">1</span><span class="dm-03__token--comment">/* Native CSS light-dark() — no @media needed */</span></div>
      <div class="dm-03__line"><span class="dm-03__ln">2</span></div>
      <div class="dm-03__line"><span class="dm-03__ln">3</span><span class="dm-03__token--selector">:root</span><span class="dm-03__token--punc"> { </span><span class="dm-03__token--prop">color-scheme</span><span class="dm-03__token--punc">: </span><span class="dm-03__token--val-light">light dark</span><span class="dm-03__token--punc">; }</span></div>
      <div class="dm-03__line"><span class="dm-03__ln">4</span></div>
      <div class="dm-03__line"><span class="dm-03__ln">5</span><span class="dm-03__token--selector">.card</span><span class="dm-03__token--punc"> {</span></div>
      <div class="dm-03__line"><span class="dm-03__ln">6</span>&nbsp;&nbsp;<span class="dm-03__token--prop">background</span><span class="dm-03__token--punc">: </span><span class="dm-03__token--fn">light-dark</span><span class="dm-03__token--punc">(</span><span class="dm-03__token--val-light">#ffffff</span><span class="dm-03__token--punc">, </span><span class="dm-03__token--val-dark">#111827</span><span class="dm-03__token--punc">);</span></div>
      <div class="dm-03__line"><span class="dm-03__ln">7</span>&nbsp;&nbsp;<span class="dm-03__token--prop">color</span><span class="dm-03__token--punc">: </span><span class="dm-03__token--fn">light-dark</span><span class="dm-03__token--punc">(</span><span class="dm-03__token--val-light">#0f172a</span><span class="dm-03__token--punc">, </span><span class="dm-03__token--val-dark">#f1f5f9</span><span class="dm-03__token--punc">);</span></div>
      <div class="dm-03__line"><span class="dm-03__ln">8</span>&nbsp;&nbsp;<span class="dm-03__token--prop">border</span><span class="dm-03__token--punc">: </span><span class="dm-03__token--fn">light-dark</span><span class="dm-03__token--punc">(</span><span class="dm-03__token--val-light">#e2e8f0</span><span class="dm-03__token--punc">, </span><span class="dm-03__token--val-dark">#1e2a3a</span><span class="dm-03__token--punc">);</span></div>
      <div class="dm-03__line"><span class="dm-03__ln">9</span><span class="dm-03__token--punc">}</span></div>
      <div class="dm-03__preview">
        <span class="dm-03__preview-head">⬡ Live Preview</span>
        <div class="dm-03__preview-title">light-dark() function</div>
        <p class="dm-03__preview-body">Single declaration. No @media duplication. No custom property redeclaring. Just two comma-separated values and the browser picks the right one.</p>
        <span class="dm-03__preview-tag">Chrome 123 · Safari 17.5 · FF 120</span>
      </div>
    </div>
    <div class="dm-03__statusbar">
      <span class="dm-03__status-item">CSS &bull; UTF-8</span>
      <span class="dm-03__status-badge" id="dm-03-scheme">LIGHT MODE</span>
      <span class="dm-03__status-item">light-dark()</span>
    </div>
  </div>
</div>
```
## CSS
```css
.dm-03,
.dm-03 *,
.dm-03 *::before,
.dm-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.dm-03 ::selection {
  background: #22d3ee;
  color: #000;
}

.dm-03 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  color-scheme: light;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
}

.dm-03.is-dark {
  color-scheme: dark;
}
/* ── All colors via light-dark() ── */

.dm-03__editor {
  width: min(560px,100%);
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 4px 48px light-dark(rgba(0,0,0,0.1),rgba(0,0,0,0.7));
  border: 1px solid light-dark(#e2e8f0,#1e2a3a);
}
/* Editor chrome bar */

.dm-03__bar {
  background: light-dark(#f1f5f9,#0f1829);
  padding: 14px 18px;
  display: flex;
  align-items: center;
  gap: 12px;
  border-bottom: 1px solid light-dark(#e2e8f0,#1e2a3a);
}

.dm-03__dots {
  display: flex;
  gap: 6px;
}

.dm-03__dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
}

.dm-03__dot:nth-child(1) {
  background: #ff5f57;
}

.dm-03__dot:nth-child(2) {
  background: #febc2e;
}

.dm-03__dot:nth-child(3) {
  background: #28c840;
}

.dm-03__bar-title {
  flex: 1;
  text-align: center;
  font-size: 0.75rem;
  font-weight: 600;
  color: light-dark(#94a3b8,#4a5568);
  font-family: monospace;
}
/* Theme switcher button in bar */

.dm-03__switcher {
  display: flex;
  align-items: center;
  gap: 6px;
  background: light-dark(#e2e8f0,#1e2a3a);
  border: 1px solid light-dark(#cbd5e1,#2d3f54);
  border-radius: 8px;
  padding: 5px 10px;
  cursor: pointer;
  font-size: 0.72rem;
  font-weight: 700;
  color: light-dark(#475569,#64748b);
  letter-spacing: 0.05em;
  transition: background 0.3s ease,color 0.3s ease;
}

.dm-03__switcher:hover {
  background: light-dark(#cbd5e1,#2d3f54);
}

.dm-03__switcher-icon {
  font-size: 14px;
}
/* Editor body */

.dm-03__code {
  background: light-dark(#ffffff,#0a1120);
  padding: 28px 24px;
}

.dm-03__line {
  display: flex;
  gap: 16px;
  margin-bottom: 6px;
  font-family: 'Courier New',monospace;
  font-size: 0.82rem;
  line-height: 1.7;
}

.dm-03__ln {
  color: light-dark(#cbd5e1,#2d3f54);
  user-select: none;
  min-width: 20px;
  text-align: right;
  font-size: 0.75rem;
  padding-top: 1px;
}

.dm-03__token--comment {
  color: light-dark(#94a3b8,#485e7a);
  font-style: italic;
}

.dm-03__token--prop {
  color: light-dark(#7c3aed,#c084fc);
}

.dm-03__token--fn {
  color: light-dark(#0891b2,#22d3ee);
}

.dm-03__token--val-light {
  color: light-dark(#166534,#86efac);
}

.dm-03__token--val-dark {
  color: light-dark(#991b1b,#fca5a5);
}

.dm-03__token--punc {
  color: light-dark(#64748b,#475569);
}

.dm-03__token--selector {
  color: light-dark(#b45309,#fbbf24);
}
/* Preview card in editor */

.dm-03__preview {
  background: light-dark(#f8fafc,#111827);
  border: 1px solid light-dark(#e2e8f0,#1e2a3a);
  border-radius: 12px;
  padding: 20px;
  margin: 12px 0;
}

.dm-03__preview-head {
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: light-dark(#0891b2,#22d3ee);
  margin-bottom: 8px;
  display: block;
}

.dm-03__preview-title {
  font-size: 1.1rem;
  font-weight: 800;
  letter-spacing: -0.02em;
  color: light-dark(#0f172a,#f1f5f9);
  margin-bottom: 6px;
}

.dm-03__preview-body {
  font-size: 0.8rem;
  line-height: 1.6;
  color: light-dark(#475569,#64748b);
}

.dm-03__preview-tag {
  display: inline-block;
  margin-top: 10px;
  padding: 3px 10px;
  border-radius: 99px;
  font-size: 0.65rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  background: light-dark(rgba(8,145,178,0.12),rgba(34,211,238,0.12));
  color: light-dark(#0891b2,#22d3ee);
  border: 1px solid light-dark(rgba(8,145,178,0.2),rgba(34,211,238,0.2));
}
/* Status bar */

.dm-03__statusbar {
  background: light-dark(#0891b2,#0c4a6e);
  padding: 6px 18px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.dm-03__status-item {
  font-size: 0.68rem;
  font-weight: 600;
  color: light-dark(#fff,#bae6fd);
  letter-spacing: 0.06em;
}

.dm-03__status-badge {
  background: rgba(255,255,255,0.2);
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 0.62rem;
  font-weight: 700;
  color: #fff;
}

@media (prefers-reduced-motion: reduce) {
  .dm-03,
    .dm-03 * {
    transition: none!important;
  }
}
```

## JavaScript
```js
const root=document.getElementById('dm-03-root');
const btn=document.getElementById('dm-03-btn');
const icon=document.getElementById('dm-03-icon');
const label=document.getElementById('dm-03-label');
const badge=document.getElementById('dm-03-scheme');
btn.addEventListener('click',()=>{
  const dark=root.classList.toggle('is-dark');
  root.style.colorScheme=dark?'dark':'light';
  icon.textContent=dark?'🌙':'☀️';
  label.textContent=dark?'Dark':'Light';
  badge.textContent=dark?'DARK MODE':'LIGHT MODE';
});
```
