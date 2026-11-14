---
source: "codefronts"
url: "https://codefronts.com/motion/css-scroll-progress-bar/ultra-thin-2px-minimalist-micro-progress-line/"
title: "Ultra-Thin 2px Minimalist Micro Progress Line"
section: "motion"
category: "css-scroll-progress-bar"
category_name: "CSS Scroll Progress Bar"
description: "The version to ship when the design should not be noticed: two pixels, no track, no glow, no percentage."
has_js: "true"
---

Here's a working CSS Scroll Progress Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Ultra-Thin 2px Minimalist Micro Progress Line
Source: https://codefronts.com/motion/css-scroll-progress-bar/ultra-thin-2px-minimalist-micro-progress-line/

The version to ship when the design should not be noticed: two pixels, no track, no glow, no percentage. It stays invisible over the masthead and only materialises once the reader is inside the article — the most restrained pattern in this collection and, for text-first publications, usually the correct one.
## HTML
```html
<section class="sp-18" aria-label="Ultra-thin minimalist scroll progress line demo">
  <i class="sp-18__line" aria-hidden="true"></i>
  <header class="sp-18__masthead">
    <a class="sp-18__brand" href="#sp-18-s1">The Quiet Review</a>
    <p class="sp-18__issue">Issue 41 · Winter</p>
  </header>
  <article class="sp-18__article">
    <div class="sp-18__lead">
      <p class="sp-18__eyebrow">Essay</p>
      <h2 class="sp-18__title">Two pixels of feedback</h2>
      <p class="sp-18__standfirst">On restraint, hairlines, and knowing when an interface should refuse to be interesting.</p>
      <p class="sp-18__byline">by A. Whitfield · 6 min</p>
    </div>
    <figure class="sp-18__fig">
      <img class="sp-18__img" src="https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&amp;fit=crop&amp;w=1600&amp;q=70" alt="A still lake reflecting a pale sky and distant hills" loading="lazy" decoding="async">
      <figcaption class="sp-18__cap">Restraint is a design position, not an absence of one.</figcaption>
    </figure>
    <section class="sp-18__sec" id="sp-18-s1">
      <p class="sp-18__p sp-18__p--lede">The loudest progress bar on a text page is the one with an empty track, drawn permanently across the top whether or not anybody is reading. Removing it is the first decision.</p>
      <p class="sp-18__p">What remains is a single hairline that begins at zero width, so it is genuinely absent until the reader moves. It does not glow, it does not count, and it does not follow a cursor. It occupies two pixels and answers one question.</p>
    </section>
    <section class="sp-18__sec" id="sp-18-s2">
      <h3 class="sp-18__h">Appear late</h3>
      <p class="sp-18__p">Over the masthead the bar has nothing to report, so it is not there. A second animation on the same timeline, ranged to the first eight percent, fades it in once the reader is inside the article — one extra declaration for a noticeably calmer page.</p>
      <p class="sp-18__p">This is the part that separates a minimal design from a small one: the restraint is behavioural, not just visual.</p>
    </section>
    <section class="sp-18__sec" id="sp-18-s3">
      <h3 class="sp-18__h">Hairlines are physical</h3>
      <p class="sp-18__p">Two CSS pixels on a 2× display are four device pixels, which is heavier than the drawing intends. Dropping to one and a half above 2dppx is a correction nobody consciously notices and everybody feels.</p>
    </section>
    <section class="sp-18__sec" id="sp-18-s4">
      <h3 class="sp-18__h">Inherit everything</h3>
      <p class="sp-18__p">The bar is <code>currentColor</code>. Change the type colour and the indicator follows; switch to the dark theme and there is no second decision to keep in sync. On modern engines it ships with no JavaScript at all.</p>
      <p class="sp-18__chip">2px · no track · no script</p>
    </section>
  </article>
  <footer class="sp-18__pagefoot"><p class="sp-18__pagefootin">Scroll progress pattern 18 of 18 · codefronts.com</p></footer>
</section>
```
## CSS
```css
.sp-18 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--sp-18-bg);
  --sp-18-bg: oklch(0.985 0.004 90);
  --sp-18-ink: oklch(0.22 0.012 80);
  --sp-18-mut: oklch(0.5 0.01 80);
  --sp-18-line: oklch(0.22 0.012 80/.14);
  --sp-18-h: 2px;
  --sp-18-p: 0;
  font-family: Georgia,'Iowan Old Style','Times New Roman',serif;
  color: var(--sp-18-ink);
  -webkit-font-smoothing: antialiased;
}

.sp-18 *,
.sp-18 *::before,
.sp-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sp-18__line {
  position: fixed;
  inset-block-start: 0;
  inset-inline: 0;
  block-size: var(--sp-18-h);
  z-index: 60;
  display: block;
  transform-origin: 0 50%;
  transform: scaleX(var(--sp-18-p));
  background: currentColor;
  color: var(--sp-18-ink);
  opacity: 0;
  pointer-events: none;
}

@supports (animation-timeline: scroll()) {
  .sp-18__line {
    transform: scaleX(0);
    animation: sp-18-fill linear both,sp-18-in linear both;
    animation-timeline: scroll(root block),scroll(root block);
    animation-range: normal,0 8%;
  }
}

@keyframes sp-18-fill {
  from {
    transform: scaleX(0);
  }

  to {
    transform: scaleX(1);
  }
}

@keyframes sp-18-in {
  from {
    opacity: 0;
  }

  to {
    opacity: 1;
  }
}

.sp-18__masthead {
  display: flex;
  align-items: baseline;
  gap: 16px;
  padding-block: 22px 18px;
  border-block-end: 1px solid var(--sp-18-line);
}

.sp-18__brand {
  font-size: 17px;
  font-weight: 600;
  letter-spacing: .02em;
  color: inherit;
  text-decoration: none;
}

.sp-18__brand:focus-visible {
  outline: 2px solid var(--sp-18-ink);
  outline-offset: 4px;
}

.sp-18__issue {
  margin-inline-start: auto;
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 11.5px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--sp-18-mut);
}

.sp-18__lead {
  display: grid;
  gap: 14px;
  padding-block: clamp(44px,9vh,104px) clamp(20px,4vh,40px);
}

.sp-18__eyebrow {
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 11.5px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--sp-18-mut);
}

.sp-18__title {
  font-size: clamp(36px,6.4vw,72px);
  line-height: 1.02;
  letter-spacing: -.028em;
  font-weight: 400;
  max-inline-size: 16ch;
  text-wrap: balance;
}

.sp-18__standfirst {
  font-size: clamp(17px,2vw,22px);
  line-height: 1.5;
  color: var(--sp-18-mut);
  max-inline-size: 48ch;
  font-style: italic;
  text-wrap: pretty;
}

.sp-18__byline {
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 12.4px;
  letter-spacing: .06em;
  color: var(--sp-18-mut);
}

.sp-18__fig {
  display: grid;
  gap: 10px;
  padding-block-end: clamp(20px,4vh,40px);
}

.sp-18__img {
  inline-size: 100%;
  aspect-ratio: 16/8;
  object-fit: cover;
  display: block;
  background: linear-gradient(160deg,oklch(0.85 0.02 220),oklch(0.7 0.03 90));
}

.sp-18__cap {
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 12.4px;
  color: var(--sp-18-mut);
}

.sp-18__sec {
  scroll-margin-top: 24px;
  display: grid;
  gap: 16px;
  padding-block: clamp(22px,5vh,50px);
  border-block-start: 1px solid var(--sp-18-line);
}

.sp-18__h {
  font-size: clamp(21px,2.6vw,28px);
  line-height: 1.18;
  letter-spacing: -.02em;
  font-weight: 600;
  text-wrap: balance;
}

.sp-18__p {
  max-inline-size: 64ch;
  font-size: 18px;
  line-height: 1.72;
  color: var(--sp-18-ink);
  text-wrap: pretty;
}

.sp-18__p--lede {
  font-size: 20.5px;
  line-height: 1.62;
}

.sp-18__p code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .8em;
  background: oklch(0.22 0.012 80/.07);
  padding: 2px 6px;
  border-radius: 4px;
}

.sp-18__chip {
  justify-self: start;
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 11.5px;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--sp-18-mut);
  padding-block-start: 4px;
}

.sp-18__pagefoot {
  display: grid;
  place-items: center;
  padding: clamp(44px,9vh,110px) 24px;
  border-block-start: 1px solid var(--sp-18-line);
}

.sp-18__pagefootin {
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 12px;
  letter-spacing: .06em;
  color: var(--sp-18-mut);
  text-align: center;
}

.sp-18__masthead,
.sp-18__lead,
.sp-18__fig,
.sp-18__sec {
  padding-inline: max(clamp(20px,5vw,40px),calc((100% - 720px)/2));
}

:root:has(.sp-18) {
  scroll-behavior: smooth;
}

@media (min-resolution: 2dppx) {
  .sp-18 {
    --sp-18-h: 1.5px;
  }
}

@media (prefers-color-scheme: dark) {
  .sp-18 {
    --sp-18-bg: oklch(0.16 0.008 80);
    --sp-18-ink: oklch(0.94 0.006 85);
    --sp-18-mut: oklch(0.68 0.01 85);
    --sp-18-line: oklch(1 0 0/.14);
  }
}

@media (prefers-reduced-motion: reduce) {
  :root:has(.sp-18) {
    scroll-behavior: auto;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sp-18');
  if (!root || root.dataset.spWired) return;
  root.dataset.spWired = '1';
  if (CSS.supports('animation-timeline', 'scroll()')) return; // modern engines need no script at all
  const line = root.querySelector('.sp-18__line');
  let ticking = false;
  const paint = () => {
    ticking = false;
    const d = document.documentElement;
    const max = d.scrollHeight - d.clientHeight;
    const p = max > 0 ? Math.min(1, Math.max(0, d.scrollTop / max)) : 0;
    root.style.setProperty('--sp-18-p', p.toFixed(4));
    line.style.opacity = String(Math.min(1, p / 0.08));
  };
  addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(paint); } }, { passive: true });
  addEventListener('resize', () => { if (!ticking) { ticking = true; requestAnimationFrame(paint); } }, { passive: true });
  paint();
})();
```
