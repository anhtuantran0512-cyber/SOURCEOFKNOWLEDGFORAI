---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-claymorphism/clay-icon-tiles-and-app-grid/"
title: "Clay Icon Tiles and App Grid"
section: "design-styles"
category: "css-claymorphism"
category_name: "CSS Claymorphism"
description: "Nine clay app tiles on a squircle grid, each hue generated from a single --h value, with a 3D perspective tilt on hover and a staggered load-in that uses…"
has_js: "false"
---

Here's a working CSS Claymorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Clay Icon Tiles and App Grid
Source: https://codefronts.com/design-styles/css-claymorphism/clay-icon-tiles-and-app-grid/

Nine clay app tiles on a squircle grid, each hue generated from a single --h value, with a 3D perspective tilt on hover and a staggered load-in that uses only animation-delay derived from each tile's index. This is the pattern that sells claymorphism — playful, tactile, and cheap enough to render at 60 fps on a phone.
## HTML
```html
<section class="cl-17" aria-label="Clay icon tiles and app grid demo">
  <div class="cl-17__stage">
    <header class="cl-17__head">
      <h2 class="cl-17__h">Nine tiles, one hue variable</h2>
      <p class="cl-17__lede">Hover to tilt. Fill and both shadow colours are derived from each tile's <code>--h</code>, so nothing needs per-colour tuning.</p>
    </header>
    <ul class="cl-17__grid">
      <li class="cl-17__cell" style="--cl-17-h:28;--cl-17-i:0"><button class="cl-17__tile" type="button"><svg viewBox="0 0 24 24" width="30" height="30" aria-hidden="true"><path d="M4 11.2 12 4l8 7.2V20a1 1 0 0 1-1 1h-4v-6H9v6H5a1 1 0 0 1-1-1z" fill="currentColor"/></svg><span>Home</span></button></li>
      <li class="cl-17__cell" style="--cl-17-h:62;--cl-17-i:1"><button class="cl-17__tile" type="button"><svg viewBox="0 0 24 24" width="30" height="30" aria-hidden="true"><path d="M12 3.5 14.6 9l6 .9-4.3 4.2 1 6-5.3-2.8-5.3 2.8 1-6L3.4 9.9 9.4 9z" fill="currentColor"/></svg><span>Streaks</span></button></li>
      <li class="cl-17__cell" style="--cl-17-h:145;--cl-17-i:2"><button class="cl-17__tile" type="button"><svg viewBox="0 0 24 24" width="30" height="30" aria-hidden="true"><path d="M5 4h9l5 5v11a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1zm8 1.8V10h4.2z" fill="currentColor"/></svg><span>Docs</span></button></li>
      <li class="cl-17__cell" style="--cl-17-h:190;--cl-17-i:3"><button class="cl-17__tile" type="button"><svg viewBox="0 0 24 24" width="30" height="30" aria-hidden="true"><path d="M4 5h16v11H4zm5 13h6v2H9z" fill="currentColor"/></svg><span>Watch</span></button></li>
      <li class="cl-17__cell" style="--cl-17-h:232;--cl-17-i:4"><button class="cl-17__tile" type="button"><svg viewBox="0 0 24 24" width="30" height="30" aria-hidden="true"><path d="M12 3a9 9 0 1 1 0 18 9 9 0 0 1 0-18zm.9 4h-1.8v5.5l4.4 2.6.9-1.5-3.5-2z" fill="currentColor"/></svg><span>Focus</span></button></li>
      <li class="cl-17__cell" style="--cl-17-h:280;--cl-17-i:5"><button class="cl-17__tile" type="button"><svg viewBox="0 0 24 24" width="30" height="30" aria-hidden="true"><path d="M12 20.3 10.6 19C6 14.9 3.5 12.6 3.5 9.6A4.1 4.1 0 0 1 7.6 5.5c1.5 0 2.9.7 3.8 1.9.9-1.2 2.3-1.9 3.8-1.9a4.1 4.1 0 0 1 4.1 4.1c0 3-2.5 5.3-7.1 9.4z" fill="currentColor"/></svg><span>Saved</span></button></li>
      <li class="cl-17__cell" style="--cl-17-h:318;--cl-17-i:6"><button class="cl-17__tile" type="button"><svg viewBox="0 0 24 24" width="30" height="30" aria-hidden="true"><path d="M12 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8zm0 2c-4 0-7 2.2-7 5v1h14v-1c0-2.8-3-5-7-5z" fill="currentColor"/></svg><span>People</span></button></li>
      <li class="cl-17__cell" style="--cl-17-h:352;--cl-17-i:7"><button class="cl-17__tile" type="button"><svg viewBox="0 0 24 24" width="30" height="30" aria-hidden="true"><path d="M11 3h2l.4 2.3 2 .8 1.9-1.3 1.4 1.4-1.3 1.9.8 2L20.7 11v2l-2.3.4-.8 2 1.3 1.9-1.4 1.4-1.9-1.3-2 .8L13 20.7h-2l-.4-2.3-2-.8-1.9 1.3-1.4-1.4 1.3-1.9-.8-2L3.3 13v-2l2.3-.4.8-2L5.1 6.7l1.4-1.4 1.9 1.3 2-.8zM12 9a3 3 0 1 0 0 6 3 3 0 0 0 0-6z" fill="currentColor"/></svg><span>Settings</span></button></li>
      <li class="cl-17__cell" style="--cl-17-h:12;--cl-17-i:8"><button class="cl-17__tile" type="button"><svg viewBox="0 0 24 24" width="30" height="30" aria-hidden="true"><path d="M11 4h2v7h7v2h-7v7h-2v-7H4v-2h7z" fill="currentColor"/></svg><span>Add</span></button></li>
    </ul>
    <p class="cl-17__chip" aria-hidden="true">oklch hue rotation · individual transform properties · animation-delay: calc(--i * 60ms)</p>
  </div>
</section>
```
## CSS
```css
.cl-17,
.cl-17 *,
.cl-17 *::before,
.cl-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cl-17 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--cl-17-bg);
  --cl-17-bg: oklch(0.94 0.02 250);
  --cl-17-ink: oklch(0.27 0.04 250);
  --cl-17-mut: oklch(0.5 0.03 250);
  --cl-17-shade: oklch(0.55 0.06 250/.4);
  font-family: system-ui,-apple-system,'Segoe UI',sans-serif;
  color: var(--cl-17-ink);
}

.cl-17__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(22px,4vw,36px);
  padding: clamp(20px,5vw,56px);
  background: radial-gradient(85% 60% at 50% 0%,oklch(0.98 0.02 250),transparent 70%);
}

.cl-17__head {
  text-align: center;
  max-width: 56ch;
  display: grid;
  gap: 9px;
}

.cl-17__h {
  font-size: clamp(23px,3.8vw,34px);
  font-weight: 780;
  letter-spacing: -.022em;
  text-wrap: balance;
}

.cl-17__lede {
  font-size: 15px;
  line-height: 1.6;
  color: var(--cl-17-mut);
  text-wrap: pretty;
}

.cl-17__lede code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 13.5px;
}

.cl-17__grid {
  list-style: none;
  display: grid;
  grid-template-columns: repeat(3,minmax(88px,132px));
  gap: clamp(14px,2.6vw,24px);
  perspective: 900px;
  padding: 6px;
}

.cl-17__cell {
  display: grid;
}

.cl-17__tile {
  --cl-17-h: 30;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 9px;
  aspect-ratio: 1;
  padding: 10px;
  border: 0;
  border-radius: 34px;
  font: inherit;
  cursor: pointer;
  color: oklch(0.28 0.08 var(--cl-17-h));
  background: oklch(0.85 0.1 var(--cl-17-h));
  transform-style: preserve-3d;
  box-shadow: 0 18px 30px -10px oklch(0.52 0.13 var(--cl-17-h)/.5),inset 0 -13px 20px -9px oklch(0.52 0.13 var(--cl-17-h)/.55),inset 0 15px 20px -7px oklch(1 0.02 var(--cl-17-h)/.95);
  animation: cl-17-pop .55s cubic-bezier(.34,1.5,.5,1) backwards;
  animation-delay: calc(var(--cl-17-i) * 60ms);
  transition: rotate .35s cubic-bezier(.2,.8,.3,1.1),translate .4s cubic-bezier(.34,1.35,.5,1),scale .4s cubic-bezier(.34,1.35,.5,1),box-shadow .4s;
}

@keyframes cl-17-pop {
  from {
    opacity: 0;
    scale: .7;
    translate: 0 16px;
  }

  to {
    opacity: 1;
    scale: 1;
    translate: 0 0;
  }
}

.cl-17__tile:hover {
  rotate: x 13deg;
  translate: 0 -7px;
  scale: 1.05;
  box-shadow: 0 30px 44px -12px oklch(0.52 0.13 var(--cl-17-h)/.55),inset 0 -13px 20px -9px oklch(0.52 0.13 var(--cl-17-h)/.55),inset 0 17px 22px -7px oklch(1 0.02 var(--cl-17-h)/.98);
}

.cl-17__tile:active {
  rotate: x 0deg;
  translate: 0 2px;
  scale: .95;
  box-shadow: inset 0 14px 22px -8px oklch(0.52 0.13 var(--cl-17-h)/.6),inset 0 -10px 18px -10px oklch(1 0.02 var(--cl-17-h)/.8);
}

.cl-17__tile:focus-visible {
  outline: 3px solid oklch(0.32 0.09 var(--cl-17-h));
  outline-offset: 4px;
}

.cl-17__tile span {
  font-size: 12px;
  font-weight: 680;
  letter-spacing: -.005em;
}

@supports (corner-shape: squircle) {
  .cl-17__tile {
    border-radius: 36%;
    corner-shape: squircle;
  }
}

.cl-17__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--cl-17-mut);
  padding: 9px 16px;
  border-radius: 99px;
  text-align: center;
  background: oklch(1 0 0/.6);
  box-shadow: inset 0 -4px 10px -8px var(--cl-17-shade),inset 0 6px 10px -6px oklch(1 0 0);
}

@media (prefers-reduced-motion: reduce) {
  .cl-17__tile {
    animation: none;
  }

  .cl-17 * {
    transition-duration: .01ms !important;
  }
}
```
