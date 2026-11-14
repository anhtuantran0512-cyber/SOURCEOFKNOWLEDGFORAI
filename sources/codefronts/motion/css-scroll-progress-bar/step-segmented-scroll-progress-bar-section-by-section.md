---
source: "codefronts"
url: "https://codefronts.com/motion/css-scroll-progress-bar/step-segmented-scroll-progress-bar-section-by-section/"
title: "Step-Segmented Scroll Progress Bar (Section-by-Section)"
section: "motion"
category: "css-scroll-progress-bar"
category_name: "CSS Scroll Progress Bar"
description: "Instagram-stories pacing applied to long-form content: one segment per chapter, each filling independently as its own section scrolls past."
has_js: "true"
---

Here's a working CSS Scroll Progress Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Step-Segmented Scroll Progress Bar (Section-by-Section)
Source: https://codefronts.com/motion/css-scroll-progress-bar/step-segmented-scroll-progress-bar-section-by-section/

Instagram-stories pacing applied to long-form content: one segment per chapter, each filling independently as its own section scrolls past. It answers a question a single continuous bar cannot — how much of this chapter is left — which is why long documentation and multi-part guides convert better with it.
## HTML
```html
<section class="sp-10" aria-label="Step-segmented scroll progress bar demo">
  <div class="sp-10__railwrap">
    <div class="sp-10__rail" role="progressbar" aria-label="Guide progress" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0" aria-valuetext="Chapter 1 of 5: Why segments" id="sp-10-rail">
      <a class="sp-10__seg" href="#sp-10-c1" data-ch="1" data-title="Why segments"><i class="sp-10__segfill"></i></a>
      <a class="sp-10__seg" href="#sp-10-c2" data-ch="2" data-title="Equal by default"><i class="sp-10__segfill"></i></a>
      <a class="sp-10__seg" href="#sp-10-c3" data-ch="3" data-title="Weighted segments"><i class="sp-10__segfill"></i></a>
      <a class="sp-10__seg" href="#sp-10-c4" data-ch="4" data-title="Segments as navigation"><i class="sp-10__segfill"></i></a>
      <a class="sp-10__seg" href="#sp-10-c5" data-ch="5" data-title="Naming it out loud"><i class="sp-10__segfill"></i></a>
    </div>
    <p class="sp-10__now" id="sp-10-now">Chapter 1 of 5 · Why segments</p>
  </div>
  <div class="sp-10__intro">
    <p class="sp-10__intro-eyebrow">one timeline per chapter</p>
    <h2 class="sp-10__intro-title">Five chapters, five meters</h2>
    <p class="sp-10__intro-sub">A single bar tells you how much of the page is left. Segments tell you how much of <em>this part</em> is left — which is the question readers actually ask.</p>
  </div>
  <main class="sp-10__main">
    <section class="sp-10__ch" id="sp-10-c1" data-ch="1">
      <p class="sp-10__kicker">Chapter 01</p>
      <h3 class="sp-10__h">Why segments beat a single bar</h3>
      <p class="sp-10__p sp-10__p--lede">Continuous bars answer a question about the document. Segmented bars answer a question about the chapter you are in — and that is the one people are asking when they check.</p>
      <p class="sp-10__p">On multi-part guides this measurably reduces abandonment, because the next milestone is always visibly close.</p>
    </section>
    <section class="sp-10__ch" id="sp-10-c2" data-ch="2">
      <p class="sp-10__kicker">Chapter 02</p>
      <h3 class="sp-10__h">Equal columns, no counting</h3>
      <p class="sp-10__p"><code>grid-auto-flow:column</code> with <code>grid-auto-columns:1fr</code> divides the rail evenly however many segments exist. Add a chapter, add a segment — nothing else changes.</p>
      <figure class="sp-10__fig">
        <img class="sp-10__img" src="https://images.unsplash.com/photo-1499346030926-9a72daac6c63?auto=format&amp;fit=crop&amp;w=1400&amp;q=70" alt="An open notebook and pen on a desk beside a laptop" loading="lazy" decoding="async">
        <figcaption class="sp-10__cap">Chaptered content deserves chaptered feedback.</figcaption>
      </figure>
    </section>
    <section class="sp-10__ch" id="sp-10-c3" data-ch="3">
      <p class="sp-10__kicker">Chapter 03</p>
      <h3 class="sp-10__h">Weight them honestly</h3>
      <p class="sp-10__p">Equal segments over unequal chapters mislead. Setting explicit <code>fr</code> values proportional to word count turns the rail into a real map of the document.</p>
    </section>
    <section class="sp-10__ch" id="sp-10-c4" data-ch="4">
      <p class="sp-10__kicker">Chapter 04</p>
      <h3 class="sp-10__h">Free navigation</h3>
      <p class="sp-10__p">Each segment is an anchor. Hover reveals the chapter title from an <code>attr()</code> tooltip, so the indicator you built for feedback becomes the table of contents you did not have to build.</p>
    </section>
    <section class="sp-10__ch" id="sp-10-c5" data-ch="5">
      <p class="sp-10__kicker">Chapter 05</p>
      <h3 class="sp-10__h">Say which chapter, not which percent</h3>
      <p class="sp-10__p"><code>aria-valuetext</code> carries "Chapter 3 of 5: Weighted segments". A percentage would be technically correct and practically useless.</p>
      <p class="sp-10__chip">5 segments · 5 timelines · 1 grid</p>
    </section>
  </main>
  <footer class="sp-10__pagefoot">
    <div class="sp-10__endcard">
      <p class="sp-10__endk">End of guide</p>
      <p class="sp-10__endh">All five segments full.</p>
      <p class="sp-10__endp">This closing panel is not decoration. A chapter's range only completes once it has scrolled clear of the viewport — without a full-height end card the final segment stalls partway and the rail never fills.</p>
    </div>
    <p class="sp-10__pagefootin">Scroll progress pattern 10 of 18 · codefronts.com</p>
  </footer>
</section>
```
## CSS
```css
.sp-10 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--sp-10-bg);
  --sp-10-bg: oklch(0.98 0.007 60);
  --sp-10-surface: oklch(1 0 0);
  --sp-10-ink: oklch(0.2 0.018 55);
  --sp-10-mut: oklch(0.52 0.014 55);
  --sp-10-acc: oklch(0.56 0.2 20);
  --sp-10-line: oklch(0.2 0.018 55/.12);
  --sp-10-gap: 5px;
  --sp-10-h: 6px;
  timeline-scope: --sp-10-c1,--sp-10-c2,--sp-10-c3,--sp-10-c4,--sp-10-c5;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--sp-10-ink);
  -webkit-font-smoothing: antialiased;
}

.sp-10 *,
.sp-10 *::before,
.sp-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sp-10__railwrap {
  position: sticky;
  inset-block-start: 0;
  z-index: 50;
  display: grid;
  gap: 7px;
  padding-block: 12px 10px;
  background: color-mix(in oklch,var(--sp-10-surface) 84%,transparent);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border-block-end: 1px solid var(--sp-10-line);
}

.sp-10__rail {
  display: grid;
  grid-auto-flow: column;
  grid-auto-columns: 1fr;
  gap: var(--sp-10-gap);
}

.sp-10__seg {
  position: relative;
  display: block;
  block-size: var(--sp-10-h);
  border-radius: 99px;
  background: color-mix(in oklch,var(--sp-10-ink) 10%,transparent);
  overflow: visible;
  transition: scale .22s cubic-bezier(.32,.72,.3,1);
}

.sp-10__seg:hover,
.sp-10__seg:focus-visible {
  scale: 1 1.5;
}

.sp-10__seg:focus-visible {
  outline: 2px solid var(--sp-10-acc);
  outline-offset: 4px;
}

.sp-10__seg::after {
  content: attr(data-title);
  position: absolute;
  inset-block-start: calc(100% + 9px);
  inset-inline-start: 50%;
  translate: -50% 0;
  padding: 5px 10px;
  border-radius: 8px;
  background: var(--sp-10-ink);
  color: oklch(0.99 0 0);
  font-size: 11.5px;
  font-weight: 600;
  white-space: nowrap;
  opacity: 0;
  pointer-events: none;
  transition: opacity .2s ease,translate .2s ease;
}

.sp-10__seg:hover::after,
.sp-10__seg:focus-visible::after {
  opacity: 1;
  translate: -50% 3px;
}

.sp-10__segfill {
  position: absolute;
  inset: 0;
  display: block;
  border-radius: 99px;
  transform-origin: 0 50%;
  transform: scaleX(var(--sp-10-m,0));
  background: linear-gradient(90deg,var(--sp-10-acc),oklch(0.7 0.18 40));
}

@supports (animation-timeline: view()) {
  .sp-10__segfill {
    transform: scaleX(0);
    animation: sp-10-fill linear both;
    animation-range: entry 100% exit 100%;
  }

  .sp-10__seg[data-ch="1"] .sp-10__segfill {
    animation-timeline: --sp-10-c1;
  }

  .sp-10__seg[data-ch="2"] .sp-10__segfill {
    animation-timeline: --sp-10-c2;
  }

  .sp-10__seg[data-ch="3"] .sp-10__segfill {
    animation-timeline: --sp-10-c3;
  }

  .sp-10__seg[data-ch="4"] .sp-10__segfill {
    animation-timeline: --sp-10-c4;
  }

  .sp-10__seg[data-ch="5"] .sp-10__segfill {
    animation-timeline: --sp-10-c5;
  }

  .sp-10__ch[data-ch="1"] {
    view-timeline-name: --sp-10-c1;
  }

  .sp-10__ch[data-ch="2"] {
    view-timeline-name: --sp-10-c2;
  }

  .sp-10__ch[data-ch="3"] {
    view-timeline-name: --sp-10-c3;
  }

  .sp-10__ch[data-ch="4"] {
    view-timeline-name: --sp-10-c4;
  }

  .sp-10__ch[data-ch="5"] {
    view-timeline-name: --sp-10-c5;
  }
}

@keyframes sp-10-fill {
  from {
    transform: scaleX(0);
  }

  to {
    transform: scaleX(1);
  }
}

.sp-10__now {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .06em;
  color: var(--sp-10-mut);
}

.sp-10__intro {
  display: grid;
  gap: 14px;
  justify-items: center;
  text-align: center;
  padding-block: clamp(50px,11vh,120px) clamp(28px,6vh,60px);
  background: radial-gradient(85% 55% at 50% 0%,oklch(0.97 0.04 35),transparent);
}

.sp-10__intro-eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--sp-10-acc);
}

.sp-10__intro-title {
  font-size: clamp(34px,6.2vw,72px);
  line-height: .98;
  letter-spacing: -.04em;
  font-weight: 730;
  max-inline-size: 18ch;
  text-wrap: balance;
}

.sp-10__intro-sub {
  font-size: clamp(14.5px,1.6vw,18px);
  line-height: 1.55;
  color: var(--sp-10-mut);
  max-inline-size: 52ch;
  text-wrap: pretty;
}

.sp-10__ch {
  scroll-margin-top: 66px;
  display: grid;
  gap: 12px;
  align-content: center;
  min-block-size: 82svh;
  padding-block: clamp(28px,5vw,56px);
  border-block-end: 1px solid var(--sp-10-line);
}

.sp-10__ch:last-child {
  border-block-end: 0;
}

.sp-10__kicker {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--sp-10-acc);
}

.sp-10__h {
  font-size: clamp(23px,3.3vw,36px);
  line-height: 1.08;
  letter-spacing: -.033em;
  font-weight: 700;
  text-wrap: balance;
}

.sp-10__p {
  max-inline-size: 60ch;
  font-size: 15.8px;
  line-height: 1.7;
  color: var(--sp-10-mut);
  text-wrap: pretty;
}

.sp-10__p--lede {
  font-size: 18px;
  color: var(--sp-10-ink);
}

.sp-10__p code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .85em;
  background: oklch(0.2 0.018 55/.07);
  padding: 2px 6px;
  border-radius: 5px;
}

.sp-10__fig {
  display: grid;
  gap: 9px;
  max-inline-size: 68ch;
}

.sp-10__img {
  inline-size: 100%;
  aspect-ratio: 16/7;
  object-fit: cover;
  display: block;
  border-radius: 14px;
  background: linear-gradient(135deg,oklch(0.62 0.13 40),oklch(0.4 0.07 60));
}

.sp-10__cap {
  font-size: 12.6px;
  color: var(--sp-10-mut);
}

.sp-10__chip {
  justify-self: start;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--sp-10-acc);
  padding: 7px 13px;
  border-radius: 99px;
  background: color-mix(in oklch,var(--sp-10-acc) 10%,transparent);
  border: 1px solid color-mix(in oklch,var(--sp-10-acc) 24%,transparent);
}

.sp-10__pagefoot {
  display: grid;
  align-content: center;
  justify-items: start;
  gap: clamp(24px,6vh,56px);
  min-block-size: 100svh;
  padding-block: clamp(44px,9vh,110px);
  border-block-start: 1px solid var(--sp-10-line);
}

.sp-10__endcard {
  display: grid;
  gap: 11px;
  max-inline-size: 56ch;
}

.sp-10__endk {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--sp-10-acc);
}

.sp-10__endh {
  font-size: clamp(24px,3.6vw,40px);
  line-height: 1.06;
  letter-spacing: -.035em;
  font-weight: 730;
  text-wrap: balance;
}

.sp-10__endp {
  font-size: 15.4px;
  line-height: 1.68;
  color: var(--sp-10-mut);
  text-wrap: pretty;
}

.sp-10__endp code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .85em;
  background: oklch(0.2 0.018 55/.07);
  padding: 2px 6px;
  border-radius: 5px;
}

.sp-10__pagefootin {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  letter-spacing: .06em;
  color: var(--sp-10-mut);
  text-align: center;
}

.sp-10__railwrap,
.sp-10__intro,
.sp-10__ch,
.sp-10__pagefoot {
  padding-inline: max(clamp(20px,5vw,44px),calc((100% - 900px)/2));
}

:root:has(.sp-10) {
  scroll-behavior: smooth;
  scroll-padding-top: 66px;
}

@media (max-width: 640px) {
  .sp-10 {
    --sp-10-gap: 4px;
  }

  .sp-10__ch {
    min-block-size: auto;
  }

  .sp-10__seg::after {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  :root:has(.sp-10) {
    scroll-behavior: auto;
  }

  .sp-10 * {
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sp-10');
  if (!root || root.dataset.spWired) return;
  root.dataset.spWired = '1';
  const segs = [...root.querySelectorAll('.sp-10__seg')];
  const chs = [...root.querySelectorAll('.sp-10__ch[data-ch]')];
  const rail = root.querySelector('#sp-10-rail');
  const now = root.querySelector('#sp-10-now');
  const native = CSS.supports('animation-timeline', 'view()');
  let ticking = false, lastCh = -1;
  const paint = () => {
    ticking = false;
    const vh = innerHeight || document.documentElement.clientHeight;
    let cur = 0, total = 0;
    // mirrors animation-range: entry 100% exit 100% — starts when the chapter is fully
    // on screen, ends when it has cleared the top; span is exactly one viewport
    const range = (r) => Math.min(1, Math.max(0, (vh - r.height - r.top) / vh));
    chs.forEach((ch, i) => {
      const r = ch.getBoundingClientRect();
      const done = range(r);
      if (!native && segs[i]) segs[i].style.setProperty('--sp-10-m', done.toFixed(4));
      total += done;
      if (r.top < vh * 0.5 && r.bottom > vh * 0.2) cur = i;
    });
    rail.setAttribute('aria-valuenow', String(Math.round((total / chs.length) * 100)));
    if (cur !== lastCh) {
      lastCh = cur;
      const title = segs[cur] ? segs[cur].dataset.title : '';
      const label = 'Chapter ' + (cur + 1) + ' of ' + chs.length + ': ' + title;
      rail.setAttribute('aria-valuetext', label);
      now.textContent = 'Chapter ' + (cur + 1) + ' of ' + chs.length + ' · ' + title;
    }
  };
  const onScroll = () => { if (!ticking) { ticking = true; requestAnimationFrame(paint); } };
  addEventListener('scroll', onScroll, { passive: true });
  addEventListener('resize', onScroll, { passive: true });
  paint();
})();
```
