---
source: "codefronts"
url: "https://codefronts.com/components/css-loading-buttons/ghost-outline-loading-button/"
title: "Ghost Outline Loading Button"
section: "components"
category: "css-loading-buttons"
category_name: "CSS Loading Buttons"
description: "Border-only at rest, with the pending state carried by the border itself: a dash travels the perimeter while the request runs, so the outline is the…"
has_js: "false"
---

Here's a working CSS Loading Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Ghost Outline Loading Button
Source: https://codefronts.com/components/css-loading-buttons/ghost-outline-loading-button/

Border-only at rest, with the pending state carried by the border itself: a dash travels the perimeter while the request runs, so the outline is the indicator and nothing inside the button moves. No script — an SVG rect stroke does the drawing, and a checkbox stands in for the request so the whole state machine is CSS.
## HTML
```html
<div class="lb-16">
  <div class="lb-16__stage">
    <section class="lb-16__card" aria-labelledby="lb-16-h">
      <span class="lb-16__glyph" aria-hidden="true">
        <svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M3.5 7.5h17v12h-17z"/><path d="M3.5 7.5 6 4.5h12l2.5 3M12 11v5M9.5 13.5 12 16l2.5-2.5"/></svg>
      </span>
      <h2 class="lb-16__h" id="lb-16-h">Nothing archived yet</h2>
      <p class="lb-16__sub">Older threads move here after 90 days. Loading the archive can take a moment.</p>

      <button class="lb-16__btn" type="button" data-state="idle" aria-busy="false">
        <svg class="lb-16__trace" aria-hidden="true" preserveAspectRatio="none" viewBox="0 0 200 48">
          <rect class="lb-16__rect" x="1" y="1" width="198" height="46" rx="23" pathLength="100" fill="none" stroke="currentColor" stroke-width="2" vector-effect="non-scaling-stroke"/>
        </svg>
        <span class="lb-16__faces">
          <span class="lb-16__face lb-16__face--idle">Load archive</span>
          <span class="lb-16__face lb-16__face--pending">Loading archive</span>
        </span>
      </button>

      <div class="lb-16__control">
        <input class="lb-16__switch" type="checkbox" id="lb-16-switch">
        <label class="lb-16__lab" for="lb-16-switch">Hold the request open</label>
      </div>
    </section>
  </div>
</div>
```
## CSS
```css
.lb-16 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --bg: #f3f6fb;
  --surface: #ffffff;
  --ink: #14243a;
  --muted: #63799a;
  --rule: #dbe4f0;
  --accent: #1d54b8;
  font-family: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
  background: var(--bg);
  color: var(--ink);
  padding: 40px 16px;
}

.lb-16 *,
.lb-16 *::before,
.lb-16 *::after {
  box-sizing: border-box;
}

.lb-16__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  min-height: calc(100vh - 80px);
}

.lb-16__card {
  inline-size: 100%;
  max-inline-size: 28rem;
  min-inline-size: 0;
  background: var(--surface);
  border: 1px solid var(--rule);
  border-radius: 12px;
  padding: 32px 26px 26px;
  text-align: center;
}

.lb-16__glyph {
  display: inline-flex;
  color: var(--muted);
  margin-block-end: 14px;
}

.lb-16__h {
  margin: 0;
  font-size: 18px;
  font-weight: 640;
  letter-spacing: -.015em;
}

.lb-16__sub {
  margin: 8px auto 22px;
  font-size: 13px;
  line-height: 1.6;
  color: var(--muted);
  max-inline-size: 34ch;
}

.lb-16__btn {
  appearance: none;
  position: relative;
  border: 0;
  background: transparent;
  color: var(--accent);
  border-radius: 999px;
  font: inherit;
  font-size: 13.5px;
  font-weight: 600;
  padding: 0 26px;
  min-block-size: 48px;
  min-inline-size: 11rem;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.lb-16__btn:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

.lb-16__trace {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  overflow: visible;
}

.lb-16__rect {
  stroke-dasharray: 100 0;
  stroke-dashoffset: 0;
  opacity: .55;
}

.lb-16__faces {
  display: grid;
  place-items: center;
}

.lb-16__face {
  grid-area: 1 / 1;
  white-space: nowrap;
  visibility: hidden;
}

.lb-16__face--idle {
  visibility: visible;
}

.lb-16:has(.lb-16__switch:checked) .lb-16__face--idle {
  visibility: hidden;
}

.lb-16:has(.lb-16__switch:checked) .lb-16__face--pending {
  visibility: visible;
}

.lb-16:has(.lb-16__switch:checked) .lb-16__rect {
  opacity: 1;
  stroke-dasharray: 22 78;
  animation: lb-16-trace 1.6s linear infinite;
}

@keyframes lb-16-trace {
  to {
    stroke-dashoffset: -100;
  }
}

.lb-16__control {
  display: flex;
  justify-content: center;
  margin-block-start: 20px;
}

.lb-16__lab {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 12px;
  color: var(--muted);
  min-height: 44px;
  cursor: pointer;
}

.lb-16__switch {
  accent-color: var(--accent);
  inline-size: 16px;
  block-size: 16px;
  margin: 0;
}

.lb-16__switch:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .lb-16:has(.lb-16__switch:checked) .lb-16__rect {
    animation: none;
    stroke-dasharray: 50 50;
  }
}

@media (prefers-color-scheme: dark) {
  .lb-16 {
    --bg: #0d141d;
    --surface: #141d28;
    --ink: #e6edf6;
    --muted: #8ba0bb;
    --rule: #223040;
    --accent: #7fb0ff;
  }
}

[data-theme="dark"] .lb-16 {
  --bg: #0d141d;
  --surface: #141d28;
  --ink: #e6edf6;
  --muted: #8ba0bb;
  --rule: #223040;
  --accent: #7fb0ff;
}
```
