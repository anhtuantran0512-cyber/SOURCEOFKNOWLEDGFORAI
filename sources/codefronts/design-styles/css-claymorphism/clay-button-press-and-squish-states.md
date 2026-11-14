---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-claymorphism/clay-button-press-and-squish-states/"
title: "Clay Button Press and Squish States"
section: "design-styles"
category: "css-claymorphism"
category_name: "CSS Claymorphism"
description: "Five clay buttons with a real physical press: on :active the object squashes on the Y axis, the drop shadow collapses, and the inset layers invert so the…"
has_js: "false"
---

Here's a working CSS Claymorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Clay Button Press and Squish States
Source: https://codefronts.com/design-styles/css-claymorphism/clay-button-press-and-squish-states/

Five clay buttons with a real physical press: on :active the object squashes on the Y axis, the drop shadow collapses, and the inset layers invert so the surface genuinely looks depressed. Includes the animator's squash-and-stretch release — the button overshoots slightly on the way back up — plus an icon button, a pill, a destructive variant and a disabled state, all keyboard-operable.
## HTML
```html
<section class="cl-09" aria-label="Clay button press and squish states demo">
  <div class="cl-09__stage">
    <header class="cl-09__head">
      <h2 class="cl-09__h">Press it. It squishes.</h2>
      <p class="cl-09__lede">Squash on Y, sink 4px, invert both insets — then release on a springy curve. Hold a button down to feel the three changes.</p>
    </header>
    <div class="cl-09__row">
      <button class="cl-09__btn cl-09__btn--primary" type="button">Start lesson</button>
      <button class="cl-09__btn" type="button">Save draft</button>
      <button class="cl-09__btn cl-09__btn--pill" type="button">Follow</button>
      <button class="cl-09__btn cl-09__btn--icon" type="button" aria-label="Add to favourites">
        <svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path d="M12 20.3l-1.4-1.3C6 14.9 3.5 12.6 3.5 9.6A4.1 4.1 0 017.6 5.5c1.5 0 2.9.7 3.8 1.9.9-1.2 2.3-1.9 3.8-1.9a4.1 4.1 0 014.1 4.1c0 3-2.5 5.3-7.1 9.4z" fill="currentColor"/></svg>
      </button>
      <button class="cl-09__btn cl-09__btn--danger" type="button">Delete</button>
      <button class="cl-09__btn cl-09__btn--off" type="button" disabled aria-disabled="true">Unavailable</button>
    </div>
    <p class="cl-09__chip" aria-hidden="true">scale 1 .93 · translate 0 4px · insets inverted · overshoot on release</p>
  </div>
</section>
```
## CSS
```css
.cl-09,
.cl-09 *,
.cl-09 *::before,
.cl-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cl-09 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--cl-09-bg);
  --cl-09-bg: oklch(0.94 0.03 165);
  --cl-09-clay: oklch(0.88 0.06 170);
  --cl-09-accent: oklch(0.82 0.13 155);
  --cl-09-danger: oklch(0.79 0.14 25);
  --cl-09-shade: oklch(0.55 0.09 170/.55);
  --cl-09-light: oklch(1 0.015 170/.95);
  --cl-09-ink: oklch(0.28 0.05 170);
  --cl-09-mut: oklch(0.5 0.04 170);
  font-family: system-ui,-apple-system,'Segoe UI',sans-serif;
  color: var(--cl-09-ink);
}

.cl-09__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(24px,4vw,40px);
  padding: clamp(20px,5vw,58px);
  background: radial-gradient(75% 55% at 50% 5%,oklch(0.97 0.035 165),transparent 65%);
}

.cl-09__head {
  text-align: center;
  max-width: 56ch;
  display: grid;
  gap: 9px;
}

.cl-09__h {
  font-size: clamp(24px,3.8vw,34px);
  font-weight: 780;
  letter-spacing: -.02em;
  text-wrap: balance;
}

.cl-09__lede {
  font-size: 15px;
  line-height: 1.6;
  color: var(--cl-09-mut);
  text-wrap: pretty;
}

.cl-09__row {
  display: flex;
  flex-wrap: wrap;
  gap: clamp(12px,2vw,20px);
  justify-content: center;
  align-items: center;
  width: min(100%,880px);
}

.cl-09__btn {
  --cl-09-sq: 1;
  display: grid;
  place-items: center;
  min-height: 58px;
  padding: 0 30px;
  border: 0;
  border-radius: 26px;
  font: inherit;
  font-size: 15px;
  font-weight: 680;
  letter-spacing: -.005em;
  color: var(--cl-09-ink);
  cursor: pointer;
  background: var(--cl-09-clay);
  scale: 1 var(--cl-09-sq);
  box-shadow: 0 18px 30px -10px var(--cl-09-shade),inset 0 -14px 22px -10px var(--cl-09-shade),inset 0 16px 22px -8px var(--cl-09-light);
  transition: scale .2s cubic-bezier(.2,.8,.3,1.5),translate .2s cubic-bezier(.2,.8,.3,1.5),box-shadow .2s ease,filter .25s;
}

.cl-09__btn:hover {
  translate: 0 -3px;
  filter: brightness(1.03);
}

.cl-09__btn:active {
  --cl-09-sq: .93;
  translate: 0 4px;
  filter: none;
  box-shadow: inset 0 14px 20px -8px var(--cl-09-shade),inset 0 -10px 18px -10px var(--cl-09-light);
}

.cl-09__btn:focus-visible {
  outline: 3px solid var(--cl-09-ink);
  outline-offset: 4px;
}

.cl-09__btn--primary {
  padding: 0 34px;
  font-size: 16px;
  background: var(--cl-09-accent);
  box-shadow: 0 22px 36px -12px var(--cl-09-shade),inset 0 -16px 24px -10px var(--cl-09-shade),inset 0 18px 24px -8px var(--cl-09-light);
}

.cl-09__btn--pill {
  border-radius: 99px;
}

.cl-09__btn--icon {
  width: 58px;
  padding: 0;
  border-radius: 22px;
}

.cl-09__btn--danger {
  background: var(--cl-09-danger);
  color: oklch(0.26 0.07 25);
}

.cl-09__btn--off {
  background: color-mix(in oklch,var(--cl-09-bg) 88%,white);
  color: color-mix(in oklch,var(--cl-09-mut) 70%,transparent);
  cursor: not-allowed;
  opacity: .62;
  box-shadow: inset 0 6px 12px -8px var(--cl-09-shade),inset 0 -5px 10px -8px var(--cl-09-light);
}

.cl-09__btn--off:hover,
.cl-09__btn--off:active {
  translate: 0;
  --cl-09-sq: 1;
  filter: none;
  box-shadow: inset 0 6px 12px -8px var(--cl-09-shade),inset 0 -5px 10px -8px var(--cl-09-light);
}

.cl-09__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--cl-09-mut);
  padding: 9px 16px;
  border-radius: 99px;
  text-align: center;
  background: oklch(1 0 0/.55);
  box-shadow: inset 0 -4px 10px -8px var(--cl-09-shade),inset 0 6px 10px -6px oklch(1 0 0);
}

@media (prefers-reduced-motion: reduce) {
  .cl-09 * {
    transition-duration: .01ms !important;
  }

  .cl-09__btn:active {
    --cl-09-sq: 1;
  }
}
```
