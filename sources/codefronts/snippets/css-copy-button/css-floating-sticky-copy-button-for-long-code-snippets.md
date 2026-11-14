---
source: "codefronts"
url: "https://codefronts.com/snippets/css-copy-button/css-floating-sticky-copy-button-for-long-code-snippets/"
title: "CSS Floating Sticky Copy Button for Long Code Snippets"
section: "snippets"
category: "css-copy-button"
category_name: "CSS Copy Buttons"
description: "A forty-line snippet in a scrollable container, with a copy button that stays reachable the whole way down."
has_js: "true"
---

Here's a working CSS Copy Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Floating Sticky Copy Button for Long Code Snippets
Source: https://codefronts.com/snippets/css-copy-button/css-floating-sticky-copy-button-for-long-code-snippets/

A forty-line snippet in a scrollable container, with a copy button that stays reachable the whole way down. It is position:sticky in a scroll container the block owns &mdash; not fixed, which would float over unrelated content &mdash; plus the two silent sticky killers spelled out: an ancestor overflow that is not visible, and an ancestor transform.
## HTML
```html
<div class="cpy-10">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&display=swap">
  <input class="cpy-10__sr" type="checkbox" id="cpy-10-dark">
  <label class="cpy-10__theme" for="cpy-10-dark" title="Switch light or dark theme">
    <svg class="cpy-10__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.3" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.7v2.2M12 19.1v2.2M2.7 12h2.2M19.1 12h2.2M5.4 5.4l1.6 1.6M17 17l1.6 1.6M18.6 5.4 17 7M7 17l-1.6 1.6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="cpy-10__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="cpy-10__vh">Switch light or dark theme</span>
  </label>

  <div class="cpy-10__stage">
    <div class="cpy-10__wrap">
      <p class="cpy-10__eyebrow">Sticky &middot; long snippet</p>
      <h2 class="cpy-10__title">Scroll the snippet, keep the button</h2>

      <div class="cpy-10__block">
        <div class="cpy-10__scroll" tabindex="0" role="group" aria-label="Scrollable code snippet">
          <div class="cpy-10__bar">
            <span class="cpy-10__pos" aria-hidden="true">line 1 / 24</span>
            <button class="cpy-10__btn" type="button" data-state="idle">
              <span class="cpy-10__icons">
                <svg class="cpy-10__i1" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><rect x="9" y="9" width="11" height="11" rx="2.4" stroke="currentColor" stroke-width="1.8"/><path d="M15.5 5.6A2.6 2.6 0 0 0 13 4H6.6A2.6 2.6 0 0 0 4 6.6V13a2.6 2.6 0 0 0 1.6 2.4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
                <svg class="cpy-10__i2" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4.8 12.6 9.5 17.3 19.2 7.2" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"/></svg>
              </span>
              <span class="cpy-10__labels"><span class="cpy-10__l1">Copy all</span><span class="cpy-10__l2">Copied</span></span>
            </button>
          </div>
          <pre class="cpy-10__pre"><code id="cpy-10-code">:root{
  --copy-dur:200ms;
  --copy-radius:.8rem;
}
.copy{
  min-block-size:2.75rem;
  display:inline-flex;
  align-items:center;
  gap:.5rem;
  padding-inline:1rem;
  border-radius:var(--copy-radius);
  transition:background var(--copy-dur);
}
.copy__icons{position:relative; inline-size:1.1rem; block-size:1.1rem;}
.copy__icons svg{position:absolute; inset:0;}
.copy__tick{stroke-dasharray:1; stroke-dashoffset:1;}
.copy[data-state="copied"] .copy__tick{stroke-dashoffset:0;}
.copy__labels{display:grid;}
.copy__labels span{grid-area:1/1;}
@media (prefers-reduced-motion:reduce){
  .copy,.copy *{transition:none;}
}
@media (forced-colors:active){
  .copy{border:1px solid CanvasText;}
}
/* end of snippet - the button is still up there */</code></pre>
        </div>
      </div>

      <p class="cpy-10__note">Two things silently break sticky: an ancestor with <code>overflow</code> other than <code>visible</code>, and an ancestor with a <code>transform</code>. Both create a containing block the sticky element cannot escape.</p>
      <p class="cpy-10__live" role="status" aria-live="polite"></p>
    </div>
  </div>
</div>
```
## CSS
```css
.cpy-10 {
  --bg: #f7f7f9;
  --panel: #ffffff;
  --code: #0f1216;
  --code-ink: #dee4ec;
  --ink: #0b0d12;
  --muted: #5b6069;
  --line: rgba(11,13,18,.11);
  --accent: #6366f1;
  --ok: #34d399;
  --dur: 190ms;
  --sans: system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.cpy-10 *,
.cpy-10 *::before,
.cpy-10 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(.5 .1 250)) {
  .cpy-10 {
    --accent: oklch(.6 .19 277);
    --ok: oklch(.78 .15 162);
  }
}

.cpy-10__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  clip-path: inset(50%);
  pointer-events: none;
}

.cpy-10__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cpy-10__theme {
  position: absolute;
  inset-block-start: clamp(1rem,3vw,1.75rem);
  inset-inline-end: clamp(1rem,3vw,1.75rem);
  z-index: 5;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  border-radius: 999px;
  border: 1px solid var(--line);
  background: rgba(255,255,255,.6);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  color: var(--ink);
  cursor: pointer;
}

.cpy-10__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.cpy-10__moon {
  display: none;
}

.cpy-10__sr:focus-visible + .cpy-10__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.cpy-10__stage {
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,6vw,4.5rem);
}

.cpy-10__wrap {
  inline-size: min(100%,40rem);
  display: grid;
  gap: .85rem;
}

.cpy-10__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.cpy-10__title {
  margin: 0 0 .2rem;
  font-size: clamp(1.4rem,3.4vw,1.95rem);
  line-height: 1.15;
  letter-spacing: -.02em;
  font-weight: 640;
}

.cpy-10__block {
  border-radius: 1.15rem;
  background: var(--code);
  border: 1px solid rgba(255,255,255,.08);
  overflow: hidden;
  box-shadow: 0 26px 50px -34px rgba(11,13,18,.6);
}

.cpy-10__scroll {
  max-block-size: 22rem;
  overflow-y: auto;
  overscroll-behavior: contain;
  scrollbar-gutter: stable;
}

.cpy-10__scroll:focus-visible {
  outline: 2px solid var(--ok);
  outline-offset: -2px;
}

.cpy-10__bar {
  position: sticky;
  inset-block-start: 0;
  z-index: 2;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: .75rem;
  padding: .6rem .65rem;
  background: color-mix(in srgb,var(--code) 82%,transparent);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  border-block-end: 1px solid rgba(255,255,255,.07);
}

.cpy-10__pos {
  font-family: var(--mono);
  font-size: .7rem;
  letter-spacing: .06em;
  color: rgba(255,255,255,.5);
  padding-inline-start: .35rem;
}

.cpy-10__pre {
  margin: 0;
  padding: 1rem 1.25rem 1.4rem;
  overflow-x: auto;
}

.cpy-10__pre code {
  font-family: var(--mono);
  font-size: clamp(.74rem,1.4vw,.85rem);
  line-height: 1.85;
  color: var(--code-ink);
  white-space: pre;
}

.cpy-10__btn {
  flex: none;
  min-block-size: 2.4rem;
  min-inline-size: 44px;
  display: inline-flex;
  align-items: center;
  gap: .45rem;
  padding-inline: .8rem;
  border: 1px solid rgba(255,255,255,.16);
  border-radius: .65rem;
  background: rgba(255,255,255,.09);
  color: var(--code-ink);
  font: inherit;
  font-size: .8rem;
  font-weight: 540;
  cursor: pointer;
  transition: background var(--dur),color var(--dur),border-color var(--dur),scale var(--dur);
}

.cpy-10__btn:hover {
  background: rgba(255,255,255,.17);
}

.cpy-10__btn:active {
  scale: .96;
}

.cpy-10__btn:focus-visible {
  outline: 2px solid var(--ok);
  outline-offset: 2px;
}

.cpy-10__btn[data-state="copied"] {
  color: var(--ok);
  border-color: color-mix(in srgb,var(--ok) 45%,transparent);
}

.cpy-10__icons {
  position: relative;
  inline-size: 1rem;
  block-size: 1rem;
  flex: none;
}

.cpy-10__icons svg {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  transition: opacity var(--dur),scale var(--dur);
}

.cpy-10__i2 {
  opacity: 0;
  scale: .55;
}

.cpy-10__btn[data-state="copied"] .cpy-10__i1 {
  opacity: 0;
  scale: .55;
}

.cpy-10__btn[data-state="copied"] .cpy-10__i2 {
  opacity: 1;
  scale: 1;
}

.cpy-10__labels {
  display: grid;
}

.cpy-10__labels span {
  grid-area: 1/1;
  transition: opacity var(--dur),translate var(--dur);
}

.cpy-10__l2 {
  opacity: 0;
  translate: 0 .35rem;
}

.cpy-10__btn[data-state="copied"] .cpy-10__l1 {
  opacity: 0;
  translate: 0 -.35rem;
}

.cpy-10__btn[data-state="copied"] .cpy-10__l2 {
  opacity: 1;
  translate: 0 0;
}

.cpy-10__note {
  margin: 0;
  font-size: .86rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.cpy-10__note code {
  font-family: var(--mono);
  font-size: .78rem;
  padding: .1rem .3rem;
  border-radius: .3rem;
  background: var(--panel);
}

.cpy-10__live {
  margin: 0;
  min-block-size: 1.2rem;
  font-family: var(--mono);
  font-size: .78rem;
  color: var(--accent);
}

@media not (prefers-color-scheme: dark) {
  .cpy-10:has(#cpy-10-dark:checked) {
    --bg: #07080b;
    --panel: #101318;
    --code: #12151a;
    --ink: #e8eaf0;
    --muted: rgba(232,234,240,.62);
    --line: rgba(232,234,240,.14);
    --accent: #a5b4fc;
  }

  .cpy-10:has(#cpy-10-dark:checked) .cpy-10__theme {
    background: rgba(255,255,255,.07);
  }

  .cpy-10:has(#cpy-10-dark:checked) .cpy-10__sun {
    display: none;
  }

  .cpy-10:has(#cpy-10-dark:checked) .cpy-10__moon {
    display: block;
  }
}

@media (prefers-color-scheme: dark) {
  .cpy-10:not([data-theme="light"]):not(:has(#cpy-10-dark:checked)) {
    --bg: #07080b;
    --panel: #101318;
    --code: #12151a;
    --ink: #e8eaf0;
    --muted: rgba(232,234,240,.62);
    --line: rgba(232,234,240,.14);
    --accent: #a5b4fc;
  }

  .cpy-10__theme {
    background: rgba(255,255,255,.07);
  }

  .cpy-10__sun {
    display: none;
  }

  .cpy-10__moon {
    display: block;
  }

  .cpy-10:has(#cpy-10-dark:checked) .cpy-10__sun {
    display: block;
  }

  .cpy-10:has(#cpy-10-dark:checked) .cpy-10__moon {
    display: none;
  }
}

.cpy-10[data-theme="dark"] {
  --bg: #07080b;
  --panel: #101318;
  --code: #12151a;
  --ink: #e8eaf0;
  --muted: rgba(232,234,240,.62);
  --line: rgba(232,234,240,.14);
  --accent: #a5b4fc;
}

@media (prefers-reduced-motion: reduce) {
  .cpy-10 *,
    .cpy-10 *::before,
    .cpy-10 *::after {
    transition: none !important;
    animation: none !important;
    scroll-behavior: auto !important;
  }
}

@media (forced-colors: active) {
  .cpy-10__block,
    .cpy-10__btn,
    .cpy-10__bar,
    .cpy-10__theme {
    border-color: CanvasText;
    background: Canvas;
    color: CanvasText;
    box-shadow: none;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
  }
}
```

