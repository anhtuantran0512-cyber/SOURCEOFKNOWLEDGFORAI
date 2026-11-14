---
source: "codefronts"
url: "https://codefronts.com/snippets/css-tags-chips/liquid-fill/"
title: "CSS Liquid Fill Hover Tag Component"
section: "snippets"
category: "css-tags-chips"
category_name: "CSS Tags & Chips"
description: "The classic liquid-rise effect, done the honest CSS way: a huge rotating blob (a square with ~42% uneven border-radius) hides below each pill; hover…"
has_js: "false"
---

Here's a working CSS Tags & Chip from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Liquid Fill Hover Tag Component
Source: https://codefronts.com/snippets/css-tags-chips/liquid-fill/

The classic liquid-rise effect, done the honest CSS way: a huge rotating blob (a square with ~42% uneven border-radius) hides below each pill; hover translates it upward while it keeps spinning, and the uneven radius sloshes across the top edge like a real waterline. The rotation runs as an animation on the standalone rotate property while the rise is a transition on translate — the two never fight, which is the whole trick.
## HTML
```html
<section class="ctc-08" aria-label="Liquid fill hover tag demo">
  <div class="ctc-08__stage">
    <div class="ctc-08__wrap">
      <header class="ctc-08__head">
        <p class="ctc-08__kicker">Liquid fill · rotating blob + rising translate</p>
        <h1>Hover to pour</h1>
      </header>
      <div class="ctc-08__panel">
        <p class="ctc-08__lab">01 · Rise — the blob translates up while it spins</p>
        <div class="ctc-08__row">
          <a class="ctc-08__pill" style="--h:60" href="#ctc08">mango</a>
          <a class="ctc-08__pill" style="--h:350" href="#ctc08">berry crush</a>
          <a class="ctc-08__pill" style="--h:150" href="#ctc08">matcha</a>
          <a class="ctc-08__pill" style="--h:250" href="#ctc08">blue lagoon</a>
          <a class="ctc-08__pill" style="--h:30" href="#ctc08">cold brew</a>
        </div>
      </div>
      <div class="ctc-08__panel">
        <p class="ctc-08__lab">02 · Sweep — same blob, entering from the left</p>
        <div class="ctc-08__row">
          <a class="ctc-08__pill ctc-08__pill--sweep" style="--h:292" href="#ctc08">add to queue</a>
          <a class="ctc-08__pill ctc-08__pill--sweep" style="--h:200" href="#ctc08">save for later</a>
          <a class="ctc-08__pill ctc-08__pill--sweep" style="--h:150" href="#ctc08">follow topic</a>
        </div>
      </div>
      <div class="ctc-08__panel">
        <p class="ctc-08__lab">03 · Resting level — park the waterline as a quota chip</p>
        <div class="ctc-08__row">
          <span class="ctc-08__pill ctc-08__pill--level" style="--h:150;--fill:-32%">storage 32%</span>
          <span class="ctc-08__pill ctc-08__pill--level" style="--h:60;--fill:-58%">credits 58%</span>
          <span class="ctc-08__pill ctc-08__pill--level" style="--h:350;--fill:-86%">inbox 86%</span>
        </div>
      </div>
      <p class="ctc-08__note">The spin is an <code>animation</code> on <code>rotate</code>; the rise is a <code>transition</code> on <code>translate</code>. Standalone transform properties compose — with classic <code>transform:</code> the hover would kill the spin.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.ctc-08,
.ctc-08 *,
.ctc-08 *::before,
.ctc-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ctc-08 {
  --bg: oklch(0.965 0.012 85);
  --ink: oklch(0.26 0.03 60);
  --mut: oklch(0.5 0.025 60);
  --line: oklch(0.88 0.015 80);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
}

.ctc-08__stage {
  width: 100%;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  display: grid;
  place-items: center;
  padding: clamp(16px,4cqi,48px);
  background: radial-gradient(70cqi 55cqi at 90% -10%,oklch(0.9 0.06 60/.55),transparent 62%),radial-gradient(60cqi 50cqi at -5% 112%,oklch(0.88 0.06 350/.4),transparent 60%),var(--bg);
  container: ctc08/inline-size;
}

.ctc-08__wrap {
  width: min(700px,100%);
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.ctc-08__kicker {
  font-size: 11.5px;
  font-weight: 800;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: oklch(0.6 0.16 60);
}

.ctc-08__head h1 {
  font-size: clamp(24px,3.8cqi,38px);
  font-weight: 800;
  letter-spacing: -.03em;
  margin: 8px 0 8px;
}

.ctc-08__panel {
  background: oklch(0.998 0.003 85);
  border: 1px solid var(--line);
  border-radius: 18px;
  padding: 16px 18px;
}

.ctc-08__lab {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .05em;
  text-transform: uppercase;
  color: var(--mut);
  margin-bottom: 12px;
}

.ctc-08__note code,
.ctc-08__lab code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .95em;
  letter-spacing: 0;
  text-transform: none;
  background: oklch(0.92 0.012 80);
  padding: 1px 5px;
  border-radius: 4px;
  color: var(--ink);
}

.ctc-08__row {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

.ctc-08__pill {
  --c: oklch(0.68 0.15 var(--h,60));
  --deep: oklch(0.52 0.16 var(--h,60));
  position: relative;
  overflow: hidden;
  display: inline-flex;
  align-items: center;
  min-height: 46px;
  padding: 0 21px;
  border-radius: 99px;
  font-size: 14px;
  font-weight: 750;
  text-decoration: none;
  color: color-mix(in oklch,var(--deep) 80%,var(--ink));
  background: color-mix(in oklch,var(--c) 10%,oklch(1 0 0));
  border: 1.5px solid color-mix(in oklch,var(--c) 35%,transparent);
  isolation: isolate;
  transition: border-color .3s,box-shadow .3s;
}

.ctc-08__pill::before {
  content: "";
  position: absolute;
  z-index: -1;
  left: -25%;
  top: 108%;
  width: 150%;
  aspect-ratio: 1;
  border-radius: 42% 44% 41% 43%;
  background: linear-gradient(180deg,var(--c),var(--deep));
  rotate: 0deg;
  animation: ctc08-spin 5s linear infinite;
  transition: translate .6s ease;
}

a.ctc-08__pill:hover,
a.ctc-08__pill:focus-visible {
  border-color: transparent;
  box-shadow: 0 10px 22px -10px var(--deep);
}

a.ctc-08__pill:hover::before,
a.ctc-08__pill:focus-visible::before {
  translate: 0 -78%;
}

.ctc-08__pill span,
.ctc-08__pill {
  transition: color .3s .18s,border-color .3s,box-shadow .3s;
}

a.ctc-08__pill:hover,
a.ctc-08__pill:focus-visible {
  color: oklch(0.99 0.005 85);
}

a.ctc-08__pill:focus-visible {
  outline: 2px solid var(--deep);
  outline-offset: 3px;
}

@keyframes ctc08-spin {
  to {
    rotate: 360deg;
  }
}

.ctc-08__pill--sweep::before {
  left: auto;
  right: 105%;
  top: -25%;
  width: 220%;
  transition: translate .55s ease;
}

a.ctc-08__pill--sweep:hover::before,
a.ctc-08__pill--sweep:focus-visible::before {
  translate: 78% 0;
}

.ctc-08__pill--level {
  color: oklch(0.99 0.005 85);
  border-color: transparent;
  background: color-mix(in oklch,var(--c) 18%,oklch(0.3 0.02 60));
}

.ctc-08__pill--level::before {
  translate: 0 var(--fill,-30%);
  animation-duration: 7s;
}

.ctc-08__pill--level {
  text-shadow: 0 1px 4px oklch(0 0 0/.3);
  font-variant-numeric: tabular-nums;
}

.ctc-08__note {
  font-size: 12.5px;
  line-height: 1.6;
  color: var(--mut);
  border-left: 3px solid oklch(0.6 0.16 60);
  padding-left: 12px;
}

@media (prefers-reduced-motion: reduce) {
  .ctc-08 * {
    transition-duration: .01ms !important;
  }

  .ctc-08__pill::before {
    animation: none;
  }
}
```
