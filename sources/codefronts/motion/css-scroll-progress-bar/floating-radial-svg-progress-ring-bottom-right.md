---
source: "codefronts"
url: "https://codefronts.com/motion/css-scroll-progress-bar/floating-radial-svg-progress-ring-bottom-right/"
title: "Floating Radial SVG Progress Ring (Bottom-Right)"
section: "motion"
category: "css-scroll-progress-bar"
category_name: "CSS Scroll Progress Bar"
description: "A 56px ring that hovers in the bottom-right corner and closes as the reader descends — the indicator of choice when the top of the page is already crowded…"
has_js: "true"
---

Here's a working CSS Scroll Progress Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Floating Radial SVG Progress Ring (Bottom-Right)
Source: https://codefronts.com/motion/css-scroll-progress-bar/floating-radial-svg-progress-ring-bottom-right/

A 56px ring that hovers in the bottom-right corner and closes as the reader descends — the indicator of choice when the top of the page is already crowded with a header, a breadcrumb and an announcement bar. Built on the pathLength="1" trick so the maths is literally 0→1, with a conic-gradient variant for teams who would rather not ship an SVG at all.
## HTML
```html
<section class="sp-03" aria-label="Floating radial SVG scroll progress ring demo">
  <div class="sp-03__dock" aria-hidden="false">
    <div class="sp-03__ring" role="progressbar" aria-label="Page scrolled" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0" id="sp-03-ring">
      <svg class="sp-03__svg" viewBox="0 0 56 56" aria-hidden="true" focusable="false">
        <circle class="sp-03__track" cx="28" cy="28" r="24" pathLength="1"></circle>
        <circle class="sp-03__value" cx="28" cy="28" r="24" pathLength="1"></circle>
      </svg>
      <span class="sp-03__num" id="sp-03-num">0</span>
    </div>
    <p class="sp-03__docklab">scrolled</p>
  </div>
  <header class="sp-03__bar">
    <a class="sp-03__brand" href="#sp-03-s1"><span class="sp-03__logo" aria-hidden="true"></span>Radial</a>
    <p class="sp-03__meta">pathLength = 1</p>
  </header>
  <div class="sp-03__intro">
    <div class="sp-03__introin">
      <p class="sp-03__intro-eyebrow">stroke-dashoffset · scroll()</p>
      <h2 class="sp-03__intro-title">A ring that closes as you read</h2>
      <p class="sp-03__intro-sub">Bottom-right, thumb-reachable, notch-safe. Scroll and watch the arc complete — no circumference maths anywhere in the code.</p>
    </div>
  </div>
  <main class="sp-03__main">
    <section class="sp-03__sec" id="sp-03-s1">
      <p class="sp-03__kicker">Geometry</p>
      <h3 class="sp-03__h">Let SVG do the maths</h3>
      <p class="sp-03__p sp-03__p--lede">Declare <code>pathLength="1"</code> and the circle's real circumference stops mattering. A dash offset of 1 is empty, 0 is full, and the radius becomes a pure design decision.</p>
    </section>
    <section class="sp-03__sec" id="sp-03-s2">
      <p class="sp-03__kicker">Placement</p>
      <h3 class="sp-03__h">The thumb zone is not decoration</h3>
      <p class="sp-03__p">Bottom-right on a phone is the cheapest pixel to reach. The dock pads itself with <code>max(20px, env(safe-area-inset-bottom))</code>, so the ring never hides under a home indicator.</p>
      <figure class="sp-03__fig">
        <img class="sp-03__img" src="https://images.unsplash.com/photo-1522199755839-a2bacb67c546?auto=format&amp;fit=crop&amp;w=1400&amp;q=70" alt="A workspace with a laptop, notebook and coffee on a wooden desk" loading="lazy" decoding="async">
        <figcaption class="sp-03__cap">Corner indicators survive dense headers — nothing above the fold has to move.</figcaption>
      </figure>
    </section>
    <section class="sp-03__sec" id="sp-03-s3">
      <p class="sp-03__kicker">No-SVG variant</p>
      <h3 class="sp-03__h">conic-gradient plus a mask</h3>
      <p class="sp-03__p">One <code>&lt;div&gt;</code>, a conic fill to <code>calc(var(--p) * 360deg)</code> and a radial mask punching out the middle. Identical result with zero SVG — the edge is a hair softer, which nobody has ever noticed at 56px.</p>
      <div class="sp-03__demo2"><div class="sp-03__conic" id="sp-03-conic" aria-hidden="true"></div><p class="sp-03__demo2p">Live conic variant, same <code>--sp-03-p</code> source.</p></div>
    </section>
    <section class="sp-03__sec" id="sp-03-s4">
      <p class="sp-03__kicker">Pointer safety</p>
      <h3 class="sp-03__h">Never eat a tap</h3>
      <p class="sp-03__p">The dock is <code>pointer-events:none</code>; only the ring itself can receive input. A floating indicator that blocks a link behind it is a bug report waiting to happen.</p>
      <p class="sp-03__chip">56px ring · 2 circles · 1 keyframe</p>
    </section>
  </main>
  <footer class="sp-03__pagefoot"><p class="sp-03__pagefootin">Scroll progress pattern 03 of 18 · codefronts.com</p></footer>
</section>
```
## CSS
```css
.sp-03 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--sp-03-bg);
  --sp-03-bg: oklch(0.975 0.01 160);
  --sp-03-surface: oklch(1 0 0);
  --sp-03-ink: oklch(0.21 0.03 175);
  --sp-03-mut: oklch(0.52 0.02 175);
  --sp-03-acc: oklch(0.62 0.15 175);
  --sp-03-acc2: oklch(0.7 0.16 145);
  --sp-03-line: oklch(0.21 0.03 175/.11);
  --sp-03-size: 56px;
  --sp-03-stroke: 5px;
  --sp-03-p: 0;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--sp-03-ink);
  -webkit-font-smoothing: antialiased;
}

.sp-03 *,
.sp-03 *::before,
.sp-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sp-03__dock {
  position: fixed;
  inset-block-end: max(20px,env(safe-area-inset-bottom));
  inset-inline-end: max(20px,env(safe-area-inset-right));
  z-index: 60;
  display: grid;
  justify-items: center;
  gap: 6px;
  pointer-events: none;
}

.sp-03__ring {
  position: relative;
  inline-size: var(--sp-03-size);
  block-size: var(--sp-03-size);
  display: grid;
  place-items: center;
  border-radius: 50%;
  background: color-mix(in oklch,var(--sp-03-surface) 86%,transparent);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  box-shadow: 0 10px 26px -12px oklch(0.21 0.03 175/.5),0 0 0 1px var(--sp-03-line);
}

.sp-03__svg {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  transform: rotate(-90deg);
  overflow: visible;
}

.sp-03__track,
.sp-03__value {
  fill: none;
  stroke-width: var(--sp-03-stroke);
  stroke-linecap: round;
}

.sp-03__track {
  stroke: color-mix(in oklch,var(--sp-03-acc) 18%,transparent);
}

.sp-03__value {
  stroke: url(#sp-03-grad);
  stroke: var(--sp-03-acc);
  stroke-dasharray: 1;
  stroke-dashoffset: calc(1 - var(--sp-03-p));
  filter: drop-shadow(0 0 5px color-mix(in oklch,var(--sp-03-acc) 55%,transparent));
}

@supports (animation-timeline: scroll()) {
  .sp-03__value {
    stroke-dashoffset: 1;
    animation: sp-03-ring linear both;
    animation-timeline: scroll(root block);
  }
}

@keyframes sp-03-ring {
  from {
    stroke-dashoffset: 1;
  }

  to {
    stroke-dashoffset: 0;
  }
}

.sp-03__num {
  position: relative;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 13px;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
  color: var(--sp-03-ink);
}

.sp-03__num::after {
  content: "%";
  font-size: 9px;
  opacity: .6;
  margin-inline-start: 1px;
}

.sp-03__docklab {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 9.5px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--sp-03-mut);
  opacity: .8;
}

.sp-03__bar {
  position: sticky;
  inset-block-start: 0;
  z-index: 40;
  display: flex;
  align-items: center;
  gap: 14px;
  min-block-size: 58px;
  background: color-mix(in oklch,var(--sp-03-surface) 80%,transparent);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border-block-end: 1px solid var(--sp-03-line);
}

.sp-03__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 15px;
  font-weight: 730;
  letter-spacing: -.02em;
  color: inherit;
  text-decoration: none;
}

.sp-03__brand:focus-visible {
  outline: 2px solid var(--sp-03-acc);
  outline-offset: 3px;
  border-radius: 6px;
}

.sp-03__logo {
  inline-size: 18px;
  block-size: 18px;
  border-radius: 50%;
  border: 4px solid var(--sp-03-acc);
  border-block-start-color: transparent;
}

.sp-03__meta {
  margin-inline-start: auto;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--sp-03-mut);
}

.sp-03__intro {
  display: grid;
  place-items: center;
  min-block-size: min(86svh,820px);
  padding-block: clamp(56px,12vh,140px) clamp(40px,8vh,90px);
  background: radial-gradient(88% 58% at 50% 0%,oklch(0.98 0.05 168),transparent);
}

.sp-03__introin {
  display: grid;
  justify-items: center;
  gap: clamp(12px,1.8vw,18px);
  text-align: center;
  max-inline-size: 28ch;
}

.sp-03__intro-eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: clamp(11px,1.1vw,13px);
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--sp-03-acc);
}

.sp-03__intro-title {
  font-size: clamp(36px,6.8vw,78px);
  line-height: 1;
  letter-spacing: -.04em;
  font-weight: 730;
  text-wrap: balance;
}

.sp-03__intro-sub {
  font-size: clamp(15px,1.7vw,19px);
  line-height: 1.55;
  color: var(--sp-03-mut);
  max-inline-size: 46ch;
  text-wrap: pretty;
}

.sp-03__sec {
  scroll-margin-top: 72px;
  display: grid;
  gap: 12px;
  align-content: center;
  min-block-size: 72svh;
  padding-block: clamp(28px,5vw,56px);
  border-block-end: 1px solid var(--sp-03-line);
}

.sp-03__sec:last-child {
  border-block-end: 0;
}

.sp-03__kicker {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--sp-03-acc);
}

.sp-03__h {
  font-size: clamp(22px,3.2vw,34px);
  line-height: 1.1;
  letter-spacing: -.032em;
  font-weight: 700;
  text-wrap: balance;
}

.sp-03__p {
  max-inline-size: 60ch;
  font-size: 15.8px;
  line-height: 1.7;
  color: var(--sp-03-mut);
  text-wrap: pretty;
}

.sp-03__p--lede {
  font-size: 18px;
  color: var(--sp-03-ink);
}

.sp-03__p code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .85em;
  background: oklch(0.21 0.03 175/.07);
  padding: 2px 6px;
  border-radius: 5px;
}

.sp-03__fig {
  display: grid;
  gap: 9px;
  max-inline-size: 70ch;
}

.sp-03__img {
  inline-size: 100%;
  aspect-ratio: 16/7;
  object-fit: cover;
  display: block;
  border-radius: 16px;
  background: linear-gradient(135deg,oklch(0.62 0.1 160),oklch(0.4 0.06 200));
}

.sp-03__cap {
  font-size: 12.6px;
  color: var(--sp-03-mut);
}

.sp-03__demo2 {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 16px;
  border: 1px solid var(--sp-03-line);
  border-radius: 16px;
  background: var(--sp-03-surface);
  max-inline-size: 52ch;
}

.sp-03__conic {
  inline-size: 52px;
  block-size: 52px;
  border-radius: 50%;
  flex: none;
  background: conic-gradient(var(--sp-03-acc2) calc(var(--sp-03-p) * 360deg),color-mix(in oklch,var(--sp-03-acc2) 15%,transparent) 0);
  -webkit-mask: radial-gradient(closest-side,transparent 68%,#000 69%);
  mask: radial-gradient(closest-side,transparent 68%,#000 69%);
}

.sp-03__demo2p {
  font-size: 13.6px;
  line-height: 1.55;
  color: var(--sp-03-mut);
}

.sp-03__chip {
  justify-self: start;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--sp-03-acc);
  padding: 7px 13px;
  border-radius: 99px;
  background: color-mix(in oklch,var(--sp-03-acc) 10%,transparent);
  border: 1px solid color-mix(in oklch,var(--sp-03-acc) 24%,transparent);
}

.sp-03__pagefoot {
  display: grid;
  place-items: center;
  padding: clamp(44px,9vh,110px) 24px;
  border-block-start: 1px solid var(--sp-03-line);
}

.sp-03__pagefootin {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  letter-spacing: .06em;
  color: var(--sp-03-mut);
  text-align: center;
}

.sp-03__bar {
  padding-inline: max(clamp(16px,3vw,26px),calc((100% - 1180px)/2));
}

.sp-03__intro,
.sp-03__sec {
  padding-inline: max(clamp(22px,5vw,44px),calc((100% - 900px)/2));
}

:root:has(.sp-03) {
  scroll-behavior: smooth;
  scroll-padding-top: 72px;
}

@media (max-width: 640px) {
  .sp-03 {
    --sp-03-size: 50px;
  }

  .sp-03__sec {
    min-block-size: auto;
  }

  .sp-03__docklab {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  :root:has(.sp-03) {
    scroll-behavior: auto;
  }

  .sp-03__value {
    filter: none;
  }

  .sp-03 * {
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sp-03');
  if (!root || root.dataset.spWired) return;
  root.dataset.spWired = '1';
  const ring = root.querySelector('#sp-03-ring');
  const num = root.querySelector('#sp-03-num');
  const native = CSS.supports('animation-timeline', 'scroll()');
  let ticking = false;
  const paint = () => {
    ticking = false;
    const d = document.documentElement;
    const max = d.scrollHeight - d.clientHeight;
    const p = max > 0 ? Math.min(1, Math.max(0, d.scrollTop / max)) : 0;
    // the conic variant always reads the property; the SVG only needs it without native support
    root.style.setProperty('--sp-03-p', p.toFixed(4));
    if (native) root.querySelector('.sp-03__value').style.removeProperty('stroke-dashoffset');
    const n = Math.round(p * 100);
    num.textContent = String(n);
    ring.setAttribute('aria-valuenow', String(n));
  };
  const onScroll = () => { if (!ticking) { ticking = true; requestAnimationFrame(paint); } };
  addEventListener('scroll', onScroll, { passive: true });
  addEventListener('resize', onScroll, { passive: true });
  paint();
})();
```
