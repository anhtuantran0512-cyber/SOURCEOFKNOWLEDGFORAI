---
source: "codefronts"
url: "https://codefronts.com/snippets/css-tags-chips/removable-pill/"
title: "Deletable Pill Tag with Close Button"
section: "snippets"
category: "css-tags-chips"
category_name: "CSS Tags & Chips"
description: "Pills that actually delete — with zero JavaScript."
has_js: "false"
---

Here's a working CSS Tags & Chip from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Deletable Pill Tag with Close Button
Source: https://codefronts.com/snippets/css-tags-chips/removable-pill/

Pills that actually delete — with zero JavaScript. The × is a real focusable control (a restyled checkbox), so clicking or pressing Space collapses the pill with a width-and-scale exit animation; a CSS counter live-decrements the total; and one <button type="reset"> resurrects everything because the group is a <form>. The anatomy is the part worth stealing: text region and delete control are separate hit targets, exactly like Gmail's recipient chips.
## HTML
```html
<section class="ctc-05" aria-label="Deletable pill tag demo">
  <form class="ctc-05__stage">
    <div class="ctc-05__wrap">
      <header class="ctc-05__head">
        <p class="ctc-05__kicker">Deletable pills · checkbox as close button</p>
        <h1>Delete with ×. Undo with reset.</h1>
      </header>
      <div class="ctc-05__panel">
        <p class="ctc-05__lab">Skills <span class="ctc-05__n" aria-hidden="true"></span></p>
        <div class="ctc-05__row ctc-05__row--skills">
          <span class="ctc-05__pill"><span>Design systems</span><input type="checkbox" aria-label="Remove Design systems"></span>
          <span class="ctc-05__pill"><span>Figma</span><input type="checkbox" aria-label="Remove Figma"></span>
          <span class="ctc-05__pill"><span>CSS architecture</span><input type="checkbox" aria-label="Remove CSS architecture"></span>
          <span class="ctc-05__pill"><span>Motion design</span><input type="checkbox" aria-label="Remove Motion design"></span>
          <span class="ctc-05__pill"><span>Accessibility</span><input type="checkbox" aria-label="Remove Accessibility"></span>
          <span class="ctc-05__pill"><span>Prototyping</span><input type="checkbox" aria-label="Remove Prototyping"></span>
          <span class="ctc-05__pill"><span>User research</span><input type="checkbox" aria-label="Remove User research"></span>
        </div>
      </div>
      <div class="ctc-05__panel">
        <p class="ctc-05__lab">Recipient variant — same anatomy, plus an initial block</p>
        <div class="ctc-05__row">
          <span class="ctc-05__pill ctc-05__pill--who" style="--h:250"><i>JR</i><span>[email protected]</span><input type="checkbox" aria-label="Remove [email protected]"></span>
          <span class="ctc-05__pill ctc-05__pill--who" style="--h:330"><i>MV</i><span>[email protected]</span><input type="checkbox" aria-label="Remove [email protected]"></span>
          <span class="ctc-05__pill ctc-05__pill--who" style="--h:150"><i>PA</i><span>[email protected]</span><input type="checkbox" aria-label="Remove [email protected]"></span>
        </div>
      </div>
      <footer class="ctc-05__foot">
        <button class="ctc-05__reset" type="reset">↺ Restore all</button>
        <p>The × is the checkbox itself — <code>appearance:none</code>, drawn with two bars, focusable, Space-toggleable. Deletion is <code>.pill:has(:checked)</code> collapsing max-width, padding, margin and scale together.</p>
      </footer>
    </div>
  </form>
</section>
```
## CSS
```css
.ctc-05,
.ctc-05 *,
.ctc-05 *::before,
.ctc-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ctc-05 {
  --bg: oklch(0.965 0.008 250);
  --ink: oklch(0.24 0.025 255);
  --mut: oklch(0.5 0.02 255);
  --line: oklch(0.88 0.012 250);
  --acc: oklch(0.55 0.19 262);
  --del: oklch(0.6 0.21 25);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
}

.ctc-05__stage {
  width: 100%;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  display: grid;
  place-items: center;
  padding: clamp(16px,4cqi,48px);
  background: radial-gradient(75cqi 55cqi at 88% -12%,color-mix(in oklch,var(--acc) 13%,transparent),transparent 65%),var(--bg);
  container: ctc05/inline-size;
  border: 0;
}

.ctc-05__wrap {
  width: min(680px,100%);
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.ctc-05__kicker {
  font-size: 11.5px;
  font-weight: 800;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--acc);
}

.ctc-05__head h1 {
  font-size: clamp(24px,3.8cqi,38px);
  font-weight: 800;
  letter-spacing: -.03em;
  margin: 8px 0 6px;
}

.ctc-05__panel {
  background: oklch(0.995 0.002 250);
  border: 1px solid var(--line);
  border-radius: 18px;
  padding: 16px 18px;
}

.ctc-05__lab {
  font-size: 11.5px;
  font-weight: 800;
  letter-spacing: .09em;
  text-transform: uppercase;
  color: var(--mut);
  margin-bottom: 10px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.ctc-05__n {
  display: inline-flex;
  min-height: 22px;
  align-items: center;
  padding: 0 9px;
  border-radius: 99px;
  background: color-mix(in oklch,var(--acc) 13%,transparent);
  color: var(--acc);
  font-size: 11px;
  font-weight: 800;
  font-variant-numeric: tabular-nums;
  letter-spacing: 0;
}

.ctc-05__row {
  display: flex;
  flex-wrap: wrap;
}

.ctc-05__row--skills {
  counter-reset: ctc05n;
}

.ctc-05__row--skills .ctc-05__pill:not(:has(:checked)) {
  counter-increment: ctc05n;
}

.ctc-05__n::after {
  content: counter(ctc05n) " kept";
}

.ctc-05__pill {
  display: inline-flex;
  align-items: center;
  gap: 9px;
  min-height: 44px;
  max-width: 320px;
  padding: 0 9px 0 17px;
  margin: 0 9px 9px 0;
  border-radius: 99px;
  border: 1.5px solid var(--line);
  background: oklch(0.975 0.006 250);
  font-size: 14px;
  font-weight: 650;
  white-space: nowrap;
  overflow: hidden;
  transition: max-width .38s,padding .38s,margin .38s,opacity .3s,scale .3s,border-color .2s,background .2s;
}

.ctc-05__pill:hover {
  border-color: color-mix(in oklch,var(--acc) 40%,var(--line));
  background: oklch(0.99 0.004 250);
}

.ctc-05__pill input {
  appearance: none;
  -webkit-appearance: none;
  position: relative;
  flex: none;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  border: 0;
  background: color-mix(in oklch,var(--ink) 8%,transparent);
  cursor: pointer;
  transition: background .2s,rotate .25s;
  outline-offset: 2px;
}

.ctc-05__pill input::before,
.ctc-05__pill input::after {
  content: "";
  position: absolute;
  left: 50%;
  top: 50%;
  width: 10px;
  height: 1.8px;
  border-radius: 2px;
  background: var(--mut);
  translate: -50% -50%;
  transition: background .2s;
}

.ctc-05__pill input::before {
  rotate: 45deg;
}

.ctc-05__pill input::after {
  rotate: -45deg;
}

.ctc-05__pill input:hover,
.ctc-05__pill input:focus-visible {
  background: color-mix(in oklch,var(--del) 16%,transparent);
  rotate: 90deg;
}

.ctc-05__pill input:hover::before,
.ctc-05__pill input:hover::after,
.ctc-05__pill input:focus-visible::before,
.ctc-05__pill input:focus-visible::after {
  background: var(--del);
}

.ctc-05__pill input:focus-visible {
  outline: 2px solid var(--del);
}

.ctc-05__pill:has(:checked) {
  max-width: 0;
  padding-inline: 0;
  margin: 0;
  opacity: 0;
  scale: .7;
  pointer-events: none;
  border-color: transparent;
}

.ctc-05__pill--who {
  padding-left: 6px;
  gap: 8px;
}

.ctc-05__pill--who i {
  width: 30px;
  height: 30px;
  flex: none;
  border-radius: 50%;
  display: grid;
  place-items: center;
  font-style: normal;
  font-size: 11px;
  font-weight: 800;
  color: oklch(0.99 0 0);
  background: linear-gradient(140deg,oklch(0.68 0.13 var(--h)),oklch(0.5 0.15 calc(var(--h) + 45)));
}

.ctc-05__pill--who span {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 12.5px;
}

.ctc-05__foot {
  display: flex;
  align-items: flex-start;
  gap: 16px;
}

.ctc-05__reset {
  flex: none;
  min-height: 44px;
  padding: 0 18px;
  border-radius: 12px;
  border: 1.5px solid var(--line);
  background: oklch(0.995 0.002 250);
  font: inherit;
  font-size: 13.5px;
  font-weight: 700;
  color: var(--ink);
  cursor: pointer;
  transition: border-color .2s,translate .2s,box-shadow .2s;
}

.ctc-05__reset:hover,
.ctc-05__reset:focus-visible {
  border-color: var(--acc);
  color: var(--acc);
  translate: 0 -1px;
  box-shadow: 0 8px 16px -10px var(--acc);
}

.ctc-05__reset:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.ctc-05__foot p {
  font-size: 12.5px;
  line-height: 1.6;
  color: var(--mut);
}

.ctc-05__foot code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .9em;
  background: oklch(0.92 0.01 250);
  padding: 1px 5px;
  border-radius: 4px;
  color: var(--ink);
}

@container ctc05 (width < 520px) {
  .ctc-05__foot {
    flex-direction: column;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ctc-05 * {
    transition-duration: .01ms !important;
  }
}
```
