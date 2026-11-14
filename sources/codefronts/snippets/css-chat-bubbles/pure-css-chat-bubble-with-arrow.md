---
source: "codefronts"
url: "https://codefronts.com/snippets/css-chat-bubbles/pure-css-chat-bubble-with-arrow/"
title: "Pure CSS Chat Bubble With Arrow"
section: "snippets"
category: "css-chat-bubbles"
category_name: "CSS Chat Bubbles"
description: "Six tail silhouettes drawn with zero SVG and zero extra markup, across three techniques: two ::after border-triangle variants (a baseline wedge and a centred…"
has_js: "false"
---

Here's a working CSS Chat Bubble from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure CSS Chat Bubble With Arrow
Source: https://codefronts.com/snippets/css-chat-bubbles/pure-css-chat-bubble-with-arrow/

Six tail silhouettes drawn with zero SVG and zero extra markup, across three techniques: two ::after border-triangle variants (a baseline wedge and a centred arrow), three clip-path polygons (straight wedge, concave curl, pixel staircase), and the real curved iOS-style curl built from two pseudo-elements. Flip between them with the segmented control — the switch is a radio group read by :has(), so the whole demo is genuinely stylesheet-only, including the light/dark toggle.
## HTML
```html
<div class="cb-01">
  <input class="cb-01__sr" type="checkbox" id="cb-01-dark">
  <label class="cb-01__theme" for="cb-01-dark">
    <svg class="cb-01__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="cb-01__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.9 5.9 7.3 7.3M16.7 16.7l1.4 1.4M18.1 5.9l-1.4 1.4M7.3 16.7l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <span class="cb-01__sr-text">Dark theme</span>
  </label>

  <input class="cb-01__sr" type="radio" name="cb-01-tail" id="cb-01-border" checked>
  <input class="cb-01__sr" type="radio" name="cb-01-tail" id="cb-01-arrow">
  <input class="cb-01__sr" type="radio" name="cb-01-tail" id="cb-01-clip">
  <input class="cb-01__sr" type="radio" name="cb-01-tail" id="cb-01-leaf">
  <input class="cb-01__sr" type="radio" name="cb-01-tail" id="cb-01-step">
  <input class="cb-01__sr" type="radio" name="cb-01-tail" id="cb-01-curve">

  <div class="cb-01__stage">
    <ol class="cb-01__thread" aria-label="Conversation">
      <li class="cb-01__turn cb-01__turn--in">
        <p class="cb-01__msg cb-01__msg--in"><b class="cb-01__who">Priya:</b> The tail is a pseudo-element — no SVG, no extra div.</p>
      </li>
      <li class="cb-01__turn cb-01__turn--out">
        <p class="cb-01__msg cb-01__msg--out"><b class="cb-01__who">You:</b> So one element carries the bubble and the arrow?</p>
      </li>
      <li class="cb-01__turn cb-01__turn--in">
        <p class="cb-01__msg cb-01__msg--in"><b class="cb-01__who">Priya:</b> Exactly. Switch the technique below and watch the same markup change shape.</p>
      </li>
    </ol>

    <div class="cb-01__switch" role="radiogroup" aria-label="Tail technique">
      <label class="cb-01__chip" for="cb-01-border"><span>border</span><code>wedge</code></label>
      <label class="cb-01__chip" for="cb-01-arrow"><span>border</span><code>arrow</code></label>
      <label class="cb-01__chip" for="cb-01-clip"><span>clip-path</span><code>wedge</code></label>
      <label class="cb-01__chip" for="cb-01-leaf"><span>clip-path</span><code>curl</code></label>
      <label class="cb-01__chip" for="cb-01-step"><span>clip-path</span><code>stepped</code></label>
      <label class="cb-01__chip" for="cb-01-curve"><span>curved</span><code>radius</code></label>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

@property --cb-01-tail {
  syntax: '<length>';
  inherits: true;
  initial-value: 11px;
}

.cb-01 {
  --bg: #f1f2f6;
  --surface: #ffffff;
  --ink: #0b0e14;
  --muted: #5b6474;
  --line: #e2e6ee;
  --acc: #3a27e6;
  --acc-ink: #ffffff;
  --in: #ffffff;
  --in-ink: #0b0e14;
  --ring: #3a27e6;
  --shadow: rgba(11,14,20,.14);
  --radius: 1.35rem;
  --cb-01-tail: 11px;
  --sans: "Instrument Sans",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
  background: radial-gradient(120% 80% at 50% -20%, color-mix(in oklab,var(--acc) 13%,transparent), transparent 60%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.cb-01,
.cb-01 *,
.cb-01 *::before,
.cb-01 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .cb-01 {
    --bg: oklch(96.2% .005 265);
    --surface: oklch(100% 0 0);
    --ink: oklch(17% .02 265);
    --muted: oklch(53% .02 265);
    --line: oklch(91% .008 265);
    --acc: oklch(52% .24 275);
    --in: oklch(100% 0 0);
    --in-ink: oklch(17% .02 265);
  }
}
/* ── visually hidden, still focusable ── */

.cb-01__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  margin: 0;
  overflow: hidden;
  clip: rect(0 0 0 0);
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
  opacity: 0;
}

.cb-01__sr-text {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}
/* ── theme toggle ── */

.cb-01__theme {
  position: absolute;
  inset-block-start: clamp(.9rem,3vw,1.6rem);
  inset-inline-end: clamp(.9rem,3vw,1.6rem);
  inline-size: 44px;
  block-size: 44px;
  display: grid;
  place-items: center;
  cursor: pointer;
  border-radius: 14px;
  border: 1px solid var(--line);
  background: var(--surface);
  color: var(--ink);
  box-shadow: 0 2px 10px -6px var(--shadow);
  transition: transform .25s cubic-bezier(.16,1,.3,1), background .25s;
}

.cb-01__theme:hover {
  transform: translateY(-2px);
}

.cb-01__theme svg {
  inline-size: 20px;
  block-size: 20px;
}

.cb-01__sun {
  display: none;
}

.cb-01__sr:focus-visible + .cb-01__theme {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}
/* ── layout ── */

.cb-01__stage {
  inline-size: min(100%,42rem);
  display: grid;
  gap: clamp(1.25rem,3vw,2rem);
  container-type: inline-size;
}

.cb-01__thread {
  list-style: none;
  margin: 0;
  padding: clamp(1rem,3cqi,1.75rem);
  display: grid;
  gap: .7rem;
  border-radius: calc(var(--radius) + .6rem);
  background: color-mix(in oklab,var(--surface) 55%,transparent);
  border: 1px solid color-mix(in oklab,var(--line) 70%,transparent);
  backdrop-filter: blur(14px) saturate(1.3);
}

.cb-01__turn {
  display: flex;
}

.cb-01__turn--in {
  justify-content: flex-start;
}

.cb-01__turn--out {
  justify-content: flex-end;
}
/* ── the bubble ── */

.cb-01__msg {
  position: relative;
  margin: 0;
  max-inline-size: min(30rem,82cqi);
  padding: .8rem 1.1rem;
  font-size: clamp(.95rem,.4cqi + .88rem,1.05rem);
  line-height: 1.5;
  letter-spacing: -.006em;
  text-wrap: pretty;
  border-radius: var(--radius);
  filter: drop-shadow(0 8px 18px color-mix(in oklab,var(--shadow) 55%,transparent));
  animation: cb-01-pop .5s cubic-bezier(.16,1,.3,1) backwards;
}

.cb-01__turn:nth-child(2) .cb-01__msg {
  animation-delay: .09s;
}

.cb-01__turn:nth-child(3) .cb-01__msg {
  animation-delay: .18s;
}

.cb-01__msg--in {
  background: var(--in);
  color: var(--in-ink);
  border-end-start-radius: 0;
  transform-origin: 0 100%;
}

.cb-01__msg--out {
  background: var(--acc);
  color: var(--acc-ink);
  border-end-end-radius: 0;
  transform-origin: 100% 100%;
}

.cb-01__who {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

@keyframes cb-01-pop {
  from {
    opacity: 0;
    transform: translateY(10px) scale(.94);
  }

  to {
    opacity: 1;
    transform: none;
  }
}
/* ═══ TECHNIQUE 1 — border triangle (default) ═══ */

.cb-01__msg::after {
  content: '';
  position: absolute;
  inset-block-end: 0;
}

.cb-01__msg--in::after {
  inset-inline-start: calc(var(--cb-01-tail) * -1 + 1px);
  /* 1px overlap kills the seam */
  border-block-start: var(--cb-01-tail) solid transparent;
  border-inline-end: var(--cb-01-tail) solid var(--in);
}

.cb-01__msg--out::after {
  inset-inline-end: calc(var(--cb-01-tail) * -1 + 1px);
  border-block-start: var(--cb-01-tail) solid transparent;
  border-inline-start: var(--cb-01-tail) solid var(--acc);
}
/* ═══ TECHNIQUE 1b — border ARROW: isosceles, centred on the side ═══ */

.cb-01:has(#cb-01-arrow:checked) .cb-01__msg {
  border-radius: var(--radius);
}

.cb-01:has(#cb-01-arrow:checked) .cb-01__msg::after {
  inset-block: 50% auto;
  translate: 0 -50%;
  border-block: calc(var(--cb-01-tail) * .8) solid transparent;
  border-block-start-color: transparent;
}

.cb-01:has(#cb-01-arrow:checked) .cb-01__msg--in::after {
  inset-inline-start: calc(var(--cb-01-tail) * -1 + 1px);
  border-inline-end: var(--cb-01-tail) solid var(--in);
}

.cb-01:has(#cb-01-arrow:checked) .cb-01__msg--out::after {
  inset-inline-end: calc(var(--cb-01-tail) * -1 + 1px);
  border-inline-start: var(--cb-01-tail) solid var(--acc);
}
/* ═══ TECHNIQUE 2 — clip-path polygon, three silhouettes from one box ═══ */

.cb-01:has(#cb-01-clip:checked) .cb-01__msg::after,
.cb-01:has(#cb-01-leaf:checked) .cb-01__msg::after,
.cb-01:has(#cb-01-step:checked) .cb-01__msg::after {
  --w: calc(var(--cb-01-tail) + 5px);
  border: 0;
  inline-size: var(--w);
  block-size: var(--cb-01-tail);
}
/* paint the flat fill, not the bubble's inherited background layers */

.cb-01:has(#cb-01-clip:checked) .cb-01__msg--in::after,
.cb-01:has(#cb-01-leaf:checked) .cb-01__msg--in::after,
.cb-01:has(#cb-01-step:checked) .cb-01__msg--in::after {
  background: var(--in);
}

.cb-01:has(#cb-01-clip:checked) .cb-01__msg--out::after,
.cb-01:has(#cb-01-leaf:checked) .cb-01__msg--out::after,
.cb-01:has(#cb-01-step:checked) .cb-01__msg--out::after {
  background: var(--acc);
}

.cb-01:has(#cb-01-clip:checked) .cb-01__msg--in::after,
.cb-01:has(#cb-01-leaf:checked) .cb-01__msg--in::after,
.cb-01:has(#cb-01-step:checked) .cb-01__msg--in::after {
  inset-inline-start: calc(var(--w) * -1 + 1px);
}

.cb-01:has(#cb-01-clip:checked) .cb-01__msg--out::after,
.cb-01:has(#cb-01-leaf:checked) .cb-01__msg--out::after,
.cb-01:has(#cb-01-step:checked) .cb-01__msg--out::after {
  inset-inline-end: calc(var(--w) * -1 + 1px);
}
/* 2a · straight wedge */

.cb-01:has(#cb-01-clip:checked) .cb-01__msg--in::after {
  clip-path: polygon(100% 0, 100% 100%, 0 100%);
}

.cb-01:has(#cb-01-clip:checked) .cb-01__msg--out::after {
  clip-path: polygon(0 0, 0 100%, 100% 100%);
}
/* 2b · curl — a concave hypotenuse approximated with five points */

.cb-01:has(#cb-01-leaf:checked) .cb-01__msg::after {
  --w: calc(var(--cb-01-tail) + 8px);
  block-size: calc(var(--cb-01-tail) + 4px);
}

.cb-01:has(#cb-01-leaf:checked) .cb-01__msg--in::after {
  clip-path: polygon(100% 0, 74% 40%, 40% 74%, 0 100%, 100% 100%);
}

.cb-01:has(#cb-01-leaf:checked) .cb-01__msg--out::after {
  clip-path: polygon(0 0, 26% 40%, 60% 74%, 100% 100%, 0 100%);
}
/* 2c · stepped — a three-tread staircase, no antialiasing anywhere */

.cb-01:has(#cb-01-step:checked) .cb-01__msg::after {
  --w: calc(var(--cb-01-tail) + 7px);
  block-size: calc(var(--cb-01-tail) + 1px);
}

.cb-01:has(#cb-01-step:checked) .cb-01__msg--in::after {
  clip-path: polygon(100% 0, 100% 100%, 0 100%, 0 66%, 34% 66%, 34% 33%, 67% 33%, 67% 0);
}

.cb-01:has(#cb-01-step:checked) .cb-01__msg--out::after {
  clip-path: polygon(0 0, 0 100%, 100% 100%, 100% 66%, 66% 66%, 66% 33%, 33% 33%, 33% 0);
}
/* ═══ TECHNIQUE 3 — curved iOS-style curl (two pseudo-elements) ═══ */

.cb-01:has(#cb-01-curve:checked) .cb-01__msg {
  border-radius: var(--radius);
}

.cb-01:has(#cb-01-curve:checked) .cb-01__msg::before,
.cb-01:has(#cb-01-curve:checked) .cb-01__msg::after {
  content: '';
  position: absolute;
  inset-block-end: 0;
  border: 0;
  clip-path: none;
  inline-size: 20px;
  block-size: 21px;
}

.cb-01:has(#cb-01-curve:checked) .cb-01__msg--in::before {
  background: var(--in);
  inset-inline-start: -7px;
  border-end-end-radius: 16px 14px;
}

.cb-01:has(#cb-01-curve:checked) .cb-01__msg--in::after {
  background: var(--bg);
  inset-inline-start: -20px;
  border-end-end-radius: 10px;
}

.cb-01:has(#cb-01-curve:checked) .cb-01__msg--out::before {
  background: var(--acc);
  inset-inline-end: -7px;
  border-end-start-radius: 16px 14px;
}

.cb-01:has(#cb-01-curve:checked) .cb-01__msg--out::after {
  background: var(--bg);
  inset-inline-end: -20px;
  border-end-start-radius: 10px;
}

.cb-01:has(#cb-01-curve:checked) .cb-01__msg {
  filter: none;
  box-shadow: 0 8px 18px -12px var(--shadow);
}
/* --cb-01-tail is registered, so it CAN be transitioned — but resizing a tail on hover
   shifts its anchor mid-transition and exposes a hairline. Lift the bubble instead. */

.cb-01__msg {
  transition: translate .3s cubic-bezier(.16,1,.3,1);
}

.cb-01__msg:hover {
  translate: 0 -2px;
}
/* ── segmented switch ── */

.cb-01__switch {
  display: flex;
  flex-wrap: wrap;
  gap: .5rem;
  justify-content: center;
  padding: .4rem;
  border-radius: 1rem;
  background: color-mix(in oklab,var(--surface) 70%,transparent);
  border: 1px solid var(--line);
  box-shadow: 0 1px 0 color-mix(in oklab,var(--surface) 90%,transparent) inset;
}

.cb-01__chip {
  display: grid;
  gap: .05rem;
  justify-items: center;
  cursor: pointer;
  user-select: none;
  min-block-size: 44px;
  padding: .45rem .95rem;
  border-radius: .75rem;
  color: var(--muted);
  transition: background .22s, color .22s, transform .22s cubic-bezier(.16,1,.3,1);
}

.cb-01__chip span {
  font-size: .85rem;
  font-weight: 600;
  letter-spacing: -.01em;
}

.cb-01__chip code {
  font-family: var(--mono);
  font-size: .66rem;
  opacity: .75;
}

.cb-01__chip:hover {
  transform: translateY(-1px);
  color: var(--ink);
}

#cb-01-border:checked ~ .cb-01__stage .cb-01__chip[for="cb-01-border"],
#cb-01-arrow:checked ~ .cb-01__stage .cb-01__chip[for="cb-01-arrow"],
#cb-01-clip:checked ~ .cb-01__stage .cb-01__chip[for="cb-01-clip"],
#cb-01-leaf:checked ~ .cb-01__stage .cb-01__chip[for="cb-01-leaf"],
#cb-01-step:checked ~ .cb-01__stage .cb-01__chip[for="cb-01-step"],
#cb-01-curve:checked ~ .cb-01__stage .cb-01__chip[for="cb-01-curve"] {
  background: var(--acc);
  color: var(--acc-ink);
}

#cb-01-border:focus-visible ~ .cb-01__stage .cb-01__chip[for="cb-01-border"],
#cb-01-arrow:focus-visible ~ .cb-01__stage .cb-01__chip[for="cb-01-arrow"],
#cb-01-clip:focus-visible ~ .cb-01__stage .cb-01__chip[for="cb-01-clip"],
#cb-01-leaf:focus-visible ~ .cb-01__stage .cb-01__chip[for="cb-01-leaf"],
#cb-01-step:focus-visible ~ .cb-01__stage .cb-01__chip[for="cb-01-step"],
#cb-01-curve:focus-visible ~ .cb-01__stage .cb-01__chip[for="cb-01-curve"] {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}
/* ── dark ── */

.cb-01:has(#cb-01-dark:checked) {
  --bg: #0a0c11;
  --surface: #141821;
  --ink: #eef1f7;
  --muted: #98a2b3;
  --line: #242a36;
  --in: #1b212c;
  --in-ink: #eef1f7;
  --acc: #7c6bff;
  --acc-ink: #0a0c11;
  --shadow: rgba(0,0,0,.6);
}

.cb-01:has(#cb-01-dark:checked) .cb-01__moon {
  display: none;
}

.cb-01:has(#cb-01-dark:checked) .cb-01__sun {
  display: block;
}

@supports (color: oklch(0 0 0)) {
  .cb-01:has(#cb-01-dark:checked) {
    --bg: oklch(15% .015 265);
    --surface: oklch(22% .018 265);
    --ink: oklch(96% .006 265);
    --muted: oklch(70% .02 265);
    --line: oklch(29% .02 265);
    --in: oklch(26% .02 265);
    --acc: oklch(70% .17 285);
    --acc-ink: oklch(16% .02 285);
  }
}

@media (prefers-color-scheme: dark) {
  .cb-01:not(:has(#cb-01-dark:checked)) {
    --bg: #0a0c11;
    --surface: #141821;
    --ink: #eef1f7;
    --muted: #98a2b3;
    --line: #242a36;
    --in: #1b212c;
    --in-ink: #eef1f7;
    --acc: #7c6bff;
    --acc-ink: #0a0c11;
    --shadow: rgba(0,0,0,.6);
  }

  .cb-01:not(:has(#cb-01-dark:checked)) .cb-01__moon {
    display: none;
  }

  .cb-01:not(:has(#cb-01-dark:checked)) .cb-01__sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cb-01 *,
    .cb-01 *::before,
    .cb-01 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .cb-01__msg {
    border: 1px solid CanvasText;
    filter: none;
  }

  .cb-01__msg::before,
    .cb-01__msg::after {
    forced-color-adjust: none;
  }

  .cb-01__chip {
    border: 1px solid CanvasText;
  }
}
```
