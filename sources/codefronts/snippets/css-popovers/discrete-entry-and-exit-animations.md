---
source: "codefronts"
url: "https://codefronts.com/snippets/css-popovers/discrete-entry-and-exit-animations/"
title: "Discrete Entry and Exit Animations"
section: "snippets"
category: "css-popovers"
category_name: "CSS Popovers"
description: "Animating a popover takes three declarations and almost everyone ships two of them."
has_js: "false"
---

Here's a working CSS Popover from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Discrete Entry and Exit Animations
Source: https://codefronts.com/snippets/css-popovers/discrete-entry-and-exit-animations/

Animating a popover takes three declarations and almost everyone ships two of them. @starting-style supplies the entry values, transition-behavior: allow-discrete lets display animate, and transitioning overlay keeps the element in the top layer while it leaves. Skip the third and the panel drops out of the top layer mid-exit and appears to teleport behind the page.
## HTML
```html
<div class="pop-04">
  <div class="pop-04__stage">
    <div class="pop-04__console">
      <div class="pop-04__row">
        <span class="pop-04__dot" aria-hidden="true"></span>
        <p class="pop-04__label">Build 4821 · main</p>
        <button class="pop-04__icon" type="button" popovertarget="pop-04-panel" aria-label="Build details">
          <svg viewBox="0 0 20 20" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><circle cx="10" cy="10" r="7.2"/><path d="M10 9v5M10 6.4v.7"/></svg>
        </button>
      </div>
      <p class="pop-04__meta">passed in 2m 41s · 318 tests</p>
      <ol class="pop-04__recipe">
        <li class="pop-04__step"><span class="pop-04__num">1</span> @starting-style holds the entry values</li>
        <li class="pop-04__step"><span class="pop-04__num">2</span> allow-discrete lets display join in</li>
        <li class="pop-04__step"><span class="pop-04__num">3</span> overlay keeps it in the top layer while it leaves</li>
      </ol>
    </div>
  </div>

  <div class="pop-04__panel" popover="auto" id="pop-04-panel" role="group" aria-label="Build details">
    <p class="pop-04__ptitle">Stage timings</p>
    <ul class="pop-04__list">
      <li class="pop-04__item"><span>install</span><span class="pop-04__t">18s</span></li>
      <li class="pop-04__item"><span>typecheck</span><span class="pop-04__t">41s</span></li>
      <li class="pop-04__item"><span>unit</span><span class="pop-04__t">1m 06s</span></li>
      <li class="pop-04__item"><span>bundle</span><span class="pop-04__t">36s</span></li>
    </ul>
    <p class="pop-04__pfoot">Close me and watch the exit stay on top.</p>
  </div>
</div>
```
## CSS
```css
.pop-04 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --void: #000000;
  --surface: #0b0b0d;
  --ink: #f4f7f4;
  --muted: #83887f;
  --rule: #1e2022;
  --glow: #c3f53c;
  --radius: 16px;
  --font-ui: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
  --font-mono: ui-monospace, "SFMono-Regular", Menlo, monospace;
  background: var(--void);
  color: var(--ink);
  font-family: var(--font-ui);
  padding: 40px 18px;
}

.pop-04__stage {
  display: grid;
  place-items: center;
  max-inline-size: 100%;
  min-height: calc(100vh - 80px);
}

.pop-04__console {
  inline-size: 100%;
  max-inline-size: 27rem;
  min-inline-size: 0;
  background: var(--surface);
  border: 1px solid var(--rule);
  border-radius: var(--radius);
  padding: 18px 18px 16px;
}

.pop-04__row {
  display: flex;
  align-items: center;
  gap: 10px;
  min-inline-size: 0;
}

.pop-04__dot {
  flex: none;
  inline-size: 9px;
  block-size: 9px;
  border-radius: 50%;
  background: var(--glow);
  box-shadow: 0 0 12px var(--glow);
}

.pop-04__label {
  flex: 1 1 auto;
  min-inline-size: 0;
  margin: 0;
  font: 650 13.5px/1.3 var(--font-mono);
}

.pop-04__icon {
  flex: none;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 44px;
  min-height: 44px;
  color: var(--glow);
  background: transparent;
  border: 1px solid var(--rule);
  border-radius: 999px;
  cursor: pointer;
  anchor-name: --pop-04-anchor;
}

.pop-04__icon:focus-visible {
  outline: 3px solid var(--glow);
  outline-offset: 2px;
}

.pop-04__meta {
  margin: 8px 0 18px;
  font: 400 12px/1.5 var(--font-mono);
  color: var(--muted);
}

.pop-04__recipe {
  margin: 0;
  padding: 16px 0 0;
  list-style: none;
  display: grid;
  gap: 10px;
  border-block-start: 1px solid var(--rule);
  counter-reset: none;
}

.pop-04__step {
  display: flex;
  gap: 10px;
  align-items: flex-start;
  font-size: 12.5px;
  line-height: 1.5;
  color: var(--muted);
  min-inline-size: 0;
}

.pop-04__num {
  flex: none;
  display: grid;
  place-items: center;
  inline-size: 20px;
  block-size: 20px;
  border-radius: 6px;
  font: 700 11px/1 var(--font-mono);
  color: var(--void);
  background: var(--glow);
}

.pop-04__panel {
  position: fixed;
  margin: 0;
  inline-size: min(17rem, calc(100vw - 32px));
  max-inline-size: calc(100vw - 32px);
  padding: 16px;
  color: var(--ink);
  background: var(--surface);
  border: 1px solid var(--glow);
  border-radius: var(--radius);
  box-shadow: 0 0 0 1px rgba(195, 245, 60, 0.15), 0 24px 60px -20px rgba(195, 245, 60, 0.35);
}

@supports (anchor-name: --a) {
  .pop-04__panel {
    position-anchor: --pop-04-anchor;
    position-area: block-end span-inline-start;
    inset: auto;
    margin-block-start: 10px;
    position-try-fallbacks: flip-block;
  }
}

.pop-04__panel {
  opacity: 0;
  transform: translateY(-8px) scale(0.97);
  transition: opacity 200ms ease, transform 240ms cubic-bezier(0.2, 0.9, 0.25, 1), display 240ms allow-discrete, overlay 240ms allow-discrete;
}

.pop-04__panel:popover-open {
  opacity: 1;
  transform: translateY(0) scale(1);
}

@starting-style {
  .pop-04__panel:popover-open {
    opacity: 0;
    transform: translateY(-8px) scale(0.97);
  }
}

.pop-04__ptitle {
  margin: 0 0 12px;
  font: 700 10px/1 var(--font-ui);
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--glow);
}

.pop-04__list {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 8px;
}

.pop-04__item {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  font: 400 12.5px/1.4 var(--font-mono);
  color: var(--muted);
  min-inline-size: 0;
}

.pop-04__t {
  color: var(--ink);
  font-variant-numeric: tabular-nums;
}

.pop-04__pfoot {
  margin: 14px 0 0;
  padding-block-start: 12px;
  border-block-start: 1px solid var(--rule);
  font-size: 11.5px;
  line-height: 1.5;
  color: var(--muted);
}

@media (prefers-reduced-motion: reduce) {
  .pop-04__panel {
    transition: none;
    opacity: 1;
    transform: none;
  }

  @starting-style {
    .pop-04__panel:popover-open {
      opacity: 1;
      transform: none;
    }
  }
}

@media (prefers-color-scheme: light) {
  .pop-04 {
    --void: #f4f5f1;
    --surface: #ffffff;
    --ink: #14160f;
    --muted: #676c60;
    --rule: #e2e4dc;
    --glow: #3f6b0a;
  }

  .pop-04__num {
    color: #ffffff;
  }

  .pop-04__dot {
    box-shadow: none;
  }

  .pop-04__panel {
    box-shadow: 0 20px 44px -24px rgba(20, 22, 15, 0.4);
  }
}

[data-theme="dark"] .pop-04 {
  --void: #000000;
  --surface: #0b0b0d;
  --ink: #f4f7f4;
  --muted: #83887f;
  --rule: #1e2022;
  --glow: #c3f53c;
}
```
