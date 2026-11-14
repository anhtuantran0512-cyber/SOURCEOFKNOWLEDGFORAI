---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-claymorphism/clay-toggle-switch-and-checkbox-set/"
title: "Clay Toggle Switch and Checkbox Set"
section: "design-styles"
category: "css-claymorphism"
category_name: "CSS Claymorphism"
description: "A complete clay form-control set: a switch whose track is an inset well and whose knob is a puffy clay pebble, checkboxes with a drawn-on tick, and a…"
has_js: "false"
---

Here's a working CSS Claymorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Clay Toggle Switch and Checkbox Set
Source: https://codefronts.com/design-styles/css-claymorphism/clay-toggle-switch-and-checkbox-set/

A complete clay form-control set: a switch whose track is an inset well and whose knob is a puffy clay pebble, checkboxes with a drawn-on tick, and a segmented radio group with a sliding clay thumb. All native inputs — real focus rings, real keyboard, real screen-reader state — with no appearance:none hacks beyond the visually-hidden pattern.
## HTML
```html
<section class="cl-10" aria-label="Clay toggle switch and checkbox set demo">
  <div class="cl-10__stage">
    <div class="cl-10__panel">
      <h2 class="cl-10__h">Preferences</h2>
      <ul class="cl-10__list">
        <li class="cl-10__rowItem">
          <span class="cl-10__rowText"><b>Daily practice reminder</b><span>A nudge at 8:00, your time</span></span>
          <input class="cl-10__in" type="checkbox" id="cl-10-sw1" checked>
          <label class="cl-10__switch" for="cl-10-sw1"><span class="cl-10__knob" aria-hidden="true"></span><span class="cl-10__sr">Daily practice reminder</span></label>
        </li>
        <li class="cl-10__rowItem">
          <span class="cl-10__rowText"><b>Sound effects</b><span>Clicks, chimes and streak fanfare</span></span>
          <input class="cl-10__in" type="checkbox" id="cl-10-sw2">
          <label class="cl-10__switch" for="cl-10-sw2"><span class="cl-10__knob" aria-hidden="true"></span><span class="cl-10__sr">Sound effects</span></label>
        </li>
      </ul>
      <fieldset class="cl-10__fs">
        <legend class="cl-10__legend">Weekly digest includes</legend>
        <div class="cl-10__checks">
          <input class="cl-10__in" type="checkbox" id="cl-10-c1" checked>
          <label class="cl-10__check" for="cl-10-c1"><span class="cl-10__box" aria-hidden="true"></span>Progress summary</label>
          <input class="cl-10__in" type="checkbox" id="cl-10-c2" checked>
          <label class="cl-10__check" for="cl-10-c2"><span class="cl-10__box" aria-hidden="true"></span>New lessons</label>
          <input class="cl-10__in" type="checkbox" id="cl-10-c3">
          <label class="cl-10__check" for="cl-10-c3"><span class="cl-10__box" aria-hidden="true"></span>Community picks</label>
        </div>
      </fieldset>
      <fieldset class="cl-10__fs">
        <legend class="cl-10__legend">Difficulty</legend>
        <div class="cl-10__seg">
          <span class="cl-10__thumb" aria-hidden="true"></span>
          <input class="cl-10__in" type="radio" name="cl-10-diff" id="cl-10-d1">
          <label class="cl-10__segOpt" for="cl-10-d1">Gentle</label>
          <input class="cl-10__in" type="radio" name="cl-10-diff" id="cl-10-d2" checked>
          <label class="cl-10__segOpt" for="cl-10-d2">Steady</label>
          <input class="cl-10__in" type="radio" name="cl-10-diff" id="cl-10-d3">
          <label class="cl-10__segOpt" for="cl-10-d3">Intense</label>
        </div>
      </fieldset>
    </div>
    <p class="cl-10__chip" aria-hidden="true">track = well · knob = object · tick = two borders, rotated and sprung · :has() thumb</p>
  </div>
</section>
```
## CSS
```css
.cl-10,
.cl-10 *,
.cl-10 *::before,
.cl-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cl-10 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--cl-10-bg);
  --cl-10-bg: oklch(0.94 0.028 275);
  --cl-10-clay: oklch(0.89 0.05 280);
  --cl-10-accent: oklch(0.78 0.13 290);
  --cl-10-shade: oklch(0.56 0.09 280/.55);
  --cl-10-light: oklch(1 0.012 280/.95);
  --cl-10-ink: oklch(0.29 0.05 280);
  --cl-10-mut: oklch(0.51 0.04 280);
  font-family: system-ui,-apple-system,'Segoe UI',sans-serif;
  color: var(--cl-10-ink);
}

.cl-10__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 20px;
  padding: clamp(20px,5vw,56px);
}

.cl-10__panel {
  width: min(100%,540px);
  display: grid;
  gap: clamp(18px,3vw,26px);
  padding: clamp(22px,3.4vw,34px);
  border-radius: 42px;
  background: color-mix(in oklch,var(--cl-10-bg) 92%,white);
  box-shadow: 0 30px 60px -24px var(--cl-10-shade),inset 0 -16px 28px -16px var(--cl-10-shade),inset 0 18px 28px -12px var(--cl-10-light);
}

.cl-10__h {
  font-size: clamp(21px,3vw,27px);
  font-weight: 780;
  letter-spacing: -.02em;
}

.cl-10__list {
  list-style: none;
  display: grid;
  gap: 12px;
}

.cl-10__rowItem {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 18px;
  padding: 16px 18px;
  border-radius: 26px;
  background: color-mix(in oklch,var(--cl-10-bg) 96%,oklch(0.7 0.05 280));
  box-shadow: inset 0 8px 16px -10px var(--cl-10-shade),inset 0 -6px 12px -10px var(--cl-10-light);
}

.cl-10__rowText {
  display: grid;
  gap: 3px;
}

.cl-10__rowText b {
  font-size: 14.5px;
  font-weight: 660;
}

.cl-10__rowText span {
  font-size: 12.5px;
  color: var(--cl-10-mut);
}

.cl-10__in {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.cl-10__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cl-10__switch {
  position: relative;
  flex: none;
  display: block;
  width: 62px;
  height: 36px;
  border-radius: 99px;
  cursor: pointer;
  background: color-mix(in oklch,var(--cl-10-bg) 90%,oklch(0.62 0.06 280));
  box-shadow: inset 0 9px 16px -6px var(--cl-10-shade),inset 0 -6px 12px -8px var(--cl-10-light);
  transition: background .3s;
}

.cl-10__knob {
  position: absolute;
  top: 4px;
  left: 4px;
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: color-mix(in oklch,var(--cl-10-clay) 60%,white);
  box-shadow: 0 8px 14px -6px var(--cl-10-shade),inset 0 -6px 10px -7px var(--cl-10-shade),inset 0 8px 10px -6px var(--cl-10-light);
  transition: translate .3s cubic-bezier(.34,1.5,.5,1),scale .3s cubic-bezier(.34,1.5,.5,1),background .3s;
}

.cl-10__in:checked+.cl-10__switch {
  background: color-mix(in oklch,var(--cl-10-accent) 62%,white);
}

.cl-10__in:checked+.cl-10__switch .cl-10__knob {
  translate: 26px 0;
  scale: 1.05;
  background: oklch(0.99 0.01 290);
}

.cl-10__in:focus-visible+.cl-10__switch,
.cl-10__in:focus-visible+.cl-10__check .cl-10__box,
.cl-10__in:focus-visible+.cl-10__segOpt {
  outline: 3px solid var(--cl-10-ink);
  outline-offset: 3px;
}

.cl-10__fs {
  border: 0;
  display: grid;
  gap: 12px;
}

.cl-10__legend {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--cl-10-mut);
  padding-bottom: 4px;
}

.cl-10__checks {
  display: grid;
  gap: 10px;
}

.cl-10__check {
  display: flex;
  align-items: center;
  gap: 14px;
  min-height: 48px;
  padding: 0 18px;
  border-radius: 24px;
  font-size: 14.5px;
  font-weight: 600;
  cursor: pointer;
  background: color-mix(in oklch,var(--cl-10-bg) 92%,white);
  box-shadow: 0 12px 20px -16px var(--cl-10-shade),inset 0 -8px 14px -12px var(--cl-10-shade),inset 0 10px 14px -9px var(--cl-10-light);
  transition: translate .25s cubic-bezier(.34,1.4,.5,1),background .25s;
}

.cl-10__check:hover {
  translate: 3px 0;
}

.cl-10__box {
  position: relative;
  flex: none;
  width: 28px;
  height: 28px;
  border-radius: 10px;
  background: color-mix(in oklch,var(--cl-10-bg) 84%,oklch(0.6 0.055 280));
  box-shadow: inset 0 0 0 1px color-mix(in oklch,var(--cl-10-shade) 30%,transparent),inset 0 8px 13px -5px var(--cl-10-shade),inset 0 -5px 10px -7px var(--cl-10-light);
  transition: background .25s,box-shadow .25s;
}

.cl-10__box::after {
  content: '';
  position: absolute;
  left: 50%;
  top: 50%;
  width: 8px;
  height: 14px;
  border-right: 3px solid oklch(0.99 0.01 290);
  border-bottom: 3px solid oklch(0.99 0.01 290);
  border-radius: 1.5px;
  translate: -50% -62%;
  rotate: 45deg;
  scale: 0;
  opacity: 0;
  transition: scale .26s cubic-bezier(.34,1.6,.5,1),opacity .2s;
}

.cl-10__check:hover .cl-10__box::after {
  scale: .7;
  opacity: .3;
}

.cl-10__in:checked+.cl-10__check {
  background: color-mix(in oklch,var(--cl-10-accent) 26%,white);
}

.cl-10__in:checked+.cl-10__check .cl-10__box {
  background: var(--cl-10-accent);
  box-shadow: 0 8px 14px -8px var(--cl-10-shade),inset 0 -6px 10px -8px var(--cl-10-shade),inset 0 8px 10px -6px var(--cl-10-light);
}

.cl-10__in:checked+.cl-10__check .cl-10__box::after {
  scale: 1;
  opacity: 1;
}

.cl-10__seg {
  position: relative;
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 4px;
  padding: 5px;
  border-radius: 26px;
  background: color-mix(in oklch,var(--cl-10-bg) 92%,oklch(0.66 0.05 280));
  box-shadow: inset 0 9px 16px -7px var(--cl-10-shade),inset 0 -6px 12px -9px var(--cl-10-light);
}

.cl-10__thumb {
  position: absolute;
  top: 5px;
  left: 5px;
  width: calc((100% - 18px) / 3);
  height: calc(100% - 10px);
  border-radius: 22px;
  background: var(--cl-10-accent);
  box-shadow: 0 10px 18px -8px var(--cl-10-shade),inset 0 -7px 12px -8px var(--cl-10-shade),inset 0 9px 12px -6px var(--cl-10-light);
  transition: translate .34s cubic-bezier(.34,1.4,.5,1);
}

.cl-10__seg:has(#cl-10-d2:checked) .cl-10__thumb {
  translate: calc(100% + 4px) 0;
}

.cl-10__seg:has(#cl-10-d3:checked) .cl-10__thumb {
  translate: calc(200% + 8px) 0;
}

.cl-10__segOpt {
  position: relative;
  display: grid;
  place-items: center;
  min-height: 46px;
  border-radius: 22px;
  font-size: 14px;
  font-weight: 640;
  color: var(--cl-10-mut);
  cursor: pointer;
  transition: color .3s;
}

.cl-10__in:checked+.cl-10__segOpt {
  color: oklch(0.99 0.01 290);
}

@media (prefers-reduced-motion: reduce) {
  .cl-10 * {
    transition-duration: .01ms !important;
  }
}
```
