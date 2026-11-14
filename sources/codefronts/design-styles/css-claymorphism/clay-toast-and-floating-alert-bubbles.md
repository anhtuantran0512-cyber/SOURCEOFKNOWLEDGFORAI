---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-claymorphism/clay-toast-and-floating-alert-bubbles/"
title: "Clay Toast & Floating Alert Bubbles"
section: "design-styles"
category: "css-claymorphism"
category_name: "CSS Claymorphism"
description: "Four semantic clay toasts — success, info, warning, error — each dismissible in pure CSS, plus a chat-style alert bubble with an asymmetric tail."
has_js: "false"
---

Here's a working CSS Claymorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Clay Toast & Floating Alert Bubbles
Source: https://codefronts.com/design-styles/css-claymorphism/clay-toast-and-floating-alert-bubbles/

Four semantic clay toasts — success, info, warning, error — each dismissible in pure CSS, plus a chat-style alert bubble with an asymmetric tail. Entry is a spring from below with a staggered delay; dismissal collapses the toast's height so the stack closes the gap. Semantics are handled properly: role="status" for the polite ones, role="alert" for the error.
## HTML
```html
<section class="cl-18" aria-label="Clay toast and floating alert bubbles demo">
  <div class="cl-18__stage">
    <div class="cl-18__stack">
      <label class="cl-18__toast" style="--cl-18-h:150;--cl-18-i:0" role="status">
        <span class="cl-18__inner">
          <span class="cl-18__puck" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20"><path d="m5 12.6 4.2 4.2L19 7" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
          <span class="cl-18__text"><b>Snippet copied</b><span>All three shadow layers, ready to paste.</span></span>
          <input type="checkbox" aria-label="Dismiss: snippet copied">
          <span class="cl-18__x" aria-hidden="true"></span>
        </span>
      </label>
      <label class="cl-18__toast" style="--cl-18-h:250;--cl-18-i:1" role="status">
        <span class="cl-18__inner">
          <span class="cl-18__puck" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20"><path d="M12 8.2V8m0 3.4v4.4" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"/><circle cx="12" cy="12" r="8.4" fill="none" stroke="currentColor" stroke-width="2"/></svg></span>
          <span class="cl-18__text"><b>Dark-mode variant available</b><span>Recalibrated shadows in demo 19.</span></span>
          <input type="checkbox" aria-label="Dismiss: dark mode variant available">
          <span class="cl-18__x" aria-hidden="true"></span>
        </span>
      </label>
      <label class="cl-18__toast" style="--cl-18-h:80;--cl-18-i:2" role="status">
        <span class="cl-18__inner">
          <span class="cl-18__puck" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20"><path d="M12 4.6 21 20H3z" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/><path d="M12 10.4v3.4" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg></span>
          <span class="cl-18__text"><b>Contrast is borderline</b><span>Body copy sits at 4.2:1 on this pastel.</span></span>
          <input type="checkbox" aria-label="Dismiss: contrast is borderline">
          <span class="cl-18__x" aria-hidden="true"></span>
        </span>
      </label>
      <label class="cl-18__toast" style="--cl-18-h:25;--cl-18-i:3" role="alert">
        <span class="cl-18__inner">
          <span class="cl-18__puck" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20"><path d="M7.5 7.5l9 9m0-9-9 9" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"/></svg></span>
          <span class="cl-18__text"><b>Publish failed</b><span>Two snippets are missing a reduced-motion block.</span></span>
          <input type="checkbox" aria-label="Dismiss: publish failed">
          <span class="cl-18__x" aria-hidden="true"></span>
        </span>
      </label>
    </div>
    <div class="cl-18__bubbleWrap">
      <span class="cl-18__avatar" aria-hidden="true">AR</span>
      <p class="cl-18__bubble">Shipped the clay tokens — every component reads from <code>--shadow-clay</code> now.</p>
    </div>
    <p class="cl-18__chip" aria-hidden="true">tier 4 · spring entry with index stagger · grid-template-rows 0fr collapse</p>
  </div>
</section>
```
## CSS
```css
.cl-18,
.cl-18 *,
.cl-18 *::before,
.cl-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cl-18 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--cl-18-bg);
  --cl-18-bg: oklch(0.93 0.022 260);
  --cl-18-shade: oklch(0.55 0.06 260/.45);
  --cl-18-light: oklch(1 0.01 260/.95);
  --cl-18-ink: oklch(0.27 0.04 260);
  --cl-18-mut: oklch(0.5 0.03 260);
  font-family: system-ui,-apple-system,'Segoe UI',sans-serif;
  color: var(--cl-18-ink);
}

.cl-18__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(20px,3.5vw,32px);
  padding: clamp(20px,5vw,56px);
  background: radial-gradient(80% 55% at 50% 0%,oklch(0.97 0.02 260),transparent 66%);
}

.cl-18__stack {
  display: grid;
  gap: 12px;
  width: min(100%,440px);
}

.cl-18__toast {
  --cl-18-h: 150;
  display: grid;
  grid-template-rows: 1fr;
  overflow: hidden;
  border-radius: 30px;
  cursor: default;
  background: oklch(0.9 0.06 var(--cl-18-h));
  box-shadow: 0 30px 50px -18px oklch(0.5 0.11 var(--cl-18-h)/.5),inset 0 -14px 24px -12px oklch(0.5 0.11 var(--cl-18-h)/.5),inset 0 16px 24px -8px oklch(1 0.02 var(--cl-18-h)/.95);
  animation: cl-18-rise .55s cubic-bezier(.34,1.5,.5,1) backwards;
  animation-delay: calc(var(--cl-18-i) * 90ms);
  transition: grid-template-rows .38s cubic-bezier(.4,0,.2,1),opacity .34s,scale .38s cubic-bezier(.4,0,.2,1),margin .38s,box-shadow .34s;
}

@keyframes cl-18-rise {
  from {
    opacity: 0;
    translate: 0 26px;
    scale: .94;
  }

  to {
    opacity: 1;
    translate: 0;
    scale: 1;
  }
}

.cl-18__inner {
  display: flex;
  align-items: center;
  gap: 14px;
  min-height: 74px;
  padding: 16px 18px;
  overflow: hidden;
  transition: min-height .38s cubic-bezier(.4,0,.2,1),padding-block .38s cubic-bezier(.4,0,.2,1);
}

.cl-18__puck {
  flex: none;
  display: grid;
  place-items: center;
  width: 42px;
  height: 42px;
  border-radius: 16px;
  color: oklch(0.34 0.13 var(--cl-18-h));
  background: oklch(0.86 0.09 var(--cl-18-h));
  box-shadow: inset 0 9px 15px -6px oklch(0.5 0.12 var(--cl-18-h)/.6),inset 0 -6px 12px -8px oklch(1 0.02 var(--cl-18-h)/.9);
}

.cl-18__text {
  flex: 1;
  min-width: 0;
  display: grid;
  gap: 3px;
}

.cl-18__text b {
  font-size: 14.5px;
  font-weight: 700;
  letter-spacing: -.01em;
  color: oklch(0.28 0.09 var(--cl-18-h));
}

.cl-18__text span {
  font-size: 12.5px;
  line-height: 1.45;
  color: oklch(0.38 0.07 var(--cl-18-h));
  text-wrap: pretty;
}

.cl-18__toast input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.cl-18__x {
  position: relative;
  flex: none;
  width: 34px;
  height: 34px;
  border-radius: 12px;
  cursor: pointer;
  background: oklch(0.94 0.03 var(--cl-18-h)/.7);
  box-shadow: 0 6px 11px -6px oklch(0.5 0.11 var(--cl-18-h)/.5),inset 0 -5px 9px -6px oklch(0.5 0.11 var(--cl-18-h)/.4),inset 0 6px 9px -5px oklch(1 0.02 var(--cl-18-h));
}

.cl-18__x::before,
.cl-18__x::after {
  content: '';
  position: absolute;
  left: 10px;
  top: 16px;
  width: 14px;
  height: 2.4px;
  border-radius: 2px;
  background: oklch(0.4 0.09 var(--cl-18-h));
}

.cl-18__x::before {
  rotate: 45deg;
}

.cl-18__x::after {
  rotate: -45deg;
}

.cl-18__toast:has(input:focus-visible) .cl-18__x {
  outline: 3px solid oklch(0.32 0.1 var(--cl-18-h));
  outline-offset: 3px;
}

.cl-18__toast:has(input:checked) {
  grid-template-rows: 0fr;
  opacity: 0;
  scale: .92;
  margin-block-end: -12px;
  pointer-events: none;
  box-shadow: none;
}

.cl-18__toast:has(input:checked) .cl-18__inner {
  min-height: 0;
  padding-block: 0;
}

.cl-18__bubbleWrap {
  display: flex;
  align-items: flex-end;
  gap: 12px;
  width: min(100%,440px);
}

.cl-18__avatar {
  flex: none;
  display: grid;
  place-items: center;
  width: 44px;
  height: 44px;
  border-radius: 50%;
  font-size: 13px;
  font-weight: 700;
  background: oklch(0.86 0.09 300);
  box-shadow: 0 12px 20px -10px var(--cl-18-shade),inset 0 -8px 13px -8px oklch(0.5 0.1 300/.5),inset 0 10px 13px -6px var(--cl-18-light);
}

.cl-18__bubble {
  flex: 1;
  padding: 16px 20px;
  border-radius: 32px 32px 32px 10px;
  font-size: 14px;
  line-height: 1.55;
  background: oklch(0.92 0.04 260);
  box-shadow: 0 22px 38px -16px var(--cl-18-shade),inset 0 -13px 22px -12px oklch(0.5 0.08 260/.45),inset 0 15px 22px -8px var(--cl-18-light);
  text-wrap: pretty;
}

.cl-18__bubble code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12.5px;
  padding: 2px 7px;
  border-radius: 8px;
  background: oklch(1 0 0/.55);
  box-shadow: inset 0 3px 5px -3px var(--cl-18-shade);
}

.cl-18__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--cl-18-mut);
  padding: 9px 16px;
  border-radius: 99px;
  text-align: center;
  background: oklch(1 0 0/.6);
  box-shadow: inset 0 -4px 10px -8px var(--cl-18-shade),inset 0 6px 10px -6px oklch(1 0 0);
}

@media (prefers-reduced-motion: reduce) {
  .cl-18__toast {
    animation: none;
  }

  .cl-18 * {
    transition-duration: .01ms !important;
  }
}
```
