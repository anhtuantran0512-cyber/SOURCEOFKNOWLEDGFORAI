---
source: "codefronts"
url: "https://codefronts.com/components/css-floating-buttons/compose-tooltip-fab/"
title: "Floating Compose Button with Tooltip on Hover CSS"
section: "components"
category: "css-floating-buttons"
category_name: "CSS Floating Buttons"
description: "An icon-only FAB is only usable if it can say what it does."
has_js: "false"
---

Here's a working CSS Floating Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Floating Compose Button with Tooltip on Hover CSS
Source: https://codefronts.com/components/css-floating-buttons/compose-tooltip-fab/

An icon-only FAB is only usable if it can say what it does. This is the tooltip done to spec: it appears on hover and keyboard focus, waits 400ms before showing but disappears instantly, never covers the button, flips when it would leave the viewport, and — critically — the tooltip text is not the accessible name, it is a description of it.
## HTML
```html
<section class="fb-19" aria-label="Floating compose button with tooltip demo">
  <div class="fb-19__app">
    <aside class="fb-19__rail">
      <button class="fb-19__railBtn" type="button" aria-label="Inbox" aria-describedby="fb-19-t1"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M3 12l3-7h12l3 7v6H3z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><path d="M3 12h5l1.4 2.4h5.2L16 12h5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg></button>
      <span class="fb-19__tip fb-19__tip--rail" id="fb-19-t1" role="tooltip">Inbox <kbd>G</kbd> <kbd>I</kbd></span>
      <button class="fb-19__railBtn" type="button" aria-label="Starred" aria-describedby="fb-19-t2"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 3.6l2.5 5.4 5.9.6-4.4 4 1.2 5.8L12 16.4 6.8 19.4 8 13.6l-4.4-4 5.9-.6z" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg></button>
      <span class="fb-19__tip fb-19__tip--rail" id="fb-19-t2" role="tooltip">Starred <kbd>G</kbd> <kbd>S</kbd></span>
      <button class="fb-19__railBtn" type="button" aria-label="Archive" aria-describedby="fb-19-t3"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><rect x="3" y="4" width="18" height="4.5" rx="1.4" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M5 8.5V19h14V8.5M10 12h4" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg></button>
      <span class="fb-19__tip fb-19__tip--rail" id="fb-19-t3" role="tooltip">Archive <kbd>E</kbd></span>
    </aside>
    <div class="fb-19__main">
      <p class="fb-19__eyebrow">400ms in · 0ms out · flip-inline</p>
      <h2 class="fb-19__title">A tooltip is a description, not a name</h2>
      <p class="fb-19__sub">Hover the rail, then tab through it. Same tooltip, same timing, and the button still announces its own label first.</p>
      <p class="fb-19__chip">aria-describedby + aria-label · anchor()</p>
    </div>
    <div class="fb-19__dock">
      <button class="fb-19__fab" id="fb-19-fab" type="button" aria-label="Compose" aria-describedby="fb-19-tip">
        <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 20h4L18.5 9.5l-4-4L4 16z" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linejoin="round"/><path d="M14.5 5.5l4 4" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>
      </button>
      <span class="fb-19__tip" id="fb-19-tip" role="tooltip"><b>Compose</b><kbd>C</kbd></span>
    </div>
  </div>
</section>
```
## CSS
```css
.fb-19 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--fb-19-bg);
  --fb-19-bg: oklch(0.96 0.008 265);
  --fb-19-brand: oklch(0.52 0.16 258);
  --fb-19-ink: oklch(0.22 0.02 262);
  --fb-19-mut: oklch(0.53 0.015 262);
  --fb-19-card: oklch(1 0 0);
  --fb-19-tip: oklch(0.24 0.03 262);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--fb-19-ink);
  display: grid;
  place-items: center;
  padding: clamp(18px,4vw,48px);
}

.fb-19 *,
.fb-19 *::before,
.fb-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fb-19__app {
  position: relative;
  width: min(100%,760px);
  min-height: min(62svh,520px);
  display: grid;
  grid-template-columns: auto 1fr;
  gap: clamp(16px,3vw,32px);
  padding: clamp(18px,3vw,26px);
  border-radius: 26px;
  background: var(--fb-19-card);
  border: 1px solid oklch(0.22 0.02 262/.09);
  box-shadow: 0 26px 60px -34px oklch(0.22 0.02 262/.85);
}

.fb-19__rail {
  position: relative;
  display: grid;
  align-content: start;
  gap: 10px;
  padding: 10px;
  border-radius: 20px;
  background: oklch(0.97 0.008 262);
  border: 1px solid oklch(0.22 0.02 262/.07);
}

.fb-19__railBtn {
  display: grid;
  place-items: center;
  width: 48px;
  height: 48px;
  border: 0;
  border-radius: 14px;
  background: transparent;
  color: var(--fb-19-mut);
  cursor: pointer;
  transition: background .16s ease,color .16s ease,transform .16s ease;
}

.fb-19__railBtn svg {
  width: 22px;
  height: 22px;
}

.fb-19__railBtn:hover {
  background: oklch(0.52 0.16 258/.1);
  color: var(--fb-19-brand);
}

.fb-19__railBtn:active {
  transform: scale(.94);
}

.fb-19__railBtn:focus-visible {
  outline: 3px solid var(--fb-19-brand);
  outline-offset: 2px;
}

.fb-19__main {
  display: grid;
  align-content: center;
  gap: 12px;
  justify-items: start;
  padding-right: clamp(0px,8vw,90px);
}

.fb-19__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--fb-19-brand);
}

.fb-19__title {
  font-size: clamp(23px,3.8vw,38px);
  line-height: 1.06;
  letter-spacing: -.03em;
  font-weight: 700;
  text-wrap: balance;
}

.fb-19__sub {
  max-width: 44ch;
  font-size: clamp(13.5px,1.6vw,16px);
  line-height: 1.62;
  color: var(--fb-19-mut);
  text-wrap: pretty;
}

.fb-19__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--fb-19-mut);
  padding: 8px 14px;
  border: 1px solid oklch(0.22 0.02 262/.14);
  border-radius: 99px;
}

.fb-19__dock {
  position: absolute;
  right: clamp(16px,3vw,28px);
  bottom: clamp(16px,3vw,28px);
}

.fb-19__fab {
  anchor-name: --fb-19-anchor;
  display: grid;
  place-items: center;
  inline-size: 60px;
  block-size: 60px;
  border: 0;
  border-radius: 20px;
  cursor: pointer;
  color: oklch(0.99 0.01 258);
  background: linear-gradient(150deg,oklch(0.62 0.17 254),oklch(0.42 0.16 262));
  box-shadow: 0 14px 32px -12px oklch(0.42 0.16 262/.85),0 2px 5px oklch(0.3 0.06 262/.25);
  transition: transform .28s cubic-bezier(.2,1.3,.4,1);
}

.fb-19__fab svg {
  width: 25px;
  height: 25px;
}

.fb-19__fab:hover {
  transform: translateY(-2px);
}

.fb-19__fab:active {
  transform: scale(.94);
}

.fb-19__fab:focus-visible {
  outline: 3px solid oklch(0.42 0.16 262);
  outline-offset: 4px;
}

.fb-19__tip {
  position: absolute;
  z-index: 8;
  display: flex;
  align-items: center;
  gap: 8px;
  white-space: nowrap;
  padding: 8px 12px;
  border-radius: 10px;
  background: var(--fb-19-tip);
  color: oklch(0.98 0.01 262);
  font-size: 12.5px;
  font-weight: 600;
  pointer-events: none;
  opacity: 0;
  box-shadow: 0 8px 22px -10px oklch(0.22 0.02 262/.9);
  right: calc(100% + 12px);
  top: 50%;
  translate: -8px -50%;
  transition: opacity .16s ease .4s,translate .2s cubic-bezier(.2,.9,.3,1) .4s;
}

.fb-19__tip::after {
  content: "";
  position: absolute;
  left: 100%;
  top: 50%;
  translate: -3px -50%;
  width: 8px;
  height: 8px;
  background: var(--fb-19-tip);
  rotate: 45deg;
  border-radius: 1px;
}

.fb-19__tip kbd {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10.5px;
  padding: 2px 6px;
  border-radius: 5px;
  background: oklch(1 0 0/.14);
  border: 1px solid oklch(1 0 0/.16);
}

.fb-19__fab:is(:hover,:focus-visible) + .fb-19__tip,
.fb-19__railBtn:is(:hover,:focus-visible) + .fb-19__tip {
  opacity: 1;
  translate: 0 -50%;
  transition-delay: 0s,0s;
}

.fb-19__tip--rail {
  right: auto;
  left: calc(100% + 12px);
  translate: 8px -50%;
  margin-top: -34px;
}

.fb-19__tip--rail::after {
  left: auto;
  right: 100%;
  translate: 3px -50%;
}

.fb-19__railBtn:is(:hover,:focus-visible) + .fb-19__tip--rail {
  translate: 0 -50%;
}

@supports (anchor-name: --x) {
  .fb-19__tip {
    position-anchor: --fb-19-anchor;
    position-try-fallbacks: flip-inline;
    right: anchor(left);
    top: anchor(center);
    inset-inline-start: auto;
  }
}

@media (max-width: 640px) {
  .fb-19__app {
    grid-template-columns: 1fr;
  }

  .fb-19__rail {
    grid-auto-flow: column;
    justify-content: start;
  }

  .fb-19__tip--rail {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .fb-19 * {
    transition: none !important;
  }
}
```
