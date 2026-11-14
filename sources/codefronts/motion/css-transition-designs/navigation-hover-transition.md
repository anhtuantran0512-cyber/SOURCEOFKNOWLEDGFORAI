---
source: "codefronts"
url: "https://codefronts.com/motion/css-transition-designs/navigation-hover-transition/"
title: "Focus Within Parent State Transitions"
section: "motion"
category: "css-transition-designs"
category_name: "CSS Transitions"
description: "A workspace search panel that expands its filter tray when any descendant receives focus, using :focus-within on the parent so keyboard and touch users get…"
has_js: "false"
---

Here's a working CSS Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Focus Within Parent State Transitions
Source: https://codefronts.com/motion/css-transition-designs/navigation-hover-transition/

A workspace search panel that expands its filter tray when any descendant receives focus, using :focus-within on the parent so keyboard and touch users get the affordance that mouse users get from :hover. A hover-only reveal is not a styling shortcut — it is a feature that does not exist for anyone who cannot hover.
## HTML
```html
<section class="trn-09" aria-labelledby="trn-09-heading">
  <div class="trn-09__stage">
    <div class="trn-09__theme">
      <input class="trn-09__themecb" type="checkbox" id="trn-09-theme">
      <label class="trn-09__themebtn" for="trn-09-theme">
        <span class="trn-09__themeico" aria-hidden="true">
          <svg class="trn-09__sun" viewBox="0 0 20 20" width="15" height="15"><circle cx="10" cy="10" r="3.9" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10 1.7v2.1M10 16.2v2.1M1.7 10h2.1M16.2 10h2.1M4.2 4.2l1.5 1.5M14.3 14.3l1.5 1.5M15.8 4.2l-1.5 1.5M5.7 14.3l-1.5 1.5" stroke="currentColor" stroke-width="1.4"/></svg>
          <svg class="trn-09__moon" viewBox="0 0 20 20" width="15" height="15"><path d="M15.4 12.7A6.7 6.7 0 0 1 7.3 4.6a6.8 6.8 0 1 0 8.1 8.1Z" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>
        </span>
        <span>Theme</span>
      </label>
    </div>
    <header class="trn-09__head">
      <p class="trn-09__kicker">:focus-within</p>
      <h2 class="trn-09__heading" id="trn-09-heading">The reveal that works without a pointer</h2>
      <p class="trn-09__sub">Press Tab into the panel below. The tray opens for focus exactly as it does for hover.</p>
    </header>

    <div class="trn-09__panel">
      <div class="trn-09__bar">
        <svg class="trn-09__icon" viewBox="0 0 20 20" width="17" height="17" aria-hidden="true"><circle cx="9" cy="9" r="6.2" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="m13.6 13.6 3.4 3.4" stroke="currentColor" stroke-width="1.6"/></svg>
        <label class="trn-09__srlabel" for="trn-09-q">Search Meridian workspace</label>
        <input class="trn-09__field" id="trn-09-q" type="text" placeholder="Search runs, datasets, people">
        <button class="trn-09__go" type="button">Search</button>
      </div>

      <div class="trn-09__tray">
        <fieldset class="trn-09__group">
          <legend class="trn-09__legend">Scope</legend>
          <label class="trn-09__chip"><input type="radio" name="trn-09-scope" checked><span>Everything</span></label>
          <label class="trn-09__chip"><input type="radio" name="trn-09-scope"><span>Datasets</span></label>
          <label class="trn-09__chip"><input type="radio" name="trn-09-scope"><span>Runs</span></label>
          <label class="trn-09__chip"><input type="radio" name="trn-09-scope"><span>People</span></label>
        </fieldset>
        <fieldset class="trn-09__group">
          <legend class="trn-09__legend">Owner</legend>
          <label class="trn-09__chip"><input type="checkbox"><span>Alex Chen</span></label>
          <label class="trn-09__chip"><input type="checkbox"><span>Priya Sharma</span></label>
          <label class="trn-09__chip"><input type="checkbox"><span>Sam Rivera</span></label>
        </fieldset>
      </div>

      <p class="trn-09__hint">Tray state: <code>.trn-09__panel:hover</code>, <code>.trn-09__panel:focus-within</code></p>
    </div>

    <p class="trn-09__foot">Both selectors are declared together. Remove the second one and the panel becomes a mouse-only feature — the fields inside stay focusable, but nobody can see what they focused.</p>
  </div>
</section>
```
## CSS
```css
.trn-09 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --page: #f4f7fc;
  --page: oklch(0.97 0.008 250);
  --card: #ffffff;
  --ink: #16233a;
  --ink: oklch(0.25 0.03 255);
  --muted: #5c6b85;
  --muted: oklch(0.52 0.03 254);
  --rule: #d8e0ec;
  --rule: oklch(0.89 0.014 250);
  --accent: #1e63d4;
  --accent: oklch(0.53 0.18 260);
  --soft: #eaf1fc;
  --soft: oklch(0.95 0.02 254);
  --reveal: 8px;
  --font-display: "Segoe UI", "Frutiger", "Myriad Pro", system-ui, sans-serif;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

.trn-09 *,
.trn-09 *::before,
.trn-09 *::after {
  box-sizing: border-box;
}

.trn-09__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(26px, 5vw, 60px) 16px;
}

.trn-09__head {
  inline-size: 100%;
  max-inline-size: 50rem;
  min-inline-size: 0;
  margin: 0 0 24px;
}

.trn-09__kicker {
  margin: 0 0 10px;
  font: 600 11.5px/1 ui-monospace, Menlo, monospace;
  letter-spacing: 0.08em;
  color: var(--accent);
}

.trn-09__heading {
  margin: 0 0 10px;
  font: 600 clamp(24px, 4.4vw, 34px)/1.14 var(--font-display);
  letter-spacing: -0.02em;
  text-wrap: balance;
}

.trn-09__sub {
  margin: 0;
  max-inline-size: 50ch;
  font-size: 14.5px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.trn-09__panel {
  inline-size: 100%;
  max-inline-size: 50rem;
  min-inline-size: 0;
  padding: 16px;
  background: var(--card);
  border: 1px solid var(--rule);
  border-radius: 12px;
  box-shadow: 0 1px 2px rgba(22, 35, 58, 0.06);
  transition: box-shadow 240ms ease, border-color 240ms ease;
}

.trn-09__panel:hover,
.trn-09__panel:focus-within {
  border-color: var(--accent);
  box-shadow: 0 10px 30px -18px rgba(30, 99, 212, 0.55);
}

.trn-09__bar {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  align-items: center;
  min-inline-size: 0;
}

.trn-09__icon {
  flex: none;
  color: var(--muted);
  transition: color 200ms ease;
}

.trn-09__panel:hover .trn-09__icon,
.trn-09__panel:focus-within .trn-09__icon {
  color: var(--accent);
}

.trn-09__srlabel {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  clip-path: inset(50%);
  overflow: hidden;
}

.trn-09__field {
  flex: 1 1 12rem;
  min-inline-size: 0;
  min-height: 44px;
  padding: 0 12px;
  background: var(--page);
  border: 1px solid var(--rule);
  border-radius: 8px;
  font: 400 14px/1 system-ui, sans-serif;
  color: var(--ink);
  transition: background-color 200ms ease, border-color 200ms ease;
}

.trn-09__field::placeholder {
  color: var(--muted);
}

.trn-09__field:hover {
  background: var(--card);
}

.trn-09__field:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
  background: var(--card);
}

.trn-09__go {
  min-height: 44px;
  padding: 0 18px;
  background: var(--accent);
  color: #fff;
  border: 0;
  border-radius: 8px;
  font: 600 13.5px/1 var(--font-display);
  cursor: pointer;
  transition: background-color 180ms ease, transform 180ms cubic-bezier(.2, .8, .3, 1);
}

.trn-09__go:hover {
  transform: translateY(-1px);
}

.trn-09__go:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.trn-09__tray {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 13rem), 1fr));
  gap: 12px;
  margin-block-start: 14px;
  min-block-size: 118px;
  opacity: 0;
  transform: translateY(calc(var(--reveal) * -1));
  transition: opacity 260ms ease, transform 260ms cubic-bezier(.2, .8, .3, 1);
}

.trn-09__panel:hover .trn-09__tray,
.trn-09__panel:focus-within .trn-09__tray {
  opacity: 1;
  transform: translateY(0);
}

.trn-09__group {
  min-inline-size: 0;
  margin: 0;
  padding: 12px;
  border: 1px solid var(--rule);
  border-radius: 9px;
  background: var(--soft);
}

.trn-09__legend {
  padding: 0 4px;
  font: 600 10.5px/1 var(--font-display);
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--muted);
}

.trn-09__chip {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  min-height: 44px;
  padding-inline-end: 10px;
  margin-inline-end: 6px;
  font-size: 13px;
  color: var(--ink);
  cursor: pointer;
}

.trn-09__chip input {
  inline-size: 16px;
  block-size: 16px;
  accent-color: var(--accent);
}

.trn-09__chip input:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.trn-09__hint {
  margin: 12px 0 0;
  font-size: 11.5px;
  line-height: 1.5;
  color: var(--muted);
}

.trn-09__hint code {
  font: 400 11px/1 ui-monospace, Menlo, monospace;
  color: var(--accent);
  overflow-wrap: anywhere;
}

.trn-09__foot {
  inline-size: 100%;
  max-inline-size: 50rem;
  margin: 18px 0 0;
  font-size: 12.5px;
  line-height: 1.6;
  color: var(--muted);
}

@media (prefers-reduced-motion: reduce) {
  .trn-09__tray {
    transform: none;
    transition: opacity 150ms ease;
  }

  .trn-09__panel:hover .trn-09__tray,
    .trn-09__panel:focus-within .trn-09__tray {
    transform: none;
  }

  .trn-09__go {
    transition: background-color 150ms ease;
  }

  .trn-09__go:hover {
    transform: none;
    background: #14479c;
  }
}

@media (prefers-color-scheme: dark) {
  .trn-09 {
    --page: #0d1420;
    --page: oklch(0.2 0.024 256);
    --card: #141d2d;
    --card: oklch(0.24 0.028 256);
    --ink: #e9eff9;
    --ink: oklch(0.95 0.012 252);
    --muted: #94a3bd;
    --muted: oklch(0.72 0.028 254);
    --rule: #253248;
    --rule: oklch(0.31 0.03 254);
    --accent: #6fa4ff;
    --accent: oklch(0.75 0.13 262);
    --soft: #101a29;
  }

  .trn-09__go {
    color: #0d1420;
  }

  .trn-09__panel {
    box-shadow: none;
  }

  @media (prefers-reduced-motion: reduce) {
    .trn-09__go:hover {
      background: #a8c6ff;
    }
  }
}

[data-theme="dark"] .trn-09 {
  --page: #0d1420;
  --card: #141d2d;
  --ink: #e9eff9;
  --muted: #94a3bd;
  --rule: #253248;
  --accent: #6fa4ff;
  --soft: #101a29;
}

[data-theme="dark"] .trn-09__go {
  color: #0d1420;
}

[data-theme="dark"] .trn-09__panel {
  box-shadow: none;
}

.trn-09__theme {
  position: relative;
  inline-size: 100%;
  min-inline-size: 0;
  display: flex;
  justify-content: flex-end;
  margin: 0 0 14px;
}

.trn-09__themecb {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  clip-path: inset(50%);
  overflow: hidden;
}

.trn-09__themebtn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  min-height: 44px;
  padding: 0 14px;
  border: 1px solid currentColor;
  border-radius: 999px;
  cursor: pointer;
  color: var(--muted);
  font: 500 11px/1 ui-monospace, Menlo, monospace;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  transition: color 200ms ease, opacity 200ms ease;
}

.trn-09__themebtn:hover {
  color: var(--ink);
}

.trn-09__themecb:focus-visible + .trn-09__themebtn {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.trn-09__themeico {
  display: grid;
  place-items: center;
  inline-size: 15px;
  block-size: 15px;
}

.trn-09__themeico svg {
  grid-area: 1 / 1;
  transition: opacity 200ms ease;
}

.trn-09__sun {
  opacity: 1;
}

.trn-09__moon {
  opacity: 0.34;
}

.trn-09:has(#trn-09-theme:checked) .trn-09__sun {
  opacity: 0.34;
}

.trn-09:has(#trn-09-theme:checked) .trn-09__moon {
  opacity: 1;
}

@media (prefers-color-scheme: light) {
  .trn-09:has(#trn-09-theme:checked) {
    --page: #0d1420;
    --page: oklch(0.2 0.024 256);
    --card: #141d2d;
    --card: oklch(0.24 0.028 256);
    --ink: #e9eff9;
    --ink: oklch(0.95 0.012 252);
    --muted: #94a3bd;
    --muted: oklch(0.72 0.028 254);
    --rule: #253248;
    --rule: oklch(0.31 0.03 254);
    --accent: #6fa4ff;
    --accent: oklch(0.75 0.13 262);
    --soft: #101a29;
  }

  .trn-09:has(#trn-09-theme:checked) .trn-09__go {
    color: #0d1420;
  }

  .trn-09:has(#trn-09-theme:checked) .trn-09__panel {
    box-shadow: none;
  }
}

@media (prefers-color-scheme: dark) {
  .trn-09:has(#trn-09-theme:checked) {
    --page: #f4f7fc;
    --page: oklch(0.97 0.008 250);
    --card: #ffffff;
    --ink: #16233a;
    --ink: oklch(0.25 0.03 255);
    --muted: #5c6b85;
    --muted: oklch(0.52 0.03 254);
    --rule: #d8e0ec;
    --rule: oklch(0.89 0.014 250);
    --accent: #1e63d4;
    --accent: oklch(0.53 0.18 260);
    --soft: #eaf1fc;
    --soft: oklch(0.95 0.02 254);
    --reveal: 8px;
    --font-display: "Segoe UI", "Frutiger", "Myriad Pro", system-ui, sans-serif;
    background: var(--page);
  }

  .trn-09:has(#trn-09-theme:checked) .trn-09__go {
    min-height: 44px;
    padding: 0 18px;
    background: var(--accent);
    color: #fff;
    border: 0;
    border-radius: 8px;
    font: 600 13.5px/1 var(--font-display);
    cursor: pointer;
    transition: background-color 180ms ease, transform 180ms cubic-bezier(.2, .8, .3, 1);
  }

  .trn-09:has(#trn-09-theme:checked) .trn-09__panel {
    inline-size: 100%;
    max-inline-size: 50rem;
    min-inline-size: 0;
    padding: 16px;
    background: var(--card);
    border: 1px solid var(--rule);
    border-radius: 12px;
    box-shadow: 0 1px 2px rgba(22, 35, 58, 0.06);
    transition: box-shadow 240ms ease, border-color 240ms ease;
  }

  .trn-09:has(#trn-09-theme:checked) .trn-09__sun {
    opacity: 1;
  }

  .trn-09:has(#trn-09-theme:checked) .trn-09__moon {
    opacity: 0.34;
  }
}
```
