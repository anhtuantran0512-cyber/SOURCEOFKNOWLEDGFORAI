---
source: "codefronts"
url: "https://codefronts.com/components/css-floating-buttons/material-design-3-floating-action-button-fab/"
title: "Material Design 3 Floating Action Button (FAB)"
section: "components"
category: "css-floating-buttons"
category_name: "CSS Floating Buttons"
description: "The FAB as Material Design 3 actually specifies it, rebuilt from tokens instead of copied from a component library: three sizes (40 / 56 / 96px) with three…"
has_js: "false"
---

Here's a working CSS Floating Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Material Design 3 Floating Action Button (FAB)
Source: https://codefronts.com/components/css-floating-buttons/material-design-3-floating-action-button-fab/

The FAB as Material Design 3 actually specifies it, rebuilt from tokens instead of copied from a component library: three sizes (40 / 56 / 96px) with three different corner radii, the four tonal colour roles, and — the part almost every hand-rolled copy misses — the state layer. M3 does not darken the button on hover; it overlays the on-colour at 8% opacity, 10% on press. Reproducing that one rule is the difference between "looks Material" and "is Material".
## HTML
```html
<section class="fb-01" aria-label="Material Design 3 floating action button demo">
  <div class="fb-01__stage">
    <header class="fb-01__head">
      <p class="fb-01__eyebrow">Material Design 3 · tokens</p>
      <h2 class="fb-01__title">Container, state layer, elevation</h2>
      <p class="fb-01__sub">Three sizes, four tonal roles, one 8% overlay doing all the interaction feedback.</p>
    </header>
    <div class="fb-01__app">
      <div class="fb-01__bar">
        <span class="fb-01__barTitle">Inbox</span>
        <span class="fb-01__barMeta">12 unread</span>
      </div>
      <ul class="fb-01__list">
        <li class="fb-01__row"><span class="fb-01__av" style="--fb-01-av:oklch(0.78 0.13 300)">RS</span><span class="fb-01__rowTxt"><b>Rhea Sandoval</b><i>Design tokens for the FAB set</i></span></li>
        <li class="fb-01__row"><span class="fb-01__av" style="--fb-01-av:oklch(0.8 0.12 200)">MT</span><span class="fb-01__rowTxt"><b>Marcus Tan</b><i>Re: elevation levels 1–5</i></span></li>
        <li class="fb-01__row"><span class="fb-01__av" style="--fb-01-av:oklch(0.82 0.11 140)">JW</span><span class="fb-01__rowTxt"><b>Julia Weiss</b><i>Shipped the tonal palette</i></span></li>
      </ul>
      <button class="fb-01__fab" type="button" aria-label="Compose new message">
        <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04a1 1 0 0 0 0-1.41l-2.34-2.34a1 1 0 0 0-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z" fill="currentColor"/></svg>
      </button>
    </div>
    <div class="fb-01__specs">
      <div class="fb-01__spec">
        <div class="fb-01__specRow">
          <button class="fb-01__fab fb-01__fab--sm" type="button" aria-label="Small FAB, add item"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M11 5h2v14h-2z" fill="currentColor"/><path d="M5 11h14v2H5z" fill="currentColor"/></svg></button>
          <button class="fb-01__fab" type="button" aria-label="Standard FAB, add item"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M11 5h2v14h-2z" fill="currentColor"/><path d="M5 11h14v2H5z" fill="currentColor"/></svg></button>
          <button class="fb-01__fab fb-01__fab--lg" type="button" aria-label="Large FAB, add item"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M11 5h2v14h-2z" fill="currentColor"/><path d="M5 11h14v2H5z" fill="currentColor"/></svg></button>
        </div>
        <p class="fb-01__cap">40 / 12 · 56 / 16 · 96 / 28 &nbsp;<span>size / radius</span></p>
      </div>
      <div class="fb-01__spec">
        <div class="fb-01__specRow">
          <button class="fb-01__fab fb-01__fab--surface" type="button" aria-label="Surface FAB"><span class="fb-01__dot"></span></button>
          <button class="fb-01__fab" type="button" aria-label="Primary container FAB"><span class="fb-01__dot"></span></button>
          <button class="fb-01__fab fb-01__fab--sec" type="button" aria-label="Secondary container FAB"><span class="fb-01__dot"></span></button>
          <button class="fb-01__fab fb-01__fab--ter" type="button" aria-label="Tertiary container FAB"><span class="fb-01__dot"></span></button>
        </div>
        <p class="fb-01__cap">surface · primary · secondary · tertiary &nbsp;<span>colour roles</span></p>
      </div>
    </div>
    <p class="fb-01__chip">state layer 8% hover · 10% pressed · elevation 3</p>
  </div>
</section>
```
## CSS
```css
.fb-01 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--fb-01-bg);
  --fb-01-bg: oklch(0.97 0.012 300);
  --fb-01-surface: oklch(0.99 0.006 300);
  --fb-01-container: oklch(0.9 0.06 305);
  --fb-01-on: oklch(0.32 0.09 300);
  --fb-01-ink: oklch(0.24 0.03 300);
  --fb-01-mut: oklch(0.55 0.02 300);
  --fb-01-line: oklch(0.24 0.03 300/.1);
  --fb-01-size: 56px;
  --fb-01-radius: 16px;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--fb-01-ink);
  display: grid;
  place-items: center;
  padding: clamp(20px,4vw,48px);
}

.fb-01 *,
.fb-01 *::before,
.fb-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fb-01__stage {
  width: min(100%,760px);
  display: grid;
  justify-items: center;
  gap: clamp(18px,3vw,30px);
  text-align: center;
}

.fb-01__head {
  display: grid;
  gap: 9px;
  justify-items: center;
}

.fb-01__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: oklch(0.52 0.16 300);
}

.fb-01__title {
  font-size: clamp(26px,4.4vw,42px);
  line-height: 1.06;
  letter-spacing: -.03em;
  font-weight: 700;
  text-wrap: balance;
}

.fb-01__sub {
  max-width: 50ch;
  font-size: clamp(13.5px,1.6vw,16px);
  line-height: 1.6;
  color: var(--fb-01-mut);
  text-wrap: pretty;
}

.fb-01__app {
  position: relative;
  width: min(100%,470px);
  background: var(--fb-01-surface);
  border: 1px solid var(--fb-01-line);
  border-radius: 26px;
  overflow: hidden;
  text-align: left;
  box-shadow: 0 1px 2px oklch(0.24 0.03 300/.09),0 18px 44px -22px oklch(0.24 0.03 300/.4);
}

.fb-01__bar {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  padding: 18px 20px 12px;
  background: oklch(0.94 0.02 300);
}

.fb-01__barTitle {
  font-size: 19px;
  font-weight: 650;
  letter-spacing: -.02em;
}

.fb-01__barMeta {
  font-size: 12px;
  color: var(--fb-01-mut);
}

.fb-01__list {
  list-style: none;
  display: grid;
}

.fb-01__row {
  display: flex;
  align-items: center;
  gap: 13px;
  padding: 13px 20px;
  border-top: 1px solid var(--fb-01-line);
}

.fb-01__row:last-child {
  padding-bottom: 74px;
}

.fb-01__av {
  flex: none;
  width: 38px;
  height: 38px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  font-size: 12.5px;
  font-weight: 650;
  background: var(--fb-01-av);
  color: oklch(0.24 0.05 300);
}

.fb-01__rowTxt {
  display: grid;
  gap: 2px;
  min-width: 0;
}

.fb-01__rowTxt b {
  font-size: 14px;
  font-weight: 620;
}

.fb-01__rowTxt i {
  font-style: normal;
  font-size: 12.5px;
  color: var(--fb-01-mut);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.fb-01__fab {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  flex: none;
  inline-size: var(--fb-01-size);
  block-size: var(--fb-01-size);
  border: 0;
  border-radius: var(--fb-01-radius);
  background: var(--fb-01-container);
  color: var(--fb-01-on);
  display: grid;
  place-items: center;
  cursor: pointer;
  box-shadow: 0 1px 3px oklch(0.2 0.03 300/.3),0 4px 8px 3px oklch(0.2 0.03 300/.15);
  transition: box-shadow .18s ease,transform .18s cubic-bezier(.2,.9,.3,1.3);
}

.fb-01__app>.fb-01__fab {
  position: absolute;
  right: 18px;
  bottom: 18px;
}

.fb-01__fab svg {
  width: 24px;
  height: 24px;
  position: relative;
  z-index: 2;
}

.fb-01__fab::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
  background: currentColor;
  opacity: 0;
  transition: opacity .12s linear;
  z-index: 1;
}

.fb-01__fab::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
  background: radial-gradient(circle at 50% 50%,currentColor 0%,transparent 62%);
  opacity: 0;
  transform: scale(.2);
  transition: transform .5s ease,opacity .6s ease;
  z-index: 1;
}

.fb-01__fab:hover::before {
  opacity: .08;
}

.fb-01__fab:hover {
  box-shadow: 0 2px 4px oklch(0.2 0.03 300/.3),0 7px 14px 5px oklch(0.2 0.03 300/.16);
  transform: translateY(-1px);
}

.fb-01__fab:active::before {
  opacity: .1;
}

.fb-01__fab:active::after {
  opacity: .14;
  transform: scale(1.6);
  transition: transform 0s,opacity 0s;
}

.fb-01__fab:active {
  transform: scale(.94);
}

.fb-01__fab:focus-visible {
  outline: 3px solid oklch(0.52 0.16 300);
  outline-offset: 3px;
}

.fb-01__fab--sm {
  --fb-01-size: 40px;
  --fb-01-radius: 12px;
}

.fb-01__fab--lg {
  --fb-01-size: 96px;
  --fb-01-radius: 28px;
}

.fb-01__fab--lg svg {
  width: 36px;
  height: 36px;
}

.fb-01__fab--surface {
  background: var(--fb-01-surface);
  color: oklch(0.52 0.16 300);
}

.fb-01__fab--sec {
  background: oklch(0.9 0.035 315);
  color: oklch(0.32 0.05 315);
}

.fb-01__fab--ter {
  background: oklch(0.9 0.05 25);
  color: oklch(0.34 0.09 25);
}

.fb-01__dot {
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: currentColor;
  position: relative;
  z-index: 2;
}

.fb-01__specs {
  display: grid;
  gap: 16px;
  width: 100%;
}

.fb-01__spec {
  background: var(--fb-01-surface);
  border: 1px solid var(--fb-01-line);
  border-radius: 20px;
  padding: 20px 18px 14px;
  display: grid;
  gap: 12px;
  justify-items: center;
}

.fb-01__specRow {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: clamp(14px,3vw,26px);
  flex-wrap: wrap;
  min-height: 96px;
}

.fb-01__cap {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--fb-01-ink);
}

.fb-01__cap span {
  color: var(--fb-01-mut);
}

.fb-01__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--fb-01-mut);
  padding: 8px 14px;
  border: 1px solid var(--fb-01-line);
  border-radius: 99px;
}

@media (min-width: 620px) {
  .fb-01__specs {
    grid-template-columns: 1fr 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .fb-01__fab,
    .fb-01__fab::before,
    .fb-01__fab::after {
    transition: none !important;
  }
}
```
