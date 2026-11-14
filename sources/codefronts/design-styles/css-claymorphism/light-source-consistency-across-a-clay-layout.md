---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-claymorphism/light-source-consistency-across-a-clay-layout/"
title: "Light Source Consistency Across a Clay Layout"
section: "design-styles"
category: "css-claymorphism"
category_name: "CSS Claymorphism"
description: "A whole dashboard lit by one variable."
has_js: "false"
---

Here's a working CSS Claymorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Light Source Consistency Across a Clay Layout
Source: https://codefronts.com/design-styles/css-claymorphism/light-source-consistency-across-a-clay-layout/

A whole dashboard lit by one variable. Pick a light direction and every card, button, avatar and toggle re-lights together — highlights, inset walls and drop shadows all rotate in lockstep, because each shadow is expressed as a function of two shared offsets instead of hand-tuned per component. This is the discipline that separates a clay design system from a pile of pretty box-shadows.
## HTML
```html
<section class="cl-06" aria-label="Light source consistency across a clay layout demo">
  <div class="cl-06__stage">
    <div class="cl-06__panel">
      <header class="cl-06__head">
        <div>
          <h2 class="cl-06__h">One light, whole layout</h2>
          <p class="cl-06__lede">Every shadow below is derived from two inherited numbers. Move the light and the entire dashboard re-lights.</p>
        </div>
        <fieldset class="cl-06__dirs">
          <legend class="cl-06__legend">Light</legend>
          <input class="cl-06__r" type="radio" name="cl-06-dir" id="cl-06-tl" checked>
          <label class="cl-06__dir" for="cl-06-tl">Top left</label>
          <input class="cl-06__r" type="radio" name="cl-06-dir" id="cl-06-tr">
          <label class="cl-06__dir" for="cl-06-tr">Top right</label>
          <input class="cl-06__r" type="radio" name="cl-06-dir" id="cl-06-bl">
          <label class="cl-06__dir" for="cl-06-bl">Bottom left</label>
          <input class="cl-06__r" type="radio" name="cl-06-dir" id="cl-06-br">
          <label class="cl-06__dir" for="cl-06-br">Bottom right</label>
        </fieldset>
      </header>
      <div class="cl-06__grid">
        <article class="cl-06__clay cl-06__kpi">
          <p class="cl-06__kpiLabel">Active learners</p>
          <p class="cl-06__kpiValue">12,480</p>
          <span class="cl-06__spark" aria-hidden="true"><i style="height:38%"></i><i style="height:62%"></i><i style="height:48%"></i><i style="height:80%"></i><i style="height:66%"></i><i style="height:94%"></i></span>
        </article>
        <article class="cl-06__clay cl-06__kpi">
          <p class="cl-06__kpiLabel">Lesson streak</p>
          <p class="cl-06__kpiValue">18 days</p>
          <span class="cl-06__ring" aria-hidden="true"></span>
        </article>
        <article class="cl-06__clay cl-06__people">
          <p class="cl-06__kpiLabel">Study group</p>
          <ul class="cl-06__avatars">
            <li class="cl-06__av cl-06__av--a" aria-hidden="true"></li>
            <li class="cl-06__av cl-06__av--b" aria-hidden="true"></li>
            <li class="cl-06__av cl-06__av--c" aria-hidden="true"></li>
            <li class="cl-06__av cl-06__av--more">+6</li>
          </ul>
          <button class="cl-06__clay cl-06__btn" type="button">Invite</button>
        </article>
      </div>
    </div>
    <p class="cl-06__chip" aria-hidden="true">--lx / --ly inherited · drop away from light · sheen toward light</p>
  </div>
</section>
```
## CSS
```css
@property --cl-06-lx {
  syntax: '<number>';
  inherits: true;
  initial-value: -1;
}

@property --cl-06-ly {
  syntax: '<number>';
  inherits: true;
  initial-value: -1;
}

.cl-06,
.cl-06 *,
.cl-06 *::before,
.cl-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cl-06 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--cl-06-bg);
  --cl-06-bg: oklch(0.94 0.026 105);
  --cl-06-clay: oklch(0.88 0.07 100);
  --cl-06-accent: oklch(0.8 0.13 145);
  --cl-06-shade: oklch(0.6 0.09 95/.6);
  --cl-06-light: oklch(1 0.02 100/.95);
  --cl-06-ink: oklch(0.3 0.04 100);
  --cl-06-mut: oklch(0.51 0.035 100);
  font-family: system-ui,-apple-system,'Segoe UI',sans-serif;
  color: var(--cl-06-ink);
}

.cl-06__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 20px;
  padding: clamp(20px,5vw,56px);
}

.cl-06__panel {
  width: min(100%,940px);
  display: grid;
  gap: clamp(20px,3vw,30px);
  padding: clamp(22px,3.4vw,38px);
  border-radius: 44px;
  background: color-mix(in oklch,var(--cl-06-bg) 92%,white);
  box-shadow: calc(var(--cl-06-lx) * -18px) calc(var(--cl-06-ly) * -18px) 46px -18px var(--cl-06-shade),inset calc(var(--cl-06-lx) * 16px) calc(var(--cl-06-ly) * 16px) 30px -14px var(--cl-06-light),inset calc(var(--cl-06-lx) * -16px) calc(var(--cl-06-ly) * -16px) 30px -18px var(--cl-06-shade);
  transition: box-shadow .6s cubic-bezier(.4,0,.2,1),--cl-06-lx .6s,--cl-06-ly .6s;
}

.cl-06:has(#cl-06-tl:checked) .cl-06__panel {
  --cl-06-lx: -1;
  --cl-06-ly: -1;
}

.cl-06:has(#cl-06-tr:checked) .cl-06__panel {
  --cl-06-lx: 1;
  --cl-06-ly: -1;
}

.cl-06:has(#cl-06-bl:checked) .cl-06__panel {
  --cl-06-lx: -1;
  --cl-06-ly: 1;
}

.cl-06:has(#cl-06-br:checked) .cl-06__panel {
  --cl-06-lx: 1;
  --cl-06-ly: 1;
}

.cl-06__head {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  align-items: flex-start;
  justify-content: space-between;
}

.cl-06__h {
  font-size: clamp(21px,3vw,29px);
  font-weight: 780;
  letter-spacing: -.02em;
}

.cl-06__lede {
  margin-top: 6px;
  max-width: 44ch;
  font-size: 14.5px;
  line-height: 1.6;
  color: var(--cl-06-mut);
  text-wrap: pretty;
}

.cl-06__dirs {
  border: 0;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
}

.cl-06__legend {
  grid-column: 1/-1;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--cl-06-mut);
  padding-bottom: 6px;
}

.cl-06__r {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.cl-06__dir {
  display: grid;
  place-items: center;
  min-height: 44px;
  padding: 0 14px;
  border-radius: 18px;
  font-size: 12.5px;
  font-weight: 620;
  cursor: pointer;
  color: var(--cl-06-mut);
  background: color-mix(in oklch,var(--cl-06-bg) 88%,white);
  box-shadow: inset calc(var(--cl-06-lx) * 10px) calc(var(--cl-06-ly) * 10px) 16px -10px var(--cl-06-light),inset calc(var(--cl-06-lx) * -10px) calc(var(--cl-06-ly) * -10px) 16px -12px var(--cl-06-shade);
  transition: color .3s,background .3s,box-shadow .5s;
}

.cl-06__dir:hover {
  color: var(--cl-06-ink);
}

.cl-06__r:checked+.cl-06__dir {
  color: var(--cl-06-ink);
  background: var(--cl-06-accent);
}

.cl-06__r:focus-visible+.cl-06__dir {
  outline: 3px solid var(--cl-06-ink);
  outline-offset: 3px;
}

.cl-06__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(212px,1fr));
  gap: clamp(14px,2.4vw,22px);
}

.cl-06__clay {
  border-radius: 32px;
  background: var(--cl-06-clay);
  box-shadow: calc(var(--cl-06-lx) * -12px) calc(var(--cl-06-ly) * -12px) 30px -14px var(--cl-06-shade),inset calc(var(--cl-06-lx) * 14px) calc(var(--cl-06-ly) * 14px) 24px -10px var(--cl-06-light),inset calc(var(--cl-06-lx) * -14px) calc(var(--cl-06-ly) * -14px) 24px -14px var(--cl-06-shade);
  transition: box-shadow .6s cubic-bezier(.4,0,.2,1),translate .35s cubic-bezier(.34,1.3,.5,1);
}

.cl-06__clay:hover {
  translate: calc(var(--cl-06-lx) * 2px) -5px;
}

.cl-06__kpi,
.cl-06__people {
  display: grid;
  gap: 9px;
  align-content: start;
  padding: 22px 24px;
}

.cl-06__kpiLabel {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: color-mix(in oklch,var(--cl-06-ink) 62%,transparent);
}

.cl-06__kpiValue {
  font-size: clamp(24px,3.4vw,30px);
  font-weight: 780;
  letter-spacing: -.03em;
  font-variant-numeric: tabular-nums;
}

.cl-06__spark {
  display: flex;
  align-items: flex-end;
  gap: 6px;
  height: 46px;
  margin-top: 4px;
}

.cl-06__spark i {
  flex: 1;
  border-radius: 8px;
  background: color-mix(in oklch,var(--cl-06-accent) 82%,white);
  box-shadow: inset calc(var(--cl-06-lx) * 6px) calc(var(--cl-06-ly) * 6px) 8px -5px var(--cl-06-light),inset calc(var(--cl-06-lx) * -6px) calc(var(--cl-06-ly) * -6px) 8px -6px var(--cl-06-shade);
  transition: box-shadow .6s;
}

.cl-06__ring {
  width: 58px;
  height: 58px;
  margin-top: 4px;
  border-radius: 50%;
  background: conic-gradient(var(--cl-06-accent) 0 62%,color-mix(in oklch,var(--cl-06-bg) 70%,white) 62% 100%);
  box-shadow: inset calc(var(--cl-06-lx) * 8px) calc(var(--cl-06-ly) * 8px) 12px -6px var(--cl-06-light),0 8px 14px -8px var(--cl-06-shade);
  -webkit-mask: radial-gradient(circle,transparent 56%,black 57%);
  mask: radial-gradient(circle,transparent 56%,black 57%);
}

.cl-06__avatars {
  list-style: none;
  display: flex;
  align-items: center;
  gap: 8px;
  margin-top: 2px;
}

.cl-06__av {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  font-size: 11.5px;
  font-weight: 700;
  box-shadow: inset calc(var(--cl-06-lx) * 8px) calc(var(--cl-06-ly) * 8px) 12px -7px var(--cl-06-light),inset calc(var(--cl-06-lx) * -8px) calc(var(--cl-06-ly) * -8px) 12px -8px var(--cl-06-shade);
  transition: box-shadow .6s;
}

.cl-06__av--a {
  background: oklch(0.82 0.11 25);
}

.cl-06__av--b {
  background: oklch(0.83 0.1 195);
}

.cl-06__av--c {
  background: oklch(0.85 0.11 290);
}

.cl-06__av--more {
  background: color-mix(in oklch,var(--cl-06-bg) 76%,white);
  color: var(--cl-06-mut);
}

.cl-06__btn {
  justify-self: start;
  min-height: 46px;
  margin-top: 8px;
  padding: 0 22px;
  border: 0;
  border-radius: 22px;
  font: inherit;
  font-size: 14px;
  font-weight: 660;
  color: var(--cl-06-ink);
  cursor: pointer;
  background: var(--cl-06-accent);
}

.cl-06__btn:active {
  translate: 0 2px;
}

.cl-06__btn:focus-visible {
  outline: 3px solid var(--cl-06-ink);
  outline-offset: 3px;
}

.cl-06__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--cl-06-mut);
  padding: 9px 16px;
  border-radius: 99px;
  text-align: center;
  background: oklch(1 0 0/.55);
  box-shadow: inset 0 -4px 10px -8px var(--cl-06-shade),inset 0 6px 10px -6px oklch(1 0 0);
}

@media (prefers-reduced-motion: reduce) {
  .cl-06 * {
    transition-duration: .01ms !important;
  }
}
```
