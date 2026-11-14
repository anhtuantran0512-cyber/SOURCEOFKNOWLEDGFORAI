---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-brutalist/neubrutalist-blog-card-grid/"
title: "Neubrutalist Blog Card Grid"
section: "design-styles"
category: "css-brutalist"
category_name: "CSS Brutalism"
description: "Three article cards with black-framed cover images, a rotated pastel category chip, a heavy headline and a byline row."
has_js: "false"
---

Here's a working CSS Brutalism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neubrutalist Blog Card Grid
Source: https://codefronts.com/design-styles/css-brutalist/neubrutalist-blog-card-grid/

Three article cards with black-framed cover images, a rotated pastel category chip, a heavy headline and a byline row. Hover moves the card toward its shadow rather than away from it — a small inversion of the usual lift that makes the block feel like a physical object being pressed onto the page.
## HTML
```html
<div class="brt-09">
  <input class="brt-09__sr" type="checkbox" id="brt-09-dark">
  <label class="brt-09__theme" for="brt-09-dark">
    <svg class="brt-09__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/></svg>
    <svg class="brt-09__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="2.2"/><path d="M12 3v2.2M12 18.8V21M3 12h2.2M18.8 12H21M5.6 5.6l1.6 1.6M16.8 16.8l1.6 1.6M18.4 5.6l-1.6 1.6M7.2 16.8l-1.6 1.6" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
    <span class="brt-09__vh">Dark theme</span>
  </label>

  <div class="brt-09__stage">
    <section class="brt-09__wrap" aria-labelledby="brt-09-h">
      <header class="brt-09__head">
        <h2 class="brt-09__h" id="brt-09-h">Field notes</h2>
        <a class="brt-09__all" href="#brt-09-h">All 84 posts
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M5 12h13m0 0-5-5m5 5-5 5" stroke="currentColor" stroke-width="2.6" stroke-linecap="square"/></svg>
        </a>
      </header>

      <ul class="brt-09__grid">
        <li class="brt-09__card">
          <img class="brt-09__shot" src="https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=640&amp;h=400&amp;fit=crop&amp;auto=format" width="640" height="400" alt="A code editor open on a laptop beside a notebook" loading="lazy" decoding="async">
          <span class="brt-09__chip" style="--chip:var(--butter)">Engineering</span>
          <h3 class="brt-09__t"><a href="#brt-09-h">We deleted 12,000 lines of CSS and nothing broke</a></h3>
          <p class="brt-09__p">Six months of dead selectors, four design systems, one very long afternoon with coverage tooling.</p>
          <p class="brt-09__by">
            <img class="brt-09__avatar" src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=120&amp;h=120&amp;fit=crop&amp;auto=format" width="120" height="120" alt="Jordan Lee" loading="lazy" decoding="async">
            <span>Jordan Lee</span><span aria-hidden="true">·</span><time datetime="2026-08-04">4 Aug</time>
            <span class="brt-09__read">6 min read</span>
          </p>
        </li>

        <li class="brt-09__card">
          <img class="brt-09__shot" src="https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=640&amp;h=400&amp;fit=crop&amp;auto=format" width="640" height="400" alt="Four colleagues reviewing work around a shared table" loading="lazy" decoding="async">
          <span class="brt-09__chip" style="--chip:var(--mint)">Process</span>
          <h3 class="brt-09__t"><a href="#brt-09-h">Design review, but nobody presents</a></h3>
          <p class="brt-09__p">Async critique with written stakes. Fewer meetings, sharper feedback, and a paper trail you can search.</p>
          <p class="brt-09__by">
            <img class="brt-09__avatar" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=120&amp;h=120&amp;fit=crop&amp;auto=format" width="120" height="120" alt="Priya Sharma" loading="lazy" decoding="async">
            <span>Priya Sharma</span><span aria-hidden="true">·</span><time datetime="2026-07-28">28 Jul</time>
            <span class="brt-09__read">9 min read</span>
          </p>
        </li>

        <li class="brt-09__card">
          <img class="brt-09__shot" src="https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=640&amp;h=400&amp;fit=crop&amp;auto=format" width="640" height="400" alt="Printed charts and a laptop showing analytics on a desk" loading="lazy" decoding="async">
          <span class="brt-09__chip" style="--chip:var(--sky)">Metrics</span>
          <h3 class="brt-09__t"><a href="#brt-09-h">The only three numbers on our wall</a></h3>
          <p class="brt-09__p">Why we retired 41 dashboards and kept activation, retained revenue and time-to-first-deploy.</p>
          <p class="brt-09__by">
            <img class="brt-09__avatar" src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=120&amp;h=120&amp;fit=crop&amp;auto=format" width="120" height="120" alt="Sam Rivera" loading="lazy" decoding="async">
            <span>Sam Rivera</span><span aria-hidden="true">·</span><time datetime="2026-07-19">19 Jul</time>
            <span class="brt-09__read">4 min read</span>
          </p>
        </li>
      </ul>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&display=swap');

.brt-09 {
  --page: #f7f4ec;
  --panel: #ffffff;
  --ink: #0b0b0f;
  --on: #0b0b0f;
  --muted: #4a4a52;
  --lilac: #c4b5fd;
  --mint: #86efac;
  --coral: #fda4af;
  --butter: #fde68a;
  --sky: #93c5fd;
  --edge: #000000;
  --sh: #000000;
  --bw: 3px;
  --r: 14px;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: 'Space Grotesk','Sora',ui-sans-serif,system-ui,sans-serif;
}

.brt-09 *,
.brt-09 *::before,
.brt-09 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 300)) {
  .brt-09 {
    --page: oklch(0.968 0.016 88);
    --panel: oklch(1 0 0);
    --ink: oklch(0.16 0.01 285);
    --lilac: oklch(0.82 0.11 296);
    --mint: oklch(0.89 0.13 155);
    --coral: oklch(0.83 0.10 15);
    --butter: oklch(0.92 0.11 95);
    --sky: oklch(0.83 0.09 250);
  }
}

.brt-09__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.brt-09__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.brt-09__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 5;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  background: var(--panel);
  color: var(--ink);
  border: var(--bw) solid var(--edge);
  border-radius: 10px;
  box-shadow: 4px 4px 0 var(--sh);
  cursor: pointer;
  transition: translate .14s ease, box-shadow .14s ease;
}

.brt-09__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
}

.brt-09__theme svg {
  inline-size: 1.25rem;
  block-size: 1.25rem;
}

.brt-09__theme:active {
  translate: 2px 2px;
  box-shadow: 2px 2px 0 var(--sh);
}

.brt-09__sr:focus-visible + .brt-09__theme {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
}

.brt-09__sun {
  display: none;
}

.brt-09__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,4.5vw,3.5rem);
}

.brt-09__wrap {
  inline-size: min(74rem,100%);
}

.brt-09__head {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  align-items: baseline;
  justify-content: space-between;
  margin-block-end: clamp(1.5rem,3.5vw,2.25rem);
  padding-inline-end: 3rem;
}

.brt-09__h {
  margin: 0;
  font-size: clamp(1.9rem,5vw,2.9rem);
  font-weight: 700;
  letter-spacing: -.03em;
}

.brt-09__all {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  min-block-size: 2.75rem;
  color: var(--ink);
  font-weight: 700;
  font-size: .95rem;
  text-decoration: 3px underline var(--lilac);
  text-underline-offset: 5px;
}

.brt-09__all svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.brt-09__all:hover {
  background: var(--lilac);
  color: var(--on);
}

.brt-09__all:focus-visible {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
}

.brt-09__grid {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: clamp(1.25rem,2.6vw,1.9rem);
  grid-template-columns: repeat(auto-fit,minmax(min(17rem,100%),1fr));
}

.brt-09__card {
  position: relative;
  display: flex;
  flex-direction: column;
  background: var(--panel);
  color: var(--ink);
  border: var(--bw) solid var(--edge);
  border-radius: var(--r);
  box-shadow: 8px 8px 0 var(--sh);
  transition: translate .15s ease, box-shadow .15s ease;
}

.brt-09__card:hover,
.brt-09__card:focus-within {
  translate: 3px 3px;
  box-shadow: 4px 4px 0 var(--sh);
}

.brt-09__shot {
  display: block;
  inline-size: 100%;
  aspect-ratio: 16/10;
  object-fit: cover;
  background: var(--page);
  border-block-end: var(--bw) solid var(--edge);
  border-start-start-radius: calc(var(--r) - 3px);
  border-start-end-radius: calc(var(--r) - 3px);
}

.brt-09__chip {
  align-self: flex-start;
  margin: -1.1rem 0 0 1.1rem;
  padding: .35rem .7rem;
  rotate: -2.5deg;
  background: var(--chip,var(--butter));
  color: var(--on);
  border: var(--bw) solid var(--edge);
  border-radius: 8px;
  box-shadow: 3px 3px 0 var(--sh);
  font-size: .72rem;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
}

.brt-09__t {
  margin: .95rem 1.15rem 0;
  font-size: 1.22rem;
  font-weight: 700;
  letter-spacing: -.02em;
  line-height: 1.18;
  text-wrap: balance;
}

.brt-09__t a {
  color: inherit;
  text-decoration: none;
}

.brt-09__t a::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: var(--r);
}

.brt-09__t a:focus-visible {
  outline: none;
}

.brt-09__card:focus-within .brt-09__t a::after {
  outline: 3px solid var(--edge);
  outline-offset: 4px;
}

.brt-09__p {
  margin: .6rem 1.15rem 1.1rem;
  font-size: .94rem;
  line-height: 1.5;
  color: var(--muted);
  text-wrap: pretty;
}

.brt-09__by {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .45rem;
  margin: auto 0 0;
  padding: .85rem 1.15rem;
  border-block-start: 2px solid var(--edge);
  font-size: .82rem;
  font-weight: 600;
  color: var(--ink);
}

.brt-09__avatar {
  inline-size: 1.9rem;
  block-size: 1.9rem;
  object-fit: cover;
  aspect-ratio: 1;
  background: var(--page);
  border: 2px solid var(--edge);
  border-radius: 50%;
}

.brt-09__read {
  margin-inline-start: auto;
  padding: .25rem .5rem;
  background: var(--page);
  border: 2px solid var(--edge);
  border-radius: 7px;
  font-size: .74rem;
  font-weight: 700;
  letter-spacing: .04em;
  white-space: nowrap;
}

.brt-09:has(#brt-09-dark:checked) {
  --page: #141319;
  --panel: #211f29;
  --ink: #f7f5ef;
  --muted: #b5b1c2;
  --edge: #f7f5ef;
  --sh: #f7f5ef;
}

.brt-09:has(#brt-09-dark:checked) .brt-09__moon {
  display: none;
}

.brt-09:has(#brt-09-dark:checked) .brt-09__sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .brt-09:not(:has(#brt-09-dark:checked)) {
    --page: #141319;
    --panel: #211f29;
    --ink: #f7f5ef;
    --muted: #b5b1c2;
    --edge: #f7f5ef;
    --sh: #f7f5ef;
  }

  .brt-09:not(:has(#brt-09-dark:checked)) .brt-09__moon {
    display: none;
  }

  .brt-09:not(:has(#brt-09-dark:checked)) .brt-09__sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .brt-09 *,
    .brt-09 *::before,
    .brt-09 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .brt-09__card,
    .brt-09__chip,
    .brt-09__read,
    .brt-09__theme {
    border-color: CanvasText;
    box-shadow: none;
  }
}
/* stage children default to min-width:auto, so a wide heading or grid
   track forces the panel past the stage; 0 lets it shrink instead */

.brt-09__stage > * {
  min-inline-size: 0;
  max-inline-size: 100%;
}
```
