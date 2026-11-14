---
source: "codefronts"
url: "https://codefronts.com/navigation/css-vertical-tabs/pure-css-vertical-tabs-no-javascript/"
title: "Pure CSS Vertical Tabs (No JavaScript)"
section: "navigation"
category: "css-vertical-tabs"
category_name: "CSS Vertical Tabs"
description: "The zero-JavaScript baseline every other pattern in this collection builds on: visually hidden radio inputs, styled labels and the general sibling combinator."
has_js: "false"
---

Here's a working CSS Vertical Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure CSS Vertical Tabs (No JavaScript)
Source: https://codefronts.com/navigation/css-vertical-tabs/pure-css-vertical-tabs-no-javascript/

The zero-JavaScript baseline every other pattern in this collection builds on: visually hidden radio inputs, styled labels and the general sibling combinator. Panels swap instantly with no hydration cost and no flash of unstyled content, and because the active tab is real form state the browser restores it on back-navigation. Ships with the honest accessibility trade-off radio tabs make.
## HTML
```html
<section class="vt-01" aria-label="Pure CSS vertical tabs demo">
  <div class="vt-01__stage">
    <div class="vt-01__head">
      <p class="vt-01__eyebrow">:checked + label · ~ .panels</p>
      <h2 class="vt-01__title">Vertical tabs, zero JavaScript</h2>
    </div>
    <div class="vt-01__card" role="radiogroup" aria-label="Project workspace panels">
      <input class="vt-01__radio" type="radio" name="vt-01" id="vt-01-t1" checked>
      <label class="vt-01__tab" for="vt-01-t1"><span class="vt-01__num">01</span>Overview</label>
      <input class="vt-01__radio" type="radio" name="vt-01" id="vt-01-t2">
      <label class="vt-01__tab" for="vt-01-t2"><span class="vt-01__num">02</span>Activity</label>
      <input class="vt-01__radio" type="radio" name="vt-01" id="vt-01-t3">
      <label class="vt-01__tab" for="vt-01-t3"><span class="vt-01__num">03</span>Members</label>
      <input class="vt-01__radio" type="radio" name="vt-01" id="vt-01-t4">
      <label class="vt-01__tab" for="vt-01-t4"><span class="vt-01__num">04</span>Billing</label>
      <div class="vt-01__panels">
        <article class="vt-01__panel" id="vt-01-p1">
          <h3 class="vt-01__h">Everything in one flat DOM</h3>
          <p class="vt-01__p">Four inputs, four labels, one panel stack — CSS Grid does the two-column layout so the sibling combinators keep working.</p>
          <p class="vt-01__chip">grid-template-columns: 230px 1fr</p>
        </article>
        <article class="vt-01__panel" id="vt-01-p2">
          <h3 class="vt-01__h">State the browser already owns</h3>
          <p class="vt-01__p">The checked radio survives back-navigation and bfcache restores, so users return to the panel they left.</p>
          <p class="vt-01__chip">no hydration · no layout shift</p>
        </article>
        <article class="vt-01__panel" id="vt-01-p3">
          <h3 class="vt-01__h">Keyboard support for free</h3>
          <p class="vt-01__p">A radio group is one tab stop and moves with the arrow keys — the roving tabindex behaviour, natively.</p>
          <p class="vt-01__chip">↑ ↓ ← → move · Tab exits</p>
        </article>
        <article class="vt-01__panel" id="vt-01-p4">
          <h3 class="vt-01__h">Where CSS stops</h3>
          <p class="vt-01__p">No persistence, no lazy loading, no analytics hook. When you need those, graduate to the ARIA pattern in demo 18.</p>
          <p class="vt-01__chip">~1.4 KB of CSS, 0 KB of JS</p>
        </article>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.vt-01 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--vt-01-bg);
  --vt-01-bg: oklch(0.968 0.007 265);
  --vt-01-card: oklch(1 0 0);
  --vt-01-rail: oklch(0.975 0.006 270);
  --vt-01-ink: oklch(0.23 0.02 272);
  --vt-01-mut: oklch(0.55 0.018 272);
  --vt-01-acc: oklch(0.55 0.19 274);
  --vt-01-line: oklch(0.23 0.02 272/.1);
  --vt-01-sel: color-mix(in oklch,var(--vt-01-acc) 10%,transparent);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--vt-01-ink);
}

.vt-01 *,
.vt-01 *::before,
.vt-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.vt-01__stage {
  min-height: 100svh;
  display: grid;
  place-content: center;
  justify-items: center;
  gap: clamp(18px,3vw,30px);
  padding: clamp(20px,5vw,64px);
  background: radial-gradient(90% 60% at 50% 0%,oklch(0.99 0.012 274),transparent);
}

.vt-01__head {
  display: grid;
  justify-items: center;
  gap: 10px;
  text-align: center;
}

.vt-01__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--vt-01-acc);
}

.vt-01__title {
  font-size: clamp(24px,3.6vw,38px);
  line-height: 1.08;
  letter-spacing: -.028em;
  font-weight: 700;
  text-wrap: balance;
}

.vt-01__card {
  width: min(94vw,880px);
  display: grid;
  grid-template-columns: clamp(160px,26%,236px) 1fr;
  grid-template-rows: repeat(4,auto);
  align-content: start;
  background: var(--vt-01-card);
  border: 1px solid var(--vt-01-line);
  border-radius: 18px;
  box-shadow: 0 22px 60px -28px oklch(0.23 0.02 272/.34);
  overflow: hidden;
}

.vt-01__card::before {
  content: "";
  grid-column: 1;
  grid-row: 1/-1;
  background: var(--vt-01-rail);
  border-right: 1px solid var(--vt-01-line);
  align-self: stretch;
}

.vt-01__radio {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.vt-01__tab {
  grid-column: 1;
  position: relative;
  z-index: 1;
  display: flex;
  align-items: center;
  gap: 11px;
  min-height: 52px;
  padding: 0 16px;
  font-size: 14.5px;
  font-weight: 600;
  color: var(--vt-01-mut);
  cursor: pointer;
  transition: color .2s ease,background .2s ease;
}

.vt-01__tab:nth-of-type(1) {
  grid-row: 1;
}

.vt-01__tab:nth-of-type(2) {
  grid-row: 2;
}

.vt-01__tab:nth-of-type(3) {
  grid-row: 3;
}

.vt-01__tab:nth-of-type(4) {
  grid-row: 4;
}

.vt-01__tab::after {
  content: "";
  position: absolute;
  inset: 8px auto 8px 0;
  width: 3px;
  border-radius: 99px;
  background: var(--vt-01-acc);
  transform: scaleY(0);
  transform-origin: center;
  transition: transform .26s cubic-bezier(.32,.72,.3,1);
}

.vt-01__num {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10.5px;
  letter-spacing: .06em;
  color: color-mix(in oklch,currentColor 55%,transparent);
}

.vt-01__tab:hover {
  color: var(--vt-01-ink);
  background: oklch(0.23 0.02 272/.035);
}

.vt-01__radio:checked+.vt-01__tab {
  color: var(--vt-01-acc);
  background: var(--vt-01-sel);
}

.vt-01__radio:checked+.vt-01__tab::after {
  transform: scaleY(1);
}

.vt-01__radio:focus-visible+.vt-01__tab {
  outline: 2px solid var(--vt-01-acc);
  outline-offset: -3px;
  border-radius: 8px;
}

.vt-01__panels {
  grid-column: 2;
  grid-row: 1/-1;
  display: grid;
  align-self: stretch;
}

.vt-01__panel {
  grid-area: 1/1;
  align-content: center;
  display: grid;
  gap: 12px;
  padding: clamp(22px,3.6vw,38px);
  opacity: 0;
  visibility: hidden;
  transform: translateY(7px);
  transition: opacity .3s ease,transform .34s cubic-bezier(.32,.72,.3,1),visibility 0s .34s;
}

.vt-01__radio:nth-of-type(1):checked~.vt-01__panels #vt-01-p1,
.vt-01__radio:nth-of-type(2):checked~.vt-01__panels #vt-01-p2,
.vt-01__radio:nth-of-type(3):checked~.vt-01__panels #vt-01-p3,
.vt-01__radio:nth-of-type(4):checked~.vt-01__panels #vt-01-p4 {
  opacity: 1;
  visibility: visible;
  transform: none;
  transition-delay: 0s,0s,0s;
}

.vt-01__h {
  font-size: clamp(19px,2.4vw,24px);
  line-height: 1.2;
  letter-spacing: -.02em;
  font-weight: 680;
  text-wrap: balance;
}

.vt-01__p {
  max-width: 44ch;
  font-size: 14.8px;
  line-height: 1.62;
  color: var(--vt-01-mut);
  text-wrap: pretty;
}

.vt-01__chip {
  justify-self: start;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--vt-01-mut);
  padding: 7px 13px;
  border: 1px solid var(--vt-01-line);
  border-radius: 99px;
}

@media (max-width: 640px) {
  .vt-01__card {
    grid-template-columns: 1fr;
    grid-template-rows: repeat(4,auto) auto;
  }

  .vt-01__card::before {
    display: none;
  }

  .vt-01__tab {
    grid-column: 1;
    border-bottom: 1px solid var(--vt-01-line);
  }

  .vt-01__panels {
    grid-column: 1;
    grid-row: auto;
    border-top: 1px solid var(--vt-01-line);
  }
}

@media (prefers-reduced-motion: reduce) {
  .vt-01 * {
    transition-duration: .01ms !important;
  }
}
```
