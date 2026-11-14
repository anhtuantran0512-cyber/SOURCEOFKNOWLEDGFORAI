---
source: "codefronts"
url: "https://codefronts.com/snippets/css-notifications/css-notification-banner-with-close-button/"
title: "CSS Notification Banner With Close Button"
section: "snippets"
category: "css-notifications"
category_name: "CSS Notifications"
description: "The same dismissible banner built in two eras: a 2027 version where :has() lets the banner react to its OWN close-checkbox and exit through display:none via…"
has_js: "false"
---

Here's a working CSS Notification from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Notification Banner With Close Button
Source: https://codefronts.com/snippets/css-notifications/css-notification-banner-with-close-button/

The same dismissible banner built in two eras: a 2027 version where :has() lets the banner react to its OWN close-checkbox and exit through display:none via allow-discrete, and the classic checkbox-hack (input + sibling combinator) that has worked since 2011 — styled identically so you can diff the two mechanisms line by line.
## HTML
```html
<div class="ntf-16-group">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="ntf-16a" aria-label="Banner dismissed by :has(:checked)">
  <div class="ntf-16a__frame">
    <p class="ntf-16a__era">2027 · :has() looks at its own checkbox</p>
    <div class="ntf-16a__banner" role="region" aria-label="Storage notice">
      <div class="ntf-16a__clip">
        <div class="ntf-16a__inner">
          <span class="ntf-16a__ico" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"><path d="M22 12H16l-2 3h-4l-2-3H2"/><path d="M5.5 5.1L2 12v6a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-6l-3.5-6.9A2 2 0 0 0 16.7 4H7.3a2 2 0 0 0-1.8 1.1z"/></svg></span>
          <p class="ntf-16a__tx"><b>Workspace storage 90% full.</b> Older exports will be archived in 7 days — download anything you need to keep.</p>
          <label class="ntf-16a__x" aria-label="Dismiss storage notice"><input class="ntf-16a__box" type="checkbox">&#10005;</label>
        </div>
      </div>
    </div>
    <p class="ntf-16a__after">Content below the banner glides up as the row collapses, then the banner leaves the layout through <b>display:none</b>.</p>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="ntf-16b" aria-label="Banner dismissed by the classic checkbox hack">
  <div class="ntf-16b__frame">
    <p class="ntf-16b__era">2011 · input:checked ~ sibling — still ships</p>
    <input class="ntf-16b__box" type="checkbox" id="ntf-16b-close" aria-label="Dismiss update notice">
    <div class="ntf-16b__banner" role="region" aria-label="Update notice">
      <div class="ntf-16b__clip">
        <div class="ntf-16b__inner">
          <span class="ntf-16b__ico" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a9 9 0 1 1-3-6.7L21 8"/><path d="M21 3v5h-5"/></svg></span>
          <p class="ntf-16b__tx"><b>Version 3.2 available.</b> Restart the app to apply the update.</p>
          <label class="ntf-16b__x" for="ntf-16b-close" aria-hidden="true">&#10005;</label>
        </div>
      </div>
    </div>
    <p class="ntf-16b__after">The input sits <b>before</b> the banner in the DOM — <b>#close:checked ~ .banner</b> is the whole mechanism. Fragile ordering, heroic browser support.</p>
  </div>
</section>
</div>
```
## CSS
```css
.ntf-16-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.ntf-16-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.ntf-16a,
.ntf-16a *,
.ntf-16a *::before,
.ntf-16a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-16a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(120% 100% at 50% 0%,#141a26,#0b0e15);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.ntf-16a__frame {
  width: min(560px,100%);
}

.ntf-16a__era {
  font-size: 11px;
  letter-spacing: .12em;
  text-transform: uppercase;
  font-weight: 600;
  color: oklch(0.75 0.13 200);
  margin-bottom: 12px;
}

.ntf-16a__banner {
  display: grid;
  grid-template-rows: 1fr;
  transition: grid-template-rows .45s cubic-bezier(.4,0,.2,1),opacity .35s ease,display .45s allow-discrete;
}

.ntf-16a__banner:has(.ntf-16a__box:checked) {
  grid-template-rows: 0fr;
  opacity: 0;
  display: none;
}

.ntf-16a__clip {
  overflow: hidden;
}

.ntf-16a__inner {
  display: flex;
  align-items: center;
  gap: 13px;
  padding: 15px 16px;
  border-radius: 14px;
  background: oklch(0.82 0.13 85 / .1);
  border: 1px solid oklch(0.82 0.13 85 / .35);
}

.ntf-16a__ico {
  flex: none;
  width: 36px;
  height: 36px;
  display: grid;
  place-items: center;
  border-radius: 10px;
  color: #171308;
  background: oklch(0.82 0.13 85);
}

.ntf-16a__ico svg {
  width: 18px;
  height: 18px;
}

.ntf-16a__tx {
  font-size: 13px;
  line-height: 1.55;
  color: rgba(235,228,205,.85);
  min-width: 0;
}

.ntf-16a__tx b {
  color: #f4eed9;
  font-weight: 600;
}

.ntf-16a__x {
  position: relative;
  margin-left: auto;
  flex: none;
  width: 30px;
  height: 30px;
  display: grid;
  place-items: center;
  border-radius: 9px;
  font-size: 12px;
  color: rgba(235,228,205,.7);
  cursor: pointer;
  transition: background .15s,color .15s;
}

.ntf-16a__x:hover {
  background: oklch(0.82 0.13 85 / .18);
  color: #f4eed9;
}

.ntf-16a__box {
  position: absolute;
  inset: 0;
  opacity: 0;
  cursor: pointer;
}

.ntf-16a__x:has(.ntf-16a__box:focus-visible) {
  outline: 2px solid oklch(0.82 0.13 85);
  outline-offset: 2px;
}

.ntf-16a__after {
  margin-top: 14px;
  font-size: 13px;
  line-height: 1.65;
  color: rgba(212,224,246,.5);
  text-wrap: pretty;
}

.ntf-16a__after b {
  color: rgba(237,242,252,.8);
}

@media (prefers-reduced-motion: reduce) {
  .ntf-16a__banner {
    transition-duration: .01s;
  }
}

.ntf-16b,
.ntf-16b *,
.ntf-16b *::before,
.ntf-16b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ntf-16b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(120% 100% at 50% 100%,#101722,#0a0d13);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.ntf-16b__frame {
  position: relative;
  width: min(560px,100%);
}

.ntf-16b__era {
  font-size: 11px;
  letter-spacing: .12em;
  text-transform: uppercase;
  font-weight: 600;
  color: oklch(0.72 0.14 250);
  margin-bottom: 12px;
}

.ntf-16b__box {
  position: absolute;
  width: 30px;
  height: 30px;
  opacity: 0;
  z-index: 2;
  inset-inline-end: 8px;
  margin-top: 44px;
  cursor: pointer;
}

.ntf-16b__banner {
  display: grid;
  grid-template-rows: 1fr;
  transition: grid-template-rows .45s cubic-bezier(.4,0,.2,1),opacity .35s ease;
}

.ntf-16b__box:checked ~ .ntf-16b__banner {
  grid-template-rows: 0fr;
  opacity: 0;
  pointer-events: none;
}

.ntf-16b__clip {
  overflow: hidden;
}

.ntf-16b__inner {
  display: flex;
  align-items: center;
  gap: 13px;
  padding: 15px 16px;
  border-radius: 14px;
  background: oklch(0.72 0.14 250 / .1);
  border: 1px solid oklch(0.72 0.14 250 / .35);
}

.ntf-16b__ico {
  flex: none;
  width: 36px;
  height: 36px;
  display: grid;
  place-items: center;
  border-radius: 10px;
  color: #0d1420;
  background: oklch(0.72 0.14 250);
}

.ntf-16b__ico svg {
  width: 18px;
  height: 18px;
}

.ntf-16b__tx {
  font-size: 13px;
  line-height: 1.55;
  color: rgba(210,224,246,.85);
  min-width: 0;
}

.ntf-16b__tx b {
  color: #e9f0fc;
  font-weight: 600;
}

.ntf-16b__x {
  margin-left: auto;
  flex: none;
  width: 30px;
  height: 30px;
  display: grid;
  place-items: center;
  border-radius: 9px;
  font-size: 12px;
  color: rgba(210,224,246,.7);
  cursor: pointer;
  transition: background .15s,color .15s;
}

.ntf-16b__x:hover {
  background: oklch(0.72 0.14 250 / .18);
  color: #e9f0fc;
}

.ntf-16b__box:focus-visible ~ .ntf-16b__banner .ntf-16b__x {
  outline: 2px solid oklch(0.72 0.14 250);
  outline-offset: 2px;
}

.ntf-16b__after {
  margin-top: 14px;
  font-size: 13px;
  line-height: 1.65;
  color: rgba(210,224,246,.5);
  text-wrap: pretty;
}

.ntf-16b__after b {
  color: rgba(233,240,252,.85);
  font-family: ui-monospace,Menlo,monospace;
  font-size: .9em;
}

@media (prefers-reduced-motion: reduce) {
  .ntf-16b__banner {
    transition-duration: .01s;
  }
}
```

## JavaScript
```js
/* No JavaScript — the banner watches its own checkbox with :has(:checked), collapses its grid row, fades, and finally transitions display itself away thanks to allow-discrete. */

/* No JavaScript — the pre-:has() classic: a checkbox BEFORE the banner plus the general sibling combinator. The input is absolutely positioned over the visible ✕ so pointer, keyboard and screen-reader users all operate the same control. */
```
