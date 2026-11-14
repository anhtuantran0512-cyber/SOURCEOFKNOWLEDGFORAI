---
source: "codefronts"
url: "https://codefronts.com/components/css-floating-buttons/whatsapp-floating-message-button-css/"
title: "WhatsApp Floating Message Button CSS"
section: "components"
category: "css-floating-buttons"
category_name: "CSS Floating Buttons"
description: "The green \"message us\" button every small-business site puts in the bottom-right corner, done properly: a resting circle that expands into a labelled pill on…"
has_js: "false"
---

Here's a working CSS Floating Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: WhatsApp Floating Message Button CSS
Source: https://codefronts.com/components/css-floating-buttons/whatsapp-floating-message-button-css/

The green "message us" button every small-business site puts in the bottom-right corner, done properly: a resting circle that expands into a labelled pill on hover and focus, an attention pulse that runs three times and then stops, and an online/away status dot. The label is real text inside the button, so it is announced, translatable and searchable — not a tooltip bolted on with a data-attribute.
## HTML
```html
<section class="fb-03" aria-label="Floating message button demo">
  <div class="fb-03__page">
    <div class="fb-03__hero">
      <p class="fb-03__eyebrow">grid-template-columns 0fr → 1fr</p>
      <h2 class="fb-03__title">A circle that becomes a sentence</h2>
      <p class="fb-03__sub">Hover or tab to the button. The label is real text inside the same element, so the accessible name never changes as it expands.</p>
      <p class="fb-03__chip">3-cycle pulse · intrinsic width · status dot</p>
    </div>
    <div class="fb-03__cards" aria-hidden="true">
      <div class="fb-03__card"></div><div class="fb-03__card"></div><div class="fb-03__card"></div>
    </div>
  </div>
  <button class="fb-03__msg" type="button">
    <span class="fb-03__ico">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 5.6A2.4 2.4 0 0 1 6.4 3.2h11.2A2.4 2.4 0 0 1 20 5.6v7.2a2.4 2.4 0 0 1-2.4 2.4h-6.24l-4.02 3.2A.6.6 0 0 1 6.4 17.9v-2.7H6.4A2.4 2.4 0 0 1 4 12.8V5.6z" fill="currentColor"/><circle cx="9" cy="9.2" r="1.05" fill="var(--fb-03-brand)"/><circle cx="12" cy="9.2" r="1.05" fill="var(--fb-03-brand)"/><circle cx="15" cy="9.2" r="1.05" fill="var(--fb-03-brand)"/></svg>
      <span class="fb-03__status" aria-hidden="true"></span>
    </span>
    <span class="fb-03__label"><b>Message us</b><i>Typically replies in 5 min</i></span>
  </button>
</section>
```
## CSS
```css
.fb-03 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--fb-03-bg);
  --fb-03-bg: oklch(0.97 0.012 150);
  --fb-03-brand: oklch(0.62 0.16 152);
  --fb-03-brandDeep: oklch(0.5 0.14 152);
  --fb-03-ink: oklch(0.24 0.03 160);
  --fb-03-mut: oklch(0.54 0.02 160);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--fb-03-ink);
  position: relative;
  display: grid;
  place-items: center;
  padding: clamp(20px,5vw,56px);
  overflow: hidden;
}

.fb-03 *,
.fb-03 *::before,
.fb-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fb-03__page {
  width: min(100%,660px);
  display: grid;
  gap: clamp(20px,4vw,34px);
  justify-items: center;
  text-align: center;
}

.fb-03__hero {
  display: grid;
  gap: 11px;
  justify-items: center;
}

.fb-03__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--fb-03-brandDeep);
}

.fb-03__title {
  font-size: clamp(26px,4.6vw,44px);
  line-height: 1.05;
  letter-spacing: -.03em;
  font-weight: 700;
  text-wrap: balance;
}

.fb-03__sub {
  max-width: 50ch;
  font-size: clamp(13.5px,1.7vw,16.5px);
  line-height: 1.62;
  color: var(--fb-03-mut);
  text-wrap: pretty;
}

.fb-03__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--fb-03-mut);
  padding: 8px 14px;
  border: 1px solid oklch(0.24 0.03 160/.14);
  border-radius: 99px;
}

.fb-03__cards {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 14px;
  width: 100%;
}

.fb-03__card {
  height: clamp(72px,12vw,104px);
  border-radius: 16px;
  background: oklch(1 0 0);
  border: 1px solid oklch(0.24 0.03 160/.09);
  box-shadow: 0 10px 26px -20px oklch(0.24 0.03 160/.6);
}

.fb-03__card:nth-child(2) {
  background: linear-gradient(120deg,oklch(0.93 0.04 152),oklch(0.98 0.01 152));
}

.fb-03__msg {
  position: absolute;
  right: clamp(16px,3vw,30px);
  bottom: calc(clamp(16px,3vw,30px) + env(safe-area-inset-bottom));
  z-index: 5;
  display: grid;
  grid-template-columns: auto 0fr;
  align-items: center;
  gap: 0;
  min-height: 60px;
  padding: 8px;
  border: 0;
  border-radius: 99px;
  background: linear-gradient(180deg,var(--fb-03-brand),var(--fb-03-brandDeep));
  color: oklch(0.99 0.01 152);
  cursor: pointer;
  text-align: left;
  box-shadow: 0 8px 26px -8px oklch(0.5 0.14 152/.7),0 2px 6px oklch(0.3 0.06 152/.25);
  transition: grid-template-columns .34s cubic-bezier(.2,.8,.2,1),gap .34s cubic-bezier(.2,.8,.2,1),box-shadow .3s ease,transform .2s ease;
}

.fb-03__msg:is(:hover,:focus-visible) {
  grid-template-columns: auto 1fr;
  gap: 12px;
  box-shadow: 0 14px 34px -8px oklch(0.5 0.14 152/.75);
}

.fb-03__msg:focus-visible {
  outline: 3px solid var(--fb-03-brandDeep);
  outline-offset: 3px;
}

.fb-03__msg:active {
  transform: scale(.97);
}

.fb-03__ico {
  position: relative;
  flex: none;
  width: 44px;
  height: 44px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  background: oklch(1 0 0/.16);
}

.fb-03__ico svg {
  width: 26px;
  height: 26px;
}

.fb-03__ico::after {
  content: "";
  position: absolute;
  inset: -9px;
  border-radius: 50%;
  border: 2px solid oklch(1 0 0/.55);
  animation: fb-03-pulse 2.1s ease-out 3;
  pointer-events: none;
}

.fb-03__msg:hover .fb-03__ico::after {
  animation: fb-03-pulse 2.1s ease-out 3;
}

@keyframes fb-03-pulse {
  0% {
    transform: scale(.86);
    opacity: .8;
  }

  70% {
    transform: scale(1.35);
    opacity: 0;
  }

  100% {
    transform: scale(1.35);
    opacity: 0;
  }
}

.fb-03__status {
  position: absolute;
  right: 1px;
  bottom: 1px;
  width: 11px;
  height: 11px;
  border-radius: 50%;
  background: oklch(0.85 0.19 130);
  box-shadow: 0 0 0 2.5px var(--fb-03-brandDeep);
}

.fb-03__label {
  overflow: hidden;
  white-space: nowrap;
  display: grid;
  gap: 1px;
  min-width: 0;
}

.fb-03__msg:is(:hover,:focus-visible) .fb-03__label {
  padding-right: 6px;
}

.fb-03__label b {
  font-size: 15px;
  font-weight: 650;
  letter-spacing: -.01em;
}

.fb-03__label i {
  font-style: normal;
  font-size: 11.5px;
  color: oklch(0.97 0.02 152/.82);
}

@media (prefers-reduced-motion: reduce) {
  .fb-03__msg {
    transition: none;
  }

  .fb-03__ico::after {
    animation: none;
    opacity: 0;
  }
}
```
