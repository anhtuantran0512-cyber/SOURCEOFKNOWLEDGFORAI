---
source: "codefronts"
url: "https://codefronts.com/motion/css-transition-designs/border-animation-transition/"
title: "Border and Outline Transitions Without Reflow"
section: "motion"
category: "css-transition-designs"
category_name: "CSS Transitions"
description: "Transitioning border-width changes the element's box, so every hover reflows the row and nudges its neighbours."
has_js: "false"
---

Here's a working CSS Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Border and Outline Transitions Without Reflow
Source: https://codefronts.com/motion/css-transition-designs/border-animation-transition/

Transitioning border-width changes the element's box, so every hover reflows the row and nudges its neighbours. Three alternatives that produce the same visual ring with no layout cost are shown beside the naive version and labelled: an inset box-shadow, an outline with outline-offset, and a pseudo-element border that scales.
## HTML
```html
<section class="trn-07" aria-labelledby="trn-07-heading">
  <div class="trn-07__stage">
    <div class="trn-07__theme">
      <input class="trn-07__themecb" type="checkbox" id="trn-07-theme">
      <label class="trn-07__themebtn" for="trn-07-theme">
        <span class="trn-07__themeico" aria-hidden="true">
          <svg class="trn-07__sun" viewBox="0 0 20 20" width="15" height="15"><circle cx="10" cy="10" r="3.9" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10 1.7v2.1M10 16.2v2.1M1.7 10h2.1M16.2 10h2.1M4.2 4.2l1.5 1.5M14.3 14.3l1.5 1.5M15.8 4.2l-1.5 1.5M5.7 14.3l-1.5 1.5" stroke="currentColor" stroke-width="1.4"/></svg>
          <svg class="trn-07__moon" viewBox="0 0 20 20" width="15" height="15"><path d="M15.4 12.7A6.7 6.7 0 0 1 7.3 4.6a6.8 6.8 0 1 0 8.1 8.1Z" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>
        </span>
        <span>Theme</span>
      </label>
    </div>
    <header class="trn-07__head">
      <h2 class="trn-07__heading" id="trn-07-heading">Four ways to grow a ring, one that costs layout</h2>
      <p class="trn-07__sub">Hover each card. Watch the sibling underneath it — only the first column moves anything.</p>
    </header>

    <div class="trn-07__grid">
      <div class="trn-07__col">
        <p class="trn-07__label trn-07__label--bad">border-width — reflows</p>
        <button class="trn-07__card trn-07__card--width" type="button">
          <span class="trn-07__name">Vale staging</span>
          <span class="trn-07__meta">border: 1px &rarr; 4px</span>
        </button>
        <p class="trn-07__ghost">Sibling row — shifts on hover</p>
      </div>

      <div class="trn-07__col">
        <p class="trn-07__label">inset box-shadow</p>
        <button class="trn-07__card trn-07__card--shadow" type="button">
          <span class="trn-07__name">Vale staging</span>
          <span class="trn-07__meta">inset 0 0 0 4px</span>
        </button>
        <p class="trn-07__ghost">Sibling row — stays put</p>
      </div>

      <div class="trn-07__col">
        <p class="trn-07__label">outline + offset</p>
        <button class="trn-07__card trn-07__card--outline" type="button">
          <span class="trn-07__name">Vale staging</span>
          <span class="trn-07__meta">outline-offset 0 &rarr; 5px</span>
        </button>
        <p class="trn-07__ghost">Sibling row — stays put</p>
      </div>

      <div class="trn-07__col">
        <p class="trn-07__label">pseudo-element ring</p>
        <button class="trn-07__card trn-07__card--pseudo" type="button">
          <span class="trn-07__name">Vale staging</span>
          <span class="trn-07__meta">::after scale + opacity</span>
        </button>
        <p class="trn-07__ghost">Sibling row — stays put</p>
      </div>
    </div>

    <p class="trn-07__foot">If the thickness does not need to change, the production answer is simpler than all four: declare the final <code>border-width</code> up front and transition <code>border-color</code> alone.</p>
  </div>
</section>
```
## CSS
```css
.trn-07 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --page: #f3f1e7;
  --page: oklch(0.95 0.014 105);
  --card: #fbfaf3;
  --ink: #1e2a20;
  --ink: oklch(0.26 0.02 150);
  --muted: #5d6b5f;
  --muted: oklch(0.5 0.02 150);
  --rule: #cfd6c6;
  --rule: oklch(0.86 0.02 130);
  --accent: #3f7d4f;
  --accent: oklch(0.52 0.11 152);
  --bad: #a83b28;
  --bad: oklch(0.48 0.15 34);
  --ring: 4px;
  --font-display: "Bookman Old Style", "Rockwell", "Roboto Slab", Georgia, serif;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

.trn-07 *,
.trn-07 *::before,
.trn-07 *::after {
  box-sizing: border-box;
}

.trn-07__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(26px, 5vw, 58px) 16px;
}

.trn-07__head {
  inline-size: 100%;
  max-inline-size: 60rem;
  min-inline-size: 0;
  margin: 0 0 26px;
}

.trn-07__heading {
  margin: 0 0 10px;
  font: 600 clamp(24px, 4.4vw, 35px)/1.12 var(--font-display);
  letter-spacing: -0.015em;
  text-wrap: balance;
}

.trn-07__sub {
  margin: 0;
  max-inline-size: 52ch;
  font-size: 14.5px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.trn-07__grid {
  inline-size: 100%;
  max-inline-size: 60rem;
  min-inline-size: 0;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 13rem), 1fr));
  gap: 16px;
}

.trn-07__col {
  min-inline-size: 0;
}

.trn-07__label {
  margin: 0 0 10px;
  font: 500 11.5px/1.3 ui-monospace, Menlo, monospace;
  letter-spacing: 0.04em;
  color: var(--accent);
}

.trn-07__label--bad {
  color: var(--bad);
}

.trn-07__card {
  inline-size: 100%;
  min-height: 84px;
  display: grid;
  gap: 5px;
  align-content: center;
  padding: 14px 15px;
  text-align: start;
  background: var(--card);
  border-radius: 6px;
  border: 1px solid var(--rule);
  cursor: pointer;
  position: relative;
}

.trn-07__card:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.trn-07__name {
  font: 600 14px/1.2 var(--font-display);
  color: var(--ink);
}

.trn-07__meta {
  font: 400 11px/1.3 ui-monospace, Menlo, monospace;
  color: var(--muted);
}

.trn-07__ghost {
  margin: 10px 0 0;
  padding: 9px 12px;
  background: rgba(0, 0, 0, 0.04);
  border-radius: 6px;
  font-size: 11.5px;
  line-height: 1.35;
  color: var(--muted);
}

.trn-07__card--width {
  transition: border-width 260ms ease, border-color 260ms ease;
}

.trn-07__card--width:hover {
  border-width: var(--ring);
  border-color: var(--bad);
}

.trn-07__card--shadow {
  box-shadow: inset 0 0 0 0 var(--accent);
  transition: box-shadow 260ms ease;
}

.trn-07__card--shadow:hover {
  box-shadow: inset 0 0 0 var(--ring) var(--accent);
}

.trn-07__card--outline {
  outline: 2px solid transparent;
  outline-offset: 0;
  transition: outline-color 260ms ease, outline-offset 260ms cubic-bezier(.2, .8, .3, 1);
}

.trn-07__card--outline:hover {
  outline-color: var(--accent);
  outline-offset: 5px;
}

.trn-07__card--outline:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.trn-07__card--pseudo::after {
  content: "";
  position: absolute;
  inset: -3px;
  border: 2px solid var(--accent);
  border-radius: 9px;
  opacity: 0;
  transform: scale(0.97);
  transform-origin: center;
  transition: opacity 260ms ease, transform 260ms cubic-bezier(.2, .8, .3, 1);
}

.trn-07__card--pseudo:hover::after {
  opacity: 1;
  transform: scale(1);
}

.trn-07__foot {
  inline-size: 100%;
  max-inline-size: 60rem;
  margin: 22px 0 0;
  padding-block-start: 16px;
  border-block-start: 1px solid var(--rule);
  font-size: 12.5px;
  line-height: 1.6;
  color: var(--muted);
}

.trn-07__foot code {
  font: 400 11.5px/1 ui-monospace, Menlo, monospace;
  color: var(--ink);
}

@media (prefers-reduced-motion: reduce) {
  .trn-07__card--width {
    transition: border-color 140ms ease;
  }

  .trn-07__card--width:hover {
    border-width: 1px;
  }

  .trn-07__card--outline {
    transition: outline-color 140ms ease;
  }

  .trn-07__card--outline:hover {
    outline-offset: 0;
  }

  .trn-07__card--pseudo::after {
    transform: none;
    transition: opacity 140ms ease;
  }

  .trn-07__card--pseudo:hover::after {
    transform: none;
  }

  .trn-07__card--shadow {
    transition: box-shadow 140ms ease;
  }
}

@media (prefers-color-scheme: dark) {
  .trn-07 {
    --page: #141814;
    --page: oklch(0.2 0.014 150);
    --card: #1c221c;
    --ink: #eaf0e8;
    --ink: oklch(0.95 0.014 150);
    --muted: #9aa89b;
    --muted: oklch(0.72 0.02 150);
    --rule: #2c352d;
    --accent: #7fd694;
    --accent: oklch(0.83 0.13 155);
    --bad: #ff8a70;
    --bad: oklch(0.75 0.15 36);
  }

  .trn-07__ghost {
    background: rgba(255, 255, 255, 0.05);
  }
}

[data-theme="dark"] .trn-07 {
  --page: #141814;
  --card: #1c221c;
  --ink: #eaf0e8;
  --muted: #9aa89b;
  --rule: #2c352d;
  --accent: #7fd694;
  --bad: #ff8a70;
}

[data-theme="dark"] .trn-07__ghost {
  background: rgba(255, 255, 255, 0.05);
}

.trn-07__theme {
  position: relative;
  inline-size: 100%;
  min-inline-size: 0;
  display: flex;
  justify-content: flex-end;
  margin: 0 0 14px;
}

.trn-07__themecb {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  clip-path: inset(50%);
  overflow: hidden;
}

.trn-07__themebtn {
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

.trn-07__themebtn:hover {
  color: var(--ink);
}

.trn-07__themecb:focus-visible + .trn-07__themebtn {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.trn-07__themeico {
  display: grid;
  place-items: center;
  inline-size: 15px;
  block-size: 15px;
}

.trn-07__themeico svg {
  grid-area: 1 / 1;
  transition: opacity 200ms ease;
}

.trn-07__sun {
  opacity: 1;
}

.trn-07__moon {
  opacity: 0.34;
}

.trn-07:has(#trn-07-theme:checked) .trn-07__sun {
  opacity: 0.34;
}

.trn-07:has(#trn-07-theme:checked) .trn-07__moon {
  opacity: 1;
}

@media (prefers-color-scheme: light) {
  .trn-07:has(#trn-07-theme:checked) {
    --page: #141814;
    --page: oklch(0.2 0.014 150);
    --card: #1c221c;
    --ink: #eaf0e8;
    --ink: oklch(0.95 0.014 150);
    --muted: #9aa89b;
    --muted: oklch(0.72 0.02 150);
    --rule: #2c352d;
    --accent: #7fd694;
    --accent: oklch(0.83 0.13 155);
    --bad: #ff8a70;
    --bad: oklch(0.75 0.15 36);
  }

  .trn-07:has(#trn-07-theme:checked) .trn-07__ghost {
    background: rgba(255, 255, 255, 0.05);
  }
}

@media (prefers-color-scheme: dark) {
  .trn-07:has(#trn-07-theme:checked) {
    --page: #f3f1e7;
    --page: oklch(0.95 0.014 105);
    --card: #fbfaf3;
    --ink: #1e2a20;
    --ink: oklch(0.26 0.02 150);
    --muted: #5d6b5f;
    --muted: oklch(0.5 0.02 150);
    --rule: #cfd6c6;
    --rule: oklch(0.86 0.02 130);
    --accent: #3f7d4f;
    --accent: oklch(0.52 0.11 152);
    --bad: #a83b28;
    --bad: oklch(0.48 0.15 34);
    --ring: 4px;
    --font-display: "Bookman Old Style", "Rockwell", "Roboto Slab", Georgia, serif;
    background: var(--page);
  }

  .trn-07:has(#trn-07-theme:checked) .trn-07__ghost {
    margin: 10px 0 0;
    padding: 9px 12px;
    background: rgba(0, 0, 0, 0.04);
    border-radius: 6px;
    font-size: 11.5px;
    line-height: 1.35;
    color: var(--muted);
  }

  .trn-07:has(#trn-07-theme:checked) .trn-07__sun {
    opacity: 1;
  }

  .trn-07:has(#trn-07-theme:checked) .trn-07__moon {
    opacity: 0.34;
  }
}
```
