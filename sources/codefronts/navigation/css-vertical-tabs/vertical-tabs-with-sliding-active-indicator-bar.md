---
source: "codefronts"
url: "https://codefronts.com/navigation/css-vertical-tabs/vertical-tabs-with-sliding-active-indicator-bar/"
title: "Vertical Tabs with Sliding Active Indicator Bar"
section: "navigation"
category: "css-vertical-tabs"
category_name: "CSS Vertical Tabs"
description: "The \"magic line\" effect — a single pill that glides between tabs instead of four separate highlights popping on and off — with no JavaScript measuring."
has_js: "false"
---

Here's a working CSS Vertical Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Vertical Tabs with Sliding Active Indicator Bar
Source: https://codefronts.com/navigation/css-vertical-tabs/vertical-tabs-with-sliding-active-indicator-bar/

The "magic line" effect — a single pill that glides between tabs instead of four separate highlights popping on and off — with no JavaScript measuring. A :has() lookup maps the checked radio to an index integer, and the marker rides translateY(calc(var(--i) * var(--step))) on a spring curve. One rule per tab, no ResizeObserver, no getBoundingClientRect.
## HTML
```html
<section class="vt-05" aria-label="Sliding active indicator vertical tabs demo">
  <div class="vt-05__stage">
    <div class="vt-05__head">
      <p class="vt-05__eyebrow">:has() → --i · translate · spring</p>
      <h2 class="vt-05__title">One marker, four stops</h2>
    </div>
    <div class="vt-05__card">
      <div class="vt-05__rail" role="radiogroup" aria-label="Release channels">
        <input class="vt-05__radio" type="radio" name="vt-05" id="vt-05-t1" checked>
        <label class="vt-05__tab" for="vt-05-t1">Stable<small>v4.2.0</small></label>
        <input class="vt-05__radio" type="radio" name="vt-05" id="vt-05-t2">
        <label class="vt-05__tab" for="vt-05-t2">Beta<small>v4.3.0-rc1</small></label>
        <input class="vt-05__radio" type="radio" name="vt-05" id="vt-05-t3">
        <label class="vt-05__tab" for="vt-05-t3">Canary<small>nightly</small></label>
        <input class="vt-05__radio" type="radio" name="vt-05" id="vt-05-t4">
        <label class="vt-05__tab" for="vt-05-t4">Legacy<small>v3.9.x</small></label>
      </div>
      <div class="vt-05__panels">
        <article class="vt-05__panel" id="vt-05-p1"><h3 class="vt-05__h">Position is arithmetic</h3><p class="vt-05__p">Fixed-height rows turn the indicator's offset into <code>index × step</code>. No measuring, no resize listener, no layout thrash.</p><p class="vt-05__chip">translate: 0 calc(var(--i) * var(--step))</p></article>
        <article class="vt-05__panel" id="vt-05-p2"><h3 class="vt-05__h">:has() reaches upward</h3><p class="vt-05__p">A checked descendant sets a custom property on its ancestor — the thing CSS could never do before 2023.</p><p class="vt-05__chip">.rail:has(#vt-05-t2:checked){--i:1}</p></article>
        <article class="vt-05__panel" id="vt-05-p3"><h3 class="vt-05__h">The curve is the product</h3><p class="vt-05__p">A 7% overshoot makes the pill feel like an object with mass. Linear easing makes it feel like a spreadsheet cursor.</p><p class="vt-05__chip">cubic-bezier(.34, 1.32, .44, 1)</p></article>
        <article class="vt-05__panel" id="vt-05-p4"><h3 class="vt-05__h">Degrades quietly</h3><p class="vt-05__p">Where <code>:has()</code> is missing the marker parks at the top and the checked tab keeps its own tint — no broken state.</p><p class="vt-05__chip">@supports selector(:has(*))</p></article>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@property --vt-05-i {
  syntax: '<integer>';
  inherits: true;
  initial-value: 0;
}

.vt-05 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--vt-05-bg);
  --vt-05-bg: oklch(0.21 0.03 296);
  --vt-05-card: oklch(0.26 0.035 296);
  --vt-05-ink: oklch(0.97 0.01 296);
  --vt-05-mut: oklch(0.73 0.02 296);
  --vt-05-acc: oklch(0.76 0.17 322);
  --vt-05-acc2: oklch(0.7 0.17 268);
  --vt-05-line: oklch(1 0 0/.11);
  --vt-05-step: 56px;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--vt-05-ink);
}

.vt-05 *,
.vt-05 *::before,
.vt-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.vt-05__stage {
  min-height: 100svh;
  display: grid;
  place-content: center;
  justify-items: center;
  gap: clamp(18px,3vw,30px);
  padding: clamp(20px,5vw,64px);
  background: radial-gradient(75% 55% at 70% 10%,oklch(0.38 0.11 320/.5),transparent),radial-gradient(60% 50% at 20% 90%,oklch(0.36 0.1 270/.45),transparent);
}

.vt-05__head {
  display: grid;
  justify-items: center;
  gap: 10px;
  text-align: center;
}

.vt-05__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--vt-05-acc);
}

.vt-05__title {
  font-size: clamp(24px,3.6vw,38px);
  line-height: 1.08;
  letter-spacing: -.028em;
  font-weight: 700;
  text-wrap: balance;
}

.vt-05__card {
  width: min(94vw,860px);
  display: grid;
  grid-template-columns: clamp(170px,28%,246px) 1fr;
  background: var(--vt-05-card);
  border: 1px solid var(--vt-05-line);
  border-radius: 20px;
  box-shadow: 0 28px 74px -36px oklch(0 0 0/.75);
  overflow: hidden;
}

.vt-05__rail {
  --vt-05-i: 0;
  position: relative;
  display: grid;
  align-content: start;
  padding: 14px 12px;
  border-right: 1px solid var(--vt-05-line);
  background: oklch(0 0 0/.14);
}

.vt-05__rail::before {
  content: "";
  position: absolute;
  z-index: 0;
  inset-block-start: 14px;
  inset-inline: 12px;
  block-size: var(--vt-05-step);
  border-radius: 13px;
  background: linear-gradient(120deg,color-mix(in oklch,var(--vt-05-acc) 26%,transparent),color-mix(in oklch,var(--vt-05-acc2) 26%,transparent));
  border: 1px solid color-mix(in oklch,var(--vt-05-acc) 42%,transparent);
  box-shadow: 0 8px 22px -10px color-mix(in oklch,var(--vt-05-acc) 70%,transparent);
  pointer-events: none;
  translate: 0 calc(var(--vt-05-i) * var(--vt-05-step));
  transition: translate .42s cubic-bezier(.34,1.32,.44,1);
}

.vt-05__rail:has(#vt-05-t2:checked) {
  --vt-05-i: 1;
}

.vt-05__rail:has(#vt-05-t3:checked) {
  --vt-05-i: 2;
}

.vt-05__rail:has(#vt-05-t4:checked) {
  --vt-05-i: 3;
}

.vt-05__radio {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.vt-05__tab {
  position: relative;
  z-index: 1;
  display: grid;
  align-content: center;
  gap: 2px;
  block-size: var(--vt-05-step);
  padding: 0 15px;
  border-radius: 13px;
  font-size: 14.6px;
  font-weight: 650;
  color: var(--vt-05-mut);
  cursor: pointer;
  transition: color .24s ease;
}

.vt-05__tab small {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10.5px;
  font-weight: 500;
  opacity: .72;
}

.vt-05__tab:hover {
  color: var(--vt-05-ink);
}

.vt-05__radio:checked+.vt-05__tab {
  color: var(--vt-05-ink);
}

.vt-05__radio:focus-visible+.vt-05__tab {
  outline: 2px solid var(--vt-05-acc);
  outline-offset: -2px;
}

.vt-05__panels {
  display: grid;
  min-height: clamp(250px,33vw,300px);
  padding: clamp(22px,3.6vw,42px);
}

.vt-05__panel {
  grid-area: 1/1;
  align-content: center;
  display: grid;
  gap: 12px;
  justify-items: start;
  opacity: 0;
  visibility: hidden;
  transform: translateY(9px);
  transition: opacity .3s ease,transform .36s cubic-bezier(.32,.72,.3,1),visibility 0s .36s;
}

.vt-05__card:has(#vt-05-t1:checked) #vt-05-p1,
.vt-05__card:has(#vt-05-t2:checked) #vt-05-p2,
.vt-05__card:has(#vt-05-t3:checked) #vt-05-p3,
.vt-05__card:has(#vt-05-t4:checked) #vt-05-p4 {
  opacity: 1;
  visibility: visible;
  transform: none;
  transition-delay: 0s;
}

.vt-05__h {
  font-size: clamp(19px,2.4vw,25px);
  line-height: 1.2;
  letter-spacing: -.022em;
  font-weight: 680;
  text-wrap: balance;
}

.vt-05__p {
  max-width: 44ch;
  font-size: 14.8px;
  line-height: 1.64;
  color: var(--vt-05-mut);
  text-wrap: pretty;
}

.vt-05__p code,
.vt-05__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
}

.vt-05__p code {
  font-size: .85em;
  background: oklch(1 0 0/.09);
  padding: 2px 6px;
  border-radius: 5px;
}

.vt-05__chip {
  font-size: 11px;
  color: var(--vt-05-mut);
  padding: 7px 13px;
  border: 1px solid var(--vt-05-line);
  border-radius: 99px;
  overflow-wrap: anywhere;
}

@supports not selector(:has(*)) {
  .vt-05__rail::before {
    opacity: 0;
  }

  .vt-05__radio:checked+.vt-05__tab {
    background: color-mix(in oklch,var(--vt-05-acc) 22%,transparent);
  }
}

@media (max-width: 640px) {
  .vt-05__card {
    grid-template-columns: 1fr;
  }

  .vt-05__rail {
    border-right: 0;
    border-bottom: 1px solid var(--vt-05-line);
  }
}

@media (prefers-reduced-motion: reduce) {
  .vt-05 * {
    transition-duration: .01ms !important;
  }
}
```
