---
source: "codefronts"
url: "https://codefronts.com/navigation/css-accordions/stepped-stair/"
title: "Stepped Stair Accordion — Indented Cascade with Depth Levels"
section: "navigation"
category: "css-accordions"
category_name: "CSS Accordions — Vertical & Horizontal"
description: "Items descend like a staircase: each header starts progressively indented and narrower, connected by corner brackets, so the closed state is already a…"
has_js: "false"
---

Here's a working CSS Accordions — Vertical & Horizontal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Stepped Stair Accordion — Indented Cascade with Depth Levels
Source: https://codefronts.com/navigation/css-accordions/stepped-stair/

Items descend like a staircase: each header starts progressively indented and narrower, connected by corner brackets, so the closed state is already a diagram of descent. Opening a step slides it flush-left to full width — it 'steps forward' out of the stair to speak. A layout-as-metaphor pattern for processes that go deeper, funnels and layered architectures.
## HTML
```html
<section class="acc-24" aria-label="Stepped stair accordion demo">
  <div class="acc-24__wrap">
    <h3 class="acc-24__title">How a request travels</h3>
    <details class="acc-24__item" style="--i:0" open>
      <summary class="acc-24__sum"><span class="acc-24__chip">L0</span>Edge network<span class="acc-24__chev"></span></summary>
      <div class="acc-24__body"><p>TLS terminates at the nearest of 280 points of presence. Static hits leave here in ~15ms and never touch a server.</p></div>
    </details>
    <details class="acc-24__item" style="--i:1">
      <summary class="acc-24__sum"><span class="acc-24__chip">L1</span>Routing layer<span class="acc-24__chev"></span></summary>
      <div class="acc-24__body"><p>A consistent-hash router picks the tenant's home region and attaches trace headers every layer below will honor.</p></div>
    </details>
    <details class="acc-24__item" style="--i:2">
      <summary class="acc-24__sum"><span class="acc-24__chip">L2</span>Service mesh<span class="acc-24__chev"></span></summary>
      <div class="acc-24__body"><p>Sidecars handle retries, circuit-breaking and mTLS between the 40-odd services. Budgets: 50ms p99 per hop.</p></div>
    </details>
    <details class="acc-24__item" style="--i:3">
      <summary class="acc-24__sum"><span class="acc-24__chip">L3</span>Storage engine<span class="acc-24__chev"></span></summary>
      <div class="acc-24__body"><p>Writes land in a replicated log before acking; reads are served from materialized views rebuilt continuously behind it.</p></div>
    </details>
  </div>
</section>
```
## CSS
```css
.acc-24,
.acc-24 *,
.acc-24 *::before,
.acc-24 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.acc-24 {
  --accent: oklch(0.55 0.14 210);
  --pitch: 34px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f0f4f5;
  padding: 44px 24px;
}

.acc-24__wrap {
  width: min(560px,100%);
}

.acc-24__title {
  font-size: 24px;
  font-weight: 800;
  color: #152b31;
  letter-spacing: -.02em;
  margin-bottom: 20px;
}

.acc-24__item {
  position: relative;
  margin-left: calc(var(--i) * var(--pitch));
  width: calc(100% - var(--i) * var(--pitch));
  margin-bottom: 10px;
  transition: margin-left .45s cubic-bezier(.4,0,.2,1),width .45s cubic-bezier(.4,0,.2,1);
}

.acc-24__item:not(:first-of-type)::before {
  content: "";
  position: absolute;
  left: calc(var(--pitch) * -0.6);
  top: -14px;
  width: calc(var(--pitch) * .6 - 6px);
  height: 42px;
  border-left: 2px solid #c3d2d6;
  border-bottom: 2px solid #c3d2d6;
  border-bottom-left-radius: 8px;
  transition: opacity .3s;
}

.acc-24__item[open] {
  margin-left: 0;
  width: 100%;
}

.acc-24__item[open]::before {
  opacity: 0;
}

.acc-24__sum {
  list-style: none;
  display: flex;
  align-items: center;
  gap: 12px;
  min-height: 54px;
  padding: 6px 18px;
  background: #fff;
  border: 1.5px solid #dbe5e8;
  border-radius: 12px;
  font-size: 15.5px;
  font-weight: 700;
  color: #1d3a42;
  cursor: pointer;
  transition: border-color .25s,box-shadow .25s;
}

.acc-24__sum::-webkit-details-marker {
  display: none;
}

.acc-24__sum::marker {
  content: "";
}

.acc-24__sum:hover {
  border-color: var(--accent);
}

.acc-24__item[open] .acc-24__sum {
  border-color: var(--accent);
  box-shadow: 0 10px 26px -18px oklch(0.55 0.14 210 / .8);
}

.acc-24__chip {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11.5px;
  font-weight: 700;
  color: var(--accent);
  background: oklch(0.55 0.14 210 / .1);
  padding: 4px 8px;
  border-radius: 7px;
  flex: none;
}

.acc-24__chev {
  margin-left: auto;
  width: 8px;
  height: 8px;
  border-right: 2px solid #7c979e;
  border-bottom: 2px solid #7c979e;
  rotate: 45deg;
  translate: 0 -1px;
  transition: rotate .3s;
  flex: none;
}

.acc-24__item[open] .acc-24__chev {
  rotate: 225deg;
}

.acc-24__body {
  padding: 14px 20px 8px;
  font-size: 14.5px;
  line-height: 1.65;
  color: #3f565d;
}

.acc-24__item[open] .acc-24__body {
  animation: acc-24-in .35s ease-out;
}

@keyframes acc-24-in {
  from {
    opacity: 0;
    translate: 0 -6px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.acc-24__sum:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
  border-radius: 12px;
}

@media (max-width: 520px) {
  .acc-24 {
    --pitch: 20px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .acc-24__item,
    .acc-24__chev,
    .acc-24__sum {
    transition: none;
  }

  .acc-24__item[open] .acc-24__body {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — each item's resting indent is calc(var(--i) * pitch) margin; details[open] transitions margin and width to flush full-width, stepping the item forward out of the staircase. */
```
