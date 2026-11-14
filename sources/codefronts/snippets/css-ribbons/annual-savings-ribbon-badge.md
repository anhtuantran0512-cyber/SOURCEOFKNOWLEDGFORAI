---
source: "codefronts"
url: "https://codefronts.com/snippets/css-ribbons/annual-savings-ribbon-badge/"
title: "Annual Savings Ribbon Badge"
section: "snippets"
category: "css-ribbons"
category_name: "CSS Ribbons"
description: "A monthly/annual switch where the savings flag is part of the interaction, not a static sticker: choose Annual and the ribbon pops with a spring, the price…"
has_js: "true"
---

Here's a working CSS Ribbon from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Annual Savings Ribbon Badge
Source: https://codefronts.com/snippets/css-ribbons/annual-savings-ribbon-badge/

A monthly/annual switch where the savings flag is part of the interaction, not a static sticker: choose Annual and the ribbon pops with a spring, the price rolls over, and the flag's little pointer stays anchored to the tab it belongs to. Built from two radio inputs and :has() — the entire state machine is the checked radio, so it works with no JavaScript at all and is keyboard-navigable by default.
## HTML
```html
<section class="rib-09" aria-label="Annual savings ribbon on billing toggle demo">
  <div class="rib-09__stage">
    <div class="rib-09__pricing">
      <header class="rib-09__head">
        <h2 class="rib-09__title">Simple, honest pricing</h2>
        <p class="rib-09__sub">Every plan includes unlimited seats for 14 days.</p>
      </header>
      <div class="rib-09__switchwrap">
        <span class="rib-09__flag" aria-hidden="true">Save 20%</span>
        <div class="rib-09__switch" role="radiogroup" aria-label="Billing period">
          <span class="rib-09__thumb" aria-hidden="true"></span>
          <label class="rib-09__opt"><input class="rib-09__radio" type="radio" name="rib-09-cycle" id="rib-09-monthly" checked><span>Monthly</span></label>
          <label class="rib-09__opt"><input class="rib-09__radio" type="radio" name="rib-09-cycle" id="rib-09-annual"><span>Annual</span></label>
        </div>
      </div>
      <div class="rib-09__card">
        <p class="rib-09__plan">Team</p>
        <p class="rib-09__amount"><span class="rib-09__cur">$</span><span class="rib-09__m">24</span><span class="rib-09__y">19</span><span class="rib-09__per">per user / month</span></p>
        <p class="rib-09__note rib-09__note--m">Billed monthly · cancel any time</p>
        <p class="rib-09__note rib-09__note--y">Billed $228 yearly · <s>$288</s> · you keep $60</p>
        <button class="rib-09__cta" type="button">Start 14-day trial</button>
        <p class="rib-09__fine">No card required · SOC 2 Type II</p>
      </div>
      <p class="rib-09__live" role="status">Monthly billing selected.</p>
    </div>
    <p class="rib-09__chip" aria-hidden="true">radiogroup + :has(:checked) · clip-path pointer notch · spring overshoot keyframes</p>
  </div>
</section>
```
## CSS
```css
.rib-09,
.rib-09 *,
.rib-09 *::before,
.rib-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.rib-09 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --rib-09-bg: #0f1117;
  --rib-09-bg: oklch(0.19 0.012 265);
  --rib-09-card: #171a22;
  --rib-09-card: oklch(0.24 0.014 265);
  --rib-09-ink: #f0f2f7;
  --rib-09-ink: oklch(0.96 0.006 265);
  --rib-09-mut: #8d93a3;
  --rib-09-mut: oklch(0.66 0.018 265);
  --rib-09-acc: #3ddc97;
  --rib-09-acc: oklch(0.82 0.16 160);
  background: var(--rib-09-bg);
  color: var(--rib-09-ink);
  font-family: system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.rib-09__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(16px,3vw,26px);
  padding: clamp(20px,5vw,56px);
  background: radial-gradient(80% 60% at 50% 6%,color-mix(in oklch,var(--rib-09-acc) 10%,transparent),transparent 65%);
}

.rib-09__pricing {
  width: min(100%,440px);
  display: grid;
  justify-items: center;
  gap: clamp(18px,3vw,26px);
}

.rib-09__head {
  display: grid;
  gap: 8px;
  text-align: center;
}

.rib-09__title {
  font-size: clamp(25px,5vw,34px);
  font-weight: 660;
  letter-spacing: -.035em;
  text-wrap: balance;
}

.rib-09__sub {
  font-size: 14px;
  color: var(--rib-09-mut);
}

.rib-09__switchwrap {
  position: relative;
  padding-block-start: 44px;
}

.rib-09__flag {
  position: absolute;
  inset-block-end: calc(100% - 40px);
  inset-inline-end: 6px;
  padding: 8px 14px 17px;
  background: #3ddc97;
  background: linear-gradient(180deg,color-mix(in oklch,var(--rib-09-acc) 100%,white 16%),var(--rib-09-acc));
  color: oklch(0.2 0.05 160);
  font-size: 12px;
  font-weight: 800;
  letter-spacing: .04em;
  border-radius: 9px;
  clip-path: polygon(0 0,100% 0,100% 72%,58% 72%,50% 100%,42% 72%,0 72%);
  opacity: .32;
  scale: .7;
  transform-origin: 50% 0;
  transition: opacity .3s,scale .3s;
}

.rib-09__switch {
  position: relative;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4px;
  padding: 5px;
  border-radius: 99px;
  background: oklch(1 0 0/.07);
  border: 1px solid oklch(1 0 0/.1);
}

.rib-09__thumb {
  position: absolute;
  inset-block: 5px;
  inset-inline-start: 5px;
  inline-size: calc(50% - 5px);
  border-radius: 99px;
  background: oklch(1 0 0/.12);
  box-shadow: inset 0 0 0 1px oklch(1 0 0/.16);
  transition: translate .38s cubic-bezier(.16,1,.3,1),background .38s;
}

.rib-09__opt {
  position: relative;
  z-index: 1;
  display: grid;
  place-items: center;
  min-height: 46px;
  padding-inline: clamp(18px,5vw,30px);
  border-radius: 99px;
  cursor: pointer;
  font-size: 14.5px;
  font-weight: 620;
  color: var(--rib-09-mut);
  transition: color .3s;
  user-select: none;
}

.rib-09__radio {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
}

.rib-09__opt:has(:checked) {
  color: var(--rib-09-ink);
}

.rib-09__opt:has(:focus-visible) {
  outline: 3px solid var(--rib-09-acc);
  outline-offset: 2px;
}

.rib-09__switch:has(#rib-09-annual:checked) .rib-09__thumb {
  translate: calc(100% + 4px) 0;
  background: color-mix(in oklch,var(--rib-09-acc) 26%,transparent);
}

.rib-09__pricing:has(#rib-09-annual:checked) .rib-09__flag {
  opacity: 1;
  scale: 1;
  animation: rib-09-pop .5s cubic-bezier(.16,1,.3,1);
}

@keyframes rib-09-pop {
  0% {
    scale: .62;
    rotate: -7deg;
  }

  55% {
    scale: 1.09;
    rotate: 2deg;
  }

  100% {
    scale: 1;
    rotate: 0deg;
  }
}

.rib-09__card {
  width: 100%;
  display: grid;
  gap: 10px;
  padding: clamp(22px,5vw,30px);
  border-radius: 22px;
  background: var(--rib-09-card);
  border: 1px solid oklch(1 0 0/.09);
  box-shadow: 0 30px 64px -32px oklch(0 0 0/.85);
}

.rib-09__plan {
  font-size: 12px;
  font-weight: 750;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--rib-09-acc);
}

.rib-09__amount {
  display: flex;
  align-items: baseline;
  flex-wrap: wrap;
  gap: 2px;
  font-size: clamp(44px,10vw,62px);
  font-weight: 760;
  letter-spacing: -.045em;
  line-height: 1;
  font-variant-numeric: tabular-nums;
}

.rib-09__cur {
  font-size: .42em;
  font-weight: 640;
  color: var(--rib-09-mut);
  margin-inline-end: 2px;
}

.rib-09__per {
  width: 100%;
  font-size: 13px;
  font-weight: 480;
  letter-spacing: 0;
  color: var(--rib-09-mut);
  margin-block-start: 8px;
}

.rib-09__y,
.rib-09__note--y {
  display: none;
}

.rib-09__pricing:has(#rib-09-annual:checked) .rib-09__m,
.rib-09__pricing:has(#rib-09-annual:checked) .rib-09__note--m {
  display: none;
}

.rib-09__pricing:has(#rib-09-annual:checked) .rib-09__y {
  display: inline;
  animation: rib-09-roll .45s cubic-bezier(.16,1,.3,1);
}

.rib-09__pricing:has(#rib-09-annual:checked) .rib-09__note--y {
  display: block;
}

@keyframes rib-09-roll {
  from {
    opacity: 0;
    translate: 0 14px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.rib-09__note {
  font-size: 13px;
  color: var(--rib-09-mut);
}

.rib-09__note s {
  opacity: .7;
}

.rib-09__cta {
  margin-block-start: 8px;
  min-height: 50px;
  border: 0;
  border-radius: 13px;
  background: var(--rib-09-acc);
  color: oklch(0.2 0.05 160);
  font: inherit;
  font-size: 15px;
  font-weight: 700;
  cursor: pointer;
  transition: filter .25s,translate .2s;
}

.rib-09__cta:hover {
  filter: brightness(1.06);
  translate: 0 -1px;
}

.rib-09__cta:focus-visible {
  outline: 3px solid var(--rib-09-ink);
  outline-offset: 3px;
}

.rib-09__fine {
  font-size: 11.5px;
  color: var(--rib-09-mut);
  text-align: center;
}

.rib-09__live {
  font-size: 12.5px;
  color: var(--rib-09-mut);
  min-height: 1.2em;
}

.rib-09__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--rib-09-mut);
  padding: 8px 15px;
  border: 1px solid oklch(1 0 0/.14);
  border-radius: 99px;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .rib-09 * {
    animation: none !important;
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  // The visual state is 100% CSS. This only mirrors the choice into a polite live region,
  // because a screen-reader user should hear the saving, not just see the flag pop.
  document.querySelectorAll('.rib-09__pricing').forEach((root) => {
    if (root.dataset.wired) return;
    root.dataset.wired = '1';
    const live = root.querySelector('.rib-09__live');
    root.querySelectorAll('.rib-09__radio').forEach((radio) => {
      radio.addEventListener('change', () => {
        live.textContent = radio.id.endsWith('annual')
          ? 'Annual billing selected — $19 per user per month, saving $60 a year.'
          : 'Monthly billing selected — $24 per user per month.';
      });
    });
  });
})();
```
