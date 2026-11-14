---
source: "codefronts"
url: "https://codefronts.com/motion/css-number-counter-animations/scroll-triggered-count-up-statistics-grid/"
title: "Scroll-Triggered Count Up Statistics Grid"
section: "motion"
category: "css-number-counter-animations"
category_name: "CSS Number Counter Animations"
description: "Stats that count only when the visitor actually reaches them — the single most-requested counter behaviour on the web."
has_js: "true"
---

Here's a working CSS Number Counter Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Scroll-Triggered Count Up Statistics Grid
Source: https://codefronts.com/motion/css-number-counter-animations/scroll-triggered-count-up-statistics-grid/

Stats that count only when the visitor actually reaches them — the single most-requested counter behaviour on the web. This build ships both routes: a pure-CSS animation-timeline: view() path where the number is literally scrubbed by the scroll position, and an IntersectionObserver fallback that fires the same animation once per card in every other browser. Scroll the panel to watch them run.
## HTML
```html
<section class="cnc-02" aria-label="Scroll triggered count up statistics grid demo">
  <div class="cnc-02__stage">
    <div class="cnc-02__scroller" tabindex="0" aria-label="Scrollable statistics panel">
      <div class="cnc-02__lead">
        <p class="cnc-02__eyebrow">Scroll this panel ↓</p>
        <h2 class="cnc-02__head">Impact report, 2026</h2>
        <p class="cnc-02__note">Each figure counts up as its card enters the viewport — scroll-driven where supported, IntersectionObserver everywhere else.</p>
      </div>
      <div class="cnc-02__grid">
        <article class="cnc-02__card" style="--cnc-02-i:0">
          <span class="cnc-02__val"><span class="cnc-02__num" style="--cnc-02-to:284" aria-hidden="true"></span><span class="cnc-02__suf">+</span></span>
          <h3 class="cnc-02__key">Enterprise migrations</h3>
          <p class="cnc-02__sub">Zero-downtime cutovers shipped this year</p>
        </article>
        <article class="cnc-02__card" style="--cnc-02-i:1">
          <span class="cnc-02__val"><span class="cnc-02__num" style="--cnc-02-to:63" aria-hidden="true"></span><span class="cnc-02__suf">%</span></span>
          <h3 class="cnc-02__key">Faster onboarding</h3>
          <p class="cnc-02__sub">Median time-to-first-value vs. 2025</p>
        </article>
        <article class="cnc-02__card" style="--cnc-02-i:2">
          <span class="cnc-02__val"><span class="cnc-02__num" style="--cnc-02-to:178" aria-hidden="true"></span><span class="cnc-02__suf">M</span></span>
          <h3 class="cnc-02__key">Events processed daily</h3>
          <p class="cnc-02__sub">Peak sustained ingest across regions</p>
        </article>
        <article class="cnc-02__card" style="--cnc-02-i:3">
          <span class="cnc-02__val"><span class="cnc-02__num" style="--cnc-02-to:47" aria-hidden="true"></span><span class="cnc-02__suf">countries</span></span>
          <h3 class="cnc-02__key">Regional coverage</h3>
          <p class="cnc-02__sub">Data residency zones now available</p>
        </article>
      </div>
      <p class="cnc-02__chip" aria-hidden="true">animation-timeline: view() · animation-range: entry/cover · IntersectionObserver fallback</p>
    </div>
  </div>
</section>
```
## CSS
```css
@property --cnc-02-n {
  syntax: '<integer>';
  inherits: false;
  initial-value: 0;
}

.cnc-02,
.cnc-02 *,
.cnc-02 *::before,
.cnc-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cnc-02 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --cnc-02-bg: oklch(0.96 0.008 250);
  --cnc-02-card: oklch(1 0 0);
  --cnc-02-ink: oklch(0.22 0.02 265);
  --cnc-02-mut: oklch(0.55 0.02 265);
  --cnc-02-acc: oklch(0.55 0.22 275);
  background: var(--cnc-02-bg);
  color: var(--cnc-02-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
}

.cnc-02__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(16px,4vw,44px);
}

.cnc-02__scroller {
  width: min(100%,860px);
  height: min(78vh,620px);
  overflow: auto;
  overscroll-behavior: contain;
  scroll-behavior: smooth;
  border-radius: 22px;
  background: var(--cnc-02-card);
  box-shadow: 0 1px 2px oklch(0 0 0/.06),0 24px 60px oklch(0.3 0.05 275/.14);
  padding: clamp(20px,4vw,38px);
}

.cnc-02__scroller:focus-visible {
  outline: 3px solid var(--cnc-02-acc);
  outline-offset: 3px;
}

.cnc-02__lead {
  max-width: 46ch;
  padding-bottom: clamp(30px,10vh,90px);
  border-bottom: 1px solid oklch(0 0 0/.07);
}

.cnc-02__eyebrow {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--cnc-02-acc);
}

.cnc-02__head {
  margin-top: 10px;
  font-size: clamp(24px,3.4vw,34px);
  font-weight: 680;
  letter-spacing: -.03em;
}

.cnc-02__note {
  margin-top: 10px;
  font-size: 14px;
  line-height: 1.55;
  color: var(--cnc-02-mut);
  text-wrap: pretty;
}

.cnc-02__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(220px,1fr));
  gap: 14px;
  padding: clamp(24px,6vh,60px) 0;
}

.cnc-02__card {
  padding: 22px;
  border-radius: 16px;
  background: color-mix(in oklch,var(--cnc-02-acc) 5%,var(--cnc-02-card));
  border: 1px solid color-mix(in oklch,var(--cnc-02-acc) 16%,transparent);
  transition: transform .3s cubic-bezier(.16,1,.3,1),box-shadow .3s;
}

.cnc-02__card:hover {
  transform: translateY(-3px);
  box-shadow: 0 12px 30px oklch(0.3 0.05 275/.16);
}

.cnc-02__val {
  display: flex;
  align-items: baseline;
  gap: 2px;
  font-size: clamp(34px,5vw,48px);
  font-weight: 720;
  letter-spacing: -.045em;
  line-height: 1;
  color: var(--cnc-02-acc);
  font-variant-numeric: tabular-nums;
  font-feature-settings: 'tnum' 1;
}

.cnc-02__num {
  counter-reset: cnc-02-n var(--cnc-02-n);
}

.cnc-02__num::after {
  content: counter(cnc-02-n);
}

.cnc-02__suf {
  font-size: .42em;
  font-weight: 640;
  letter-spacing: 0;
}

.cnc-02__key {
  margin-top: 14px;
  font-size: 15px;
  font-weight: 640;
  letter-spacing: -.01em;
}

.cnc-02__sub {
  margin-top: 5px;
  font-size: 13px;
  line-height: 1.5;
  color: var(--cnc-02-mut);
}

@keyframes cnc-02-count {
  from {
    --cnc-02-n: 0;
  }

  to {
    --cnc-02-n: var(--cnc-02-to);
  }
}

@keyframes cnc-02-rise {
  from {
    opacity: 0;
    transform: translateY(18px);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

.cnc-02__card[data-run] .cnc-02__num {
  animation: cnc-02-count 1.9s cubic-bezier(.16,1,.3,1) both;
}

.cnc-02__card[data-run] {
  animation: cnc-02-rise .7s cubic-bezier(.16,1,.3,1) both;
}

@supports (animation-timeline: view()) {
  .cnc-02__num {
    animation: cnc-02-count linear both;
    animation-timeline: view();
    animation-range: entry 18% cover 44%;
  }

  .cnc-02__card {
    animation: cnc-02-rise linear both;
    animation-timeline: view();
    animation-range: entry 5% entry 60%;
  }
}

.cnc-02__chip {
  margin: 6px 0 4px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--cnc-02-mut);
  padding: 8px 14px;
  border: 1px dashed oklch(0 0 0/.14);
  border-radius: 99px;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .cnc-02__num,
    .cnc-02__card {
    animation-duration: 1ms !important;
    animation-timeline: auto !important;
  }
}
```

## JavaScript
```js
(() => {
  const supportsView = CSS.supports('animation-timeline', 'view()');
  document.querySelectorAll('.cnc-02').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const cards = [...root.querySelectorAll('.cnc-02__card')];
    if (supportsView) return;                       // CSS already handles it
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (!e.isIntersecting) return;
        e.target.style.animationDelay = (e.target.style.getPropertyValue('--cnc-02-i') || 0) * 90 + 'ms';
        e.target.dataset.run = '1';
        io.unobserve(e.target);
      });
    }, { root: root.querySelector('.cnc-02__scroller'), threshold: 0.35, rootMargin: '0px 0px -8% 0px' });
    cards.forEach((c) => io.observe(c));
  });
})();
```
