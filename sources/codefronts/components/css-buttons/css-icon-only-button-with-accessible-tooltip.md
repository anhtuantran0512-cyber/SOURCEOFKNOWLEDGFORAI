---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-icon-only-button-with-accessible-tooltip/"
title: "CSS Icon-Only Button with Accessible Tooltip"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "A three-button icon toolbar where each control carries a real accessible name, a 44px touch target inside a 40px visual square, and a tooltip that appears on…"
has_js: "false"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Icon-Only Button with Accessible Tooltip
Source: https://codefronts.com/components/css-buttons/css-icon-only-button-with-accessible-tooltip/

A three-button icon toolbar where each control carries a real accessible name, a 44px touch target inside a 40px visual square, and a tooltip that appears on hover and keyboard focus. The tooltip animates in with @starting-style and is positioned with CSS anchor positioning, falling back to a plain absolute offset.
## HTML
```html
<div class="cb-04">
  <div class="cb-04__stage">
    <div class="cb-04__bar" role="toolbar" aria-label="Article actions">
      <span class="cb-04__item">
        <button class="cb-04__btn" type="button" aria-label="Share article" aria-describedby="cb-04-t1" style="anchor-name:--cb-04-a1">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="18" cy="5" r="2.6"/><circle cx="6" cy="12" r="2.6"/><circle cx="18" cy="19" r="2.6"/><path d="M8.4 10.8 15.6 6.6M8.4 13.2l7.2 4.2"/></svg>
        </button>
        <span class="cb-04__tip" role="tooltip" id="cb-04-t1" style="position-anchor:--cb-04-a1">Share</span>
      </span>
      <span class="cb-04__item">
        <button class="cb-04__btn" type="button" aria-label="Bookmark article" aria-describedby="cb-04-t2" style="anchor-name:--cb-04-a2" aria-pressed="false">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M7 4h10a1 1 0 0 1 1 1v15l-6-4-6 4V5a1 1 0 0 1 1-1z"/></svg>
        </button>
        <span class="cb-04__tip" role="tooltip" id="cb-04-t2" style="position-anchor:--cb-04-a2">Save for later</span>
      </span>
      <span class="cb-04__item">
        <button class="cb-04__btn" type="button" aria-label="Copy link" aria-describedby="cb-04-t3" style="anchor-name:--cb-04-a3">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M10 14a4 4 0 0 0 5.66 0l2.5-2.5A4 4 0 0 0 12.5 5.84L11 7.3"/><path d="M14 10a4 4 0 0 0-5.66 0l-2.5 2.5A4 4 0 0 0 11.5 18.16L13 16.7"/></svg>
        </button>
        <span class="cb-04__tip" role="tooltip" id="cb-04-t3" style="position-anchor:--cb-04-a3">Copy link</span>
      </span>
      <span class="cb-04__item">
        <button class="cb-04__btn cb-04__btn--danger" type="button" aria-label="Report article" aria-describedby="cb-04-t4" style="anchor-name:--cb-04-a4">
          <svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 4v11M12 19h.01"/><path d="M12 4 3.5 19h17L12 4z"/></svg>
        </button>
        <span class="cb-04__tip" role="tooltip" id="cb-04-t4" style="position-anchor:--cb-04-a4">Report</span>
      </span>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&display=swap');

.cb-04 {
  --bg: #f4f4f2;
  --surface: #ffffff;
  --text: #18181b;
  --muted: #6b6b74;
  --line: #e2e2dd;
  --accent: #2563eb;
  --danger: #dc2626;
  --tip-bg: #18181b;
  --tip-ink: #fafafa;
  --size: 2.5rem;
  --sans: "Manrope",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--text);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(50% 0 0)) {
  .cb-04 {
    --bg: oklch(96.8% .004 100);
    --accent: oklch(53% .21 262);
    --danger: oklch(55% .21 27);
  }
}

@media (prefers-color-scheme: dark) {
  .cb-04:not([data-theme="light"]) {
    --bg: #0b0b0d;
    --surface: #16161a;
    --text: #f2f2f5;
    --muted: #9c9ca6;
    --line: #2a2a31;
    --tip-bg: #f4f4f6;
    --tip-ink: #101014;
    --accent: #7aa2ff;
    --danger: #f87171;
  }
}

.cb-04[data-theme="dark"] {
  --bg: #0b0b0d;
  --surface: #16161a;
  --text: #f2f2f5;
  --muted: #9c9ca6;
  --line: #2a2a31;
  --tip-bg: #f4f4f6;
  --tip-ink: #101014;
  --accent: #7aa2ff;
  --danger: #f87171;
}

.cb-04,
.cb-04 *,
.cb-04 *::before,
.cb-04 *::after {
  box-sizing: border-box;
}

.cb-04__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-04__bar {
  display: flex;
  align-items: center;
  gap: .35rem;
  padding: .4rem;
  border-radius: 999px;
  background: var(--surface);
  border: 1px solid var(--line);
  box-shadow: 0 12px 30px -18px color-mix(in oklab,var(--text) 55%,transparent);
}

.cb-04__item {
  position: relative;
  display: inline-flex;
}

.cb-04__btn {
  position: relative;
  cursor: pointer;
  display: grid;
  place-items: center;
  width: var(--size);
  height: var(--size);
  border: 0;
  border-radius: 50%;
  color: var(--muted);
  background: transparent;
  transition: background-color .18s ease, color .18s ease, scale .2s cubic-bezier(.16,1,.3,1);
}

.cb-04__btn::after {
  content: '';
  position: absolute;
  inset: -.35rem;
  border-radius: 50%;
}

.cb-04__btn svg {
  width: 1.15rem;
  height: 1.15rem;
}

.cb-04__btn:hover {
  color: var(--accent);
  background: color-mix(in oklab,var(--accent) 12%,transparent);
  scale: 1.06;
}

.cb-04__btn--danger:hover {
  color: var(--danger);
  background: color-mix(in oklab,var(--danger) 12%,transparent);
}

.cb-04__btn:active {
  scale: .94;
}

.cb-04__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
  color: var(--accent);
}

.cb-04__btn[aria-pressed="true"] {
  color: var(--accent);
  background: color-mix(in oklab,var(--accent) 16%,transparent);
}

.cb-04__tip {
  position: absolute;
  left: 50%;
  bottom: calc(100% + .6rem);
  translate: -50% 4px;
  display: none;
  opacity: 0;
  z-index: 3;
  pointer-events: none;
  white-space: nowrap;
  padding: .35rem .6rem;
  border-radius: .4rem;
  font-size: .75rem;
  font-weight: 600;
  letter-spacing: .01em;
  color: var(--tip-ink);
  background: var(--tip-bg);
  transition: opacity .18s ease, translate .18s cubic-bezier(.16,1,.3,1);
}

.cb-04__tip::after {
  content: '';
  position: absolute;
  top: 100%;
  left: 50%;
  translate: -50% -1px;
  border: .3rem solid transparent;
  border-top-color: var(--tip-bg);
}

@supports (transition-behavior: allow-discrete) {
  .cb-04__tip {
    transition: opacity .18s ease, translate .18s cubic-bezier(.16,1,.3,1), display .18s allow-discrete;
  }
}

.cb-04__item:is(:hover,:has(:focus-visible)) .cb-04__tip {
  display: block;
  opacity: 1;
  translate: -50% 0;
}

@supports (animation-timeline: view()) {
  .cb-04__item:is(:hover,:has(:focus-visible)) .cb-04__tip {
    @starting-style {
      opacity: 0;
      translate: -50% 4px;
    }
  }
}
/* Each button carries its OWN anchor-name (inline, --cb-04-a1…a4) and each tooltip
   points at it with position-anchor. One shared anchor-name here would tether every
   tooltip to the same button — the classic anchor-positioning bug. */

@supports (anchor-name: --a) {
  .cb-04__tip {
    position: fixed;
    position-area: block-start;
    justify-self: anchor-center;
    margin-bottom: .6rem;
    left: auto;
    bottom: auto;
    translate: 0 4px;
  }

  .cb-04__item:is(:hover,:has(:focus-visible)) .cb-04__tip {
    translate: 0 0;
  }

  .cb-04__tip::after {
    left: 50%;
    translate: -50% -1px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cb-04__btn,
    .cb-04__tip {
    transition: none;
  }
}

@media (forced-colors: active) {
  .cb-04__bar,
    .cb-04__btn {
    border: 1px solid ButtonText;
  }

  .cb-04__tip {
    background: Canvas;
    color: CanvasText;
    border: 1px solid CanvasText;
  }
}
```
