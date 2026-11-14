---
source: "codefronts"
url: "https://codefronts.com/components/css-pricing-tables/dark-light-mode-adaptive-cards/"
title: "Dark / Light Mode Adaptive Cards"
section: "components"
category: "css-pricing-tables"
category_name: "CSS Pricing Tables"
description: "Theme-aware pricing done the maintainable way: every color in the component reads from a handful of custom properties, so one checkbox retints backgrounds,…"
has_js: "false"
---

Here's a working CSS Pricing Table from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark / Light Mode Adaptive Cards
Source: https://codefronts.com/components/css-pricing-tables/dark-light-mode-adaptive-cards/

Theme-aware pricing done the maintainable way: every color in the component reads from a handful of custom properties, so one checkbox retints backgrounds, borders, gradients and type contrast in a single smooth transition — the exact pattern for sites with a global theme toggle.
## HTML
```html
<section class="prc-04" aria-label="Theme-adaptive pricing cards">
  <header class="prc-04__head">
    <h2>Looks right in any theme</h2>
    <input type="checkbox" id="prc-04-theme" class="prc-04__sr" aria-label="Switch to dark theme">
    <label for="prc-04-theme" class="prc-04__switch" aria-hidden="true"><span class="prc-04__sun">☀</span><span class="prc-04__moon">☾</span><span class="prc-04__thumb"></span></label>
  </header>
  <div class="prc-04__grid">
    <article class="prc-04__card"><h3>Solo</h3><p class="prc-04__price">$8<small>/mo</small></p><ul><li>1 workspace</li><li>Core blocks</li></ul><a href="#" class="prc-04__cta">Choose Solo</a></article>
    <article class="prc-04__card prc-04__card--hot"><span class="prc-04__flag">Most popular</span><h3>Craft</h3><p class="prc-04__price">$20<small>/mo</small></p><ul><li>5 workspaces</li><li>All blocks</li><li>Version history</li></ul><a href="#" class="prc-04__cta prc-04__cta--hot">Choose Craft</a></article>
    <article class="prc-04__card"><h3>Studio</h3><p class="prc-04__price">$45<small>/mo</small></p><ul><li>Unlimited workspaces</li><li>Team roles</li></ul><a href="#" class="prc-04__cta">Choose Studio</a></article>
  </div>
</section>
```
## CSS
```css
.prc-04,
.prc-04 *,
.prc-04 *::before,
.prc-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.prc-04 {
  --bg: #f4f2ec;
  --surface: #ffffff;
  --line: #e3e0d6;
  --ink: #211f1a;
  --mut: #7a766a;
  --accent: oklch(0.6 0.15 60);
  --accent-ink: #fff;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: var(--bg);
  color: var(--ink);
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 56px 24px;
  transition: background-color .5s;
}

.prc-04:has(.prc-04__sr:checked) {
  --bg: #14130f;
  --surface: #1e1c16;
  --line: #333026;
  --ink: #f0ede2;
  --mut: #9a9584;
  --accent: oklch(0.75 0.14 75);
  --accent-ink: #1a1812;
}

.prc-04__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  clip-path: inset(50%);
  overflow: hidden;
  white-space: nowrap;
}

.prc-04__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: min(880px,100%);
  margin: 0 auto 34px;
}

.prc-04__head h2 {
  font-size: clamp(24px,3.6vw,34px);
  font-weight: 800;
  letter-spacing: -.02em;
}

.prc-04__switch {
  position: relative;
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 6px 10px;
  border-radius: 99px;
  background: var(--surface);
  border: 1px solid var(--line);
  cursor: pointer;
  font-size: 14px;
  transition: background-color .5s,border-color .5s;
}

.prc-04__sun,
.prc-04__moon {
  position: relative;
  z-index: 1;
  width: 22px;
  text-align: center;
  transition: opacity .3s;
}

.prc-04__moon {
  opacity: .4;
}

.prc-04:has(.prc-04__sr:checked) .prc-04__sun {
  opacity: .4;
}

.prc-04:has(.prc-04__sr:checked) .prc-04__moon {
  opacity: 1;
}

.prc-04__thumb {
  position: absolute;
  inset: 4px auto 4px 4px;
  width: 30px;
  border-radius: 99px;
  background: var(--accent);
  opacity: .18;
  transition: transform .35s cubic-bezier(.5,1.5,.4,1);
}

.prc-04:has(.prc-04__sr:checked) .prc-04__thumb {
  transform: translateX(28px);
}

.prc-04__sr:focus-visible + .prc-04__switch {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

.prc-04__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(220px,1fr));
  gap: 18px;
  width: min(880px,100%);
  margin: 0 auto;
}

.prc-04__card {
  position: relative;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 18px;
  padding: 28px;
  display: flex;
  flex-direction: column;
  gap: 14px;
  transition: background-color .5s,border-color .5s;
}

.prc-04__card--hot {
  border-color: var(--accent);
}

.prc-04__flag {
  position: absolute;
  top: -11px;
  left: 24px;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
  padding: 4px 10px;
  border-radius: 99px;
  background: var(--accent);
  color: var(--accent-ink);
  transition: background-color .5s,color .5s;
}

.prc-04__card h3 {
  font-size: 14px;
  font-weight: 700;
  letter-spacing: .05em;
  text-transform: uppercase;
  color: var(--mut);
  transition: color .5s;
}

.prc-04__price {
  font-size: 42px;
  font-weight: 800;
  letter-spacing: -.03em;
}

.prc-04__price small {
  font-size: 15px;
  font-weight: 600;
  color: var(--mut);
}

.prc-04__card ul {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 8px;
  font-size: 14px;
  color: var(--mut);
  flex: 1;
  transition: color .5s;
}

.prc-04__card li::before {
  content: "✓";
  color: var(--accent);
  font-weight: 700;
  margin-right: 8px;
}

.prc-04__cta {
  text-align: center;
  text-decoration: none;
  font-weight: 700;
  font-size: 13.5px;
  padding: 12px;
  border-radius: 11px;
  border: 1.5px solid var(--line);
  color: var(--ink);
  transition: border-color .3s,background-color .5s,color .5s;
}

.prc-04__cta:hover {
  border-color: var(--accent);
}

.prc-04__cta--hot {
  background: var(--accent);
  border-color: var(--accent);
  color: var(--accent-ink);
}

.prc-04__cta:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .prc-04,
    .prc-04 * {
    transition-duration: .01s!important;
  }
}
```

## JavaScript
```js
/* No JavaScript — the whole palette lives in custom properties on .prc-04; one :has(:checked) rule overrides them for dark mode and every themed element crossfades via shared transitions. Point the override at your site's [data-theme] attribute in production. */
```
