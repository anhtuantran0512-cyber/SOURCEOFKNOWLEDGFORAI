---
source: "codefronts"
url: "https://codefronts.com/motion/css-transition-designs/slide-in-animation-on-scroll/"
title: "Transition Delay Choreography with Reverse Exit"
section: "motion"
category: "css-transition-designs"
category_name: "CSS Transitions"
description: "A menu panel whose items transition in with an increasing transition-delay and — the part almost every implementation gets wrong — transition out in reverse…"
has_js: "false"
---

Here's a working CSS Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Transition Delay Choreography with Reverse Exit
Source: https://codefronts.com/motion/css-transition-designs/slide-in-animation-on-scroll/

A menu panel whose items transition in with an increasing transition-delay and — the part almost every implementation gets wrong — transition out in reverse order, because the delay on the resting state is calculated from the other end of the list. Both delay sets are printed beside the panels so the entry ladder and the exit ladder can be read directly.
## HTML
```html
<section class="trn-02" aria-labelledby="trn-02-heading">
  <div class="trn-02__stage">
    <div class="trn-02__theme">
      <input class="trn-02__themecb" type="checkbox" id="trn-02-theme">
      <label class="trn-02__themebtn" for="trn-02-theme">
        <span class="trn-02__themeico" aria-hidden="true">
          <svg class="trn-02__sun" viewBox="0 0 20 20" width="15" height="15"><circle cx="10" cy="10" r="3.9" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10 1.7v2.1M10 16.2v2.1M1.7 10h2.1M16.2 10h2.1M4.2 4.2l1.5 1.5M14.3 14.3l1.5 1.5M15.8 4.2l-1.5 1.5M5.7 14.3l-1.5 1.5" stroke="currentColor" stroke-width="1.4"/></svg>
          <svg class="trn-02__moon" viewBox="0 0 20 20" width="15" height="15"><path d="M15.4 12.7A6.7 6.7 0 0 1 7.3 4.6a6.8 6.8 0 1 0 8.1 8.1Z" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>
        </span>
        <span>Theme</span>
      </label>
    </div>
    <header class="trn-02__head">
      <p class="trn-02__kicker">transition-delay</p>
      <h2 class="trn-02__heading" id="trn-02-heading">In from the top, out from the bottom</h2>
      <p class="trn-02__sub">Hover or Tab into either panel. Only the exit delay differs between them.</p>
    </header>

    <div class="trn-02__pair">
      <article class="trn-02__col">
        <h3 class="trn-02__label trn-02__label--bad">Same delays both ways — drains downward, reads as lag</h3>
        <div class="trn-02__menu trn-02__menu--naive" style="--n: 5">
          <button class="trn-02__trigger" type="button">Workspace</button>
          <ul class="trn-02__items">
            <li class="trn-02__item" style="--i: 0"><a href="#trn-02-heading">Deploy to production</a></li>
            <li class="trn-02__item" style="--i: 1"><a href="#trn-02-heading">Sync 4 repositories</a></li>
            <li class="trn-02__item" style="--i: 2"><a href="#trn-02-heading">Invite teammate</a></li>
            <li class="trn-02__item" style="--i: 3"><a href="#trn-02-heading">Rotate access keys</a></li>
            <li class="trn-02__item" style="--i: 4"><a href="#trn-02-heading">Archive workspace</a></li>
          </ul>
        </div>
      </article>

      <article class="trn-02__col">
        <h3 class="trn-02__label trn-02__label--good">Reversed exit — collapses back toward the trigger</h3>
        <div class="trn-02__menu trn-02__menu--reverse" style="--n: 5">
          <button class="trn-02__trigger" type="button">Workspace</button>
          <ul class="trn-02__items">
            <li class="trn-02__item" style="--i: 0"><a href="#trn-02-heading">Deploy to production</a></li>
            <li class="trn-02__item" style="--i: 1"><a href="#trn-02-heading">Sync 4 repositories</a></li>
            <li class="trn-02__item" style="--i: 2"><a href="#trn-02-heading">Invite teammate</a></li>
            <li class="trn-02__item" style="--i: 3"><a href="#trn-02-heading">Rotate access keys</a></li>
            <li class="trn-02__item" style="--i: 4"><a href="#trn-02-heading">Archive workspace</a></li>
          </ul>
        </div>
      </article>
    </div>

    <table class="trn-02__ladder">
      <caption>Delay ladder — five items, 45ms step</caption>
      <thead><tr><th scope="col">Item</th><th scope="col">Enter delay</th><th scope="col">Exit delay (reversed)</th></tr></thead>
      <tbody>
        <tr><th scope="row">Deploy to production</th><td>0ms</td><td>225ms</td></tr>
        <tr><th scope="row">Sync 4 repositories</th><td>45ms</td><td>180ms</td></tr>
        <tr><th scope="row">Invite teammate</th><td>90ms</td><td>135ms</td></tr>
        <tr><th scope="row">Rotate access keys</th><td>135ms</td><td>90ms</td></tr>
        <tr><th scope="row">Archive workspace</th><td>180ms</td><td>45ms</td></tr>
      </tbody>
    </table>
    </div>
  </div>
</section>
```
## CSS
```css
.trn-02 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --page: #080f1f;
  --page: oklch(0.17 0.04 262);
  --card: #0f1930;
  --card: oklch(0.23 0.048 263);
  --ink: #eaf2ff;
  --ink: oklch(0.96 0.014 250);
  --muted: #8ea3c6;
  --muted: oklch(0.72 0.037 254);
  --rule: #1e2c4d;
  --rule: oklch(0.3 0.048 262);
  --accent: #2ee6d6;
  --accent: oklch(0.85 0.126 186);
  --warn: #ff8f6b;
  --warn: oklch(0.76 0.148 42);
  --step: 45ms;
  --font-display: "Haas Grot Display", "Archivo Narrow", "Oswald", system-ui, sans-serif;
  background: radial-gradient(120% 90% at 15% 0%, #12203c 0%, var(--page) 62%);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

.trn-02 *,
.trn-02 *::before,
.trn-02 *::after {
  box-sizing: border-box;
}

.trn-02__stage {
  display: grid;
  place-items: start center;
  max-inline-size: 100%;
  padding: clamp(28px, 6vw, 64px) 16px;
}

.trn-02__head {
  inline-size: 100%;
  max-inline-size: 58rem;
  min-inline-size: 0;
  margin: 0 0 30px;
}

.trn-02__kicker {
  margin: 0 0 12px;
  font: 600 11px/1 ui-monospace, Menlo, monospace;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--accent);
}

.trn-02__heading {
  margin: 0 0 12px;
  font: 700 clamp(26px, 5.2vw, 42px)/1.05 var(--font-display);
  letter-spacing: 0.01em;
  text-transform: uppercase;
  text-wrap: balance;
}

.trn-02__sub {
  margin: 0;
  max-inline-size: 48ch;
  font-size: 15px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.trn-02__pair {
  inline-size: 100%;
  max-inline-size: 58rem;
  min-inline-size: 0;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 18rem), 1fr));
  gap: 22px;
}

.trn-02__col {
  min-inline-size: 0;
}

.trn-02__label {
  margin: 0 0 12px;
  font: 600 12px/1.45 ui-monospace, Menlo, monospace;
  letter-spacing: 0.02em;
}

.trn-02__label--bad {
  color: var(--warn);
}

.trn-02__label--good {
  color: var(--accent);
}

.trn-02__menu {
  min-inline-size: 0;
  padding: 20px;
  background: var(--card);
  border: 1px solid var(--rule);
  border-radius: 14px;
}

.trn-02__trigger {
  inline-size: 100%;
  min-height: 44px;
  padding: 0 18px;
  text-align: start;
  background: transparent;
  border: 1px solid var(--rule);
  border-radius: 9px;
  color: var(--ink);
  font: 600 14px/1 var(--font-display);
  letter-spacing: 0.06em;
  text-transform: uppercase;
  cursor: pointer;
  transition: border-color 200ms ease, box-shadow 200ms ease, color 200ms ease;
}

.trn-02__menu:hover .trn-02__trigger,
.trn-02__menu:focus-within .trn-02__trigger {
  border-color: var(--accent);
  color: var(--accent);
  box-shadow: 0 0 0 1px var(--accent), 0 8px 26px -14px var(--accent);
}

.trn-02__trigger:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.trn-02__items {
  list-style: none;
  margin: 12px 0 0;
  padding: 0;
  display: grid;
  gap: 6px;
}

.trn-02__item {
  min-inline-size: 0;
  opacity: 0;
  transform: translateY(-8px);
  transition: opacity 220ms ease, transform 220ms cubic-bezier(.2, .8, .3, 1);
}

.trn-02__menu--naive .trn-02__item {
  transition-delay: calc(var(--i) * var(--step));
}

.trn-02__menu--reverse .trn-02__item {
  transition-delay: calc((var(--n) - 1 - var(--i)) * var(--step));
}

.trn-02__menu:hover .trn-02__item,
.trn-02__menu:focus-within .trn-02__item {
  opacity: 1;
  transform: translateY(0);
  transition-delay: calc(var(--i) * var(--step));
}

.trn-02__item a {
  display: flex;
  align-items: center;
  min-height: 44px;
  padding: 0 14px;
  border-radius: 8px;
  color: var(--muted);
  text-decoration: none;
  font-size: 14px;
  transition: background-color 160ms ease, color 160ms ease;
}

.trn-02__item a:hover {
  background: rgba(46, 230, 214, 0.1);
  color: var(--ink);
}

.trn-02__item a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.trn-02__ladder {
  inline-size: 100%;
  max-inline-size: 58rem;
  margin: 30px 0 0;
  border-collapse: collapse;
  font-size: 12.5px;
}

.trn-02__ladder caption {
  margin-block-end: 10px;
  text-align: start;
  font: 600 11px/1 ui-monospace, Menlo, monospace;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--muted);
}

.trn-02__ladder th,
.trn-02__ladder td {
  padding: 9px 10px;
  text-align: start;
  border-block-end: 1px solid var(--rule);
  font-weight: 400;
  color: var(--muted);
}

.trn-02__ladder thead th {
  color: var(--ink);
  font: 600 11px/1.3 ui-monospace, Menlo, monospace;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.trn-02__ladder tbody th {
  color: var(--ink);
}

.trn-02__ladder td {
  font-family: ui-monospace, Menlo, monospace;
}

@media (prefers-reduced-motion: reduce) {
  .trn-02__item {
    transform: none;
    transition: opacity 140ms ease;
  }

  .trn-02__menu--naive .trn-02__item,
    .trn-02__menu--reverse .trn-02__item {
    transition-delay: 0s;
  }

  .trn-02__menu:hover .trn-02__item,
    .trn-02__menu:focus-within .trn-02__item {
    transform: none;
    transition-delay: calc(var(--i) * 12ms);
  }
}

@media (prefers-color-scheme: light) {
  .trn-02 {
    --page: #f2f5fb;
    --card: #ffffff;
    --ink: #0d1730;
    --muted: #4d5f80;
    --rule: #d6dfee;
    --accent: #0f8f86;
    --warn: #b8481f;
    background: radial-gradient(120% 90% at 15% 0%, #e6ecf8 0%, var(--page) 62%);
  }

  .trn-02__item a:hover {
    background: rgba(15, 143, 134, 0.12);
  }
}

[data-theme="dark"] .trn-02 {
  --page: #080f1f;
  --card: #0f1930;
  --ink: #eaf2ff;
  --muted: #8ea3c6;
  --rule: #1e2c4d;
  --accent: #2ee6d6;
  --warn: #ff8f6b;
  background: radial-gradient(120% 90% at 15% 0%, #12203c 0%, var(--page) 62%);
}

[data-theme="dark"] .trn-02__item a:hover {
  background: rgba(46, 230, 214, 0.1);
}

.trn-02__theme {
  position: relative;
  inline-size: 100%;
  min-inline-size: 0;
  display: flex;
  justify-content: flex-end;
  margin: 0 0 14px;
}

.trn-02__themecb {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  clip-path: inset(50%);
  overflow: hidden;
}

.trn-02__themebtn {
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

.trn-02__themebtn:hover {
  color: var(--ink);
}

.trn-02__themecb:focus-visible + .trn-02__themebtn {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.trn-02__themeico {
  display: grid;
  place-items: center;
  inline-size: 15px;
  block-size: 15px;
}

.trn-02__themeico svg {
  grid-area: 1 / 1;
  transition: opacity 200ms ease;
}

.trn-02__sun {
  opacity: 0.34;
}

.trn-02__moon {
  opacity: 1;
}

.trn-02:has(#trn-02-theme:checked) .trn-02__sun {
  opacity: 1;
}

.trn-02:has(#trn-02-theme:checked) .trn-02__moon {
  opacity: 0.34;
}

@media (prefers-color-scheme: dark) {
  .trn-02:has(#trn-02-theme:checked) {
    --page: #f2f5fb;
    --card: #ffffff;
    --ink: #0d1730;
    --muted: #4d5f80;
    --rule: #d6dfee;
    --accent: #0f8f86;
    --warn: #b8481f;
    background: radial-gradient(120% 90% at 15% 0%, #e6ecf8 0%, var(--page) 62%);
  }

  .trn-02:has(#trn-02-theme:checked) .trn-02__item a:hover {
    background: rgba(15, 143, 134, 0.12);
  }
}

@media (prefers-color-scheme: light) {
  .trn-02:has(#trn-02-theme:checked) {
    --page: #080f1f;
    --page: oklch(0.17 0.04 262);
    --card: #0f1930;
    --card: oklch(0.23 0.048 263);
    --ink: #eaf2ff;
    --ink: oklch(0.96 0.014 250);
    --muted: #8ea3c6;
    --muted: oklch(0.72 0.037 254);
    --rule: #1e2c4d;
    --rule: oklch(0.3 0.048 262);
    --accent: #2ee6d6;
    --accent: oklch(0.85 0.126 186);
    --warn: #ff8f6b;
    --warn: oklch(0.76 0.148 42);
    --step: 45ms;
    --font-display: "Haas Grot Display", "Archivo Narrow", "Oswald", system-ui, sans-serif;
    background: radial-gradient(120% 90% at 15% 0%, #12203c 0%, var(--page) 62%);
  }

  .trn-02:has(#trn-02-theme:checked) .trn-02__item a:hover {
    background: rgba(46, 230, 214, 0.1);
    color: var(--ink);
  }

  .trn-02:has(#trn-02-theme:checked) .trn-02__sun {
    opacity: 0.34;
  }

  .trn-02:has(#trn-02-theme:checked) .trn-02__moon {
    opacity: 1;
  }
}
```
