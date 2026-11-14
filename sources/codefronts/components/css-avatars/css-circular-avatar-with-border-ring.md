---
source: "codefronts"
url: "https://codefronts.com/components/css-avatars/css-circular-avatar-with-border-ring/"
title: "CSS Circular Avatar with Border Ring"
section: "components"
category: "css-avatars"
category_name: "CSS Avatars"
description: "The production default, done properly: the ring is a box-shadow spread rather than a border, so it paints outside the box and costs zero layout — swap a 2px…"
has_js: "false"
---

Here's a working CSS Avatar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Circular Avatar with Border Ring
Source: https://codefronts.com/components/css-avatars/css-circular-avatar-with-border-ring/

The production default, done properly: the ring is a box-shadow spread rather than a border, so it paints outside the box and costs zero layout — swap a 2px ring for a 6px one and nothing in the row moves. Three treatments sit side by side (solid, offset-gap, double) and a real radio group retunes ring width live through one custom property, with no JavaScript.
## HTML
```html
<div class="av-01">
  <input class="av-01__sr" type="checkbox" id="av-01-dark">
  <label class="av-01__theme" for="av-01-dark">
    <svg class="av-01__i av-01__i--moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.3A8.4 8.4 0 0 1 9.7 3.5a8.5 8.5 0 1 0 10.8 10.8Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="av-01__i av-01__i--sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.1" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.7 5.7l1.4 1.4M16.9 16.9l1.4 1.4M18.3 5.7l-1.4 1.4M7.1 16.9l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <span class="av-01__vh">Dark theme</span>
  </label>

  <div class="av-01__stage">
    <section class="av-01__wrap" aria-labelledby="av-01-h">
      <header class="av-01__head">
        <p class="av-01__eyebrow">Identity · Avatar</p>
        <h2 class="av-01__h" id="av-01-h">Ring treatments</h2>
        <p class="av-01__sub">Ring width is a token, not a border — the row never reflows.</p>
      </header>

      <fieldset class="av-01__seg">
        <legend class="av-01__vh">Ring width</legend>
        <label class="av-01__segbtn"><input type="radio" name="av-01-w" id="av-01-w2"><span>2px</span></label>
        <label class="av-01__segbtn"><input type="radio" name="av-01-w" id="av-01-w3" checked><span>3px</span></label>
        <label class="av-01__segbtn"><input type="radio" name="av-01-w" id="av-01-w4"><span>4px</span></label>
      </fieldset>

      <ul class="av-01__row">
        <li class="av-01__item">
          <span class="av-01__fig av-01__fig--solid">
            <img class="av-01__img" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=200&auto=format&fit=facearea&facepad=2.5" alt="Priya Sharma" width="200" height="200" loading="lazy" decoding="async">
          </span>
          <p class="av-01__name">Priya Sharma</p>
          <p class="av-01__meta">Solid</p>
          <code class="av-01__snip">0 0 0 var(--rw)</code>
        </li>
        <li class="av-01__item">
          <span class="av-01__fig av-01__fig--gap">
            <img class="av-01__img" src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=200&auto=format&fit=facearea&facepad=2.5" alt="Alex Chen" width="200" height="200" loading="lazy" decoding="async">
          </span>
          <p class="av-01__name">Alex Chen</p>
          <p class="av-01__meta">Offset gap</p>
          <code class="av-01__snip">3px panel + ring</code>
        </li>
        <li class="av-01__item">
          <span class="av-01__fig av-01__fig--double">
            <img class="av-01__img" src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=200&auto=format&fit=facearea&facepad=2.5" alt="Maya Okonkwo" width="200" height="200" loading="lazy" decoding="async">
          </span>
          <p class="av-01__name">Maya Okonkwo</p>
          <p class="av-01__meta">Double</p>
          <code class="av-01__snip">ring + halo</code>
        </li>
      </ul>

      <p class="av-01__foot">Rings paint outside the border box, so switching width shifts nothing.</p>
    </section>
  </div>
</div>
```
## CSS
```css
@supports (color: oklch(50% .1 250)) {
  .av-01 {
    --page: oklch(97.6% .004 265);
    --panel: oklch(100% 0 0);
    --panel-2: oklch(96.4% .006 265);
    --ink: oklch(20% .022 265);
    --muted: oklch(53% .022 265);
    --line: oklch(92% .008 265);
    --accent: oklch(58% .196 272);
  }
}

@supports (background: color-mix(in oklab, red, blue)) {
  .av-01__fig--double {
    --halo: color-mix(in oklab, var(--accent) 32%, transparent);
  }
}

@property --av-01-rw {
  syntax: '<length>';
  inherits: true;
  initial-value: 3px;
}

.av-01 {
  --page: #f7f8fa;
  --panel: #ffffff;
  --panel-2: #f1f3f7;
  --ink: #10131a;
  --muted: #5f6672;
  --line: #e4e7ee;
  --accent: #4f46e5;
  --glass: rgba(255,255,255,.68);
  --shadow: 0 1px 2px rgba(16,19,26,.05), 0 16px 36px -20px rgba(16,19,26,.3);
  --r: 16px;
  --av-01-rw: 3px;
  --rw: var(--av-01-rw);
  --halo: rgba(79,70,229,.32);
  width: 100%;
  inline-size: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui,-apple-system,"Segoe UI",sans-serif;
  -webkit-font-smoothing: antialiased;
}

.av-01 *,
.av-01 *::before,
.av-01 *::after {
  box-sizing: border-box;
}

.av-01__vh {
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

.av-01__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  margin: 0;
  pointer-events: none;
}

.av-01__theme {
  position: absolute;
  inset-block-start: clamp(.85rem,2.2vw,1.5rem);
  inset-inline-end: clamp(.85rem,2.2vw,1.5rem);
  z-index: 20;
  display: grid;
  place-items: center;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  border-radius: 999px;
  border: 1px solid var(--line);
  background: var(--glass);
  color: var(--ink);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  cursor: pointer;
  transition: translate .2s ease, background .2s ease;
}

.av-01__theme::after {
  content: "";
  position: absolute;
  inset: -.4rem;
  border-radius: inherit;
}

.av-01__theme:hover {
  translate: 0 -1px;
}

.av-01__i {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.av-01__i--sun {
  display: none;
}

.av-01__sr:focus-visible + .av-01__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.av-01__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
}

.av-01__wrap {
  inline-size: min(56rem,100%);
  display: flex;
  flex-direction: column;
  gap: clamp(1.25rem,3vw,2rem);
}

.av-01__head {
  display: flex;
  flex-direction: column;
  gap: .4rem;
  padding-inline-end: 3.5rem;
}

.av-01__eyebrow {
  margin: 0;
  font-size: .7rem;
  font-weight: 600;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.av-01__h {
  margin: 0;
  font-size: clamp(1.6rem,4.2vw,2.4rem);
  font-weight: 650;
  letter-spacing: -.03em;
  line-height: 1.05;
}

.av-01__sub {
  margin: 0;
  max-inline-size: 34rem;
  font-size: .95rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.av-01__seg {
  display: inline-flex;
  align-self: flex-start;
  gap: .15rem;
  margin: 0;
  padding: .25rem;
  border: 1px solid var(--line);
  border-radius: 999px;
  background: var(--panel);
  box-shadow: var(--shadow);
}

.av-01__segbtn {
  position: relative;
}

.av-01__segbtn input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  margin: 0;
}

.av-01__segbtn span {
  display: grid;
  place-items: center;
  min-inline-size: 3.25rem;
  min-block-size: 2.25rem;
  padding: 0 .6rem;
  border-radius: 999px;
  font-size: .8rem;
  font-weight: 600;
  font-variant-numeric: tabular-nums;
  color: var(--muted);
  cursor: pointer;
  transition: background .18s ease, color .18s ease;
}

.av-01__segbtn:hover span {
  background: var(--panel-2);
}

.av-01__segbtn input:checked + span {
  background: var(--ink);
  color: var(--panel);
}

.av-01__segbtn input:focus-visible + span {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.av-01__row {
  --size: clamp(4.5rem,13vw,7rem);
  list-style: none;
  margin: 0;
  padding: clamp(1.5rem,4vw,2.5rem) clamp(1rem,3vw,2rem);
  display: grid;
  gap: clamp(1.5rem,4vw,3rem);
  grid-template-columns: repeat(auto-fit,minmax(9rem,1fr));
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: var(--r);
  box-shadow: var(--shadow);
}

.av-01__item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: .55rem;
  text-align: center;
}

.av-01__fig {
  position: relative;
  display: block;
  inline-size: var(--size);
  aspect-ratio: 1;
  border-radius: 50%;
  background: var(--panel-2);
  transition: translate .24s cubic-bezier(.2,.7,.3,1), box-shadow .24s ease, --av-01-rw .24s ease;
}

.av-01__item:hover .av-01__fig {
  translate: 0 -4px;
}

.av-01__img {
  display: block;
  inline-size: 100%;
  block-size: auto;
  aspect-ratio: 1;
  border-radius: inherit;
  object-fit: cover;
  object-position: center top;
}

.av-01__fig--solid {
  box-shadow: 0 0 0 var(--rw) var(--accent);
}

.av-01__fig--gap {
  box-shadow: 0 0 0 3px var(--panel), 0 0 0 calc(3px + var(--rw)) var(--accent);
}

.av-01__fig--double {
  box-shadow: 0 0 0 var(--rw) var(--accent), 0 0 0 calc(var(--rw) + 3px) var(--panel), 0 0 0 calc(var(--rw) * 2 + 3px) var(--halo);
}

.av-01__name {
  margin: 0;
  font-size: .95rem;
  font-weight: 600;
  letter-spacing: -.01em;
}

.av-01__meta {
  margin: -.35rem 0 0;
  font-size: .8rem;
  color: var(--muted);
}

.av-01__snip {
  font-size: .68rem;
  font-family: ui-monospace,SFMono-Regular,Menlo,monospace;
  letter-spacing: -.01em;
  color: var(--muted);
  padding: .2rem .45rem;
  border-radius: 6px;
  background: var(--panel-2);
}

.av-01__foot {
  margin: 0;
  font-size: .82rem;
  color: var(--muted);
}

.av-01:has(#av-01-w2:checked) {
  --av-01-rw: 2px;
}

.av-01:has(#av-01-w4:checked) {
  --av-01-rw: 4px;
}

.av-01:has(#av-01-dark:checked) {
  --page: #0a0b0e;
  --panel: #14161c;
  --panel-2: #1c1f27;
  --ink: #f2f4f9;
  --muted: #98a0b0;
  --line: #262a33;
  --accent: #8b8cf9;
  --glass: rgba(255,255,255,.07);
  --halo: rgba(139,140,249,.3);
  --shadow: 0 1px 2px rgba(0,0,0,.6), 0 20px 44px -24px rgba(0,0,0,.85);
}

.av-01:has(#av-01-dark:checked) .av-01__i--moon {
  display: none;
}

.av-01:has(#av-01-dark:checked) .av-01__i--sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .av-01:not(:has(#av-01-dark:checked)) {
    --page: #0a0b0e;
    --panel: #14161c;
    --panel-2: #1c1f27;
    --ink: #f2f4f9;
    --muted: #98a0b0;
    --line: #262a33;
    --accent: #8b8cf9;
    --glass: rgba(255,255,255,.07);
    --halo: rgba(139,140,249,.3);
    --shadow: 0 1px 2px rgba(0,0,0,.6), 0 20px 44px -24px rgba(0,0,0,.85);
  }

  .av-01:not(:has(#av-01-dark:checked)) .av-01__i--moon {
    display: none;
  }

  .av-01:not(:has(#av-01-dark:checked)) .av-01__i--sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .av-01 *,
    .av-01 *::before,
    .av-01 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .av-01__fig {
    box-shadow: none !important;
    outline: 3px solid CanvasText;
  }

  .av-01__segbtn input:checked + span {
    background: Highlight;
    color: HighlightText;
  }

  .av-01__row,
    .av-01__seg,
    .av-01__theme {
    border-color: CanvasText;
  }
}
```
