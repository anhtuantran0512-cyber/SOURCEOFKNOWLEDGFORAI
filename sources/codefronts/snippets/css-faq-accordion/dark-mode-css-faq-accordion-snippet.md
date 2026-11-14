---
source: "codefronts"
url: "https://codefronts.com/snippets/css-faq-accordion/dark-mode-css-faq-accordion-snippet/"
title: "Dark Mode CSS FAQ Accordion Snippet"
section: "snippets"
category: "css-faq-accordion"
category_name: "CSS FAQ Accordions"
description: "One accordion, two complete themes, zero duplicated rules: every color is declared once with the light-dark() function, and a single color-scheme property…"
has_js: "false"
---

Here's a working CSS FAQ Accordion from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark Mode CSS FAQ Accordion Snippet
Source: https://codefronts.com/snippets/css-faq-accordion/dark-mode-css-faq-accordion-snippet/

One accordion, two complete themes, zero duplicated rules: every color is declared once with the light-dark() function, and a single color-scheme property flips the whole component. The demo follows the OS preference by default and adds a pure-CSS sun/moon toggle (checkbox + :has()) to override it — the exact three-state setup (auto / forced light / forced dark) production sites need, with no JavaScript and no .dark class cascade.
## HTML
```html
<section class="cfa-06" aria-label="Dark mode FAQ accordion with light-dark()">
  <div class="cfa-06__wrap">
    <div class="cfa-06__bar">
      <span class="cfa-06__brand">Nightshift Docs</span>
      <input type="checkbox" id="cfa06-mode" class="cfa-06__modecb">
      <label class="cfa-06__toggle" for="cfa06-mode" title="Toggle dark mode">
        <span class="cfa-06__sun" aria-hidden="true"><svg viewBox="0 0 24 24" width="13" height="13"><circle cx="12" cy="12" r="4.4" fill="currentColor"/><g stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M12 2.5v3M12 18.5v3M2.5 12h3M18.5 12h3M5 5l2.1 2.1M16.9 16.9L19 19M19 5l-2.1 2.1M7.1 16.9L5 19"/></g></svg></span>
        <span class="cfa-06__knob" aria-hidden="true"></span>
        <span class="cfa-06__moon" aria-hidden="true"><svg viewBox="0 0 24 24" width="13" height="13"><path d="M20 14.5A8.5 8.5 0 019.5 4a8.5 8.5 0 1010.5 10.5z" fill="currentColor"/></svg></span>
        <span class="cfa-06__sr">Force dark theme (off = follow system)</span>
      </label>
    </div>
    <header class="cfa-06__head">
      <h1>Frequently asked questions</h1>
      <p>Every color below is one <code>light-dark()</code> token. Flip the switch — or your OS theme — and watch the whole component re-skin.</p>
    </header>
    <div class="cfa-06__list">
      <details class="cfa-06__item" open>
        <summary class="cfa-06__q">Does dark mode save battery?<i aria-hidden="true"></i></summary>
        <div class="cfa-06__a"><p>On OLED screens, meaningfully — black pixels are unlit. On LCD panels the backlight runs regardless, so the gain is comfort, not power.</p></div>
      </details>
      <details class="cfa-06__item">
        <summary class="cfa-06__q">Why not just add a .dark class?<i aria-hidden="true"></i></summary>
        <div class="cfa-06__a"><p>Class-swapping duplicates every color rule and misses native UI: scrollbars, form controls and highlight colors stay light. color-scheme re-skins those for free and light-dark() keeps each token in one place.</p></div>
      </details>
      <details class="cfa-06__item">
        <summary class="cfa-06__q">Should dark mode be pure black?<i aria-hidden="true"></i></summary>
        <div class="cfa-06__a"><p>Usually no — near-black surfaces (this panel is oklch 0.21) reduce smearing on OLED and let shadows still read. Reserve true black for media canvases.</p></div>
      </details>
      <details class="cfa-06__item">
        <summary class="cfa-06__q">How do I persist the user's choice?<i aria-hidden="true"></i></summary>
        <div class="cfa-06__a"><p>Store one value ('light' / 'dark' / 'auto') in localStorage and restore it before first paint in a tiny inline script. The CSS here needs zero changes — you are only setting the checkbox.</p></div>
      </details>
    </div>
    <p class="cfa-06__foot">Unchecked = follow the OS (<code>color-scheme: light dark</code>). Checked = forced dark via <code>:has()</code>. CodeFronts collection.</p>
  </div>
</section>
```
## CSS
```css
.cfa-06,
.cfa-06 *,
.cfa-06 *::before,
.cfa-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cfa-06 {
  color-scheme: light dark;
  --bg: light-dark(oklch(0.975 0.008 250),oklch(0.15 0.02 258));
  --panel: light-dark(oklch(1 0 0),oklch(0.2 0.022 258));
  --ink: light-dark(oklch(0.22 0.025 258),oklch(0.95 0.006 250));
  --mut: light-dark(oklch(0.5 0.02 255),oklch(0.68 0.015 252));
  --line: light-dark(oklch(0.9 0.01 250),oklch(0.3 0.025 256));
  --acc: light-dark(oklch(0.55 0.19 255),oklch(0.75 0.14 250));
  --shadow: light-dark(oklch(0.3 0.05 255/.08),oklch(0 0 0/.35));
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(20px,4vw,56px);
  background: var(--bg);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  transition: background .45s,color .45s;
}

.cfa-06:has(#cfa06-mode:checked) {
  color-scheme: dark;
}

.cfa-06__wrap {
  width: min(100%,640px);
}

.cfa-06__bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
}

.cfa-06__brand {
  font-size: 14px;
  font-weight: 800;
  letter-spacing: -.01em;
}

.cfa-06__modecb {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.cfa-06__toggle {
  position: relative;
  display: flex;
  align-items: center;
  gap: 7px;
  min-height: 44px;
  padding: 6px 10px;
  border: 1px solid var(--line);
  border-radius: 99px;
  background: var(--panel);
  cursor: pointer;
  color: var(--mut);
  transition: border-color .3s,background .45s;
}

.cfa-06__toggle:hover {
  border-color: var(--acc);
}

.cfa-06__modecb:focus-visible ~ .cfa-06__toggle {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.cfa-06__knob {
  width: 34px;
  height: 20px;
  border-radius: 99px;
  background: var(--line);
  position: relative;
  transition: background .3s;
}

.cfa-06__knob::after {
  content: "";
  position: absolute;
  top: 3px;
  left: 3px;
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: var(--panel);
  box-shadow: 0 1px 4px var(--shadow);
  transition: translate .3s cubic-bezier(.4,0,.2,1),background .45s;
}

.cfa-06:has(#cfa06-mode:checked) .cfa-06__knob {
  background: var(--acc);
}

.cfa-06:has(#cfa06-mode:checked) .cfa-06__knob::after {
  translate: 14px 0;
}

.cfa-06__sun {
  color: oklch(0.72 0.15 75);
}

.cfa-06__moon {
  color: var(--mut);
}

.cfa-06:has(#cfa06-mode:checked) .cfa-06__moon {
  color: var(--acc);
}

.cfa-06__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.cfa-06__head {
  margin-top: 26px;
}

.cfa-06__head h1 {
  font-size: clamp(26px,4.5cqi,36px);
  font-weight: 800;
  letter-spacing: -.025em;
}

.cfa-06__head p {
  margin-top: 8px;
  font-size: 14px;
  line-height: 1.65;
  color: var(--mut);
}

.cfa-06__head code,
.cfa-06__foot code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .87em;
  background: color-mix(in oklch,var(--acc) 10%,transparent);
  padding: 2px 6px;
  border-radius: 5px;
  color: var(--acc);
}

.cfa-06__list {
  margin-top: 22px;
  display: flex;
  flex-direction: column;
  gap: 9px;
  interpolate-size: allow-keywords;
}

.cfa-06__item {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 13px;
  overflow: hidden;
  box-shadow: 0 4px 16px var(--shadow);
  transition: border-color .3s,background .45s,box-shadow .45s;
}

.cfa-06__item[open] {
  border-color: color-mix(in oklch,var(--acc) 40%,var(--line));
}

.cfa-06__q {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  min-height: 44px;
  padding: 15px 17px;
  cursor: pointer;
  font-size: 15px;
  font-weight: 650;
  list-style: none;
  transition: color .2s;
}

.cfa-06__q::-webkit-details-marker {
  display: none;
}

.cfa-06__q:hover {
  color: var(--acc);
}

.cfa-06__q:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
  border-radius: 13px;
}

.cfa-06__q i {
  flex: none;
  width: 9px;
  height: 9px;
  border-right: 2px solid var(--acc);
  border-bottom: 2px solid var(--acc);
  rotate: 45deg;
  translate: 0 -2px;
  transition: rotate .35s;
}

.cfa-06__item[open] .cfa-06__q i {
  rotate: 225deg;
  translate: 0 2px;
}

.cfa-06__a p {
  padding: 0 17px 16px;
  font-size: 13.5px;
  line-height: 1.7;
  color: var(--mut);
  max-width: 58ch;
}

@supports (interpolate-size: allow-keywords) {
  .cfa-06__item::details-content {
    height: 0;
    overflow: clip;
    opacity: 0;
    transition: height .38s cubic-bezier(.4,0,.2,1),opacity .3s,content-visibility .38s allow-discrete;
  }

  .cfa-06__item[open]::details-content {
    height: auto;
    opacity: 1;
  }
}

.cfa-06__foot {
  margin-top: 20px;
  font-size: 12.5px;
  color: var(--mut);
}

@media (prefers-reduced-motion: reduce) {
  .cfa-06 *,
    .cfa-06 .cfa-06__item::details-content {
    transition-duration: .01ms !important;
  }
}
```
