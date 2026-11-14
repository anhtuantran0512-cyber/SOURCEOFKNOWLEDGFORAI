---
source: "codefronts"
url: "https://codefronts.com/components/css-gradient-buttons/css-gradient-pill-button/"
title: "CSS Gradient Pill Button"
section: "components"
category: "css-gradient-buttons"
category_name: "CSS Gradient Buttons"
description: "A topic-picker of fully-rounded gradient pills — six duotone palettes, hidden-checkbox selection with hue-matched glows, and gradient slides on hover, all…"
has_js: "false"
---

Here's a working CSS Gradient Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Gradient Pill Button
Source: https://codefronts.com/components/css-gradient-buttons/css-gradient-pill-button/

A topic-picker of fully-rounded gradient pills — six duotone palettes, hidden-checkbox selection with hue-matched glows, and gradient slides on hover, all without JavaScript.
## HTML
```html
<div class="gb-14">
  <div class="gb-14__panel">
    <h3 class="gb-14__h">What are you into?</h3>
    <p class="gb-14__sub">Pick a few topics — we'll tune your feed.</p>
    <div class="gb-14__cloud">
      <input class="gb-14__check" type="checkbox" id="gb-14-sun" checked>
      <label class="gb-14__pill gb-14__pill--sun" for="gb-14-sun"><i aria-hidden="true">◐</i>Photography</label>
      <input class="gb-14__check" type="checkbox" id="gb-14-reef">
      <label class="gb-14__pill gb-14__pill--reef" for="gb-14-reef"><i aria-hidden="true">◆</i>Freediving</label>
      <input class="gb-14__check" type="checkbox" id="gb-14-moss" checked>
      <label class="gb-14__pill gb-14__pill--moss" for="gb-14-moss"><i aria-hidden="true">✳</i>Trail running</label>
      <input class="gb-14__check" type="checkbox" id="gb-14-berry">
      <label class="gb-14__pill gb-14__pill--berry" for="gb-14-berry"><i aria-hidden="true">◈</i>Synthwave</label>
      <input class="gb-14__check" type="checkbox" id="gb-14-dawn">
      <label class="gb-14__pill gb-14__pill--dawn" for="gb-14-dawn"><i aria-hidden="true">✺</i>Ceramics</label>
      <input class="gb-14__check" type="checkbox" id="gb-14-ocean">
      <label class="gb-14__pill gb-14__pill--ocean" for="gb-14-ocean"><i aria-hidden="true">❋</i>Astronomy</label>
    </div>
    <p class="gb-14__count">Toggle any pill — selection is pure CSS via hidden checkboxes</p>
  </div>
</div>
```
## CSS
```css
.gb-14,
.gb-14 *,
.gb-14 *::before,
.gb-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gb-14 ::selection {
  background: #0ea5e9;
  color: #fff;
}

.gb-14 {
  --ink: #0f172a;
  font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
  background: #fbfcfe;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 24px;
}

.gb-14__panel {
  width: 100%;
  max-width: 520px;
}

.gb-14__h {
  font-size: 22px;
  font-weight: 800;
  color: var(--ink);
  letter-spacing: -.4px;
  margin-bottom: 6px;
}

.gb-14__sub {
  font-size: 14px;
  color: #7b8794;
  margin-bottom: 26px;
}

.gb-14__cloud {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}
/* fully-rounded pills, each with its own duotone at 200% width so
   hover glides the hues; the checked state (pure CSS via hidden
   checkbox) locks the gradient on and adds a hue-matched glow. */

.gb-14__check {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.gb-14__pill {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 11px 22px;
  border-radius: 9999px;
  font-size: 14px;
  font-weight: 700;
  color: #475569;
  cursor: pointer;
  background: #fff;
  box-shadow: inset 0 0 0 1.5px #e2e8f0;
  transition: color .3s ease,box-shadow .35s ease,transform .25s ease;
  -webkit-tap-highlight-color: transparent;
  position: relative;
  isolation: isolate;
  overflow: hidden;
  user-select: none;
}

.gb-14__pill::before {
  content: "";
  position: absolute;
  inset: 0;
  z-index: -1;
  border-radius: inherit;
  background-image: linear-gradient(110deg,var(--a),var(--b),var(--a));
  background-size: 220% auto;
  background-position: 0% center;
  opacity: 0;
  transition: opacity .35s ease,background-position .6s ease;
}

.gb-14__pill:hover {
  transform: translateY(-2px);
}

.gb-14__pill:hover::before {
  opacity: .14;
}

.gb-14__check:checked + .gb-14__pill {
  color: #fff;
  box-shadow: inset 0 0 0 1.5px transparent,0 10px 24px -10px var(--glow);
}

.gb-14__check:checked + .gb-14__pill::before {
  opacity: 1;
}

.gb-14__check:checked + .gb-14__pill:hover::before {
  background-position: 100% center;
}

.gb-14__check:focus-visible + .gb-14__pill {
  outline: 3px solid var(--a);
  outline-offset: 3px;
}

.gb-14__pill i {
  font-style: normal;
  font-size: 15px;
  line-height: 1;
}

.gb-14__pill--sun {
  --a: #f59e0b;
  --b: #ef4444;
  --glow: rgba(239,68,68,.45);
}

.gb-14__pill--reef {
  --a: #06b6d4;
  --b: #3b82f6;
  --glow: rgba(59,130,246,.45);
}

.gb-14__pill--moss {
  --a: #22c55e;
  --b: #14b8a6;
  --glow: rgba(20,184,166,.45);
}

.gb-14__pill--berry {
  --a: #d946ef;
  --b: #8b5cf6;
  --glow: rgba(139,92,246,.45);
}

.gb-14__pill--dawn {
  --a: #fb7185;
  --b: #f97316;
  --glow: rgba(251,113,133,.45);
}

.gb-14__pill--ocean {
  --a: #0ea5e9;
  --b: #6366f1;
  --glow: rgba(14,165,233,.45);
}

.gb-14__count {
  margin-top: 24px;
  font-size: 13px;
  color: #94a3b8;
}

@media (prefers-reduced-motion: reduce) {
  .gb-14__pill,
    .gb-14__pill::before {
    transition: none;
  }

  .gb-14__pill:hover {
    transform: none;
  }
}
```
