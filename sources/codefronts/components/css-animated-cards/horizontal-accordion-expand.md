---
source: "codefronts"
url: "https://codefronts.com/components/css-animated-cards/horizontal-accordion-expand/"
title: "Horizontal Accordion Expand"
section: "components"
category: "css-animated-cards"
category_name: "CSS Animated Cards"
description: "The image accordion: hover or focus a panel and it expands while its neighbours shrink, with captions rotating upright as their panel opens."
has_js: "false"
---

Here's a working CSS Animated Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Horizontal Accordion Expand
Source: https://codefronts.com/components/css-animated-cards/horizontal-accordion-expand/

The image accordion: hover or focus a panel and it expands while its neighbours shrink, with captions rotating upright as their panel opens. Built on :has() and animatable grid-template-columns, so the whole interaction is declarative CSS — and it is fully keyboard-operable, which almost no version of this effect on the web is.
## HTML
```html
<section class="ac-24" aria-label="Horizontal accordion expand demo">
  <div class="ac-24__stage">
    <header class="ac-24__head">
      <p class="ac-24__eyebrow">Gallery layout</p>
      <h2 class="ac-24__title">Hover a panel — or tab through it</h2>
    </header>
    <div class="ac-24__rail">
      <a class="ac-24__panel" href="#ac-24-1" id="ac-24-1">
        <img src="https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?q=80&w=900&auto=format&fit=crop" alt="Fog moving through a stand of tall pines" loading="lazy" decoding="async" width="900" height="1200">
        <span class="ac-24__scrim" aria-hidden="true"></span>
        <span class="ac-24__cap"><b>Cascade Fog</b><i>Oregon · 06:14</i></span>
      </a>
      <a class="ac-24__panel" href="#ac-24-2" id="ac-24-2">
        <img src="https://images.unsplash.com/photo-1493246507139-91e8fad9978e?q=80&w=900&auto=format&fit=crop" alt="Ridge lines lit by early sun" loading="lazy" decoding="async" width="900" height="1200">
        <span class="ac-24__scrim" aria-hidden="true"></span>
        <span class="ac-24__cap"><b>First Light</b><i>Dolomites · 05:41</i></span>
      </a>
      <a class="ac-24__panel" href="#ac-24-3" id="ac-24-3">
        <img src="https://images.unsplash.com/photo-1506744038136-46273834b3fb?q=80&w=900&auto=format&fit=crop" alt="Still lake reflecting a wooded shore" loading="lazy" decoding="async" width="900" height="1200">
        <span class="ac-24__scrim" aria-hidden="true"></span>
        <span class="ac-24__cap"><b>Glass Water</b><i>Wanaka · 07:02</i></span>
      </a>
      <a class="ac-24__panel" href="#ac-24-4" id="ac-24-4">
        <img src="https://images.unsplash.com/photo-1441974231531-c6227db76b6e?q=80&w=900&auto=format&fit=crop" alt="Sunbeams cutting through a green canopy" loading="lazy" decoding="async" width="900" height="1200">
        <span class="ac-24__scrim" aria-hidden="true"></span>
        <span class="ac-24__cap"><b>Understory</b><i>Vancouver Is. · 09:20</i></span>
      </a>
      <a class="ac-24__panel" href="#ac-24-5" id="ac-24-5">
        <img src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=900&auto=format&fit=crop" alt="Night lights tracing connections across a dark globe" loading="lazy" decoding="async" width="900" height="1200">
        <span class="ac-24__scrim" aria-hidden="true"></span>
        <span class="ac-24__cap"><b>Night Grid</b><i>Orbit · 23:58</i></span>
      </a>
    </div>
    <p class="ac-24__chip" aria-hidden="true">:has() parent selector · animatable grid-template-columns · :focus-within parity · writing-mode caption rotation</p>
  </div>
</section>
```
## CSS
```css
.ac-24,
.ac-24 *,
.ac-24 *::before,
.ac-24 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ac-24 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --ac-24-bg: oklch(0.14 0.012 250);
  --ac-24-ink: oklch(0.98 0.004 255);
  --ac-24-mut: oklch(0.74 0.02 255);
  --ac-24-acc: oklch(0.84 0.13 88);
  background: var(--ac-24-bg);
  color: var(--ac-24-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.ac-24__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(16px,2.6vw,26px);
  padding: clamp(18px,4vw,52px);
}

.ac-24__head {
  display: grid;
  justify-items: center;
  gap: 9px;
  text-align: center;
}

.ac-24__eyebrow {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--ac-24-acc);
}

.ac-24__title {
  font-size: clamp(22px,3.2vw,36px);
  font-weight: 650;
  line-height: 1.12;
  letter-spacing: -.03em;
  text-wrap: balance;
}

.ac-24__rail {
  display: grid;
  grid-template-columns: repeat(5,1fr);
  gap: 10px;
  width: min(100%,940px);
  height: min(58vh,430px);
  transition: grid-template-columns .55s cubic-bezier(.16,1,.3,1);
}

.ac-24__panel {
  position: relative;
  display: block;
  border-radius: 18px;
  overflow: hidden;
  background: oklch(0.22 0.02 250);
  text-decoration: none;
  color: inherit;
  isolation: isolate;
}

.ac-24__panel img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  scale: 1.06;
  transition: scale .6s cubic-bezier(.16,1,.3,1),filter .5s;
  filter: saturate(.72) brightness(.78);
}

.ac-24__panel:hover img,
.ac-24__panel:focus-visible img {
  scale: 1;
  filter: saturate(1) brightness(1);
}

.ac-24__panel:focus-visible {
  outline: 2px solid var(--ac-24-acc);
  outline-offset: 3px;
}

.ac-24__scrim {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg,transparent 40%,oklch(0.10 0.01 250/.82));
  transition: opacity .4s;
}

.ac-24__cap {
  position: absolute;
  left: 0;
  bottom: 0;
  display: grid;
  gap: 3px;
  padding: 16px;
  writing-mode: vertical-rl;
  rotate: 180deg;
  transition: rotate .5s cubic-bezier(.16,1,.3,1),writing-mode .5s,gap .4s;
}

.ac-24__cap b {
  font-size: 15px;
  font-weight: 660;
  letter-spacing: -.02em;
  white-space: nowrap;
}

.ac-24__cap i {
  font-style: normal;
  font-size: 11.5px;
  color: var(--ac-24-mut);
  font-variant-numeric: tabular-nums;
  white-space: nowrap;
}

.ac-24__rail:has(.ac-24__panel:nth-child(1):hover),
.ac-24__rail:has(.ac-24__panel:nth-child(1):focus-within) {
  grid-template-columns: 2.6fr 1fr 1fr 1fr 1fr;
}

.ac-24__rail:has(.ac-24__panel:nth-child(2):hover),
.ac-24__rail:has(.ac-24__panel:nth-child(2):focus-within) {
  grid-template-columns: 1fr 2.6fr 1fr 1fr 1fr;
}

.ac-24__rail:has(.ac-24__panel:nth-child(3):hover),
.ac-24__rail:has(.ac-24__panel:nth-child(3):focus-within) {
  grid-template-columns: 1fr 1fr 2.6fr 1fr 1fr;
}

.ac-24__rail:has(.ac-24__panel:nth-child(4):hover),
.ac-24__rail:has(.ac-24__panel:nth-child(4):focus-within) {
  grid-template-columns: 1fr 1fr 1fr 2.6fr 1fr;
}

.ac-24__rail:has(.ac-24__panel:nth-child(5):hover),
.ac-24__rail:has(.ac-24__panel:nth-child(5):focus-within) {
  grid-template-columns: 1fr 1fr 1fr 1fr 2.6fr;
}

.ac-24__panel:hover .ac-24__cap,
.ac-24__panel:focus-within .ac-24__cap {
  writing-mode: horizontal-tb;
  rotate: 0deg;
  gap: 4px;
}

.ac-24__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  line-height: 1.6;
  color: var(--ac-24-mut);
  padding: 8px 15px;
  border: 1px solid oklch(1 0 0/.13);
  border-radius: 99px;
  text-align: center;
  max-width: min(100%,800px);
}

@media (max-width: 680px) {
  .ac-24__rail {
    grid-template-columns: 1fr;
    grid-template-rows: repeat(5,1fr);
    height: min(72vh,520px);
    transition: grid-template-rows .55s cubic-bezier(.16,1,.3,1);
  }

  .ac-24__cap {
    writing-mode: horizontal-tb;
    rotate: 0deg;
  }

  .ac-24__rail:has(.ac-24__panel:nth-child(1):hover),
    .ac-24__rail:has(.ac-24__panel:nth-child(1):focus-within) {
    grid-template-columns: 1fr;
    grid-template-rows: 2.6fr 1fr 1fr 1fr 1fr;
  }

  .ac-24__rail:has(.ac-24__panel:nth-child(2):hover),
    .ac-24__rail:has(.ac-24__panel:nth-child(2):focus-within) {
    grid-template-columns: 1fr;
    grid-template-rows: 1fr 2.6fr 1fr 1fr 1fr;
  }

  .ac-24__rail:has(.ac-24__panel:nth-child(3):hover),
    .ac-24__rail:has(.ac-24__panel:nth-child(3):focus-within) {
    grid-template-columns: 1fr;
    grid-template-rows: 1fr 1fr 2.6fr 1fr 1fr;
  }

  .ac-24__rail:has(.ac-24__panel:nth-child(4):hover),
    .ac-24__rail:has(.ac-24__panel:nth-child(4):focus-within) {
    grid-template-columns: 1fr;
    grid-template-rows: 1fr 1fr 1fr 2.6fr 1fr;
  }

  .ac-24__rail:has(.ac-24__panel:nth-child(5):hover),
    .ac-24__rail:has(.ac-24__panel:nth-child(5):focus-within) {
    grid-template-columns: 1fr;
    grid-template-rows: 1fr 1fr 1fr 1fr 2.6fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ac-24__rail,
    .ac-24__panel img,
    .ac-24__cap {
    transition-duration: .01ms;
  }
}
```
