---
source: "codefronts"
url: "https://codefronts.com/motion/css-scroll-progress-bar/gradient-animated-multi-color-scroll-bar/"
title: "Gradient Animated Multi-Color Scroll Bar"
section: "motion"
category: "css-scroll-progress-bar"
category_name: "CSS Scroll Progress Bar"
description: "A progress bar where the colour itself travels."
has_js: "true"
---

Here's a working CSS Scroll Progress Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Gradient Animated Multi-Color Scroll Bar
Source: https://codefronts.com/motion/css-scroll-progress-bar/gradient-animated-multi-color-scroll-bar/

A progress bar where the colour itself travels. The fill scales as usual, but a 300%-wide multi-stop gradient slides through it as you scroll, so the leading edge is a different hue at 20% than at 80% — and because the stops are interpolated in oklch, there are none of the muddy grey midpoints that sRGB gradients produce between complementary colours.
## HTML
```html
<section class="sp-06" aria-label="Animated gradient multi-color scroll bar demo">
  <div class="sp-06__rail" role="progressbar" aria-label="Reading progress" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0" id="sp-06-rail"><i class="sp-06__fill"></i></div>
  <header class="sp-06__bar">
    <a class="sp-06__brand" href="#sp-06-s1"><span class="sp-06__logo" aria-hidden="true"></span>Spectra</a>
    <p class="sp-06__meta">in oklch · 300% background</p>
  </header>
  <div class="sp-06__intro">
    <div class="sp-06__introin">
      <p class="sp-06__intro-eyebrow">background-position on a scroll timeline</p>
      <h2 class="sp-06__intro-title">The colour travels with you</h2>
      <p class="sp-06__intro-sub">Scroll slowly and watch the leading edge change hue. Same bar, five stops, one perceptually-uniform colour space.</p>
      <div class="sp-06__swatches" aria-hidden="true"><span></span><span></span><span></span><span></span><span></span></div>
    </div>
  </div>
  <main class="sp-06__main">
    <section class="sp-06__sec" id="sp-06-s1">
      <p class="sp-06__kicker">Technique</p>
      <h3 class="sp-06__h">Oversize, then slide</h3>
      <p class="sp-06__p sp-06__p--lede">A 300%-wide gradient translated by <code>background-position</code> is cheap. Re-defining the gradient's stops each frame is not — that is the difference between a smooth bar and a stuttering one.</p>
    </section>
    <section class="sp-06__sec" id="sp-06-s2">
      <p class="sp-06__kicker">Colour</p>
      <h3 class="sp-06__h">Why oklch changes everything</h3>
      <p class="sp-06__p">Purple to yellow in sRGB goes through mud. In <code>oklch</code> the same two stops stay saturated the whole way, because the engine interpolates in a space built around human perception rather than phosphor voltages.</p>
      <figure class="sp-06__fig">
        <img class="sp-06__img" src="https://images.unsplash.com/photo-1493612276216-ee3925520721?auto=format&amp;fit=crop&amp;w=1400&amp;q=70" alt="Abstract long-exposure light streaks in violet and orange" loading="lazy" decoding="async">
        <figcaption class="sp-06__cap">One token — <code>in oklch</code> — separates a vivid gradient from a grey one.</figcaption>
      </figure>
    </section>
    <section class="sp-06__sec" id="sp-06-s3">
      <p class="sp-06__kicker">Detail</p>
      <h3 class="sp-06__h">A specular nib</h3>
      <p class="sp-06__p">A narrow white sheen blended with <code>plus-lighter</code> sits at the leading edge. It reads as light catching the tip of the bar, and it is one pseudo-element.</p>
    </section>
    <section class="sp-06__sec" id="sp-06-s4">
      <p class="sp-06__kicker">Restraint</p>
      <h3 class="sp-06__h">Freeze the colour, keep the meaning</h3>
      <p class="sp-06__p">Under <code>prefers-reduced-motion</code> the travel stops and the bar holds a single palette. The information never depended on the animation.</p>
      <p class="sp-06__chip">5 stops · 2 animations · 1 timeline</p>
    </section>
  </main>
  <footer class="sp-06__pagefoot"><p class="sp-06__pagefootin">Scroll progress pattern 06 of 18 · codefronts.com</p></footer>
</section>
```
## CSS
```css
.sp-06 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--sp-06-bg);
  --sp-06-bg: oklch(0.16 0.024 300);
  --sp-06-surface: oklch(0.22 0.03 300);
  --sp-06-ink: oklch(0.97 0.006 300);
  --sp-06-mut: oklch(0.73 0.02 300);
  --sp-06-acc: oklch(0.72 0.19 320);
  --sp-06-line: oklch(1 0 0/.12);
  --sp-06-h: 6px;
  --sp-06-p: 0;
  --sp-06-grad: linear-gradient(in oklch 90deg,oklch(0.62 0.24 295),oklch(0.68 0.24 350),oklch(0.79 0.17 75),oklch(0.75 0.17 160),oklch(0.62 0.24 295));
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--sp-06-ink);
  -webkit-font-smoothing: antialiased;
}

.sp-06 *,
.sp-06 *::before,
.sp-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sp-06__rail {
  position: fixed;
  inset-block-start: 0;
  inset-inline: 0;
  block-size: var(--sp-06-h);
  z-index: 60;
  background: oklch(1 0 0/.08);
  isolation: isolate;
  pointer-events: none;
}

.sp-06__fill {
  position: relative;
  display: block;
  block-size: 100%;
  transform-origin: 0 50%;
  transform: scaleX(var(--sp-06-p));
  background-image: var(--sp-06-grad);
  background-size: 300% 100%;
  background-position: 0 0;
  filter: saturate(1.15);
}

.sp-06__fill::after {
  content: "";
  position: absolute;
  inset-block: 0;
  inset-inline-end: 0;
  inline-size: 44px;
  background: linear-gradient(90deg,transparent,oklch(1 0 0/.85));
  mix-blend-mode: plus-lighter;
}

@supports (animation-timeline: scroll()) {
  .sp-06__fill {
    transform: scaleX(0);
    animation: sp-06-scale linear both,sp-06-slide linear both;
    animation-timeline: scroll(root block),scroll(root block);
  }
}

@keyframes sp-06-scale {
  from {
    transform: scaleX(0);
  }

  to {
    transform: scaleX(1);
  }
}

@keyframes sp-06-slide {
  from {
    background-position: 0 0;
  }

  to {
    background-position: -200% 0;
  }
}

.sp-06__bar {
  position: sticky;
  inset-block-start: 0;
  z-index: 40;
  display: flex;
  align-items: center;
  gap: 14px;
  min-block-size: 60px;
  padding-block-start: var(--sp-06-h);
  background: color-mix(in oklch,var(--sp-06-bg) 74%,transparent);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border-block-end: 1px solid var(--sp-06-line);
}

.sp-06__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 15px;
  font-weight: 730;
  letter-spacing: -.02em;
  color: inherit;
  text-decoration: none;
}

.sp-06__brand:focus-visible {
  outline: 2px solid var(--sp-06-acc);
  outline-offset: 3px;
  border-radius: 6px;
}

.sp-06__logo {
  inline-size: 18px;
  block-size: 18px;
  border-radius: 6px;
  background: var(--sp-06-grad);
  background-size: 200% 100%;
}

.sp-06__meta {
  margin-inline-start: auto;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .08em;
  color: var(--sp-06-mut);
}

.sp-06__intro {
  display: grid;
  place-items: center;
  min-block-size: min(88svh,860px);
  padding-block: clamp(56px,12vh,140px) clamp(40px,8vh,90px);
  background: radial-gradient(80% 50% at 50% 0%,oklch(0.3 0.13 310),transparent);
}

.sp-06__introin {
  display: grid;
  justify-items: center;
  gap: clamp(12px,1.8vw,18px);
  text-align: center;
  max-inline-size: 26ch;
}

.sp-06__intro-eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: clamp(11px,1.1vw,13px);
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--sp-06-acc);
}

.sp-06__intro-title {
  font-size: clamp(38px,7.2vw,82px);
  line-height: .98;
  letter-spacing: -.04em;
  font-weight: 730;
  text-wrap: balance;
  background: var(--sp-06-grad);
  background-size: 200% 100%;
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  animation: sp-06-drift 14s linear infinite;
}

@keyframes sp-06-drift {
  to {
    background-position: -200% 0;
  }
}

.sp-06__intro-sub {
  font-size: clamp(15px,1.7vw,19px);
  line-height: 1.55;
  color: var(--sp-06-mut);
  max-inline-size: 48ch;
  text-wrap: pretty;
}

.sp-06__swatches {
  display: flex;
  gap: 8px;
  margin-block-start: 8px;
}

.sp-06__swatches span {
  inline-size: 34px;
  block-size: 10px;
  border-radius: 99px;
}

.sp-06__swatches span:nth-child(1) {
  background: oklch(0.62 0.24 295);
}

.sp-06__swatches span:nth-child(2) {
  background: oklch(0.68 0.24 350);
}

.sp-06__swatches span:nth-child(3) {
  background: oklch(0.79 0.17 75);
}

.sp-06__swatches span:nth-child(4) {
  background: oklch(0.75 0.17 160);
}

.sp-06__swatches span:nth-child(5) {
  background: oklch(0.62 0.24 295);
}

.sp-06__sec {
  scroll-margin-top: 76px;
  display: grid;
  gap: 12px;
  align-content: center;
  min-block-size: 74svh;
  padding-block: clamp(28px,5vw,56px);
  border-block-end: 1px solid var(--sp-06-line);
}

.sp-06__sec:last-child {
  border-block-end: 0;
}

.sp-06__kicker {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--sp-06-acc);
}

.sp-06__h {
  font-size: clamp(22px,3.2vw,34px);
  line-height: 1.1;
  letter-spacing: -.032em;
  font-weight: 700;
  text-wrap: balance;
}

.sp-06__p {
  max-inline-size: 60ch;
  font-size: 15.8px;
  line-height: 1.7;
  color: var(--sp-06-mut);
  text-wrap: pretty;
}

.sp-06__p--lede {
  font-size: 18px;
  color: var(--sp-06-ink);
}

.sp-06__p code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .85em;
  background: oklch(1 0 0/.1);
  padding: 2px 6px;
  border-radius: 5px;
}

.sp-06__fig {
  display: grid;
  gap: 9px;
  max-inline-size: 70ch;
}

.sp-06__img {
  inline-size: 100%;
  aspect-ratio: 16/7;
  object-fit: cover;
  display: block;
  border-radius: 16px;
  background: linear-gradient(135deg,oklch(0.5 0.18 300),oklch(0.6 0.16 60));
}

.sp-06__cap {
  font-size: 12.6px;
  color: var(--sp-06-mut);
}

.sp-06__chip {
  justify-self: start;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--sp-06-acc);
  padding: 7px 13px;
  border-radius: 99px;
  background: color-mix(in oklch,var(--sp-06-acc) 14%,transparent);
  border: 1px solid color-mix(in oklch,var(--sp-06-acc) 30%,transparent);
}

.sp-06__pagefoot {
  display: grid;
  place-items: center;
  padding: clamp(44px,9vh,110px) 24px;
  border-block-start: 1px solid var(--sp-06-line);
}

.sp-06__pagefootin {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  letter-spacing: .06em;
  color: var(--sp-06-mut);
  text-align: center;
}

.sp-06__bar {
  padding-inline: max(clamp(16px,3vw,26px),calc((100% - 1180px)/2));
}

.sp-06__intro,
.sp-06__sec {
  padding-inline: max(clamp(22px,5vw,44px),calc((100% - 900px)/2));
}

:root:has(.sp-06) {
  scroll-behavior: smooth;
  scroll-padding-top: 76px;
}

@media (max-width: 640px) {
  .sp-06__sec {
    min-block-size: auto;
  }
}

@media (prefers-reduced-motion: reduce) {
  :root:has(.sp-06) {
    scroll-behavior: auto;
  }

  .sp-06__intro-title {
    animation: none;
  }

  .sp-06__fill {
    animation-name: sp-06-scale;
    animation-timeline: scroll(root block);
  }

  .sp-06__fill::after {
    display: none;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sp-06');
  if (!root || root.dataset.spWired) return;
  root.dataset.spWired = '1';
  const rail = root.querySelector('#sp-06-rail');
  const fill = root.querySelector('.sp-06__fill');
  const native = CSS.supports('animation-timeline', 'scroll()');
  let ticking = false;
  const paint = () => {
    ticking = false;
    const d = document.documentElement;
    const max = d.scrollHeight - d.clientHeight;
    const p = max > 0 ? Math.min(1, Math.max(0, d.scrollTop / max)) : 0;
    if (!native) {
      root.style.setProperty('--sp-06-p', p.toFixed(4));
      fill.style.backgroundPosition = (-200 * p).toFixed(2) + '% 0';
    }
    rail.setAttribute('aria-valuenow', String(Math.round(p * 100)));
  };
  const onScroll = () => { if (!ticking) { ticking = true; requestAnimationFrame(paint); } };
  addEventListener('scroll', onScroll, { passive: true });
  addEventListener('resize', onScroll, { passive: true });
  paint();
})();
```
