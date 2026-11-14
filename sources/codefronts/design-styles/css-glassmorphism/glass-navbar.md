---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-glassmorphism/glass-navbar/"
title: "Sticky Glass Navigation Bar"
section: "design-styles"
category: "css-glassmorphism"
category_name: "CSS Glassmorphism"
description: "The classic sticky glass header: position: sticky; top: 0 with 18px blur and 170% saturate, over content that scrolls beneath it."
has_js: "false"
---

Here's a working CSS Glassmorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sticky Glass Navigation Bar
Source: https://codefronts.com/design-styles/css-glassmorphism/glass-navbar/

The classic sticky glass header: position: sticky; top: 0 with 18px blur and 170% saturate, over content that scrolls beneath it. Scroll the panel and watch text pass under the bar — this is the one place where blur cost is always worth paying, because the surface is small and always in view.
## HTML
```html
<div class="gm-14">
  <input class="gm-14__sr" type="checkbox" id="gm-14-theme">
  <label class="gm-14__theme" for="gm-14-theme" title="Switch theme">
    <svg class="gm-14__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="gm-14__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="gm-14__vh">Switch light or dark theme</span>
  </label>

  <div class="gm-14__scroll">
    <nav class="gm-14__bar" aria-label="Primary">
      <a class="gm-14__logo" href="#gm-14-top">
        <span class="gm-14__mark" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none"><path d="M4 17.5 12 4l8 13.5H4Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg></span>
        Atlas
      </a>
      <ul class="gm-14__links">
        <li><a class="gm-14__link" href="#gm-14-top" aria-current="page">Product</a></li>
        <li><a class="gm-14__link" href="#gm-14-docs">Docs</a></li>
        <li><a class="gm-14__link" href="#gm-14-changelog">Changelog</a></li>
        <li><a class="gm-14__link" href="#gm-14-pricing">Pricing</a></li>
      </ul>
      <div class="gm-14__auth">
        <a class="gm-14__ghost" href="#gm-14-top">Sign in</a>
        <a class="gm-14__cta" href="#gm-14-top">Start free</a>
      </div>
    </nav>

    <main class="gm-14__content" id="gm-14-top">
      <h1 class="gm-14__h">Glass reads best when something moves behind it</h1>
      <p class="gm-14__lead">Scroll this panel. The bar above stays put, the type passes underneath, and the blur samples whatever happens to be there — that is the whole reason a sticky header earns its compositor layer.</p>
      <h2 class="gm-14__h2" id="gm-14-docs">Why sticky, not fixed</h2>
      <p class="gm-14__p">A fixed header leaves the document flow and needs a spacer; a sticky header keeps its box in the flow until it reaches the offset, which means no layout hacks and no double-scrollbar surprises on iOS.</p>
      <p class="gm-14__p">Sticky also inherits the scroll container's clipping, so a header inside a modal or a panel behaves exactly like a header on the page. The catch is that any ancestor with overflow hidden breaks it silently.</p>
      <h2 class="gm-14__h2" id="gm-14-changelog">Tuning the film</h2>
      <p class="gm-14__p">Twelve percent white over a colourful gradient keeps nav labels comfortably above 4.5:1. Over photography, raise it — small text over unpredictable imagery is where glass headers fail accessibility review.</p>
      <div class="gm-14__band"><span></span><span></span><span></span><span></span></div>
      <h2 class="gm-14__h2" id="gm-14-pricing">Cost, honestly</h2>
      <p class="gm-14__p">One thin blurred surface that is always on screen is the cheapest possible place to spend a compositor layer. Six blurred cards in a list is the expensive place — see the containment demo for what that costs and how to contain it.</p>
      <p class="gm-14__p">Everything else here is ordinary layout: a flex row, a hairline border, and an underline drawn with a scaled pseudo-element so hover never triggers layout.</p>
    </main>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

.gm-14 {
  --a1: rgba(125,211,252,.5);
  --a2: rgba(216,180,254,.55);
  --a3: rgba(254,240,138,.5);
  --a4: rgba(153,246,228,.5);
  --base: #f0f3fb;
  --base2: #e2e8fc;
  --ink: #0f1120;
  --muted: rgba(15,17,32,.68);
  --tint: #ffffff;
  --accent: #0ea5e9;
  --rim: rgba(255,255,255,.95);
  --rim2: rgba(255,255,255,.5);
  --edge: rgba(15,17,32,.12);
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
  background: radial-gradient(52% 40% at 14% 10%, var(--a1) 0%, transparent 60%), radial-gradient(54% 44% at 88% 22%, var(--a2) 0%, transparent 62%), radial-gradient(44% 36% at 74% 84%, var(--a3) 0%, transparent 58%), radial-gradient(48% 40% at 16% 88%, var(--a4) 0%, transparent 60%), linear-gradient(164deg, var(--base) 0%, var(--base2) 52%, var(--base) 100%);
}

.gm-14 *,
.gm-14 *::before,
.gm-14 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 300)) {
  .gm-14 {
    --a1: oklch(0.78 0.16 220 / .52);
    --a2: oklch(0.68 0.24 305 / .56);
    --a3: oklch(0.88 0.16 95 / .36);
    --a4: oklch(0.82 0.15 178 / .46);
    --base: oklch(0.97 0.008 275);
    --base2: oklch(0.93 0.015 285);
    --accent: oklch(0.85 0.11 220);
  }
}

.gm-14__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.gm-14__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.gm-14__theme {
  position: absolute;
  inset-block-start: 4.6rem;
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

.gm-14__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: inherit;
}

.gm-14__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.gm-14__theme:hover {
  scale: 1.06;
}

.gm-14__sr:focus-visible + .gm-14__theme {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.gm-14__moon {
  display: none;
}

.gm-14__scroll {
  block-size: 100vh;
  block-size: 100svh;
  overflow-y: auto;
  overscroll-behavior: contain;
  scrollbar-width: thin;
}

.gm-14__bar {
  position: sticky;
  inset-block-start: 0;
  z-index: 5;
  display: flex;
  align-items: center;
  gap: clamp(.8rem,2vw,2rem);
  padding: .75rem clamp(1rem,3vw,2.25rem);
  background: rgba(255,255,255,.12);
  border-block-end: 1px solid var(--rim2);
  box-shadow: inset 0 1px 0 var(--rim);
}

@supports (background: color-mix(in oklab, white 10%, transparent)) {
  .gm-14__bar {
    background: color-mix(in oklab, var(--tint) 12%, transparent);
  }
}

@supports ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .gm-14__bar {
    -webkit-backdrop-filter: blur(18px) saturate(170%);
    backdrop-filter: blur(18px) saturate(170%);
  }
}

@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .gm-14__bar {
    background: rgba(14,14,40,.92);
  }
}

.gm-14__logo {
  display: inline-flex;
  align-items: center;
  gap: .5rem;
  min-block-size: 2.75rem;
  padding-inline-end: .4rem;
  font-size: 1.02rem;
  font-weight: 600;
  letter-spacing: -.01em;
  color: var(--ink);
  text-decoration: none;
}

.gm-14__mark {
  display: grid;
  place-items: center;
  inline-size: 1.9rem;
  block-size: 1.9rem;
  border-radius: .6rem;
  background: rgba(255,255,255,.18);
  border: 1px solid var(--edge);
  box-shadow: inset 0 1px 0 var(--rim2);
}

.gm-14__mark svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
}

.gm-14__links {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  align-items: center;
  gap: clamp(.2rem,1vw,.6rem);
}

.gm-14__link {
  position: relative;
  display: inline-flex;
  align-items: center;
  min-block-size: 2.75rem;
  padding: .5rem .7rem;
  border-radius: .6rem;
  font-size: .94rem;
  font-weight: 500;
  color: var(--muted);
  text-decoration: none;
  transition: color .18s ease, background .18s ease;
}

.gm-14__link::after {
  content: '';
  position: absolute;
  inset-inline: .7rem;
  inset-block-end: .45rem;
  block-size: 2px;
  border-radius: 2px;
  background: var(--accent);
  scale: 0 1;
  transform-origin: left;
  transition: scale .2s ease;
}

.gm-14__link:hover {
  color: var(--ink);
}

.gm-14__link:hover::after {
  scale: 1 1;
}

.gm-14__link[aria-current="page"] {
  color: var(--ink);
}

.gm-14__link[aria-current="page"]::after {
  scale: 1 1;
}

.gm-14__link:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.gm-14__auth {
  margin-inline-start: auto;
  display: flex;
  align-items: center;
  gap: .5rem;
}

.gm-14__ghost,
.gm-14__cta {
  display: inline-flex;
  align-items: center;
  min-block-size: 2.75rem;
  padding: .55rem 1rem;
  border-radius: .8rem;
  font-size: .92rem;
  font-weight: 500;
  text-decoration: none;
  transition: translate .18s ease, background .18s ease;
}

.gm-14__ghost {
  color: var(--ink);
  background: rgba(255,255,255,.1);
  border: 1px solid var(--edge);
}

.gm-14__cta {
  color: #08131c;
  background: var(--accent);
  border: 1px solid transparent;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.5), 0 12px 26px -16px rgba(0,0,0,.7);
}

.gm-14__ghost:hover,
.gm-14__cta:hover {
  translate: 0 -2px;
}

.gm-14__ghost:focus-visible,
.gm-14__cta:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

@media (max-width: 46rem) {
  .gm-14__links {
    display: none;
  }
}

.gm-14__content {
  max-inline-size: min(52rem,100%);
  margin: 0 auto;
  padding: clamp(2rem,6vw,4.5rem) clamp(1.25rem,3vw,2.25rem) 6rem;
  display: grid;
  gap: 1rem;
}

.gm-14__h {
  margin: 0;
  font-size: clamp(1.9rem,5vw,3.2rem);
  font-weight: 600;
  letter-spacing: -.035em;
  line-height: 1.04;
  text-wrap: balance;
}

.gm-14__lead {
  margin: 0;
  font-size: clamp(1rem,1.6vw,1.15rem);
  line-height: 1.65;
  color: var(--ink);
  opacity: .85;
  text-wrap: pretty;
}

.gm-14__h2 {
  margin: 1.4rem 0 0;
  font-size: clamp(1.15rem,2.2vw,1.45rem);
  font-weight: 600;
  letter-spacing: -.02em;
  scroll-margin-block-start: 5rem;
}

.gm-14__p {
  margin: 0;
  font-size: 1rem;
  line-height: 1.7;
  color: var(--muted);
  text-wrap: pretty;
}

.gm-14__band {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(6rem,1fr));
  gap: .8rem;
  margin: .6rem 0;
}

.gm-14__band span {
  block-size: 5rem;
  border-radius: 1rem;
  background: rgba(255,255,255,.1);
  border: 1px solid var(--edge);
  box-shadow: inset 0 1px 0 var(--rim2);
}

.gm-14[data-theme="light"],
.gm-14:has(#gm-14-theme:checked) {
  --a1: rgba(56,189,248,.5);
  --a2: rgba(168,85,247,.55);
  --a3: rgba(250,204,21,.35);
  --a4: rgba(45,212,191,.45);
  --base: #05070f;
  --base2: #111634;
  --ink: #f9fafe;
  --muted: rgba(249,250,254,.72);
  --rim: rgba(255,255,255,.5);
  --rim2: rgba(255,255,255,.14);
  --edge: rgba(255,255,255,.18);
  --accent: #7dd3fc;
}

.gm-14:has(#gm-14-theme:checked) .gm-14__sun {
  display: none;
}

.gm-14:has(#gm-14-theme:checked) .gm-14__moon {
  display: block;
}

.gm-14[data-theme="light"] .gm-14__cta,
.gm-14:has(#gm-14-theme:checked) .gm-14__cta {
  color: #fff;
}

@media (prefers-reduced-motion: reduce) {
  .gm-14 *,
    .gm-14 *::before,
    .gm-14 *::after {
    transition: none !important;
    animation: none !important;
    scroll-behavior: auto !important;
  }
}

@media (forced-colors: active) {
  .gm-14__bar,
    .gm-14__cta,
    .gm-14__ghost,
    .gm-14__theme,
    .gm-14__band span {
    border-color: CanvasText;
    box-shadow: none;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
    background: Canvas;
  }
}
```
