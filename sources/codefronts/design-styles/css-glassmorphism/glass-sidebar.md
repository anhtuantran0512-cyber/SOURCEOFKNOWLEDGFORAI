---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-glassmorphism/glass-sidebar/"
title: "Frosted Glass Sidebar Menu"
section: "design-styles"
category: "css-glassmorphism"
category_name: "CSS Glassmorphism"
description: "A 20px-blur sidebar pinned to the left of an app shell, with grouped nav sections, hairline dividers, hover states and a profile block at the bottom — while…"
has_js: "false"
---

Here's a working CSS Glassmorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Frosted Glass Sidebar Menu
Source: https://codefronts.com/design-styles/css-glassmorphism/glass-sidebar/

A 20px-blur sidebar pinned to the left of an app shell, with grouped nav sections, hairline dividers, hover states and a profile block at the bottom — while the content column scrolls behind its edge. The layout is one CSS grid; the glass is four declarations.
## HTML
```html
<div class="gm-16">
  <input class="gm-16__sr" type="checkbox" id="gm-16-theme">
  <label class="gm-16__theme" for="gm-16-theme" title="Switch theme">
    <svg class="gm-16__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="gm-16__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="gm-16__vh">Switch light or dark theme</span>
  </label>

  <div class="gm-16__shell">
    <nav class="gm-16__side" aria-label="Workspace">
      <a class="gm-16__brand" href="#gm-16-main">
        <span class="gm-16__mark" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none"><path d="M4 17.5 12 4l8 13.5H4Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg></span>
        <span class="gm-16__bname">Atlas<span class="gm-16__bsub">design system</span></span>
      </a>

      <p class="gm-16__group" id="gm-16-g1">Workspace</p>
      <ul class="gm-16__list" aria-labelledby="gm-16-g1">
        <li><a class="gm-16__link" href="#gm-16-main" aria-current="page"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><rect x="4" y="4" width="7" height="7" rx="1.8" stroke="currentColor" stroke-width="1.7"/><rect x="13" y="4" width="7" height="7" rx="1.8" stroke="currentColor" stroke-width="1.7"/><rect x="4" y="13" width="7" height="7" rx="1.8" stroke="currentColor" stroke-width="1.7"/><rect x="13" y="13" width="7" height="7" rx="1.8" stroke="currentColor" stroke-width="1.7"/></svg>Overview</a></li>
        <li><a class="gm-16__link" href="#gm-16-main"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4 18V9m5 9V5m5 13v-6m5 6V8" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>Usage</a></li>
        <li><a class="gm-16__link" href="#gm-16-main"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" stroke="currentColor" stroke-width="1.7"/><path d="M12 8v4l3 2" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>Activity</a></li>
      </ul>

      <p class="gm-16__group" id="gm-16-g2">Library</p>
      <ul class="gm-16__list" aria-labelledby="gm-16-g2">
        <li><a class="gm-16__link" href="#gm-16-main"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M5 6.5h14M5 12h14M5 17.5h9" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>Tokens</a></li>
        <li><a class="gm-16__link" href="#gm-16-main"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><rect x="4.5" y="5" width="15" height="14" rx="2.5" stroke="currentColor" stroke-width="1.7"/><path d="M4.5 10h15" stroke="currentColor" stroke-width="1.7"/></svg>Components</a></li>
        <li><a class="gm-16__link" href="#gm-16-main"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 4.5l7 4v7l-7 4-7-4v-7l7-4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>Materials</a></li>
      </ul>

      <div class="gm-16__profile">
        <img class="gm-16__avatar" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=128&h=128&q=80" width="64" height="64" loading="lazy" decoding="async" alt="Portrait of Priya Sharma">
        <span class="gm-16__pmeta"><span class="gm-16__pname">Priya Sharma</span><span class="gm-16__prole">Owner · Atlas</span></span>
        <button class="gm-16__more" type="button" aria-label="Open account menu">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="6" r="1.5" fill="currentColor"/><circle cx="12" cy="12" r="1.5" fill="currentColor"/><circle cx="12" cy="18" r="1.5" fill="currentColor"/></svg>
        </button>
      </div>
    </nav>

    <main class="gm-16__main" id="gm-16-main">
      <header class="gm-16__mhead">
        <p class="gm-16__eyebrow">Materials · glass</p>
        <h1 class="gm-16__h">Surface library</h1>
        <p class="gm-16__lead">Scroll this column. The sidebar edge stays put and keeps sampling whatever passes behind it — that live sample is the entire reason to blur a shell panel instead of tinting it.</p>
      </header>
      <ul class="gm-16__cards">
        <li class="gm-16__card"><h2 class="gm-16__ctitle">Chrome / 12px</h2><p class="gm-16__ccopy">Toolbars and sticky headers. Cheapest surface in the set.</p></li>
        <li class="gm-16__card"><h2 class="gm-16__ctitle">Sheet / 24px</h2><p class="gm-16__ccopy">Modals and inline panels holding long-form copy.</p></li>
        <li class="gm-16__card"><h2 class="gm-16__ctitle">Shell / 20px</h2><p class="gm-16__ccopy">Sidebars and rails. One large layer, always on screen.</p></li>
        <li class="gm-16__card"><h2 class="gm-16__ctitle">Privacy / 40px</h2><p class="gm-16__ccopy">Auth and lock states where the backdrop must be unreadable.</p></li>
        <li class="gm-16__card"><h2 class="gm-16__ctitle">Rim / inset pair</h2><p class="gm-16__ccopy">Bright top, dim bottom. The bevel that sells the thickness.</p></li>
        <li class="gm-16__card"><h2 class="gm-16__ctitle">Grain / 8%</h2><p class="gm-16__ccopy">Fine turbulence over the film so frost reads as etched, not plastic.</p></li>
      </ul>
    </main>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

.gm-16 {
  --a1: rgba(45,212,191,.5);
  --a2: rgba(129,140,248,.6);
  --a3: rgba(244,114,182,.45);
  --a4: rgba(250,204,21,.35);
  --base: #05070f;
  --base2: #101832;
  --ink: #f9fbfe;
  --muted: rgba(249,251,254,.68);
  --tint: #ffffff;
  --accent: #5eead4;
  --rim: rgba(255,255,255,.45);
  --rim2: rgba(255,255,255,.14);
  --edge: rgba(255,255,255,.16);
  --mono: 'Geist Mono',ui-monospace,'SFMono-Regular',Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  color: var(--ink);
  isolation: isolate;
  font-family: 'Geist',ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif;
  background: radial-gradient(48% 40% at 8% 14%, var(--a1) 0%, transparent 58%), radial-gradient(54% 46% at 88% 18%, var(--a2) 0%, transparent 62%), radial-gradient(48% 42% at 76% 88%, var(--a3) 0%, transparent 58%), radial-gradient(42% 36% at 22% 92%, var(--a4) 0%, transparent 58%), linear-gradient(162deg, var(--base) 0%, var(--base2) 52%, var(--base) 100%);
}

.gm-16 *,
.gm-16 *::before,
.gm-16 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 300)) {
  .gm-16 {
    --a1: oklch(0.82 0.15 178 / .52);
    --a2: oklch(0.68 0.19 280 / .62);
    --a3: oklch(0.74 0.19 5 / .46);
    --a4: oklch(0.88 0.16 95 / .36);
    --base: oklch(0.13 0.025 268);
    --base2: oklch(0.22 0.08 268);
    --accent: oklch(0.86 0.13 175);
  }
}

.gm-16__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.gm-16__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.gm-16__theme {
  position: fixed;
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

.gm-16__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: inherit;
}

.gm-16__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.gm-16__theme:hover {
  scale: 1.06;
}

.gm-16__sr:focus-visible + .gm-16__theme {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.gm-16__moon {
  display: none;
}

.gm-16__shell {
  display: grid;
  grid-template-columns: 17rem 1fr;
  align-items: start;
  min-block-size: 100vh;
}

@media (max-width: 52rem) {
  .gm-16__shell {
    grid-template-columns: 1fr;
  }
}

.gm-16__side {
  position: sticky;
  inset-block-start: 0;
  block-size: 100vh;
  block-size: 100svh;
  display: flex;
  flex-direction: column;
  gap: .35rem;
  padding: 1.1rem .85rem;
  background: rgba(255,255,255,.13);
  border-inline-end: 1px solid var(--rim2);
  box-shadow: inset 1px 0 0 rgba(255,255,255,.32);
}

@supports (background: color-mix(in oklab, white 10%, transparent)) {
  .gm-16__side {
    background: color-mix(in oklab, var(--tint) 13%, transparent);
  }
}

@supports ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .gm-16__side {
    -webkit-backdrop-filter: blur(20px) saturate(170%);
    backdrop-filter: blur(20px) saturate(170%);
  }
}

@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .gm-16__side {
    background: rgba(14,16,40,.92);
  }
}

@media (max-width: 52rem) {
  .gm-16__side {
    position: static;
    block-size: auto;
  }
}

.gm-16__brand {
  display: flex;
  align-items: center;
  gap: .6rem;
  min-block-size: 2.75rem;
  padding: .4rem .5rem;
  border-radius: .8rem;
  color: var(--ink);
  text-decoration: none;
}

.gm-16__mark {
  display: grid;
  place-items: center;
  inline-size: 2rem;
  block-size: 2rem;
  border-radius: .6rem;
  background: rgba(255,255,255,.18);
  border: 1px solid var(--edge);
  box-shadow: inset 0 1px 0 var(--rim2);
}

.gm-16__mark svg {
  inline-size: 1.1rem;
  block-size: 1.1rem;
}

.gm-16__bname {
  display: grid;
  font-size: 1rem;
  font-weight: 600;
  letter-spacing: -.01em;
  line-height: 1.1;
}

.gm-16__bsub {
  font-family: var(--mono);
  font-size: .6rem;
  font-weight: 400;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.gm-16__group {
  margin: 1.1rem 0 .35rem;
  padding: .9rem .55rem 0;
  border-block-start: 1px solid var(--rim2);
  font-family: var(--mono);
  font-size: .62rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.gm-16__list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: .15rem;
}

.gm-16__link {
  display: flex;
  align-items: center;
  gap: .65rem;
  min-block-size: 2.75rem;
  padding: .55rem .6rem;
  border-radius: .75rem;
  font-size: .94rem;
  font-weight: 500;
  color: var(--muted);
  text-decoration: none;
  transition: background .18s ease, color .18s ease;
}

.gm-16__link svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
  flex: none;
}

.gm-16__link:hover {
  background: rgba(255,255,255,.1);
  color: var(--ink);
}

.gm-16__link[aria-current="page"] {
  background: rgba(255,255,255,.18);
  color: var(--ink);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.45);
}

.gm-16__link:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.gm-16__profile {
  margin-block-start: auto;
  display: flex;
  align-items: center;
  gap: .65rem;
  padding: .6rem;
  border-radius: 1rem;
  border: 1px solid var(--edge);
  background: rgba(255,255,255,.1);
  box-shadow: inset 0 1px 0 var(--rim2);
}

.gm-16__avatar {
  inline-size: 2.4rem;
  block-size: 2.4rem;
  border-radius: 999px;
  object-fit: cover;
  flex: none;
  background: rgba(255,255,255,.12);
  border: 1px solid var(--edge);
}

.gm-16__pmeta {
  display: grid;
  gap: .05rem;
  min-inline-size: 0;
}

.gm-16__pname {
  font-size: .9rem;
  font-weight: 500;
  letter-spacing: -.01em;
}

.gm-16__prole {
  font-family: var(--mono);
  font-size: .62rem;
  letter-spacing: .06em;
  color: var(--muted);
}

.gm-16__more {
  margin-inline-start: auto;
  inline-size: 2.25rem;
  block-size: 2.25rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  border-radius: .6rem;
  color: var(--ink);
  background: transparent;
  border: 1px solid transparent;
  transition: background .18s ease;
}

.gm-16__more svg {
  inline-size: 1.1rem;
  block-size: 1.1rem;
}

.gm-16__more:hover {
  background: rgba(255,255,255,.14);
}

.gm-16__more:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.gm-16__main {
  padding: clamp(1.5rem,4vw,3rem) clamp(1.25rem,3.5vw,2.75rem) 4rem;
  display: grid;
  gap: clamp(1.25rem,3vw,2rem);
  align-content: start;
}

.gm-16__mhead {
  display: grid;
  gap: .5rem;
  max-inline-size: 44rem;
}

.gm-16__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .68rem;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: var(--muted);
}

.gm-16__h {
  margin: 0;
  font-size: clamp(1.8rem,4.4vw,2.8rem);
  font-weight: 600;
  letter-spacing: -.035em;
  line-height: 1.05;
}

.gm-16__lead {
  margin: 0;
  font-size: clamp(.98rem,1.5vw,1.1rem);
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

.gm-16__cards {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: clamp(.85rem,1.6vw,1.25rem);
  grid-template-columns: repeat(auto-fit,minmax(14rem,1fr));
}

.gm-16__card {
  display: grid;
  gap: .35rem;
  padding: clamp(1rem,1.8vw,1.35rem);
  border-radius: 1.2rem;
  background: rgba(255,255,255,.1);
  border: 1px solid var(--edge);
  -webkit-backdrop-filter: blur(18px) saturate(165%);
  backdrop-filter: blur(18px) saturate(165%);
  box-shadow: inset 0 1px 0 var(--rim), inset 0 -1px 0 var(--rim2), 0 24px 52px -28px rgba(0,0,0,.6);
  transition: translate .22s cubic-bezier(.2,.7,.3,1);
}

.gm-16__card:hover {
  translate: 0 -3px;
}

.gm-16__ctitle {
  margin: 0;
  font-family: var(--mono);
  font-size: .82rem;
  letter-spacing: .04em;
  font-weight: 500;
}

.gm-16__ccopy {
  margin: 0;
  font-size: .9rem;
  line-height: 1.5;
  color: var(--muted);
  text-wrap: pretty;
}

.gm-16[data-theme="light"],
.gm-16:has(#gm-16-theme:checked) {
  --a1: rgba(153,246,228,.5);
  --a2: rgba(165,180,252,.6);
  --a3: rgba(249,168,212,.5);
  --a4: rgba(254,240,138,.5);
  --base: #eff3fa;
  --base2: #e1e8fb;
  --ink: #0e1220;
  --muted: rgba(14,18,32,.68);
  --rim: rgba(255,255,255,.9);
  --rim2: rgba(255,255,255,.5);
  --edge: rgba(14,18,32,.12);
  --accent: #0d9488;
}

.gm-16:has(#gm-16-theme:checked) .gm-16__sun {
  display: none;
}

.gm-16:has(#gm-16-theme:checked) .gm-16__moon {
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .gm-16 *,
    .gm-16 *::before,
    .gm-16 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .gm-16__side,
    .gm-16__card,
    .gm-16__profile,
    .gm-16__theme {
    border-color: CanvasText;
    box-shadow: none;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
    background: Canvas;
  }

  .gm-16__link[aria-current="page"] {
    background: Highlight;
    color: HighlightText;
  }
}
```
