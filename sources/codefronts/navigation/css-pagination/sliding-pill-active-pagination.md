---
source: "codefronts"
url: "https://codefronts.com/navigation/css-pagination/sliding-pill-active-pagination/"
title: "Sliding Pill Active Pagination"
section: "navigation"
category: "css-pagination"
category_name: "CSS Pagination"
description: "One pill that slides between five positions instead of five backgrounds blinking on and off."
has_js: "false"
---

Here's a working CSS Pagination from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sliding Pill Active Pagination
Source: https://codefronts.com/navigation/css-pagination/sliding-pill-active-pagination/

One pill that slides between five positions instead of five backgrounds blinking on and off. Built on a native radio group, so arrow-key traversal is free, and driven entirely by a custom property the parent selector rewrites — the movement is a single compositor-only translate with a little overshoot.
## HTML
```html
<section class="pgn-14" aria-label="Sliding Pill Active Indicator Pagination demo">
  <div class="pgn-14__stage">
    <header class="pgn-14__head">
      <p class="pgn-14__eyebrow">Radio group · arrow keys work</p>
      <h2 class="pgn-14__title">One pill, five positions</h2>
      <p class="pgn-14__sub">Focus any page and press the left or right arrow — the group is a native radio set, so keyboard traversal comes free and the indicator slides instead of blinking.</p>
    </header>

    <nav class="pgn-14__nav" aria-label="Pagination">
      <div class="pgn-14__track" role="none">
        <span class="pgn-14__pill" aria-hidden="true"></span>
        <input class="pgn-14__radio" type="radio" name="pgn-14" id="pgn-14-1" checked>
        <label class="pgn-14__label" for="pgn-14-1">1</label>
        <input class="pgn-14__radio" type="radio" name="pgn-14" id="pgn-14-2">
        <label class="pgn-14__label" for="pgn-14-2">2</label>
        <input class="pgn-14__radio" type="radio" name="pgn-14" id="pgn-14-3">
        <label class="pgn-14__label" for="pgn-14-3">3</label>
        <input class="pgn-14__radio" type="radio" name="pgn-14" id="pgn-14-4">
        <label class="pgn-14__label" for="pgn-14-4">4</label>
        <input class="pgn-14__radio" type="radio" name="pgn-14" id="pgn-14-5">
        <label class="pgn-14__label" for="pgn-14-5">5</label>
      </div>
    </nav>

    <p class="pgn-14__readout" role="status" aria-live="polite">
      <span class="pgn-14__r" data-i="1">Page 1 · results 1–20</span>
      <span class="pgn-14__r" data-i="2">Page 2 · results 21–40</span>
      <span class="pgn-14__r" data-i="3">Page 3 · results 41–60</span>
      <span class="pgn-14__r" data-i="4">Page 4 · results 61–80</span>
      <span class="pgn-14__r" data-i="5">Page 5 · results 81–100</span>
    </p>
  </div>
</section>
```
## CSS
```css
.pgn-14 {
  --bg: #fafafa;
  --surface: #ffffff;
  --surface-2: #f0f0f2;
  --text: #09090b;
  --muted: #71717a;
  --line: #e4e4e7;
  --acc: #18181b;
  --acc-fg: #ffffff;
  --ring: #6366f1;
  --n: 5;
}

@supports (color: oklch(50% 0 0)) {
  .pgn-14 {
    --bg: oklch(98.4% .002 286);
    --surface: oklch(100% 0 0);
    --surface-2: oklch(95.5% .004 286);
    --text: oklch(17% .006 286);
    --muted: oklch(55% .015 286);
    --line: oklch(92% .004 286);
    --acc: oklch(22% .008 286);
    --acc-fg: oklch(99% 0 0);
    --ring: oklch(62% .19 277);
  }
}

@media (prefers-color-scheme: dark) {
  .pgn-14:not([data-theme="light"]) {
    --bg: #09090b;
    --surface: #151518;
    --surface-2: #202024;
    --text: #fafafa;
    --muted: #a1a1aa;
    --line: #27272a;
    --acc: #fafafa;
    --acc-fg: #09090b;
    --ring: #818cf8;
  }
}

.pgn-14[data-theme="dark"] {
  --bg: #09090b;
  --surface: #151518;
  --surface-2: #202024;
  --text: #fafafa;
  --muted: #a1a1aa;
  --line: #27272a;
  --acc: #fafafa;
  --acc-fg: #09090b;
  --ring: #818cf8;
}

.pgn-14 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,5vw,4rem);
  background: var(--bg);
  color: var(--text);
  font-family: system-ui,-apple-system,"Segoe UI",sans-serif;
  -webkit-font-smoothing: antialiased;
}

.pgn-14,
.pgn-14 *,
.pgn-14 *::before,
.pgn-14 *::after {
  box-sizing: border-box;
}

.pgn-14__stage {
  width: 100%;
  max-width: 40rem;
  display: grid;
  gap: 2rem;
  justify-items: center;
  text-align: center;
}

.pgn-14__eyebrow {
  margin: 0 0 .4rem;
  font-size: .6875rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.pgn-14__title {
  margin: 0 0 .55rem;
  font-size: clamp(1.4rem,3.2vw,1.9rem);
  font-weight: 600;
  letter-spacing: -.025em;
}

.pgn-14__sub {
  margin: 0;
  max-width: 32rem;
  font-size: .875rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.pgn-14__track {
  position: relative;
  display: grid;
  grid-auto-flow: column;
  grid-auto-columns: 3.25rem;
  padding: .3rem;
  background: var(--surface-2);
  border: 1px solid var(--line);
  border-radius: 999px;
  --i: 0;
}

.pgn-14__pill {
  position: absolute;
  inset: .3rem auto .3rem .3rem;
  width: 3.25rem;
  border-radius: 999px;
  background: var(--acc);
  translate: calc(var(--i) * 3.25rem) 0;
  transition: translate .34s cubic-bezier(.34,1.4,.5,1);
}

.pgn-14__radio {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.pgn-14__label {
  position: relative;
  z-index: 1;
  display: grid;
  place-items: center;
  height: 2.75rem;
  border-radius: 999px;
  color: var(--muted);
  font-size: .9375rem;
  font-variant-numeric: tabular-nums;
  cursor: pointer;
  transition: color .2s ease;
}

.pgn-14__label:hover {
  color: var(--text);
}

.pgn-14:has(#pgn-14-1:checked) .pgn-14__track {
  --i: 0;
}

.pgn-14:has(#pgn-14-2:checked) .pgn-14__track {
  --i: 1;
}

.pgn-14:has(#pgn-14-3:checked) .pgn-14__track {
  --i: 2;
}

.pgn-14:has(#pgn-14-4:checked) .pgn-14__track {
  --i: 3;
}

.pgn-14:has(#pgn-14-5:checked) .pgn-14__track {
  --i: 4;
}

.pgn-14__radio:checked + .pgn-14__label {
  color: var(--acc-fg);
  font-weight: 600;
}

.pgn-14__radio:focus-visible + .pgn-14__label {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.pgn-14__readout {
  margin: 0;
  font-size: .875rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
  min-height: 1.4em;
}

.pgn-14__r {
  display: none;
}

.pgn-14:has(#pgn-14-1:checked) [data-i="1"],
.pgn-14:has(#pgn-14-2:checked) [data-i="2"],
.pgn-14:has(#pgn-14-3:checked) [data-i="3"],
.pgn-14:has(#pgn-14-4:checked) [data-i="4"],
.pgn-14:has(#pgn-14-5:checked) [data-i="5"] {
  display: inline;
}

@media (prefers-reduced-motion: reduce) {
  .pgn-14 * {
    animation: none !important;
    transition: none !important;
  }
}
```
