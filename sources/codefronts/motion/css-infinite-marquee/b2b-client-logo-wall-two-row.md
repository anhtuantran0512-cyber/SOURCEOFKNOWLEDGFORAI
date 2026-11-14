---
source: "codefronts"
url: "https://codefronts.com/motion/css-infinite-marquee/b2b-client-logo-wall-two-row/"
title: "B2B Client Logo Wall — Two-Row Counter-Scrolling Marquee"
section: "motion"
category: "css-infinite-marquee"
category_name: "CSS Infinite Marquee Designs"
description: "An agency-grade client wall: two logo rows gliding in opposite directions at slightly different speeds, wrapped in badge-style logo cards that lift on hover…"
has_js: "false"
---

Here's a working CSS Infinite Marquee Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: B2B Client Logo Wall — Two-Row Counter-Scrolling Marquee
Source: https://codefronts.com/motion/css-infinite-marquee/b2b-client-logo-wall-two-row/

An agency-grade client wall: two logo rows gliding in opposite directions at slightly different speeds, wrapped in badge-style logo cards that lift on hover while the whole wall pauses — the counter-motion reads as 'lots of clients' at a glance without a single line of JavaScript.
## HTML
```html
<section class="mqs-02" aria-label="Client logo wall marquee demo">
  <div class="mqs-02__inner">
    <h3 class="mqs-02__title">Trusted by 200+ product teams</h3>
    <div class="mqs-02__wall">
      <div class="mqs-02__viewport">
        <div class="mqs-02__group" style="--speed:30s">
          <span class="mqs-02__card"><span class="mqs-02__dot" style="--c:#2563eb"></span>Northbeam</span>
          <span class="mqs-02__card"><span class="mqs-02__dot" style="--c:#dc2626"></span>Cartload</span>
          <span class="mqs-02__card"><span class="mqs-02__dot" style="--c:#059669"></span>Fernwork</span>
          <span class="mqs-02__card"><span class="mqs-02__dot" style="--c:#7c3aed"></span>Quill &amp; Co</span>
          <span class="mqs-02__card"><span class="mqs-02__dot" style="--c:#ea580c"></span>Baseline</span>
          <span class="mqs-02__card"><span class="mqs-02__dot" style="--c:#0891b2"></span>Harbourly</span>
        </div>
        <div class="mqs-02__group" style="--speed:30s" aria-hidden="true">
          <span class="mqs-02__card"><span class="mqs-02__dot" style="--c:#2563eb"></span>Northbeam</span>
          <span class="mqs-02__card"><span class="mqs-02__dot" style="--c:#dc2626"></span>Cartload</span>
          <span class="mqs-02__card"><span class="mqs-02__dot" style="--c:#059669"></span>Fernwork</span>
          <span class="mqs-02__card"><span class="mqs-02__dot" style="--c:#7c3aed"></span>Quill &amp; Co</span>
          <span class="mqs-02__card"><span class="mqs-02__dot" style="--c:#ea580c"></span>Baseline</span>
          <span class="mqs-02__card"><span class="mqs-02__dot" style="--c:#0891b2"></span>Harbourly</span>
        </div>
      </div>
      <div class="mqs-02__viewport">
        <div class="mqs-02__group mqs-02__group--rev" style="--speed:38s">
          <span class="mqs-02__card"><span class="mqs-02__dot" style="--c:#be185d"></span>Alpenglow</span>
          <span class="mqs-02__card"><span class="mqs-02__dot" style="--c:#4d7c0f"></span>Statfield</span>
          <span class="mqs-02__card"><span class="mqs-02__dot" style="--c:#b45309"></span>Mooring</span>
          <span class="mqs-02__card"><span class="mqs-02__dot" style="--c:#1d4ed8"></span>Deltaform</span>
          <span class="mqs-02__card"><span class="mqs-02__dot" style="--c:#0f766e"></span>Palisade</span>
          <span class="mqs-02__card"><span class="mqs-02__dot" style="--c:#9333ea"></span>Winward</span>
        </div>
        <div class="mqs-02__group mqs-02__group--rev" style="--speed:38s" aria-hidden="true">
          <span class="mqs-02__card"><span class="mqs-02__dot" style="--c:#be185d"></span>Alpenglow</span>
          <span class="mqs-02__card"><span class="mqs-02__dot" style="--c:#4d7c0f"></span>Statfield</span>
          <span class="mqs-02__card"><span class="mqs-02__dot" style="--c:#b45309"></span>Mooring</span>
          <span class="mqs-02__card"><span class="mqs-02__dot" style="--c:#1d4ed8"></span>Deltaform</span>
          <span class="mqs-02__card"><span class="mqs-02__dot" style="--c:#0f766e"></span>Palisade</span>
          <span class="mqs-02__card"><span class="mqs-02__dot" style="--c:#9333ea"></span>Winward</span>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.mqs-02,
.mqs-02 *,
.mqs-02 *::before,
.mqs-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.mqs-02 {
  min-height: 100vh;
  width: 100%;
  --gap: 20px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #0f172a;
  padding: 64px 24px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.mqs-02__inner {
  width: min(960px,100%);
}

.mqs-02__title {
  font-size: clamp(18px,3vw,24px);
  font-weight: 700;
  color: #e2e8f0;
  text-align: center;
  margin-bottom: 34px;
  letter-spacing: -.01em;
}

.mqs-02__wall {
  display: flex;
  flex-direction: column;
  gap: var(--gap);
}

.mqs-02__viewport {
  display: flex;
  gap: var(--gap);
  overflow: hidden;
  mask-image: linear-gradient(90deg,transparent,#000 10%,#000 90%,transparent);
  -webkit-mask-image: linear-gradient(90deg,transparent,#000 10%,#000 90%,transparent);
}

.mqs-02__group {
  flex: none;
  display: flex;
  gap: var(--gap);
  animation: mqs-02-scroll var(--speed,30s) linear infinite;
  will-change: transform;
}

.mqs-02__group--rev {
  animation-direction: reverse;
}

@keyframes mqs-02-scroll {
  to {
    transform: translateX(calc(-100% - var(--gap)));
  }
}

.mqs-02__wall:hover .mqs-02__group,
.mqs-02__wall:focus-within .mqs-02__group {
  animation-play-state: paused;
}

.mqs-02__card {
  flex: none;
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 15px;
  font-weight: 600;
  color: #cbd5e1;
  background: #1e293b;
  border: 1px solid #334155;
  border-radius: 12px;
  padding: 14px 22px;
  transition: transform .2s,border-color .2s,color .2s;
  cursor: default;
}

.mqs-02__card:hover {
  transform: translateY(-3px);
  border-color: #64748b;
  color: #f8fafc;
}

.mqs-02__dot {
  width: 10px;
  height: 10px;
  border-radius: 3px;
  background: var(--c,#64748b);
}

@media (prefers-reduced-motion: reduce) {
  .mqs-02__group {
    animation: none;
  }

  .mqs-02__viewport {
    overflow-x: auto;
    mask-image: none;
    -webkit-mask-image: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — two rows share one keyframe; the second row only adds animation-direction:reverse and a different --speed token. */
```
