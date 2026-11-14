---
source: "codefronts"
url: "https://codefronts.com/snippets/css-ribbons/swallowtail-v-cut-ribbon-banner/"
title: "Swallowtail V-Cut Ribbon Banner"
section: "snippets"
category: "css-ribbons"
category_name: "CSS Ribbons"
description: "The swallowtail — a section header with a V notched into each end, like a pennant."
has_js: "false"
---

Here's a working CSS Ribbon from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Swallowtail V-Cut Ribbon Banner
Source: https://codefronts.com/snippets/css-ribbons/swallowtail-v-cut-ribbon-banner/

The swallowtail — a section header with a V notched into each end, like a pennant. One clip-path polygon cuts both ends, and because every point is written against a single --rib-06-v property, notch depth is one number you can theme, animate, or shrink on mobile. The band genuinely overhangs the sheet and its fold tails attach flush to the outer ends, so it reads as tied around the page — the detail that separates a wrapped ribbon from a coloured rectangle with decorations near it. Flat ink, no gloss: the only shading is a 3px darker edge that the clip follows.
## HTML
```html
<section class="rib-06" aria-label="Full width swallowtail V-cut section ribbon header demo">
  <div class="rib-06__stage">
    <div class="rib-06__sheet">
      <div class="rib-06__ribbonwrap">
        <div class="rib-06__ribbon">
          <p class="rib-06__kicker">Season 07 · ends Thursday 9am</p>
          <h2 class="rib-06__title">End of Season Clearance</h2>
        </div>
        <span class="rib-06__tab rib-06__tab--l" aria-hidden="true"></span>
        <span class="rib-06__tab rib-06__tab--r" aria-hidden="true"></span>
      </div>
      <p class="rib-06__lede">Up to 60% off every outerwear line. Final markdowns land Thursday at 9am — sizes are not restocked once they sell through.</p>
      <div class="rib-06__row">
        <article class="rib-06__tile"><span class="rib-06__pct">−60%</span><span class="rib-06__cat">Parkas &amp; shells</span></article>
        <article class="rib-06__tile"><span class="rib-06__pct">−45%</span><span class="rib-06__cat">Knitwear</span></article>
        <article class="rib-06__tile"><span class="rib-06__pct">−35%</span><span class="rib-06__cat">Footwear</span></article>
      </div>
      <div class="rib-06__mini">
        <span class="rib-06__minirib">Members get first access</span>
      </div>
    </div>
    <p class="rib-06__chip" aria-hidden="true">6-point clip-path polygon · centred 50% apexes · flush fold tails · real overhang</p>
  </div>
</section>
```
## CSS
```css
.rib-06,
.rib-06 *,
.rib-06 *::before,
.rib-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.rib-06 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --rib-06-bg: #eeeae3;
  --rib-06-bg: oklch(0.94 0.01 82);
  --rib-06-sheet: #fffdfa;
  --rib-06-sheet: oklch(0.99 0.005 85);
  --rib-06-ink: #211d19;
  --rib-06-ink: oklch(0.24 0.012 60);
  --rib-06-mut: #6f675e;
  --rib-06-mut: oklch(0.55 0.015 66);
  --rib-06-acc: #b03526;
  --rib-06-acc: oklch(0.51 0.18 29);
  --rib-06-deep: #6d1f14;
  --rib-06-deep: oklch(0.33 0.11 29);
  --rib-06-pad: clamp(20px,4vw,44px);
  --rib-06-v: clamp(16px,3.6vw,38px);
  --rib-06-over: clamp(14px,3vw,32px);
  --rib-06-tab: clamp(14px,2.6vw,24px);
  background: var(--rib-06-bg);
  color: var(--rib-06-ink);
  font-family: system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.rib-06__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(18px,3vw,28px);
  padding: clamp(20px,5vw,56px);
}

.rib-06__sheet {
  position: relative;
  width: min(100%,880px);
  padding: clamp(30px,5vw,54px) var(--rib-06-pad) clamp(28px,5vw,50px);
  border-radius: 6px;
  background: var(--rib-06-sheet);
  border: 1px solid oklch(0.24 0.012 60/.1);
  box-shadow: 0 18px 40px -30px oklch(0.3 0.04 60/.5);
}

.rib-06__ribbonwrap {
  position: relative;
  margin-inline: calc((var(--rib-06-pad) + var(--rib-06-over)) * -1);
  margin-block-end: calc(var(--rib-06-tab) + clamp(22px,4vw,34px));
  filter: drop-shadow(0 5px 10px oklch(0.35 0.12 29/.22));
}

.rib-06__ribbon {
  position: relative;
  display: grid;
  justify-items: center;
  gap: 9px;
  padding: clamp(15px,3vw,24px) calc(var(--rib-06-v) + clamp(22px,5vw,56px));
  background: var(--rib-06-acc);
  background: linear-gradient(180deg,var(--rib-06-acc) 0 calc(100% - 3px),color-mix(in oklch,var(--rib-06-acc) 78%,black) calc(100% - 3px));
  clip-path: polygon(0 0,100% 0,calc(100% - var(--rib-06-v)) 50%,100% 100%,0 100%,var(--rib-06-v) 50%);
}

.rib-06__kicker {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: clamp(9.5px,1.6vw,11px);
  font-weight: 500;
  letter-spacing: .28em;
  text-transform: uppercase;
  color: oklch(0.99 0.008 85/.88);
}

.rib-06__title {
  color: oklch(0.99 0.008 85);
  font-size: clamp(21px,4.6vw,40px);
  font-weight: 600;
  letter-spacing: -.035em;
  line-height: 1;
  text-align: center;
  text-wrap: balance;
}

.rib-06__tab {
  position: absolute;
  inset-block-start: 100%;
  inline-size: var(--rib-06-over);
  block-size: var(--rib-06-tab);
  background: var(--rib-06-deep);
}

.rib-06__tab--l {
  inset-inline-start: 0;
  clip-path: polygon(0 0,100% 0,0 100%);
}

.rib-06__tab--r {
  inset-inline-end: 0;
  clip-path: polygon(0 0,100% 0,100% 100%);
}

.rib-06__lede {
  max-width: 56ch;
  margin-inline: auto;
  text-align: center;
  font-size: clamp(14px,2.3vw,16.5px);
  line-height: 1.6;
  color: var(--rib-06-mut);
  text-wrap: pretty;
}

.rib-06__row {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(140px,1fr));
  gap: clamp(14px,3vw,30px);
  margin-block-start: clamp(24px,4vw,36px);
  border-block-start: 1px solid oklch(0.24 0.012 60/.12);
  padding-block-start: clamp(16px,3vw,24px);
}

.rib-06__tile {
  display: grid;
  gap: 4px;
  justify-items: center;
  text-align: center;
}

.rib-06__pct {
  font-size: clamp(28px,5.6vw,44px);
  font-weight: 600;
  letter-spacing: -.045em;
  line-height: 1;
  color: var(--rib-06-acc);
  font-variant-numeric: tabular-nums;
}

.rib-06__cat {
  font-size: 11px;
  font-weight: 600;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--rib-06-mut);
}

.rib-06__mini {
  display: grid;
  justify-items: center;
  margin-block-start: clamp(24px,4vw,36px);
}

.rib-06__minirib {
  --rib-06-v: 11px;
  padding: 9px calc(var(--rib-06-v) + 22px);
  background: var(--rib-06-ink);
  color: oklch(0.97 0.006 85);
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10.5px;
  font-weight: 500;
  letter-spacing: .2em;
  text-transform: uppercase;
  clip-path: polygon(0 0,100% 0,calc(100% - var(--rib-06-v)) 50%,100% 100%,0 100%,var(--rib-06-v) 50%);
}

.rib-06__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--rib-06-mut);
  padding: 8px 15px;
  border: 1px solid oklch(0.24 0.012 60/.14);
  border-radius: 99px;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .rib-06 * {
    transition-duration: .01ms !important;
    animation: none !important;
  }
}
```
