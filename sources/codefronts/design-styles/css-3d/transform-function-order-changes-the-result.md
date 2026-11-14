---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-3d/transform-function-order-changes-the-result/"
title: "Transform Function Order Changes the Result"
section: "design-styles"
category: "css-3d"
category_name: "CSS 3D Effects"
description: "translateX(120px) rotate(45deg) and rotate(45deg) translateX(120px) land in different places, because each function operates in the coordinate space the…"
has_js: "false"
---

Here's a working CSS 3D Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Transform Function Order Changes the Result
Source: https://codefronts.com/design-styles/css-3d/transform-function-order-changes-the-result/

translateX(120px) rotate(45deg) and rotate(45deg) translateX(120px) land in different places, because each function operates in the coordinate space the previous one left behind. Both orders run on identical elements with their travel traced, and the same lesson is then repeated in 3D where it bites harder.
## HTML
```html
<section class="d3-04" aria-labelledby="d3-04-title">
  <h2 class="d3-04__sr" id="d3-04-title">Transform order compared</h2>

  <div class="d3-04__theme">
    <input class="d3-04__theme-input" type="checkbox" id="d3-04-theme">
    <label class="d3-04__theme-label" for="d3-04-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="d3-04__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="d3-04__stage">
    <div class="d3-04__viewport">
      <header class="d3-04__head">
        <span class="d3-04__kicker">Northbound Freight &mdash; dispatch board</span>
        <strong>Two routes, same two moves</strong>
      </header>

      <div class="d3-04__lanes">
        <section class="d3-04__lane">
          <p class="d3-04__cap d3-04__cap--a"><span class="d3-04__tag d3-04__tag--a">Route A</span> <code>translateX() rotate()</code> &mdash; move first, then turn on the spot</p>
          <div class="d3-04__field">
            <span class="d3-04__origin" aria-hidden="true"></span>
            <span class="d3-04__trace d3-04__trace--line" aria-hidden="true"></span>
            <div class="d3-04__tile d3-04__tile--a">
              <span class="d3-04__no">A-118</span>
              <b>Depot &rarr; Bay 4</b>
              <i class="d3-04__bars" aria-hidden="true"></i>
            </div>
          </div>
          <ul class="d3-04__steps"><li><b>1</b> translateX(7rem)</li><li><b>2</b> rotate(45deg)</li></ul>
        </section>

        <section class="d3-04__lane">
          <p class="d3-04__cap d3-04__cap--b"><span class="d3-04__tag d3-04__tag--b">Route B</span> <code>rotate() translateX()</code> &mdash; turn first, then move along the new axis</p>
          <div class="d3-04__field">
            <span class="d3-04__origin" aria-hidden="true"></span>
            <span class="d3-04__trace d3-04__trace--arc" aria-hidden="true"></span>
            <div class="d3-04__tile d3-04__tile--b">
              <span class="d3-04__no">B-902</span>
              <b>Depot &rarr; Bay 9</b>
              <i class="d3-04__bars" aria-hidden="true"></i>
            </div>
          </div>
          <ul class="d3-04__steps"><li><b>1</b> rotate(45deg)</li><li><b>2</b> translateX(7rem)</li></ul>
        </section>
      </div>

      <p class="d3-04__note">Both parcels leave the same dock with the same two instructions. Route B travels down a rotated axis, so it lands somewhere else entirely.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.d3-04 {
  --d3-04-bg: #f6f0e4;
  --d3-04-surf: #fffdf8;
  --d3-04-line: #ddd2ba;
  --d3-04-ink: #221c12;
  --d3-04-mut: #6c6250;
  --d3-04-a: #1f6b4f;
  --d3-04-a: oklch(45% 0.11 158);
  --d3-04-b: #b02c2c;
  --d3-04-b: oklch(50% 0.17 25);
  --d3-04-dist: clamp(3.5rem, 14vw, 7rem);
  --d3-04-angle: 45deg;
  --d3-04-beat: 6s;
  --d3-04-font-display: "Bookman Old Style", "Rockwell", "Zilla Slab", Georgia, serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background-color: var(--d3-04-bg);
  background-image: radial-gradient(52rem 26rem at 90% -8%, color-mix(in oklab, var(--d3-04-b) 14%, transparent), transparent 60%), radial-gradient(48rem 24rem at -6% 104%, color-mix(in oklab, var(--d3-04-a) 16%, transparent), transparent 62%);
  color: var(--d3-04-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.5;
}

.d3-04 *,
.d3-04 *::before,
.d3-04 *::after {
  box-sizing: border-box;
}

.d3-04__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.d3-04:has(.d3-04__theme-input:checked) {
  --d3-04-bg: #17140f;
  --d3-04-surf: #201c15;
  --d3-04-line: #3b342a;
  --d3-04-ink: #f4eee2;
  --d3-04-mut: #a99d88;
  --d3-04-a: #6fd8a8;
  --d3-04-a: oklch(82% 0.13 160);
  --d3-04-b: #f4907f;
  --d3-04-b: oklch(78% 0.13 28);
}

@media (prefers-color-scheme: dark) {
  .d3-04 {
    --d3-04-bg: #17140f;
    --d3-04-surf: #201c15;
    --d3-04-line: #3b342a;
    --d3-04-ink: #f4eee2;
    --d3-04-mut: #a99d88;
    --d3-04-a: #6fd8a8;
    --d3-04-a: oklch(82% 0.13 160);
    --d3-04-b: #f4907f;
    --d3-04-b: oklch(78% 0.13 28);
  }

  .d3-04:has(.d3-04__theme-input:checked) {
    --d3-04-bg: #f6f0e4;
    --d3-04-surf: #fffdf8;
    --d3-04-line: #ddd2ba;
    --d3-04-ink: #221c12;
    --d3-04-mut: #6c6250;
    --d3-04-a: #1f6b4f;
    --d3-04-a: oklch(45% 0.11 158);
    --d3-04-b: #b02c2c;
    --d3-04-b: oklch(50% 0.17 25);
  }
}

@media (prefers-color-scheme: light) {
  .d3-04:has(.d3-04__theme-input:checked) {
    --d3-04-bg: #17140f;
    --d3-04-surf: #201c15;
    --d3-04-line: #3b342a;
    --d3-04-ink: #f4eee2;
    --d3-04-mut: #a99d88;
    --d3-04-a: #6fd8a8;
    --d3-04-a: oklch(82% 0.13 160);
    --d3-04-b: #f4907f;
    --d3-04-b: oklch(78% 0.13 28);
  }
}

.d3-04__theme {
  position: absolute;
  inset-block-start: clamp(0.75rem, 3vw, 1.5rem);
  inset-inline-end: clamp(0.75rem, 3vw, 1.5rem);
  z-index: 20;
}

.d3-04__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.d3-04__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--d3-04-line);
  border-radius: 4px;
  background: var(--d3-04-surf);
  color: var(--d3-04-ink);
  cursor: pointer;
  box-shadow: 3px 3px 0 var(--d3-04-line);
}

.d3-04__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.d3-04__theme-input:focus-visible + .d3-04__theme-label {
  outline: 2px solid var(--d3-04-b);
  outline-offset: 3px;
}

.d3-04__stage {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  place-items: center;
  min-block-size: 100vh;
  padding: clamp(3.5rem, 9vw, 5rem) clamp(0.75rem, 4vw, 2.5rem);
}

.d3-04__viewport {
  inline-size: 100%;
  max-inline-size: 64rem;
  overflow: hidden;
  display: grid;
  gap: clamp(1rem, 3vw, 1.6rem);
  padding: clamp(1rem, 3.5vw, 2rem);
  border: 1px solid var(--d3-04-line);
  border-radius: 6px;
  background: var(--d3-04-surf);
  box-shadow: 10px 10px 0 color-mix(in oklab, var(--d3-04-ink) 10%, transparent);
}

.d3-04__head {
  display: grid;
  gap: 0.15rem;
  padding-block-end: 0.9rem;
  border-block-end: 2px solid var(--d3-04-ink);
}

.d3-04__kicker {
  font: 700 0.66rem/1.4 ui-monospace, Menlo, monospace;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--d3-04-mut);
}

.d3-04__head strong {
  font: 700 clamp(1.3rem, 4.4vw, 2.1rem)/1.05 var(--d3-04-font-display);
  letter-spacing: -0.01em;
}

.d3-04__lanes {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 17rem), 1fr));
  gap: clamp(0.9rem, 3vw, 1.5rem);
}

.d3-04__lane {
  display: grid;
  gap: 0.7rem;
}

.d3-04__cap {
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.4rem;
  font: 500 clamp(0.74rem, 2vw, 0.84rem)/1.35 system-ui, sans-serif;
  color: var(--d3-04-mut);
}

.d3-04__cap code {
  font: 600 0.95em/1 ui-monospace, Menlo, monospace;
  color: var(--d3-04-ink);
}

.d3-04__cap--a code {
  color: var(--d3-04-a);
}

.d3-04__cap--b code {
  color: var(--d3-04-b);
}

.d3-04__tag {
  padding: 0.2rem 0.5rem;
  border-radius: 3px;
  font: 800 0.62rem/1.5 ui-monospace, Menlo, monospace;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--d3-04-surf);
}

.d3-04__tag--a {
  background: var(--d3-04-a);
}

.d3-04__tag--b {
  background: var(--d3-04-b);
}

.d3-04__field {
  position: relative;
  block-size: clamp(11rem, 32vw, 14rem);
  border: 1px solid var(--d3-04-line);
  border-radius: 4px;
  overflow: hidden;
  background-color: color-mix(in oklab, var(--d3-04-bg) 60%, var(--d3-04-surf));
  background-image: linear-gradient(color-mix(in oklab, var(--d3-04-line) 55%, transparent) 1px, transparent 1px), linear-gradient(90deg, color-mix(in oklab, var(--d3-04-line) 55%, transparent) 1px, transparent 1px);
  background-size: 18px 18px;
}

.d3-04__origin {
  position: absolute;
  inset-block-start: 50%;
  inset-inline-start: 20%;
  inline-size: 9px;
  block-size: 9px;
  margin: -4.5px 0 0 -4.5px;
  border-radius: 999px;
  background: var(--d3-04-ink);
  box-shadow: 0 0 0 4px color-mix(in oklab, var(--d3-04-ink) 15%, transparent);
}

.d3-04__trace {
  position: absolute;
  inset-block-start: 50%;
  inset-inline-start: 20%;
  border: 1px dashed var(--d3-04-mut);
  opacity: 0.75;
}

.d3-04__trace--line {
  inline-size: var(--d3-04-dist);
  block-size: 0;
  border-width: 1px 0 0 0;
}

.d3-04__trace--arc {
  inline-size: calc(var(--d3-04-dist) * 2);
  block-size: calc(var(--d3-04-dist) * 2);
  margin: calc(var(--d3-04-dist) * -1) 0 0 calc(var(--d3-04-dist) * -1);
  border-radius: 999px;
}

.d3-04__tile {
  position: absolute;
  inset-block-start: 50%;
  inset-inline-start: 20%;
  inline-size: clamp(5.5rem, 17vw, 7.5rem);
  margin: -2.1rem 0 0 -0.9rem;
  padding: 0.5rem 0.6rem 0.55rem;
  display: grid;
  gap: 0.15rem;
  border-radius: 5px;
  color: #fff;
  box-shadow: 0 14px 26px -12px rgba(0, 0, 0, 0.5);
}

.d3-04__no {
  font: 800 0.6rem/1.4 ui-monospace, Menlo, monospace;
  letter-spacing: 0.12em;
  opacity: 0.85;
}

.d3-04__tile b {
  font: 700 clamp(0.72rem, 2vw, 0.82rem)/1.15 var(--d3-04-font-display);
}

.d3-04__bars {
  display: block;
  block-size: 0.85rem;
  margin-block-start: 0.15rem;
  border-radius: 2px;
  background-image: repeating-linear-gradient(90deg, rgba(255, 255, 255, 0.9) 0 2px, transparent 2px 4px, rgba(255, 255, 255, 0.9) 4px 5px, transparent 5px 7px);
}

.d3-04__tile--a {
  background: linear-gradient(150deg, var(--d3-04-a), color-mix(in oklab, var(--d3-04-a) 60%, #05231a));
  animation: d3-04-order-a var(--d3-04-beat) ease-in-out infinite;
}

.d3-04__tile--b {
  background: linear-gradient(150deg, var(--d3-04-b), color-mix(in oklab, var(--d3-04-b) 60%, #2c0606));
  animation: d3-04-order-b var(--d3-04-beat) ease-in-out infinite;
}

@keyframes d3-04-order-a {
  0%,
    12% {
    transform: translateX(0) rotate(0deg);
  }

  50%,
    62% {
    transform: translateX(var(--d3-04-dist)) rotate(var(--d3-04-angle));
  }

  100% {
    transform: translateX(0) rotate(0deg);
  }
}

@keyframes d3-04-order-b {
  0%,
    12% {
    transform: rotate(0deg) translateX(0);
  }

  50%,
    62% {
    transform: rotate(var(--d3-04-angle)) translateX(var(--d3-04-dist));
  }

  100% {
    transform: rotate(0deg) translateX(0);
  }
}

.d3-04__steps {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
}

.d3-04__steps li {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  padding: 0.3rem 0.55rem;
  border: 1px solid var(--d3-04-line);
  border-radius: 999px;
  font: 500 0.72rem/1.2 ui-monospace, Menlo, monospace;
  color: var(--d3-04-mut);
}

.d3-04__steps b {
  display: grid;
  place-items: center;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  border-radius: 999px;
  background: var(--d3-04-ink);
  color: var(--d3-04-surf);
  font-size: 0.62rem;
}

.d3-04__note {
  margin: 0;
  max-inline-size: 46ch;
  font: 500 clamp(0.74rem, 2vw, 0.84rem)/1.5 system-ui, sans-serif;
  color: var(--d3-04-mut);
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .d3-04__tile--a {
    animation: none;
    transform: translateX(var(--d3-04-dist)) rotate(var(--d3-04-angle));
  }

  .d3-04__tile--b {
    animation: none;
    transform: rotate(var(--d3-04-angle)) translateX(var(--d3-04-dist));
  }
}
```
