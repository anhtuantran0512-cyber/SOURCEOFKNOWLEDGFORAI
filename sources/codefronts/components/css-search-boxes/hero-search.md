---
source: "codefronts"
url: "https://codefronts.com/components/css-search-boxes/hero-search/"
title: "Hero Section CSS Search Bar with CTA"
section: "components"
category: "css-search-boxes"
category_name: "CSS Search Bars"
description: "A landing-page hero built around search: an oversized field with a solid CTA fused to its right edge, a fluid headline above and popular-query chips below."
has_js: "true"
---

Here's a working CSS Search Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Hero Section CSS Search Bar with CTA
Source: https://codefronts.com/components/css-search-boxes/hero-search/

A landing-page hero built around search: an oversized field with a solid CTA fused to its right edge, a fluid headline above and popular-query chips below. Everything scales with clamp(), and the CTA drops under the field on narrow screens without a media-query pile-up.
## HTML
```html
<div class="sb-23">
  <button class="sb-23__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="sb-23__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="sb-23__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="sb-23__stage">
    <div class="sb-23__hero">
      <span class="sb-23__eyebrow">Marketplace</span>
      <h1 class="sb-23__h1">Search 10,000+ products from 400 independent makers</h1>
      <div class="sb-23__bar" role="search">
        <span class="sb-23__inputwrap">
          <svg class="sb-23__ico" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.4" stroke="currentColor" stroke-width="1.8"/><path d="m16 16 4.2 4.2" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
          <label class="sb-23__vh" for="sb-23-input">Search products</label>
          <input class="sb-23__input" id="sb-23-input" type="search" placeholder="Try &ldquo;wireless headphones&rdquo;" autocomplete="off">
        </span>
        <button class="sb-23__cta" type="button">
          Search
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M5 12h13m-5.5-5.5L18 12l-5.5 5.5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </button>
      </div>
      <div class="sb-23__chips">
        <span class="sb-23__chiplabel">Popular</span>
        <button class="sb-23__chip" type="button">wireless headphones</button>
        <button class="sb-23__chip" type="button">standing desk</button>
        <button class="sb-23__chip" type="button">espresso machine</button>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.sb-23 {
  --bg: #fbfaf9;
  --card: #ffffff;
  --ink: #151312;
  --muted: #6d6763;
  --line: #e6e2de;
  --acc: #1a5c3f;
  --acc-ink: #ffffff;
  --wash: #e8f2ec;
  --ring: #1a5c3f;
  --shadow: rgba(21,19,18,.16);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  box-sizing: border-box;
  font-family: system-ui,-apple-system,"Segoe UI",sans-serif;
  color: var(--ink);
  background: radial-gradient(46rem 26rem at 18% -6%, rgba(26,92,63,.10), transparent 68%), radial-gradient(38rem 24rem at 92% 8%, rgba(214,157,74,.14), transparent 66%), repeating-linear-gradient(0deg, rgba(21,19,18,.022) 0 1px, transparent 1px 76px), var(--bg);
  -webkit-font-smoothing: antialiased;
}

.sb-23 *,
.sb-23 *::before,
.sb-23 *::after {
  box-sizing: border-box;
}

.sb-23__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
}

.sb-23__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sb-23__hero {
  inline-size: min(46rem,100%);
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: 1.1rem;
}

.sb-23__eyebrow {
  padding: .32rem .7rem;
  border-radius: 999px;
  background: var(--wash);
  color: var(--acc);
  font: 600 .74rem/1 inherit;
  letter-spacing: .1em;
  text-transform: uppercase;
}

.sb-23__h1 {
  margin: 0;
  max-inline-size: 22ch;
  font-size: clamp(1.9rem,1.2rem + 3.4vw,3.4rem);
  font-weight: 700;
  line-height: 1.06;
  letter-spacing: -.028em;
  text-wrap: balance;
}

.sb-23__bar {
  display: flex;
  flex-wrap: wrap;
  gap: .5rem;
  inline-size: min(38rem,100%);
  margin-block-start: .6rem;
  padding: .42rem;
  border: 1px solid var(--line);
  border-radius: 18px;
  background: var(--card);
  box-shadow: 0 26px 50px -30px var(--shadow), 0 1px 2px rgba(21,19,18,.05);
  transition: box-shadow .24s, border-color .24s;
}

.sb-23__bar:focus-within {
  border-color: var(--acc);
  box-shadow: 0 30px 60px -30px var(--shadow), 0 0 0 4px rgba(26,92,63,.14);
}

.sb-23__inputwrap {
  display: flex;
  align-items: center;
  gap: .7rem;
  flex: 1 1 16rem;
  min-inline-size: 0;
  min-block-size: clamp(52px,3.4vw + 42px,62px);
  padding-inline: .95rem;
}

.sb-23__ico {
  inline-size: 20px;
  block-size: 20px;
  flex: none;
  color: var(--muted);
}

.sb-23__input {
  flex: 1;
  min-inline-size: 0;
  border: 0;
  background: none;
  color: var(--ink);
  text-align: start;
  font: 400 clamp(.98rem,.9rem + .3vw,1.08rem)/1 inherit;
}

.sb-23__input::placeholder {
  color: var(--muted);
}

.sb-23__input:focus {
  outline: none;
}

.sb-23__input::-webkit-search-cancel-button {
  -webkit-appearance: none;
  appearance: none;
}

.sb-23__cta {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: .45rem;
  flex: 1 1 auto;
  min-block-size: clamp(52px,3.4vw + 42px,62px);
  padding-inline: 1.6rem;
  border: 0;
  border-radius: 14px;
  background: var(--acc);
  color: var(--acc-ink);
  cursor: pointer;
  font: 650 1rem/1 inherit;
  letter-spacing: -.01em;
  transition: filter .18s, scale .12s;
}

.sb-23__cta:hover {
  filter: brightness(1.12);
}

.sb-23__cta:active {
  scale: .985;
}

.sb-23__cta svg {
  inline-size: 18px;
  block-size: 18px;
}

.sb-23__chips {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  gap: .45rem;
  margin-block-start: .4rem;
}

.sb-23__chiplabel {
  color: var(--muted);
  font: 600 .78rem/1 inherit;
  margin-inline-end: .2rem;
}

.sb-23__chip {
  min-block-size: 36px;
  padding-inline: .85rem;
  border: 1px solid var(--line);
  border-radius: 999px;
  background: var(--card);
  color: var(--ink);
  cursor: pointer;
  font: 500 .84rem/1 inherit;
  transition: background .16s, border-color .16s, translate .16s;
}

.sb-23__chip:hover {
  background: var(--wash);
  border-color: var(--acc);
  color: var(--acc);
  translate: 0 -1px;
}

.sb-23 :focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.sb-23__input:focus-visible {
  outline: none;
}

.sb-23[data-theme="dark"] {
  --bg: #0d0f0e;
  --card: #161a18;
  --ink: #eef1ee;
  --muted: #8d958f;
  --line: #242a27;
  --acc: #4ade80;
  --acc-ink: #0b1410;
  --wash: rgba(74,222,128,.14);
  --ring: #4ade80;
  --shadow: rgba(0,0,0,.7);
  background: radial-gradient(46rem 26rem at 18% -6%, rgba(74,222,128,.12), transparent 68%), radial-gradient(38rem 24rem at 92% 8%, rgba(214,157,74,.10), transparent 66%), var(--bg);
}

@media (prefers-color-scheme: dark) {
  .sb-23:not([data-theme="light"]) {
    --bg: #0d0f0e;
    --card: #161a18;
    --ink: #eef1ee;
    --muted: #8d958f;
    --line: #242a27;
    --acc: #4ade80;
    --acc-ink: #0b1410;
    --wash: rgba(74,222,128,.14);
    --ring: #4ade80;
    --shadow: rgba(0,0,0,.7);
    background: radial-gradient(46rem 26rem at 18% -6%, rgba(74,222,128,.12), transparent 68%), radial-gradient(38rem 24rem at 92% 8%, rgba(214,157,74,.10), transparent 66%), var(--bg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sb-23 *,
    .sb-23 *::before,
    .sb-23 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .sb-23__bar,
    .sb-23__cta,
    .sb-23__chip {
    border: 1px solid CanvasText;
  }
}

.sb-23__theme {
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

.sb-23[data-theme="dark"] .sb-23__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .sb-23:not([data-theme="light"]) .sb-23__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.sb-23__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.sb-23[data-theme="dark"] .sb-23__theme:hover,
.sb-23:not([data-theme="light"]) .sb-23__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.sb-23__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.sb-23__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.sb-23__sun {
  display: none;
}

.sb-23__theme[aria-pressed="true"] .sb-23__sun {
  display: block;
}

.sb-23__theme[aria-pressed="true"] .sb-23__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .sb-23__theme {
    transition: none;
  }

  .sb-23__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(()=>{const r=document.querySelector('.sb-23');if(!r)return;const t=r.querySelector('.sb-23__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
