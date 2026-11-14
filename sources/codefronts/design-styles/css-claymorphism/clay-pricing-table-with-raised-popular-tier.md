---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-claymorphism/clay-pricing-table-with-raised-popular-tier/"
title: "Clay Pricing Table with Raised Popular Tier"
section: "design-styles"
category: "css-claymorphism"
category_name: "CSS Claymorphism"
description: "Three plans where hierarchy is built from depth instead of a coloured border: the popular tier sits a full elevation tier above its neighbours, is physically…"
has_js: "false"
---

Here's a working CSS Claymorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Clay Pricing Table with Raised Popular Tier
Source: https://codefronts.com/design-styles/css-claymorphism/clay-pricing-table-with-raised-popular-tier/

Three plans where hierarchy is built from depth instead of a coloured border: the popular tier sits a full elevation tier above its neighbours, is physically larger, and carries a floating clay ribbon. The monthly/yearly switch is pure CSS — a checkbox drives both prices and the saving badge through :has(), so the price actually changes with no script.
## HTML
```html
<section class="cl-15" aria-label="Clay pricing table with raised popular tier demo">
  <div class="cl-15__stage">
    <header class="cl-15__head">
      <h2 class="cl-15__h">Plans that feel their weight</h2>
      <div class="cl-15__billing">
        <input class="cl-15__chk" type="checkbox" id="cl-15-billing">
        <label class="cl-15__switch" for="cl-15-billing">
          <span class="cl-15__opt">Monthly</span>
          <span class="cl-15__track" aria-hidden="true"><span class="cl-15__knob"></span></span>
          <span class="cl-15__opt">Yearly <b class="cl-15__save">save 20%</b></span>
        </label>
      </div>
    </header>
    <div class="cl-15__plans">
      <article class="cl-15__plan" style="--cl-15-elev:2">
        <p class="cl-15__name">Starter</p>
        <p class="cl-15__price"><span class="cl-15__mo">$0<em>/mo</em></span><span class="cl-15__yr">$0<em>/yr</em></span></p>
        <p class="cl-15__blurb">Every snippet, no account needed.</p>
        <ul class="cl-15__feats"><li>All 20 demos</li><li>Copy any snippet</li><li>Community support</li></ul>
        <button class="cl-15__cta" type="button">Start free</button>
      </article>
      <article class="cl-15__plan cl-15__plan--pop" style="--cl-15-elev:4">
        <span class="cl-15__ribbon">Most popular</span>
        <p class="cl-15__name">Pro</p>
        <p class="cl-15__price"><span class="cl-15__mo">$19<em>/mo</em></span><span class="cl-15__yr">$182<em>/yr</em></span></p>
        <p class="cl-15__blurb">Figma tokens, dark-mode variants and the clay generator.</p>
        <ul class="cl-15__feats"><li>Token &amp; Tailwind presets</li><li>Dark-mode recalibration</li><li>Figma clay library</li><li>Priority answers</li></ul>
        <button class="cl-15__cta cl-15__cta--go" type="button">Get Pro</button>
      </article>
      <article class="cl-15__plan" style="--cl-15-elev:2">
        <p class="cl-15__name">Team</p>
        <p class="cl-15__price"><span class="cl-15__mo">$49<em>/mo</em></span><span class="cl-15__yr">$470<em>/yr</em></span></p>
        <p class="cl-15__blurb">Shared design tokens for the whole product team.</p>
        <ul class="cl-15__feats"><li>10 seats</li><li>Design-system audit</li><li>Onboarding session</li></ul>
        <button class="cl-15__cta" type="button">Talk to us</button>
      </article>
    </div>
    <p class="cl-15__chip" aria-hidden="true">hierarchy from --elev + scale · pure-CSS price swap · tabular numerals</p>
  </div>
</section>
```
## CSS
```css
.cl-15,
.cl-15 *,
.cl-15 *::before,
.cl-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cl-15 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--cl-15-bg);
  --cl-15-bg: oklch(0.94 0.028 250);
  --cl-15-clay: oklch(0.9 0.045 250);
  --cl-15-accent: oklch(0.82 0.13 200);
  --cl-15-shade: oklch(0.53 0.09 250/.5);
  --cl-15-light: oklch(1 0.012 250/.95);
  --cl-15-ink: oklch(0.27 0.05 250);
  --cl-15-mut: oklch(0.5 0.04 250);
  font-family: system-ui,-apple-system,'Segoe UI',sans-serif;
  color: var(--cl-15-ink);
}

.cl-15__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(22px,4vw,36px);
  padding: clamp(20px,5vw,56px);
  background: radial-gradient(85% 55% at 50% 0%,oklch(0.97 0.03 240),transparent 66%);
}

.cl-15__head {
  display: grid;
  gap: 18px;
  justify-items: center;
  text-align: center;
}

.cl-15__h {
  font-size: clamp(24px,4vw,36px);
  font-weight: 780;
  letter-spacing: -.024em;
  text-wrap: balance;
}

.cl-15__chk {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.cl-15__switch {
  display: inline-flex;
  align-items: center;
  gap: 14px;
  min-height: 52px;
  padding: 0 20px;
  border-radius: 99px;
  font-size: 14px;
  font-weight: 640;
  cursor: pointer;
  background: color-mix(in oklch,var(--cl-15-bg) 92%,white);
  box-shadow: 0 14px 24px -16px var(--cl-15-shade),inset 0 -9px 15px -11px var(--cl-15-shade),inset 0 11px 15px -8px var(--cl-15-light);
}

.cl-15__opt {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  color: var(--cl-15-mut);
  transition: color .3s;
}

.cl-15__opt:first-of-type {
  color: var(--cl-15-ink);
}

.cl-15__chk:checked+.cl-15__switch .cl-15__opt:first-of-type {
  color: var(--cl-15-mut);
}

.cl-15__chk:checked+.cl-15__switch .cl-15__opt:last-of-type {
  color: var(--cl-15-ink);
}

.cl-15__track {
  position: relative;
  width: 52px;
  height: 30px;
  border-radius: 99px;
  background: color-mix(in oklch,var(--cl-15-bg) 90%,oklch(0.6 0.05 250));
  box-shadow: inset 0 8px 14px -6px var(--cl-15-shade),inset 0 -5px 10px -8px var(--cl-15-light);
}

.cl-15__knob {
  position: absolute;
  top: 3px;
  left: 3px;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: oklch(0.99 0.01 250);
  box-shadow: 0 7px 12px -5px var(--cl-15-shade),inset 0 -5px 8px -6px var(--cl-15-shade),inset 0 7px 9px -5px var(--cl-15-light);
  transition: translate .32s cubic-bezier(.34,1.5,.5,1);
}

.cl-15__chk:checked+.cl-15__switch .cl-15__knob {
  translate: 22px 0;
  background: var(--cl-15-accent);
}

.cl-15__chk:focus-visible+.cl-15__switch {
  outline: 3px solid var(--cl-15-ink);
  outline-offset: 3px;
}

.cl-15__save {
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
  padding: 5px 9px;
  border-radius: 99px;
  background: color-mix(in oklch,var(--cl-15-accent) 42%,white);
  box-shadow: inset 0 4px 7px -4px oklch(1 0 0);
  opacity: .5;
  transition: opacity .3s,scale .3s cubic-bezier(.34,1.5,.5,1);
}

.cl-15__chk:checked+.cl-15__switch .cl-15__save {
  opacity: 1;
  scale: 1.06;
}

.cl-15__plans {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(250px,1fr));
  gap: clamp(18px,3vw,26px);
  align-items: center;
  width: min(100%,1000px);
}

.cl-15__plan {
  position: relative;
  display: grid;
  gap: 11px;
  align-content: start;
  padding: clamp(24px,3vw,32px);
  border-radius: 38px;
  background: var(--cl-15-clay);
  translate: 0 calc(var(--cl-15-elev) * -1px);
  box-shadow: 0 calc(var(--cl-15-elev) * 9px) calc(var(--cl-15-elev) * 17px) calc(var(--cl-15-elev) * -4px) var(--cl-15-shade),inset 0 calc(var(--cl-15-elev) * -4px) calc(var(--cl-15-elev) * 8px) -8px var(--cl-15-shade),inset 0 calc(var(--cl-15-elev) * 5px) calc(var(--cl-15-elev) * 8px) -6px var(--cl-15-light);
  transition: translate .4s cubic-bezier(.34,1.3,.5,1),box-shadow .4s,scale .4s cubic-bezier(.34,1.3,.5,1);
}

.cl-15__plan--pop {
  z-index: 1;
  scale: 1.04;
  background: color-mix(in oklch,var(--cl-15-clay) 72%,var(--cl-15-accent));
  padding-top: clamp(30px,3.6vw,40px);
}

.cl-15__plan--pop:hover {
  translate: 0 -10px;
}

.cl-15__ribbon {
  position: absolute;
  top: -14px;
  left: 50%;
  translate: -50% 0;
  padding: 8px 16px;
  border-radius: 99px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  white-space: nowrap;
  color: oklch(0.99 0.01 200);
  background: oklch(0.5 0.13 250);
  box-shadow: 0 12px 20px -8px var(--cl-15-shade),inset 0 -5px 9px -6px oklch(0 0 0/.4),inset 0 7px 9px -5px oklch(1 0 0/.45);
}

.cl-15__name {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: color-mix(in oklch,var(--cl-15-ink) 62%,transparent);
}

.cl-15__price {
  font-size: clamp(30px,4.4vw,40px);
  font-weight: 780;
  letter-spacing: -.035em;
  font-variant-numeric: tabular-nums;
  line-height: 1;
}

.cl-15__price em {
  font-size: 15px;
  font-weight: 600;
  font-style: normal;
  letter-spacing: -.01em;
  color: var(--cl-15-mut);
}

.cl-15__yr {
  display: none;
}

.cl-15:has(#cl-15-billing:checked) .cl-15__mo {
  display: none;
}

.cl-15:has(#cl-15-billing:checked) .cl-15__yr {
  display: revert;
}

.cl-15__blurb {
  font-size: 13.5px;
  line-height: 1.55;
  color: color-mix(in oklch,var(--cl-15-ink) 80%,transparent);
  text-wrap: pretty;
}

.cl-15__feats {
  list-style: none;
  display: grid;
  gap: 7px;
  margin: 6px 0 2px;
  padding: 16px 18px;
  border-radius: 24px;
  font-size: 13.5px;
  background: color-mix(in oklch,var(--cl-15-clay) 88%,oklch(0.6 0.05 250));
  box-shadow: inset 0 9px 16px -8px var(--cl-15-shade),inset 0 -6px 12px -10px var(--cl-15-light);
}

.cl-15__feats li {
  display: flex;
  align-items: center;
  gap: 10px;
}

.cl-15__feats li::before {
  content: '';
  flex: none;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: oklch(0.6 0.13 200);
  box-shadow: inset 0 2px 3px -1px oklch(1 0 0/.8);
}

.cl-15__cta {
  min-height: 52px;
  margin-top: 6px;
  padding: 0 22px;
  border: 0;
  border-radius: 24px;
  font: inherit;
  font-size: 14.5px;
  font-weight: 680;
  color: var(--cl-15-ink);
  cursor: pointer;
  background: color-mix(in oklch,var(--cl-15-clay) 62%,white);
  box-shadow: 0 14px 22px -12px var(--cl-15-shade),inset 0 -10px 16px -9px var(--cl-15-shade),inset 0 12px 16px -7px var(--cl-15-light);
  transition: translate .18s,scale .18s cubic-bezier(.2,.8,.3,1.4),box-shadow .18s;
}

.cl-15__cta--go {
  color: oklch(0.24 0.06 220);
  background: var(--cl-15-accent);
}

.cl-15__cta:hover {
  translate: 0 -3px;
}

.cl-15__cta:active {
  scale: 1 .94;
  translate: 0 3px;
  box-shadow: inset 0 12px 18px -8px var(--cl-15-shade);
}

.cl-15__cta:focus-visible {
  outline: 3px solid var(--cl-15-ink);
  outline-offset: 3px;
}

.cl-15__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--cl-15-mut);
  padding: 9px 16px;
  border-radius: 99px;
  text-align: center;
  background: oklch(1 0 0/.55);
  box-shadow: inset 0 -4px 10px -8px var(--cl-15-shade),inset 0 6px 10px -6px oklch(1 0 0);
}

@media (prefers-reduced-motion: reduce) {
  .cl-15 * {
    transition-duration: .01ms !important;
  }
}
```
