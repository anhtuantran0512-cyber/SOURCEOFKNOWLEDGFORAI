---
source: "codefronts"
url: "https://codefronts.com/motion/css-number-counter-animations/reading-progress-counter/"
title: "Blog Reading Time & Scroll Progress Indicator"
section: "motion"
category: "css-number-counter-animations"
category_name: "CSS Number Counter Animations"
description: "A reading-progress header with a live percentage — and not one line of JavaScript."
has_js: "true"
---

Here's a working CSS Number Counter Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Blog Reading Time & Scroll Progress Indicator
Source: https://codefronts.com/motion/css-number-counter-animations/reading-progress-counter/

A reading-progress header with a live percentage — and not one line of JavaScript. animation-timeline: scroll() ties both the bar and a counting percentage directly to the scroll position of the article, so the number is scrubbed by the reader's own gesture. Minutes remaining tick down the same way.
## HTML
```html
<section class="cnc-17" aria-label="Blog reading time and scroll progress indicator demo">
  <div class="cnc-17__stage">
    <div class="cnc-17__reader">
      <header class="cnc-17__bar">
        <div class="cnc-17__meta">
          <p class="cnc-17__kicker">Engineering · 8 min read</p>
          <h3 class="cnc-17__title">Why your counters should live in CSS</h3>
        </div>
        <div class="cnc-17__readout">
          <span class="cnc-17__pct" aria-hidden="true"></span>
          <span class="cnc-17__mins" aria-hidden="true"></span>
        </div>
        <span class="cnc-17__progress" aria-hidden="true"><b></b></span>
      </header>
      <article class="cnc-17__article" tabindex="0" aria-label="Article body, scroll to see progress">
        <p class="cnc-17__lead">Scroll this column. The bar, the percentage and the minutes remaining are all driven by the same scroll timeline — no listener, no JavaScript, no jank.</p>
        <p>Counters in CSS start with a registered custom property. Registration gives the property a type, and a typed property can be interpolated by the animation engine rather than swapped at the halfway point.</p>
        <p>Once the value animates, a counter can read it and <code>content</code> can print it. The number on screen is therefore a genuine interpolation, not a sequence of strings written by a script on every frame.</p>
        <p>Scroll-driven animations extend the same idea to gesture. The timeline is no longer wall-clock time but scroll offset, so the reader controls the value directly, and the browser can run the whole thing off the main thread.</p>
        <p>That matters most on touch devices. A JavaScript scroll handler runs after the compositor has already moved the page, so the indicator trails the content by a frame or two — visible, and impossible to fix with throttling.</p>
        <p>The practical rule: if a value is a pure function of scroll position, express it as a scroll-driven animation. If it depends on data, use JavaScript to set one custom property and let CSS derive everything else from it.</p>
        <p>Everything else — easing, staggering, reduced-motion behaviour, theming — stays in the stylesheet where designers can reach it without touching application code.</p>
        <p class="cnc-17__end">— end of article —</p>
      </article>
    </div>
    <p class="cnc-17__chip" aria-hidden="true">rAF scroll listener · one --p custom property · CSS counter() readouts · cross-browser</p>
  </div>
</section>
```
## CSS
```css
@property --cnc-17-n {
  syntax: '<integer>';
  inherits: true;
  initial-value: 0;
}

@property --cnc-17-m {
  syntax: '<integer>';
  inherits: true;
  initial-value: 8;
}

.cnc-17,
.cnc-17 *,
.cnc-17 *::before,
.cnc-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cnc-17 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --cnc-17-bg: oklch(0.96 0.006 80);
  --cnc-17-card: oklch(1 0 0);
  --cnc-17-ink: oklch(0.22 0.015 265);
  --cnc-17-mut: oklch(0.55 0.015 265);
  --cnc-17-acc: oklch(0.58 0.19 25);
  background: var(--cnc-17-bg);
  color: var(--cnc-17-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
}

.cnc-17__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 16px;
  padding: clamp(16px,4vw,44px);
}

.cnc-17__reader {
  width: min(100%,660px);
  border-radius: 20px;
  overflow: hidden;
  background: var(--cnc-17-card);
  box-shadow: 0 1px 2px oklch(0 0 0/.05),0 24px 56px oklch(0.4 0.02 265/.14);
}

.cnc-17__bar {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  padding: 16px 20px 18px;
  border-bottom: 1px solid oklch(0 0 0/.07);
}

.cnc-17__kicker {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--cnc-17-acc);
}

.cnc-17__title {
  margin-top: 5px;
  font-size: 16.5px;
  font-weight: 660;
  letter-spacing: -.02em;
}

.cnc-17__readout {
  display: grid;
  justify-items: end;
  gap: 2px;
  flex: none;
}

.cnc-17__pct {
  font-size: 22px;
  font-weight: 750;
  letter-spacing: -.04em;
  font-variant-numeric: tabular-nums;
  font-feature-settings: 'tnum' 1;
  counter-reset: cnc-17-n var(--cnc-17-n);
}

.cnc-17__pct::after {
  content: counter(cnc-17-n) "%";
}

.cnc-17__mins {
  font-size: 11.5px;
  color: var(--cnc-17-mut);
  counter-reset: cnc-17-m var(--cnc-17-m);
}

.cnc-17__mins::after {
  content: counter(cnc-17-m) " min left";
}

.cnc-17__progress {
  position: absolute;
  left: 0;
  right: 0;
  bottom: -1px;
  height: 3px;
  background: oklch(0 0 0/.07);
}

.cnc-17__progress b {
  display: block;
  height: 100%;
  width: 100%;
  transform-origin: left center;
  transform: scaleX(var(--cnc-17-p,0));
  background: linear-gradient(90deg,var(--cnc-17-acc),oklch(0.72 0.17 55));
  transition: transform .1s linear;
}

.cnc-17__article {
  height: min(52vh,420px);
  overflow: auto;
  overscroll-behavior: contain;
  padding: 22px 24px 30px;
  display: grid;
  gap: 14px;
  font-size: 14.5px;
  line-height: 1.65;
  color: color-mix(in oklch,var(--cnc-17-ink) 88%,transparent);
  text-wrap: pretty;
}

.cnc-17__article:focus-visible {
  outline: 3px solid var(--cnc-17-acc);
  outline-offset: -3px;
}

.cnc-17__lead {
  font-size: 16px;
  font-weight: 600;
  color: var(--cnc-17-ink);
}

.cnc-17__article code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .88em;
  padding: 1px 5px;
  border-radius: 5px;
  background: oklch(0 0 0/.06);
}

.cnc-17__end {
  text-align: center;
  font-size: 12px;
  color: var(--cnc-17-mut);
  padding-top: 8px;
}

.cnc-17__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--cnc-17-mut);
  padding: 7px 14px;
  border: 1px solid oklch(0 0 0/.12);
  border-radius: 99px;
  text-align: center;
  max-width: min(100%,560px);
}

@media (max-width: 520px) {
  .cnc-17__bar {
    flex-wrap: wrap;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cnc-17__progress b {
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  const reader = document.querySelector('.cnc-17');
  const article = reader && reader.querySelector('.cnc-17__article');
  if (!article || article.dataset.cncWired) return;
  article.dataset.cncWired = '1';
  const TOTAL_MIN = 8;
  let raf = 0;
  const update = () => {
    raf = 0;
    const max = article.scrollHeight - article.clientHeight;
    const p = max > 0 ? Math.min(1, Math.max(0, article.scrollTop / max)) : 0;
    reader.style.setProperty('--cnc-17-p', p.toFixed(4));
    reader.style.setProperty('--cnc-17-n', Math.round(p * 100));
    reader.style.setProperty('--cnc-17-m', Math.max(0, Math.round(TOTAL_MIN * (1 - p))));
  };
  article.addEventListener('scroll', () => {
    if (!raf) raf = requestAnimationFrame(update);
  }, { passive: true });
  update();
})();
```
