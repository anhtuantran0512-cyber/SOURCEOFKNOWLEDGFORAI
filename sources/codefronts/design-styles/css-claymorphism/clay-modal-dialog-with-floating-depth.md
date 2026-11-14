---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-claymorphism/clay-modal-dialog-with-floating-depth/"
title: "Clay Modal Dialog with Floating Depth"
section: "design-styles"
category: "css-claymorphism"
category_name: "CSS Claymorphism"
description: "A top-tier clay dialog built on the native popover API — no focus-trap library, no aria-modal hand-wiring."
has_js: "false"
---

Here's a working CSS Claymorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Clay Modal Dialog with Floating Depth
Source: https://codefronts.com/design-styles/css-claymorphism/clay-modal-dialog-with-floating-depth/

A top-tier clay dialog built on the native popover API — no focus-trap library, no aria-modal hand-wiring. The browser handles the top layer, light dismiss, Escape and focus. Clay does the rest: tier-4 depth, a blurred scrim, and an entry that scales from 0.94 with @starting-style, plus a matching exit.
## HTML
```html
<section class="cl-14" aria-label="Clay modal dialog with floating depth demo">
  <div class="cl-14__stage">
    <div class="cl-14__page">
      <h2 class="cl-14__h">Native popover, clay depth</h2>
      <p class="cl-14__lede">The top layer, light dismiss, Escape and focus are the browser's job. Tier-4 shadows and a blurred backdrop are ours.</p>
      <button class="cl-14__open" type="button" popovertarget="cl-14-dialog">Publish collection</button>
      <ul class="cl-14__facts">
        <li>popover="auto"</li>
        <li>@starting-style</li>
        <li>transition-behavior: allow-discrete</li>
        <li>::backdrop blur</li>
      </ul>
    </div>
    <div class="cl-14__modal" id="cl-14-dialog" popover="auto" aria-labelledby="cl-14-title">
      <span class="cl-14__grip" aria-hidden="true"></span>
      <h3 class="cl-14__title" id="cl-14-title">Publish “20 CSS Claymorphism”?</h3>
      <p class="cl-14__body">All 20 demos become public and the collection page goes live at once. You can unpublish any single demo later.</p>
      <ul class="cl-14__check">
        <li>Snippets validated</li>
        <li>Reduced-motion pass</li>
        <li>Contrast pass</li>
      </ul>
      <div class="cl-14__actions">
        <button class="cl-14__btn cl-14__btn--ghost" type="button" popovertarget="cl-14-dialog" popovertargetaction="hide">Not yet</button>
        <button class="cl-14__btn cl-14__btn--go" type="button" popovertarget="cl-14-dialog" popovertargetaction="hide">Publish now</button>
      </div>
    </div>
    <p class="cl-14__chip" aria-hidden="true">tier 4 elevation · display + overlay allow-discrete · native top layer</p>
  </div>
</section>
```
## CSS
```css
.cl-14,
.cl-14 *,
.cl-14 *::before,
.cl-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cl-14 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--cl-14-bg);
  --cl-14-bg: oklch(0.93 0.035 300);
  --cl-14-clay: oklch(0.9 0.05 300);
  --cl-14-accent: oklch(0.79 0.14 300);
  --cl-14-shade: oklch(0.5 0.1 300/.55);
  --cl-14-light: oklch(1 0.012 300/.95);
  --cl-14-ink: oklch(0.27 0.06 300);
  --cl-14-mut: oklch(0.5 0.045 300);
  font-family: system-ui,-apple-system,'Segoe UI',sans-serif;
  color: var(--cl-14-ink);
}

.cl-14__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 20px;
  padding: clamp(20px,5vw,56px);
  background: radial-gradient(85% 60% at 50% 0%,oklch(0.97 0.035 310),transparent 68%);
}

.cl-14__page {
  display: grid;
  gap: 14px;
  justify-items: center;
  text-align: center;
  width: min(100%,620px);
  padding: clamp(26px,4vw,44px);
  border-radius: 44px;
  background: color-mix(in oklch,var(--cl-14-bg) 94%,white);
  box-shadow: 0 26px 48px -20px var(--cl-14-shade),inset 0 -16px 28px -16px var(--cl-14-shade),inset 0 18px 28px -12px var(--cl-14-light);
}

.cl-14__h {
  font-size: clamp(23px,3.6vw,32px);
  font-weight: 780;
  letter-spacing: -.022em;
  text-wrap: balance;
}

.cl-14__lede {
  max-width: 48ch;
  font-size: 15px;
  line-height: 1.6;
  color: var(--cl-14-mut);
  text-wrap: pretty;
}

.cl-14__open {
  min-height: 58px;
  margin-top: 6px;
  padding: 0 34px;
  border: 0;
  border-radius: 26px;
  font: inherit;
  font-size: 16px;
  font-weight: 680;
  color: oklch(0.24 0.07 300);
  cursor: pointer;
  background: var(--cl-14-accent);
  box-shadow: 0 22px 36px -12px var(--cl-14-shade),inset 0 -16px 24px -10px var(--cl-14-shade),inset 0 18px 24px -8px var(--cl-14-light);
  transition: translate .2s cubic-bezier(.2,.8,.3,1.4),scale .2s cubic-bezier(.2,.8,.3,1.4),box-shadow .2s;
}

.cl-14__open:hover {
  translate: 0 -4px;
}

.cl-14__open:active {
  scale: 1 .93;
  translate: 0 3px;
  box-shadow: inset 0 14px 22px -8px var(--cl-14-shade);
}

.cl-14__open:focus-visible {
  outline: 3px solid var(--cl-14-ink);
  outline-offset: 4px;
}

.cl-14__facts {
  list-style: none;
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  justify-content: center;
  margin-top: 6px;
}

.cl-14__facts li {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  padding: 7px 12px;
  border-radius: 99px;
  color: var(--cl-14-mut);
  background: oklch(1 0 0/.6);
  box-shadow: inset 0 -4px 8px -7px var(--cl-14-shade),inset 0 5px 8px -5px oklch(1 0 0);
}

.cl-14__modal {
  position: fixed;
  inset: 0;
  margin: auto;
  width: min(92vw,460px);
  max-height: 86svh;
  overflow: auto;
  display: none;
  gap: 14px;
  padding: clamp(24px,3.6vw,34px);
  border: 0;
  border-radius: 40px;
  background: var(--cl-14-clay);
  color: var(--cl-14-ink);
  box-shadow: 0 60px 110px -30px oklch(0.32 0.08 300/.65),0 24px 44px -16px var(--cl-14-shade),inset 0 -20px 34px -16px var(--cl-14-shade),inset 0 24px 34px -10px var(--cl-14-light);
  opacity: 0;
  scale: .94;
  translate: 0 12px;
  transition: opacity .32s cubic-bezier(.2,.8,.3,1),scale .32s cubic-bezier(.2,.9,.3,1.15),translate .32s cubic-bezier(.2,.9,.3,1.15),display .32s allow-discrete,overlay .32s allow-discrete;
}

.cl-14__modal:popover-open {
  display: grid;
  opacity: 1;
  scale: 1;
  translate: 0;
}

@starting-style {
  .cl-14__modal:popover-open {
    display: grid;
    opacity: 0;
    scale: .94;
    translate: 0 12px;
  }
}

.cl-14__modal::backdrop {
  background: oklch(0.34 0.06 300/.42);
  -webkit-backdrop-filter: blur(7px);
  backdrop-filter: blur(7px);
  opacity: 0;
  transition: opacity .32s,display .32s allow-discrete,overlay .32s allow-discrete;
}

.cl-14__modal:popover-open::backdrop {
  opacity: 1;
}

@starting-style {
  .cl-14__modal:popover-open::backdrop {
    opacity: 0;
  }
}

.cl-14__grip {
  justify-self: center;
  width: 54px;
  height: 6px;
  border-radius: 99px;
  background: color-mix(in oklch,var(--cl-14-shade) 40%,transparent);
  box-shadow: inset 0 2px 3px -1px var(--cl-14-shade);
}

.cl-14__title {
  font-size: clamp(20px,3vw,24px);
  font-weight: 780;
  letter-spacing: -.02em;
  text-wrap: balance;
}

.cl-14__body {
  font-size: 14.5px;
  line-height: 1.6;
  color: color-mix(in oklch,var(--cl-14-ink) 82%,transparent);
  text-wrap: pretty;
}

.cl-14__check {
  list-style: none;
  display: grid;
  gap: 8px;
  margin: 2px 0 4px;
}

.cl-14__check li {
  display: flex;
  align-items: center;
  gap: 11px;
  padding: 11px 15px;
  border-radius: 20px;
  font-size: 13.5px;
  font-weight: 600;
  background: color-mix(in oklch,var(--cl-14-clay) 78%,white);
  box-shadow: inset 0 -6px 11px -8px var(--cl-14-shade),inset 0 7px 11px -6px var(--cl-14-light);
}

.cl-14__check li::before {
  content: '';
  flex: none;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: oklch(0.78 0.14 155);
  box-shadow: inset 0 5px 7px -4px oklch(1 0 0/.7),0 4px 7px -4px var(--cl-14-shade);
}

.cl-14__actions {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 4px;
}

.cl-14__btn {
  flex: 1;
  min-width: 130px;
  min-height: 52px;
  padding: 0 22px;
  border: 0;
  border-radius: 24px;
  font: inherit;
  font-size: 14.5px;
  font-weight: 680;
  cursor: pointer;
  transition: translate .18s,scale .18s cubic-bezier(.2,.8,.3,1.4),box-shadow .18s;
}

.cl-14__btn--ghost {
  color: var(--cl-14-ink);
  background: color-mix(in oklch,var(--cl-14-clay) 66%,white);
  box-shadow: 0 12px 20px -12px var(--cl-14-shade),inset 0 -9px 15px -9px var(--cl-14-shade),inset 0 11px 15px -7px var(--cl-14-light);
}

.cl-14__btn--go {
  color: oklch(0.24 0.07 300);
  background: var(--cl-14-accent);
  box-shadow: 0 16px 26px -12px var(--cl-14-shade),inset 0 -11px 18px -9px var(--cl-14-shade),inset 0 13px 18px -7px var(--cl-14-light);
}

.cl-14__btn:hover {
  translate: 0 -3px;
}

.cl-14__btn:active {
  scale: 1 .94;
  translate: 0 3px;
  box-shadow: inset 0 12px 18px -8px var(--cl-14-shade);
}

.cl-14__btn:focus-visible {
  outline: 3px solid var(--cl-14-ink);
  outline-offset: 3px;
}

.cl-14__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--cl-14-mut);
  padding: 9px 16px;
  border-radius: 99px;
  text-align: center;
  background: oklch(1 0 0/.55);
  box-shadow: inset 0 -4px 10px -8px var(--cl-14-shade),inset 0 6px 10px -6px oklch(1 0 0);
}

@media (prefers-reduced-motion: reduce) {
  .cl-14 * {
    transition-duration: .01ms !important;
  }
}
```
