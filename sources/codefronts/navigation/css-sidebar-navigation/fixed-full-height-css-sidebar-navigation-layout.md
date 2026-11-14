---
source: "codefronts"
url: "https://codefronts.com/navigation/css-sidebar-navigation/fixed-full-height-css-sidebar-navigation-layout/"
title: "Sticky Full Height Sidebar Layout Mechanics"
section: "navigation"
category: "css-sidebar-navigation"
category_name: "CSS Sidebar Navigation"
description: "Why height: 100% on a grid child silently fails, and why position: sticky needs a containing block taller than itself."
has_js: "true"
---

Here's a working CSS Sidebar Navigation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sticky Full Height Sidebar Layout Mechanics
Source: https://codefronts.com/navigation/css-sidebar-navigation/fixed-full-height-css-sidebar-navigation-layout/

Why height: 100% on a grid child silently fails, and why position: sticky needs a containing block taller than itself. These are the two mechanics behind every full-height sidebar, and both fail without an error &mdash; the rail simply is not full height, or simply does not stick. The build here is the version that works: no height declaration on the rail at all, and align-self: start giving sticky the room it needs.
## HTML
```html
<section class="sdb-17" aria-label="Talon editor">
  <div class="sdb-17__theme">
    <input class="sdb-17__theme-input" type="checkbox" id="sdb-17-theme">
    <label class="sdb-17__theme-label" for="sdb-17-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sdb-17__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="sdb-17__app">
    <nav class="sdb-17__rail" aria-label="Talon explorer">
      <p class="sdb-17__rail-title">Explorer</p>
      <ul class="sdb-17__list">
        <li><a class="sdb-17__link" href="#sdb-17-code" aria-current="page">index.ts</a></li>
        <li><a class="sdb-17__link" href="#sdb-17-code">router.ts</a></li>
        <li><a class="sdb-17__link" href="#sdb-17-code">tokens.css</a></li>
        <li><a class="sdb-17__link" href="#sdb-17-code">shell.tsx</a></li>
        <li><a class="sdb-17__link" href="#sdb-17-code">rail.tsx</a></li>
        <li><a class="sdb-17__link" href="#sdb-17-code">measure.ts</a></li>
      </ul>
    </nav>

    <div class="sdb-17__code" id="sdb-17-code">
      <p class="sdb-17__tab">shell.tsx</p>
      <pre class="sdb-17__pre">.shell {
  display: grid;
  grid-template-columns:
    minmax(0, 13rem) minmax(0, 1fr);
  block-size: 100dvh;
  overflow-y: auto;
}

/* no height declaration on the rail:
   align-items: stretch already gives
   the column its full height */
.rail {
  align-self: start;
  position: sticky;
  inset-block-start: 0;
}

.code { min-inline-size: 0; }

export function mount(root) {
  const rail = root.querySelector('.rail');
  const routes = ['overview', 'deploy'];
  render(routes[0]);
  return () =&gt; rail.remove();
}

observe(rail, () =&gt; {
  measure(rail).height;
});

// keep scrolling — the rail holds its
// position because its containing block
// is taller than it is
scroll(0);
flush();
teardown();

const active = routes[0];
render(active);
observe(rail, () =&gt; measure(rail));
scroll(240);
flush();</pre>
    </div>
  </div>
</section>
```
## CSS
```css
.sdb-17 {
  --sdb-17-bg: #06070a;
  --sdb-17-surf: #0d0f14;
  --sdb-17-surf2: #13161d;
  --sdb-17-line: #1e2330;
  --sdb-17-ink: #e7ecf4;
  --sdb-17-mut: #8b95a8;
  --sdb-17-acc: #45e2e0;
  --sdb-17-acc: oklch(85% 0.13 190);
  --sdb-17-acc-soft: #0d2b30;
  --sdb-17-font-display: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--sdb-17-bg);
  color: var(--sdb-17-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.sdb-17 *,
.sdb-17 *::before,
.sdb-17 *::after {
  box-sizing: border-box;
}

.sdb-17:has(.sdb-17__theme-input:checked) {
  --sdb-17-bg: #f5f7fa;
  --sdb-17-surf: #ffffff;
  --sdb-17-surf2: #eaeef4;
  --sdb-17-line: #d3dae4;
  --sdb-17-ink: #0d1117;
  --sdb-17-mut: #566072;
  --sdb-17-acc: #0a6d72;
  --sdb-17-acc: oklch(45% 0.09 195);
  --sdb-17-acc-soft: #d6eef0;
}

@media (prefers-color-scheme: light) {
  .sdb-17 {
    --sdb-17-bg: #f5f7fa;
    --sdb-17-surf: #ffffff;
    --sdb-17-surf2: #eaeef4;
    --sdb-17-line: #d3dae4;
    --sdb-17-ink: #0d1117;
    --sdb-17-mut: #566072;
    --sdb-17-acc: #0a6d72;
    --sdb-17-acc: oklch(45% 0.09 195);
    --sdb-17-acc-soft: #d6eef0;
  }

  .sdb-17:has(.sdb-17__theme-input:checked) {
    --sdb-17-bg: #06070a;
    --sdb-17-surf: #0d0f14;
    --sdb-17-surf2: #13161d;
    --sdb-17-line: #1e2330;
    --sdb-17-ink: #e7ecf4;
    --sdb-17-mut: #8b95a8;
    --sdb-17-acc: #45e2e0;
    --sdb-17-acc: oklch(85% 0.13 190);
    --sdb-17-acc-soft: #0d2b30;
  }
}

@media (prefers-color-scheme: dark) {
  .sdb-17:has(.sdb-17__theme-input:checked) {
    --sdb-17-bg: #f5f7fa;
    --sdb-17-surf: #ffffff;
    --sdb-17-surf2: #eaeef4;
    --sdb-17-line: #d3dae4;
    --sdb-17-ink: #0d1117;
    --sdb-17-mut: #566072;
    --sdb-17-acc: #0a6d72;
    --sdb-17-acc: oklch(45% 0.09 195);
    --sdb-17-acc-soft: #d6eef0;
  }
}

.sdb-17__theme {
  position: absolute;
  inset-block-start: 0.85rem;
  inset-inline-end: 0.85rem;
  z-index: 60;
}

.sdb-17__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.sdb-17__theme-label {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border: 1px solid var(--sdb-17-line);
  background: var(--sdb-17-surf2);
  color: var(--sdb-17-ink);
  cursor: pointer;
}

.sdb-17__theme-label svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.sdb-17__theme-input:focus-visible + .sdb-17__theme-label {
  outline: 2px solid var(--sdb-17-acc);
  outline-offset: 2px;
}

.sdb-17__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}
/* The shell is the scroll container and align-items: stretch gives the rail its
   height — no height declaration on the rail itself. */

.sdb-17__app {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  block-size: 100dvh;
  overflow-y: auto;
  background: var(--sdb-17-surf);
}

@media (min-width: 40rem) {
  .sdb-17__app {
    grid-template-columns: minmax(0, 13rem) minmax(0, 1fr);
  }
}

.sdb-17__rail {
  min-inline-size: 0;
  align-self: start;
  position: sticky;
  inset-block-start: 0;
  z-index: 2;
  background: var(--sdb-17-surf2);
  border-inline-end: 1px solid var(--sdb-17-line);
  padding: 0.6rem 0.4rem;
}

.sdb-17__rail-title {
  margin: 0 0 0.4rem;
  padding-inline: 0.45rem;
  font-family: var(--sdb-17-font-display);
  font-size: 0.7rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--sdb-17-mut);
}

.sdb-17__list {
  list-style: none;
  margin: 0;
  padding: 0;
}

.sdb-17__link {
  display: flex;
  align-items: center;
  min-block-size: 2.75rem;
  padding: 0.4rem 0.5rem;
  font-family: var(--sdb-17-font-display);
  font-size: 0.8rem;
  color: var(--sdb-17-ink);
  text-decoration: none;
  min-inline-size: 0;
}

.sdb-17__link:hover {
  background: var(--sdb-17-surf);
}

.sdb-17__link[aria-current="page"] {
  background: var(--sdb-17-acc-soft);
  color: var(--sdb-17-acc);
}

.sdb-17__link:focus-visible {
  outline: 2px solid var(--sdb-17-acc);
  outline-offset: -2px;
}

.sdb-17__code {
  min-inline-size: 0;
  padding: 0.7rem 1rem 3rem;
}

.sdb-17__tab {
  margin: 0 0 0.7rem;
  font-family: var(--sdb-17-font-display);
  font-size: 0.72rem;
  letter-spacing: 0.06em;
  color: var(--sdb-17-acc);
}

.sdb-17__pre {
  margin: 0;
  font-family: var(--sdb-17-font-display);
  font-size: 0.78rem;
  line-height: 1.85;
  color: var(--sdb-17-mut);
  white-space: pre;
}
```
