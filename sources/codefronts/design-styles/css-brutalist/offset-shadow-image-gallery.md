---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-brutalist/offset-shadow-image-gallery/"
title: "Offset Shadow Image Gallery"
section: "design-styles"
category: "css-brutalist"
category_name: "CSS Brutalism"
description: "Six photographs in thick black frames, each tilted at an alternating angle and sitting on a hard offset shadow."
has_js: "false"
---

Here's a working CSS Brutalism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Offset Shadow Image Gallery
Source: https://codefronts.com/design-styles/css-brutalist/offset-shadow-image-gallery/

Six photographs in thick black frames, each tilted at an alternating angle and sitting on a hard offset shadow. Hover or keyboard focus straightens the frame and pushes the shadow out; captions sit below in bold uppercase. Every frame declares its ratio up front, so the grid never reflows as photos arrive.
## HTML
```html
<div class="brt-12">
  <input class="brt-12__sr" type="checkbox" id="brt-12-dark">
  <label class="brt-12__theme" for="brt-12-dark">
    <svg class="brt-12__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/></svg>
    <svg class="brt-12__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="2.2"/><path d="M12 3v2.2M12 18.8V21M3 12h2.2M18.8 12H21M5.6 5.6l1.6 1.6M16.8 16.8l1.6 1.6M18.4 5.6l-1.6 1.6M7.2 16.8l-1.6 1.6" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
    <span class="brt-12__vh">Dark theme</span>
  </label>

  <div class="brt-12__stage">
    <section class="brt-12__wrap" aria-labelledby="brt-12-h">
      <header class="brt-12__head">
        <h2 class="brt-12__h" id="brt-12-h">Field trip, 2026</h2>
        <p class="brt-12__sub">Six frames from a fortnight on the north coast. Hover or tab through to straighten them.</p>
      </header>

      <ul class="brt-12__grid">
        <li class="brt-12__item">
          <figure class="brt-12__frame">
            <img class="brt-12__img" src="https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?w=640&amp;h=480&amp;fit=crop&amp;auto=format" width="640" height="480" alt="Fog rolling between pine ridges at first light" loading="lazy" decoding="async">
          </figure>
          <figcaption class="brt-12__cap"><a href="#brt-12-h">Ridge fog, 05:40</a></figcaption>
        </li>
        <li class="brt-12__item">
          <figure class="brt-12__frame">
            <img class="brt-12__img" src="https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=640&amp;h=480&amp;fit=crop&amp;auto=format" width="640" height="480" alt="A hiker on a rocky outcrop above a wide valley" loading="lazy" decoding="async">
          </figure>
          <figcaption class="brt-12__cap"><a href="#brt-12-h">Long way down</a></figcaption>
        </li>
        <li class="brt-12__item">
          <figure class="brt-12__frame">
            <img class="brt-12__img" src="https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=640&amp;h=480&amp;fit=crop&amp;auto=format" width="640" height="480" alt="Sunlight through the trunks of a dense beech wood" loading="lazy" decoding="async">
          </figure>
          <figcaption class="brt-12__cap"><a href="#brt-12-h">Beech wood, noon</a></figcaption>
        </li>
        <li class="brt-12__item">
          <figure class="brt-12__frame">
            <img class="brt-12__img" src="https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?w=640&amp;h=480&amp;fit=crop&amp;auto=format" width="640" height="480" alt="Cloud breaking over a granite mountain face" loading="lazy" decoding="async">
          </figure>
          <figcaption class="brt-12__cap"><a href="#brt-12-h">Granite and cloud</a></figcaption>
        </li>
        <li class="brt-12__item">
          <figure class="brt-12__frame">
            <img class="brt-12__img" src="https://images.unsplash.com/photo-1519681393784-d120267933ba?w=640&amp;h=480&amp;fit=crop&amp;auto=format" width="640" height="480" alt="A dark mountain lake under a sky full of stars" loading="lazy" decoding="async">
          </figure>
          <figcaption class="brt-12__cap"><a href="#brt-12-h">Lake, no moon</a></figcaption>
        </li>
        <li class="brt-12__item">
          <figure class="brt-12__frame">
            <img class="brt-12__img" src="https://images.unsplash.com/photo-1465101162946-4377e57745c3?w=640&amp;h=480&amp;fit=crop&amp;auto=format" width="640" height="480" alt="Long grass bending in wind on an open headland" loading="lazy" decoding="async">
          </figure>
          <figcaption class="brt-12__cap"><a href="#brt-12-h">Headland wind</a></figcaption>
        </li>
      </ul>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&display=swap');

.brt-12 {
  --page: #f6f2ea;
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
  --bw: 4px;
  --r: 10px;
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

.brt-12 *,
.brt-12 *::before,
.brt-12 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 300)) {
  .brt-12 {
    --page: oklch(0.963 0.014 88);
    --panel: oklch(1 0 0);
    --ink: oklch(0.16 0.01 285);
    --lilac: oklch(0.82 0.11 296);
    --mint: oklch(0.89 0.13 155);
    --coral: oklch(0.83 0.10 15);
    --butter: oklch(0.92 0.11 95);
    --sky: oklch(0.83 0.09 250);
  }
}

.brt-12__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.brt-12__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.brt-12__theme {
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
  border: 3px solid var(--edge);
  border-radius: 10px;
  box-shadow: 4px 4px 0 var(--sh);
  cursor: pointer;
  transition: translate .14s ease, box-shadow .14s ease;
}

.brt-12__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
}

.brt-12__theme svg {
  inline-size: 1.25rem;
  block-size: 1.25rem;
}

.brt-12__theme:active {
  translate: 2px 2px;
  box-shadow: 2px 2px 0 var(--sh);
}

.brt-12__sr:focus-visible + .brt-12__theme {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
}

.brt-12__sun {
  display: none;
}

.brt-12__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.75rem,5vw,3.5rem);
}

.brt-12__wrap {
  inline-size: min(76rem,100%);
}

.brt-12__head {
  margin-block-end: clamp(1.75rem,4vw,2.5rem);
  padding-inline-end: 3rem;
}

.brt-12__h {
  margin: 0;
  font-size: clamp(1.9rem,5vw,3rem);
  font-weight: 700;
  letter-spacing: -.03em;
}

.brt-12__sub {
  margin: .5rem 0 0;
  max-inline-size: 46ch;
  font-size: .98rem;
  color: var(--muted);
  text-wrap: pretty;
}

.brt-12__grid {
  list-style: none;
  margin: 0;
  padding: .5rem;
  display: grid;
  gap: clamp(1.5rem,3.4vw,2.5rem);
  grid-template-columns: repeat(auto-fit,minmax(min(15rem,100%),1fr));
}

.brt-12__item {
  display: grid;
  gap: .85rem;
}

.brt-12__frame {
  margin: 0;
  padding: 0;
  overflow: hidden;
  --rot: 0deg;
  rotate: var(--rot);
  background: var(--panel);
  border: var(--bw) solid var(--edge);
  border-radius: var(--r);
  box-shadow: 8px 8px 0 var(--sh);
  transition: rotate .16s ease, translate .16s ease, box-shadow .16s ease;
}

.brt-12__item:nth-child(odd) .brt-12__frame {
  --rot: -2.2deg;
}

.brt-12__item:nth-child(even) .brt-12__frame {
  --rot: 1.8deg;
}

.brt-12__item:nth-child(3n) .brt-12__frame {
  --rot: -3.4deg;
}

@media (hover: hover) {
  .brt-12__item:hover .brt-12__frame {
    rotate: 0deg;
    translate: -2px -3px;
    box-shadow: 12px 12px 0 var(--sh);
  }
}

.brt-12__item:focus-within .brt-12__frame {
  rotate: 0deg;
  translate: -2px -3px;
  box-shadow: 12px 12px 0 var(--sh);
}

.brt-12__img {
  display: block;
  inline-size: 100%;
  aspect-ratio: 4/3;
  object-fit: cover;
  background: var(--page);
}

.brt-12__cap {
  font-size: .82rem;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
}

.brt-12__cap a {
  color: var(--ink);
  text-decoration: none;
  border-block-end: 3px solid transparent;
}

.brt-12__cap a:hover {
  border-block-end-color: var(--edge);
  background: var(--butter);
  color: var(--on);
}

.brt-12__cap a:focus-visible {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
}

.brt-12:has(#brt-12-dark:checked) {
  --page: #131217;
  --panel: #1e1c25;
  --ink: #f7f5ef;
  --muted: #b5b1c2;
  --edge: #f7f5ef;
  --sh: #f7f5ef;
}

.brt-12:has(#brt-12-dark:checked) .brt-12__moon {
  display: none;
}

.brt-12:has(#brt-12-dark:checked) .brt-12__sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .brt-12:not(:has(#brt-12-dark:checked)) {
    --page: #131217;
    --panel: #1e1c25;
    --ink: #f7f5ef;
    --muted: #b5b1c2;
    --edge: #f7f5ef;
    --sh: #f7f5ef;
  }

  .brt-12:not(:has(#brt-12-dark:checked)) .brt-12__moon {
    display: none;
  }

  .brt-12:not(:has(#brt-12-dark:checked)) .brt-12__sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .brt-12 *,
    .brt-12 *::before,
    .brt-12 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .brt-12__frame,
    .brt-12__theme {
    border-color: CanvasText;
    box-shadow: none;
  }
}
/* stage children default to min-width:auto, so a wide heading or grid
   track forces the panel past the stage; 0 lets it shrink instead */

.brt-12__stage > * {
  min-inline-size: 0;
  max-inline-size: 100%;
}
```
