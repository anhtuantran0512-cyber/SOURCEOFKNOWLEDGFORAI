---
source: "codefronts"
url: "https://codefronts.com/motion/css-shimmer-skeleton-cards/dark-mode-skeleton/"
title: "Dark Mode Skeleton"
section: "motion"
category: "css-shimmer-skeleton-cards"
category_name: "CSS Shimmer Skeleton Cards"
description: "The Simple Utility Card's dark twin — theme-switchable live: the same 16:9 media slot, title and text blocks, but every colour flows from two custom…"
has_js: "true"
---

Here's a working CSS Shimmer Skeleton Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark Mode Skeleton
Source: https://codefronts.com/motion/css-shimmer-skeleton-cards/dark-mode-skeleton/

The Simple Utility Card's dark twin — theme-switchable live: the same 16:9 media slot, title and text blocks, but every colour flows from two custom properties (--sk-bg / --sk-shine) resolved through a data-theme attribute, with a real toggle button to flip light ↔ dark. On dark surfaces the shimmer must get SUBTLER, not brighter — this demo encodes that rule.
## HTML
```html
<section class="ssc-15" data-theme="dark" aria-label="Dark mode skeleton demo">
  <button class="ssc-15__toggle" id="ssc-15-toggle" type="button" aria-pressed="true">🌙 Dark</button>
  <div class="ssc-15__card" role="status" aria-busy="true">
    <span class="ssc-sr">Loading content…</span>
    <div aria-hidden="true">
      <div class="ssc-sk ssc-15__media"></div>
      <div class="ssc-15__body">
        <div class="ssc-sk ssc-15__title" style="width:72%"></div>
        <div class="ssc-15__block">
          <div class="ssc-sk ssc-15__line" style="width:100%"></div>
          <div class="ssc-sk ssc-15__line" style="width:88%"></div>
        </div>
        <div class="ssc-15__block">
          <div class="ssc-sk ssc-15__line" style="width:96%"></div>
          <div class="ssc-sk ssc-15__line" style="width:54%"></div>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.ssc-15,
.ssc-15 *,
.ssc-15 *::before,
.ssc-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ssc-15 {
  --sk-bg: oklch(0.28 0.015 280);
  --sk-shine: rgba(255,255,255,.07);
  --stage: oklch(0.17 0.015 280);
  --surface: oklch(0.22 0.015 280);
  --edge: rgba(255,255,255,.09);
  --toggle-fg: #e8e8f2;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  gap: 18px;
  padding: 40px 24px 48px;
  background: var(--stage);
  transition: background .45s ease;
}

.ssc-15[data-theme="light"] {
  --sk-bg: oklch(0.92 0.008 280);
  --sk-shine: rgba(255,255,255,.85);
  --stage: oklch(0.96 0.006 280);
  --surface: #fff;
  --edge: oklch(0.9 0.01 280);
  --toggle-fg: #2a2a35;
}

.ssc-15 .ssc-sk {
  position: relative;
  overflow: hidden;
  background: var(--sk-bg);
  border-radius: 8px;
  transition: background .45s ease;
}

.ssc-15 .ssc-sk::after {
  content: "";
  position: absolute;
  inset: 0;
  transform: translateX(-100%);
  background: linear-gradient(105deg,transparent 30%,var(--sk-shine) 50%,transparent 70%);
  animation: ssc-15-shimmer 1.8s ease-in-out infinite;
}

@keyframes ssc-15-shimmer {
  100% {
    transform: translateX(100%);
  }
}

.ssc-15 .ssc-sr {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
  white-space: nowrap;
  border: 0;
}

.ssc-15 .ssc-15__toggle {
  font: 600 13px/1 'Segoe UI',system-ui,sans-serif;
  color: var(--toggle-fg);
  background: var(--surface);
  border: 1px solid var(--edge);
  border-radius: 999px;
  padding: 9px 18px;
  cursor: pointer;
  transition: background .45s ease,color .45s ease;
  box-shadow: 0 6px 18px -10px rgba(0,0,0,.5);
}

.ssc-15 .ssc-15__toggle:focus-visible {
  outline: 3px solid oklch(0.65 0.15 280);
  outline-offset: 3px;
}

.ssc-15 .ssc-15__card {
  position: relative;
  width: min(340px,100%);
  background: var(--surface);
  border: 1px solid var(--edge);
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 22px 48px -30px rgba(0,0,0,.7);
  transition: background .45s ease;
}

.ssc-15 .ssc-15__media {
  width: 100%;
  aspect-ratio: 16/9;
  border-radius: 0;
}

.ssc-15 .ssc-15__body {
  padding: 18px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.ssc-15 .ssc-15__title {
  height: 16px;
}

.ssc-15 .ssc-15__block {
  display: flex;
  flex-direction: column;
  gap: 9px;
}

.ssc-15 .ssc-15__line {
  height: 11px;
}

@media (prefers-reduced-motion: reduce) {
  .ssc-15 .ssc-sk::after {
    animation: none;
    opacity: 0;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.ssc-15'); if (!root) return;
  const btn = root.querySelector('#ssc-15-toggle');
  // In production, seed from the OS preference instead of hardcoding dark:
  // root.dataset.theme = matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  btn.addEventListener('click', () => {
    const dark = root.dataset.theme !== 'dark';
    root.dataset.theme = dark ? 'dark' : 'light';
    btn.setAttribute('aria-pressed', String(dark));
    btn.textContent = dark ? '🌙 Dark' : '☀️ Light';
  });
})();
```
