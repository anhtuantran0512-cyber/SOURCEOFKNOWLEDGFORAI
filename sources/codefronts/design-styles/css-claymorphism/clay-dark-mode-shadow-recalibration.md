---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-claymorphism/clay-dark-mode-shadow-recalibration/"
title: "Clay Dark Mode Shadow Recalibration"
section: "design-styles"
category: "css-claymorphism"
category_name: "CSS Claymorphism"
description: "Dark mode is where naive clay dies: black shadows on a dark page are invisible, so the object flattens."
has_js: "false"
---

Here's a working CSS Claymorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Clay Dark Mode Shadow Recalibration
Source: https://codefronts.com/design-styles/css-claymorphism/clay-dark-mode-shadow-recalibration/

Dark mode is where naive clay dies: black shadows on a dark page are invisible, so the object flattens. This demo recalibrates all three layers for dark — a near-black drop with higher alpha, a much weaker inset shade, and a top rim highlight that becomes the primary depth cue — and ships both themes from one token block using light-dark(), with a clay switch to compare instantly.
## HTML
```html
<section class="cl-19" aria-label="Clay dark mode shadow recalibration demo">
  <div class="cl-19__stage">
    <header class="cl-19__head">
      <h2 class="cl-19__h">Same object, recalibrated</h2>
      <p class="cl-19__lede">Flip the theme. The drop shadow gets darker and longer, the inset shade halves, and a 1px rim highlight takes over as the edge.</p>
      <div class="cl-19__toggleWrap">
        <input class="cl-19__chk" type="checkbox" id="cl-19-dark">
        <label class="cl-19__toggle" for="cl-19-dark">
          <span class="cl-19__tTrack" aria-hidden="true"><span class="cl-19__tKnob"></span></span>
          Dark mode
        </label>
      </div>
    </header>
    <div class="cl-19__pane">
      <article class="cl-19__card">
        <span class="cl-19__puck" aria-hidden="true"></span>
        <p class="cl-19__kicker">Tier 3 · floating</p>
        <h3 class="cl-19__title">Recalibrated clay</h3>
        <p class="cl-19__body">Fill sits 8% lighter than the page in both themes, so the object stays lifted rather than dissolving into the background.</p>
        <ul class="cl-19__tokens">
          <li><b>drop</b><span class="cl-19__v cl-19__v--drop"></span></li>
          <li><b>inset shade</b><span class="cl-19__v cl-19__v--shade"></span></li>
          <li><b>rim + sheen</b><span class="cl-19__v cl-19__v--light"></span></li>
        </ul>
        <div class="cl-19__btns">
          <button class="cl-19__btn cl-19__btn--go" type="button">Apply theme</button>
          <button class="cl-19__btn" type="button">Copy tokens</button>
        </div>
      </article>
      <aside class="cl-19__rules">
        <h4 class="cl-19__rulesH">Dark-mode rules</h4>
        <ol class="cl-19__list">
          <li><b>Lift the fill</b> — +6 to 10% lightness over the page.</li>
          <li><b>Add a 1px rim</b> — <code>inset 0 1px 0 oklch(1 0 0/.16)</code>.</li>
          <li><b>Halve the inset shade</b> — dark on dark is mud.</li>
          <li><b>Longer, darker drop</b> — near-black at 70%+ alpha.</li>
        </ol>
      </aside>
    </div>
    <p class="cl-19__chip" aria-hidden="true">light-dark() tokens · color-scheme override · highlight-led depth in dark</p>
  </div>
</section>
```
## CSS
```css
.cl-19,
.cl-19 *,
.cl-19 *::before,
.cl-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cl-19 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  color-scheme: light;
  background: var(--cl-19-bg);
  --cl-19-bg: light-dark(oklch(0.94 0.025 285),oklch(0.19 0.02 285));
  --cl-19-clay: light-dark(oklch(0.9 0.05 285),oklch(0.3 0.03 285));
  --cl-19-clay2: light-dark(oklch(0.94 0.03 285),oklch(0.26 0.025 285));
  --cl-19-accent: light-dark(oklch(0.79 0.13 290),oklch(0.62 0.16 290));
  --cl-19-drop: light-dark(oklch(0.55 0.09 285/.5),oklch(0 0 0/.72));
  --cl-19-inShade: light-dark(oklch(0.55 0.09 285/.55),oklch(0 0 0/.5));
  --cl-19-inLight: light-dark(oklch(1 0 0/.9),oklch(1 0 0/.1));
  --cl-19-rim: light-dark(oklch(1 0 0/0),oklch(1 0 0/.16));
  --cl-19-ink: light-dark(oklch(0.27 0.05 285),oklch(0.96 0.01 285));
  --cl-19-mut: light-dark(oklch(0.5 0.04 285),oklch(0.74 0.02 285));
  font-family: system-ui,-apple-system,'Segoe UI',sans-serif;
  color: var(--cl-19-ink);
  transition: background .45s;
}

.cl-19:has(#cl-19-dark:checked) {
  color-scheme: dark;
}

.cl-19__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(20px,3.5vw,32px);
  padding: clamp(20px,5vw,56px);
}

.cl-19__head {
  display: grid;
  gap: 14px;
  justify-items: center;
  text-align: center;
  max-width: 60ch;
}

.cl-19__h {
  font-size: clamp(23px,3.8vw,34px);
  font-weight: 780;
  letter-spacing: -.022em;
  text-wrap: balance;
}

.cl-19__lede {
  font-size: 15px;
  line-height: 1.6;
  color: var(--cl-19-mut);
  text-wrap: pretty;
}

.cl-19__chk {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.cl-19__toggle {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  min-height: 50px;
  padding: 0 22px 0 12px;
  border-radius: 99px;
  font-size: 14px;
  font-weight: 640;
  cursor: pointer;
  background: var(--cl-19-clay2);
  box-shadow: 0 14px 24px -14px var(--cl-19-drop),inset 0 1px 0 0 var(--cl-19-rim),inset 0 -8px 14px -10px var(--cl-19-inShade),inset 0 10px 14px -8px var(--cl-19-inLight);
  transition: background .45s,box-shadow .45s;
}

.cl-19__tTrack {
  position: relative;
  width: 50px;
  height: 28px;
  border-radius: 99px;
  background: color-mix(in oklch,var(--cl-19-bg) 82%,var(--cl-19-mut));
  box-shadow: inset 0 8px 13px -6px var(--cl-19-inShade),inset 0 -5px 10px -8px var(--cl-19-inLight);
}

.cl-19__tKnob {
  position: absolute;
  top: 3px;
  left: 3px;
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: var(--cl-19-clay);
  box-shadow: 0 6px 11px -5px var(--cl-19-drop),inset 0 1px 0 0 var(--cl-19-rim),inset 0 7px 9px -5px var(--cl-19-inLight);
  transition: translate .34s cubic-bezier(.34,1.5,.5,1),background .45s;
}

.cl-19__chk:checked+.cl-19__toggle .cl-19__tKnob {
  translate: 22px 0;
  background: var(--cl-19-accent);
}

.cl-19__chk:focus-visible+.cl-19__toggle {
  outline: 3px solid var(--cl-19-ink);
  outline-offset: 3px;
}

.cl-19__pane {
  display: grid;
  grid-template-columns: 1fr;
  gap: clamp(16px,2.6vw,24px);
  width: min(100%,880px);
  align-items: center;
}

@media (min-width: 820px) {
  .cl-19__pane {
    grid-template-columns: 1.15fr .85fr;
  }
}

.cl-19__card {
  display: grid;
  gap: 11px;
  padding: clamp(24px,3.2vw,34px);
  border-radius: 40px;
  background: var(--cl-19-clay);
  box-shadow: 0 30px 56px -18px var(--cl-19-drop),inset 0 1px 0 0 var(--cl-19-rim),inset 0 -16px 26px -12px var(--cl-19-inShade),inset 0 18px 30px -10px var(--cl-19-inLight);
  transition: background .45s,box-shadow .45s,translate .4s cubic-bezier(.34,1.3,.5,1);
}

.cl-19__card:hover {
  translate: 0 -6px;
}

.cl-19__puck {
  width: 56px;
  height: 56px;
  border-radius: 22px;
  background: var(--cl-19-accent);
  box-shadow: 0 14px 24px -10px var(--cl-19-drop),inset 0 1px 0 0 var(--cl-19-rim),inset 0 -10px 16px -9px var(--cl-19-inShade),inset 0 12px 16px -7px var(--cl-19-inLight);
  transition: background .45s,box-shadow .45s;
}

.cl-19__kicker {
  margin-top: 4px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: var(--cl-19-mut);
}

.cl-19__title {
  font-size: clamp(20px,2.8vw,25px);
  font-weight: 770;
  letter-spacing: -.02em;
}

.cl-19__body {
  font-size: 14px;
  line-height: 1.6;
  color: var(--cl-19-mut);
  text-wrap: pretty;
}

.cl-19__tokens {
  list-style: none;
  display: grid;
  gap: 8px;
  margin: 6px 0 2px;
  padding: 16px 18px;
  border-radius: 24px;
  background: var(--cl-19-clay2);
  box-shadow: inset 0 9px 16px -8px var(--cl-19-inShade),inset 0 -6px 12px -10px var(--cl-19-inLight);
  transition: background .45s,box-shadow .45s;
}

.cl-19__tokens li {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  color: var(--cl-19-mut);
}

.cl-19__v {
  width: 74px;
  height: 16px;
  border-radius: 99px;
}

.cl-19__v--drop {
  background: var(--cl-19-drop);
}

.cl-19__v--shade {
  background: var(--cl-19-inShade);
}

.cl-19__v--light {
  background: var(--cl-19-inLight);
  box-shadow: inset 0 0 0 1px var(--cl-19-mut);
}

.cl-19__btns {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 6px;
}

.cl-19__btn {
  min-height: 50px;
  padding: 0 22px;
  border: 0;
  border-radius: 22px;
  font: inherit;
  font-size: 14px;
  font-weight: 660;
  color: var(--cl-19-ink);
  cursor: pointer;
  background: var(--cl-19-clay2);
  box-shadow: 0 12px 20px -12px var(--cl-19-drop),inset 0 1px 0 0 var(--cl-19-rim),inset 0 -9px 15px -9px var(--cl-19-inShade),inset 0 11px 15px -7px var(--cl-19-inLight);
  transition: translate .18s,scale .18s cubic-bezier(.2,.8,.3,1.4),background .45s,box-shadow .3s;
}

.cl-19__btn--go {
  color: light-dark(oklch(0.24 0.06 290),oklch(0.98 0.01 290));
  background: var(--cl-19-accent);
}

.cl-19__btn:hover {
  translate: 0 -3px;
}

.cl-19__btn:active {
  scale: 1 .94;
  translate: 0 3px;
  box-shadow: inset 0 12px 18px -8px var(--cl-19-inShade);
}

.cl-19__btn:focus-visible {
  outline: 3px solid var(--cl-19-ink);
  outline-offset: 3px;
}

.cl-19__rules {
  display: grid;
  gap: 10px;
  padding: clamp(22px,3vw,30px);
  border-radius: 36px;
  background: var(--cl-19-clay2);
  box-shadow: 0 22px 42px -20px var(--cl-19-drop),inset 0 1px 0 0 var(--cl-19-rim),inset 0 -14px 24px -14px var(--cl-19-inShade),inset 0 16px 26px -12px var(--cl-19-inLight);
  transition: background .45s,box-shadow .45s;
}

.cl-19__rulesH {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--cl-19-mut);
}

.cl-19__list {
  display: grid;
  gap: 10px;
  padding-left: 20px;
  font-size: 13.5px;
  line-height: 1.5;
}

.cl-19__list li {
  color: var(--cl-19-mut);
}

.cl-19__list b {
  color: var(--cl-19-ink);
}

.cl-19__list code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
}

.cl-19__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--cl-19-mut);
  padding: 9px 16px;
  border-radius: 99px;
  text-align: center;
  background: var(--cl-19-clay2);
  box-shadow: inset 0 1px 0 0 var(--cl-19-rim),inset 0 -4px 10px -8px var(--cl-19-inShade),inset 0 6px 10px -6px var(--cl-19-inLight);
  transition: background .45s;
}

@media (prefers-reduced-motion: reduce) {
  .cl-19 * {
    transition-duration: .01ms !important;
  }
}
```
