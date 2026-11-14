---
source: "codefronts"
url: "https://codefronts.com/snippets/css-tags-chips/tag-input/"
title: "Pure CSS Tag Selector Component"
section: "snippets"
category: "css-tags-chips"
category_name: "CSS Tags & Chips"
description: "The onboarding classic — 'pick up to 3 topics' — enforced entirely in CSS."
has_js: "false"
---

Here's a working CSS Tags & Chip from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure CSS Tag Selector Component
Source: https://codefronts.com/snippets/css-tags-chips/tag-input/

The onboarding classic — 'pick up to 3 topics' — enforced entirely in CSS. The 3-of-N gate is a :has() selector chaining three checked sibling inputs (checkboxes flat in the grid, each styled through its adjacent label — because :has() legally cannot nest); the moment it matches, every unchecked chip fades and stops accepting clicks while checked ones stay togglable, the live counter (a CSS counter) turns amber, and the continue button — enabled by the first selection — is a real link the whole time. A selection limit with zero JavaScript, and the trick generalizes to any N.
## HTML
```html
<section class="ctc-18" aria-label="Pure CSS tag selector demo">
  <form class="ctc-18__stage">
    <div class="ctc-18__card">
      <header class="ctc-18__head">
        <p class="ctc-18__kicker">Onboarding · pure CSS pick-3 gate</p>
        <h1>What should we send you?</h1>
        <p class="ctc-18__sub">Pick up to <b>3</b> topics — at the limit, the rest lock until you free a slot.</p>
      </header>
      <div class="ctc-18__meter"><span class="ctc-18__count" aria-hidden="true"></span><span class="ctc-18__hint">selected</span><button class="ctc-18__clear" type="reset">Start over</button></div>
      <div class="ctc-18__grid" role="group" aria-label="Topics, choose up to three">
        <input class="ctc-18__sr" type="checkbox" name="t" id="ctc18-css" value="css"><label class="ctc-18__opt" style="--h:255" for="ctc18-css"><span>Modern CSS</span></label>
        <input class="ctc-18__sr" type="checkbox" name="t" id="ctc18-js" value="js"><label class="ctc-18__opt" style="--h:200" for="ctc18-js"><span>JavaScript</span></label>
        <input class="ctc-18__sr" type="checkbox" name="t" id="ctc18-a11y" value="a11y"><label class="ctc-18__opt" style="--h:150" for="ctc18-a11y"><span>Accessibility</span></label>
        <input class="ctc-18__sr" type="checkbox" name="t" id="ctc18-perf" value="perf"><label class="ctc-18__opt" style="--h:85" for="ctc18-perf"><span>Performance</span></label>
        <input class="ctc-18__sr" type="checkbox" name="t" id="ctc18-design" value="design"><label class="ctc-18__opt" style="--h:40" for="ctc18-design"><span>UI design</span></label>
        <input class="ctc-18__sr" type="checkbox" name="t" id="ctc18-anim" value="anim"><label class="ctc-18__opt" style="--h:320" for="ctc18-anim"><span>Animation</span></label>
        <input class="ctc-18__sr" type="checkbox" name="t" id="ctc18-svg" value="svg"><label class="ctc-18__opt" style="--h:10" for="ctc18-svg"><span>SVG</span></label>
        <input class="ctc-18__sr" type="checkbox" name="t" id="ctc18-tooling" value="tooling"><label class="ctc-18__opt" style="--h:290" for="ctc18-tooling"><span>Tooling</span></label>
        <input class="ctc-18__sr" type="checkbox" name="t" id="ctc18-career" value="career"><label class="ctc-18__opt" style="--h:180" for="ctc18-career"><span>Career</span></label>
      </div>
      <a class="ctc-18__cta" href="#ctc18-next">Continue<i aria-hidden="true">→</i></a>
      <p class="ctc-18__note">The gate: <code>.grid:has(input:checked ~ input:checked ~ input:checked) input:not(:checked) + label</code> — N−1 tildes for a limit of N. Inputs sit flat in the grid (:has() can't nest), and checked chips stay unlockable, so you can always trade.</p>
    </div>
  </form>
</section>
```
## CSS
```css
.ctc-18,
.ctc-18 *,
.ctc-18 *::before,
.ctc-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ctc-18 {
  --bg: oklch(0.23 0.028 300);
  --card: oklch(0.985 0.004 300);
  --ink: oklch(0.25 0.03 300);
  --mut: oklch(0.52 0.02 300);
  --line: oklch(0.9 0.012 300);
  --acc: oklch(0.56 0.19 300);
  --warn: oklch(0.72 0.15 75);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
}

.ctc-18__stage {
  width: 100%;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  display: grid;
  place-items: center;
  padding: clamp(16px,4cqi,48px);
  background: radial-gradient(70cqi 60cqi at 15% -10%,oklch(0.4 0.11 300/.55),transparent 62%),radial-gradient(60cqi 50cqi at 108% 110%,oklch(0.38 0.1 220/.5),transparent 60%),var(--bg);
  container: ctc18/inline-size;
  border: 0;
}

.ctc-18__card {
  width: min(560px,100%);
  background: var(--card);
  border-radius: 22px;
  padding: clamp(20px,4cqi,30px);
  display: flex;
  flex-direction: column;
  gap: 16px;
  box-shadow: 0 30px 80px -30px oklch(0.1 0.03 300/.8),0 0 0 1px oklch(1 0 0/.12);
}

.ctc-18__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.ctc-18__kicker {
  font-size: 11.5px;
  font-weight: 800;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--acc);
}

.ctc-18__head h1 {
  font-size: clamp(23px,3.6cqi,32px);
  font-weight: 800;
  letter-spacing: -.03em;
  margin: 8px 0 6px;
}

.ctc-18__sub {
  font-size: 13.5px;
  line-height: 1.55;
  color: var(--mut);
}

.ctc-18__meter {
  display: flex;
  align-items: center;
  gap: 8px;
}

.ctc-18__count {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 52px;
  min-height: 30px;
  padding: 0 10px;
  border-radius: 99px;
  background: color-mix(in oklch,var(--acc) 13%,transparent);
  color: var(--acc);
  font-size: 12.5px;
  font-weight: 800;
  font-variant-numeric: tabular-nums;
  transition: background .25s,color .25s;
}

.ctc-18__count::after {
  content: counter(ctc18n) " / 3";
}

.ctc-18__hint {
  font-size: 12px;
  color: var(--mut);
}

.ctc-18__clear {
  margin-left: auto;
  min-height: 44px;
  padding: 0 12px;
  border: 0;
  background: none;
  font: inherit;
  font-size: 12.5px;
  font-weight: 700;
  color: var(--mut);
  cursor: pointer;
  text-decoration: underline 1.5px color-mix(in oklch,var(--mut) 40%,transparent);
  text-underline-offset: 3px;
  transition: color .2s;
}

.ctc-18__clear:hover,
.ctc-18__clear:focus-visible {
  color: var(--acc);
}

.ctc-18__clear:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.ctc-18__grid {
  display: flex;
  flex-wrap: wrap;
  gap: 9px;
  counter-reset: ctc18n;
}

.ctc-18__opt {
  --c: oklch(0.58 0.15 var(--h,300));
  position: relative;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  min-height: 44px;
  padding: 0 17px;
  border-radius: 99px;
  border: 1.5px solid var(--line);
  background: oklch(0.975 0.005 300);
  font-size: 13.5px;
  font-weight: 650;
  color: var(--mut);
  cursor: pointer;
  user-select: none;
  transition: border-color .2s,background .25s,color .2s,opacity .3s,filter .3s,translate .2s;
}

.ctc-18__opt::before {
  content: "";
  width: 0;
  height: 8px;
  border-left: 2.5px solid currentColor;
  border-bottom: 2.5px solid currentColor;
  rotate: -45deg;
  translate: 0 -2px;
  scale: 0;
  opacity: 0;
  transition: scale .3s cubic-bezier(.34,1.56,.64,1),opacity .2s,width .25s cubic-bezier(.34,1.56,.64,1);
}

.ctc-18__opt:hover {
  border-color: color-mix(in oklch,var(--c) 50%,var(--line));
  color: var(--ink);
  translate: 0 -1px;
}

.ctc-18__grid input:focus-visible+.ctc-18__opt {
  outline: 2px solid var(--c);
  outline-offset: 2px;
}

.ctc-18__grid input:checked {
  counter-increment: ctc18n;
}

.ctc-18__grid input:checked+.ctc-18__opt {
  background: color-mix(in oklch,var(--c) 14%,oklch(1 0 0));
  border-color: color-mix(in oklch,var(--c) 55%,transparent);
  color: color-mix(in oklch,var(--c) 75%,var(--ink));
}

.ctc-18__grid input:checked+.ctc-18__opt::before {
  width: 13px;
  scale: 1;
  opacity: 1;
}

.ctc-18__grid:has(input:checked ~ input:checked ~ input:checked) input:not(:checked)+.ctc-18__opt {
  opacity: .4;
  pointer-events: none;
  filter: saturate(.2);
}

.ctc-18__card:has(input:checked ~ input:checked ~ input:checked) .ctc-18__count {
  background: color-mix(in oklch,var(--warn) 22%,transparent);
  color: oklch(0.5 0.13 75);
}

.ctc-18__cta {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 9px;
  min-height: 48px;
  border-radius: 14px;
  background: var(--ink);
  color: oklch(0.97 0.005 300);
  font-size: 14.5px;
  font-weight: 800;
  text-decoration: none;
  opacity: .45;
  pointer-events: none;
  translate: 0 0;
  transition: opacity .3s,background .2s,translate .2s,box-shadow .25s;
}

.ctc-18__cta i {
  font-style: normal;
  transition: translate .2s;
}

.ctc-18__card:has(input:checked) .ctc-18__cta {
  opacity: 1;
  pointer-events: auto;
}

.ctc-18__cta:hover,
.ctc-18__cta:focus-visible {
  background: var(--acc);
  translate: 0 -2px;
  box-shadow: 0 12px 26px -12px var(--acc);
}

.ctc-18__cta:hover i,
.ctc-18__cta:focus-visible i {
  translate: 3px 0;
}

.ctc-18__cta:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.ctc-18__note {
  font-size: 12px;
  line-height: 1.6;
  color: var(--mut);
  border-top: 1px dashed var(--line);
  padding-top: 13px;
}

.ctc-18__note code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .85em;
  background: oklch(0.93 0.008 300);
  padding: 1px 5px;
  border-radius: 4px;
  color: var(--ink);
}

@media (prefers-reduced-motion: reduce) {
  .ctc-18 * {
    transition-duration: .01ms !important;
  }
}
```
