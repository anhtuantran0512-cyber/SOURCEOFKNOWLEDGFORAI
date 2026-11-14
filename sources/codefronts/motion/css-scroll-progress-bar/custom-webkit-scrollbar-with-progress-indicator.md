---
source: "codefronts"
url: "https://codefronts.com/motion/css-scroll-progress-bar/custom-webkit-scrollbar-with-progress-indicator/"
title: "Custom ::-webkit-scrollbar with Progress Indicator"
section: "motion"
category: "css-scroll-progress-bar"
category_name: "CSS Scroll Progress Bar"
description: "Two scrollbar systems exist and neither is going away: WebKit's shadow pseudo-elements and the standard scrollbar-width/scrollbar-color pair."
has_js: "true"
---

Here's a working CSS Scroll Progress Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Custom ::-webkit-scrollbar with Progress Indicator
Source: https://codefronts.com/motion/css-scroll-progress-bar/custom-webkit-scrollbar-with-progress-indicator/

Two scrollbar systems exist and neither is going away: WebKit's shadow pseudo-elements and the standard scrollbar-width/scrollbar-color pair. This demo ships both correctly — then shows why the popular 'fill the scrollbar track with a gradient' trick cannot work (backgrounds stop at the padding box) and replaces it with a six-pixel gauge that reads the panel's own scroll timeline.
## HTML
```html
<section class="sp-15" aria-label="Custom scrollbar with progress indicator demo">
  <header class="sp-15__bar">
    <a class="sp-15__brand" href="#sp-15-box"><span class="sp-15__logo" aria-hidden="true"></span>Gutter</a>
    <p class="sp-15__meta">::-webkit-scrollbar + scrollbar-color</p>
  </header>
  <div class="sp-15__intro">
    <p class="sp-15__intro-eyebrow">two systems, both required</p>
    <h2 class="sp-15__intro-title">A scrollbar that doubles as a progress bar</h2>
    <p class="sp-15__intro-sub">Scroll inside the panel. The scrollbar is styled in both systems, and the six-pixel gauge beside it reads the panel's own scroll timeline.</p>
  </div>
  <div class="sp-15__stage">
    <div class="sp-15__boxwrap">
    <div class="sp-15__box" id="sp-15-box" tabindex="0" role="region" aria-label="Release notes, scrollable">
      <p class="sp-15__lede">Release notes · v4.2</p>
      <h4 class="sp-15__sh">Standard first</h4>
      <p class="sp-15__bp"><code>scrollbar-width</code> and <code>scrollbar-color</code> are the interoperable properties. They are coarse — three widths and two colours — but they are honoured by Firefox and increasingly by everyone else.</p>
      <h4 class="sp-15__sh">WebKit for the detail</h4>
      <p class="sp-15__bp">Radii, gradients, inset padding and hover growth all live in the pseudo-elements. Layer them on top rather than instead.</p>
      <h4 class="sp-15__sh">The inset thumb trick</h4>
      <p class="sp-15__bp">A transparent border plus <code>background-clip: content-box</code> is how the thumb appears to float inside the track. The border reserves space the background never paints into.</p>
      <h4 class="sp-15__sh">The progress layer</h4>
      <p class="sp-15__bp">You cannot paint it inside the scrollbar. A background's positioning area stops at the padding box, so a gradient at <code>right top</code> lands under the text padding — and overlay or 2px scrollbars leave nothing to see through. The gauge to the right is a real element on this panel's named timeline.</p>
      <h4 class="sp-15__sh">Gutter stability</h4>
      <p class="sp-15__bp"><code>scrollbar-gutter: stable</code> reserves the space up front so text does not reflow the moment content grows past one screen.</p>
      <h4 class="sp-15__sh">Never hide it</h4>
      <p class="sp-15__bp">A hidden scrollbar removes the only cue that content continues and takes away a drag target some users depend on. Hide it only where another indicator exists.</p>
      <h4 class="sp-15__sh">Grab size</h4>
      <p class="sp-15__bp">Below roughly 8 by 24 pixels a thumb stops being grabbable. Thin is a style; invisible is a bug.</p>
      <h4 class="sp-15__sh">Platform truth</h4>
      <p class="sp-15__bp">iOS draws overlay scrollbars at the system level and ignores your styling entirely. Treat scrollbar design as decoration, never as the only signal.</p>
      <p class="sp-15__end">End of notes — the gauge beside the scrollbar is now full.</p>
    </div>
    <div class="sp-15__gauge" role="progressbar" aria-label="Release notes read" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0" id="sp-15-gauge"><i class="sp-15__gfill"></i></div>
    </div>
    <div class="sp-15__legend">
      <p class="sp-15__lrow"><span class="sp-15__sw sp-15__sw--thumb"></span><span>Thumb · <code>scrollbar-color</code> arg 1</span></p>
      <p class="sp-15__lrow"><span class="sp-15__sw sp-15__sw--track"></span><span>Gauge · a real element, bound to the panel's named scroll timeline</span></p>
      <p class="sp-15__lrow"><span class="sp-15__sw sp-15__sw--gut"></span><span>Gutter · reserved by <code>scrollbar-gutter</code></span></p>
    </div>
  </div>
  <section class="sp-15__notes">
    <p class="sp-15__kicker">Coverage</p>
    <h3 class="sp-15__h">Write both, always — and don't trust either for meaning</h3>
    <p class="sp-15__p">WebKit pseudo-elements will never land in Firefox, and the standard properties cannot express a gradient thumb. Shipping only one leaves a large slice of users with a bar that does not match the design — and iOS ignores both, drawing its own overlay bar. Anything that has to <em>communicate</em> position belongs in an element you control.</p>
    <p class="sp-15__chip">2 systems · 1 gauge · 0 hidden scrollbars</p>
  </section>
  <footer class="sp-15__pagefoot"><p class="sp-15__pagefootin">Scroll progress pattern 15 of 18 · codefronts.com</p></footer>
</section>
```
## CSS
```css
.sp-15 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--sp-15-bg);
  --sp-15-bg: oklch(0.16 0.014 275);
  --sp-15-surface: oklch(0.21 0.018 275);
  --sp-15-ink: oklch(0.97 0.004 275);
  --sp-15-mut: oklch(0.72 0.016 275);
  --sp-15-acc: oklch(0.74 0.15 100);
  --sp-15-track: oklch(1 0 0/.08);
  --sp-15-line: oklch(1 0 0/.12);
  --sp-15-p: 0;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--sp-15-ink);
  -webkit-font-smoothing: antialiased;
}

.sp-15 *,
.sp-15 *::before,
.sp-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sp-15__bar {
  position: sticky;
  inset-block-start: 0;
  z-index: 40;
  display: flex;
  align-items: center;
  gap: 14px;
  min-block-size: 58px;
  background: color-mix(in oklch,var(--sp-15-bg) 78%,transparent);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border-block-end: 1px solid var(--sp-15-line);
}

.sp-15__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 15px;
  font-weight: 730;
  letter-spacing: -.02em;
  color: inherit;
  text-decoration: none;
}

.sp-15__brand:focus-visible {
  outline: 2px solid var(--sp-15-acc);
  outline-offset: 3px;
  border-radius: 6px;
}

.sp-15__logo {
  inline-size: 7px;
  block-size: 20px;
  border-radius: 99px;
  background: linear-gradient(180deg,var(--sp-15-acc),oklch(0.6 0.16 140));
}

.sp-15__meta {
  margin-inline-start: auto;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .06em;
  color: var(--sp-15-mut);
}

.sp-15__intro {
  display: grid;
  gap: 14px;
  padding-block: clamp(44px,10vh,110px) clamp(22px,5vh,46px);
}

.sp-15__intro-eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--sp-15-acc);
}

.sp-15__intro-title {
  font-size: clamp(30px,5.4vw,62px);
  line-height: 1;
  letter-spacing: -.04em;
  font-weight: 730;
  max-inline-size: 18ch;
  text-wrap: balance;
}

.sp-15__intro-sub {
  font-size: clamp(14.5px,1.6vw,18px);
  line-height: 1.55;
  color: var(--sp-15-mut);
  max-inline-size: 54ch;
  text-wrap: pretty;
}

.sp-15__stage {
  display: grid;
  grid-template-columns: minmax(0,1fr) minmax(200px,250px);
  gap: clamp(16px,3vw,32px);
  align-items: start;
  padding-block-end: clamp(30px,6vh,64px);
}

.sp-15__boxwrap {
  position: relative;
  timeline-scope: --sp-15-tl;
  padding-inline-end: 18px;
}

.sp-15__gauge {
  position: absolute;
  inset-block: 8px;
  inset-inline-end: 0;
  inline-size: 6px;
  border-radius: 99px;
  background: var(--sp-15-track);
  box-shadow: inset 0 0 0 1px var(--sp-15-line);
  overflow: hidden;
  pointer-events: none;
}

.sp-15__gfill {
  display: block;
  inline-size: 100%;
  block-size: 100%;
  transform-origin: 50% 0;
  transform: scaleY(var(--sp-15-p));
  border-radius: 99px;
  background: linear-gradient(180deg,var(--sp-15-acc),oklch(0.62 0.16 140));
}

.sp-15__box {
  block-size: min(62svh,520px);
  overflow-y: auto;
  overscroll-behavior: contain;
  scrollbar-gutter: stable;
  scrollbar-width: thin;
  scrollbar-color: var(--sp-15-acc) var(--sp-15-track);
  padding: 20px clamp(16px,3vw,26px);
  border: 1px solid var(--sp-15-line);
  border-radius: 16px;
  background: var(--sp-15-surface);
  display: grid;
  gap: 11px;
  align-content: start;
}

@supports (animation-timeline: scroll()) {
  .sp-15__box {
    scroll-timeline-name: --sp-15-tl;
    scroll-timeline-axis: block;
  }

  .sp-15__gfill {
    animation: sp-15-track linear;
    animation-timeline: --sp-15-tl;
  }
}

@keyframes sp-15-track {
  from {
    transform: scaleY(0);
  }

  to {
    transform: scaleY(1);
  }
}

.sp-15__box::-webkit-scrollbar {
  inline-size: 12px;
}

.sp-15__box::-webkit-scrollbar-track {
  background: transparent;
}

.sp-15__box::-webkit-scrollbar-thumb {
  border-radius: 99px;
  background: linear-gradient(180deg,var(--sp-15-acc),oklch(0.62 0.16 140));
  background-clip: content-box;
  border: 3px solid transparent;
  transition: background .2s ease;
}

.sp-15__box::-webkit-scrollbar-thumb:hover {
  background: oklch(0.82 0.16 100);
  background-clip: content-box;
}

.sp-15__box:focus-visible {
  outline: 2px solid var(--sp-15-acc);
  outline-offset: -2px;
}

.sp-15__lede {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--sp-15-acc);
}

.sp-15__sh {
  margin-block-start: 7px;
  font-size: 14.6px;
  font-weight: 700;
  letter-spacing: -.015em;
}

.sp-15__bp {
  font-size: 14.6px;
  line-height: 1.68;
  color: var(--sp-15-mut);
  text-wrap: pretty;
  max-inline-size: 62ch;
}

.sp-15__bp code,
.sp-15__p code,
.sp-15__lrow code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .85em;
  background: oklch(1 0 0/.1);
  padding: 2px 6px;
  border-radius: 5px;
}

.sp-15__end {
  margin-block-start: 8px;
  padding: 11px 13px;
  border-radius: 11px;
  font-size: 13.6px;
  color: var(--sp-15-acc);
  background: color-mix(in oklch,var(--sp-15-acc) 12%,transparent);
  border: 1px solid color-mix(in oklch,var(--sp-15-acc) 26%,transparent);
}

.sp-15__legend {
  display: grid;
  gap: 11px;
  padding: 16px;
  border: 1px solid var(--sp-15-line);
  border-radius: 16px;
  background: color-mix(in oklch,var(--sp-15-surface) 70%,transparent);
}

.sp-15__lrow {
  display: grid;
  grid-template-columns: auto minmax(0,1fr);
  gap: 9px;
  align-items: start;
  font-size: 12.6px;
  line-height: 1.5;
  color: var(--sp-15-mut);
}

.sp-15__sw {
  inline-size: 14px;
  block-size: 14px;
  border-radius: 5px;
  flex: none;
  margin-block-start: 3px;
}

.sp-15__sw--thumb {
  background: linear-gradient(180deg,var(--sp-15-acc),oklch(0.62 0.16 140));
}

.sp-15__sw--track {
  background: linear-gradient(180deg,var(--sp-15-acc),var(--sp-15-track));
  border: 1px solid var(--sp-15-line);
}

.sp-15__sw--gut {
  background: repeating-linear-gradient(45deg,oklch(1 0 0/.14) 0 3px,transparent 3px 6px);
}

.sp-15__notes {
  display: grid;
  gap: 12px;
  padding-block: clamp(28px,5vh,56px);
}

.sp-15__kicker {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--sp-15-acc);
}

.sp-15__h {
  font-size: clamp(21px,3vw,31px);
  line-height: 1.12;
  letter-spacing: -.032em;
  font-weight: 700;
  text-wrap: balance;
}

.sp-15__p {
  max-inline-size: 62ch;
  font-size: 15.6px;
  line-height: 1.7;
  color: var(--sp-15-mut);
  text-wrap: pretty;
}

.sp-15__chip {
  justify-self: start;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--sp-15-acc);
  padding: 7px 13px;
  border-radius: 99px;
  background: color-mix(in oklch,var(--sp-15-acc) 14%,transparent);
  border: 1px solid color-mix(in oklch,var(--sp-15-acc) 30%,transparent);
}

.sp-15__pagefoot {
  display: grid;
  place-items: center;
  padding: clamp(40px,8vh,100px) 24px;
  border-block-start: 1px solid var(--sp-15-line);
}

.sp-15__pagefootin {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  letter-spacing: .06em;
  color: var(--sp-15-mut);
  text-align: center;
}

.sp-15__bar,
.sp-15__intro,
.sp-15__stage,
.sp-15__notes {
  padding-inline: max(clamp(18px,4vw,36px),calc((100% - 1060px)/2));
}

@media (max-width: 800px) {
  .sp-15__stage {
    grid-template-columns: minmax(0,1fr);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sp-15 * {
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sp-15');
  if (!root || root.dataset.spWired) return;
  root.dataset.spWired = '1';
  const box = root.querySelector('#sp-15-box');
  const gauge = root.querySelector('#sp-15-gauge');
  let ticking = false;
  const paint = () => {
    ticking = false;
    const max = box.scrollHeight - box.clientHeight;
    const p = max > 0 ? Math.min(1, Math.max(0, box.scrollTop / max)) : 0;
    root.style.setProperty('--sp-15-p', p.toFixed(4));
    gauge.setAttribute('aria-valuenow', String(Math.round(p * 100)));
  };
  box.addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(paint); } }, { passive: true });
  addEventListener('resize', () => { if (!ticking) { ticking = true; requestAnimationFrame(paint); } }, { passive: true });
  paint();
})();
```
