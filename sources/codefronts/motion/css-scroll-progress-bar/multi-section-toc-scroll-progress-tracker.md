---
source: "codefronts"
url: "https://codefronts.com/motion/css-scroll-progress-bar/multi-section-toc-scroll-progress-tracker/"
title: "Multi-Section TOC Scroll Progress Tracker"
section: "motion"
category: "css-scroll-progress-bar"
category_name: "CSS Scroll Progress Bar"
description: "The documentation sidebar, upgraded from a binary highlight to a real per-section meter."
has_js: "true"
---

Here's a working CSS Scroll Progress Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Multi-Section TOC Scroll Progress Tracker
Source: https://codefronts.com/motion/css-scroll-progress-bar/multi-section-toc-scroll-progress-tracker/

The documentation sidebar, upgraded from a binary highlight to a real per-section meter. Each table-of-contents entry has its own progress line that fills as its section passes through the viewport — so you can see not just which chapter you are in, but how far through it you are. Scrollspy without a single observer.
## HTML
```html
<section class="sp-09" aria-label="Multi-section table of contents scroll tracker demo">
  <header class="sp-09__bar">
    <a class="sp-09__brand" href="#sp-09-s1"><span class="sp-09__logo" aria-hidden="true"></span>Docs</a>
    <p class="sp-09__meta">view-timeline · contain</p>
  </header>
  <div class="sp-09__intro">
    <p class="sp-09__intro-eyebrow">scrollspy, minus the observer</p>
    <h2 class="sp-09__intro-title">Every chapter gets its own meter</h2>
    <p class="sp-09__intro-sub">Scroll and watch the sidebar. Each entry fills while its own section is on screen — declaratively, from CSS.</p>
  </div>
  <div class="sp-09__layout">
    <nav class="sp-09__toc" aria-label="On this page">
      <p class="sp-09__toctitle">On this page</p>
      <ul class="sp-09__list">
        <li><a class="sp-09__item" href="#sp-09-s1" data-for="1" aria-current="location"><span class="sp-09__label">Scroll vs view</span><span class="sp-09__meter"><i class="sp-09__mfill"></i></span></a></li>
        <li><a class="sp-09__item" href="#sp-09-s2" data-for="2"><span class="sp-09__label">Named ranges</span><span class="sp-09__meter"><i class="sp-09__mfill"></i></span></a></li>
        <li><a class="sp-09__item" href="#sp-09-s3" data-for="3"><span class="sp-09__label">timeline-scope</span><span class="sp-09__meter"><i class="sp-09__mfill"></i></span></a></li>
        <li><a class="sp-09__item" href="#sp-09-s4" data-for="4"><span class="sp-09__label">Accessibility</span><span class="sp-09__meter"><i class="sp-09__mfill"></i></span></a></li>
        <li><a class="sp-09__item" href="#sp-09-s5" data-for="5"><span class="sp-09__label">Shipping it</span><span class="sp-09__meter"><i class="sp-09__mfill"></i></span></a></li>
      </ul>
      <p class="sp-09__tocfoot">5 sections · ~7 min</p>
    </nav>
    <main class="sp-09__article">
      <section class="sp-09__sec" id="sp-09-s1" data-sec="1">
        <p class="sp-09__kicker">01</p>
        <h3 class="sp-09__h">Scroll timelines vs view timelines</h3>
        <p class="sp-09__p sp-09__p--lede">A scroll timeline measures the container. A view timeline measures one element's trip through that container. Reading progress is the first; a table of contents is the second.</p>
        <p class="sp-09__p">Once that distinction lands, most scroll UI stops needing JavaScript at all.</p>
      </section>
      <section class="sp-09__sec" id="sp-09-s2" data-sec="2">
        <p class="sp-09__kicker">02</p>
        <h3 class="sp-09__h">cover, contain, entry, exit</h3>
        <p class="sp-09__p"><code>cover</code> is the full journey from first pixel in to last pixel out. <code>contain</code> is the stretch where the element fills the port — the part a reader would describe as being in this section.</p>
        <p class="sp-09__p">Choosing the right phase is most of the design work; the rest is one keyframe block.</p>
      </section>
      <section class="sp-09__sec" id="sp-09-s3" data-sec="3">
        <p class="sp-09__kicker">03</p>
        <h3 class="sp-09__h">Names need scope</h3>
        <p class="sp-09__p">A timeline named on a section is private to that section. <code>timeline-scope</code> on the layout wrapper publishes it, which is what lets a sidebar link consume a timeline declared in the article.</p>
        <figure class="sp-09__fig">
          <img class="sp-09__img" src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&amp;fit=crop&amp;w=1400&amp;q=70" alt="A network of glowing blue connections over a dark surface" loading="lazy" decoding="async">
          <figcaption class="sp-09__cap">Scope turns isolated timelines into a coordinated interface.</figcaption>
        </figure>
      </section>
      <section class="sp-09__sec" id="sp-09-s4" data-sec="4">
        <p class="sp-09__kicker">04</p>
        <h3 class="sp-09__h">Say it out loud</h3>
        <p class="sp-09__p">Visual highlighting is not orientation. The current entry carries <code>aria-current="location"</code>, the correct token for a within-page position, and every target has <code>scroll-margin-top</code> so anchor jumps clear the header.</p>
      </section>
      <section class="sp-09__sec" id="sp-09-s5" data-sec="5">
        <p class="sp-09__kicker">05</p>
        <h3 class="sp-09__h">Ship it today</h3>
        <p class="sp-09__p">Modern engines run the CSS path. Everything else gets one observer and the same markup. No page has to choose.</p>
        <p class="sp-09__chip">5 timelines · 1 scope · 1 aria attribute</p>
      </section>
    </main>
  </div>
  <footer class="sp-09__pagefoot"><p class="sp-09__pagefootin">Scroll progress pattern 09 of 18 · codefronts.com</p></footer>
</section>
```
## CSS
```css
.sp-09 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--sp-09-bg);
  --sp-09-bg: oklch(0.15 0.018 260);
  --sp-09-surface: oklch(0.2 0.022 260);
  --sp-09-ink: oklch(0.97 0.005 260);
  --sp-09-mut: oklch(0.71 0.018 260);
  --sp-09-acc: oklch(0.78 0.16 195);
  --sp-09-line: oklch(1 0 0/.12);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--sp-09-ink);
  -webkit-font-smoothing: antialiased;
}

.sp-09 *,
.sp-09 *::before,
.sp-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sp-09__bar {
  position: sticky;
  inset-block-start: 0;
  z-index: 40;
  display: flex;
  align-items: center;
  gap: 14px;
  min-block-size: 58px;
  background: color-mix(in oklch,var(--sp-09-bg) 78%,transparent);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border-block-end: 1px solid var(--sp-09-line);
}

.sp-09__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 15px;
  font-weight: 730;
  letter-spacing: -.02em;
  color: inherit;
  text-decoration: none;
}

.sp-09__brand:focus-visible,
.sp-09__item:focus-visible {
  outline: 2px solid var(--sp-09-acc);
  outline-offset: 3px;
  border-radius: 8px;
}

.sp-09__logo {
  inline-size: 18px;
  block-size: 18px;
  border-radius: 5px;
  background: linear-gradient(140deg,var(--sp-09-acc),oklch(0.6 0.2 260));
}

.sp-09__meta {
  margin-inline-start: auto;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .08em;
  color: var(--sp-09-mut);
}

.sp-09__intro {
  display: grid;
  gap: 14px;
  justify-items: center;
  text-align: center;
  padding-block: clamp(48px,10vh,110px) clamp(28px,6vh,60px);
  background: radial-gradient(80% 50% at 50% 0%,oklch(0.26 0.07 210),transparent);
}

.sp-09__intro-eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--sp-09-acc);
}

.sp-09__intro-title {
  font-size: clamp(32px,5.8vw,66px);
  line-height: 1;
  letter-spacing: -.04em;
  font-weight: 730;
  max-inline-size: 20ch;
  text-wrap: balance;
}

.sp-09__intro-sub {
  font-size: clamp(14.5px,1.6vw,18px);
  line-height: 1.55;
  color: var(--sp-09-mut);
  max-inline-size: 52ch;
  text-wrap: pretty;
}

.sp-09__layout {
  timeline-scope: --sp-09-s1,--sp-09-s2,--sp-09-s3,--sp-09-s4,--sp-09-s5;
  display: grid;
  grid-template-columns: minmax(190px,230px) minmax(0,1fr);
  gap: clamp(20px,4vw,56px);
  align-items: start;
}

.sp-09__toc {
  position: sticky;
  inset-block-start: 78px;
  align-self: start;
  display: grid;
  gap: 10px;
  padding: 16px;
  border: 1px solid var(--sp-09-line);
  border-radius: 16px;
  background: color-mix(in oklch,var(--sp-09-surface) 70%,transparent);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
}

.sp-09__toctitle {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10px;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--sp-09-mut);
}

.sp-09__list {
  list-style: none;
  display: grid;
  gap: 3px;
}

.sp-09__item {
  display: grid;
  gap: 6px;
  padding: 8px 10px;
  border-radius: 10px;
  text-decoration: none;
  color: var(--sp-09-mut);
  transition: color .2s ease,background .2s ease;
}

.sp-09__item:hover {
  color: var(--sp-09-ink);
  background: oklch(1 0 0/.05);
}

.sp-09__item[aria-current="location"] {
  color: var(--sp-09-ink);
  background: oklch(1 0 0/.07);
}

.sp-09__label {
  font-size: 13.4px;
  font-weight: 620;
  line-height: 1.25;
}

.sp-09__meter {
  display: block;
  block-size: 2px;
  border-radius: 99px;
  background: oklch(1 0 0/.14);
  overflow: hidden;
}

.sp-09__mfill {
  display: block;
  block-size: 100%;
  transform-origin: 0 50%;
  transform: scaleX(var(--sp-09-m,0));
  background: var(--sp-09-acc);
  box-shadow: 0 0 8px -1px var(--sp-09-acc);
}

@supports (animation-timeline: view()) {
  .sp-09__mfill {
    transform: scaleX(0);
    animation: sp-09-fill linear both;
    animation-range: contain 0% contain 100%;
  }

  .sp-09__item[data-for="1"] .sp-09__mfill {
    animation-timeline: --sp-09-s1;
  }

  .sp-09__item[data-for="2"] .sp-09__mfill {
    animation-timeline: --sp-09-s2;
  }

  .sp-09__item[data-for="3"] .sp-09__mfill {
    animation-timeline: --sp-09-s3;
  }

  .sp-09__item[data-for="4"] .sp-09__mfill {
    animation-timeline: --sp-09-s4;
  }

  .sp-09__item[data-for="5"] .sp-09__mfill {
    animation-timeline: --sp-09-s5;
  }

  .sp-09__sec[data-sec="1"] {
    view-timeline-name: --sp-09-s1;
  }

  .sp-09__sec[data-sec="2"] {
    view-timeline-name: --sp-09-s2;
  }

  .sp-09__sec[data-sec="3"] {
    view-timeline-name: --sp-09-s3;
  }

  .sp-09__sec[data-sec="4"] {
    view-timeline-name: --sp-09-s4;
  }

  .sp-09__sec[data-sec="5"] {
    view-timeline-name: --sp-09-s5;
  }
}

@keyframes sp-09-fill {
  from {
    transform: scaleX(0);
  }

  to {
    transform: scaleX(1);
  }
}

.sp-09__tocfoot {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10.5px;
  letter-spacing: .08em;
  color: var(--sp-09-mut);
  opacity: .75;
}

.sp-09__article {
  display: grid;
  min-inline-size: 0;
}

.sp-09__sec {
  scroll-margin-top: 78px;
  display: grid;
  gap: 12px;
  align-content: center;
  min-block-size: 80svh;
  padding-block: clamp(24px,4vw,48px);
  border-block-end: 1px solid var(--sp-09-line);
}

.sp-09__sec:last-child {
  border-block-end: 0;
}

.sp-09__kicker {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .13em;
  color: var(--sp-09-acc);
}

.sp-09__h {
  font-size: clamp(22px,3.1vw,33px);
  line-height: 1.1;
  letter-spacing: -.032em;
  font-weight: 700;
  text-wrap: balance;
}

.sp-09__p {
  max-inline-size: 58ch;
  font-size: 15.8px;
  line-height: 1.7;
  color: var(--sp-09-mut);
  text-wrap: pretty;
}

.sp-09__p--lede {
  font-size: 18px;
  color: var(--sp-09-ink);
}

.sp-09__p code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .85em;
  background: oklch(1 0 0/.1);
  padding: 2px 6px;
  border-radius: 5px;
}

.sp-09__fig {
  display: grid;
  gap: 9px;
  max-inline-size: 66ch;
}

.sp-09__img {
  inline-size: 100%;
  aspect-ratio: 16/7;
  object-fit: cover;
  display: block;
  border-radius: 14px;
  background: linear-gradient(135deg,oklch(0.45 0.12 220),oklch(0.28 0.06 265));
}

.sp-09__cap {
  font-size: 12.6px;
  color: var(--sp-09-mut);
}

.sp-09__chip {
  justify-self: start;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--sp-09-acc);
  padding: 7px 13px;
  border-radius: 99px;
  background: color-mix(in oklch,var(--sp-09-acc) 14%,transparent);
  border: 1px solid color-mix(in oklch,var(--sp-09-acc) 30%,transparent);
}

.sp-09__pagefoot {
  display: grid;
  place-items: center;
  padding: clamp(44px,9vh,110px) 24px;
  border-block-start: 1px solid var(--sp-09-line);
}

.sp-09__pagefootin {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  letter-spacing: .06em;
  color: var(--sp-09-mut);
  text-align: center;
}

.sp-09__bar {
  padding-inline: max(clamp(16px,3vw,26px),calc((100% - 1240px)/2));
}

.sp-09__intro,
.sp-09__layout {
  padding-inline: max(clamp(20px,4vw,40px),calc((100% - 1160px)/2));
}

:root:has(.sp-09) {
  scroll-behavior: smooth;
  scroll-padding-top: 78px;
}

@media (max-width: 820px) {
  .sp-09__layout {
    grid-template-columns: minmax(0,1fr);
  }

  .sp-09__toc {
    position: sticky;
    inset-block-start: 58px;
    z-index: 30;
  }

  .sp-09__list {
    grid-auto-flow: column;
    grid-auto-columns: minmax(120px,1fr);
    overflow-x: auto;
    padding-block-end: 4px;
  }

  .sp-09__sec {
    min-block-size: auto;
  }
}

@media (prefers-reduced-motion: reduce) {
  :root:has(.sp-09) {
    scroll-behavior: auto;
  }

  .sp-09 * {
    transition-duration: .01ms !important;
  }

  .sp-09__mfill {
    box-shadow: none;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sp-09');
  if (!root || root.dataset.spWired) return;
  root.dataset.spWired = '1';
  const items = [...root.querySelectorAll('.sp-09__item')];
  const secs = [...root.querySelectorAll('.sp-09__sec[data-sec]')];
  const native = CSS.supports('animation-timeline', 'view()');
  let ticking = false;
  const paint = () => {
    ticking = false;
    const vh = innerHeight || document.documentElement.clientHeight;
    let bestIdx = 0, bestTop = Infinity;
    secs.forEach((sec, i) => {
      const r = sec.getBoundingClientRect();
      if (!native) {
        const span = r.height + vh;
        const done = Math.min(1, Math.max(0, (vh - r.top) / span));
        const item = items[i];
        if (item) item.style.setProperty('--sp-09-m', done.toFixed(4));
      }
      const dist = Math.abs(r.top - 90);
      if (r.bottom > 120 && dist < bestTop) { bestTop = dist; bestIdx = i; }
    });
    items.forEach((it, i) => {
      if (i === bestIdx) it.setAttribute('aria-current', 'location');
      else it.removeAttribute('aria-current');
    });
  };
  const onScroll = () => { if (!ticking) { ticking = true; requestAnimationFrame(paint); } };
  addEventListener('scroll', onScroll, { passive: true });
  addEventListener('resize', onScroll, { passive: true });
  paint();
})();
```
