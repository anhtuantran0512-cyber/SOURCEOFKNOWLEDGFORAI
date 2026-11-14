---
source: "codefronts"
url: "https://codefronts.com/motion/css-scroll-progress-bar/scroll-progress-bar-with-back-to-top-button-circular-morph/"
title: "Scroll Progress Bar with Back-to-Top Button (Circular Morph)"
section: "motion"
category: "css-scroll-progress-bar"
category_name: "CSS Scroll Progress Bar"
description: "The back-to-top control, upgraded: it does not just appear, it reports."
has_js: "true"
---

Here's a working CSS Scroll Progress Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Scroll Progress Bar with Back-to-Top Button (Circular Morph)
Source: https://codefronts.com/motion/css-scroll-progress-bar/scroll-progress-bar-with-back-to-top-button-circular-morph/

The back-to-top control, upgraded: it does not just appear, it reports. The ring around it is the page progress, it only materialises once the reader is genuinely committed, and on hover it morphs from a 52px circle into a pill with a label — one element, one grid-template-columns transition, no JavaScript for any of the motion.
## HTML
```html
<section class="sp-05" aria-label="Scroll progress with circular back-to-top button demo">
  <div class="sp-05__topline" aria-hidden="true"><i class="sp-05__topfill"></i></div>
  <button class="sp-05__fab" type="button" id="sp-05-fab" aria-label="Back to top">
    <span class="sp-05__ringwrap" aria-hidden="true">
      <svg class="sp-05__svg" viewBox="0 0 52 52" focusable="false"><circle class="sp-05__track" cx="26" cy="26" r="22" pathLength="1"></circle><circle class="sp-05__value" cx="26" cy="26" r="22" pathLength="1"></circle></svg>
      <svg class="sp-05__arrow" viewBox="0 0 24 24" focusable="false"><path d="M12 19V5M5 12l7-7 7 7" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"></path></svg>
    </span>
    <span class="sp-05__label"><span class="sp-05__labelin">Back to top</span></span>
  </button>
  <header class="sp-05__bar">
    <a class="sp-05__brand" href="#sp-05-top"><span class="sp-05__logo" aria-hidden="true"></span>Ascend</a>
    <p class="sp-05__meta">animation-range: 8% 16%</p>
  </header>
  <div class="sp-05__intro" id="sp-05-top">
    <div class="sp-05__introin">
      <p class="sp-05__intro-eyebrow">reveal · morph · return</p>
      <h2 class="sp-05__intro-title" id="sp-05-h1" tabindex="-1">A return button that knows how far you got</h2>
      <p class="sp-05__intro-sub">Scroll past the first screen. The circle fades in, its ring tracks your progress, and hovering it grows a label out of nothing.</p>
    </div>
  </div>
  <main class="sp-05__main">
    <section class="sp-05__sec" id="sp-05-s1">
      <p class="sp-05__kicker">Threshold</p>
      <h3 class="sp-05__h">animation-range replaces the observer</h3>
      <p class="sp-05__p sp-05__p--lede">Mapping keyframes onto a slice of the timeline turns "appear after 15%" from a scroll listener and a class toggle into a single declaration.</p>
    </section>
    <section class="sp-05__sec" id="sp-05-s2">
      <p class="sp-05__kicker">Morph</p>
      <h3 class="sp-05__h">0fr to 1fr, no magic numbers</h3>
      <p class="sp-05__p">Grid track sizes animate. A collapsed <code>0fr</code> column expanding to <code>1fr</code> reveals the label at its natural width — no <code>max-width</code> guess, no measuring, no jump when the copy is translated.</p>
      <figure class="sp-05__fig">
        <img class="sp-05__img" src="https://images.unsplash.com/photo-1483058712412-4245e9b90334?auto=format&amp;fit=crop&amp;w=1400&amp;q=70" alt="A tidy desk with a monitor, keyboard and notes" loading="lazy" decoding="async">
        <figcaption class="sp-05__cap">The best micro-interactions are the ones you only notice on the second visit.</figcaption>
      </figure>
    </section>
    <section class="sp-05__sec" id="sp-05-s3">
      <p class="sp-05__kicker">Return</p>
      <h3 class="sp-05__h">Move the focus, not just the viewport</h3>
      <p class="sp-05__p">Scrolling to the top without moving focus strands keyboard users at the bottom of the document. The handler sends focus to the article heading, which carries <code>tabindex="-1"</code> for exactly this purpose.</p>
    </section>
    <section class="sp-05__sec" id="sp-05-s4">
      <p class="sp-05__kicker">Restraint</p>
      <h3 class="sp-05__h">Reduced motion means instant</h3>
      <p class="sp-05__p">Under <code>prefers-reduced-motion</code> the jump is immediate and the reveal is a plain opacity swap. The control still works — it just stops performing.</p>
      <p class="sp-05__chip">1 button · 2 SVGs · 4 lines of behaviour</p>
    </section>
  </main>
  <footer class="sp-05__pagefoot"><p class="sp-05__pagefootin">Scroll progress pattern 05 of 18 · codefronts.com</p></footer>
</section>
```
## CSS
```css
.sp-05 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--sp-05-bg);
  --sp-05-bg: oklch(0.973 0.012 300);
  --sp-05-surface: oklch(1 0 0);
  --sp-05-ink: oklch(0.2 0.03 300);
  --sp-05-mut: oklch(0.52 0.02 300);
  --sp-05-acc: oklch(0.55 0.22 300);
  --sp-05-acc2: oklch(0.68 0.19 350);
  --sp-05-line: oklch(0.2 0.03 300/.11);
  --sp-05-p: 0;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--sp-05-ink);
  -webkit-font-smoothing: antialiased;
}

.sp-05 *,
.sp-05 *::before,
.sp-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sp-05__topline {
  position: fixed;
  inset-block-start: 0;
  inset-inline: 0;
  block-size: 3px;
  z-index: 55;
  background: color-mix(in oklch,var(--sp-05-acc) 12%,transparent);
  pointer-events: none;
}

.sp-05__topfill {
  display: block;
  block-size: 100%;
  transform-origin: 0 50%;
  transform: scaleX(var(--sp-05-p));
  background: linear-gradient(90deg,var(--sp-05-acc),var(--sp-05-acc2));
}

.sp-05__fab {
  position: fixed;
  inset-block-end: max(22px,env(safe-area-inset-bottom));
  inset-inline-end: max(22px,env(safe-area-inset-right));
  z-index: 60;
  display: grid;
  grid-template-columns: auto 0fr;
  align-items: center;
  padding: 5px;
  border: 1px solid var(--sp-05-line);
  border-radius: 99px;
  background: color-mix(in oklch,var(--sp-05-surface) 88%,transparent);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  color: var(--sp-05-ink);
  cursor: pointer;
  box-shadow: 0 14px 34px -16px oklch(0.2 0.03 300/.6);
  opacity: 0;
  scale: .6;
  transition: grid-template-columns .38s cubic-bezier(.32,.72,.3,1),box-shadow .3s ease,opacity .3s ease,scale .3s ease;
}

.sp-05__fab[data-shown="true"] {
  opacity: 1;
  scale: 1;
}

@supports (animation-timeline: scroll()) {
  .sp-05__fab {
    animation: sp-05-in linear both;
    animation-timeline: scroll(root block);
    animation-range: 8% 16%;
  }
}

@keyframes sp-05-in {
  from {
    opacity: 0;
    scale: .6;
  }

  to {
    opacity: 1;
    scale: 1;
  }
}

.sp-05__fab:hover,
.sp-05__fab:focus-visible {
  grid-template-columns: auto 1fr;
  box-shadow: 0 18px 40px -16px oklch(0.55 0.22 300/.6);
}

.sp-05__fab:focus-visible {
  outline: 2px solid var(--sp-05-acc);
  outline-offset: 3px;
}

.sp-05__fab:active {
  scale: .95;
}

.sp-05__ringwrap {
  position: relative;
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
}

.sp-05__svg {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  transform: rotate(-90deg);
  overflow: visible;
}

.sp-05__track,
.sp-05__value {
  fill: none;
  stroke-width: 3.4;
  stroke-linecap: round;
}

.sp-05__track {
  stroke: color-mix(in oklch,var(--sp-05-acc) 16%,transparent);
}

.sp-05__value {
  stroke: var(--sp-05-acc);
  stroke-dasharray: 1;
  stroke-dashoffset: calc(1 - var(--sp-05-p));
}

@supports (animation-timeline: scroll()) {
  .sp-05__value {
    stroke-dashoffset: 1;
    animation: sp-05-ring linear both;
    animation-timeline: scroll(root block);
  }

  .sp-05__topfill {
    transform: scaleX(0);
    animation: sp-05-fill linear both;
    animation-timeline: scroll(root block);
  }
}

@keyframes sp-05-ring {
  to {
    stroke-dashoffset: 0;
  }
}

@keyframes sp-05-fill {
  from {
    transform: scaleX(0);
  }

  to {
    transform: scaleX(1);
  }
}

.sp-05__arrow {
  inline-size: 17px;
  block-size: 17px;
  color: var(--sp-05-acc);
  transition: translate .3s cubic-bezier(.32,.72,.3,1);
}

.sp-05__fab:hover .sp-05__arrow {
  translate: 0 -2px;
}

.sp-05__label {
  overflow: hidden;
  min-inline-size: 0;
}

.sp-05__labelin {
  display: block;
  padding-inline: 10px 12px;
  font-size: 13.4px;
  font-weight: 650;
  white-space: nowrap;
}

.sp-05__bar {
  position: sticky;
  inset-block-start: 0;
  z-index: 40;
  display: flex;
  align-items: center;
  gap: 14px;
  min-block-size: 60px;
  padding-block-start: 3px;
  background: color-mix(in oklch,var(--sp-05-surface) 78%,transparent);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border-block-end: 1px solid var(--sp-05-line);
}

.sp-05__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 15px;
  font-weight: 730;
  letter-spacing: -.02em;
  color: inherit;
  text-decoration: none;
}

.sp-05__brand:focus-visible {
  outline: 2px solid var(--sp-05-acc);
  outline-offset: 3px;
  border-radius: 6px;
}

.sp-05__logo {
  inline-size: 18px;
  block-size: 18px;
  border-radius: 6px;
  background: linear-gradient(140deg,var(--sp-05-acc),var(--sp-05-acc2));
}

.sp-05__meta {
  margin-inline-start: auto;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .08em;
  color: var(--sp-05-mut);
}

.sp-05__intro {
  display: grid;
  place-items: center;
  min-block-size: min(88svh,860px);
  padding-block: clamp(56px,12vh,140px) clamp(40px,8vh,90px);
  background: radial-gradient(88% 58% at 50% 0%,oklch(0.96 0.06 310),transparent);
}

.sp-05__introin {
  display: grid;
  justify-items: center;
  gap: clamp(12px,1.8vw,18px);
  text-align: center;
  max-inline-size: 26ch;
}

.sp-05__intro-eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: clamp(11px,1.1vw,13px);
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--sp-05-acc);
}

.sp-05__intro-title {
  font-size: clamp(36px,6.8vw,78px);
  line-height: 1;
  letter-spacing: -.04em;
  font-weight: 730;
  text-wrap: balance;
}

.sp-05__intro-title:focus-visible {
  outline: 2px dashed var(--sp-05-acc);
  outline-offset: 8px;
  border-radius: 8px;
}

.sp-05__intro-sub {
  font-size: clamp(15px,1.7vw,19px);
  line-height: 1.55;
  color: var(--sp-05-mut);
  max-inline-size: 48ch;
  text-wrap: pretty;
}

.sp-05__sec {
  scroll-margin-top: 76px;
  display: grid;
  gap: 12px;
  align-content: center;
  min-block-size: 74svh;
  padding-block: clamp(28px,5vw,56px);
  border-block-end: 1px solid var(--sp-05-line);
}

.sp-05__sec:last-child {
  border-block-end: 0;
}

.sp-05__kicker {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--sp-05-acc);
}

.sp-05__h {
  font-size: clamp(22px,3.2vw,34px);
  line-height: 1.1;
  letter-spacing: -.032em;
  font-weight: 700;
  text-wrap: balance;
}

.sp-05__p {
  max-inline-size: 60ch;
  font-size: 15.8px;
  line-height: 1.7;
  color: var(--sp-05-mut);
  text-wrap: pretty;
}

.sp-05__p--lede {
  font-size: 18px;
  color: var(--sp-05-ink);
}

.sp-05__p code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .85em;
  background: oklch(0.2 0.03 300/.07);
  padding: 2px 6px;
  border-radius: 5px;
}

.sp-05__fig {
  display: grid;
  gap: 9px;
  max-inline-size: 70ch;
}

.sp-05__img {
  inline-size: 100%;
  aspect-ratio: 16/7;
  object-fit: cover;
  display: block;
  border-radius: 16px;
  background: linear-gradient(135deg,oklch(0.55 0.12 310),oklch(0.35 0.08 340));
}

.sp-05__cap {
  font-size: 12.6px;
  color: var(--sp-05-mut);
}

.sp-05__chip {
  justify-self: start;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--sp-05-acc);
  padding: 7px 13px;
  border-radius: 99px;
  background: color-mix(in oklch,var(--sp-05-acc) 10%,transparent);
  border: 1px solid color-mix(in oklch,var(--sp-05-acc) 24%,transparent);
}

.sp-05__pagefoot {
  display: grid;
  place-items: center;
  padding: clamp(44px,9vh,110px) 24px;
  border-block-start: 1px solid var(--sp-05-line);
}

.sp-05__pagefootin {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  letter-spacing: .06em;
  color: var(--sp-05-mut);
  text-align: center;
}

.sp-05__bar {
  padding-inline: max(clamp(16px,3vw,26px),calc((100% - 1180px)/2));
}

.sp-05__intro,
.sp-05__sec {
  padding-inline: max(clamp(22px,5vw,44px),calc((100% - 900px)/2));
}

:root:has(.sp-05) {
  scroll-padding-top: 76px;
}

@media (max-width: 640px) {
  .sp-05__sec {
    min-block-size: auto;
  }

  .sp-05__labelin {
    font-size: 12.6px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sp-05__fab,
    .sp-05__arrow {
    transition-duration: .01ms !important;
  }

  .sp-05 * {
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sp-05');
  if (!root || root.dataset.spWired) return;
  root.dataset.spWired = '1';
  const fab = root.querySelector('#sp-05-fab');
  const h1 = root.querySelector('#sp-05-h1');
  const native = CSS.supports('animation-timeline', 'scroll()');
  let ticking = false;
  const paint = () => {
    ticking = false;
    const d = document.documentElement;
    const max = d.scrollHeight - d.clientHeight;
    const p = max > 0 ? Math.min(1, Math.max(0, d.scrollTop / max)) : 0;
    if (!native) {
      root.style.setProperty('--sp-05-p', p.toFixed(4));
      fab.dataset.shown = String(p > 0.08);
    }
  };
  const onScroll = () => { if (!ticking) { ticking = true; requestAnimationFrame(paint); } };
  addEventListener('scroll', onScroll, { passive: true });
  addEventListener('resize', onScroll, { passive: true });
  paint();
  fab.addEventListener('click', () => {
    const calm = matchMedia('(prefers-reduced-motion: reduce)').matches;
    scrollTo({ top: 0, behavior: calm ? 'auto' : 'smooth' });
    setTimeout(() => h1.focus({ preventScroll: true }), calm ? 0 : 520);
  });
})();
```
