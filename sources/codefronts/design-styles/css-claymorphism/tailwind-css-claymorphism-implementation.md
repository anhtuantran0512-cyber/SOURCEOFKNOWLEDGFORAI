---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-claymorphism/tailwind-css-claymorphism-implementation/"
title: "Tailwind CSS Claymorphism Implementation"
section: "design-styles"
category: "css-claymorphism"
category_name: "CSS Claymorphism"
description: "Claymorphism in Tailwind, both ways: the arbitrary-value one-liner you paste into a className today, and the Tailwind v4 @theme token you should ship in a…"
has_js: "false"
---

Here's a working CSS Claymorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind CSS Claymorphism Implementation
Source: https://codefronts.com/design-styles/css-claymorphism/tailwind-css-claymorphism-implementation/

Claymorphism in Tailwind, both ways: the arbitrary-value one-liner you paste into a className today, and the Tailwind v4 @theme token you should ship in a real project. The panel prints the exact utility strings next to live components. The demo renders in plain CSS mirroring Tailwind's compiled output, so it runs in any playground without a build step.
## HTML
```html
<section class="cl-08" aria-label="Tailwind CSS claymorphism implementation demo">
  <div class="cl-08__stage">
    <header class="cl-08__head">
      <h2 class="cl-08__h">Clay, the Tailwind way</h2>
      <p class="cl-08__lede">Live components on the left, the exact utility strings on the right. Copy the arbitrary value for a one-off; register the token for a real app.</p>
    </header>
    <div class="cl-08__cols">
      <div class="cl-08__preview">
        <button class="cl-08__btn" type="button">rounded-clay shadow-clay</button>
        <div class="cl-08__card">
          <p class="cl-08__cardTitle">Card token</p>
          <p class="cl-08__cardBody">One <code>shadow-clay</code> utility, three shadow layers, zero custom CSS at the call site.</p>
          <div class="cl-08__tags"><span>rounded-clay</span><span>shadow-clay</span><span>active:shadow-clay-press</span></div>
        </div>
      </div>
      <div class="cl-08__code">
        <p class="cl-08__codeLabel">v4 · @theme token <b>recommended</b></p>
        <pre><code>@theme {
  --radius-clay: 40px;
  --shadow-clay:
    0 24px 44px -12px var(--sh),
    inset 0 -16px 26px -10px var(--sh),
    inset 0 18px 26px -8px var(--hl);
  --shadow-clay-press:
    inset 0 14px 22px -8px var(--sh);
}</code></pre>
        <p class="cl-08__codeLabel">arbitrary value · one-off</p>
        <pre><code>class="rounded-[40px] bg-rose-200
  shadow-[0_24px_44px_-12px_rgb(190_100_110_/_.55),
  inset_0_-16px_26px_-10px_rgb(190_100_110_/_.55),
  inset_0_18px_26px_-8px_rgb(255_255_255_/_.9)]
  hover:-translate-y-1 active:shadow-[inset_0_14px_22px_-8px_rgb(190_100_110_/_.6)]"</code></pre>
      </div>
    </div>
    <p class="cl-08__chip" aria-hidden="true">underscores for spaces · shadow utilities replace, never merge · register a radius token</p>
  </div>
</section>
```
## CSS
```css
.cl-08,
.cl-08 *,
.cl-08 *::before,
.cl-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cl-08 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--cl-08-bg);
  --cl-08-bg: oklch(0.95 0.02 250);
  --cl-08-clay: oklch(0.85 0.09 355);
  --cl-08-shade: oklch(0.6 0.11 358/.55);
  --cl-08-light: oklch(1 0.01 340/.92);
  --cl-08-ink: oklch(0.3 0.04 300);
  --cl-08-mut: oklch(0.51 0.035 300);
  --cl-08-code: oklch(0.26 0.035 285);
  font-family: system-ui,-apple-system,'Segoe UI',sans-serif;
  color: var(--cl-08-ink);
}

.cl-08__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(22px,4vw,34px);
  padding: clamp(20px,5vw,56px);
}

.cl-08__head {
  text-align: center;
  max-width: 62ch;
  display: grid;
  gap: 9px;
}

.cl-08__h {
  font-size: clamp(24px,3.8vw,34px);
  font-weight: 780;
  letter-spacing: -.02em;
  text-wrap: balance;
}

.cl-08__lede {
  font-size: 15px;
  line-height: 1.6;
  color: var(--cl-08-mut);
  text-wrap: pretty;
}

.cl-08__cols {
  display: grid;
  grid-template-columns: 1fr;
  gap: clamp(18px,3vw,28px);
  width: min(100%,980px);
  align-items: center;
}

@media (min-width: 880px) {
  .cl-08__cols {
    grid-template-columns: minmax(0,.85fr) minmax(0,1.15fr);
  }
}

.cl-08__preview {
  display: grid;
  gap: 20px;
  justify-items: center;
  align-content: center;
}

.cl-08__btn {
  min-height: 56px;
  padding: 0 30px;
  border: 0;
  border-radius: 40px;
  font: inherit;
  font-size: 14.5px;
  font-weight: 680;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  color: var(--cl-08-ink);
  cursor: pointer;
  background: var(--cl-08-clay);
  box-shadow: 0 24px 44px -12px var(--cl-08-shade),inset 0 -16px 26px -10px var(--cl-08-shade),inset 0 18px 26px -8px var(--cl-08-light);
  transition: translate .22s cubic-bezier(.34,1.4,.5,1),box-shadow .22s;
}

.cl-08__btn:hover {
  translate: 0 -4px;
}

.cl-08__btn:active {
  translate: 0 2px;
  box-shadow: inset 0 14px 22px -8px var(--cl-08-shade);
}

.cl-08__btn:focus-visible {
  outline: 3px solid var(--cl-08-ink);
  outline-offset: 4px;
}

.cl-08__card {
  display: grid;
  gap: 10px;
  width: min(100%,340px);
  padding: 26px 28px;
  border-radius: 40px;
  background: color-mix(in oklch,var(--cl-08-clay) 55%,white);
  box-shadow: 0 24px 44px -12px var(--cl-08-shade),inset 0 -16px 26px -10px var(--cl-08-shade),inset 0 18px 26px -8px var(--cl-08-light);
}

.cl-08__cardTitle {
  font-size: 18px;
  font-weight: 740;
  letter-spacing: -.015em;
}

.cl-08__cardBody {
  font-size: 13.5px;
  line-height: 1.6;
  color: color-mix(in oklch,var(--cl-08-ink) 80%,transparent);
}

.cl-08__cardBody code,
.cl-08__tags span {
  font-family: ui-monospace,Menlo,Consolas,monospace;
}

.cl-08__tags {
  display: flex;
  flex-wrap: wrap;
  gap: 7px;
  margin-top: 4px;
}

.cl-08__tags span {
  font-size: 11px;
  padding: 6px 11px;
  border-radius: 99px;
  background: oklch(1 0 0/.62);
  color: var(--cl-08-mut);
  box-shadow: inset 0 -4px 8px -7px var(--cl-08-shade),inset 0 5px 8px -5px oklch(1 0 0);
}

.cl-08__code {
  display: grid;
  gap: 9px;
  padding: clamp(18px,2.6vw,26px);
  border-radius: 36px;
  background: var(--cl-08-code);
  box-shadow: 0 30px 56px -22px oklch(0.3 0.05 290/.6),inset 0 -14px 24px -14px oklch(0 0 0/.6),inset 0 16px 24px -12px oklch(1 0 0/.14);
}

.cl-08__codeLabel {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: oklch(0.76 0.04 290);
}

.cl-08__codeLabel b {
  font-size: 9.5px;
  letter-spacing: .1em;
  padding: 4px 8px;
  border-radius: 99px;
  background: oklch(0.8 0.14 150/.22);
  color: oklch(0.86 0.13 155);
}

.cl-08__code pre {
  margin: 0;
  padding: 14px 16px;
  border-radius: 22px;
  background: oklch(0.21 0.03 285);
  overflow-x: auto;
  box-shadow: inset 0 8px 14px -10px oklch(0 0 0/.8);
}

.cl-08__code code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  line-height: 1.75;
  color: oklch(0.92 0.03 200);
  white-space: pre;
}

.cl-08__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--cl-08-mut);
  padding: 9px 16px;
  border-radius: 99px;
  text-align: center;
  background: oklch(1 0 0/.6);
  box-shadow: inset 0 -4px 10px -8px var(--cl-08-shade),inset 0 6px 10px -6px oklch(1 0 0);
}

@media (prefers-reduced-motion: reduce) {
  .cl-08 * {
    transition-duration: .01ms !important;
  }
}
```
