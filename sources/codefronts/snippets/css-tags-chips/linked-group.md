---
source: "codefronts"
url: "https://codefronts.com/snippets/css-tags-chips/linked-group/"
title: "Connected Radio Button Tag Selector"
section: "snippets"
category: "css-tags-chips"
category_name: "CSS Tags & Chips"
description: "The segmented control — connected single-select tags with a thumb that GLIDES to the checked option instead of teleporting."
has_js: "false"
---

Here's a working CSS Tags & Chip from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Connected Radio Button Tag Selector
Source: https://codefronts.com/snippets/css-tags-chips/linked-group/

The segmented control — connected single-select tags with a thumb that GLIDES to the checked option instead of teleporting. Radios provide the machine (arrow-key navigation between options is native browser behavior, zero code), an equal-column grid provides the geometry, and the thumb is one absolutely-positioned span whose translate is driven by :has() rules mapping checked-index → position. Includes the iOS-style filled thumb, an underline variant, and a billing toggle with a savings badge.
## HTML
```html
<section class="ctc-23" aria-label="Connected radio tag selector demo">
  <div class="ctc-23__stage">
    <div class="ctc-23__wrap">
      <header class="ctc-23__head">
        <p class="ctc-23__kicker">Segmented control · radios do the machine</p>
        <h1>The thumb glides. Arrows work. Free.</h1>
      </header>
      <div class="ctc-23__panel">
        <p class="ctc-23__lab">01 · Filled thumb — Tab in, then use ← → (native radio behavior)</p>
        <fieldset class="ctc-23__seg" style="--n:3">
          <legend class="ctc-23__sr">Delivery speed</legend>
          <span class="ctc-23__thumb" aria-hidden="true"></span>
          <label><input class="ctc-23__sr" type="radio" name="ctc23a" checked><span>Standard</span></label>
          <label><input class="ctc-23__sr" type="radio" name="ctc23a"><span>Express</span></label>
          <label><input class="ctc-23__sr" type="radio" name="ctc23a"><span>Same-day</span></label>
        </fieldset>
      </div>
      <div class="ctc-23__panel">
        <p class="ctc-23__lab">02 · Underline — same machine, tab-style thumb, 4 options</p>
        <fieldset class="ctc-23__seg ctc-23__seg--line" style="--n:4">
          <legend class="ctc-23__sr">Chart range</legend>
          <span class="ctc-23__thumb" aria-hidden="true"></span>
          <label><input class="ctc-23__sr" type="radio" name="ctc23b"><span>1D</span></label>
          <label><input class="ctc-23__sr" type="radio" name="ctc23b" checked><span>1W</span></label>
          <label><input class="ctc-23__sr" type="radio" name="ctc23b"><span>1M</span></label>
          <label><input class="ctc-23__sr" type="radio" name="ctc23b"><span>1Y</span></label>
        </fieldset>
      </div>
      <div class="ctc-23__panel">
        <p class="ctc-23__lab">03 · Billing toggle — the badge rides the label, never the thumb</p>
        <fieldset class="ctc-23__seg ctc-23__seg--big" style="--n:2">
          <legend class="ctc-23__sr">Billing period</legend>
          <span class="ctc-23__thumb" aria-hidden="true"></span>
          <label><input class="ctc-23__sr" type="radio" name="ctc23c"><span>Monthly</span></label>
          <label><input class="ctc-23__sr" type="radio" name="ctc23c" checked><span>Yearly</span><em>−20%</em></label>
        </fieldset>
      </div>
      <p class="ctc-23__note">Never rebuild this from buttons — radios ship arrow-key roving, group semantics and form value for free. The thumb is one span; <code>:has(label:nth-of-type(2) :checked)</code> sets <code>translate:100%</code>.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.ctc-23,
.ctc-23 *,
.ctc-23 *::before,
.ctc-23 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ctc-23 {
  --bg: oklch(0.965 0.008 265);
  --panel: oklch(0.997 0.002 265);
  --ink: oklch(0.25 0.025 265);
  --mut: oklch(0.51 0.02 265);
  --line: oklch(0.885 0.012 265);
  --acc: oklch(0.55 0.18 265);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
}

.ctc-23__stage {
  width: 100%;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  display: grid;
  place-items: center;
  padding: clamp(16px,4cqi,48px);
  background: radial-gradient(70cqi 55cqi at 12% -10%,color-mix(in oklch,var(--acc) 12%,transparent),transparent 62%),var(--bg);
  container: ctc23/inline-size;
}

.ctc-23__wrap {
  width: min(560px,100%);
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.ctc-23__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.ctc-23__kicker {
  font-size: 11.5px;
  font-weight: 800;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--acc);
}

.ctc-23__head h1 {
  font-size: clamp(23px,3.6cqi,36px);
  font-weight: 800;
  letter-spacing: -.03em;
  margin: 8px 0 8px;
}

.ctc-23__panel {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 18px;
  padding: 16px 18px;
}

.ctc-23__lab {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .05em;
  text-transform: uppercase;
  color: var(--mut);
  margin-bottom: 13px;
}

.ctc-23__seg {
  position: relative;
  display: grid;
  grid-template-columns: repeat(var(--n,3),1fr);
  border: 0;
  background: oklch(0.93 0.01 265);
  border-radius: 13px;
  padding: 4px;
  width: fit-content;
  min-width: min(100%,340px);
}

.ctc-23__seg label {
  position: relative;
  z-index: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 7px;
  min-height: 40px;
  padding: 0 18px;
  border-radius: 10px;
  font-size: 13.5px;
  font-weight: 700;
  color: var(--mut);
  cursor: pointer;
  user-select: none;
  white-space: nowrap;
  transition: color .3s;
}

.ctc-23__seg label:has(:checked) {
  color: var(--ink);
}

.ctc-23__seg label:has(:focus-visible) {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
}

.ctc-23__thumb {
  position: absolute;
  z-index: 0;
  top: 4px;
  bottom: 4px;
  left: 4px;
  width: calc((100% - 8px)/var(--n,3));
  border-radius: 10px;
  background: oklch(0.998 0.002 265);
  box-shadow: 0 2px 8px oklch(0.3 0.03 265/.18),0 0 0 1px oklch(0.3 0.03 265/.05);
  transition: translate .35s cubic-bezier(.3,1.25,.4,1);
}

.ctc-23__seg:has(label:nth-of-type(2) :checked) .ctc-23__thumb {
  translate: 100% 0;
}

.ctc-23__seg:has(label:nth-of-type(3) :checked) .ctc-23__thumb {
  translate: 200% 0;
}

.ctc-23__seg:has(label:nth-of-type(4) :checked) .ctc-23__thumb {
  translate: 300% 0;
}

.ctc-23__seg--line {
  background: none;
  padding: 0;
  border-radius: 0;
  border-bottom: 1.5px solid var(--line);
}

.ctc-23__seg--line label {
  border-radius: 8px 8px 0 0;
  min-height: 44px;
}

.ctc-23__seg--line label:has(:checked) {
  color: var(--acc);
}

.ctc-23__seg--line .ctc-23__thumb {
  top: auto;
  bottom: -1.5px;
  left: 0;
  height: 2.5px;
  width: calc(100%/var(--n,3));
  border-radius: 99px;
  background: var(--acc);
  box-shadow: none;
}

.ctc-23__seg--big label {
  min-height: 46px;
  padding: 0 22px;
  font-size: 14px;
}

.ctc-23__seg--big em {
  font-style: normal;
  font-size: 10.5px;
  font-weight: 800;
  letter-spacing: .04em;
  color: oklch(0.52 0.14 150);
  background: color-mix(in oklch,oklch(0.72 0.17 150) 18%,transparent);
  padding: 3px 8px;
  border-radius: 99px;
}

.ctc-23__note {
  font-size: 12.5px;
  line-height: 1.6;
  color: var(--mut);
  border-left: 3px solid var(--acc);
  padding-left: 12px;
}

.ctc-23__note code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .88em;
  background: oklch(0.93 0.008 265);
  padding: 1px 5px;
  border-radius: 4px;
  color: var(--ink);
}

@media (prefers-reduced-motion: reduce) {
  .ctc-23 * {
    transition-duration: .01ms !important;
  }
}
```
