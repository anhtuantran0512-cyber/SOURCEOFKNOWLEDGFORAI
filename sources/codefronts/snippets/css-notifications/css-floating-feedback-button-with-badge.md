---
source: "codefronts"
url: "https://codefronts.com/snippets/css-notifications/css-floating-feedback-button-with-badge/"
title: "CSS Floating Feedback Button With Badge"
section: "snippets"
category: "css-notifications"
category_name: "CSS Notifications"
description: "Two endgames for the floating button: a circle-to-pill FAB whose label expands through an animatable grid column (the transition-to-auto-width trick that…"
has_js: "false"
---

Here's a working CSS Notification from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Floating Feedback Button With Badge
Source: https://codefronts.com/snippets/css-notifications/css-floating-feedback-button-with-badge/

Two endgames for the floating button: a circle-to-pill FAB whose label expands through an animatable grid column (the transition-to-auto-width trick that works today, with interpolate-size noted as the 2027 one-liner), badge riding the morph — and a speed-dial FAB that blooms three labeled actions on a checkbox toggle, each springing out with its own delay, the unread badge clearing the moment the dial opens.
## HTML
```html
<div class="ntf-30-group">
<link href="https://fonts.googleapis.com/css2?family=Outfit:[email protected]&display=swap" rel="stylesheet">
<section class="ntf-30a" aria-label="Floating feedback button expanding to a pill">
  <div class="ntf-30a__page">
    <h2 class="ntf-30a__ghost">Docs page</h2>
    <p class="ntf-30a__ghostsub">hover (or tab to) the button in the corner</p>
  </div>
  <button class="ntf-30a__fab" type="button" aria-label="Feedback, 2 unread replies">
    <span class="ntf-30a__glyph" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.4 8.4 0 0 1-9 8.4 8.6 8.6 0 0 1-3.9-.9L3 20l1-4.1a8.4 8.4 0 1 1 17-4.4z"/></svg></span>
    <span class="ntf-30a__label" aria-hidden="true"><span>Give feedback</span></span>
    <b class="ntf-30a__badge" aria-hidden="true">2</b>
  </button>
</section>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="ntf-30b" aria-label="Speed dial floating button with actions">
  <div class="ntf-30b__page">
    <h2 class="ntf-30b__ghost">Support corner</h2>
    <p class="ntf-30b__ghostsub">open the dial — the badge clears, three labeled actions bloom</p>
  </div>
  <div class="ntf-30b__dial">
    <a class="ntf-30b__act" href="#" onclick="return false" style="--i:3"><span class="ntf-30b__pill">Report a bug</span><i class="ntf-30b__mini" aria-hidden="true">&#9888;</i></a>
    <a class="ntf-30b__act" href="#" onclick="return false" style="--i:2"><span class="ntf-30b__pill">Suggest a feature</span><i class="ntf-30b__mini" aria-hidden="true">&#10022;</i></a>
    <a class="ntf-30b__act" href="#" onclick="return false" style="--i:1"><span class="ntf-30b__pill">Message support</span><i class="ntf-30b__mini" aria-hidden="true">&#9993;</i></a>
    <label class="ntf-30b__fab" aria-label="Open support menu, 3 unread">
      <input class="ntf-30b__state" type="checkbox">
      <i class="ntf-30b__plus" aria-hidden="true"></i>
      <b class="ntf-30b__badge" aria-hidden="true">3</b>
    </label>
  </div>
</section>
</div>
```
## CSS
```css
.ntf-30-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.ntf-30-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.ntf-30a,
.ntf-30a *,
.ntf-30a *::before,
.ntf-30a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-30a {
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: linear-gradient(180deg,#f6f4ef,#ebe7dc);
  font-family: 'Outfit','Segoe UI',system-ui,sans-serif;
}

.ntf-30a__page {
  text-align: center;
  padding: 24px;
}

.ntf-30a__ghost {
  font-size: clamp(26px,4vw,36px);
  font-weight: 600;
  letter-spacing: -.02em;
  color: rgba(35,31,24,.22);
}

.ntf-30a__ghostsub {
  margin-top: 8px;
  font-size: 13px;
  color: rgba(35,31,24,.35);
}

.ntf-30a__fab {
  position: absolute;
  bottom: calc(22px + env(safe-area-inset-bottom,0px));
  inset-inline-end: 22px;
  display: flex;
  align-items: center;
  height: 56px;
  padding: 0 16px;
  border: 0;
  border-radius: 999px;
  color: #f6f4ef;
  background: #232019;
  cursor: pointer;
  box-shadow: 0 3px 8px rgba(35,31,24,.3),0 22px 44px -16px rgba(35,31,24,.5);
  transition: scale .15s,background .2s;
}

.ntf-30a__fab:hover {
  background: #38332a;
}

.ntf-30a__fab:active {
  scale: .96;
}

.ntf-30a__fab:focus-visible {
  outline: 2.5px solid #232019;
  outline-offset: 3px;
}

.ntf-30a__glyph {
  flex: none;
  display: grid;
  place-items: center;
  width: 24px;
  height: 24px;
}

.ntf-30a__glyph svg {
  width: 22px;
  height: 22px;
}

.ntf-30a__label {
  display: grid;
  grid-template-columns: 0fr;
  transition: grid-template-columns .35s cubic-bezier(.22,1.2,.36,1);
}

.ntf-30a__label span {
  overflow: hidden;
  white-space: nowrap;
  font-size: 14px;
  font-weight: 700;
  padding-inline-start: 0;
  transition: padding .35s cubic-bezier(.22,1.2,.36,1);
}

.ntf-30a__fab:hover .ntf-30a__label,
.ntf-30a__fab:focus-visible .ntf-30a__label {
  grid-template-columns: 1fr;
}

.ntf-30a__fab:hover .ntf-30a__label span,
.ntf-30a__fab:focus-visible .ntf-30a__label span {
  padding-inline-start: 10px;
}

.ntf-30a__badge {
  position: absolute;
  top: -4px;
  inset-inline-end: -2px;
  min-inline-size: 20px;
  block-size: 20px;
  display: grid;
  place-items: center;
  padding-inline: 5px;
  border-radius: 999px;
  font-size: 11px;
  font-weight: 800;
  font-variant-numeric: tabular-nums;
  color: #fff;
  background: oklch(0.63 0.21 25);
  border: 2.5px solid #f6f4ef;
  animation: ntf-30a-pop .5s cubic-bezier(.22,1.6,.36,1) both .4s;
}

@keyframes ntf-30a-pop {
  from {
    scale: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ntf-30a__label,
    .ntf-30a__label span {
    transition-duration: .01s;
  }

  .ntf-30a__badge {
    animation: none;
  }
}

.ntf-30b,
.ntf-30b *,
.ntf-30b *::before,
.ntf-30b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-30b {
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: radial-gradient(120% 100% at 50% 0%,#161b27,#0c0e15);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.ntf-30b__page {
  text-align: center;
  padding: 24px;
}

.ntf-30b__ghost {
  font-size: clamp(26px,4vw,36px);
  font-weight: 600;
  letter-spacing: -.02em;
  color: rgba(226,234,250,.22);
}

.ntf-30b__ghostsub {
  margin-top: 8px;
  font-size: 13px;
  color: rgba(226,234,250,.32);
}

.ntf-30b__dial {
  position: absolute;
  bottom: calc(22px + env(safe-area-inset-bottom,0px));
  inset-inline-end: 22px;
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 12px;
}

.ntf-30b__act {
  display: flex;
  align-items: center;
  gap: 10px;
  text-decoration: none;
  opacity: 0;
  translate: 0 14px;
  scale: .85;
  pointer-events: none;
  transition: opacity .25s ease,translate .3s cubic-bezier(.22,1.4,.36,1),scale .3s cubic-bezier(.22,1.4,.36,1);
}

.ntf-30b__dial:has(.ntf-30b__state:checked) .ntf-30b__act {
  opacity: 1;
  translate: 0 0;
  scale: 1;
  pointer-events: auto;
  transition-delay: calc(var(--i) * .05s);
}

.ntf-30b__pill {
  font-size: 12.5px;
  font-weight: 600;
  color: #0c0e15;
  background: #e8eefc;
  padding: 8px 13px;
  border-radius: 999px;
  box-shadow: 0 10px 24px -12px rgba(0,0,0,.8);
}

.ntf-30b__mini {
  flex: none;
  width: 42px;
  height: 42px;
  display: grid;
  place-items: center;
  border-radius: 50%;
  font-style: normal;
  font-size: 16px;
  color: #e8eefc;
  background: rgba(255,255,255,.1);
  border: 1px solid rgba(165,190,230,.28);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
}

.ntf-30b__act:hover .ntf-30b__mini {
  background: rgba(255,255,255,.18);
}

.ntf-30b__fab {
  position: relative;
  width: 56px;
  height: 56px;
  display: grid;
  place-items: center;
  border-radius: 50%;
  background: oklch(0.75 0.13 200);
  cursor: pointer;
  box-shadow: 0 3px 8px rgba(0,0,0,.4),0 22px 44px -16px oklch(0.75 0.13 200 / .5);
  transition: scale .15s,background .2s;
}

.ntf-30b__fab:hover {
  scale: 1.05;
}

.ntf-30b__fab:active {
  scale: .95;
}

.ntf-30b__state {
  position: absolute;
  inset: 0;
  opacity: 0;
  cursor: pointer;
}

.ntf-30b__fab:has(.ntf-30b__state:focus-visible) {
  outline: 2.5px solid #e8eefc;
  outline-offset: 3px;
}

.ntf-30b__plus {
  position: relative;
  width: 20px;
  height: 20px;
  transition: rotate .35s cubic-bezier(.22,1.2,.36,1);
}

.ntf-30b__plus::before,
.ntf-30b__plus::after {
  content: "";
  position: absolute;
  inset: 0;
  margin: auto;
  background: #0c0e15;
  border-radius: 2px;
}

.ntf-30b__plus::before {
  width: 20px;
  height: 3px;
}

.ntf-30b__plus::after {
  width: 3px;
  height: 20px;
}

.ntf-30b__dial:has(.ntf-30b__state:checked) .ntf-30b__plus {
  rotate: 45deg;
}

.ntf-30b__badge {
  position: absolute;
  top: -3px;
  inset-inline-end: -3px;
  min-inline-size: 20px;
  block-size: 20px;
  display: grid;
  place-items: center;
  padding-inline: 5px;
  border-radius: 999px;
  font-size: 11px;
  font-weight: 800;
  color: #fff;
  background: oklch(0.63 0.21 25);
  border: 2.5px solid #161b27;
  transition: scale .25s cubic-bezier(.22,1.4,.36,1);
}

.ntf-30b__dial:has(.ntf-30b__state:checked) .ntf-30b__badge {
  scale: 0;
}

@media (prefers-reduced-motion: reduce) {
  .ntf-30b__act {
    transition-duration: .01s;
    transition-delay: 0s!important;
  }

  .ntf-30b__plus {
    transition-duration: .01s;
  }
}
```

## JavaScript
```js
/* No JavaScript — the label lives in a grid column that animates 0fr → 1fr on hover/focus-visible (the today-everywhere version of transitioning to width:auto; interpolate-size:allow-keywords is the coming one-liner). */

/* No JavaScript — a checkbox is the dial's state: :has(:checked) blooms the actions (staggered via --i delays that reset to 0 on close), rotates + into ×, and clears the badge because opening acknowledges the unread count. */
```
