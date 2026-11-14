---
source: "codefronts"
url: "https://codefronts.com/navigation/css-pagination/vertical-side-docked-pagination/"
title: "Vertical Side-Docked Pagination"
section: "navigation"
category: "css-pagination"
category_name: "CSS Pagination"
description: "For sectioned long-form content the index belongs on the same axis as the reading: a sticky rail of labelled dots docked to the right edge, with a fill bar…"
has_js: "false"
---

Here's a working CSS Pagination from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Vertical Side-Docked Pagination
Source: https://codefronts.com/navigation/css-pagination/vertical-side-docked-pagination/

For sectioned long-form content the index belongs on the same axis as the reading: a sticky rail of labelled dots docked to the right edge, with a fill bar driven by a scroll-progress timeline where supported. Scroll snapping makes each jump land cleanly, and every dot is a real anchor so deep links survive a reload.
## HTML
```html
<section class="pgn-17" aria-label="Vertical Side-Docked Pagination demo">
  <div class="pgn-17__scroller">
    <nav class="pgn-17__rail" aria-label="Section pagination">
      <span class="pgn-17__progress" aria-hidden="true"><i></i></span>
      <ol class="pgn-17__dots">
        <li><a class="pgn-17__dot" href="#pgn-17-s1" aria-current="page"><span class="pgn-17__label">Overview</span></a></li>
        <li><a class="pgn-17__dot" href="#pgn-17-s2"><span class="pgn-17__label">Pricing</span></a></li>
        <li><a class="pgn-17__dot" href="#pgn-17-s3"><span class="pgn-17__label">Security</span></a></li>
        <li><a class="pgn-17__dot" href="#pgn-17-s4"><span class="pgn-17__label">Changelog</span></a></li>
      </ol>
    </nav>

    <section class="pgn-17__panel" id="pgn-17-s1"><p class="pgn-17__idx">01</p><h2>Overview</h2><p>A docked rail keeps the page index in the periphery while long-form content scrolls past it. Scroll this panel to watch the rail fill.</p></section>
    <section class="pgn-17__panel" id="pgn-17-s2"><p class="pgn-17__idx">02</p><h2>Pricing</h2><p>Vertical pagination suits sectioned documents better than a horizontal number row, because the axis of the control matches the axis of the content.</p></section>
    <section class="pgn-17__panel" id="pgn-17-s3"><p class="pgn-17__idx">03</p><h2>Security</h2><p>Each dot is an anchor to a section id, so the rail works with the keyboard and deep links survive a reload.</p></section>
    <section class="pgn-17__panel" id="pgn-17-s4"><p class="pgn-17__idx">04</p><h2>Changelog</h2><p>The fill bar is driven by a scroll-progress timeline where supported, and stays a static rule everywhere else.</p></section>
  </div>
</section>
```
## CSS
```css
.pgn-17 {
  --bg: #fafafa;
  --surface: #ffffff;
  --surface-2: #f1f1f3;
  --text: #09090b;
  --muted: #71717a;
  --line: #e4e4e7;
  --acc: #18181b;
  --acc-fg: #ffffff;
  --ring: #6366f1;
}

@supports (color: oklch(50% 0 0)) {
  .pgn-17 {
    --bg: oklch(98.4% .002 286);
    --surface: oklch(100% 0 0);
    --surface-2: oklch(96% .003 286);
    --text: oklch(17% .006 286);
    --muted: oklch(55% .015 286);
    --line: oklch(92% .004 286);
    --acc: oklch(22% .008 286);
    --acc-fg: oklch(99% 0 0);
    --ring: oklch(62% .19 277);
  }
}

@media (prefers-color-scheme: dark) {
  .pgn-17:not([data-theme="light"]) {
    --bg: #09090b;
    --surface: #131316;
    --surface-2: #1c1c20;
    --text: #fafafa;
    --muted: #a1a1aa;
    --line: #27272a;
    --acc: #fafafa;
    --acc-fg: #09090b;
    --ring: #818cf8;
  }
}

.pgn-17[data-theme="dark"] {
  --bg: #09090b;
  --surface: #131316;
  --surface-2: #1c1c20;
  --text: #fafafa;
  --muted: #a1a1aa;
  --line: #27272a;
  --acc: #fafafa;
  --acc-fg: #09090b;
  --ring: #818cf8;
}

.pgn-17 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: var(--bg);
  color: var(--text);
  font-family: system-ui,-apple-system,"Segoe UI",sans-serif;
  -webkit-font-smoothing: antialiased;
}

.pgn-17,
.pgn-17 *,
.pgn-17 *::before,
.pgn-17 *::after {
  box-sizing: border-box;
}

.pgn-17__scroller {
  position: relative;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  scroll-snap-type: y proximity;
  scroll-behavior: smooth;
}

.pgn-17__panel {
  min-height: 100vh;
  min-height: 100svh;
  scroll-snap-align: start;
  scroll-margin: 0;
  display: grid;
  align-content: center;
  gap: .6rem;
  padding: clamp(2rem,7vw,5rem);
  padding-right: clamp(6rem,14vw,12rem);
  border-bottom: 1px solid var(--line);
}

.pgn-17__idx {
  margin: 0;
  font-family: ui-monospace,SFMono-Regular,Menlo,monospace;
  font-size: .75rem;
  letter-spacing: .14em;
  color: var(--muted);
}

.pgn-17__panel h2 {
  margin: 0;
  font-size: clamp(1.75rem,5vw,3rem);
  font-weight: 600;
  letter-spacing: -.035em;
}

.pgn-17__panel p:not(.pgn-17__idx) {
  margin: 0;
  max-width: 34rem;
  font-size: 1rem;
  line-height: 1.7;
  color: var(--muted);
  text-wrap: pretty;
}

.pgn-17__rail {
  position: sticky;
  top: 0;
  float: right;
  height: 0;
  z-index: 2;
  display: grid;
  justify-items: end;
  padding: 0 clamp(1rem,3vw,2.25rem);
}

.pgn-17__progress {
  position: absolute;
  top: calc(50svh - 4.5rem);
  right: calc(clamp(1rem,3vw,2.25rem) + 1.2rem);
  width: 2px;
  height: 9rem;
  background: var(--line);
  border-radius: 2px;
  overflow: hidden;
}

.pgn-17__progress i {
  display: block;
  width: 100%;
  height: 100%;
  background: var(--acc);
  transform-origin: top center;
  scale: 1 .25;
}

@supports (animation-timeline: scroll()) {
  .pgn-17__progress i {
    scale: 1 0;
    animation: pgn-17-fill linear both;
    animation-timeline: scroll(nearest block);
  }
}

@keyframes pgn-17-fill {
  from {
    scale: 1 0;
  }

  to {
    scale: 1 1;
  }
}

.pgn-17__dots {
  position: absolute;
  top: calc(50svh - 4.5rem);
  right: clamp(1rem,3vw,2.25rem);
  display: grid;
  gap: 1.85rem;
  list-style: none;
  margin: 0;
  padding: 0;
  height: 9rem;
  align-content: space-between;
}

.pgn-17__dot {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: .6rem;
  min-height: 2.75rem;
  padding-right: .15rem;
  text-decoration: none;
  color: var(--muted);
}

.pgn-17__dot::after {
  content: "";
  width: .5rem;
  height: .5rem;
  border-radius: 50%;
  background: var(--line);
  outline: 1px solid var(--bg);
  transition: background .2s ease, scale .2s cubic-bezier(.16,1,.3,1);
}

.pgn-17__label {
  font-size: .75rem;
  letter-spacing: .01em;
  padding: .3rem .55rem;
  border-radius: .4rem;
  background: var(--surface);
  border: 1px solid var(--line);
  opacity: 0;
  translate: .4rem 0;
  transition: opacity .2s ease, translate .2s ease;
}

.pgn-17__dot:hover .pgn-17__label,
.pgn-17__dot:focus-visible .pgn-17__label {
  opacity: 1;
  translate: 0 0;
}

.pgn-17__dot:hover::after {
  background: var(--muted);
  scale: 1.3;
}

.pgn-17__dot:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
  border-radius: .5rem;
}

.pgn-17__dot[aria-current="page"]::after {
  background: var(--acc);
  scale: 1.35;
}

.pgn-17__scroller:has(#pgn-17-s2:target) [href="#pgn-17-s2"]::after,
.pgn-17__scroller:has(#pgn-17-s3:target) [href="#pgn-17-s3"]::after,
.pgn-17__scroller:has(#pgn-17-s4:target) [href="#pgn-17-s4"]::after {
  background: var(--acc);
  scale: 1.35;
}

@media (prefers-reduced-motion: reduce) {
  .pgn-17 * {
    animation: none !important;
    transition: none !important;
  }

  .pgn-17__scroller {
    scroll-behavior: auto;
  }

  .pgn-17__progress i {
    scale: 1 .25;
  }
}
```
