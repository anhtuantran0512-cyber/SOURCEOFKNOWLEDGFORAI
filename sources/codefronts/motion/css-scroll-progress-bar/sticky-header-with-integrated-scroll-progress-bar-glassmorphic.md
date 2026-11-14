---
source: "codefronts"
url: "https://codefronts.com/motion/css-scroll-progress-bar/sticky-header-with-integrated-scroll-progress-bar-glassmorphic/"
title: "Sticky Header with Integrated Scroll Progress Bar (Glassmorphic)"
section: "motion"
category: "css-scroll-progress-bar"
category_name: "CSS Scroll Progress Bar"
description: "The pattern most publishers actually ship: the progress bar is not a separate strip floating over the page, it is the bottom edge of a frosted-glass header."
has_js: "true"
---

Here's a working CSS Scroll Progress Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sticky Header with Integrated Scroll Progress Bar (Glassmorphic)
Source: https://codefronts.com/motion/css-scroll-progress-bar/sticky-header-with-integrated-scroll-progress-bar-glassmorphic/

The pattern most publishers actually ship: the progress bar is not a separate strip floating over the page, it is the bottom edge of a frosted-glass header. Content dissolves under the blur as it passes, the hairline fills left-to-right, and the header quietly gains depth the moment it detaches from the top of the page.
## HTML
```html
<section class="sp-02" aria-label="Glassmorphic sticky header with progress bar demo">
  <div class="sp-02__sentinel" id="sp-02-sentinel" aria-hidden="true"></div>
  <header class="sp-02__bar" id="sp-02-bar">
    <a class="sp-02__brand" href="#sp-02-s1"><span class="sp-02__logo" aria-hidden="true"></span>Prism<span class="sp-02__brandthin">Journal</span></a>
    <nav class="sp-02__nav" aria-label="Article sections">
      <a class="sp-02__link" href="#sp-02-s1" aria-current="page">Overview</a>
      <a class="sp-02__link" href="#sp-02-s2">Method</a>
      <a class="sp-02__link" href="#sp-02-s3">Results</a>
    </nav>
    <p class="sp-02__pct" id="sp-02-pct" role="progressbar" aria-label="Article read" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0">0%</p>
  </header>
  <div class="sp-02__hero">
    <img class="sp-02__heroimg" src="https://images.unsplash.com/photo-1519681393784-d120267933ba?auto=format&amp;fit=crop&amp;w=1800&amp;q=70" alt="A mountain ridge under a deep blue night sky" loading="eager" decoding="async">
    <div class="sp-02__herotext">
      <p class="sp-02__eyebrow">Field notes · 9 min</p>
      <h2 class="sp-02__htitle">Frosted glass, one hairline, no extra markup</h2>
      <p class="sp-02__hsub">The indicator is the header's bottom edge — scroll and watch it fill while the photograph dissolves underneath.</p>
    </div>
  </div>
  <main class="sp-02__main">
    <section class="sp-02__sec" id="sp-02-s1">
      <p class="sp-02__kicker">Overview</p>
      <h3 class="sp-02__h">One element, three layers</h3>
      <p class="sp-02__p sp-02__p--lede">Glass plate, content row, progress edge. The edge is a pseudo-element, so it shares the header's stacking context and can never be painted over.</p>
      <p class="sp-02__p">Blur alone drains colour. Pairing <code>blur()</code> with <code>saturate()</code> restores it, which is why real frosted glass looks lively and a plain translucent rectangle looks dead.</p>
    </section>
    <section class="sp-02__sec" id="sp-02-s2">
      <p class="sp-02__kicker">Method</p>
      <h3 class="sp-02__h">Depth on detach</h3>
      <p class="sp-02__p">The header starts flat against the hero and gains a shadow the instant it detaches. Where <code>scroll-state(stuck: top)</code> exists that is pure CSS; everywhere else a single sentinel and an IntersectionObserver set the same state.</p>
      <figure class="sp-02__fig">
        <img class="sp-02__img" src="https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?auto=format&amp;fit=crop&amp;w=1400&amp;q=70" alt="Mist moving between dark pine trees" loading="lazy" decoding="async">
        <figcaption class="sp-02__cap">Translucency only reads as glass when something interesting passes behind it.</figcaption>
      </figure>
    </section>
    <section class="sp-02__sec" id="sp-02-s3">
      <p class="sp-02__kicker">Results</p>
      <h3 class="sp-02__h">The percentage is for people, not for looks</h3>
      <p class="sp-02__p">The numeric readout doubles as the accessible name of a real <code>progressbar</code>. Screen reader users get the same information sighted users get from the hairline.</p>
    </section>
    <section class="sp-02__sec" id="sp-02-s4">
      <p class="sp-02__kicker">Cost</p>
      <h3 class="sp-02__h">Know what blur costs</h3>
      <p class="sp-02__p">A blurred sticky header repaints every scroll frame. It is worth it above the fold on desktop and rarely worth it on a low-end phone — drop to an opaque background under 768px and nobody notices.</p>
      <p class="sp-02__chip">1 header · 1 pseudo-element · 0 extra nodes</p>
    </section>
  </main>
  <footer class="sp-02__pagefoot"><p class="sp-02__pagefootin">Scroll progress pattern 02 of 18 · codefronts.com</p></footer>
</section>
```
## CSS
```css
.sp-02 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--sp-02-bg);
  --sp-02-bg: oklch(0.972 0.008 250);
  --sp-02-surface: oklch(1 0 0);
  --sp-02-ink: oklch(0.2 0.024 265);
  --sp-02-mut: oklch(0.53 0.02 265);
  --sp-02-acc: oklch(0.6 0.19 250);
  --sp-02-acc2: oklch(0.68 0.17 320);
  --sp-02-line: oklch(0.2 0.024 265/.1);
  --sp-02-h: 3px;
  --sp-02-bar: 62px;
  --sp-02-p: 0;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--sp-02-ink);
  -webkit-font-smoothing: antialiased;
}

.sp-02 *,
.sp-02 *::before,
.sp-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sp-02__sentinel {
  block-size: 1px;
  margin-block-end: -1px;
}

.sp-02__bar {
  position: sticky;
  inset-block-start: 0;
  z-index: 50;
  display: flex;
  align-items: center;
  gap: clamp(10px,2vw,24px);
  min-block-size: var(--sp-02-bar);
  background: color-mix(in oklch,var(--sp-02-surface) 58%,transparent);
  backdrop-filter: blur(18px) saturate(1.8);
  -webkit-backdrop-filter: blur(18px) saturate(1.8);
  box-shadow: inset 0 1px 0 oklch(1 0 0/.6),0 0 0 rgba(0,0,0,0);
  transition: background .3s ease,box-shadow .3s ease;
}

.sp-02__bar::after {
  content: "";
  position: absolute;
  inset: auto 0 0 0;
  block-size: var(--sp-02-h);
  transform-origin: 0 50%;
  transform: scaleX(var(--sp-02-p));
  background: linear-gradient(90deg,var(--sp-02-acc),var(--sp-02-acc2));
  box-shadow: 0 0 12px -1px color-mix(in oklch,var(--sp-02-acc) 65%,transparent);
}

@supports (animation-timeline: scroll()) {
  .sp-02__bar::after {
    transform: scaleX(0);
    animation: sp-02-fill linear both;
    animation-timeline: scroll(root block);
  }
}

@keyframes sp-02-fill {
  from {
    transform: scaleX(0);
  }

  to {
    transform: scaleX(1);
  }
}

.sp-02__bar[data-stuck="true"] {
  background: color-mix(in oklch,var(--sp-02-surface) 78%,transparent);
  box-shadow: inset 0 1px 0 oklch(1 0 0/.7),0 10px 30px -18px oklch(0.2 0.024 265/.55);
}

@supports (container-type: scroll-state) {
  .sp-02__bar {
    container-type: scroll-state;
  }

  @container scroll-state(stuck: top) {
    .sp-02__bar {
      background: color-mix(in oklch,var(--sp-02-surface) 78%,transparent);
      box-shadow: inset 0 1px 0 oklch(1 0 0/.7),0 10px 30px -18px oklch(0.2 0.024 265/.55);
    }
  }
}

.sp-02__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 15.5px;
  font-weight: 730;
  letter-spacing: -.025em;
  color: inherit;
  text-decoration: none;
  white-space: nowrap;
}

.sp-02__brandthin {
  font-weight: 400;
  color: var(--sp-02-mut);
}

.sp-02__logo {
  inline-size: 20px;
  block-size: 20px;
  border-radius: 6px;
  background: conic-gradient(from 140deg,var(--sp-02-acc),var(--sp-02-acc2),var(--sp-02-acc));
  box-shadow: 0 3px 12px -3px var(--sp-02-acc);
}

.sp-02__nav {
  display: flex;
  align-items: center;
  gap: 2px;
  margin-inline-start: auto;
}

.sp-02__link {
  display: flex;
  align-items: center;
  min-block-size: 36px;
  padding: 0 11px;
  border-radius: 9px;
  font-size: 13.4px;
  font-weight: 600;
  color: var(--sp-02-mut);
  text-decoration: none;
  transition: color .18s ease,background .18s ease;
}

.sp-02__link:hover {
  color: var(--sp-02-ink);
  background: oklch(0.2 0.024 265/.05);
}

.sp-02__link[aria-current="page"] {
  color: var(--sp-02-acc);
  background: color-mix(in oklch,var(--sp-02-acc) 10%,transparent);
}

.sp-02__link:focus-visible,
.sp-02__brand:focus-visible {
  outline: 2px solid var(--sp-02-acc);
  outline-offset: 2px;
  border-radius: 9px;
}

.sp-02__pct {
  min-inline-size: 4.5ch;
  text-align: end;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12.5px;
  font-variant-numeric: tabular-nums;
  color: var(--sp-02-acc);
  font-weight: 600;
}

.sp-02__hero {
  position: relative;
  min-block-size: min(78svh,720px);
  display: grid;
  align-items: end;
  overflow: hidden;
  background: linear-gradient(150deg,oklch(0.34 0.09 260),oklch(0.2 0.05 290));
}

.sp-02__heroimg {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
  opacity: .62;
}

.sp-02__herotext {
  position: relative;
  display: grid;
  gap: 12px;
  padding-block: clamp(30px,7vh,70px);
  color: oklch(0.98 0 0);
  background: linear-gradient(to top,oklch(0.16 0.03 265/.9),transparent);
}

.sp-02__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: oklch(0.85 0.1 250);
}

.sp-02__htitle {
  font-size: clamp(30px,5.6vw,62px);
  line-height: 1;
  letter-spacing: -.04em;
  font-weight: 730;
  max-inline-size: 20ch;
  text-wrap: balance;
}

.sp-02__hsub {
  font-size: clamp(14.5px,1.6vw,18px);
  line-height: 1.55;
  color: oklch(0.9 0.01 250);
  max-inline-size: 52ch;
  text-wrap: pretty;
}

.sp-02__sec {
  scroll-margin-top: calc(var(--sp-02-bar) + 14px);
  display: grid;
  gap: 12px;
  align-content: center;
  min-block-size: 72svh;
  padding-block: clamp(28px,5vw,56px);
  border-block-end: 1px solid var(--sp-02-line);
}

.sp-02__sec:nth-of-type(even) {
  background: oklch(0.988 0.005 265);
}

.sp-02__kicker {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--sp-02-acc);
}

.sp-02__h {
  font-size: clamp(22px,3.2vw,34px);
  line-height: 1.1;
  letter-spacing: -.032em;
  font-weight: 700;
  text-wrap: balance;
}

.sp-02__p {
  max-inline-size: 60ch;
  font-size: 15.8px;
  line-height: 1.7;
  color: var(--sp-02-mut);
  text-wrap: pretty;
}

.sp-02__p--lede {
  font-size: 18px;
  color: var(--sp-02-ink);
}

.sp-02__p code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .85em;
  background: oklch(0.2 0.024 265/.07);
  padding: 2px 6px;
  border-radius: 5px;
}

.sp-02__fig {
  display: grid;
  gap: 9px;
  margin-block-start: 6px;
  max-inline-size: 70ch;
}

.sp-02__img {
  inline-size: 100%;
  aspect-ratio: 16/7;
  object-fit: cover;
  display: block;
  border-radius: 16px;
  background: linear-gradient(135deg,oklch(0.5 0.08 200),oklch(0.3 0.05 260));
}

.sp-02__cap {
  font-size: 12.6px;
  color: var(--sp-02-mut);
}

.sp-02__chip {
  justify-self: start;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--sp-02-acc);
  padding: 7px 13px;
  border-radius: 99px;
  background: color-mix(in oklch,var(--sp-02-acc) 9%,transparent);
  border: 1px solid color-mix(in oklch,var(--sp-02-acc) 24%,transparent);
}

.sp-02__pagefoot {
  display: grid;
  place-items: center;
  padding: clamp(44px,9vh,110px) 24px;
  border-block-start: 1px solid var(--sp-02-line);
}

.sp-02__pagefootin {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  letter-spacing: .06em;
  color: var(--sp-02-mut);
  text-align: center;
}

.sp-02__bar {
  padding-inline: max(clamp(16px,3vw,26px),calc((100% - 1240px)/2));
}

.sp-02__herotext,
.sp-02__sec {
  padding-inline: max(clamp(22px,5vw,44px),calc((100% - 940px)/2));
}

:root:has(.sp-02) {
  scroll-behavior: smooth;
  scroll-padding-top: 76px;
}

@media (max-width: 720px) {
  .sp-02 {
    --sp-02-bar: 54px;
  }

  .sp-02__nav {
    display: none;
  }

  .sp-02__bar {
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
  }

  .sp-02__sec {
    min-block-size: auto;
  }
}

@media (prefers-reduced-motion: reduce) {
  :root:has(.sp-02) {
    scroll-behavior: auto;
  }

  .sp-02 * {
    transition-duration: .01ms !important;
  }

  .sp-02__bar::after {
    box-shadow: none;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sp-02');
  if (!root || root.dataset.spWired) return;
  root.dataset.spWired = '1';
  const bar = root.querySelector('#sp-02-bar');
  const pct = root.querySelector('#sp-02-pct');
  const native = CSS.supports('animation-timeline', 'scroll()');
  let ticking = false;
  const paint = () => {
    ticking = false;
    const d = document.documentElement;
    const max = d.scrollHeight - d.clientHeight;
    const p = max > 0 ? Math.min(1, Math.max(0, d.scrollTop / max)) : 0;
    if (!native) root.style.setProperty('--sp-02-p', p.toFixed(4));
    const n = Math.round(p * 100);
    pct.textContent = n + '%';
    pct.setAttribute('aria-valuenow', String(n));
  };
  const onScroll = () => { if (!ticking) { ticking = true; requestAnimationFrame(paint); } };
  addEventListener('scroll', onScroll, { passive: true });
  addEventListener('resize', onScroll, { passive: true });
  paint();
  const sentinel = root.querySelector('#sp-02-sentinel');
  new IntersectionObserver(([e]) => { bar.dataset.stuck = String(!e.isIntersecting); },
    { threshold: 0 }).observe(sentinel);
})();
```
