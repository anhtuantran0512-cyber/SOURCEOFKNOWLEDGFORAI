---
source: "codefronts"
url: "https://codefronts.com/snippets/css-notifications/pure-css-notification-toggle-switch/"
title: "Pure CSS Notification Toggle Switch"
section: "snippets"
category: "css-notifications"
category_name: "CSS Notifications"
description: "The switch pattern end-to-end: a notification preferences panel where each control is a genuine checkbox restyled into a sliding switch (spring thumb via…"
has_js: "false"
---

Here's a working CSS Notification from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure CSS Notification Toggle Switch
Source: https://codefronts.com/snippets/css-notifications/pure-css-notification-toggle-switch/

The switch pattern end-to-end: a notification preferences panel where each control is a genuine checkbox restyled into a sliding switch (spring thumb via linear(), tinted row via :has(), visible focus ring), and a mute-all panel where one master switch dims, disables and un-tints every child row — pointer-events, opacity and state, all coordinated by :has() with zero JavaScript.
## HTML
```html
<div class="ntf-21-group">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="ntf-21a" aria-label="Notification preferences with CSS-only switches">
  <form class="ntf-21a__panel">
    <h2 class="ntf-21a__title">Notifications</h2>
    <label class="ntf-21a__row"><span class="ntf-21a__tx"><b>Product updates</b><small>Release notes, new snippet drops</small></span><span class="ntf-21a__switch"><input type="checkbox" checked><i class="ntf-21a__track" aria-hidden="true"><b></b></i></span></label>
    <label class="ntf-21a__row"><span class="ntf-21a__tx"><b>Comments</b><small>Replies on your snippets</small></span><span class="ntf-21a__switch"><input type="checkbox" checked><i class="ntf-21a__track" aria-hidden="true"><b></b></i></span></label>
    <label class="ntf-21a__row"><span class="ntf-21a__tx"><b>SMS alerts</b><small>Only for security events</small></span><span class="ntf-21a__switch"><input type="checkbox"><i class="ntf-21a__track" aria-hidden="true"><b></b></i></span></label>
    <p class="ntf-21a__cap">Real checkboxes underneath — keyboard, forms and focus rings come free. The thumb settles on a <b>linear()</b> spring.</p>
  </form>
</section>
<link href="https://fonts.googleapis.com/css2?family=Outfit:[email protected]&display=swap" rel="stylesheet">
<section class="ntf-21b" aria-label="Master mute switch disabling child switches">
  <form class="ntf-21b__panel">
    <label class="ntf-21b__master"><span class="ntf-21b__mtx"><b>Pause everything</b><small>One switch, whole subtree — pure :has()</small></span><span class="ntf-21b__switch ntf-21b__switch--big"><input type="checkbox" id="ntf-21b-all"><i class="ntf-21b__track" aria-hidden="true"><b></b></i></span></label>
    <div class="ntf-21b__kids">
      <label class="ntf-21b__row"><span class="ntf-21b__tx"><b>Mentions</b></span><span class="ntf-21b__switch"><input type="checkbox" checked><i class="ntf-21b__track" aria-hidden="true"><b></b></i></span></label>
      <label class="ntf-21b__row"><span class="ntf-21b__tx"><b>Weekly digest</b></span><span class="ntf-21b__switch"><input type="checkbox" checked><i class="ntf-21b__track" aria-hidden="true"><b></b></i></span></label>
      <label class="ntf-21b__row"><span class="ntf-21b__tx"><b>Marketing</b></span><span class="ntf-21b__switch"><input type="checkbox"><i class="ntf-21b__track" aria-hidden="true"><b></b></i></span></label>
    </div>
    <p class="ntf-21b__cap">Pausing dims and disables the children <em>without touching their state</em> — unpause and every row remembers itself.</p>
  </form>
</section>
</div>
```
## CSS
```css
.ntf-21-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.ntf-21-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.ntf-21a,
.ntf-21a *,
.ntf-21a *::before,
.ntf-21a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-21a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(120% 100% at 50% 0%,#151a26,#0b0e15);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.ntf-21a__panel {
  width: min(410px,100%);
  padding: 24px;
  border-radius: 20px;
  background: rgba(255,255,255,.045);
  border: 1px solid rgba(165,190,230,.16);
  box-shadow: 0 30px 70px -40px rgba(0,0,0,.9);
}

.ntf-21a__title {
  font-size: 19px;
  font-weight: 600;
  letter-spacing: -.01em;
  color: #edf2fc;
  margin-bottom: 8px;
}

.ntf-21a__row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  padding: 14px 12px;
  border-radius: 13px;
  cursor: pointer;
  transition: background .2s;
}

.ntf-21a__row:hover {
  background: rgba(255,255,255,.04);
}

.ntf-21a__row:has(input:checked) {
  background: oklch(0.75 0.14 200 / .07);
}

.ntf-21a__row+.ntf-21a__row {
  margin-top: 2px;
}

.ntf-21a__tx {
  display: grid;
  gap: 2px;
  min-width: 0;
}

.ntf-21a__tx b {
  font-size: 14px;
  font-weight: 600;
  color: #edf2fc;
}

.ntf-21a__tx small {
  font-size: 12px;
  color: rgba(212,224,246,.5);
}

.ntf-21a__switch {
  position: relative;
  flex: none;
}

.ntf-21a__switch input {
  position: absolute;
  inset: 0;
  opacity: 0;
  cursor: pointer;
}

.ntf-21a__track {
  display: block;
  width: 46px;
  height: 27px;
  border-radius: 999px;
  background: rgba(255,255,255,.14);
  padding: 3.5px;
  transition: background .25s;
}

.ntf-21a__track b {
  display: block;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: #fff;
  box-shadow: 0 1px 3px rgba(0,0,0,.4);
  transition: translate .28s ease;
  transition: translate .45s linear(0,0.62 18%,1.02 38%,1.12 50%,1.02 66%,0.98 78%,1);
}

.ntf-21a__switch:has(input:checked) .ntf-21a__track {
  background: oklch(0.75 0.14 200);
}

.ntf-21a__switch:has(input:checked) .ntf-21a__track b {
  translate: 19px 0;
}

.ntf-21a__switch:has(input:focus-visible) .ntf-21a__track {
  outline: 2px solid oklch(0.75 0.14 200);
  outline-offset: 3px;
}

.ntf-21a__cap {
  margin-top: 14px;
  font-size: 11.5px;
  line-height: 1.6;
  color: rgba(212,224,246,.45);
  text-wrap: pretty;
}

.ntf-21a__cap b {
  color: rgba(237,242,252,.8);
}

@media (prefers-reduced-motion: reduce) {
  .ntf-21a__track b {
    transition-duration: .01s;
  }
}

.ntf-21b,
.ntf-21b *,
.ntf-21b *::before,
.ntf-21b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-21b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,#f6f3ec,#ece5d5);
  font-family: 'Outfit','Segoe UI',system-ui,sans-serif;
}

.ntf-21b__panel {
  width: min(400px,100%);
  padding: 22px;
  border-radius: 20px;
  background: #fffdf7;
  border: 1px solid rgba(36,31,23,.11);
  box-shadow: 0 28px 62px -34px rgba(36,31,23,.5);
}

.ntf-21b__master {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  padding: 14px;
  border-radius: 14px;
  background: #241f17;
  cursor: pointer;
}

.ntf-21b__mtx {
  display: grid;
  gap: 2px;
}

.ntf-21b__mtx b {
  font-size: 14.5px;
  font-weight: 700;
  color: #fffdf7;
}

.ntf-21b__mtx small {
  font-size: 11.5px;
  color: rgba(255,253,247,.55);
}

.ntf-21b__kids {
  margin-top: 10px;
  transition: opacity .3s;
}

.ntf-21b__panel:has(#ntf-21b-all:checked) .ntf-21b__kids {
  opacity: .4;
  pointer-events: none;
}

.ntf-21b__panel:has(#ntf-21b-all:checked) .ntf-21b__kids input {
  visibility: hidden;
}

.ntf-21b__row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  padding: 12px 14px;
  border-radius: 12px;
  cursor: pointer;
  transition: background .15s;
}

.ntf-21b__row:hover {
  background: rgba(36,31,23,.045);
}

.ntf-21b__tx b {
  font-size: 13.5px;
  font-weight: 600;
  color: #241f17;
}

.ntf-21b__switch {
  position: relative;
  flex: none;
}

.ntf-21b__switch input {
  position: absolute;
  inset: 0;
  opacity: 0;
  cursor: pointer;
}

.ntf-21b__track {
  display: block;
  width: 42px;
  height: 24px;
  border-radius: 999px;
  background: rgba(36,31,23,.16);
  padding: 3px;
  transition: background .25s;
}

.ntf-21b__track b {
  display: block;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: #fffdf7;
  box-shadow: 0 1px 3px rgba(36,31,23,.35);
  transition: translate .3s cubic-bezier(.22,1.4,.36,1);
}

.ntf-21b__switch:has(input:checked) .ntf-21b__track {
  background: oklch(0.62 0.14 155);
}

.ntf-21b__switch:has(input:checked) .ntf-21b__track b {
  translate: 18px 0;
}

.ntf-21b__switch--big .ntf-21b__track {
  background: rgba(255,253,247,.22);
  width: 48px;
  height: 27px;
}

.ntf-21b__switch--big .ntf-21b__track b {
  width: 21px;
  height: 21px;
}

.ntf-21b__switch--big:has(input:checked) .ntf-21b__track {
  background: oklch(0.72 0.16 45);
}

.ntf-21b__switch--big:has(input:checked) .ntf-21b__track b {
  translate: 21px 0;
}

.ntf-21b__switch:has(input:focus-visible) .ntf-21b__track {
  outline: 2px solid #241f17;
  outline-offset: 3px;
}

.ntf-21b__master .ntf-21b__switch:has(input:focus-visible) .ntf-21b__track {
  outline-color: #fffdf7;
}

.ntf-21b__cap {
  margin-top: 14px;
  font-size: 11.5px;
  line-height: 1.6;
  color: rgba(36,31,23,.5);
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .ntf-21b__track b,
    .ntf-21b__kids {
    transition-duration: .01s;
  }
}
```

## JavaScript
```js
/* No JavaScript — checkboxes hold the state, :has() paints track, thumb and row tint, and the second (spring) transition declaration wins where linear() is supported, falling back to plain ease elsewhere. */

/* No JavaScript — .panel:has(#all:checked) dims the subtree, kills pointer events and hides the inputs from the tab order; child checkbox state is never mutated, so unpausing restores everything. */
```
