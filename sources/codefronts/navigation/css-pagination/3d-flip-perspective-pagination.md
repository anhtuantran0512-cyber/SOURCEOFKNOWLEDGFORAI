---
source: "codefronts"
url: "https://codefronts.com/navigation/css-pagination/3d-flip-perspective-pagination/"
title: "3D Flip Perspective Pagination"
section: "navigation"
category: "css-pagination"
category_name: "CSS Pagination"
description: "Each page key is a two-faced box: the number on the front, a verb on the back."
has_js: "false"
---

Here's a working CSS Pagination from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: 3D Flip Perspective Pagination
Source: https://codefronts.com/navigation/css-pagination/3d-flip-perspective-pagination/

Each page key is a two-faced box: the number on the front, a verb on the back. Hover or focus rotates it a half turn on X and the browser swaps which face points at the camera. Perspective lives on each button rather than the row, so the outer keys do not skew, and reduced motion falls back to a plain background change.
## HTML
```html
<section class="pgn-16" aria-label="3D Flip / Depth Perspective Pagination demo">
  <div class="pgn-16__stage">
    <header class="pgn-16__head">
      <p class="pgn-16__eyebrow">transform-style: preserve-3d</p>
      <h2 class="pgn-16__title">Each key flips to reveal its face</h2>
      <p class="pgn-16__sub">Hover or focus a number. Two faces sit on the same box, one rotated a quarter turn on X; the parent rotates and the browser swaps which face points at the camera.</p>
    </header>

    <nav class="pgn-16__nav" aria-label="Pagination">
      <ol class="pgn-16__list">
        <li><button class="pgn-16__key" type="button"><span class="pgn-16__inner"><span class="pgn-16__face">1</span><span class="pgn-16__face pgn-16__face--back">Go</span></span></button></li>
        <li><button class="pgn-16__key" type="button"><span class="pgn-16__inner"><span class="pgn-16__face">2</span><span class="pgn-16__face pgn-16__face--back">Go</span></span></button></li>
        <li><button class="pgn-16__key" type="button" aria-current="page"><span class="pgn-16__inner"><span class="pgn-16__face">3</span><span class="pgn-16__face pgn-16__face--back">Here</span></span></button></li>
        <li><button class="pgn-16__key" type="button"><span class="pgn-16__inner"><span class="pgn-16__face">4</span><span class="pgn-16__face pgn-16__face--back">Go</span></span></button></li>
        <li><button class="pgn-16__key" type="button"><span class="pgn-16__inner"><span class="pgn-16__face">5</span><span class="pgn-16__face pgn-16__face--back">Go</span></span></button></li>
      </ol>
    </nav>

    <p class="pgn-16__note">Page 3 of 5 · 60 results</p>
  </div>
</section>
```
## CSS
```css
.pgn-16 {
  --bg: #0c0c0f;
  --surface: #17171c;
  --surface-2: #212129;
  --text: #f4f4f5;
  --muted: #8f8f99;
  --line: #2b2b34;
  --acc: #a78bfa;
  --acc-fg: #12101b;
  --ring: #c4b5fd;
}

@supports (color: oklch(50% 0 0)) {
  .pgn-16 {
    --bg: oklch(14% .008 285);
    --surface: oklch(19% .01 285);
    --surface-2: oklch(24% .014 285);
    --text: oklch(96% .002 286);
    --muted: oklch(66% .014 286);
    --line: oklch(29% .012 285);
    --acc: oklch(75% .14 300);
    --acc-fg: oklch(16% .03 300);
    --ring: oklch(82% .1 300);
  }
}

@media (prefers-color-scheme: light) {
  .pgn-16:not([data-theme="dark"]) {
    --bg: #f6f5fa;
    --surface: #ffffff;
    --surface-2: #efeef5;
    --text: #12111a;
    --muted: #6b6a7a;
    --line: #e3e1ec;
    --acc: #6d28d9;
    --acc-fg: #ffffff;
    --ring: #7c3aed;
  }
}

.pgn-16[data-theme="light"] {
  --bg: #f6f5fa;
  --surface: #ffffff;
  --surface-2: #efeef5;
  --text: #12111a;
  --muted: #6b6a7a;
  --line: #e3e1ec;
  --acc: #6d28d9;
  --acc-fg: #ffffff;
  --ring: #7c3aed;
}

.pgn-16 {
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

.pgn-16,
.pgn-16 *,
.pgn-16 *::before,
.pgn-16 *::after {
  box-sizing: border-box;
}

.pgn-16__stage {
  width: 100%;
  max-width: 44rem;
  display: grid;
  gap: 2.25rem;
  justify-items: center;
  text-align: center;
}

.pgn-16__eyebrow {
  margin: 0 0 .4rem;
  font-family: ui-monospace,SFMono-Regular,Menlo,monospace;
  font-size: .6875rem;
  letter-spacing: .06em;
  color: var(--muted);
}

.pgn-16__title {
  margin: 0 0 .55rem;
  font-size: clamp(1.4rem,3.2vw,1.9rem);
  font-weight: 600;
  letter-spacing: -.025em;
  text-wrap: balance;
}

.pgn-16__sub {
  margin: 0;
  max-width: 33rem;
  font-size: .875rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.pgn-16__nav {
  perspective: 600px;
}

.pgn-16__list {
  display: flex;
  gap: .6rem;
  list-style: none;
  margin: 0;
  padding: 0;
}

.pgn-16__key {
  width: 3.5rem;
  height: 3.5rem;
  padding: 0;
  border: 0;
  background: transparent;
  font: inherit;
  cursor: pointer;
  perspective: 600px;
}

.pgn-16__key:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 4px;
  border-radius: .75rem;
}

.pgn-16__inner {
  position: relative;
  display: block;
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
  transition: rotate .42s cubic-bezier(.34,1.2,.5,1);
}

.pgn-16__key:hover .pgn-16__inner,
.pgn-16__key:focus-visible .pgn-16__inner {
  rotate: x -180deg;
}

.pgn-16__face {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  border: 1px solid var(--line);
  border-radius: .75rem;
  background: var(--surface);
  color: var(--text);
  font-size: 1.0625rem;
  font-variant-numeric: tabular-nums;
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  box-shadow: 0 1px 0 color-mix(in oklab,var(--text) 8%,transparent) inset;
}

.pgn-16__face--back {
  rotate: x 180deg;
  background: var(--acc);
  color: var(--acc-fg);
  border-color: transparent;
  font-size: .8125rem;
  font-weight: 600;
  letter-spacing: .01em;
}

.pgn-16__key[aria-current="page"] .pgn-16__face {
  background: var(--surface-2);
  border-color: color-mix(in oklab,var(--acc) 55%,var(--line));
  font-weight: 600;
}

.pgn-16__note {
  margin: 0;
  font-size: .8125rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

@media (prefers-reduced-motion: reduce) {
  .pgn-16 * {
    animation: none !important;
    transition: none !important;
  }

  .pgn-16__key:hover .pgn-16__inner,
    .pgn-16__key:focus-visible .pgn-16__inner {
    rotate: none;
  }

  .pgn-16__key:hover .pgn-16__face,
    .pgn-16__key:focus-visible .pgn-16__face {
    background: var(--surface-2);
  }
}
```
