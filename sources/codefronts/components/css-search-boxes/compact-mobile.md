---
source: "codefronts"
url: "https://codefronts.com/components/css-search-boxes/compact-mobile/"
title: "Mobile-First Compact CSS Search Bar"
section: "components"
category: "css-search-boxes"
category_name: "CSS Search Bars"
description: "Sized for thumbs: a 44&times;44 minimum target, 16px text (so iOS never zooms on focus), an inset pressed state, and an iOS-style Cancel link that slides in…"
has_js: "true"
---

Here's a working CSS Search Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Mobile-First Compact CSS Search Bar
Source: https://codefronts.com/components/css-search-boxes/compact-mobile/

Sized for thumbs: a 44&times;44 minimum target, 16px text (so iOS never zooms on focus), an inset pressed state, and an iOS-style Cancel link that slides in on focus. Includes env(safe-area-inset-*) padding for notched devices.
## HTML
```html
<div class="sb-30">
  <button class="sb-30__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="sb-30__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="sb-30__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="sb-30__stage">
    <div class="sb-30__phone">
      <div class="sb-30__dock">
        <div class="sb-30__bar" role="search">
          <div class="sb-30__field">
            <svg class="sb-30__ico" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.2" stroke="currentColor" stroke-width="2"/><path d="m15.8 15.8 4.4 4.4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
            <label class="sb-30__vh" for="sb-30-input">Search</label>
            <input class="sb-30__input" id="sb-30-input" type="search" placeholder="Search" autocomplete="off" enterkeyhint="search">
          </div>
          <button class="sb-30__cancel" type="button"><span>Cancel</span></button>
        </div>

        <ul class="sb-30__list" aria-label="Recent">
          <li><span class="sb-30__thumb" aria-hidden="true"></span>Wireless headphones<span class="sb-30__meta">Audio</span></li>
          <li><span class="sb-30__thumb" aria-hidden="true"></span>Standing desk mat<span class="sb-30__meta">Home</span></li>
          <li><span class="sb-30__thumb" aria-hidden="true"></span>Travel mug 500ml<span class="sb-30__meta">Kitchen</span></li>
        </ul>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.sb-30 {
  --bg: #eceef2;
  --card: #ffffff;
  --field: #eef0f4;
  --ink: #0f1115;
  --muted: #71767f;
  --line: #e2e4ea;
  --acc: #0a7cff;
  --ring: #0a7cff;
  --shadow: rgba(15,17,21,.18);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  box-sizing: border-box;
  font-family: -apple-system,system-ui,"Segoe UI",sans-serif;
  color: var(--ink);
  background: var(--bg);
  -webkit-font-smoothing: antialiased;
}

.sb-30 *,
.sb-30 *::before,
.sb-30 *::after {
  box-sizing: border-box;
}

.sb-30__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
}

.sb-30__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sb-30__phone {
  inline-size: min(22rem,100%);
  border: 1px solid var(--line);
  border-radius: 26px;
  background: var(--card);
  box-shadow: 0 30px 60px -34px var(--shadow), 0 1px 2px rgba(15,17,21,.05);
  overflow: hidden;
}

.sb-30__dock {
  padding: .85rem .8rem calc(.85rem + env(safe-area-inset-bottom, 0px));
  padding-inline-start: calc(.8rem + env(safe-area-inset-left, 0px));
  padding-inline-end: calc(.8rem + env(safe-area-inset-right, 0px));
}

.sb-30__bar {
  display: flex;
  align-items: center;
  gap: .25rem;
}

.sb-30__field {
  display: flex;
  align-items: center;
  gap: .5rem;
  flex: 1;
  min-inline-size: 0;
  min-block-size: 44px;
  padding-inline: .75rem;
  border-radius: 12px;
  background: var(--field);
  transition: box-shadow .18s, background .18s;
}

@media (hover: hover) {
  .sb-30__field:hover {
    background: #e7e9ee;
  }
}

.sb-30__field:active {
  box-shadow: inset 0 2px 5px rgba(15,17,21,.12);
}

.sb-30__field:focus-within {
  background: var(--card);
  box-shadow: 0 0 0 2px var(--acc);
}

.sb-30__ico {
  inline-size: 17px;
  block-size: 17px;
  flex: none;
  color: var(--muted);
}

.sb-30__input {
  flex: 1;
  min-inline-size: 0;
  border: 0;
  background: none;
  color: var(--ink);
  font-size: 16px;
  line-height: 1;
  font-family: inherit;
  /* 16px stops iOS zoom-on-focus */
}

.sb-30__input::placeholder {
  color: var(--muted);
}

.sb-30__input:focus {
  outline: none;
}

.sb-30__input::-webkit-search-cancel-button {
  -webkit-appearance: none;
  appearance: none;
}

.sb-30__cancel {
  display: grid;
  grid-template-columns: 0fr;
  min-block-size: 44px;
  border: 0;
  background: none;
  color: var(--acc);
  cursor: pointer;
  font: 400 16px/1 inherit;
  overflow: hidden;
  transition: grid-template-columns .26s cubic-bezier(.2,.9,.25,1), padding .26s;
  padding-inline: 0;
}

.sb-30__cancel > span {
  min-inline-size: 0;
  overflow: hidden;
  white-space: nowrap;
  align-self: center;
}

.sb-30__bar:focus-within .sb-30__cancel {
  grid-template-columns: 1fr;
  padding-inline: .65rem .35rem;
}

.sb-30__cancel:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

.sb-30__list {
  list-style: none;
  margin: .9rem 0 0;
  padding: 0;
  display: flex;
  flex-direction: column;
}

.sb-30__list li {
  display: flex;
  align-items: center;
  gap: .7rem;
  min-block-size: 52px;
  padding-inline: .15rem;
  border-block-end: 1px solid var(--line);
  font: 400 .95rem/1.2 inherit;
}

.sb-30__list li:last-child {
  border-block-end: 0;
}

.sb-30__thumb {
  inline-size: 34px;
  block-size: 34px;
  flex: none;
  border-radius: 9px;
  background: linear-gradient(135deg,#dde1e8,#eef0f4);
}

.sb-30__meta {
  margin-inline-start: auto;
  color: var(--muted);
  font: 400 .82rem/1 inherit;
}

.sb-30 :focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

.sb-30__input:focus-visible {
  outline: none;
}

.sb-30[data-theme="dark"] {
  --bg: #000000;
  --card: #111114;
  --field: #1c1c1f;
  --ink: #f2f2f5;
  --muted: #8e8e93;
  --line: #26262a;
  --acc: #0a84ff;
  --ring: #0a84ff;
  --shadow: rgba(0,0,0,.9);
}

.sb-30[data-theme="dark"] .sb-30__thumb {
  background: linear-gradient(135deg,#26262a,#1a1a1e);
}

@media (prefers-color-scheme: dark) {
  .sb-30:not([data-theme="light"]) {
    --bg: #000000;
    --card: #111114;
    --field: #1c1c1f;
    --ink: #f2f2f5;
    --muted: #8e8e93;
    --line: #26262a;
    --acc: #0a84ff;
    --ring: #0a84ff;
    --shadow: rgba(0,0,0,.9);
  }

  .sb-30:not([data-theme="light"]) .sb-30__thumb {
    background: linear-gradient(135deg,#26262a,#1a1a1e);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sb-30 *,
    .sb-30 *::before,
    .sb-30 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .sb-30__phone,
    .sb-30__field {
    border: 1px solid CanvasText;
  }
}

.sb-30__theme {
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

.sb-30[data-theme="dark"] .sb-30__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .sb-30:not([data-theme="light"]) .sb-30__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.sb-30__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.sb-30[data-theme="dark"] .sb-30__theme:hover,
.sb-30:not([data-theme="light"]) .sb-30__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.sb-30__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.sb-30__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.sb-30__sun {
  display: none;
}

.sb-30__theme[aria-pressed="true"] .sb-30__sun {
  display: block;
}

.sb-30__theme[aria-pressed="true"] .sb-30__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .sb-30__theme {
    transition: none;
  }

  .sb-30__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(()=>{const r=document.querySelector('.sb-30');if(!r)return;const t=r.querySelector('.sb-30__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
