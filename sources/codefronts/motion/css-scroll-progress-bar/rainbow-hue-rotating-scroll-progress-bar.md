---
source: "codefronts"
url: "https://codefronts.com/motion/css-scroll-progress-bar/rainbow-hue-rotating-scroll-progress-bar/"
title: "Rainbow Hue-Rotating Scroll Progress Bar"
section: "motion"
category: "css-scroll-progress-bar"
category_name: "CSS Scroll Progress Bar"
description: "The bar starts red and walks the entire colour wheel by the time you reach the footer — so the hue itself encodes position."
has_js: "true"
---

Here's a working CSS Scroll Progress Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Rainbow Hue-Rotating Scroll Progress Bar
Source: https://codefronts.com/motion/css-scroll-progress-bar/rainbow-hue-rotating-scroll-progress-bar/

The bar starts red and walks the entire colour wheel by the time you reach the footer — so the hue itself encodes position. Two implementations sit side by side: a registered <angle> property fed straight into oklch() (precise, perceptually even, controllable) and a one-line filter: hue-rotate() (cheap, blunt, works on anything).
## HTML
```html
<section class="sp-16" aria-label="Rainbow hue-rotating scroll progress bar demo">
  <div class="sp-16__rail" role="progressbar" aria-label="Reading progress" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0" id="sp-16-rail"><i class="sp-16__fill"></i></div>
  <header class="sp-16__bar">
    <a class="sp-16__brand" href="#sp-16-s1"><span class="sp-16__logo" aria-hidden="true"></span>Prism</a>
    <p class="sp-16__meta">--hue: 0deg → 360deg</p>
  </header>
  <div class="sp-16__intro">
    <p class="sp-16__intro-eyebrow">colour as position</p>
    <h2 class="sp-16__intro-title">Walk the whole wheel</h2>
    <p class="sp-16__intro-sub">The bar at the top rotates a registered angle straight into the hue channel. The pair below shows the same scroll driving both implementations.</p>
    <div class="sp-16__compare">
      <div class="sp-16__cmp"><p class="sp-16__cmplab">oklch hue channel</p><div class="sp-16__cbar"><i class="sp-16__cfill sp-16__cfill--ok"></i></div></div>
      <div class="sp-16__cmp"><p class="sp-16__cmplab">filter: hue-rotate()</p><div class="sp-16__cbar"><i class="sp-16__cfill sp-16__cfill--filter"></i></div></div>
    </div>
  </div>
  <main class="sp-16__main">
    <section class="sp-16__sec" id="sp-16-s1">
      <p class="sp-16__kicker">Precision</p>
      <h3 class="sp-16__h">Even brightness across the wheel</h3>
      <p class="sp-16__p sp-16__p--lede">An HSL rainbow dims through blue and glares through yellow because HSL lightness is a maths convenience, not a perceptual measure. In oklch, lightness holds while the hue travels.</p>
    </section>
    <section class="sp-16__sec" id="sp-16-s2">
      <p class="sp-16__kicker">Bluntness</p>
      <h3 class="sp-16__h">What hue-rotate actually does</h3>
      <p class="sp-16__p">It is a pixel filter over the whole element — glow, shadow and any text inside come along for the ride. Excellent for a decorative strip, wrong for anything containing brand colour.</p>
    </section>
    <section class="sp-16__sec" id="sp-16-s3">
      <p class="sp-16__kicker">Trap</p>
      <h3 class="sp-16__h">filter creates a containing block</h3>
      <p class="sp-16__p">A <code>position:fixed</code> child inside a filtered wrapper positions against that wrapper rather than the viewport. It is the kind of bug that costs an afternoon.</p>
    </section>
    <section class="sp-16__sec" id="sp-16-s4">
      <p class="sp-16__kicker">Restraint</p>
      <h3 class="sp-16__h">Colour is never the message</h3>
      <p class="sp-16__p">Hue is invisible to a meaningful share of users and to anyone not looking at it. The bar's length carries the information; the rainbow is a flourish that freezes under reduced motion.</p>
      <p class="sp-16__chip">1 registered angle · 2 implementations</p>
    </section>
  </main>
  <footer class="sp-16__pagefoot"><p class="sp-16__pagefootin">Scroll progress pattern 16 of 18 · codefronts.com</p></footer>
</section>
```
## CSS
```css
@property --sp-16-hue {
  syntax: "<angle>";
  inherits: true;
  initial-value: 20deg;
}

.sp-16 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--sp-16-bg);
  --sp-16-bg: oklch(0.15 0.016 280);
  --sp-16-surface: oklch(0.2 0.02 280);
  --sp-16-ink: oklch(0.97 0.005 280);
  --sp-16-mut: oklch(0.72 0.018 280);
  --sp-16-acc: oklch(0.75 0.19 var(--sp-16-hue));
  --sp-16-line: oklch(1 0 0/.12);
  --sp-16-p: 0;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--sp-16-ink);
  -webkit-font-smoothing: antialiased;
}

.sp-16 *,
.sp-16 *::before,
.sp-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sp-16__rail {
  position: fixed;
  inset-block-start: 0;
  inset-inline: 0;
  block-size: 6px;
  z-index: 60;
  background: oklch(1 0 0/.08);
  pointer-events: none;
}

.sp-16__fill {
  display: block;
  block-size: 100%;
  transform-origin: 0 50%;
  transform: scaleX(var(--sp-16-p));
  background: linear-gradient(90deg,oklch(0.72 0.2 var(--sp-16-hue)),oklch(0.78 0.19 calc(var(--sp-16-hue) + 70deg)));
  box-shadow: 0 0 16px -2px oklch(0.75 0.2 var(--sp-16-hue));
}

@supports (animation-timeline: scroll()) {
  .sp-16__fill {
    transform: scaleX(0);
    animation: sp-16-scale linear both,sp-16-hue linear both;
    animation-timeline: scroll(root block),scroll(root block);
  }

  .sp-16__cfill--ok {
    transform: scaleX(0);
    animation: sp-16-scale linear both,sp-16-hue linear both;
    animation-timeline: scroll(root block),scroll(root block);
  }

  .sp-16__cfill--filter {
    transform: scaleX(0);
    animation: sp-16-scale linear both,sp-16-rot linear both;
    animation-timeline: scroll(root block),scroll(root block);
  }
}

@keyframes sp-16-scale {
  from {
    transform: scaleX(0);
  }

  to {
    transform: scaleX(1);
  }
}

@keyframes sp-16-hue {
  from {
    --sp-16-hue: 20deg;
  }

  to {
    --sp-16-hue: 380deg;
  }
}

@keyframes sp-16-rot {
  from {
    filter: hue-rotate(0deg);
  }

  to {
    filter: hue-rotate(360deg);
  }
}

.sp-16__bar {
  position: sticky;
  inset-block-start: 0;
  z-index: 40;
  display: flex;
  align-items: center;
  gap: 14px;
  min-block-size: 58px;
  padding-block-start: 6px;
  background: color-mix(in oklch,var(--sp-16-bg) 76%,transparent);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border-block-end: 1px solid var(--sp-16-line);
}

.sp-16__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 15px;
  font-weight: 730;
  letter-spacing: -.02em;
  color: inherit;
  text-decoration: none;
}

.sp-16__brand:focus-visible {
  outline: 2px solid var(--sp-16-acc);
  outline-offset: 3px;
  border-radius: 6px;
}

.sp-16__logo {
  inline-size: 18px;
  block-size: 18px;
  border-radius: 50%;
  background: conic-gradient(oklch(0.7 0.2 0),oklch(0.7 0.2 90),oklch(0.7 0.2 180),oklch(0.7 0.2 270),oklch(0.7 0.2 360));
}

.sp-16__meta {
  margin-inline-start: auto;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .08em;
  color: var(--sp-16-mut);
}

.sp-16__intro {
  display: grid;
  gap: 16px;
  padding-block: clamp(46px,10vh,116px) clamp(26px,6vh,58px);
  background: radial-gradient(80% 50% at 50% 0%,oklch(0.28 0.1 var(--sp-16-hue)),transparent);
}

.sp-16__intro-eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--sp-16-acc);
}

.sp-16__intro-title {
  font-size: clamp(36px,6.6vw,76px);
  line-height: .98;
  letter-spacing: -.04em;
  font-weight: 730;
  max-inline-size: 14ch;
  text-wrap: balance;
}

.sp-16__intro-sub {
  font-size: clamp(14.5px,1.6vw,18px);
  line-height: 1.55;
  color: var(--sp-16-mut);
  max-inline-size: 54ch;
  text-wrap: pretty;
}

.sp-16__compare {
  display: grid;
  grid-template-columns: repeat(2,minmax(0,1fr));
  gap: 16px;
  max-inline-size: 640px;
  margin-block-start: 6px;
}

.sp-16__cmp {
  display: grid;
  gap: 8px;
}

.sp-16__cmplab {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10.5px;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--sp-16-mut);
}

.sp-16__cbar {
  block-size: 10px;
  border-radius: 99px;
  background: oklch(1 0 0/.09);
  overflow: hidden;
}

.sp-16__cfill {
  display: block;
  block-size: 100%;
  transform-origin: 0 50%;
  transform: scaleX(var(--sp-16-p));
  border-radius: 99px;
}

.sp-16__cfill--ok {
  background: linear-gradient(90deg,oklch(0.72 0.2 var(--sp-16-hue)),oklch(0.78 0.19 calc(var(--sp-16-hue) + 70deg)));
}

.sp-16__cfill--filter {
  background: linear-gradient(90deg,oklch(0.68 0.21 25),oklch(0.74 0.2 60));
  filter: hue-rotate(calc(var(--sp-16-p) * 360deg));
}

.sp-16__sec {
  scroll-margin-top: 76px;
  display: grid;
  gap: 12px;
  align-content: center;
  min-block-size: 74svh;
  padding-block: clamp(26px,5vw,52px);
  border-block-end: 1px solid var(--sp-16-line);
}

.sp-16__sec:last-child {
  border-block-end: 0;
}

.sp-16__kicker {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--sp-16-acc);
}

.sp-16__h {
  font-size: clamp(22px,3.1vw,33px);
  line-height: 1.1;
  letter-spacing: -.032em;
  font-weight: 700;
  text-wrap: balance;
}

.sp-16__p {
  max-inline-size: 60ch;
  font-size: 15.8px;
  line-height: 1.7;
  color: var(--sp-16-mut);
  text-wrap: pretty;
}

.sp-16__p--lede {
  font-size: 17.8px;
  color: var(--sp-16-ink);
}

.sp-16__p code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .85em;
  background: oklch(1 0 0/.1);
  padding: 2px 6px;
  border-radius: 5px;
}

.sp-16__chip {
  justify-self: start;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--sp-16-acc);
  padding: 7px 13px;
  border-radius: 99px;
  background: oklch(1 0 0/.08);
  border: 1px solid color-mix(in oklch,var(--sp-16-acc) 30%,transparent);
}

.sp-16__pagefoot {
  display: grid;
  place-items: center;
  padding: clamp(40px,8vh,100px) 24px;
  border-block-start: 1px solid var(--sp-16-line);
}

.sp-16__pagefootin {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  letter-spacing: .06em;
  color: var(--sp-16-mut);
  text-align: center;
}

.sp-16__bar,
.sp-16__intro,
.sp-16__sec {
  padding-inline: max(clamp(18px,4vw,36px),calc((100% - 900px)/2));
}

:root:has(.sp-16) {
  scroll-behavior: smooth;
  scroll-padding-top: 76px;
}

@media (max-width: 600px) {
  .sp-16__compare {
    grid-template-columns: minmax(0,1fr);
  }

  .sp-16__sec {
    min-block-size: auto;
  }
}

@media (prefers-reduced-motion: reduce) {
  :root:has(.sp-16) {
    scroll-behavior: auto;
  }

  .sp-16 {
    --sp-16-hue: 270deg;
  }

  .sp-16__fill,
    .sp-16__cfill--ok {
    animation-name: sp-16-scale;
    animation-timeline: scroll(root block);
  }

  .sp-16__cfill--filter {
    animation-name: sp-16-scale;
    animation-timeline: scroll(root block);
    filter: none;
  }

  .sp-16 * {
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sp-16');
  if (!root || root.dataset.spWired) return;
  root.dataset.spWired = '1';
  const rail = root.querySelector('#sp-16-rail');
  const native = CSS.supports('animation-timeline', 'scroll()');
  const calm = matchMedia('(prefers-reduced-motion: reduce)').matches;
  let ticking = false;
  const paint = () => {
    ticking = false;
    const d = document.documentElement;
    const max = d.scrollHeight - d.clientHeight;
    const p = max > 0 ? Math.min(1, Math.max(0, d.scrollTop / max)) : 0;
    if (!native) {
      root.style.setProperty('--sp-16-p', p.toFixed(4));
      if (!calm) root.style.setProperty('--sp-16-hue', (20 + p * 360).toFixed(1) + 'deg');
    }
    rail.setAttribute('aria-valuenow', String(Math.round(p * 100)));
  };
  const onScroll = () => { if (!ticking) { ticking = true; requestAnimationFrame(paint); } };
  addEventListener('scroll', onScroll, { passive: true });
  addEventListener('resize', onScroll, { passive: true });
  paint();
})();
```
