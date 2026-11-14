---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-hover-effects/css-text-color-reveal-background-clip/"
title: "CSS Text Color Reveal / Background Clip"
section: "motion"
category: "css-text-hover-effects"
category_name: "CSS Text Hover Effects"
description: "Solid ink to vivid gradient on hover — with a real crossfade, not the usual hard swap."
has_js: "false"
---

Here's a working CSS Text Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Text Color Reveal / Background Clip
Source: https://codefronts.com/motion/css-text-hover-effects/css-text-color-reveal-background-clip/

Solid ink to vivid gradient on hover — with a real crossfade, not the usual hard swap. The trick nobody writes down: keep the gradient painted underneath at all times via background-clip:text, and transition the element's COLOR to transparent — the glyph's solid fill dissolves and the gradient was waiting behind it. Once revealed, two registered @property angles keep the gradient slowly turning, so the text feels lit, not printed. Shown on a SaaS feature index where each heading carries its own --from/--to pair.
## HTML
```html
<section class="cth-03" aria-label="Gradient text color reveal demo">
  <div class="cth-03__stage">
    <div class="cth-03__scene">
      <header class="cth-03__head">
        <p class="cth-03__eyebrow">Northlight platform &mdash; 2026.3</p>
        <span class="cth-03__chip">color &rarr; transparent over background-clip:text</span>
      </header>
      <ol class="cth-03__list">
        <li><a class="cth-03__item" style="--from:oklch(0.72 0.19 25);--to:oklch(0.78 0.16 65)" href="#cth03-top" id="cth03-top"><small>001</small>Realtime ledger sync</a></li>
        <li><a class="cth-03__item" style="--from:oklch(0.74 0.17 150);--to:oklch(0.78 0.14 210)" href="#cth03-top"><small>002</small>Anomaly-aware alerts</a></li>
        <li><a class="cth-03__item" style="--from:oklch(0.66 0.21 300);--to:oklch(0.72 0.19 340)" href="#cth03-top"><small>003</small>Zero-copy exports</a></li>
        <li><a class="cth-03__item" style="--from:oklch(0.68 0.17 250);--to:oklch(0.8 0.14 190)" href="#cth03-top"><small>004</small>Region-pinned vaults</a></li>
      </ol>
      <p class="cth-03__hint">Hover or <kbd>Tab</kbd>: solid ink crossfades to a live gradient &mdash; and the gradient keeps slowly turning while you stay.</p>
    </div>
  </div>
</section>
```
## CSS
```css
@property --cth03-angle {
  syntax: '<angle>';
  inherits: false;
  initial-value: 100deg;
}

.cth-03,
.cth-03 *,
.cth-03 *::before,
.cth-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cth-03 {
  --bg: oklch(0.965 0.005 250);
  --ink: oklch(0.24 0.015 260);
  --mut: oklch(0.54 0.015 255);
  --line: oklch(0.89 0.008 250);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cth-03__stage {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  background: var(--bg);
  padding: clamp(20px,4vw,56px);
  container: cth03/inline-size;
}

.cth-03__scene {
  width: min(100%,820px);
  display: flex;
  flex-direction: column;
  gap: clamp(18px,3cqi,26px);
}

.cth-03__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
  flex-wrap: wrap;
}

.cth-03__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .24em;
  text-transform: uppercase;
  color: var(--mut);
}

.cth-03__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--mut);
  border: 1px solid var(--line);
  border-radius: 99px;
  padding: 5px 11px;
}

.cth-03__list {
  list-style: none;
  counter-reset: cth03;
}

.cth-03__list li {
  border-bottom: 1px solid var(--line);
}

.cth-03__list li:first-child {
  border-top: 1.5px solid var(--ink);
}

.cth-03__item {
  --cth03-angle: 100deg;
  display: flex;
  align-items: baseline;
  gap: clamp(14px,3cqi,26px);
  padding: clamp(14px,2.6cqi,22px) 4px;
  font-size: clamp(26px,5.4cqi,46px);
  font-weight: 800;
  letter-spacing: -.025em;
  line-height: 1.12;
  text-decoration: none;
  background-image: linear-gradient(var(--cth03-angle),var(--from),var(--to));
  -webkit-background-clip: text;
  background-clip: text;
  color: var(--ink);
  transition: color .5s ease,translate .35s cubic-bezier(.22,1,.36,1);
}

.cth-03__item small {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: .08em;
  color: var(--mut);
  -webkit-text-fill-color: var(--mut);
}

.cth-03__item:hover,
.cth-03__item:focus-visible {
  color: transparent;
  translate: 6px 0;
  animation: cth03-turn 4s ease-in-out .5s infinite alternate;
}

.cth-03__item:focus-visible {
  outline: 2px solid color-mix(in oklch,var(--from) 70%,var(--ink));
  outline-offset: 4px;
  border-radius: 3px;
}

@keyframes cth03-turn {
  from {
    --cth03-angle: 100deg;
  }

  to {
    --cth03-angle: 220deg;
  }
}

.cth-03__hint {
  font-size: 12.5px;
  color: var(--mut);
}

.cth-03__hint kbd {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  border: 1px solid var(--line);
  border-bottom-width: 2px;
  border-radius: 5px;
  padding: 2px 6px;
  background: oklch(1 0 0);
}

@container cth03 (width < 560px) {
  .cth-03__chip {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cth-03 * {
    transition-duration: .01ms !important;
    animation: none !important;
  }
}
```
