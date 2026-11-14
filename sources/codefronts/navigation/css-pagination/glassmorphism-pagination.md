---
source: "codefronts"
url: "https://codefronts.com/navigation/css-pagination/glassmorphism-pagination/"
title: "Glassmorphism Pagination"
section: "navigation"
category: "css-pagination"
category_name: "CSS Pagination"
description: "Frosted glass only reads as glass over something worth blurring, so the bar floats over a photograph with a contrast scrim beneath it."
has_js: "false"
---

Here's a working CSS Pagination from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Pagination
Source: https://codefronts.com/navigation/css-pagination/glassmorphism-pagination/

Frosted glass only reads as glass over something worth blurring, so the bar floats over a photograph with a contrast scrim beneath it. Low-alpha fill, an 18 px backdrop blur with a saturation boost, a lit hairline edge and an inset top highlight — plus a solid fallback for engines without backdrop-filter.
## HTML
```html
<section class="pgn-19" aria-label="Glassmorphism Pagination with Backdrop-Filter demo">
  <img class="pgn-19__bg" src="https://images.unsplash.com/photo-1531297484001-80022131f5a1?w=400&auto=format" alt="" aria-hidden="true" width="400" height="267" decoding="async">
  <div class="pgn-19__stage">
    <header class="pgn-19__head">
      <p class="pgn-19__eyebrow">Gallery</p>
      <h2 class="pgn-19__title">Frosted control over live pixels</h2>
    </header>

    <nav class="pgn-19__nav" aria-label="Pagination">
      <button class="pgn-19__btn" type="button" aria-label="Previous page">
        <svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M12.5 4.5 7 10l5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </button>
      <ol class="pgn-19__list">
        <li><button class="pgn-19__num" type="button">1</button></li>
        <li><button class="pgn-19__num" type="button" aria-current="page">2</button></li>
        <li><button class="pgn-19__num" type="button">3</button></li>
        <li><button class="pgn-19__num" type="button">4</button></li>
        <li aria-hidden="true" class="pgn-19__gap">…</li>
        <li><button class="pgn-19__num" type="button">9</button></li>
      </ol>
      <button class="pgn-19__btn" type="button" aria-label="Next page">
        <svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M7.5 4.5 13 10l-5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </button>
    </nav>

    <p class="pgn-19__caption">Page 2 of 9 · 216 photographs</p>
  </div>
</section>
```
## CSS
```css
.pgn-19 {
  --text: #ffffff;
  --muted: rgba(255,255,255,.72);
  --glass: rgba(255,255,255,.12);
  --glass-strong: rgba(255,255,255,.24);
  --edge: rgba(255,255,255,.28);
  --ring: #ffffff;
  --shade: rgba(6,6,12,.55);
}

@supports (color: oklch(50% 0 0)) {
  .pgn-19 {
    --glass: oklch(100% 0 0 / .13);
    --glass-strong: oklch(100% 0 0 / .26);
    --edge: oklch(100% 0 0 / .3);
    --shade: oklch(12% .02 280 / .55);
  }
}

@media (prefers-color-scheme: light) {
  .pgn-19:not([data-theme="dark"]) {
    --shade: rgba(10,10,18,.4);
  }
}

.pgn-19[data-theme="dark"] {
  --shade: rgba(4,4,10,.66);
}

.pgn-19 {
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,5vw,4rem);
  overflow: hidden;
  isolation: isolate;
  background: #1b1035;
  color: var(--text);
  font-family: system-ui,-apple-system,"Segoe UI",sans-serif;
  -webkit-font-smoothing: antialiased;
}

.pgn-19,
.pgn-19 *,
.pgn-19 *::before,
.pgn-19 *::after {
  box-sizing: border-box;
}

.pgn-19__bg {
  position: absolute;
  inset: 0;
  z-index: -2;
  width: 100%;
  height: 100%;
  object-fit: cover;
  filter: saturate(1.15);
}

.pgn-19::after {
  content: "";
  position: absolute;
  inset: 0;
  z-index: -1;
  background: var(--shade);
}

.pgn-19__stage {
  width: 100%;
  max-width: 44rem;
  display: grid;
  gap: 2rem;
  justify-items: center;
  text-align: center;
}

.pgn-19__eyebrow {
  margin: 0 0 .5rem;
  font-size: .6875rem;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--muted);
}

.pgn-19__title {
  margin: 0;
  font-size: clamp(1.5rem,4vw,2.25rem);
  font-weight: 600;
  letter-spacing: -.03em;
  text-wrap: balance;
  text-shadow: 0 1px 24px rgba(0,0,0,.35);
}

.pgn-19__nav {
  display: flex;
  align-items: center;
  gap: .4rem;
  padding: .45rem;
  border: 1px solid var(--edge);
  border-radius: 1.15rem;
  background: var(--glass);
  box-shadow: 0 8px 32px rgba(0,0,0,.28), inset 0 1px 0 rgba(255,255,255,.22);
}

@supports ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .pgn-19__nav {
    -webkit-backdrop-filter: blur(18px) saturate(1.6);
    backdrop-filter: blur(18px) saturate(1.6);
    background: var(--glass);
  }
}

@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .pgn-19__nav {
    background: rgba(20,16,40,.72);
  }
}

.pgn-19__list {
  display: flex;
  align-items: center;
  gap: .2rem;
  list-style: none;
  margin: 0;
  padding: 0;
}

.pgn-19__num,
.pgn-19__btn {
  display: grid;
  place-items: center;
  min-width: 2.75rem;
  height: 2.75rem;
  padding: 0 .5rem;
  border: 1px solid transparent;
  border-radius: .8rem;
  background: transparent;
  color: var(--text);
  font: inherit;
  font-size: .9375rem;
  font-variant-numeric: tabular-nums;
  cursor: pointer;
  transition: background .18s ease, border-color .18s ease;
}

.pgn-19__num:hover,
.pgn-19__btn:hover {
  background: var(--glass-strong);
  border-color: var(--edge);
}

.pgn-19__num:focus-visible,
.pgn-19__btn:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

.pgn-19__num[aria-current="page"] {
  background: var(--glass-strong);
  border-color: var(--edge);
  font-weight: 600;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.35);
}

.pgn-19__btn svg {
  width: 1.1rem;
  height: 1.1rem;
}

.pgn-19__gap {
  display: grid;
  place-items: end center;
  min-width: 1.5rem;
  height: 2.75rem;
  padding-bottom: .6rem;
  color: var(--muted);
}

.pgn-19__caption {
  margin: 0;
  font-size: .8125rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

@media (prefers-reduced-motion: reduce) {
  .pgn-19 * {
    animation: none !important;
    transition: none !important;
  }
}
```
