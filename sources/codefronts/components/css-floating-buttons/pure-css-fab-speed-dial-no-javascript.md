---
source: "codefronts"
url: "https://codefronts.com/components/css-floating-buttons/pure-css-fab-speed-dial-no-javascript/"
title: "Pure CSS FAB Speed Dial (No JavaScript)"
section: "components"
category: "css-floating-buttons"
category_name: "CSS Floating Buttons"
description: "A speed dial with a real open/close state, light dismiss, Escape handling and top-layer stacking — and not a line of script."
has_js: "false"
---

Here's a working CSS Floating Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure CSS FAB Speed Dial (No JavaScript)
Source: https://codefronts.com/components/css-floating-buttons/pure-css-fab-speed-dial-no-javascript/

A speed dial with a real open/close state, light dismiss, Escape handling and top-layer stacking — and not a line of script. The popover attribute gives you the behaviour for free, CSS anchor positioning places the menu against the button, and @starting-style animates it in from display:none. This is the pattern that finally makes the old checkbox hack obsolete.
## HTML
```html
<section class="fb-08" aria-label="Pure CSS speed dial demo">
  <div class="fb-08__page">
    <p class="fb-08__eyebrow">popover · anchor() · @starting-style</p>
    <h2 class="fb-08__title">Top layer, light dismiss, zero script</h2>
    <p class="fb-08__sub">Click the button, then click anywhere outside — the browser closes it, restores focus and keeps <code>aria-expanded</code> in sync on its own.</p>
    <p class="fb-08__chip">popovertarget · :popover-open · allow-discrete</p>
  </div>
  <div class="fb-08__dock">
    <ul class="fb-08__dial" id="fb-08-dial" popover>
      <li><button class="fb-08__act" type="button"><span class="fb-08__ico" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><path d="M12 5v14M5 12h14" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></span>New task</button></li>
      <li><button class="fb-08__act" type="button"><span class="fb-08__ico" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><rect x="4" y="5" width="16" height="15" rx="2.5" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M8 3v4M16 3v4M4 10h16" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg></span>Schedule</button></li>
      <li><button class="fb-08__act" type="button"><span class="fb-08__ico" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><path d="M4 6h16M4 12h16M4 18h10" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg></span>New list</button></li>
      <li><button class="fb-08__act" type="button"><span class="fb-08__ico" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><path d="M12 3l2.4 6.2H21l-5.3 3.9 2 6.4-5.7-4-5.7 4 2-6.4L3 9.2h6.6z" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg></span>Add favourite</button></li>
    </ul>
    <button class="fb-08__fab" id="fb-08-fab" type="button" popovertarget="fb-08-dial" aria-label="Quick create">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 5v14M5 12h14" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg>
    </button>
  </div>
</section>
```
## CSS
```css
.fb-08 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--fb-08-bg);
  --fb-08-bg: oklch(0.97 0.014 195);
  --fb-08-brand: oklch(0.58 0.13 195);
  --fb-08-brandDeep: oklch(0.44 0.12 200);
  --fb-08-ink: oklch(0.24 0.03 200);
  --fb-08-mut: oklch(0.53 0.02 200);
  --fb-08-card: oklch(1 0 0);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--fb-08-ink);
  position: relative;
  display: grid;
  place-items: center;
  padding: clamp(20px,5vw,56px);
}

.fb-08 *,
.fb-08 *::before,
.fb-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fb-08__page {
  width: min(100%,56ch);
  display: grid;
  gap: 12px;
  justify-items: center;
  text-align: center;
}

.fb-08__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--fb-08-brandDeep);
}

.fb-08__title {
  font-size: clamp(26px,4.6vw,44px);
  line-height: 1.05;
  letter-spacing: -.03em;
  font-weight: 700;
  text-wrap: balance;
}

.fb-08__sub {
  font-size: clamp(13.5px,1.7vw,16.5px);
  line-height: 1.62;
  color: var(--fb-08-mut);
  text-wrap: pretty;
}

.fb-08__sub code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .86em;
  background: oklch(0.58 0.13 195/.14);
  padding: 2px 6px;
  border-radius: 6px;
}

.fb-08__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--fb-08-mut);
  padding: 8px 14px;
  border: 1px solid oklch(0.24 0.03 200/.14);
  border-radius: 99px;
}

.fb-08__dock {
  position: absolute;
  right: clamp(18px,4vw,40px);
  bottom: calc(clamp(18px,4vw,40px) + env(safe-area-inset-bottom));
}

.fb-08__fab {
  anchor-name: --fb-08-anchor;
  display: grid;
  place-items: center;
  inline-size: 62px;
  block-size: 62px;
  border: 0;
  border-radius: 20px;
  cursor: pointer;
  color: oklch(0.99 0.01 195);
  background: linear-gradient(155deg,oklch(0.68 0.14 190),var(--fb-08-brandDeep));
  box-shadow: 0 14px 32px -12px oklch(0.44 0.12 200/.9),0 2px 6px oklch(0.3 0.06 200/.28);
  transition: transform .28s cubic-bezier(.2,1.3,.4,1),border-radius .28s ease;
}

.fb-08__fab svg {
  width: 27px;
  height: 27px;
  transition: rotate .32s cubic-bezier(.3,1.35,.4,1);
}

.fb-08__fab:hover {
  transform: translateY(-2px);
}

.fb-08__fab:active {
  transform: scale(.94);
}

.fb-08__fab:focus-visible {
  outline: 3px solid var(--fb-08-brandDeep);
  outline-offset: 4px;
}

.fb-08__fab[aria-expanded="true"] {
  border-radius: 50%;
}

.fb-08__fab[aria-expanded="true"] svg {
  rotate: 135deg;
}

.fb-08__dial {
  position: absolute;
  margin: 0;
  padding: 8px;
  border: 1px solid oklch(0.24 0.03 200/.1);
  border-radius: 20px;
  background: var(--fb-08-card);
  list-style: none;
  display: grid;
  gap: 4px;
  min-width: 210px;
  box-shadow: 0 26px 60px -24px oklch(0.24 0.03 200/.65),0 2px 6px oklch(0.24 0.03 200/.1);
  inset: auto;
  right: 0;
  bottom: 74px;
  opacity: 0;
  translate: 0 14px;
  scale: .96;
  transform-origin: 100% 100%;
  transition: opacity .26s ease,translate .3s cubic-bezier(.2,1.1,.3,1),scale .3s cubic-bezier(.2,1.1,.3,1),overlay .3s allow-discrete,display .3s allow-discrete;
}

.fb-08__dial:popover-open {
  opacity: 1;
  translate: 0 0;
  scale: 1;
}

@starting-style {
  .fb-08__dial:popover-open {
    opacity: 0;
    translate: 0 14px;
    scale: .96;
  }
}

@supports (anchor-name: --x) {
  .fb-08__dial {
    position-anchor: --fb-08-anchor;
    right: anchor(right);
    bottom: calc(anchor(top) + 12px);
    position-try-fallbacks: flip-block;
  }
}

.fb-08__act {
  display: flex;
  align-items: center;
  gap: 11px;
  width: 100%;
  min-height: 46px;
  padding: 0 16px 0 8px;
  border: 0;
  border-radius: 14px;
  background: transparent;
  color: var(--fb-08-ink);
  font-size: 14px;
  font-weight: 600;
  text-align: left;
  cursor: pointer;
  transition: background .16s ease,transform .16s ease;
}

.fb-08__act:hover {
  background: oklch(0.58 0.13 195/.1);
}

.fb-08__act:active {
  transform: scale(.98);
}

.fb-08__act:focus-visible {
  outline: 2.5px solid var(--fb-08-brandDeep);
  outline-offset: -2px;
}

.fb-08__ico {
  flex: none;
  width: 34px;
  height: 34px;
  border-radius: 11px;
  display: grid;
  place-items: center;
  background: oklch(0.58 0.13 195/.12);
  color: var(--fb-08-brandDeep);
}

.fb-08__ico svg {
  width: 19px;
  height: 19px;
}

@media (prefers-reduced-motion: reduce) {
  .fb-08__dial,
    .fb-08__fab,
    .fb-08__fab svg {
    transition-duration: .01ms !important;
  }
}
```
