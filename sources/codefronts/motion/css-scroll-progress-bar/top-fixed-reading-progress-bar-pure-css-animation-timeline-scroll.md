---
source: "codefronts"
url: "https://codefronts.com/motion/css-scroll-progress-bar/top-fixed-reading-progress-bar-pure-css-animation-timeline-scroll/"
title: "Top Fixed Reading Progress Bar (Pure CSS, animation-timeline: scroll())"
section: "motion"
category: "css-scroll-progress-bar"
category_name: "CSS Scroll Progress Bar"
description: "The canonical reading-progress bar, rebuilt with zero JavaScript on the hot path."
has_js: "true"
---

Here's a working CSS Scroll Progress Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Top Fixed Reading Progress Bar (Pure CSS, animation-timeline: scroll())
Source: https://codefronts.com/motion/css-scroll-progress-bar/top-fixed-reading-progress-bar-pure-css-animation-timeline-scroll/

The canonical reading-progress bar, rebuilt with zero JavaScript on the hot path. One @keyframes block plus animation-timeline: scroll() hands the whole thing to the compositor, so a 6,000-word article scrolls without a single scroll event, a single layout read, or a single frame of jank — and a five-line script keeps it working in browsers that have not shipped scroll timelines yet.
## HTML
```html
<section class="sp-01" aria-label="Top fixed reading progress bar demo">
  <div class="sp-01__prog" role="progressbar" aria-label="Reading progress" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0" id="sp-01-prog"><i class="sp-01__fill"></i></div>
  <header class="sp-01__bar">
    <a class="sp-01__brand" href="#sp-01-s1"><span class="sp-01__logo" aria-hidden="true"></span>Longform</a>
    <p class="sp-01__meta">12 min read</p>
  </header>
  <div class="sp-01__intro">
    <div class="sp-01__introin">
      <p class="sp-01__intro-eyebrow">animation-timeline: scroll(root block)</p>
      <h2 class="sp-01__intro-title">The progress bar that costs zero scroll events</h2>
      <p class="sp-01__intro-sub">Scroll the page. The bar at the very top is driven entirely by CSS — no listener, no rAF loop, no layout read on any frame.</p>
    </div>
  </div>
  <main class="sp-01__main">
    <article class="sp-01__article">
      <section class="sp-01__sec" id="sp-01-s1">
        <p class="sp-01__kicker">01 — The idea</p>
        <h3 class="sp-01__h">Progress, not time</h3>
        <p class="sp-01__p sp-01__p--lede">A scroll-driven animation is a normal keyframe animation whose playhead is bound to a scroll offset. Nothing about the keyframes changes. Only the clock does.</p>
        <p class="sp-01__p">That single substitution removes the whole legacy stack: no <code>scroll</code> handler, no <code>requestAnimationFrame</code> coalescing, no <code>getBoundingClientRect</code> on the hot path, and no risk of the main thread being busy when the user flicks the page.</p>
      </section>
      <section class="sp-01__sec" id="sp-01-s2">
        <p class="sp-01__kicker">02 — The timeline</p>
        <h3 class="sp-01__h">scroll(root block)</h3>
        <p class="sp-01__p">The first argument picks the scroller — <code>root</code>, <code>nearest</code> or <code>self</code>. The second picks the axis — <code>block</code>, <code>inline</code>, <code>x</code> or <code>y</code>. Zero percent is the top of the range, one hundred percent is the maximum scroll offset.</p>
        <p class="sp-01__p">Because the timeline is anonymous, there is nothing to name, register or clean up when the element leaves the DOM.</p>
      </section>
      <section class="sp-01__sec" id="sp-01-s3">
        <p class="sp-01__kicker">03 — Why scaleX</p>
        <h3 class="sp-01__h">Composited, not laid out</h3>
        <p class="sp-01__p">A bar animated with <code>width</code> asks the engine to re-run layout sixty times a second. A bar animated with <code>transform:scaleX()</code> asks it to change one matrix. On a mid-range Android that is the difference between a jittery bar and an invisible one.</p>
        <figure class="sp-01__fig">
          <img class="sp-01__img" src="https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&amp;fit=crop&amp;w=1400&amp;q=70" alt="A code editor open on a laptop in a dim room" loading="lazy" decoding="async">
          <figcaption class="sp-01__cap">Ten lines of CSS replace a listener, a throttle and a resize observer.</figcaption>
        </figure>
      </section>
      <section class="sp-01__sec" id="sp-01-s4">
        <p class="sp-01__kicker">04 — The fallback</p>
        <h3 class="sp-01__h">One property, two writers</h3>
        <p class="sp-01__p">Every visual reads <code>--sp-01-p</code>. CSS writes it where scroll timelines exist; a guarded script writes it where they do not. The paint code never learns which path is live.</p>
      </section>
      <section class="sp-01__sec" id="sp-01-s5">
        <p class="sp-01__kicker">05 — Ship it</p>
        <h3 class="sp-01__h">Under a kilobyte</h3>
        <p class="sp-01__p">Two elements, one keyframe block, one feature query. It is smaller than the analytics beacon that will measure whether anyone read this far.</p>
        <p class="sp-01__chip">~700 bytes of CSS · 0 bytes of JS on modern engines</p>
      </section>
    </article>
  </main>
  <footer class="sp-01__pagefoot"><p class="sp-01__pagefootin">Scroll progress pattern 01 of 18 · codefronts.com</p></footer>
</section>
```
## CSS
```css
.sp-01 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--sp-01-bg);
  --sp-01-bg: oklch(0.977 0.006 100);
  --sp-01-surface: oklch(1 0 0);
  --sp-01-ink: oklch(0.21 0.02 60);
  --sp-01-mut: oklch(0.52 0.016 65);
  --sp-01-acc: oklch(0.58 0.19 28);
  --sp-01-line: oklch(0.21 0.02 60/.11);
  --sp-01-h: 5px;
  --sp-01-bar: 60px;
  --sp-01-p: 0;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--sp-01-ink);
  -webkit-font-smoothing: antialiased;
}

.sp-01 *,
.sp-01 *::before,
.sp-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sp-01__prog {
  position: fixed;
  inset-block-start: 0;
  inset-inline: 0;
  block-size: var(--sp-01-h);
  z-index: 60;
  background: color-mix(in oklch,var(--sp-01-acc) 13%,transparent);
  pointer-events: none;
}

.sp-01__fill {
  display: block;
  block-size: 100%;
  inline-size: 100%;
  transform-origin: 0 50%;
  transform: scaleX(var(--sp-01-p));
  background: linear-gradient(90deg,var(--sp-01-acc),oklch(0.7 0.17 55));
  border-start-end-radius: 99px;
  border-end-end-radius: 99px;
  box-shadow: 0 0 14px -2px color-mix(in oklch,var(--sp-01-acc) 70%,transparent);
}

@supports (animation-timeline: scroll()) {
  .sp-01__fill {
    transform: scaleX(0);
    animation: sp-01-fill linear both;
    animation-timeline: scroll(root block);
  }
}

@keyframes sp-01-fill {
  from {
    transform: scaleX(0);
  }

  to {
    transform: scaleX(1);
  }
}

.sp-01__bar {
  position: sticky;
  inset-block-start: 0;
  z-index: 40;
  display: flex;
  align-items: center;
  gap: 14px;
  min-block-size: var(--sp-01-bar);
  background: color-mix(in oklch,var(--sp-01-surface) 80%,transparent);
  backdrop-filter: blur(14px) saturate(1.6);
  -webkit-backdrop-filter: blur(14px) saturate(1.6);
  border-block-end: 1px solid var(--sp-01-line);
}

.sp-01__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: -.02em;
  color: inherit;
  text-decoration: none;
}

.sp-01__brand:focus-visible {
  outline: 2px solid var(--sp-01-acc);
  outline-offset: 3px;
  border-radius: 6px;
}

.sp-01__logo {
  inline-size: 18px;
  block-size: 18px;
  border-radius: 5px;
  background: linear-gradient(140deg,var(--sp-01-acc),oklch(0.74 0.15 70));
}

.sp-01__meta {
  margin-inline-start: auto;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--sp-01-mut);
}

.sp-01__intro {
  display: grid;
  place-items: center;
  min-block-size: min(88svh,860px);
  padding-block: clamp(56px,12vh,140px) clamp(40px,8vh,90px);
  background: radial-gradient(90% 60% at 50% 0%,oklch(0.99 0.03 60),transparent);
}

.sp-01__introin {
  display: grid;
  justify-items: center;
  gap: clamp(12px,1.8vw,18px);
  text-align: center;
  max-inline-size: 28ch;
}

.sp-01__intro-eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: clamp(11px,1.1vw,13px);
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--sp-01-acc);
}

.sp-01__intro-title {
  font-size: clamp(38px,7.2vw,82px);
  line-height: .98;
  letter-spacing: -.042em;
  font-weight: 730;
  text-wrap: balance;
}

.sp-01__intro-sub {
  font-size: clamp(15px,1.7vw,19px);
  line-height: 1.55;
  color: var(--sp-01-mut);
  max-inline-size: 46ch;
  text-wrap: pretty;
}

.sp-01__intro::after {
  content: "Scroll — watch the top edge";
  margin-block-start: clamp(20px,4vh,44px);
  padding: 9px 18px;
  border: 1px solid var(--sp-01-line);
  border-radius: 99px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--sp-01-mut);
  animation: sp-01-cue 2.6s ease-in-out infinite;
}

@keyframes sp-01-cue {
  0%,
    100% {
    transform: translateY(0);
    opacity: .75;
  }

  50% {
    transform: translateY(5px);
    opacity: 1;
  }
}

.sp-01__article {
  display: grid;
}

.sp-01__sec {
  scroll-margin-top: calc(var(--sp-01-bar) + 12px);
  display: grid;
  gap: 12px;
  align-content: center;
  min-block-size: 74svh;
  padding-block: clamp(30px,6vw,60px);
  border-block-end: 1px solid var(--sp-01-line);
}

.sp-01__sec:last-child {
  border-block-end: 0;
}

.sp-01__kicker {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--sp-01-acc);
}

.sp-01__h {
  font-size: clamp(24px,3.4vw,38px);
  line-height: 1.08;
  letter-spacing: -.032em;
  font-weight: 700;
  text-wrap: balance;
}

.sp-01__p {
  max-inline-size: 60ch;
  font-size: 16px;
  line-height: 1.7;
  color: var(--sp-01-mut);
  text-wrap: pretty;
}

.sp-01__p--lede {
  font-size: 18.5px;
  line-height: 1.6;
  color: var(--sp-01-ink);
}

.sp-01__p code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .85em;
  background: oklch(0.21 0.02 60/.07);
  padding: 2px 6px;
  border-radius: 5px;
}

.sp-01__fig {
  display: grid;
  gap: 9px;
  margin-block-start: 6px;
  max-inline-size: 70ch;
}

.sp-01__img {
  inline-size: 100%;
  aspect-ratio: 16/7;
  object-fit: cover;
  display: block;
  border-radius: 14px;
  background: linear-gradient(135deg,oklch(0.62 0.14 30),oklch(0.42 0.09 60));
}

.sp-01__cap {
  font-size: 12.6px;
  color: var(--sp-01-mut);
}

.sp-01__chip {
  justify-self: start;
  margin-block-start: 4px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--sp-01-acc);
  padding: 7px 13px;
  border-radius: 99px;
  background: color-mix(in oklch,var(--sp-01-acc) 9%,transparent);
  border: 1px solid color-mix(in oklch,var(--sp-01-acc) 24%,transparent);
}

.sp-01__pagefoot {
  display: grid;
  place-items: center;
  padding: clamp(44px,9vh,110px) 24px;
  border-block-start: 1px solid var(--sp-01-line);
}

.sp-01__pagefootin {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  letter-spacing: .06em;
  color: var(--sp-01-mut);
  text-align: center;
}

.sp-01__bar {
  padding-inline: max(clamp(16px,3vw,26px),calc((100% - 1180px)/2));
}

.sp-01__intro,
.sp-01__sec {
  padding-inline: max(clamp(22px,5vw,44px),calc((100% - 900px)/2));
}

:root:has(.sp-01) {
  scroll-behavior: smooth;
  scroll-padding-top: calc(60px + 12px);
}

@media (prefers-reduced-motion: reduce) {
  :root:has(.sp-01) {
    scroll-behavior: auto;
  }

  .sp-01__intro::after {
    animation: none;
  }

  .sp-01__fill {
    box-shadow: none;
    transition: none;
  }

  .sp-01 * {
    transition-duration: .01ms !important;
  }
}

@media (max-width: 640px) {
  .sp-01 {
    --sp-01-bar: 52px;
    --sp-01-h: 4px;
  }

  .sp-01__sec {
    min-block-size: auto;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sp-01');
  if (!root || root.dataset.spWired) return;
  root.dataset.spWired = '1';
  const prog = root.querySelector('#sp-01-prog');
  const native = CSS.supports('animation-timeline', 'scroll()');
  let ticking = false;
  const read = () => {
    const d = document.documentElement;
    const max = d.scrollHeight - d.clientHeight;
    return max > 0 ? Math.min(1, Math.max(0, d.scrollTop / max)) : 0;
  };
  const paint = () => {
    ticking = false;
    const p = read();
    if (!native) root.style.setProperty('--sp-01-p', p.toFixed(4));
    prog.setAttribute('aria-valuenow', String(Math.round(p * 100)));
  };
  const onScroll = () => { if (!ticking) { ticking = true; requestAnimationFrame(paint); } };
  addEventListener('scroll', onScroll, { passive: true });
  addEventListener('resize', onScroll, { passive: true });
  paint();
})();
```
