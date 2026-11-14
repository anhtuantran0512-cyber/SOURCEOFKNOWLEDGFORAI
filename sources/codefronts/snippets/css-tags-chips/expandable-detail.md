---
source: "codefronts"
url: "https://codefronts.com/snippets/css-tags-chips/expandable-detail/"
title: "Expandable Content Chip on Click"
section: "snippets"
category: "css-tags-chips"
category_name: "CSS Tags & Chips"
description: "Chips that open — sideways into a longer label, or downward into a whole mini-card — using the grid 0fr→1fr trick, the cleanest 'animate to auto' CSS has…"
has_js: "false"
---

Here's a working CSS Tags & Chip from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Expandable Content Chip on Click
Source: https://codefronts.com/snippets/css-tags-chips/expandable-detail/

Chips that open — sideways into a longer label, or downward into a whole mini-card — using the grid 0fr→1fr trick, the cleanest 'animate to auto' CSS has ever had. The hidden content sits in a grid track whose fraction animates from 0fr to 1fr, so it always measures its own natural size; no max-width guesses, no JS measuring, no clipped descenders. Toggle is a real checkbox (Space/Enter work), the chevron rotates on the same state, and one-open-at-a-time works with radios instead.
## HTML
```html
<section class="ctc-22" aria-label="Expandable content chip demo">
  <div class="ctc-22__stage">
    <div class="ctc-22__wrap">
      <header class="ctc-22__head">
        <p class="ctc-22__kicker">Expandable chips · grid 0fr→1fr</p>
        <h1>Animate to auto. Actually.</h1>
      </header>
      <div class="ctc-22__panel">
        <p class="ctc-22__lab">01 · Inline reveal — columns 0fr→1fr, natural width, no max-width hack</p>
        <div class="ctc-22__row">
          <label class="ctc-22__chip" style="--h:255"><input class="ctc-22__sr" type="checkbox"><b>WCAG</b><span class="ctc-22__x"><span>&nbsp;— Web Content Accessibility Guidelines</span></span><i class="ctc-22__chev" aria-hidden="true"></i></label>
          <label class="ctc-22__chip" style="--h:150"><input class="ctc-22__sr" type="checkbox"><b>FLIP</b><span class="ctc-22__x"><span>&nbsp;— First, Last, Invert, Play</span></span><i class="ctc-22__chev" aria-hidden="true"></i></label>
          <label class="ctc-22__chip" style="--h:40"><input class="ctc-22__sr" type="checkbox"><b>LCP</b><span class="ctc-22__x"><span>&nbsp;— Largest Contentful Paint</span></span><i class="ctc-22__chev" aria-hidden="true"></i></label>
        </div>
      </div>
      <div class="ctc-22__panel">
        <p class="ctc-22__lab">02 · Card reveal — rows 0fr→1fr, radios make it an accordion</p>
        <div class="ctc-22__col">
          <label class="ctc-22__card" style="--h:255"><input class="ctc-22__sr" type="radio" name="ctc22acc"><span class="ctc-22__cardhead"><b>Standard shipping</b><em>Free</em><i class="ctc-22__chev" aria-hidden="true"></i></span><span class="ctc-22__body"><span><span class="ctc-22__inner">Arrives in 4–6 business days via ground. Tracked, carbon-neutral, no signature needed.<span class="ctc-22__meta"><span>Tracked</span><span>CO₂ neutral</span></span></span></span></span></label>
          <label class="ctc-22__card" style="--h:150"><input class="ctc-22__sr" type="radio" name="ctc22acc" checked><span class="ctc-22__cardhead"><b>Express</b><em>$9</em><i class="ctc-22__chev" aria-hidden="true"></i></span><span class="ctc-22__body"><span><span class="ctc-22__inner">Next business day for orders before 2pm. Signature on delivery, live courier map.<span class="ctc-22__meta"><span>Next day</span><span>Signature</span><span>Live map</span></span></span></span></span></label>
          <label class="ctc-22__card" style="--h:320"><input class="ctc-22__sr" type="radio" name="ctc22acc"><span class="ctc-22__cardhead"><b>Same-day courier</b><em>$24</em><i class="ctc-22__chev" aria-hidden="true"></i></span><span class="ctc-22__body"><span><span class="ctc-22__inner">Metro areas only, delivered within 4 hours. Your courier's name and photo up front.<span class="ctc-22__meta"><span>4 hours</span><span>Metro only</span></span></span></span></span></label>
        </div>
      </div>
      <p class="ctc-22__note">The one required rule: the track's direct child gets <code>overflow:hidden</code> — a 0fr track doesn't clip by itself. Radios sharing a name turn the column into an accordion with zero script.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.ctc-22,
.ctc-22 *,
.ctc-22 *::before,
.ctc-22 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ctc-22 {
  --bg: oklch(0.97 0.007 145);
  --panel: oklch(0.998 0.002 145);
  --ink: oklch(0.25 0.025 155);
  --mut: oklch(0.5 0.02 155);
  --line: oklch(0.885 0.015 145);
  --acc: oklch(0.55 0.15 155);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
}

.ctc-22__stage {
  width: 100%;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  display: grid;
  place-items: center;
  padding: clamp(16px,4cqi,48px);
  background: radial-gradient(70cqi 55cqi at 88% -10%,color-mix(in oklch,var(--acc) 13%,transparent),transparent 62%),var(--bg);
  container: ctc22/inline-size;
}

.ctc-22__wrap {
  width: min(600px,100%);
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.ctc-22__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.ctc-22__kicker {
  font-size: 11.5px;
  font-weight: 800;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--acc);
}

.ctc-22__head h1 {
  font-size: clamp(24px,3.8cqi,38px);
  font-weight: 800;
  letter-spacing: -.03em;
  margin: 8px 0 8px;
}

.ctc-22__panel {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 18px;
  padding: 16px 18px;
}

.ctc-22__lab {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .05em;
  text-transform: uppercase;
  color: var(--mut);
  margin-bottom: 13px;
}

.ctc-22__row {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.ctc-22__chip {
  --c: oklch(0.58 0.13 var(--h,155));
  display: inline-flex;
  align-items: center;
  min-height: 44px;
  padding: 0 15px;
  border-radius: 99px;
  border: 1.5px solid var(--line);
  background: oklch(0.985 0.004 145);
  font-size: 13.5px;
  cursor: pointer;
  user-select: none;
  transition: border-color .25s,background .25s,box-shadow .25s;
}

.ctc-22__chip:hover {
  border-color: color-mix(in oklch,var(--c) 50%,var(--line));
}

.ctc-22__chip:has(:focus-visible) {
  outline: 2px solid var(--c);
  outline-offset: 2px;
}

.ctc-22__chip b {
  font-weight: 800;
  color: color-mix(in oklch,var(--c) 75%,var(--ink));
}

.ctc-22__chip:has(:checked) {
  border-color: color-mix(in oklch,var(--c) 55%,transparent);
  background: color-mix(in oklch,var(--c) 9%,oklch(1 0 0));
  box-shadow: 0 6px 16px -10px var(--c);
}

.ctc-22__x {
  display: inline-grid;
  grid-template-columns: 0fr;
  transition: grid-template-columns .45s cubic-bezier(.2,.8,.2,1);
}

.ctc-22__x>span {
  overflow: hidden;
  white-space: nowrap;
  color: var(--mut);
}

.ctc-22__chip:has(:checked) .ctc-22__x {
  grid-template-columns: 1fr;
}

.ctc-22__chev {
  flex: none;
  width: 8px;
  height: 8px;
  margin-left: 9px;
  border-right: 2px solid var(--mut);
  border-bottom: 2px solid var(--mut);
  rotate: -45deg;
  translate: 0 -1px;
  transition: rotate .35s cubic-bezier(.34,1.56,.64,1),translate .35s;
}

.ctc-22__chip:has(:checked) .ctc-22__chev,
.ctc-22__card:has(:checked) .ctc-22__chev {
  rotate: 45deg;
  translate: 0 -3px;
}

.ctc-22__col {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.ctc-22__card {
  --c: oklch(0.58 0.13 var(--h,155));
  display: block;
  border: 1.5px solid var(--line);
  border-radius: 16px;
  background: oklch(0.985 0.004 145);
  cursor: pointer;
  user-select: none;
  transition: border-color .25s,background .25s,box-shadow .25s;
}

.ctc-22__card:hover {
  border-color: color-mix(in oklch,var(--c) 50%,var(--line));
}

.ctc-22__card:has(:focus-visible) {
  outline: 2px solid var(--c);
  outline-offset: 2px;
}

.ctc-22__card:has(:checked) {
  border-color: color-mix(in oklch,var(--c) 55%,transparent);
  background: color-mix(in oklch,var(--c) 7%,oklch(1 0 0));
  box-shadow: 0 10px 24px -14px var(--c);
}

.ctc-22__cardhead {
  display: flex;
  align-items: center;
  gap: 10px;
  min-height: 50px;
  padding: 0 16px;
}

.ctc-22__cardhead b {
  font-size: 14px;
  font-weight: 750;
  flex: 1;
}

.ctc-22__cardhead em {
  font-style: normal;
  font-size: 13px;
  font-weight: 800;
  color: color-mix(in oklch,var(--c) 75%,var(--ink));
  background: color-mix(in oklch,var(--c) 12%,transparent);
  padding: 4px 11px;
  border-radius: 99px;
}

.ctc-22__body {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows .45s cubic-bezier(.2,.8,.2,1);
}

.ctc-22__body>span {
  overflow: hidden;
}

.ctc-22__card:has(:checked) .ctc-22__body {
  grid-template-rows: 1fr;
}

.ctc-22__inner {
  display: block;
  padding: 2px 16px 15px;
  font-size: 12.5px;
  line-height: 1.6;
  color: var(--mut);
}

.ctc-22__meta {
  display: flex;
  flex-wrap: wrap;
  gap: 7px;
  margin-top: 10px;
}

.ctc-22__meta span {
  display: inline-flex;
  align-items: center;
  min-height: 26px;
  padding: 0 11px;
  border-radius: 99px;
  background: color-mix(in oklch,var(--c) 11%,transparent);
  color: color-mix(in oklch,var(--c) 72%,var(--ink));
  font-size: 11px;
  font-weight: 750;
}

.ctc-22__note {
  font-size: 12.5px;
  line-height: 1.6;
  color: var(--mut);
  border-left: 3px solid var(--acc);
  padding-left: 12px;
}

.ctc-22__note code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .9em;
  background: oklch(0.93 0.01 145);
  padding: 1px 5px;
  border-radius: 4px;
  color: var(--ink);
}

@media (prefers-reduced-motion: reduce) {
  .ctc-22 * {
    transition-duration: .01ms !important;
  }
}
```
