---
source: "codefronts"
url: "https://codefronts.com/layouts/css-diagonal-sections/css-animated-diagonal-section-on-scroll/"
title: "CSS Animated Diagonal Section on Scroll"
section: "layouts"
category: "css-diagonal-sections"
category_name: "CSS Diagonal Sections"
description: "The angle itself animates: the band's cut steepens as the section scrolls into view and flattens as it leaves, driven by animation-timeline: view() where…"
has_js: "true"
---

Here's a working CSS Diagonal Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Animated Diagonal Section on Scroll
Source: https://codefronts.com/layouts/css-diagonal-sections/css-animated-diagonal-section-on-scroll/

The angle itself animates: the band's cut steepens as the section scrolls into view and flattens as it leaves, driven by animation-timeline: view() where that is supported and by a one-shot IntersectionObserver transition where it is not. Under prefers-reduced-motion the band renders at its final angle and nothing moves at all.
## HTML
```html
<div class="dgs-18" data-dgs-18>
  <input class="dgs-18__sronly" type="checkbox" id="dgs-18-dark">
  <label class="dgs-18__theme" for="dgs-18-dark">
    <svg class="dgs-18__i dgs-18__i--moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.3A8.4 8.4 0 0 1 9.7 3.5a8.5 8.5 0 1 0 10.8 10.8Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="dgs-18__i dgs-18__i--sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.1" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.7 5.7l1.4 1.4M16.9 16.9l1.4 1.4M18.3 5.7l-1.4 1.4M7.1 16.9l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <span class="dgs-18__srtext">Toggle dark theme</span>
  </label>
  <div class="dgs-18__stage">
    <section class="dgs-18__intro" aria-labelledby="dgs-18-a">
      <div class="dgs-18__wrap">
        <p class="dgs-18__eyebrow">Halfnight &mdash; 12 &amp; 13 June 2027</p>
        <h2 class="dgs-18__display" id="dgs-18-a">Two stages, one field, no clashes</h2>
        <p class="dgs-18__lede">Scroll down. The band below re-cuts its own edge from scroll progress, so the angle sharpens as it enters the viewport and settles once it is centred.</p>
        <p class="dgs-18__hint" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M12 4.5v14m0 0-5-5m5 5 5-5" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>
          Keep scrolling
        </p>
      </div>
    </section>

    <section class="dgs-18__band" aria-labelledby="dgs-18-b">
      <div class="dgs-18__wrap">
        <h2 class="dgs-18__h2" id="dgs-18-b">Saturday</h2>
        <ol class="dgs-18__lineup">
          <li><span>21:40</span><strong>Vela Ruin</strong><em>Main field</em></li>
          <li><span>20:10</span><strong>Kojima Twins</strong><em>Main field</em></li>
          <li><span>18:45</span><strong>Sable Hour</strong><em>The Barn</em></li>
          <li><span>17:20</span><strong>Petra Nils</strong><em>The Barn</em></li>
          <li><span>16:00</span><strong>Cold Marina</strong><em>Main field</em></li>
        </ol>
        <p class="dgs-18__progress"><span class="dgs-18__bar" aria-hidden="true"></span><span class="dgs-18__pct">Edge angle tracking scroll progress</span></p>
      </div>
    </section>

    <section class="dgs-18__after" aria-labelledby="dgs-18-c">
      <div class="dgs-18__wrap dgs-18__cols">
        <h2 class="dgs-18__h3" id="dgs-18-c">Scroll-driven, then static</h2>
        <p class="dgs-18__note">Where <code class="dgs-18__code">animation-timeline: view()</code> is supported the edge is animated entirely in CSS with no listener at all. Everywhere else a tiny observer writes a <code class="dgs-18__code">--p</code> value from 0 to 1 and the same declaration reads it. Reduced-motion visitors get the settled angle immediately.</p>
      </div>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Unbounded:wght@400;600;800&family=Space+Grotesk:wght@400;500&display=swap');

.dgs-18 {
  --p: 0;
  --cut: calc(clamp(1.5rem, 9vw, 9rem) * var(--p));
  --night: #120424;
  --night2: #1c0836;
  --on: #fbeeff;
  --dim: #b79ccd;
  --magenta: #ff2f87;
  --grape: #7a2bff;
  --amber: #ffbe3d;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  overflow-x: clip;
  background: var(--night);
  color: var(--on);
  font-family: 'Space Grotesk', system-ui, -apple-system, sans-serif;
  font-size: 16px;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}

.dgs-18 *,
.dgs-18 *::before,
.dgs-18 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.65 0.28 350)) {
  .dgs-18 {
    --night: oklch(0.17 0.08 305);
    --night2: oklch(0.23 0.11 305);
    --on: oklch(0.96 0.02 330);
    --dim: oklch(0.76 0.06 320);
    --magenta: oklch(0.66 0.26 353);
    --grape: oklch(0.52 0.27 293);
    --amber: oklch(0.83 0.15 78);
  }
}

.dgs-18__stage {
  display: flow-root;
}

.dgs-18__wrap {
  inline-size: min(72rem, 100%);
  margin-inline: auto;
}

.dgs-18__intro {
  position: relative;
  padding: clamp(4rem, 11vw, 8rem) clamp(1.25rem, 5vw, 4rem) clamp(6rem, 16vw, 12rem);
  background: radial-gradient(38rem 26rem at 18% 12%, rgba(122,43,255,.5), transparent 65%), radial-gradient(30rem 22rem at 88% 0%, rgba(255,47,135,.35), transparent 62%), var(--night);
}

.dgs-18__eyebrow {
  margin: 0 0 1.1rem;
  font-size: .74rem;
  font-weight: 500;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--amber);
}

.dgs-18__display {
  margin: 0 0 1.1rem;
  max-inline-size: 22ch;
  font-family: 'Unbounded', sans-serif;
  font-weight: 800;
  font-size: clamp(2.1rem, 7vw, 4.4rem);
  line-height: 1.0;
  letter-spacing: -.045em;
  text-wrap: balance;
}

.dgs-18__lede {
  margin: 0 0 2rem;
  max-inline-size: 50ch;
  font-size: clamp(1.02rem, 2.1vw, 1.2rem);
  color: var(--dim);
  text-wrap: pretty;
}

.dgs-18__hint {
  margin: 0;
  display: inline-flex;
  align-items: center;
  gap: .5rem;
  font-size: .82rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--dim);
}

.dgs-18__hint svg {
  inline-size: 1.1rem;
  block-size: 1.1rem;
  animation: dgs-18-nudge 1.8s ease-in-out infinite;
}

@keyframes dgs-18-nudge {
  50% {
    translate: 0 .3rem;
  }
}

.dgs-18__band {
  position: relative;
  z-index: 1;
  color: #14031f;
  background: linear-gradient(112deg, var(--magenta) 0%, var(--amber) 100%);
  clip-path: polygon(0 var(--cut), 100% 0, 100% 100%, 0 100%);
  margin-block-start: calc(var(--cut) * -1 - 1px);
  padding: calc(var(--cut) + clamp(2.5rem, 6vw, 4rem)) clamp(1.25rem, 5vw, 4rem) clamp(3rem, 7vw, 4.5rem);
}
/* The scroll-driven animation must target the property the clip-path
   actually reads. --cut is computed on the ROOT from --p, so animating
   --p on .dgs-18__band changed a value nothing downstream consumed —
   the band's own --p advanced to ~0.2 while the root stayed at 0, and
   the polygon rendered as a plain rectangle with no visible diagonal.
   Animating --cut on the band itself keeps the driver and the consumer
   on the same element. --p stays for the JS fallback and progress bar. */

@property --cut {
  syntax: '<length>';
  inherits: true;
  initial-value: 0px;
}

@supports (animation-timeline: view()) {
  .dgs-18__band {
    animation: dgs-18-cut linear both;
    animation-timeline: view();
    animation-range: entry 0% cover 45%;
  }

  @keyframes dgs-18-cut {
    from {
      --cut: 0px;
    }

    to {
      --cut: clamp(1.5rem, 9vw, 9rem);
    }
  }
}

@property --p {
  syntax: '<number>';
  inherits: true;
  initial-value: 0;
}

.dgs-18__h2 {
  margin: 0 0 1.5rem;
  font-family: 'Unbounded', sans-serif;
  font-weight: 800;
  font-size: clamp(1.8rem, 5.5vw, 3.2rem);
  letter-spacing: -.04em;
}

.dgs-18__lineup {
  list-style: none;
  margin: 0;
  padding: 0;
}

.dgs-18__lineup li {
  display: grid;
  gap: .2rem 1.25rem;
  grid-template-columns: 4.5rem minmax(0, 1fr) auto;
  align-items: baseline;
  padding-block: .85rem;
  border-block-start: 1px solid rgba(20,3,31,.25);
}

.dgs-18__lineup li:last-child {
  border-block-end: 1px solid rgba(20,3,31,.25);
}

.dgs-18__lineup span {
  font-family: ui-monospace, Menlo, monospace;
  font-size: .82rem;
  font-variant-numeric: tabular-nums;
  opacity: .7;
}

.dgs-18__lineup strong {
  font-family: 'Unbounded', sans-serif;
  font-weight: 600;
  font-size: clamp(1.05rem, 3vw, 1.5rem);
  letter-spacing: -.03em;
}

.dgs-18__lineup em {
  font-style: normal;
  font-size: .8rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  opacity: .65;
}

.dgs-18__progress {
  margin: 1.75rem 0 0;
  display: grid;
  gap: .5rem;
}

.dgs-18__bar {
  block-size: .35rem;
  border-radius: 999px;
  background: rgba(20,3,31,.22);
  overflow: clip;
}

.dgs-18__bar::after {
  content: '';
  display: block;
  block-size: 100%;
  inline-size: calc(var(--p) * 100%);
  background: #14031f;
  border-radius: 999px;
}

.dgs-18__pct {
  font-family: ui-monospace, Menlo, monospace;
  font-size: .7rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  opacity: .7;
}

.dgs-18__after {
  background: var(--night2);
  padding: clamp(3rem, 7vw, 4.5rem) clamp(1.25rem, 5vw, 4rem) clamp(5rem, 12vw, 8rem);
}

.dgs-18__cols {
  display: grid;
  gap: 1rem clamp(2rem, 6vw, 4rem);
  grid-template-columns: repeat(auto-fit, minmax(16rem, 1fr));
  align-items: start;
}

.dgs-18__h3 {
  margin: 0;
  font-family: 'Unbounded', sans-serif;
  font-weight: 600;
  font-size: clamp(1.25rem, 3.2vw, 1.8rem);
  letter-spacing: -.035em;
}

.dgs-18__note {
  margin: 0;
  max-inline-size: 58ch;
  color: var(--dim);
  text-wrap: pretty;
}

.dgs-18__code {
  font-family: ui-monospace, Menlo, monospace;
  font-size: .86em;
  padding: .1em .35em;
  border-radius: 4px;
  background: rgba(251,238,255,.12);
  color: var(--on);
}

@media (prefers-reduced-motion: reduce) {
  .dgs-18 {
    --p: 1;
  }

  .dgs-18 *,
    .dgs-18 *::after {
    transition: none !important;
    animation: none !important;
  }

  .dgs-18__band {
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .dgs-18__band {
    forced-color-adjust: none;
    background: Canvas;
    color: CanvasText;
    border-block-start: 1px solid CanvasText;
  }
}
/* Standard top-right theme toggle — pure CSS (checkbox + :has()), so demos
   that ship no script stay tagged Pure CSS. Placed on the root rather than
   inside a demo's own control panel so every demo exposes it in one place. */

.dgs-18__sronly,
.dgs-18__srtext {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.dgs-18__theme {
  position: absolute;
  inset-block-start: clamp(.85rem, 2.2vw, 1.5rem);
  inset-inline-end: clamp(.85rem, 2.2vw, 1.5rem);
  z-index: 60;
  display: grid;
  place-items: center;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  border-radius: 999px;
  border: 1px solid currentColor;
  color: inherit;
  background: rgba(127,127,127,.16);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  cursor: pointer;
  transition: translate .2s ease;
}

.dgs-18__theme:hover {
  translate: 0 -1px;
}

.dgs-18__sronly:focus-visible + .dgs-18__theme {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.dgs-18__i {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.dgs-18__i--sun {
  display: none;
}

.dgs-18:has(#dgs-18-dark:checked) .dgs-18__i--moon {
  display: none;
}

.dgs-18:has(#dgs-18-dark:checked) .dgs-18__i--sun {
  display: block;
}

.dgs-18:has(#dgs-18-dark:checked) {
  --night: #f3f5f8;
  --ink: #0b0e14;
  --muted: #5a616c;
  --line: rgba(11,14,20,.15);
}

@media (prefers-reduced-motion: reduce) {
  .dgs-18__theme {
    transition: none;
  }
}

@media (forced-colors: active) {
  .dgs-18__theme {
    border-color: CanvasText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('[data-dgs-18]');
  if (!root) return;
  const band = root.querySelector('.dgs-18__band');
  if (!band) return;
  const still = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const native = CSS.supports('animation-timeline', 'view()');
  if (still) { root.style.setProperty('--p', '1'); return; }
  if (native) return;
  let queued = false;
  const write = () => {
    queued = false;
    const r = band.getBoundingClientRect();
    const vh = window.innerHeight || 1;
    const p = 1 - Math.min(1, Math.max(0, (r.top - vh * 0.15) / (vh * 0.85)));
    root.style.setProperty('--p', p.toFixed(3));
  };
  const onScroll = () => { if (!queued) { queued = true; requestAnimationFrame(write); } };
  addEventListener('scroll', onScroll, { passive: true });
  addEventListener('resize', onScroll);
  write();
})();
```
