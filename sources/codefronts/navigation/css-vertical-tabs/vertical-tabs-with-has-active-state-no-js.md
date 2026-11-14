---
source: "codefronts"
url: "https://codefronts.com/navigation/css-vertical-tabs/vertical-tabs-with-has-active-state-no-js/"
title: "Vertical Tabs with :has() Active State (No JS)"
section: "navigation"
category: "css-vertical-tabs"
category_name: "CSS Vertical Tabs"
description: "What the parent selector actually unlocks: not just a nicer way to write the radio trick, but a component whose whole environment reacts to the selected tab."
has_js: "false"
---

Here's a working CSS Vertical Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Vertical Tabs with :has() Active State (No JS)
Source: https://codefronts.com/navigation/css-vertical-tabs/vertical-tabs-with-has-active-state-no-js/

What the parent selector actually unlocks: not just a nicer way to write the radio trick, but a component whose whole environment reacts to the selected tab. Choosing a tab here re-themes the card, moves a spotlight gradient, restyles the header and swaps the accent — every one of those a rule CSS physically could not write before :has().
## HTML
```html
<section class="vt-13" aria-label="CSS :has() active state vertical tabs demo">
  <div class="vt-13__stage">
    <div class="vt-13__card" role="radiogroup" aria-label="Studio disciplines">
      <header class="vt-13__header">
        <p class="vt-13__eyebrow">:has() · the parent selector</p>
        <h2 class="vt-13__title">The container reacts, not just the panel</h2>
      </header>
      <input class="vt-13__radio" type="radio" name="vt-13" id="vt-13-t1" checked>
      <label class="vt-13__tab" for="vt-13-t1"><i aria-hidden="true"></i>Research</label>
      <input class="vt-13__radio" type="radio" name="vt-13" id="vt-13-t2">
      <label class="vt-13__tab" for="vt-13-t2"><i aria-hidden="true"></i>Interface</label>
      <input class="vt-13__radio" type="radio" name="vt-13" id="vt-13-t3">
      <label class="vt-13__tab" for="vt-13-t3"><i aria-hidden="true"></i>Motion</label>
      <input class="vt-13__radio" type="radio" name="vt-13" id="vt-13-t4">
      <label class="vt-13__tab" for="vt-13-t4"><i aria-hidden="true"></i>Systems</label>
      <div class="vt-13__panels">
        <article class="vt-13__panel" id="vt-13-p1"><h3 class="vt-13__h">State that cascades</h3><p class="vt-13__p">One rule sets <code>--accent</code> on the card. The rail, the glow, the border and this caption all re-theme from it — no per-element selectors.</p><p class="vt-13__chip">.card:has(#t1:checked){--accent:…}</p></article>
        <article class="vt-13__panel" id="vt-13-p2"><h3 class="vt-13__h">DOM order stops mattering</h3><p class="vt-13__p">The sibling trick could only look forward. <code>:has()</code> reads upward, so the rail may sit anywhere in the source and still drive the layout.</p><p class="vt-13__chip">no ~ combinator required</p></article>
        <article class="vt-13__panel" id="vt-13-p3"><h3 class="vt-13__h">Mind the specificity</h3><p class="vt-13__p"><code>:has()</code> inherits the weight of its heaviest argument, so <code>:has(#id:checked)</code> carries ID specificity. Plan for it instead of reaching for <code>!important</code>.</p><p class="vt-13__chip">specificity = heaviest argument</p></article>
        <article class="vt-13__panel" id="vt-13-p4"><h3 class="vt-13__h">Fast enough, scoped</h3><p class="vt-13__p">Bounded subtree matching is cheap. The expensive shape is a deep, unscoped argument evaluated against the document root.</p><p class="vt-13__chip">avoid :has(.a .b .c) at :root</p></article>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.vt-13 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--vt-13-bg);
  --vt-13-bg: oklch(0.17 0.02 270);
  --vt-13-ink: oklch(0.97 0.008 270);
  --vt-13-mut: oklch(0.71 0.017 270);
  --vt-13-line: oklch(1 0 0/.11);
  --vt-13-acc: oklch(0.78 0.15 195);
  --vt-13-spot: 18%;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--vt-13-ink);
}

.vt-13 *,
.vt-13 *::before,
.vt-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.vt-13__stage {
  min-height: 100svh;
  display: grid;
  place-content: center;
  justify-items: center;
  padding: clamp(18px,4vw,60px);
}

.vt-13__card {
  position: relative;
  width: min(96vw,900px);
  display: grid;
  grid-template-columns: minmax(160px,232px) minmax(0,1fr);
  grid-template-rows: auto repeat(4,auto) 1fr;
  background: linear-gradient(180deg,oklch(0.225 0.024 270),oklch(0.2 0.022 270));
  border: 1px solid color-mix(in oklch,var(--vt-13-acc) 26%,var(--vt-13-line));
  border-radius: 22px;
  box-shadow: 0 30px 80px -40px oklch(0 0 0/.9),0 0 60px -30px color-mix(in oklch,var(--vt-13-acc) 60%,transparent);
  overflow: hidden;
  transition: border-color .5s ease,box-shadow .5s ease;
}

.vt-13__card::before {
  content: "";
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: radial-gradient(50% 60% at var(--vt-13-spot) 0%,color-mix(in oklch,var(--vt-13-acc) 26%,transparent),transparent 70%);
  transition: background .55s cubic-bezier(.32,.72,.3,1);
}

.vt-13__card:has(#vt-13-t1:checked) {
  --vt-13-acc: oklch(0.78 0.15 195);
  --vt-13-spot: 14%;
}

.vt-13__card:has(#vt-13-t2:checked) {
  --vt-13-acc: oklch(0.76 0.17 42);
  --vt-13-spot: 36%;
}

.vt-13__card:has(#vt-13-t3:checked) {
  --vt-13-acc: oklch(0.74 0.19 328);
  --vt-13-spot: 58%;
}

.vt-13__card:has(#vt-13-t4:checked) {
  --vt-13-acc: oklch(0.82 0.17 138);
  --vt-13-spot: 80%;
}

.vt-13__header {
  position: relative;
  z-index: 1;
  grid-column: 1/-1;
  display: grid;
  gap: 7px;
  padding: clamp(20px,3vw,30px) clamp(22px,3.4vw,36px);
  border-bottom: 1px solid var(--vt-13-line);
}

.vt-13__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--vt-13-acc);
  transition: color .45s ease;
}

.vt-13__title {
  font-size: clamp(21px,3vw,30px);
  line-height: 1.1;
  letter-spacing: -.03em;
  font-weight: 700;
  text-wrap: balance;
}

.vt-13__radio {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.vt-13__tab {
  position: relative;
  z-index: 1;
  grid-column: 1;
  display: flex;
  align-items: center;
  gap: 11px;
  min-height: 56px;
  padding: 0 18px;
  font-size: 14.6px;
  font-weight: 640;
  color: var(--vt-13-mut);
  cursor: pointer;
  border-right: 1px solid var(--vt-13-line);
  transition: color .24s ease,background .24s ease;
}

.vt-13__tab i {
  inline-size: 8px;
  block-size: 8px;
  flex: none;
  border-radius: 99px;
  background: currentColor;
  opacity: .35;
  transition: opacity .24s ease,box-shadow .3s ease;
}

.vt-13__tab:hover {
  color: var(--vt-13-ink);
  background: oklch(1 0 0/.05);
}

.vt-13__radio:checked+.vt-13__tab {
  color: var(--vt-13-acc);
  background: color-mix(in oklch,var(--vt-13-acc) 12%,transparent);
}

.vt-13__radio:checked+.vt-13__tab i {
  opacity: 1;
  box-shadow: 0 0 0 4px color-mix(in oklch,var(--vt-13-acc) 22%,transparent);
}

.vt-13__radio:focus-visible+.vt-13__tab {
  outline: 2px solid var(--vt-13-acc);
  outline-offset: -3px;
}

.vt-13__panels {
  position: relative;
  z-index: 1;
  grid-column: 2;
  grid-row: 2/-1;
  display: grid;
  min-height: clamp(240px,30vw,282px);
  padding: clamp(22px,3.4vw,40px);
}

.vt-13__panel {
  grid-area: 1/1;
  align-content: center;
  display: grid;
  gap: 12px;
  justify-items: start;
  opacity: 0;
  visibility: hidden;
  transform: translateY(9px);
  transition: opacity .3s ease,transform .36s cubic-bezier(.32,.72,.3,1),visibility 0s .36s;
}

.vt-13__radio:nth-of-type(1):checked~.vt-13__panels #vt-13-p1,
.vt-13__radio:nth-of-type(2):checked~.vt-13__panels #vt-13-p2,
.vt-13__radio:nth-of-type(3):checked~.vt-13__panels #vt-13-p3,
.vt-13__radio:nth-of-type(4):checked~.vt-13__panels #vt-13-p4 {
  opacity: 1;
  visibility: visible;
  transform: none;
  transition-delay: 0s;
}

.vt-13__h {
  font-size: clamp(19px,2.4vw,26px);
  line-height: 1.18;
  letter-spacing: -.024em;
  font-weight: 690;
  text-wrap: balance;
}

.vt-13__p {
  max-width: 46ch;
  font-size: 14.8px;
  line-height: 1.64;
  color: var(--vt-13-mut);
  text-wrap: pretty;
}

.vt-13__p code,
.vt-13__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
}

.vt-13__p code {
  font-size: .85em;
  background: oklch(1 0 0/.09);
  padding: 2px 6px;
  border-radius: 5px;
}

.vt-13__chip {
  font-size: 11px;
  padding: 7px 13px;
  border-radius: 99px;
  color: var(--vt-13-acc);
  background: color-mix(in oklch,var(--vt-13-acc) 11%,transparent);
  border: 1px solid color-mix(in oklch,var(--vt-13-acc) 28%,transparent);
  overflow-wrap: anywhere;
  transition: color .45s ease,background .45s ease,border-color .45s ease;
}

@supports not selector(:has(*)) {
  .vt-13__card::before {
    background: radial-gradient(50% 60% at 18% 0%,color-mix(in oklch,var(--vt-13-acc) 22%,transparent),transparent 70%);
  }
}

@media (max-width: 680px) {
  .vt-13__card {
    grid-template-columns: 1fr;
    grid-template-rows: auto repeat(4,auto) auto;
  }

  .vt-13__tab {
    border-right: 0;
    border-bottom: 1px solid var(--vt-13-line);
  }

  .vt-13__panels {
    grid-column: 1;
    grid-row: auto;
  }
}

@media (prefers-reduced-motion: reduce) {
  .vt-13 * {
    transition-duration: .01ms !important;
  }
}
```
