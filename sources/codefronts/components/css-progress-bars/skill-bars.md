---
source: "codefronts"
url: "https://codefronts.com/components/css-progress-bars/skill-bars/"
title: "Skill Level Progress Bars for Portfolio Sites"
section: "components"
category: "css-progress-bars"
category_name: "CSS Progress Bars"
description: "Portfolio skill bars that fill as they scroll into view, driven by animation-timeline: view() where it exists and an IntersectionObserver where it does not —…"
has_js: "true"
---

Here's a working CSS Progress Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Skill Level Progress Bars for Portfolio Sites
Source: https://codefronts.com/components/css-progress-bars/skill-bars/

Portfolio skill bars that fill as they scroll into view, driven by animation-timeline: view() where it exists and an IntersectionObserver where it does not — with the level written as a word next to every bar, because "87%" of a skill is a number nobody can verify.
## HTML
```html
<div class="pb-18">
  <button class="pb-18__theme" type="button" aria-pressed="false" aria-label="Toggle dark or light theme">
    <svg class="pb-18__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="pb-18__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
  </button>

  <div class="pb-18__scroller" tabindex="0" role="group" aria-label="Skills, scroll to reveal">
    <header class="pb-18__intro">
      <p class="pb-18__kicker">Sam Rivera &middot; Front-end engineer</p>
      <h2 class="pb-18__title">What I actually reach for</h2>
      <p class="pb-18__lead">Scroll down. Each bar fills on its own view timeline &mdash; no observer where the browser has one built in.</p>
      <p class="pb-18__cue"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 4.5v13.5M6.5 12.6 12 18.2l5.5-5.6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>keep scrolling</p>
    </header>

    <ul class="pb-18__list">
      <li class="pb-18__row" style="--value:92">
        <span class="pb-18__name">TypeScript</span>
        <span class="pb-18__bar" role="progressbar" aria-valuenow="92" aria-valuemin="0" aria-valuemax="100" aria-valuetext="Expert" aria-label="TypeScript"><span class="pb-18__fill"></span></span>
        <span class="pb-18__lvl">Expert<span class="pb-18__yrs">8 yrs</span></span>
      </li>
      <li class="pb-18__row" style="--value:88">
        <span class="pb-18__name">CSS architecture</span>
        <span class="pb-18__bar" role="progressbar" aria-valuenow="88" aria-valuemin="0" aria-valuemax="100" aria-valuetext="Expert" aria-label="CSS architecture"><span class="pb-18__fill"></span></span>
        <span class="pb-18__lvl">Expert<span class="pb-18__yrs">9 yrs</span></span>
      </li>
      <li class="pb-18__row" style="--value:80">
        <span class="pb-18__name">React</span>
        <span class="pb-18__bar" role="progressbar" aria-valuenow="80" aria-valuemin="0" aria-valuemax="100" aria-valuetext="Advanced" aria-label="React"><span class="pb-18__fill"></span></span>
        <span class="pb-18__lvl">Advanced<span class="pb-18__yrs">7 yrs</span></span>
      </li>
      <li class="pb-18__row" style="--value:72">
        <span class="pb-18__name">Node.js</span>
        <span class="pb-18__bar" role="progressbar" aria-valuenow="72" aria-valuemin="0" aria-valuemax="100" aria-valuetext="Advanced" aria-label="Node.js"><span class="pb-18__fill"></span></span>
        <span class="pb-18__lvl">Advanced<span class="pb-18__yrs">6 yrs</span></span>
      </li>
      <li class="pb-18__row" style="--value:58">
        <span class="pb-18__name">Accessibility audits</span>
        <span class="pb-18__bar" role="progressbar" aria-valuenow="58" aria-valuemin="0" aria-valuemax="100" aria-valuetext="Working knowledge" aria-label="Accessibility audits"><span class="pb-18__fill"></span></span>
        <span class="pb-18__lvl">Working<span class="pb-18__yrs">4 yrs</span></span>
      </li>
      <li class="pb-18__row" style="--value:44">
        <span class="pb-18__name">Rust (wasm)</span>
        <span class="pb-18__bar" role="progressbar" aria-valuenow="44" aria-valuemin="0" aria-valuemax="100" aria-valuetext="Foundational" aria-label="Rust for WebAssembly"><span class="pb-18__fill"></span></span>
        <span class="pb-18__lvl">Foundational<span class="pb-18__yrs">2 yrs</span></span>
      </li>
    </ul>

    <footer class="pb-18__foot">
      <p class="pb-18__mono" id="pb-18-mode">detecting timeline support&hellip;</p>
      <p class="pb-18__footNote">Levels are words first. A percentage on a skill is a number nobody can verify &mdash; the bar is the texture, the word is the claim.</p>
    </footer>
  </div>
</div>
```
## CSS
```css
.pb-18 {
  --bg: #fbfaf8;
  --ink: #14120f;
  --muted: rgba(20,18,15,.58);
  --line: rgba(20,18,15,.12);
  --track: rgba(20,18,15,.08);
  --accent: #1c1917;
  --accent-2: #b45309;
  --sans: system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: ui-monospace,"JetBrains Mono","Geist Mono",SFMono-Regular,Menlo,monospace;
  inline-size: 100%;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.pb-18 *,
.pb-18 *::before,
.pb-18 *::after {
  box-sizing: border-box;
}

.pb-18__theme {
  position: absolute;
  inset-block-start: clamp(.9rem,2.4vw,1.6rem);
  inset-inline-end: clamp(.9rem,2.4vw,1.6rem);
  z-index: 5;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  border-radius: 99px;
  border: 1px solid var(--line);
  color: var(--ink);
  background: rgba(20,18,15,.05);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  transition: background .2s,transform .2s;
}

.pb-18__theme:hover {
  transform: translateY(-1px);
}

.pb-18__theme:focus-visible {
  outline: 2px solid var(--accent-2);
  outline-offset: 3px;
}

.pb-18__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.pb-18__sun {
  display: block;
}

.pb-18__moon {
  display: none;
}

.pb-18[data-theme="dark"] .pb-18__sun {
  display: none;
}

.pb-18[data-theme="dark"] .pb-18__moon {
  display: block;
}

.pb-18__scroller {
  block-size: 100vh;
  overflow-y: auto;
  overscroll-behavior-y: contain;
  scroll-behavior: smooth;
  padding: clamp(1.4rem,5vw,4rem) clamp(1.1rem,5vw,3rem) clamp(3rem,10vh,6rem);
  display: grid;
  gap: clamp(1.6rem,5vh,3.2rem);
  justify-items: center;
  align-content: start;
}

.pb-18__scroller:focus-visible {
  outline: 2px solid var(--accent-2);
  outline-offset: -4px;
}

.pb-18__intro {
  inline-size: min(38rem,100%);
  display: grid;
  gap: .6rem;
  min-block-size: 52vh;
  align-content: center;
}

.pb-18__kicker {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--accent-2);
}

.pb-18__title {
  margin: 0;
  font-size: clamp(1.9rem,6vw,3.2rem);
  line-height: 1.04;
  letter-spacing: -.035em;
  font-weight: 600;
  text-wrap: balance;
}

.pb-18__lead {
  margin: 0;
  max-inline-size: 42ch;
  font-size: clamp(.95rem,1.6vw,1.08rem);
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.pb-18__cue {
  margin: .6rem 0 0;
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  font-family: var(--mono);
  font-size: .7rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.pb-18__cue svg {
  inline-size: 1rem;
  block-size: 1rem;
  animation: pb-18-bob 1.8s ease-in-out infinite;
}

@keyframes pb-18-bob {
  0%,
    100% {
    transform: translateY(0);
  }

  50% {
    transform: translateY(.2rem);
  }
}

.pb-18__list {
  list-style: none;
  margin: 0;
  padding: 0;
  inline-size: min(38rem,100%);
  display: grid;
  gap: 0;
}

.pb-18__row {
  display: grid;
  grid-template-columns: minmax(7rem,10rem) 1fr minmax(6rem,8rem);
  gap: 1rem;
  align-items: center;
  padding-block: clamp(1rem,2.6vh,1.5rem);
  border-block-start: 1px solid var(--line);
}

.pb-18__row:last-child {
  border-block-end: 1px solid var(--line);
}

.pb-18__name {
  font-size: clamp(.92rem,1.6vw,1.02rem);
  font-weight: 550;
  letter-spacing: -.01em;
}

.pb-18__bar {
  position: relative;
  display: block;
  inline-size: 100%;
  block-size: .4rem;
  border-radius: 99px;
  background: var(--track);
  overflow: hidden;
}

.pb-18__fill {
  position: absolute;
  inset-block: 0;
  inset-inline-start: 0;
  inline-size: calc(var(--value,0) * 1%);
  border-radius: 99px;
  background: linear-gradient(90deg,var(--accent),var(--accent-2));
  transform-origin: left center;
  will-change: transform;
}

.pb-18__lvl {
  display: grid;
  gap: .05rem;
  justify-items: end;
  text-align: end;
}

.pb-18__lvl {
  font-size: .85rem;
  font-weight: 600;
}

.pb-18__yrs {
  font-family: var(--mono);
  font-size: .66rem;
  font-weight: 400;
  color: var(--muted);
}

.pb-18__foot {
  inline-size: min(38rem,100%);
  display: grid;
  gap: .5rem;
  padding-block-start: .6rem;
}

.pb-18__mono {
  margin: 0;
  font-family: var(--mono);
  font-size: .7rem;
  color: var(--muted);
}

.pb-18__footNote {
  margin: 0;
  max-inline-size: 46ch;
  font-size: .85rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

@keyframes pb-18-grow {
  from {
    transform: scaleX(0);
  }

  to {
    transform: scaleX(1);
  }
}

@supports (animation-timeline: view()) {
  .pb-18__fill {
    animation: pb-18-grow linear both;
    animation-timeline: view();
    animation-range: entry 15% cover 45%;
  }
}

@supports not (animation-timeline: view()) {
  .pb-18__fill {
    transform: scaleX(0);
    transition: transform .7s cubic-bezier(.4,0,.2,1);
  }

  .pb-18__row[data-inview="true"] .pb-18__fill {
    transform: scaleX(1);
  }
}

.pb-18[data-theme="dark"] {
  --bg: #0d0c0a;
  --ink: #f4f1ec;
  --muted: rgba(244,241,236,.6);
  --line: rgba(244,241,236,.13);
  --track: rgba(244,241,236,.1);
  --accent: #f4f1ec;
  --accent-2: #fbbf24;
}

.pb-18[data-theme="dark"] .pb-18__theme {
  background: rgba(255,255,255,.07);
}

@media (prefers-color-scheme: dark) {
  .pb-18:not([data-theme="light"]) {
    --bg: #0d0c0a;
    --ink: #f4f1ec;
    --muted: rgba(244,241,236,.6);
    --line: rgba(244,241,236,.13);
    --track: rgba(244,241,236,.1);
    --accent: #f4f1ec;
    --accent-2: #fbbf24;
  }

  .pb-18:not([data-theme="light"]) .pb-18__theme {
    background: rgba(255,255,255,.07);
  }

  .pb-18:not([data-theme="light"]) .pb-18__sun {
    display: none;
  }

  .pb-18:not([data-theme="light"]) .pb-18__moon {
    display: block;
  }

  .pb-18[data-theme="light"] .pb-18__sun {
    display: block;
  }

  .pb-18[data-theme="light"] .pb-18__moon {
    display: none;
  }
}

@media (max-width: 34rem) {
  .pb-18__row {
    grid-template-columns: 1fr auto;
    row-gap: .5rem;
  }

  .pb-18__bar {
    grid-column: 1 / -1;
    grid-row: 2;
  }
}

@media (prefers-reduced-motion: reduce) {
  .pb-18 *,
    .pb-18 *::before,
    .pb-18 *::after {
    animation: none !important;
    transition: none !important;
  }

  .pb-18__scroller {
    scroll-behavior: auto;
  }

  .pb-18__fill {
    transform: scaleX(1) !important;
  }
}

@media (forced-colors: active) {
  .pb-18__bar,
    .pb-18__theme {
    border: 1px solid CanvasText;
  }

  .pb-18__fill {
    background: Highlight;
  }
}
```

## JavaScript
```js
const pb18 = document.querySelector('.pb-18');
if (pb18) {
  const rows = [...pb18.querySelectorAll('.pb-18__row')];
  const native = CSS.supports('animation-timeline', 'view()');
  pb18.querySelector('#pb-18-mode').textContent = native
    ? 'animation-timeline: view() \u2014 running natively, zero JS for the fills'
    : 'no view() support \u2014 IntersectionObserver fallback active';
  if (!native) {
    const io = new IntersectionObserver((entries) => entries.forEach((e) => {
      if (e.isIntersecting) { e.target.dataset.inview = 'true'; io.unobserve(e.target); }
    }), { threshold: 0.35, root: pb18.querySelector('.pb-18__scroller') });
    rows.forEach((row) => io.observe(row));
  }
  pb18.querySelector('.pb-18__theme').addEventListener('click', (e) => {
    const dark = pb18.dataset.theme !== 'dark';
    pb18.dataset.theme = dark ? 'dark' : 'light';
    e.currentTarget.setAttribute('aria-pressed', String(dark));
  });
}
```
