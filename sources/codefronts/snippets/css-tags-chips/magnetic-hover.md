---
source: "codefronts"
url: "https://codefronts.com/snippets/css-tags-chips/magnetic-hover/"
title: "Interactive Hover Scale Pill Tag"
section: "snippets"
category: "css-tags-chips"
category_name: "CSS Tags & Chips"
description: "Hover feel is a spec, not an accident."
has_js: "false"
---

Here's a working CSS Tags & Chip from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Interactive Hover Scale Pill Tag
Source: https://codefronts.com/snippets/css-tags-chips/magnetic-hover/

Hover feel is a spec, not an accident. This demo ships three tuned scale recipes side by side — Subtle (1.03, product UIs), Springy (1.07 on an overshooting cubic-bezier, marketing pages) and Playful (scale + tilt, editorial) — plus a sheen-sweep and a shadow-lift layer you can stack on any of them. Every pill also presses down to .96 on :active, fires identically on :focus-visible, and stays put under prefers-reduced-motion.
## HTML
```html
<section class="ctc-06" aria-label="Hover scale pill tag demo">
  <div class="ctc-06__stage">
    <div class="ctc-06__wrap">
      <header class="ctc-06__head">
        <p class="ctc-06__kicker">Hover scale · three tuned recipes</p>
        <h1>The bounce is a bezier, not a library</h1>
      </header>
      <div class="ctc-06__panel">
        <p class="ctc-06__lab">01 · Subtle — <code>scale:1.03, ease</code> — for product UI</p>
        <div class="ctc-06__row">
          <a class="ctc-06__pill" style="--h:255" href="#ctc06">typescript</a>
          <a class="ctc-06__pill" style="--h:150" href="#ctc06">node</a>
          <a class="ctc-06__pill" style="--h:40" href="#ctc06">rust</a>
          <a class="ctc-06__pill" style="--h:320" href="#ctc06">swift</a>
          <a class="ctc-06__pill" style="--h:200" href="#ctc06">go</a>
        </div>
      </div>
      <div class="ctc-06__panel">
        <p class="ctc-06__lab">02 · Springy — <code>scale:1.07, cubic-bezier(.34,1.56,.64,1)</code> — the overshoot IS the spring</p>
        <div class="ctc-06__row">
          <a class="ctc-06__pill ctc-06__pill--spring" style="--h:255" href="#ctc06">design tokens</a>
          <a class="ctc-06__pill ctc-06__pill--spring" style="--h:150" href="#ctc06">motion</a>
          <a class="ctc-06__pill ctc-06__pill--spring" style="--h:40" href="#ctc06">micro-interactions</a>
          <a class="ctc-06__pill ctc-06__pill--spring" style="--h:320" href="#ctc06">easing</a>
        </div>
      </div>
      <div class="ctc-06__panel">
        <p class="ctc-06__lab">03 · Playful — scale + <code>rotate:-2deg</code> + sheen sweep + color-matched lift</p>
        <div class="ctc-06__row">
          <a class="ctc-06__pill ctc-06__pill--play" style="--h:255" href="#ctc06">weekend reads ✺</a>
          <a class="ctc-06__pill ctc-06__pill--play" style="--h:150" href="#ctc06">fresh drops</a>
          <a class="ctc-06__pill ctc-06__pill--play" style="--h:40" href="#ctc06">hot right now</a>
          <a class="ctc-06__pill ctc-06__pill--play" style="--h:320" href="#ctc06">staff picks</a>
        </div>
      </div>
      <p class="ctc-06__note">Press any pill — <code>:active</code> drops to <code>scale:.96</code> in 80ms while the release keeps the slow spring. Keyboard focus fires the exact same motion via <code>:focus-visible</code>.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.ctc-06,
.ctc-06 *,
.ctc-06 *::before,
.ctc-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ctc-06 {
  --bg: oklch(0.975 0.008 85);
  --ink: oklch(0.25 0.02 60);
  --mut: oklch(0.5 0.02 60);
  --line: oklch(0.89 0.012 80);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
}

.ctc-06__stage {
  width: 100%;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  display: grid;
  place-items: center;
  padding: clamp(16px,4cqi,48px);
  background: radial-gradient(65cqi 50cqi at 10% -10%,oklch(0.92 0.05 40/.6),transparent 62%),radial-gradient(60cqi 50cqi at 105% 112%,oklch(0.9 0.05 255/.5),transparent 60%),var(--bg);
  container: ctc06/inline-size;
}

.ctc-06__wrap {
  width: min(720px,100%);
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.ctc-06__kicker {
  font-size: 11.5px;
  font-weight: 800;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: oklch(0.58 0.15 40);
}

.ctc-06__head h1 {
  font-size: clamp(24px,3.8cqi,38px);
  font-weight: 800;
  letter-spacing: -.03em;
  margin: 8px 0 8px;
}

.ctc-06__panel {
  background: oklch(0.998 0.002 85);
  border: 1px solid var(--line);
  border-radius: 18px;
  padding: 16px 18px;
}

.ctc-06__lab {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .05em;
  text-transform: uppercase;
  color: var(--mut);
  margin-bottom: 12px;
}

.ctc-06__lab code,
.ctc-06__note code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .95em;
  letter-spacing: 0;
  text-transform: none;
  background: oklch(0.93 0.01 80);
  padding: 1px 5px;
  border-radius: 4px;
  color: var(--ink);
}

.ctc-06__row {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.ctc-06__pill {
  --c: oklch(0.6 0.14 var(--h,255));
  position: relative;
  overflow: hidden;
  display: inline-flex;
  align-items: center;
  min-height: 44px;
  padding: 0 19px;
  border-radius: 99px;
  font-size: 14px;
  font-weight: 700;
  text-decoration: none;
  color: color-mix(in oklch,var(--c) 70%,var(--ink));
  background: color-mix(in oklch,var(--c) 12%,oklch(1 0 0));
  border: 1px solid color-mix(in oklch,var(--c) 26%,transparent);
  transition: scale .25s ease,translate .25s,box-shadow .25s,rotate .25s;
}

.ctc-06__pill:hover,
.ctc-06__pill:focus-visible {
  scale: 1.03;
  z-index: 1;
}

.ctc-06__pill:active {
  scale: .96;
  transition-duration: .08s;
}

.ctc-06__pill:focus-visible {
  outline: 2px solid var(--c);
  outline-offset: 2px;
}

.ctc-06__pill--spring {
  transition: scale .3s cubic-bezier(.34,1.56,.64,1),box-shadow .25s,rotate .3s cubic-bezier(.34,1.56,.64,1);
}

.ctc-06__pill--spring:hover,
.ctc-06__pill--spring:focus-visible {
  scale: 1.07;
  box-shadow: 0 10px 22px -10px var(--c);
}

.ctc-06__pill--play {
  transition: scale .3s cubic-bezier(.34,1.7,.64,1),rotate .3s cubic-bezier(.34,1.7,.64,1),box-shadow .3s;
}

.ctc-06__pill--play::before {
  content: "";
  position: absolute;
  inset: -30% auto;
  width: 34%;
  translate: -160% 0;
  rotate: 18deg;
  background: linear-gradient(90deg,transparent,oklch(1 0 0/.75),transparent);
  transition: translate .55s ease .05s;
}

.ctc-06__pill--play:hover,
.ctc-06__pill--play:focus-visible {
  scale: 1.07;
  rotate: -2deg;
  box-shadow: 0 14px 26px -12px var(--c);
}

.ctc-06__pill--play:hover::before,
.ctc-06__pill--play:focus-visible::before {
  translate: 400% 0;
}

.ctc-06__note {
  font-size: 12.5px;
  line-height: 1.6;
  color: var(--mut);
  border-left: 3px solid oklch(0.58 0.15 40);
  padding-left: 12px;
}

@media (prefers-reduced-motion: reduce) {
  .ctc-06 * {
    transition-duration: .01ms !important;
  }

  .ctc-06__pill:hover,
    .ctc-06__pill:focus-visible {
    scale: 1;
    rotate: 0deg;
  }
}
```
