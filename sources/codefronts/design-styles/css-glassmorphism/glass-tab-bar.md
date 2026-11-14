---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-glassmorphism/glass-tab-bar/"
title: "Glassmorphism Bottom Tab Bar"
section: "design-styles"
category: "css-glassmorphism"
category_name: "CSS Glassmorphism"
description: "An iOS 26 / visionOS-style floating tab bar: a rounded pill of frosted glass hovering above scrolling content, with the active tab carrying an accent tint…"
has_js: "false"
---

Here's a working CSS Glassmorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Bottom Tab Bar
Source: https://codefronts.com/design-styles/css-glassmorphism/glass-tab-bar/

An iOS 26 / visionOS-style floating tab bar: a rounded pill of frosted glass hovering above scrolling content, with the active tab carrying an accent tint and a visible label while the others stay muted icons. Tab state is a radio group — fully interactive, zero JavaScript.
## HTML
```html
<div class="gm-15">
  <input class="gm-15__sr" type="checkbox" id="gm-15-theme">
  <label class="gm-15__theme" for="gm-15-theme" title="Switch theme">
    <svg class="gm-15__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="gm-15__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="gm-15__vh">Switch light or dark theme</span>
  </label>

  <div class="gm-15__stage">
    <div class="gm-15__phone">
      <div class="gm-15__scroll">
        <header class="gm-15__top">
          <p class="gm-15__eyebrow">Now playing</p>
          <h2 class="gm-15__h">Ambient Sessions</h2>
        </header>
        <ul class="gm-15__rows">
          <li class="gm-15__row"><span class="gm-15__art" aria-hidden="true"></span><span class="gm-15__rmeta"><span class="gm-15__rtitle">Low Orbit</span><span class="gm-15__rsub">Priya Sharma · 4:12</span></span></li>
          <li class="gm-15__row"><span class="gm-15__art" aria-hidden="true"></span><span class="gm-15__rmeta"><span class="gm-15__rtitle">Glass Rain</span><span class="gm-15__rsub">Sam Rivera · 3:48</span></span></li>
          <li class="gm-15__row"><span class="gm-15__art" aria-hidden="true"></span><span class="gm-15__rmeta"><span class="gm-15__rtitle">Refraction</span><span class="gm-15__rsub">Alex Chen · 5:06</span></span></li>
          <li class="gm-15__row"><span class="gm-15__art" aria-hidden="true"></span><span class="gm-15__rmeta"><span class="gm-15__rtitle">Depth Field</span><span class="gm-15__rsub">Jordan Lee · 2:57</span></span></li>
          <li class="gm-15__row"><span class="gm-15__art" aria-hidden="true"></span><span class="gm-15__rmeta"><span class="gm-15__rtitle">Sandblast</span><span class="gm-15__rsub">Priya Sharma · 6:20</span></span></li>
          <li class="gm-15__row"><span class="gm-15__art" aria-hidden="true"></span><span class="gm-15__rmeta"><span class="gm-15__rtitle">Turbulence</span><span class="gm-15__rsub">Sam Rivera · 3:31</span></span></li>
          <li class="gm-15__row"><span class="gm-15__art" aria-hidden="true"></span><span class="gm-15__rmeta"><span class="gm-15__rtitle">Specular</span><span class="gm-15__rsub">Alex Chen · 4:44</span></span></li>
        </ul>

        <nav class="gm-15__tabs" aria-label="Sections">
          <input class="gm-15__radio gm-15__sr" type="radio" name="gm-15-tab" id="gm-15-t1" checked>
          <label class="gm-15__tab" for="gm-15-t1">
            <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4 11.2 12 4.5l8 6.7V19a1 1 0 0 1-1 1h-4v-5h-6v5H5a1 1 0 0 1-1-1v-7.8Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
            <span class="gm-15__label">Home</span>
          </label>

          <input class="gm-15__radio gm-15__sr" type="radio" name="gm-15-tab" id="gm-15-t2">
          <label class="gm-15__tab" for="gm-15-t2">
            <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.4" stroke="currentColor" stroke-width="1.7"/><path d="m16 16 4 4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
            <span class="gm-15__label">Search</span>
          </label>

          <input class="gm-15__radio gm-15__sr" type="radio" name="gm-15-tab" id="gm-15-t3">
          <label class="gm-15__tab" for="gm-15-t3">
            <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M9 18V6.8l9-1.6V16" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><circle cx="7" cy="18" r="2.2" stroke="currentColor" stroke-width="1.7"/><circle cx="16" cy="16" r="2.2" stroke="currentColor" stroke-width="1.7"/></svg>
            <span class="gm-15__label">Library</span>
          </label>

          <input class="gm-15__radio gm-15__sr" type="radio" name="gm-15-tab" id="gm-15-t4">
          <label class="gm-15__tab" for="gm-15-t4">
            <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="8.5" r="3.6" stroke="currentColor" stroke-width="1.7"/><path d="M5 19.5c1.4-3.2 4-4.6 7-4.6s5.6 1.4 7 4.6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
            <span class="gm-15__label">You</span>
          </label>
        </nav>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

.gm-15 {
  --a1: rgba(236,72,153,.55);
  --a2: rgba(99,102,241,.6);
  --a3: rgba(45,212,191,.45);
  --a4: rgba(251,146,60,.4);
  --base: #06060f;
  --base2: #180f31;
  --ink: #fafaff;
  --muted: rgba(250,250,255,.66);
  --tint: #ffffff;
  --accent: #f0abfc;
  --rim: rgba(255,255,255,.55);
  --rim2: rgba(255,255,255,.14);
  --edge: rgba(255,255,255,.18);
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
  background: radial-gradient(50% 42% at 12% 16%, var(--a1) 0%, transparent 60%), radial-gradient(54% 46% at 86% 14%, var(--a2) 0%, transparent 62%), radial-gradient(46% 40% at 80% 88%, var(--a3) 0%, transparent 58%), radial-gradient(44% 38% at 14% 90%, var(--a4) 0%, transparent 58%), linear-gradient(158deg, var(--base) 0%, var(--base2) 52%, var(--base) 100%);
}

.gm-15 *,
.gm-15 *::before,
.gm-15 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 300)) {
  .gm-15 {
    --a1: oklch(0.7 0.24 350 / .56);
    --a2: oklch(0.62 0.22 275 / .62);
    --a3: oklch(0.82 0.15 178 / .46);
    --a4: oklch(0.78 0.17 55 / .42);
    --base: oklch(0.13 0.025 285);
    --base2: oklch(0.24 0.1 300);
    --accent: oklch(0.84 0.13 320);
  }
}

.gm-15__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.gm-15__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.gm-15__theme {
  position: absolute;
  inset-block-start: 1.15rem;
  inset-inline-end: 1.15rem;
  z-index: 9;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  border-radius: 999px;
  color: var(--ink);
  background: rgba(255,255,255,.14);
  border: 1px solid var(--edge);
  -webkit-backdrop-filter: blur(10px) saturate(160%);
  backdrop-filter: blur(10px) saturate(160%);
  box-shadow: inset 0 1px 0 var(--rim), 0 10px 24px -14px rgba(0,0,0,.7);
  transition: scale .18s ease;
}

.gm-15__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: inherit;
}

.gm-15__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.gm-15__theme:hover {
  scale: 1.06;
}

.gm-15__sr:focus-visible + .gm-15__theme {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.gm-15__moon {
  display: none;
}

.gm-15__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,4vw,3rem);
}

.gm-15__phone {
  inline-size: min(26rem,100%);
  block-size: min(40rem,80vh);
  position: relative;
  border-radius: 2.25rem;
  overflow: hidden;
  border: 1px solid var(--edge);
  background: rgba(255,255,255,.05);
  box-shadow: inset 0 1px 0 var(--rim2), 0 40px 90px -36px rgba(0,0,0,.75);
}

.gm-15__scroll {
  block-size: 100%;
  overflow-y: auto;
  overscroll-behavior: contain;
  scrollbar-width: none;
  padding-block-end: 1rem;
}

.gm-15__scroll::-webkit-scrollbar {
  width: 0;
}

.gm-15__top {
  padding: clamp(1.25rem,4vw,1.75rem) 1.25rem .75rem;
  display: grid;
  gap: .25rem;
}

.gm-15__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .66rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--muted);
}

.gm-15__h {
  margin: 0;
  font-size: clamp(1.5rem,4.5vw,2rem);
  font-weight: 600;
  letter-spacing: -.03em;
}

.gm-15__rows {
  list-style: none;
  margin: 0;
  padding: .5rem .9rem 1rem;
  display: grid;
  gap: .6rem;
}

.gm-15__row {
  display: flex;
  align-items: center;
  gap: .85rem;
  padding: .7rem .85rem;
  border-radius: 1.05rem;
  background: rgba(255,255,255,.1);
  border: 1px solid var(--edge);
  -webkit-backdrop-filter: blur(16px) saturate(160%);
  backdrop-filter: blur(16px) saturate(160%);
  box-shadow: inset 0 1px 0 var(--rim2);
}

.gm-15__art {
  inline-size: 2.75rem;
  block-size: 2.75rem;
  flex: none;
  border-radius: .75rem;
  background: linear-gradient(140deg, rgba(255,255,255,.35), rgba(255,255,255,.08));
  border: 1px solid var(--edge);
}

.gm-15__rmeta {
  display: grid;
  gap: .1rem;
  min-inline-size: 0;
}

.gm-15__rtitle {
  font-size: .95rem;
  font-weight: 500;
  letter-spacing: -.01em;
}

.gm-15__rsub {
  font-family: var(--mono);
  font-size: .66rem;
  letter-spacing: .04em;
  color: var(--muted);
}

.gm-15__tabs {
  position: sticky;
  inset-block-end: .85rem;
  z-index: 3;
  inline-size: min(22rem,calc(100% - 1.8rem));
  margin: .5rem auto 0;
  display: flex;
  align-items: center;
  gap: .2rem;
  padding: .35rem;
  padding-block-end: max(.35rem, env(safe-area-inset-bottom));
  border-radius: 999px;
  background: rgba(255,255,255,.16);
  border: 1px solid var(--edge);
  box-shadow: inset 0 1px 0 var(--rim), inset 0 -1px 0 var(--rim2), 0 22px 46px -22px rgba(0,0,0,.72);
}

@supports (background: color-mix(in oklab, white 10%, transparent)) {
  .gm-15__tabs {
    background: color-mix(in oklab, var(--tint) 16%, transparent);
  }
}

@supports ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .gm-15__tabs {
    -webkit-backdrop-filter: blur(26px) saturate(185%);
    backdrop-filter: blur(26px) saturate(185%);
  }
}

@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .gm-15__tabs,
    .gm-15__row {
    background: rgba(20,14,44,.92);
  }
}

.gm-15__tab {
  flex: 1;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: .4rem;
  min-block-size: 2.75rem;
  padding: .5rem .55rem;
  border-radius: 999px;
  cursor: pointer;
  color: var(--muted);
  font-size: .82rem;
  font-weight: 500;
  transition: background .2s ease, color .2s ease;
}

.gm-15__tab svg {
  inline-size: 1.3rem;
  block-size: 1.3rem;
  flex: none;
}

.gm-15__label {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.gm-15__radio:checked + .gm-15__tab {
  color: var(--ink);
  background: rgba(240,171,252,.32);
  box-shadow: inset 0 1px 0 var(--rim);
}

@supports (background: color-mix(in oklab, red 10%, transparent)) {
  .gm-15__radio:checked + .gm-15__tab {
    background: color-mix(in oklab, var(--accent) 32%, transparent);
  }
}

.gm-15__radio:checked + .gm-15__tab .gm-15__label {
  position: static;
  inline-size: auto;
  block-size: auto;
  margin: 0;
  clip-path: none;
  overflow: visible;
}

.gm-15__radio:focus-visible + .gm-15__tab {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.gm-15__tab:hover {
  color: var(--ink);
}

.gm-15[data-theme="light"],
.gm-15:has(#gm-15-theme:checked) {
  --a1: rgba(249,168,212,.55);
  --a2: rgba(165,180,252,.6);
  --a3: rgba(153,246,228,.5);
  --a4: rgba(253,186,116,.45);
  --base: #f2f2fb;
  --base2: #e6e2fb;
  --ink: #101020;
  --muted: rgba(16,16,32,.66);
  --rim: rgba(255,255,255,.95);
  --rim2: rgba(255,255,255,.5);
  --edge: rgba(16,16,32,.12);
  --accent: #c026d3;
}

.gm-15:has(#gm-15-theme:checked) .gm-15__sun {
  display: none;
}

.gm-15:has(#gm-15-theme:checked) .gm-15__moon {
  display: block;
}

.gm-15[data-theme="light"] .gm-15__radio:checked + .gm-15__tab,
.gm-15:has(#gm-15-theme:checked) .gm-15__radio:checked + .gm-15__tab {
  color: #fff;
}

@media (prefers-reduced-motion: reduce) {
  .gm-15 *,
    .gm-15 *::before,
    .gm-15 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .gm-15__tabs,
    .gm-15__row,
    .gm-15__phone,
    .gm-15__theme {
    border-color: CanvasText;
    box-shadow: none;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
    background: Canvas;
  }

  .gm-15__radio:checked + .gm-15__tab {
    background: Highlight;
    color: HighlightText;
  }
}
```
