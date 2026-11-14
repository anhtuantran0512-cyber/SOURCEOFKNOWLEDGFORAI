---
source: "codefronts"
url: "https://codefronts.com/motion/css-scroll-progress-bar/vertical-side-docked-scroll-progress-line/"
title: "Vertical Side-Docked Scroll Progress Line"
section: "motion"
category: "css-scroll-progress-bar"
category_name: "CSS Scroll Progress Bar"
description: "A hairline rail docked to the side of the viewport, filling downward as the page moves — the indicator for designs where the top edge is sacred."
has_js: "true"
---

Here's a working CSS Scroll Progress Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Vertical Side-Docked Scroll Progress Line
Source: https://codefronts.com/motion/css-scroll-progress-bar/vertical-side-docked-scroll-progress-line/

A hairline rail docked to the side of the viewport, filling downward as the page moves — the indicator for designs where the top edge is sacred. Section dots along the rail light up as their section enters the viewport, using view() timelines rather than an observer, so the whole thing is a single element plus one dot per section.
## HTML
```html
<section class="sp-07" aria-label="Vertical side-docked scroll progress line demo">
  <div class="sp-07__rail" aria-hidden="true">
    <p class="sp-07__raillab">progress</p>
    <div class="sp-07__stack">
      <div class="sp-07__track"><i class="sp-07__fill"></i></div>
      <div class="sp-07__dots">
        <i class="sp-07__dot" data-dot="1"></i><i class="sp-07__dot" data-dot="2"></i><i class="sp-07__dot" data-dot="3"></i><i class="sp-07__dot" data-dot="4"></i>
      </div>
    </div>
  </div>
  <header class="sp-07__bar">
    <a class="sp-07__brand" href="#sp-07-s1"><span class="sp-07__logo" aria-hidden="true"></span>Margin</a>
    <p class="sp-07__meta">scaleY · view()</p>
  </header>
  <div class="sp-07__intro">
    <div class="sp-07__introin">
      <p class="sp-07__intro-eyebrow">transform-origin: 50% 0</p>
      <h2 class="sp-07__intro-title">Keep the top edge clean</h2>
      <p class="sp-07__intro-sub">The rail lives in the margin, out of the way of the masthead. Its dots light as each section enters the viewport.</p>
    </div>
  </div>
  <main class="sp-07__main">
    <section class="sp-07__sec" id="sp-07-s1" data-sec="1">
      <p class="sp-07__kicker">01 · Origin</p>
      <h3 class="sp-07__h">Scale down from the top</h3>
      <p class="sp-07__p sp-07__p--lede">A vertical fill is the horizontal one rotated, plus one correction: the transform origin has to move to the top edge or the bar grows out of its own middle.</p>
    </section>
    <section class="sp-07__sec" id="sp-07-s2" data-sec="2">
      <p class="sp-07__kicker">02 · view()</p>
      <h3 class="sp-07__h">Dots that know their section</h3>
      <p class="sp-07__p">A view progress timeline measures one element's trip through the viewport. Each dot is bound to its own section's timeline, so the state is declarative rather than observed.</p>
      <figure class="sp-07__fig">
        <img class="sp-07__img" src="https://images.unsplash.com/photo-1441974231531-c6227db76b6e?auto=format&amp;fit=crop&amp;w=1400&amp;q=70" alt="Sunlight through the trunks of a tall forest" loading="lazy" decoding="async">
        <figcaption class="sp-07__cap">Side rails suit long editorial pages where the header is already busy.</figcaption>
      </figure>
    </section>
    <section class="sp-07__sec" id="sp-07-s3" data-sec="3">
      <p class="sp-07__kicker">03 · Scope</p>
      <h3 class="sp-07__h">timeline-scope is the glue</h3>
      <p class="sp-07__p">Names declared on a section are invisible to elements outside it — until a shared ancestor declares <code>timeline-scope</code>. That one property is what makes cross-layout coordination possible.</p>
    </section>
    <section class="sp-07__sec" id="sp-07-s4" data-sec="4">
      <p class="sp-07__kicker">04 · Type</p>
      <h3 class="sp-07__h">Rotate with writing-mode</h3>
      <p class="sp-07__p">The vertical label uses <code>writing-mode:vertical-rl</code>, not a transform, so its box is genuinely vertical and the rail's spacing stays honest.</p>
      <p class="sp-07__chip">1 rail · 4 dots · 0 observers on modern engines</p>
    </section>
  </main>
  <footer class="sp-07__pagefoot"><p class="sp-07__pagefootin">Scroll progress pattern 07 of 18 · codefronts.com</p></footer>
</section>
```
## CSS
```css
.sp-07 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--sp-07-bg);
  --sp-07-bg: oklch(0.968 0.006 90);
  --sp-07-surface: oklch(1 0 0);
  --sp-07-ink: oklch(0.19 0.015 80);
  --sp-07-mut: oklch(0.51 0.012 80);
  --sp-07-acc: oklch(0.52 0.14 145);
  --sp-07-line: oklch(0.19 0.015 80/.12);
  --sp-07-w: 3px;
  --sp-07-gap: clamp(14px,3vw,34px);
  --sp-07-p: 0;
  timeline-scope: --sp-07-s1,--sp-07-s2,--sp-07-s3,--sp-07-s4;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--sp-07-ink);
  -webkit-font-smoothing: antialiased;
}

.sp-07 *,
.sp-07 *::before,
.sp-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sp-07__rail {
  position: fixed;
  inset-block: clamp(70px,12vh,110px) clamp(40px,10vh,90px);
  inset-inline-start: var(--sp-07-gap);
  z-index: 50;
  display: grid;
  grid-template-rows: auto 1fr;
  justify-items: center;
  gap: 12px;
  pointer-events: none;
}

.sp-07__raillab {
  writing-mode: vertical-rl;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 9.5px;
  letter-spacing: .28em;
  text-transform: uppercase;
  color: var(--sp-07-mut);
  opacity: .75;
}

.sp-07__stack {
  position: relative;
  inline-size: var(--sp-07-w);
  block-size: 100%;
}

.sp-07__track {
  inline-size: 100%;
  block-size: 100%;
  border-radius: 99px;
  background: color-mix(in oklch,var(--sp-07-ink) 10%,transparent);
  overflow: hidden;
}

.sp-07__fill {
  display: block;
  inline-size: 100%;
  block-size: 100%;
  transform-origin: 50% 0;
  transform: scaleY(var(--sp-07-p));
  border-radius: 99px;
  background: linear-gradient(180deg,var(--sp-07-acc),oklch(0.65 0.15 120));
}

@supports (animation-timeline: scroll()) {
  .sp-07__fill {
    transform: scaleY(0);
    animation: sp-07-grow linear both;
    animation-timeline: scroll(root block);
  }
}

@keyframes sp-07-grow {
  from {
    transform: scaleY(0);
  }

  to {
    transform: scaleY(1);
  }
}

.sp-07__dots {
  position: absolute;
  inset-block: 0;
  inset-inline-start: calc(100% + 9px);
  display: grid;
  align-content: space-between;
  padding-block: 6%;
}

.sp-07__dot {
  inline-size: 7px;
  block-size: 7px;
  border-radius: 50%;
  background: color-mix(in oklch,var(--sp-07-ink) 16%,transparent);
  scale: 1;
  transition: background .3s ease,scale .3s ease;
}

.sp-07__dot[data-on="true"] {
  background: var(--sp-07-acc);
  scale: 1.5;
}

@supports (animation-timeline: view()) {
  .sp-07__dot {
    animation: sp-07-dot steps(1,end) both;
  }

  .sp-07__dot[data-dot="1"] {
    animation-timeline: --sp-07-s1;
  }

  .sp-07__dot[data-dot="2"] {
    animation-timeline: --sp-07-s2;
  }

  .sp-07__dot[data-dot="3"] {
    animation-timeline: --sp-07-s3;
  }

  .sp-07__dot[data-dot="4"] {
    animation-timeline: --sp-07-s4;
  }

  .sp-07__sec[data-sec="1"] {
    view-timeline-name: --sp-07-s1;
  }

  .sp-07__sec[data-sec="2"] {
    view-timeline-name: --sp-07-s2;
  }

  .sp-07__sec[data-sec="3"] {
    view-timeline-name: --sp-07-s3;
  }

  .sp-07__sec[data-sec="4"] {
    view-timeline-name: --sp-07-s4;
  }
}

@keyframes sp-07-dot {
  0% {
    background: color-mix(in oklch,var(--sp-07-ink) 16%,transparent);
    scale: 1;
  }

  1%,
    99% {
    background: var(--sp-07-acc);
    scale: 1.5;
  }

  100% {
    background: color-mix(in oklch,var(--sp-07-ink) 16%,transparent);
    scale: 1;
  }
}

.sp-07__bar {
  position: sticky;
  inset-block-start: 0;
  z-index: 40;
  display: flex;
  align-items: center;
  gap: 14px;
  min-block-size: 58px;
  background: color-mix(in oklch,var(--sp-07-surface) 80%,transparent);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border-block-end: 1px solid var(--sp-07-line);
}

.sp-07__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 15px;
  font-weight: 730;
  letter-spacing: -.02em;
  color: inherit;
  text-decoration: none;
}

.sp-07__brand:focus-visible {
  outline: 2px solid var(--sp-07-acc);
  outline-offset: 3px;
  border-radius: 6px;
}

.sp-07__logo {
  inline-size: 6px;
  block-size: 20px;
  border-radius: 99px;
  background: linear-gradient(180deg,var(--sp-07-acc),oklch(0.68 0.14 120));
}

.sp-07__meta {
  margin-inline-start: auto;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .08em;
  color: var(--sp-07-mut);
}

.sp-07__intro {
  display: grid;
  place-items: center;
  min-block-size: min(86svh,820px);
  padding-block: clamp(56px,12vh,140px) clamp(40px,8vh,90px);
  background: radial-gradient(85% 55% at 50% 0%,oklch(0.97 0.04 140),transparent);
}

.sp-07__introin {
  display: grid;
  justify-items: center;
  gap: clamp(12px,1.8vw,18px);
  text-align: center;
  max-inline-size: 24ch;
}

.sp-07__intro-eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: clamp(11px,1.1vw,13px);
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--sp-07-acc);
}

.sp-07__intro-title {
  font-size: clamp(38px,7vw,80px);
  line-height: .98;
  letter-spacing: -.042em;
  font-weight: 730;
  text-wrap: balance;
}

.sp-07__intro-sub {
  font-size: clamp(15px,1.7vw,19px);
  line-height: 1.55;
  color: var(--sp-07-mut);
  max-inline-size: 46ch;
  text-wrap: pretty;
}

.sp-07__sec {
  scroll-margin-top: 72px;
  display: grid;
  gap: 12px;
  align-content: center;
  min-block-size: 78svh;
  padding-block: clamp(28px,5vw,56px);
  border-block-end: 1px solid var(--sp-07-line);
}

.sp-07__sec:last-child {
  border-block-end: 0;
}

.sp-07__kicker {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--sp-07-acc);
}

.sp-07__h {
  font-size: clamp(22px,3.2vw,34px);
  line-height: 1.1;
  letter-spacing: -.032em;
  font-weight: 700;
  text-wrap: balance;
}

.sp-07__p {
  max-inline-size: 60ch;
  font-size: 15.8px;
  line-height: 1.7;
  color: var(--sp-07-mut);
  text-wrap: pretty;
}

.sp-07__p--lede {
  font-size: 18px;
  color: var(--sp-07-ink);
}

.sp-07__p code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .85em;
  background: oklch(0.19 0.015 80/.07);
  padding: 2px 6px;
  border-radius: 5px;
}

.sp-07__fig {
  display: grid;
  gap: 9px;
  max-inline-size: 70ch;
}

.sp-07__img {
  inline-size: 100%;
  aspect-ratio: 16/7;
  object-fit: cover;
  display: block;
  border-radius: 14px;
  background: linear-gradient(135deg,oklch(0.55 0.1 140),oklch(0.35 0.06 160));
}

.sp-07__cap {
  font-size: 12.6px;
  color: var(--sp-07-mut);
}

.sp-07__chip {
  justify-self: start;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--sp-07-acc);
  padding: 7px 13px;
  border-radius: 99px;
  background: color-mix(in oklch,var(--sp-07-acc) 10%,transparent);
  border: 1px solid color-mix(in oklch,var(--sp-07-acc) 24%,transparent);
}

.sp-07__pagefoot {
  display: grid;
  place-items: center;
  padding: clamp(44px,9vh,110px) 24px;
  border-block-start: 1px solid var(--sp-07-line);
}

.sp-07__pagefootin {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  letter-spacing: .06em;
  color: var(--sp-07-mut);
  text-align: center;
}

.sp-07__bar {
  padding-inline: max(calc(var(--sp-07-gap) + 34px),calc((100% - 1180px)/2));
}

.sp-07__intro,
.sp-07__sec {
  padding-inline: max(calc(var(--sp-07-gap) + 34px),calc((100% - 880px)/2));
}

:root:has(.sp-07) {
  scroll-behavior: smooth;
  scroll-padding-top: 72px;
}

@media (max-width: 640px) {
  .sp-07 {
    --sp-07-gap: 10px;
    --sp-07-w: 2px;
  }

  .sp-07__raillab,
    .sp-07__dots {
    display: none;
  }

  .sp-07__sec {
    min-block-size: auto;
  }
}

@media (prefers-reduced-motion: reduce) {
  :root:has(.sp-07) {
    scroll-behavior: auto;
  }

  .sp-07 * {
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sp-07');
  if (!root || root.dataset.spWired) return;
  root.dataset.spWired = '1';
  const nativeScroll = CSS.supports('animation-timeline', 'scroll()');
  const nativeView = CSS.supports('animation-timeline', 'view()');
  let ticking = false;
  const paint = () => {
    ticking = false;
    const d = document.documentElement;
    const max = d.scrollHeight - d.clientHeight;
    const p = max > 0 ? Math.min(1, Math.max(0, d.scrollTop / max)) : 0;
    if (!nativeScroll) root.style.setProperty('--sp-07-p', p.toFixed(4));
  };
  const onScroll = () => { if (!ticking) { ticking = true; requestAnimationFrame(paint); } };
  addEventListener('scroll', onScroll, { passive: true });
  addEventListener('resize', onScroll, { passive: true });
  paint();
  if (!nativeView) {
    const dots = new Map();
    root.querySelectorAll('.sp-07__dot').forEach((d) => dots.set(d.dataset.dot, d));
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        const dot = dots.get(e.target.dataset.sec);
        if (dot) dot.dataset.on = String(e.isIntersecting);
      });
    }, { threshold: 0.15 });
    root.querySelectorAll('.sp-07__sec[data-sec]').forEach((s) => io.observe(s));
  }
})();
```
