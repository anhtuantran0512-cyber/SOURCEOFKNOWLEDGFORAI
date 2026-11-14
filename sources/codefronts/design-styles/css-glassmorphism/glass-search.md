---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-glassmorphism/glass-search/"
title: "Glassmorphism Search Bar"
section: "design-styles"
category: "css-glassmorphism"
category_name: "CSS Glassmorphism"
description: "A wide frosted search bar with an inline SVG icon, a clear button, a filter chip and a suggestions panel that appears on :focus-within — the Google-bar…"
has_js: "false"
---

Here's a working CSS Glassmorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Search Bar
Source: https://codefronts.com/design-styles/css-glassmorphism/glass-search/

A wide frosted search bar with an inline SVG icon, a clear button, a filter chip and a suggestions panel that appears on :focus-within — the Google-bar pattern rebuilt as glass. Marked up as <search> with role="search", and it never touches a form submit handler, so it runs in any sandboxed playground.
## HTML
```html
<div class="gm-19">
  <input class="gm-19__sr" type="checkbox" id="gm-19-theme">
  <label class="gm-19__theme" for="gm-19-theme" title="Switch theme">
    <svg class="gm-19__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="gm-19__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="gm-19__vh">Switch light or dark theme</span>
  </label>

  <div class="gm-19__stage">
    <div class="gm-19__wrap">
      <header class="gm-19__head">
        <p class="gm-19__eyebrow">&lt;search&gt; · :focus-within</p>
        <h2 class="gm-19__h">Search anything in Atlas</h2>
      </header>

      <search class="gm-19__search" role="search">
        <div class="gm-19__shell">
          <span class="gm-19__icon" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none"><circle cx="11" cy="11" r="6.6" stroke="currentColor" stroke-width="1.8"/><path d="m16.2 16.2 4.3 4.3" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
          </span>
          <label class="gm-19__vh" for="gm-19-q">Search components, tokens and docs</label>
          <input class="gm-19__input" id="gm-19-q" type="search" placeholder="Search anything…" autocomplete="off" spellcheck="false">
          <button class="gm-19__clear" type="button" aria-label="Clear search">
            <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M7 7l10 10M17 7L7 17" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>
          </button>
          <button class="gm-19__filter" type="button">
            <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4 7h16M7 12h10M10 17h4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
            <span>Filters</span>
            <span class="gm-19__count">2</span>
          </button>
        </div>

        <div class="gm-19__panel">
          <p class="gm-19__ptitle">Suggestions</p>
          <ul class="gm-19__list">
            <li><button class="gm-19__item" type="button"><span class="gm-19__ikind">token</span>--surface-glass-24<span class="gm-19__imeta">blur 24px · saturate 180%</span></button></li>
            <li><button class="gm-19__item" type="button"><span class="gm-19__ikind">component</span>GlassSheet<span class="gm-19__imeta">modal · sidebar · popover</span></button></li>
            <li><button class="gm-19__item" type="button"><span class="gm-19__ikind">doc</span>Choosing a blur radius<span class="gm-19__imeta">updated by Alex Chen</span></button></li>
            <li><button class="gm-19__item" type="button"><span class="gm-19__ikind">token</span>--rim-highlight-top<span class="gm-19__imeta">inset 0 1px 0 white 50%</span></button></li>
          </ul>
          <p class="gm-19__phint">Panel opens on <span class="gm-19__code">:focus-within</span> — no JavaScript, no submit handler.</p>
        </div>
      </search>

      <div class="gm-19__chips">
        <span class="gm-19__chip">materials</span>
        <span class="gm-19__chip">tokens</span>
        <span class="gm-19__chip">accessibility</span>
        <span class="gm-19__chip">performance</span>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

.gm-19 {
  --a1: rgba(251,146,60,.5);
  --a2: rgba(56,189,248,.55);
  --a3: rgba(168,85,247,.5);
  --a4: rgba(52,211,153,.42);
  --base: #f2f4fb;
  --base2: #e3e9fc;
  --ink: #0f1120;
  --muted: rgba(15,17,32,.66);
  --tint: #ffffff;
  --accent: #4f46e5;
  --rim: rgba(255,255,255,.9);
  --rim2: rgba(255,255,255,.5);
  --edge: rgba(15,17,32,.12);
  --mono: 'Geist Mono',ui-monospace,'SFMono-Regular',Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  overflow: hidden;
  box-sizing: border-box;
  color: var(--ink);
  isolation: isolate;
  font-family: 'Geist',ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif;
  background: radial-gradient(52% 44% at 10% 16%, var(--a1) 0%, transparent 60%), radial-gradient(54% 46% at 90% 14%, var(--a2) 0%, transparent 62%), radial-gradient(48% 42% at 78% 88%, var(--a3) 0%, transparent 60%), radial-gradient(44% 38% at 16% 90%, var(--a4) 0%, transparent 58%), linear-gradient(160deg, var(--base) 0%, var(--base2) 52%, var(--base) 100%);
}

.gm-19 *,
.gm-19 *::before,
.gm-19 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 300)) {
  .gm-19 {
    --a1: oklch(0.82 0.15 60 / .52);
    --a2: oklch(0.82 0.14 220 / .56);
    --a3: oklch(0.72 0.2 305 / .5);
    --a4: oklch(0.84 0.14 165 / .44);
    --base: oklch(0.97 0.008 275);
    --base2: oklch(0.93 0.03 275);
    --accent: oklch(0.52 0.2 285);
  }
}

.gm-19__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.gm-19__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.gm-19__theme {
  position: absolute;
  inset-block-start: 1.15rem;
  inset-inline-end: 1.15rem;
  z-index: 8;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  border-radius: 999px;
  color: var(--ink);
  background: rgba(255,255,255,.5);
  border: 1px solid var(--edge);
  -webkit-backdrop-filter: blur(10px) saturate(180%);
  backdrop-filter: blur(10px) saturate(180%);
  box-shadow: inset 0 1px 0 var(--rim), 0 10px 24px -16px rgba(20,20,60,.45);
  transition: scale .18s ease;
}

.gm-19__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: inherit;
}

.gm-19__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.gm-19__theme:hover {
  scale: 1.06;
}

.gm-19__sr:focus-visible + .gm-19__theme {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.gm-19__sun {
  display: none;
}

.gm-19__moon {
  display: block;
}

.gm-19__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,4vw,3.5rem);
}

.gm-19__wrap {
  inline-size: min(44rem,100%);
  display: grid;
  gap: 1.1rem;
}

.gm-19__head {
  display: grid;
  gap: .4rem;
  justify-items: center;
  text-align: center;
}

.gm-19__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .7rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.gm-19__h {
  margin: 0;
  font-size: clamp(1.7rem,4vw,2.6rem);
  font-weight: 600;
  letter-spacing: -.035em;
  line-height: 1.06;
  text-wrap: balance;
}

.gm-19__search {
  position: relative;
  display: grid;
}

.gm-19__shell {
  display: grid;
  grid-template-columns: auto 1fr auto auto;
  align-items: center;
  gap: .6rem;
  min-block-size: 3.25rem;
  padding: .5rem .6rem .5rem .95rem;
  border-radius: 999px;
  background: rgba(255,255,255,.55);
  border: 1px solid var(--edge);
  -webkit-backdrop-filter: blur(22px) saturate(175%);
  backdrop-filter: blur(22px) saturate(175%);
  box-shadow: inset 0 1px 0 var(--rim), inset 0 2px 8px rgba(20,20,60,.1), 0 22px 48px -26px rgba(20,20,60,.45);
  transition: box-shadow .2s ease;
}

@supports (background: color-mix(in oklab, white 10%, transparent)) {
  .gm-19__shell {
    background: color-mix(in oklab, var(--tint) 58%, transparent);
  }
}

@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .gm-19__shell {
    background: rgba(255,255,255,.95);
  }
}

.gm-19__shell:focus-within {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
  box-shadow: inset 0 1px 0 var(--rim), 0 26px 54px -24px rgba(20,20,60,.5);
}

.gm-19__icon {
  display: grid;
  place-items: center;
  color: var(--muted);
}

.gm-19__icon svg {
  inline-size: 1.25rem;
  block-size: 1.25rem;
}

.gm-19__input {
  min-inline-size: 0;
  min-block-size: 2.4rem;
  padding: 0;
  border: 0;
  background: transparent;
  color: var(--ink);
  font: inherit;
  font-size: 1.02rem;
  letter-spacing: -.01em;
}

.gm-19__input::placeholder {
  color: var(--ink);
  opacity: .6;
}

.gm-19__input:focus {
  outline: none;
}

.gm-19__input::-webkit-search-cancel-button {
  -webkit-appearance: none;
  appearance: none;
}

.gm-19__clear {
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  border-radius: 999px;
  color: var(--muted);
  background: transparent;
  border: 1px solid transparent;
  transition: background .18s ease, color .18s ease;
}

.gm-19__clear svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
}

.gm-19__clear:hover {
  background: rgba(15,17,32,.06);
  color: var(--ink);
}

.gm-19__clear:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.gm-19__filter {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  min-block-size: 2.5rem;
  padding: .5rem .85rem;
  border-radius: 999px;
  cursor: pointer;
  font: inherit;
  font-size: .9rem;
  font-weight: 500;
  color: var(--ink);
  background: rgba(255,255,255,.7);
  border: 1px solid var(--edge);
  box-shadow: inset 0 1px 0 var(--rim);
  transition: translate .18s ease, background .18s ease;
}

.gm-19__filter svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
}

.gm-19__count {
  display: grid;
  place-items: center;
  min-inline-size: 1.25rem;
  block-size: 1.25rem;
  border-radius: 999px;
  font-family: var(--mono);
  font-size: .66rem;
  color: #fff;
  background: var(--accent);
}

.gm-19__filter:hover {
  translate: 0 -1px;
}

.gm-19__filter:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

@media (max-width: 34rem) {
  .gm-19__filter span:not(.gm-19__count) {
    display: none;
  }
}

.gm-19__panel {
  position: absolute;
  inset-inline: 0;
  inset-block-start: calc(100% + .6rem);
  z-index: 4;
  padding: 1rem;
  border-radius: 1.35rem;
  border: 1px solid var(--edge);
  background: rgba(255,255,255,.6);
  -webkit-backdrop-filter: blur(26px) saturate(180%);
  backdrop-filter: blur(26px) saturate(180%);
  box-shadow: inset 0 1px 0 var(--rim), 0 30px 66px -30px rgba(20,20,60,.5);
  display: grid;
  gap: .6rem;
  opacity: 0;
  translate: 0 -.4rem;
  pointer-events: none;
  transition: opacity .2s ease, translate .2s ease;
}

.gm-19__search:focus-within .gm-19__panel {
  opacity: 1;
  translate: 0 0;
  pointer-events: auto;
}

.gm-19__ptitle {
  margin: 0;
  font-family: var(--mono);
  font-size: .66rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.gm-19__list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: .25rem;
}

.gm-19__item {
  inline-size: 100%;
  display: grid;
  grid-template-columns: auto 1fr auto;
  align-items: center;
  gap: .7rem;
  min-block-size: 2.75rem;
  padding: .55rem .7rem;
  border-radius: .85rem;
  cursor: pointer;
  text-align: start;
  font: inherit;
  font-size: .94rem;
  color: var(--ink);
  background: transparent;
  border: 1px solid transparent;
  transition: background .16s ease;
}

.gm-19__item:hover {
  background: rgba(15,17,32,.06);
}

.gm-19__item:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.gm-19__ikind {
  padding: .16rem .42rem;
  border-radius: .4rem;
  font-family: var(--mono);
  font-size: .62rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
  background: rgba(15,17,32,.07);
  border: 1px solid var(--edge);
}

.gm-19__imeta {
  font-family: var(--mono);
  font-size: .68rem;
  color: var(--muted);
}

@media (max-width: 34rem) {
  .gm-19__imeta {
    display: none;
  }
}

.gm-19__phint {
  margin: 0;
  font-size: .78rem;
  color: var(--muted);
}

.gm-19__code {
  font-family: var(--mono);
  font-size: .74rem;
  padding: .1rem .32rem;
  border-radius: .3rem;
  background: rgba(15,17,32,.07);
  border: 1px solid var(--edge);
}

.gm-19__chips {
  display: flex;
  flex-wrap: wrap;
  gap: .45rem;
  justify-content: center;
}

.gm-19__chip {
  padding: .4rem .75rem;
  border-radius: 999px;
  font-size: .85rem;
  color: var(--ink);
  background: rgba(255,255,255,.5);
  border: 1px solid var(--edge);
  -webkit-backdrop-filter: blur(14px) saturate(170%);
  backdrop-filter: blur(14px) saturate(170%);
  box-shadow: inset 0 1px 0 var(--rim);
}
/* this demo is light-first — the toggle flips it to dark */

.gm-19[data-theme="dark"],
.gm-19:has(#gm-19-theme:checked) {
  --a1: rgba(251,146,60,.45);
  --a2: rgba(56,189,248,.5);
  --a3: rgba(168,85,247,.55);
  --a4: rgba(52,211,153,.4);
  --base: #06070f;
  --base2: #141134;
  --ink: #f9fafe;
  --muted: rgba(249,250,254,.68);
  --rim: rgba(255,255,255,.5);
  --rim2: rgba(255,255,255,.14);
  --edge: rgba(255,255,255,.2);
  --accent: #a5b4fc;
}

.gm-19:has(#gm-19-theme:checked) .gm-19__moon {
  display: none;
}

.gm-19:has(#gm-19-theme:checked) .gm-19__sun {
  display: block;
}

.gm-19[data-theme="dark"] .gm-19__shell,
.gm-19:has(#gm-19-theme:checked) .gm-19__shell {
  background: rgba(255,255,255,.14);
  box-shadow: inset 0 1px 0 var(--rim), inset 0 2px 8px rgba(0,0,0,.25), 0 26px 54px -26px rgba(0,0,0,.7);
}

.gm-19[data-theme="dark"] .gm-19__panel,
.gm-19:has(#gm-19-theme:checked) .gm-19__panel {
  background: rgba(255,255,255,.12);
  box-shadow: inset 0 1px 0 var(--rim), 0 30px 66px -30px rgba(0,0,0,.75);
}

.gm-19[data-theme="dark"] .gm-19__filter,
.gm-19[data-theme="dark"] .gm-19__chip,
.gm-19:has(#gm-19-theme:checked) .gm-19__filter,
.gm-19:has(#gm-19-theme:checked) .gm-19__chip {
  background: rgba(255,255,255,.14);
}

.gm-19[data-theme="dark"] .gm-19__theme,
.gm-19:has(#gm-19-theme:checked) .gm-19__theme {
  background: rgba(255,255,255,.14);
}

.gm-19[data-theme="dark"] .gm-19__ikind,
.gm-19[data-theme="dark"] .gm-19__code,
.gm-19:has(#gm-19-theme:checked) .gm-19__ikind,
.gm-19:has(#gm-19-theme:checked) .gm-19__code {
  background: rgba(255,255,255,.12);
}

.gm-19[data-theme="dark"] .gm-19__item:hover,
.gm-19[data-theme="dark"] .gm-19__clear:hover,
.gm-19:has(#gm-19-theme:checked) .gm-19__item:hover,
.gm-19:has(#gm-19-theme:checked) .gm-19__clear:hover {
  background: rgba(255,255,255,.14);
}

.gm-19[data-theme="dark"] .gm-19__count,
.gm-19:has(#gm-19-theme:checked) .gm-19__count {
  color: #14102c;
}

@media (prefers-reduced-motion: reduce) {
  .gm-19 *,
    .gm-19 *::before,
    .gm-19 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .gm-19__shell,
    .gm-19__panel,
    .gm-19__filter,
    .gm-19__chip,
    .gm-19__theme {
    border-color: CanvasText;
    box-shadow: none;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
    background: Canvas;
  }
}
```
