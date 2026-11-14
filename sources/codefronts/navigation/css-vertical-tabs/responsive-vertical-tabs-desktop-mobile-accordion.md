---
source: "codefronts"
url: "https://codefronts.com/navigation/css-vertical-tabs/responsive-vertical-tabs-desktop-mobile-accordion/"
title: "Responsive Vertical Tabs (Desktop → Mobile Accordion)"
section: "navigation"
category: "css-vertical-tabs"
category_name: "CSS Vertical Tabs"
description: "One component, two layouts: a two-column vertical tab set on desktop that becomes a stacked accordion on narrow screens — where a fixed 240px rail would eat…"
has_js: "false"
---

Here's a working CSS Vertical Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Responsive Vertical Tabs (Desktop → Mobile Accordion)
Source: https://codefronts.com/navigation/css-vertical-tabs/responsive-vertical-tabs-desktop-mobile-accordion/

One component, two layouts: a two-column vertical tab set on desktop that becomes a stacked accordion on narrow screens — where a fixed 240px rail would eat half the viewport. Driven by a container query so it adapts to the space the component actually has, not the space the browser has, which means it works inside a sidebar, a modal or a CMS column with no extra breakpoints.
## HTML
```html
<section class="vt-02" aria-label="Responsive vertical tabs demo">
  <div class="vt-02__stage">
    <div class="vt-02__head">
      <p class="vt-02__eyebrow">@container · order · 0fr → 1fr</p>
      <h2 class="vt-02__title">Tabs wide, accordion narrow</h2>
      <p class="vt-02__sub">Resize the frame — the flip is driven by the component's own width, not the viewport's.</p>
    </div>
    <div class="vt-02__wrap">
      <div class="vt-02__tabs" role="radiogroup" aria-label="Delivery options">
        <input class="vt-02__radio" type="radio" name="vt-02" id="vt-02-t1" checked>
        <label class="vt-02__tab" for="vt-02-t1">Shipping<span class="vt-02__chev" aria-hidden="true"></span></label>
        <div class="vt-02__panel" id="vt-02-p1"><div class="vt-02__inner">
          <h3 class="vt-02__h">Same DOM, two shapes</h3>
          <p class="vt-02__p">No cloned markup and no duplicate ids — the narrow layout just reorders the flat grid so each label sits above its own panel.</p>
        </div></div>
        <input class="vt-02__radio" type="radio" name="vt-02" id="vt-02-t2">
        <label class="vt-02__tab" for="vt-02-t2">Returns<span class="vt-02__chev" aria-hidden="true"></span></label>
        <div class="vt-02__panel" id="vt-02-p2"><div class="vt-02__inner">
          <h3 class="vt-02__h">Container, not viewport</h3>
          <p class="vt-02__p">Drop this in a 380px dashboard column on a 4K display and it still renders the accordion. Media queries can't know that.</p>
        </div></div>
        <input class="vt-02__radio" type="radio" name="vt-02" id="vt-02-t3">
        <label class="vt-02__tab" for="vt-02-t3">Warranty<span class="vt-02__chev" aria-hidden="true"></span></label>
        <div class="vt-02__panel" id="vt-02-p3"><div class="vt-02__inner">
          <h3 class="vt-02__h">Height without measuring</h3>
          <p class="vt-02__p">The open panel animates from <code>grid-template-rows:0fr</code> to <code>1fr</code> — auto-height easing with nothing to measure in JavaScript.</p>
        </div></div>
        <input class="vt-02__radio" type="radio" name="vt-02" id="vt-02-t4">
        <label class="vt-02__tab" for="vt-02-t4">Support<span class="vt-02__chev" aria-hidden="true"></span></label>
        <div class="vt-02__panel" id="vt-02-p4"><div class="vt-02__inner">
          <h3 class="vt-02__h">One breakpoint to tune</h3>
          <p class="vt-02__p">Every responsive behaviour in this component keys off a single <code>max-width</code> value. Change it once.</p>
        </div></div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.vt-02 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--vt-02-bg);
  --vt-02-bg: oklch(0.24 0.026 250);
  --vt-02-card: oklch(0.28 0.03 252);
  --vt-02-ink: oklch(0.97 0.008 250);
  --vt-02-mut: oklch(0.76 0.018 250);
  --vt-02-acc: oklch(0.82 0.16 178);
  --vt-02-line: oklch(1 0 0/.11);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--vt-02-ink);
}

.vt-02 *,
.vt-02 *::before,
.vt-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.vt-02__stage {
  min-height: 100svh;
  display: grid;
  place-content: center;
  justify-items: center;
  gap: clamp(18px,3vw,30px);
  padding: clamp(20px,5vw,64px);
  background: radial-gradient(80% 55% at 50% 0%,oklch(0.32 0.05 200/.55),transparent);
}

.vt-02__head {
  display: grid;
  justify-items: center;
  gap: 10px;
  text-align: center;
  max-width: 52ch;
}

.vt-02__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--vt-02-acc);
}

.vt-02__title {
  font-size: clamp(24px,3.6vw,38px);
  line-height: 1.08;
  letter-spacing: -.028em;
  font-weight: 700;
  text-wrap: balance;
}

.vt-02__sub {
  font-size: 14.5px;
  line-height: 1.6;
  color: var(--vt-02-mut);
  text-wrap: pretty;
}

.vt-02__wrap {
  container-type: inline-size;
  width: min(94vw,860px);
}

.vt-02__tabs {
  display: grid;
  grid-template-columns: clamp(150px,25%,224px) 1fr;
  grid-template-rows: repeat(4,auto);
  align-content: start;
  background: var(--vt-02-card);
  border: 1px solid var(--vt-02-line);
  border-radius: 18px;
  box-shadow: 0 26px 70px -34px oklch(0 0 0/.7);
  overflow: hidden;
}

.vt-02__radio {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.vt-02__tab {
  grid-column: 1;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  min-height: 54px;
  padding: 0 18px;
  font-size: 14.5px;
  font-weight: 600;
  color: var(--vt-02-mut);
  border-right: 1px solid var(--vt-02-line);
  cursor: pointer;
  transition: color .2s ease,background .2s ease;
}

.vt-02__tab:nth-of-type(1) {
  grid-row: 1;
}

.vt-02__tab:nth-of-type(2) {
  grid-row: 2;
}

.vt-02__tab:nth-of-type(3) {
  grid-row: 3;
}

.vt-02__tab:nth-of-type(4) {
  grid-row: 4;
}

.vt-02__chev {
  width: 9px;
  height: 9px;
  border-right: 2px solid currentColor;
  border-bottom: 2px solid currentColor;
  rotate: -45deg;
  opacity: 0;
  transition: rotate .3s ease,opacity .2s ease;
}

.vt-02__tab:hover {
  color: var(--vt-02-ink);
  background: oklch(1 0 0/.05);
}

.vt-02__radio:checked+.vt-02__tab {
  color: var(--vt-02-acc);
  background: color-mix(in oklch,var(--vt-02-acc) 12%,transparent);
  box-shadow: inset 3px 0 0 var(--vt-02-acc);
}

.vt-02__radio:focus-visible+.vt-02__tab {
  outline: 2px solid var(--vt-02-acc);
  outline-offset: -3px;
}

.vt-02__panel {
  grid-column: 2;
  grid-row: 1/-1;
  display: grid;
  grid-template-rows: 1fr;
  align-content: center;
  align-self: stretch;
  opacity: 0;
  visibility: hidden;
  transform: translateY(8px);
  transition: opacity .3s ease,transform .34s cubic-bezier(.32,.72,.3,1),visibility 0s .34s;
}

.vt-02__inner {
  min-height: 0;
  overflow: hidden;
  display: grid;
  gap: 11px;
  padding: clamp(22px,3.4vw,38px);
}

.vt-02__radio:checked+.vt-02__tab+.vt-02__panel {
  opacity: 1;
  visibility: visible;
  transform: none;
  transition-delay: 0s;
}

.vt-02__h {
  font-size: clamp(18px,2.3vw,23px);
  line-height: 1.22;
  letter-spacing: -.02em;
  font-weight: 680;
  text-wrap: balance;
}

.vt-02__p {
  max-width: 46ch;
  font-size: 14.6px;
  line-height: 1.64;
  color: var(--vt-02-mut);
  text-wrap: pretty;
}

.vt-02__p code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .85em;
  background: oklch(1 0 0/.09);
  padding: 2px 6px;
  border-radius: 5px;
}

@container (max-width: 640px) {
  .vt-02__tabs {
    grid-template-columns: 1fr;
    grid-template-rows: none;
    grid-auto-rows: auto;
  }

  .vt-02__tab {
    grid-column: 1;
    grid-row: auto;
    border-right: 0;
    border-bottom: 1px solid var(--vt-02-line);
  }

  .vt-02__tab:nth-of-type(n) {
    grid-row: auto;
  }

  .vt-02__chev {
    opacity: 1;
  }

  .vt-02__radio:checked+.vt-02__tab .vt-02__chev {
    rotate: 45deg;
  }

  .vt-02__panel {
    grid-column: 1;
    grid-row: auto;
    min-height: 0;
    grid-template-rows: 0fr;
    transform: none;
    opacity: 1;
    visibility: visible;
    align-content: start;
    align-self: start;
    transition: grid-template-rows .34s cubic-bezier(.32,.72,.3,1);
  }

  .vt-02__panel .vt-02__inner {
    padding-block: 0;
    transition: padding-block .34s cubic-bezier(.32,.72,.3,1);
  }

  .vt-02__radio:checked+.vt-02__tab+.vt-02__panel {
    grid-template-rows: 1fr;
    border-bottom: 1px solid var(--vt-02-line);
  }

  .vt-02__radio:checked+.vt-02__tab+.vt-02__panel .vt-02__inner {
    padding-block: clamp(22px,3.4vw,38px);
  }
}

@media (prefers-reduced-motion: reduce) {
  .vt-02 * {
    transition-duration: .01ms !important;
  }
}
```
