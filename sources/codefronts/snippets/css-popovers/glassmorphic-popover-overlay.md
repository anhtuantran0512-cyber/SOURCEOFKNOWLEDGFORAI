---
source: "codefronts"
url: "https://codefronts.com/snippets/css-popovers/glassmorphic-popover-overlay/"
title: "Glassmorphic Popover Overlay"
section: "snippets"
category: "css-popovers"
category_name: "CSS Popovers"
description: "A frosted panel over a rich background, with the solid fallback declared first so an unsupporting engine gets an opaque card rather than unreadable text."
has_js: "false"
---

Here's a working CSS Popover from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphic Popover Overlay
Source: https://codefronts.com/snippets/css-popovers/glassmorphic-popover-overlay/

A frosted panel over a rich background, with the solid fallback declared first so an unsupporting engine gets an opaque card rather than unreadable text. The top-layer wrinkle is the interesting part: a popover samples what is painted beneath it, so the same panel can blur differently in the top layer than it does inline.
## HTML
```html
<div class="pop-18">
  <div class="pop-18__stage">
    <div class="pop-18__hero">
      <p class="pop-18__kicker">Now playing</p>
      <h2 class="pop-18__h">Wickfield No. 5</h2>
      <p class="pop-18__sub">Marisa Ault · Slow Water · 2026</p>
      <button class="pop-18__icon" type="button" popovertarget="pop-18-panel" aria-label="Track details">
        <svg viewBox="0 0 22 22" width="19" height="19" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><circle cx="11" cy="11" r="8"/><path d="M11 10v5.4M11 7.2v.9"/></svg>
      </button>
      <p class="pop-18__foot">Open the panel: it blurs the top layer's view of this page, not a mocked-up copy of it.</p>
    </div>
  </div>

  <div class="pop-18__panel" popover="auto" id="pop-18-panel" role="group" aria-label="Track details">
    <p class="pop-18__ptitle">Track details</p>
    <dl class="pop-18__dl">
      <div class="pop-18__drow"><dt class="pop-18__dt">Length</dt><dd class="pop-18__dd">6:41</dd></div>
      <div class="pop-18__drow"><dt class="pop-18__dt">Key</dt><dd class="pop-18__dd">D minor</dd></div>
      <div class="pop-18__drow"><dt class="pop-18__dt">Mastered</dt><dd class="pop-18__dd">Alex Chen</dd></div>
    </dl>
    <p class="pop-18__pfoot">Opaque fallback first, frost second.</p>
  </div>
</div>
```
## CSS
```css
.pop-18 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --ink: #f4f1ff;
  --muted: #b8b0d8;
  --glass-solid: #241d3c;
  --rim: rgba(255, 255, 255, 0.34);
  --font-ui: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
  color: var(--ink);
  font-family: var(--font-ui);
  padding: 40px 18px;
  background: radial-gradient(46rem 30rem at 12% 8%, #4a2a7a 0%, transparent 62%), radial-gradient(38rem 26rem at 88% 22%, #0f5f75 0%, transparent 60%), radial-gradient(34rem 28rem at 62% 92%, #a8324f 0%, transparent 58%), #100c1c;
}

.pop-18__stage {
  display: grid;
  place-items: center;
  max-inline-size: 100%;
  min-height: calc(100vh - 80px);
}

.pop-18__hero {
  inline-size: 100%;
  max-inline-size: 28rem;
  min-inline-size: 0;
  text-align: start;
}

.pop-18__kicker {
  margin: 0 0 10px;
  font: 700 10px/1 var(--font-ui);
  letter-spacing: 0.24em;
  text-transform: uppercase;
  color: var(--muted);
}

.pop-18__h {
  margin: 0 0 6px;
  font: 600 clamp(30px, 8vw, 48px)/1.05 var(--font-ui);
  letter-spacing: -0.03em;
}

.pop-18__sub {
  margin: 0 0 22px;
  font-size: 14px;
  color: var(--muted);
}

.pop-18__icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 44px;
  min-height: 44px;
  color: var(--ink);
  background: rgba(255, 255, 255, 0.12);
  border: 1px solid var(--rim);
  border-radius: 999px;
  cursor: pointer;
  anchor-name: --pop-18-anchor;
}

.pop-18__icon:focus-visible {
  outline: 3px solid var(--ink);
  outline-offset: 3px;
}

.pop-18__foot {
  margin: 20px 0 0;
  max-inline-size: 24rem;
  font-size: 12.5px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.pop-18__panel {
  position: fixed;
  margin: 0;
  inline-size: min(18rem, calc(100vw - 28px));
  max-inline-size: calc(100vw - 28px);
  padding: 18px;
  color: var(--ink);
  background: var(--glass-solid);
  border: 1px solid var(--rim);
  border-radius: 20px;
  box-shadow: 0 26px 60px -28px rgba(0, 0, 0, 0.8), inset 0 1px 0 rgba(255, 255, 255, 0.22);
  opacity: 0;
  transform: translateY(6px);
  transition: opacity 200ms ease, transform 240ms cubic-bezier(0.2, 0.9, 0.25, 1), display 240ms allow-discrete, overlay 240ms allow-discrete;
}

.pop-18__panel:popover-open {
  opacity: 1;
  transform: translateY(0);
}

@starting-style {
  .pop-18__panel:popover-open {
    opacity: 0;
    transform: translateY(6px);
  }
}

@supports (backdrop-filter: blur(1px)) {
  .pop-18__panel {
    background: rgba(36, 29, 60, 0.55);
    backdrop-filter: blur(18px) saturate(150%);
  }
}

@supports (background: color-mix(in oklab, white 50%, transparent)) {
  @supports (backdrop-filter: blur(1px)) {
    .pop-18__panel {
      background: color-mix(in oklab, #241d3c 58%, transparent);
    }
  }
}

@supports (anchor-name: --a) {
  .pop-18__panel {
    position-anchor: --pop-18-anchor;
    position-area: block-end span-inline-end;
    inset: auto;
    margin-block-start: 10px;
    position-try-fallbacks: flip-block, flip-inline;
  }
}

.pop-18__ptitle {
  margin: 0 0 12px;
  font: 700 10px/1 var(--font-ui);
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--muted);
}

.pop-18__dl {
  margin: 0;
  display: grid;
  gap: 8px;
}

.pop-18__drow {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  min-inline-size: 0;
}

.pop-18__dt {
  margin: 0;
  font-size: 12.5px;
  color: var(--muted);
}

.pop-18__dd {
  margin: 0;
  font-size: 12.5px;
  font-weight: 650;
}

.pop-18__pfoot {
  margin: 14px 0 0;
  padding-block-start: 11px;
  border-block-start: 1px solid rgba(255, 255, 255, 0.16);
  font-size: 11.5px;
  color: var(--muted);
}

@media (prefers-reduced-motion: reduce) {
  .pop-18__panel {
    transition: none;
    opacity: 1;
    transform: none;
  }

  @starting-style {
    .pop-18__panel:popover-open {
      opacity: 1;
      transform: none;
    }
  }
}

@media (prefers-color-scheme: light) {
  .pop-18 {
    --ink: #17122a;
    --muted: #56507a;
    --glass-solid: #ffffff;
    --rim: rgba(23, 18, 42, 0.16);
    background: radial-gradient(46rem 30rem at 12% 8%, #d9c8f5 0%, transparent 62%), radial-gradient(38rem 26rem at 88% 22%, #bfe6ef 0%, transparent 60%), radial-gradient(34rem 28rem at 62% 92%, #f7cdd6 0%, transparent 58%), #f4f1fa;
  }

  .pop-18__icon {
    background: rgba(255, 255, 255, 0.6);
  }

  .pop-18__panel {
    box-shadow: 0 24px 52px -30px rgba(23, 18, 42, 0.45), inset 0 1px 0 rgba(255, 255, 255, 0.7);
  }

  .pop-18__pfoot {
    border-block-start-color: rgba(23, 18, 42, 0.14);
  }

  @supports (backdrop-filter: blur(1px)) {
    .pop-18__panel {
      background: rgba(255, 255, 255, 0.62);
    }
  }
}

[data-theme="dark"] .pop-18 {
  --ink: #f4f1ff;
  --muted: #b8b0d8;
  --glass-solid: #241d3c;
  --rim: rgba(255, 255, 255, 0.34);
}
```
