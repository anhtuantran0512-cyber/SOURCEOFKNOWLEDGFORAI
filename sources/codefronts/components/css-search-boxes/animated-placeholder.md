---
source: "codefronts"
url: "https://codefronts.com/components/css-search-boxes/animated-placeholder/"
title: "CSS Search Bar with Rotating Placeholder Text"
section: "components"
category: "css-search-boxes"
category_name: "CSS Search Bars"
description: "The placeholder cycles through four real example queries — wireless headphones, invoice template, Q3 revenue, team photo — on a stacked-keyframe rotator with…"
has_js: "true"
---

Here's a working CSS Search Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Search Bar with Rotating Placeholder Text
Source: https://codefronts.com/components/css-search-boxes/animated-placeholder/

The placeholder cycles through four real example queries — wireless headphones, invoice template, Q3 revenue, team photo — on a stacked-keyframe rotator with a blinking type cursor. It disappears the instant you type, and it is 100% CSS: the real placeholder attribute stays empty-but-present so :placeholder-shown still works.
## HTML
```html
<div class="sb-19">
  <button class="sb-19__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="sb-19__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="sb-19__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="sb-19__stage">
    <div class="sb-19__bar" role="search">
      <svg class="sb-19__ico" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.4" stroke="currentColor" stroke-width="1.8"/><path d="m16 16 4.2 4.2" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
      <span class="sb-19__box">
        <label class="sb-19__vh" for="sb-19-input">Search products, documents and people</label>
        <input class="sb-19__input" id="sb-19-input" type="search" placeholder=" " autocomplete="off">
        <span class="sb-19__rot" aria-hidden="true">
          <span>Search &ldquo;wireless headphones&rdquo;</span>
          <span>Search &ldquo;invoice template&rdquo;</span>
          <span>Search &ldquo;Q3 revenue&rdquo;</span>
          <span>Search &ldquo;team photo&rdquo;</span>
          <i class="sb-19__caret"></i>
        </span>
      </span>
      <kbd class="sb-19__kbd">/</kbd>
    </div>
  </div>
</div>
```
## CSS
```css
.sb-19 {
  --bg: #f7f7f9;
  --card: #ffffff;
  --ink: #16181d;
  --muted: #71767f;
  --line: #e5e6ea;
  --acc: #111318;
  --ring: #4f46e5;
  --shadow: rgba(22,24,29,.14);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  box-sizing: border-box;
  font-family: system-ui,-apple-system,"Segoe UI",sans-serif;
  color: var(--ink);
  background: radial-gradient(36rem 20rem at 50% 10%, #fff, var(--bg) 76%);
  -webkit-font-smoothing: antialiased;
}

.sb-19 *,
.sb-19 *::before,
.sb-19 *::after {
  box-sizing: border-box;
}

.sb-19__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
}

.sb-19__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sb-19__bar {
  display: flex;
  align-items: center;
  gap: .75rem;
  inline-size: min(30rem,100%);
  min-block-size: 56px;
  padding-inline: 1.05rem .5rem;
  border: 1px solid var(--line);
  border-radius: 15px;
  background: var(--card);
  box-shadow: 0 1px 2px rgba(22,24,29,.05);
  transition: border-color .2s, box-shadow .2s;
}

.sb-19__bar:focus-within {
  border-color: var(--acc);
  box-shadow: 0 0 0 4px rgba(17,19,24,.08);
}

.sb-19__ico {
  inline-size: 19px;
  block-size: 19px;
  flex: none;
  color: var(--muted);
}

.sb-19__box {
  position: relative;
  flex: 1;
  min-inline-size: 0;
  display: flex;
  align-items: center;
}

.sb-19__input {
  position: relative;
  z-index: 2;
  inline-size: 100%;
  border: 0;
  background: none;
  color: var(--ink);
  font: 400 .97rem/1.2 inherit;
}

.sb-19__input:focus {
  outline: none;
}

.sb-19__input::-webkit-search-cancel-button {
  -webkit-appearance: none;
  appearance: none;
}

.sb-19__rot {
  position: absolute;
  inset-block: 0;
  inset-inline: 0;
  z-index: 1;
  display: flex;
  align-items: center;
  pointer-events: none;
  color: var(--muted);
  font: 400 .97rem/1.2 inherit;
  overflow: hidden;
  transition: opacity .18s;
}

.sb-19__rot span {
  position: absolute;
  inset-inline-start: 0;
  white-space: nowrap;
  opacity: 0;
  animation: sb-19-cycle 12s cubic-bezier(.2,.9,.25,1) infinite;
}

.sb-19__rot span:nth-child(2) {
  animation-delay: 3s;
}

.sb-19__rot span:nth-child(3) {
  animation-delay: 6s;
}

.sb-19__rot span:nth-child(4) {
  animation-delay: 9s;
}

@keyframes sb-19-cycle {
  0%,
    2% {
    opacity: 0;
    -webkit-transform: translateY(6px);
    transform: translateY(6px);
    translate: 0 6px;
  }

  6%,
    22% {
    opacity: 1;
    -webkit-transform: none;
    transform: none;
    translate: 0 0;
  }

  27%,
    100% {
    opacity: 0;
    -webkit-transform: translateY(-6px);
    transform: translateY(-6px);
    translate: 0 -6px;
  }
}

.sb-19__caret {
  position: absolute;
  inset-inline-start: 0;
  inline-size: 1.5px;
  block-size: 1.15em;
  background: var(--acc);
  opacity: .55;
  animation: sb-19-blink 1s steps(1,end) infinite;
  margin-inline-start: -.35rem;
}

@keyframes sb-19-blink {
  0%,
    49% {
    opacity: .55;
  }

  50%,
    100% {
    opacity: 0;
  }
}

.sb-19__input:not(:placeholder-shown) ~ .sb-19__rot {
  opacity: 0;
}

.sb-19__kbd {
  display: inline-grid;
  place-items: center;
  inline-size: 1.9rem;
  block-size: 1.9rem;
  flex: none;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: #fafbfc;
  color: var(--muted);
  font: 500 .82rem/1 ui-monospace,Menlo,monospace;
}

.sb-19 :focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

.sb-19__input:focus-visible {
  outline: none;
}

.sb-19[data-theme="dark"] {
  --bg: #0b0c10;
  --card: #141720;
  --ink: #eceef4;
  --muted: #878d99;
  --line: #232833;
  --acc: #eceef4;
  --ring: #8b83ff;
  --shadow: rgba(0,0,0,.7);
  background: radial-gradient(36rem 20rem at 50% 10%, #171b26, var(--bg) 76%);
}

.sb-19[data-theme="dark"] .sb-19__kbd {
  background: #1a1f2a;
}

.sb-19[data-theme="dark"] .sb-19__bar:focus-within {
  box-shadow: 0 0 0 4px rgba(236,238,244,.09);
}

@media (prefers-color-scheme: dark) {
  .sb-19:not([data-theme="light"]) {
    --bg: #0b0c10;
    --card: #141720;
    --ink: #eceef4;
    --muted: #878d99;
    --line: #232833;
    --acc: #eceef4;
    --ring: #8b83ff;
    --shadow: rgba(0,0,0,.7);
    background: radial-gradient(36rem 20rem at 50% 10%, #171b26, var(--bg) 76%);
  }

  .sb-19:not([data-theme="light"]) .sb-19__kbd {
    background: #1a1f2a;
  }

  .sb-19:not([data-theme="light"]) .sb-19__bar:focus-within {
    box-shadow: 0 0 0 4px rgba(236,238,244,.09);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sb-19 *,
    .sb-19 *::before,
    .sb-19 *::after {
    animation: none !important;
    transition: none !important;
  }

  .sb-19__rot span {
    opacity: 0;
  }

  .sb-19__rot span:first-child {
    opacity: 1;
  }
}

@media (forced-colors: active) {
  .sb-19__bar,
    .sb-19__kbd {
    border: 1px solid CanvasText;
  }
}

.sb-19__theme {
  position: absolute;
  inset-block-start: clamp(.75rem,2vw,1.25rem);
  inset-inline-end: clamp(.75rem,2vw,1.25rem);
  z-index: 50;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  padding: 0;
  border-radius: 999px;
  border: 1px solid rgba(0,0,0,.12);
  color: currentColor;
  background: rgba(255,255,255,.72);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  transition: background .25s ease, transform .25s cubic-bezier(.16,1,.3,1), border-color .25s ease;
}

.sb-19[data-theme="dark"] .sb-19__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .sb-19:not([data-theme="light"]) .sb-19__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.sb-19__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.sb-19[data-theme="dark"] .sb-19__theme:hover,
.sb-19:not([data-theme="light"]) .sb-19__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.sb-19__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.sb-19__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.sb-19__sun {
  display: none;
}

.sb-19__theme[aria-pressed="true"] .sb-19__sun {
  display: block;
}

.sb-19__theme[aria-pressed="true"] .sb-19__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .sb-19__theme {
    transition: none;
  }

  .sb-19__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(()=>{const r=document.querySelector('.sb-19');if(!r)return;const t=r.querySelector('.sb-19__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