## JavaScript
```js
const cpy10 = document.querySelector('.cpy-10');
if (cpy10) {
  const btn = cpy10.querySelector('.cpy-10__btn');
  const code = cpy10.querySelector('#cpy-10-code');
  const live = cpy10.querySelector('.cpy-10__live');
  const scroll = cpy10.querySelector('.cpy-10__scroll');
  const pos = cpy10.querySelector('.cpy-10__pos');
  const total = code.textContent.split('\n').length;
  scroll.addEventListener('scroll', () => {          // proof the sticky bar never leaves
    const ratio = scroll.scrollTop / Math.max(1, scroll.scrollHeight - scroll.clientHeight);
    pos.textContent = 'line ' + Math.max(1, Math.round(ratio * total)) + ' / ' + total;
  }, { passive: true });
  let timer;
  btn.addEventListener('click', async () => {
    let ok = true;
    try { await navigator.clipboard.writeText(code.textContent); } catch { ok = false; }
    btn.dataset.state = ok ? 'copied' : 'idle';
    live.textContent = ok ? 'Copied all ' + total + ' lines' : 'Clipboard blocked - press Ctrl C';
    clearTimeout(timer);
    timer = setTimeout(() => { btn.dataset.state = 'idle'; live.textContent = ''; }, 2000);
  });
}
```
