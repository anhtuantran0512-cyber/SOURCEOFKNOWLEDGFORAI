---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-claymorphism/clay-badge-and-pill-tag-system/"
title: "Clay Badge & Pill Tag System"
section: "design-styles"
category: "css-claymorphism"
category_name: "CSS Claymorphism"
description: "A full badge and tag system at clay scale: status badges with semantic hues, count bubbles that sit on an avatar, removable filter tags that vanish on click…"
has_js: "false"
---

Here's a working CSS Claymorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Clay Badge & Pill Tag System
Source: https://codefronts.com/design-styles/css-claymorphism/clay-badge-and-pill-tag-system/

A full badge and tag system at clay scale: status badges with semantic hues, count bubbles that sit on an avatar, removable filter tags that vanish on click with pure CSS, and a size scale from 20px micro-dot to 40px pill. The lesson here is scale discipline — the three-layer recipe has to be re-tuned, not shrunk, once an object drops below ~32px.
## HTML
```html
<section class="cl-12" aria-label="Clay badge and pill tag system demo">
  <div class="cl-12__stage">
    <div class="cl-12__panel">
      <section class="cl-12__block">
        <h3 class="cl-12__lab">Status badges</h3>
        <div class="cl-12__row">
          <span class="cl-12__badge" style="--cl-12-h:150"><i aria-hidden="true"></i>Published</span>
          <span class="cl-12__badge" style="--cl-12-h:85"><i aria-hidden="true"></i>In review</span>
          <span class="cl-12__badge" style="--cl-12-h:25"><i aria-hidden="true"></i>Blocked</span>
          <span class="cl-12__badge" style="--cl-12-h:250"><i aria-hidden="true"></i>Scheduled</span>
          <span class="cl-12__badge cl-12__badge--ghost"><i aria-hidden="true"></i>Draft</span>
        </div>
      </section>
      <section class="cl-12__block">
        <h3 class="cl-12__lab">Size scale · one --u unit</h3>
        <div class="cl-12__row cl-12__row--base">
          <span class="cl-12__pill" style="--cl-12-u:.62;font-size:11px">micro</span>
          <span class="cl-12__pill" style="--cl-12-u:.8;font-size:12.5px">small</span>
          <span class="cl-12__pill" style="--cl-12-u:1">base</span>
          <span class="cl-12__pill" style="--cl-12-u:1.25;font-size:16px">large</span>
          <span class="cl-12__pill" style="--cl-12-u:1.5;font-size:18px">hero</span>
        </div>
      </section>
      <section class="cl-12__block">
        <h3 class="cl-12__lab">Count bubbles</h3>
        <div class="cl-12__row">
          <span class="cl-12__avatar cl-12__avatar--a">JD<b class="cl-12__count" aria-label="3 unread messages">3</b></span>
          <span class="cl-12__avatar cl-12__avatar--b">SR<b class="cl-12__count cl-12__count--hot" aria-label="12 unread messages">12</b></span>
          <span class="cl-12__avatar cl-12__avatar--c">MK<b class="cl-12__count cl-12__count--dot" aria-label="New activity"></b></span>
        </div>
      </section>
      <section class="cl-12__block">
        <h3 class="cl-12__lab">Removable filter tags · pure CSS</h3>
        <div class="cl-12__row">
          <label class="cl-12__tag">Motion<input type="checkbox" aria-label="Remove tag: Motion"><span class="cl-12__x" aria-hidden="true"></span></label>
          <label class="cl-12__tag">Shadows<input type="checkbox" aria-label="Remove tag: Shadows"><span class="cl-12__x" aria-hidden="true"></span></label>
          <label class="cl-12__tag">Radius<input type="checkbox" aria-label="Remove tag: Radius"><span class="cl-12__x" aria-hidden="true"></span></label>
          <label class="cl-12__tag">Tailwind<input type="checkbox" aria-label="Remove tag: Tailwind"><span class="cl-12__x" aria-hidden="true"></span></label>
          <label class="cl-12__tag">A11y<input type="checkbox" aria-label="Remove tag: A11y"><span class="cl-12__x" aria-hidden="true"></span></label>
        </div>
      </section>
    </div>
    <p class="cl-12__chip" aria-hidden="true">layers scale from --u · :has(:checked) removal · hue-only semantics</p>
  </div>
</section>
```
## CSS
```css
.cl-12,
.cl-12 *,
.cl-12 *::before,
.cl-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cl-12 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--cl-12-bg);
  --cl-12-bg: oklch(0.94 0.022 320);
  --cl-12-clay: oklch(0.89 0.05 320);
  --cl-12-shade: oklch(0.55 0.08 320/.5);
  --cl-12-light: oklch(1 0.01 320/.95);
  --cl-12-ink: oklch(0.28 0.05 320);
  --cl-12-mut: oklch(0.5 0.04 320);
  font-family: system-ui,-apple-system,'Segoe UI',sans-serif;
  color: var(--cl-12-ink);
}

.cl-12__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 20px;
  padding: clamp(20px,5vw,56px);
}

.cl-12__panel {
  width: min(100%,720px);
  display: grid;
  gap: clamp(18px,3vw,26px);
  padding: clamp(22px,3.4vw,34px);
  border-radius: 42px;
  background: color-mix(in oklch,var(--cl-12-bg) 92%,white);
  box-shadow: 0 30px 60px -24px var(--cl-12-shade),inset 0 -16px 28px -16px var(--cl-12-shade),inset 0 18px 28px -12px var(--cl-12-light);
}

.cl-12__block {
  display: grid;
  gap: 12px;
}

.cl-12__lab {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--cl-12-mut);
}

.cl-12__row {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  align-items: center;
}

.cl-12__row--base {
  align-items: baseline;
}

.cl-12__badge {
  --cl-12-h: 320;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  min-height: 34px;
  padding: 0 15px;
  border-radius: 99px;
  font-size: 13px;
  font-weight: 660;
  color: oklch(0.3 0.06 var(--cl-12-h));
  background: oklch(0.88 0.075 var(--cl-12-h));
  box-shadow: 0 7px 13px -5px oklch(0.55 0.1 var(--cl-12-h)/.5),inset 0 -5px 9px -6px oklch(0.55 0.1 var(--cl-12-h)/.55),inset 0 6px 9px -5px oklch(1 0.02 var(--cl-12-h)/.95);
  transition: translate .22s cubic-bezier(.34,1.4,.5,1);
}

.cl-12__badge:hover {
  translate: 0 -2px;
}

.cl-12__badge i {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: oklch(0.62 0.16 var(--cl-12-h));
  box-shadow: inset 0 2px 3px -1px oklch(1 0 0/.7);
}

.cl-12__badge--ghost {
  color: var(--cl-12-mut);
  background: color-mix(in oklch,var(--cl-12-bg) 90%,white);
  box-shadow: inset 0 5px 10px -5px var(--cl-12-shade),inset 0 -4px 8px -6px var(--cl-12-light);
}

.cl-12__badge--ghost i {
  background: var(--cl-12-mut);
}

.cl-12__pill {
  --cl-12-u: 1;
  display: inline-grid;
  place-items: center;
  min-height: calc(34px * var(--cl-12-u));
  padding: 0 calc(18px * var(--cl-12-u));
  border-radius: 99px;
  font-size: 14px;
  font-weight: 660;
  background: var(--cl-12-clay);
  box-shadow: 0 calc(6px * var(--cl-12-u)) calc(12px * var(--cl-12-u)) calc(-4px * var(--cl-12-u)) var(--cl-12-shade),inset 0 calc(-5px * var(--cl-12-u)) calc(9px * var(--cl-12-u)) -6px var(--cl-12-shade),inset 0 calc(6px * var(--cl-12-u)) calc(9px * var(--cl-12-u)) -5px var(--cl-12-light);
}

.cl-12__avatar {
  position: relative;
  display: grid;
  place-items: center;
  width: 56px;
  height: 56px;
  border-radius: 22px;
  font-size: 14px;
  font-weight: 700;
  letter-spacing: .02em;
  color: oklch(0.28 0.05 320);
  box-shadow: 0 12px 22px -10px var(--cl-12-shade),inset 0 -9px 15px -9px var(--cl-12-shade),inset 0 11px 15px -7px var(--cl-12-light);
}

.cl-12__avatar--a {
  background: oklch(0.85 0.09 30);
}

.cl-12__avatar--b {
  background: oklch(0.85 0.08 200);
}

.cl-12__avatar--c {
  background: oklch(0.86 0.09 145);
}

.cl-12__count {
  position: absolute;
  inset-block-start: -7px;
  inset-inline-end: -7px;
  display: grid;
  place-items: center;
  min-width: 24px;
  height: 24px;
  padding: 0 6px;
  border-radius: 99px;
  font-size: 12px;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
  color: oklch(0.99 0.01 320);
  background: oklch(0.62 0.16 320);
  box-shadow: 0 0 0 3px color-mix(in oklch,var(--cl-12-bg) 92%,white),0 6px 10px -4px var(--cl-12-shade),inset 0 5px 7px -4px oklch(1 0 0/.55);
}

.cl-12__count--hot {
  background: oklch(0.6 0.19 25);
}

.cl-12__count--dot {
  min-width: 14px;
  height: 14px;
  padding: 0;
  background: oklch(0.72 0.17 150);
}

.cl-12__tag {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  min-height: 38px;
  padding: 0 8px 0 16px;
  border-radius: 99px;
  font-size: 13.5px;
  font-weight: 640;
  cursor: pointer;
  background: color-mix(in oklch,var(--cl-12-clay) 70%,white);
  box-shadow: 0 8px 15px -6px var(--cl-12-shade),inset 0 -6px 11px -7px var(--cl-12-shade),inset 0 7px 11px -6px var(--cl-12-light);
  transition: scale .32s cubic-bezier(.34,1.3,.5,1),opacity .3s,margin .32s,translate .22s;
}

.cl-12__tag:hover {
  translate: 0 -2px;
}

.cl-12__tag input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.cl-12__x {
  position: relative;
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: color-mix(in oklch,var(--cl-12-bg) 84%,white);
  box-shadow: inset 0 4px 7px -4px var(--cl-12-shade);
}

.cl-12__x::before,
.cl-12__x::after {
  content: '';
  position: absolute;
  left: 6px;
  top: 10.5px;
  width: 10px;
  height: 2px;
  border-radius: 2px;
  background: var(--cl-12-mut);
}

.cl-12__x::before {
  rotate: 45deg;
}

.cl-12__x::after {
  rotate: -45deg;
}

.cl-12__tag:has(input:focus-visible) {
  outline: 3px solid var(--cl-12-ink);
  outline-offset: 3px;
}

.cl-12__tag:has(input:checked) {
  scale: .55;
  opacity: 0;
  margin-inline-end: -14px;
  pointer-events: none;
}

.cl-12__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--cl-12-mut);
  padding: 9px 16px;
  border-radius: 99px;
  text-align: center;
  background: oklch(1 0 0/.55);
  box-shadow: inset 0 -4px 10px -8px var(--cl-12-shade),inset 0 6px 10px -6px oklch(1 0 0);
}

@media (prefers-reduced-motion: reduce) {
  .cl-12 * {
    transition-duration: .01ms !important;
  }
}
```
