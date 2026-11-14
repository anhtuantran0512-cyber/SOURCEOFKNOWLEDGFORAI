---
source: "codefronts"
url: "https://codefronts.com/snippets/css-chat-bubbles/css-speech-bubble-with-border/"
title: "CSS Speech Bubble With Border"
section: "snippets"
category: "css-chat-bubbles"
category_name: "CSS Chat Bubbles"
description: "The hardest bubble to get right: an outlined one where the tail's stroke joins the border seamlessly."
has_js: "false"
---

Here's a working CSS Chat Bubble from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Speech Bubble With Border
Source: https://codefronts.com/snippets/css-chat-bubbles/css-speech-bubble-with-border/

The hardest bubble to get right: an outlined one where the tail's stroke joins the border seamlessly. Three solutions side by side — the classic two stacked triangles, a single clip-path wedge outlined with filter: drop-shadow(), and and a nested-box stroke that can carry a gradient outline. Move the tail to any of the four sides with the pure-CSS control and watch all three follow.
## HTML
```html
<div class="cb-09">
  <input class="cb-09__sr" type="checkbox" id="cb-09-dark">
  <label class="cb-09__theme" for="cb-09-dark">
    <svg class="cb-09__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="cb-09__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.9 5.9 7.3 7.3M16.7 16.7l1.4 1.4M18.1 5.9l-1.4 1.4M7.3 16.7l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <span class="cb-09__sr-text">Dark theme</span>
  </label>

  <input class="cb-09__sr" type="radio" name="cb-09-side" id="cb-09-left" checked>
  <input class="cb-09__sr" type="radio" name="cb-09-side" id="cb-09-right">
  <input class="cb-09__sr" type="radio" name="cb-09-side" id="cb-09-top">
  <input class="cb-09__sr" type="radio" name="cb-09-side" id="cb-09-bottom">

  <div class="cb-09__stage">
    <div class="cb-09__row">
      <figure class="cb-09__cell">
        <p class="cb-09__bubble cb-09__a">Two stacked triangles: outer stroke, inner fill, offset by the mitre distance.</p>
        <figcaption class="cb-09__tag">border ×2</figcaption>
      </figure>
      <figure class="cb-09__cell">
        <p class="cb-09__bubble cb-09__b">One clipped wedge, outlined by four drop-shadows that trace the silhouette.</p>
        <figcaption class="cb-09__tag">clip-path + drop-shadow</figcaption>
      </figure>
      <figure class="cb-09__cell">
        <p class="cb-09__bubble cb-09__c"><span class="cb-09__c-in">A nested box carries the fill, so the outer box is free to hold a gradient stroke.</span></p>
        <figcaption class="cb-09__tag">nested box · gradient stroke</figcaption>
      </figure>
    </div>

    <div class="cb-09__switch" role="radiogroup" aria-label="Tail side">
      <label class="cb-09__chip" for="cb-09-left">Left</label>
      <label class="cb-09__chip" for="cb-09-right">Right</label>
      <label class="cb-09__chip" for="cb-09-top">Top</label>
      <label class="cb-09__chip" for="cb-09-bottom">Bottom</label>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

@property --cb-09-bw {
  syntax: '<length>';
  inherits: true;
  initial-value: 2px;
}

.cb-09 {
  --bg: #fbfaf7;
  --fill: #ffffff;
  --stroke: #141414;
  --ink: #141414;
  --muted: #6b6b66;
  --line: #e6e4dd;
  --acc: #ff4d2d;
  --acc-ink: #ffffff;
  --ring: #141414;
  --shadow: rgba(20,20,20,.12);
  --cb-09-bw: 2px;
  --tail: 16px;
  --radius: 1.1rem;
  --sans: "Sora",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,5vw,4rem);
  background-color: var(--bg);
  background-image: linear-gradient(var(--line) 1px, transparent 1px), linear-gradient(90deg, var(--line) 1px, transparent 1px);
  background-size: 2.5rem 2.5rem;
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.cb-09,
.cb-09 *,
.cb-09 *::before,
.cb-09 *::after {
  box-sizing: border-box;
}

.cb-09__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  opacity: 0;
}

.cb-09__sr-text {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cb-09__theme {
  position: absolute;
  inset-block-start: clamp(.9rem,3vw,1.6rem);
  inset-inline-end: clamp(.9rem,3vw,1.6rem);
  inline-size: 44px;
  block-size: 44px;
  display: grid;
  place-items: center;
  cursor: pointer;
  border-radius: 14px;
  border: 2px solid var(--stroke);
  background: var(--fill);
  color: var(--ink);
  transition: transform .25s cubic-bezier(.16,1,.3,1);
}

.cb-09__theme:hover {
  transform: translate(-1px,-2px);
}

.cb-09__theme svg {
  inline-size: 20px;
  block-size: 20px;
}

.cb-09__sun {
  display: none;
}

.cb-09__sr:focus-visible + .cb-09__theme {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.cb-09__stage {
  inline-size: min(100%,66rem);
  display: grid;
  gap: clamp(2rem,5vw,3.25rem);
  justify-items: center;
}

.cb-09__row {
  display: grid;
  gap: clamp(2rem,4vw,3rem);
  grid-template-columns: repeat(auto-fit,minmax(15rem,1fr));
  inline-size: 100%;
}

.cb-09__cell {
  margin: 0;
  display: grid;
  gap: 1rem;
  justify-items: center;
  align-content: start;
}

.cb-09__tag {
  font-family: var(--mono);
  font-size: .68rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.cb-09__bubble {
  position: relative;
  margin: 0;
  inline-size: 100%;
  max-inline-size: 19rem;
  padding: 1.05rem 1.2rem;
  border-radius: var(--radius);
  font-size: .95rem;
  line-height: 1.5;
  letter-spacing: -.008em;
  text-wrap: pretty;
  background: var(--fill);
  color: var(--ink);
  transition: --cb-09-bw .35s cubic-bezier(.16,1,.3,1), translate .35s cubic-bezier(.16,1,.3,1);
}

.cb-09__cell:hover .cb-09__bubble {
  --cb-09-bw: 3px;
  translate: 0 -3px;
}
/* ═══ A · two stacked triangles ═══ */

.cb-09__a {
  border: var(--cb-09-bw) solid var(--stroke);
}

.cb-09__a::before,
.cb-09__a::after {
  content: '';
  position: absolute;
  inline-size: 0;
  block-size: 0;
}
/* ═══ B · clip-path wedge + drop-shadow outline ═══ */

.cb-09__b {
  filter: drop-shadow(var(--cb-09-bw) 0 0 var(--stroke)) drop-shadow(calc(var(--cb-09-bw) * -1) 0 0 var(--stroke)) drop-shadow(0 var(--cb-09-bw) 0 var(--stroke)) drop-shadow(0 calc(var(--cb-09-bw) * -1) 0 var(--stroke));
}

.cb-09__b::after {
  content: '';
  position: absolute;
  background: var(--fill);
}
/* ═══ C · nested box — the only technique that supports a GRADIENT stroke ═══ */

.cb-09__c {
  border: 0;
  padding: var(--cb-09-bw);
  background: var(--stroke);
}

@supports (background: linear-gradient(in oklab,red,blue)) {
  .cb-09__c {
    background: linear-gradient(140deg in oklab, var(--stroke), color-mix(in oklab,var(--stroke) 45%,var(--acc)));
  }
}

.cb-09__c-in {
  position: relative;
  display: block;
  padding: 1.05rem 1.2rem;
  border-radius: calc(var(--radius) - var(--cb-09-bw));
  background: var(--fill);
  color: var(--ink);
}

.cb-09__c::before,
.cb-09__c::after {
  content: '';
  position: absolute;
  inline-size: 0;
  block-size: 0;
}
/* ── TAIL GEOMETRY, one block per side ── */
/* LEFT (default) */

.cb-09__a::before {
  inset-block-start: 50%;
  inset-inline-start: calc(var(--tail) * -1);
  translate: 0 -50%;
  border-block: calc(var(--tail) * .8) solid transparent;
  border-inline-end: var(--tail) solid var(--stroke);
}

.cb-09__a::after {
  inset-block-start: 50%;
  inset-inline-start: calc(var(--tail) * -1 + var(--cb-09-bw) * 1.6);
  translate: 0 -50%;
  border-block: calc(var(--tail) * .8) solid transparent;
  border-inline-end: var(--tail) solid var(--fill);
}

.cb-09__b::after {
  inset-block-start: 50%;
  inset-inline-start: calc(var(--tail) * -1 + 1px);
  translate: 0 -50%;
  inline-size: var(--tail);
  block-size: calc(var(--tail) * 1.5);
  clip-path: polygon(100% 0, 0 50%, 100% 100%);
}
/* RIGHT */

.cb-09:has(#cb-09-right:checked) .cb-09__a::before {
  inset-inline: auto calc(var(--tail) * -1);
  border-inline: 0;
  border-inline-start: var(--tail) solid var(--stroke);
  border-block: calc(var(--tail) * .8) solid transparent;
}

.cb-09:has(#cb-09-right:checked) .cb-09__a::after {
  inset-inline: auto calc(var(--tail) * -1 + var(--cb-09-bw) * 1.6);
  border-inline: 0;
  border-inline-start: var(--tail) solid var(--fill);
  border-block: calc(var(--tail) * .8) solid transparent;
}

.cb-09:has(#cb-09-right:checked) .cb-09__b::after {
  inset-inline: auto calc(var(--tail) * -1 + 1px);
  clip-path: polygon(0 0, 100% 50%, 0 100%);
}
/* TOP */

.cb-09:has(#cb-09-top:checked) .cb-09__a::before {
  inset-block: calc(var(--tail) * -1) auto;
  inset-inline-start: 50%;
  translate: -50% 0;
  border-inline: calc(var(--tail) * .8) solid transparent;
  border-block: 0;
  border-block-end: var(--tail) solid var(--stroke);
}

.cb-09:has(#cb-09-top:checked) .cb-09__a::after {
  inset-block: calc(var(--tail) * -1 + var(--cb-09-bw) * 1.6) auto;
  inset-inline-start: 50%;
  translate: -50% 0;
  border-inline: calc(var(--tail) * .8) solid transparent;
  border-block: 0;
  border-block-end: var(--tail) solid var(--fill);
}

.cb-09:has(#cb-09-top:checked) .cb-09__b::after {
  inset-block: calc(var(--tail) * -1 + 1px) auto;
  inset-inline-start: 50%;
  translate: -50% 0;
  inline-size: calc(var(--tail) * 1.5);
  block-size: var(--tail);
  clip-path: polygon(50% 0, 0 100%, 100% 100%);
}
/* BOTTOM */

.cb-09:has(#cb-09-bottom:checked) .cb-09__a::before {
  inset-block: auto calc(var(--tail) * -1);
  inset-inline-start: 50%;
  translate: -50% 0;
  border-inline: calc(var(--tail) * .8) solid transparent;
  border-block: 0;
  border-block-start: var(--tail) solid var(--stroke);
}

.cb-09:has(#cb-09-bottom:checked) .cb-09__a::after {
  inset-block: auto calc(var(--tail) * -1 + var(--cb-09-bw) * 1.6);
  inset-inline-start: 50%;
  translate: -50% 0;
  border-inline: calc(var(--tail) * .8) solid transparent;
  border-block: 0;
  border-block-start: var(--tail) solid var(--fill);
}

.cb-09:has(#cb-09-bottom:checked) .cb-09__b::after {
  inset-block: auto calc(var(--tail) * -1 + 1px);
  inset-inline-start: 50%;
  translate: -50% 0;
  inline-size: calc(var(--tail) * 1.5);
  block-size: var(--tail);
  clip-path: polygon(50% 100%, 0 0, 100% 0);
}
/* the nested-box variant draws its tail with the same two-triangle overlap, on the OUTER box */

.cb-09__c::after {
  content: '';
  position: absolute;
  inline-size: 0;
  block-size: 0;
  inset-block-start: 50%;
  inset-inline-start: calc(var(--tail) * -1);
  translate: 0 -50%;
  border-block: calc(var(--tail) * .8) solid transparent;
  border-inline-end: var(--tail) solid var(--stroke);
}

.cb-09__c::before {
  content: '';
  position: absolute;
  inline-size: 0;
  block-size: 0;
  z-index: 1;
  inset-block-start: 50%;
  inset-inline-start: calc(var(--tail) * -1 + var(--cb-09-bw) * 1.6);
  translate: 0 -50%;
  border-block: calc(var(--tail) * .8) solid transparent;
  border-inline-end: var(--tail) solid var(--fill);
}

.cb-09:has(#cb-09-right:checked) .cb-09__c::after {
  inset-inline: auto calc(var(--tail) * -1);
  border-inline: 0;
  border-inline-start: var(--tail) solid var(--stroke);
  border-block: calc(var(--tail) * .8) solid transparent;
}

.cb-09:has(#cb-09-right:checked) .cb-09__c::before {
  inset-inline: auto calc(var(--tail) * -1 + var(--cb-09-bw) * 1.6);
  border-inline: 0;
  border-inline-start: var(--tail) solid var(--fill);
  border-block: calc(var(--tail) * .8) solid transparent;
}

.cb-09:has(#cb-09-top:checked) .cb-09__c::after {
  inset-block: calc(var(--tail) * -1) auto;
  inset-inline-start: 50%;
  translate: -50% 0;
  border-inline: calc(var(--tail) * .8) solid transparent;
  border-block: 0;
  border-block-end: var(--tail) solid var(--stroke);
}

.cb-09:has(#cb-09-top:checked) .cb-09__c::before {
  inset-block: calc(var(--tail) * -1 + var(--cb-09-bw) * 1.6) auto;
  inset-inline-start: 50%;
  translate: -50% 0;
  border-inline: calc(var(--tail) * .8) solid transparent;
  border-block: 0;
  border-block-end: var(--tail) solid var(--fill);
}

.cb-09:has(#cb-09-bottom:checked) .cb-09__c::after {
  inset-block: auto calc(var(--tail) * -1);
  inset-inline-start: 50%;
  translate: -50% 0;
  border-inline: calc(var(--tail) * .8) solid transparent;
  border-block: 0;
  border-block-start: var(--tail) solid var(--stroke);
}

.cb-09:has(#cb-09-bottom:checked) .cb-09__c::before {
  inset-block: auto calc(var(--tail) * -1 + var(--cb-09-bw) * 1.6);
  inset-inline-start: 50%;
  translate: -50% 0;
  border-inline: calc(var(--tail) * .8) solid transparent;
  border-block: 0;
  border-block-start: var(--tail) solid var(--fill);
}
/* ── switch ── */

.cb-09__switch {
  display: flex;
  flex-wrap: wrap;
  gap: .4rem;
  justify-content: center;
  padding: .4rem;
  border-radius: 1rem;
  border: 2px solid var(--stroke);
  background: var(--fill);
  box-shadow: 4px 4px 0 var(--stroke);
}

.cb-09__chip {
  min-block-size: 44px;
  display: grid;
  place-items: center;
  padding: .5rem 1.15rem;
  cursor: pointer;
  border-radius: .7rem;
  color: var(--muted);
  font-size: .85rem;
  font-weight: 600;
  letter-spacing: -.01em;
  transition: background .2s, color .2s;
}

.cb-09__chip:hover {
  color: var(--ink);
}

#cb-09-left:checked ~ .cb-09__stage .cb-09__chip[for="cb-09-left"],
#cb-09-right:checked ~ .cb-09__stage .cb-09__chip[for="cb-09-right"],
#cb-09-top:checked ~ .cb-09__stage .cb-09__chip[for="cb-09-top"],
#cb-09-bottom:checked ~ .cb-09__stage .cb-09__chip[for="cb-09-bottom"] {
  background: var(--acc);
  color: var(--acc-ink);
}

#cb-09-left:focus-visible ~ .cb-09__stage .cb-09__chip[for="cb-09-left"],
#cb-09-right:focus-visible ~ .cb-09__stage .cb-09__chip[for="cb-09-right"],
#cb-09-top:focus-visible ~ .cb-09__stage .cb-09__chip[for="cb-09-top"],
#cb-09-bottom:focus-visible ~ .cb-09__stage .cb-09__chip[for="cb-09-bottom"] {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}
/* ── dark ── */

.cb-09:has(#cb-09-dark:checked) {
  --bg: #0d0d0c;
  --fill: #161615;
  --stroke: #f4f2ec;
  --ink: #f4f2ec;
  --muted: #9a9a93;
  --line: #1f1f1d;
  --acc: #ff6a4d;
  --acc-ink: #14100f;
}

.cb-09:has(#cb-09-dark:checked) .cb-09__moon {
  display: none;
}

.cb-09:has(#cb-09-dark:checked) .cb-09__sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .cb-09:not(:has(#cb-09-dark:checked)) {
    --bg: #0d0d0c;
    --fill: #161615;
    --stroke: #f4f2ec;
    --ink: #f4f2ec;
    --muted: #9a9a93;
    --line: #1f1f1d;
    --acc: #ff6a4d;
    --acc-ink: #14100f;
  }

  .cb-09:not(:has(#cb-09-dark:checked)) .cb-09__moon {
    display: none;
  }

  .cb-09:not(:has(#cb-09-dark:checked)) .cb-09__sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cb-09 *,
    .cb-09 *::before,
    .cb-09 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .cb-09__bubble {
    border: 2px solid CanvasText !important;
    filter: none !important;
    background: Canvas !important;
  }
}
```
