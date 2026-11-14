---
source: "codefronts"
url: "https://codefronts.com/navigation/css-mega-menus/panel-positioning-and-viewport-edge-collision/"
title: "Panel Positioning and Viewport Edge Collision"
section: "navigation"
category: "css-mega-menus"
category_name: "CSS Mega Menus"
description: "The panel that hangs off the last nav item, where a left-aligned panel runs straight off the right edge of the viewport."
has_js: "false"
---

Here's a working CSS Mega Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Panel Positioning and Viewport Edge Collision
Source: https://codefronts.com/navigation/css-mega-menus/panel-positioning-and-viewport-edge-collision/

The panel that hangs off the last nav item, where a left-aligned panel runs straight off the right edge of the viewport. This documentation header anchors from the trailing edge and clamps with max-inline-size, then upgrades to CSS Anchor Positioning with position-try-fallbacks behind an @supports gate so Chromium flips automatically and everything else keeps the clamp.
## HTML
```html
<section class="mm-05" aria-labelledby="mm-05-title">
  <h2 class="mm-05__sr" id="mm-05-title">Sable developer documentation</h2>

  <div class="mm-05__theme">
    <input class="mm-05__theme-input" type="checkbox" id="mm-05-theme">
    <label class="mm-05__theme-label" for="mm-05-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="mm-05__sr">Toggle dark theme</span>
    </label>
  </div>

  <header class="mm-05__header">
    <div class="mm-05__bar">
      <a class="mm-05__brand" href="#mm-05-title">
        <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 6h16v12H4Z" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M8 10h8M8 14h5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
        Sable <span>docs</span>
      </a>
      <span class="mm-05__version">v4.2</span>

      <span class="mm-05__search" aria-hidden="true">
        <svg viewBox="0 0 24 24" focusable="false"><circle cx="11" cy="11" r="6.5" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="m16 16 4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
        Search the docs
        <kbd>&#8984;K</kbd>
      </span>

      <nav class="mm-05__nav" aria-label="Primary">
        <ul class="mm-05__list">
          <li class="mm-05__item"><a class="mm-05__plain" href="#mm-05-title">Guides</a></li>
          <li class="mm-05__item"><a class="mm-05__plain" href="#mm-05-title">API</a></li>
          <li class="mm-05__item">
            <button class="mm-05__trigger" type="button" aria-expanded="false" aria-controls="mm-05-panel-resources">Resources
              <svg class="mm-05__chev" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
            </button>
            <div class="mm-05__panel" id="mm-05-panel-resources" aria-label="Resources">
              <div class="mm-05__grid">
                <section class="mm-05__col" aria-labelledby="mm-05-h-learn">
                  <h3 class="mm-05__col-head" id="mm-05-h-learn">Learn</h3>
                  <ul class="mm-05__links">
                    <li><a href="#mm-05-title">Quickstart</a></li>
                    <li><a href="#mm-05-title">Tutorials</a></li>
                    <li><a href="#mm-05-title">Example repos</a></li>
                  </ul>
                </section>
                <section class="mm-05__col" aria-labelledby="mm-05-h-ref">
                  <h3 class="mm-05__col-head" id="mm-05-h-ref">Reference</h3>
                  <ul class="mm-05__links">
                    <li><a href="#mm-05-title">CLI commands</a></li>
                    <li><a href="#mm-05-title">Error codes</a></li>
                    <li><a href="#mm-05-title">Rate limits</a></li>
                  </ul>
                </section>
              </div>
              <a class="mm-05__panel-cta" href="#mm-05-title">
                <b>Release notes &mdash; v4.2</b>
                <span>Regional read replicas and a smaller CLI binary.</span>
              </a>
            </div>
          </li>
        </ul>
      </nav>

      <a class="mm-05__ghost" href="#mm-05-title">Console</a>
    </div>
  </header>

  <main class="mm-05__page">
    <p class="mm-05__crumbs"><a href="#mm-05-title">Docs</a> / <a href="#mm-05-title">Guides</a> / Deploy</p>
    <h1 class="mm-05__h1">Deploying to the edge</h1>
    <p class="mm-05__lede">A first deploy takes one command and about ninety seconds. This guide covers the build step, region selection and rollback.</p>
    <pre class="mm-05__pre"><code>sable deploy --region eu-west-2 --canary 25</code></pre>
  </main>
</section>
```
## CSS
```css
.mm-05 {
  --mm-05-bg: #f1f5f9;
  --mm-05-surf: #ffffff;
  --mm-05-line: #cbd5e1;
  --mm-05-ink: #0f172a;
  --mm-05-mut: #64748b;
  --mm-05-acc: #0f766e;
  --mm-05-acc: oklch(48% 0.1 180);
  --mm-05-panel-w: 34rem;
  --mm-05-font-display: "Space Grotesk", ui-sans-serif, system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--mm-05-bg);
  color: var(--mm-05-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.6;
  overflow-x: clip;
}

.mm-05 *,
.mm-05 *::before,
.mm-05 *::after {
  box-sizing: border-box;
}

.mm-05 :focus-visible {
  outline: 2px solid var(--mm-05-acc);
  outline-offset: 3px;
  border-radius: 4px;
}

.mm-05__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.mm-05:has(.mm-05__theme-input:checked) {
  --mm-05-bg: #060a12;
  --mm-05-surf: #0f1729;
  --mm-05-line: #253046;
  --mm-05-ink: #e6edf7;
  --mm-05-mut: #94a3b8;
  --mm-05-acc: #2dd4bf;
  --mm-05-acc: oklch(80% 0.13 180);
}

@media (prefers-color-scheme: dark) {
  .mm-05 {
    --mm-05-bg: #060a12;
    --mm-05-surf: #0f1729;
    --mm-05-line: #253046;
    --mm-05-ink: #e6edf7;
    --mm-05-mut: #94a3b8;
    --mm-05-acc: #2dd4bf;
    --mm-05-acc: oklch(80% 0.13 180);
  }

  .mm-05:has(.mm-05__theme-input:checked) {
    --mm-05-bg: #f1f5f9;
    --mm-05-surf: #ffffff;
    --mm-05-line: #cbd5e1;
    --mm-05-ink: #0f172a;
    --mm-05-mut: #64748b;
    --mm-05-acc: #0f766e;
    --mm-05-acc: oklch(48% 0.1 180);
  }
}

@media (prefers-color-scheme: light) {
  .mm-05:has(.mm-05__theme-input:checked) {
    --mm-05-bg: #060a12;
    --mm-05-surf: #0f1729;
    --mm-05-line: #253046;
    --mm-05-ink: #e6edf7;
    --mm-05-mut: #94a3b8;
    --mm-05-acc: #2dd4bf;
    --mm-05-acc: oklch(80% 0.13 180);
  }
}

.mm-05__theme {
  position: absolute;
  inset-block-start: 11px;
  inset-inline-end: clamp(0.75rem, 3vw, 1.5rem);
  z-index: 60;
}

.mm-05__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.mm-05__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--mm-05-line);
  border-radius: 8px;
  background: var(--mm-05-surf);
  color: var(--mm-05-ink);
  cursor: pointer;
}

.mm-05__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.mm-05__theme-input:focus-visible + .mm-05__theme-label {
  outline: 2px solid var(--mm-05-acc);
  outline-offset: 3px;
}

.mm-05__header {
  position: relative;
  z-index: 10;
  inline-size: 100%;
  background: var(--mm-05-surf);
  border-block-end: 1px solid var(--mm-05-line);
}

.mm-05__bar {
  inline-size: min(76rem, calc(100% - 2rem));
  margin-inline: auto;
  display: flex;
  align-items: center;
  gap: 0.75rem;
  flex-wrap: wrap;
  min-block-size: 66px;
  padding-inline-end: 60px;
}

.mm-05__brand {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  color: var(--mm-05-ink);
  text-decoration: none;
  font: 700 1rem/1 var(--mm-05-font-display);
  letter-spacing: -0.03em;
}

.mm-05__brand span {
  color: var(--mm-05-mut);
  font-weight: 500;
}

.mm-05__brand svg {
  inline-size: 20px;
  block-size: 20px;
  color: var(--mm-05-acc);
}

.mm-05__version {
  display: inline-flex;
  align-items: center;
  block-size: 22px;
  padding-inline: 0.45rem;
  border: 1px solid var(--mm-05-line);
  border-radius: 999px;
  font: 600 0.68rem/1 var(--mm-05-font-display);
  color: var(--mm-05-mut);
}

.mm-05__search {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  min-block-size: 38px;
  padding-inline: 0.7rem;
  border: 1px solid var(--mm-05-line);
  border-radius: 8px;
  background: color-mix(in oklab, var(--mm-05-ink) 4%, transparent);
  color: var(--mm-05-mut);
  font-size: 0.83rem;
  min-inline-size: 0;
}

.mm-05__search svg {
  inline-size: 15px;
  block-size: 15px;
}

.mm-05__search kbd {
  padding: 0.1rem 0.3rem;
  border: 1px solid var(--mm-05-line);
  border-radius: 4px;
  font: 600 0.68rem/1.4 var(--mm-05-font-display);
}

.mm-05__nav {
  margin-inline-start: auto;
  min-inline-size: 0;
}

.mm-05__list {
  display: flex;
  flex-wrap: wrap;
  gap: 0.15rem;
  list-style: none;
  margin: 0;
  padding: 0;
  min-inline-size: 0;
}

.mm-05__item {
  position: relative;
}

.mm-05__trigger,
.mm-05__plain {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  min-block-size: 44px;
  padding-inline: 0.75rem;
  border: 0;
  border-radius: 8px;
  background: transparent;
  color: var(--mm-05-ink);
  font: 600 0.88rem/1 system-ui, sans-serif;
  text-decoration: none;
  cursor: pointer;
}

.mm-05__chev {
  inline-size: 14px;
  block-size: 14px;
}

.mm-05__item--open > .mm-05__trigger,
.mm-05__item:hover > .mm-05__trigger,
.mm-05__item:focus-within > .mm-05__trigger {
  background: color-mix(in oklab, var(--mm-05-acc) 14%, transparent);
  color: var(--mm-05-acc);
}

.mm-05__plain:hover,
.mm-05__trigger:hover {
  color: var(--mm-05-acc);
}

.mm-05__ghost {
  display: inline-flex;
  align-items: center;
  min-block-size: 40px;
  padding-inline: 0.9rem;
  border: 1px solid var(--mm-05-line);
  border-radius: 8px;
  color: var(--mm-05-ink);
  text-decoration: none;
  font: 600 0.85rem/1 system-ui, sans-serif;
}

.mm-05__ghost:hover {
  border-color: var(--mm-05-acc);
  color: var(--mm-05-acc);
}
/* Bridge the 8px gap between the trigger and the panel with transparent
   padding, so the pointer never crosses dead space on its way in. Without
   it, pointerleave fires on the item mid-travel and the panel closes before
   the cursor arrives — WCAG SC 1.4.13 requires hover content to be
   hoverable. background-clip keeps the padding transparent. */

.mm-05__panel {
  position: absolute;
  padding-block-start: 12px;
  margin-block-start: -12px;
  background-clip: content-box;
  inset-block-start: 100%;
  inset-inline-end: 0;
  z-index: 30;
  inline-size: min(var(--mm-05-panel-w), calc(100vw - 2rem));
  max-inline-size: min(var(--mm-05-panel-w), calc(100vw - 2rem));
  display: grid;
  gap: 0.75rem;
  padding: clamp(0.9rem, 2.4vw, 1.2rem);
  border: 1px solid var(--mm-05-line);
  border-radius: 12px;
  background: var(--mm-05-surf);
  box-shadow: 0 24px 54px -30px rgba(15, 23, 42, 0.55);
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transform: translateY(-6px);
  transition: opacity 150ms ease, transform 150ms ease, visibility 0s linear 150ms;
}

.mm-05__item--open > .mm-05__panel,
.mm-05__item:focus-within > .mm-05__panel {
  opacity: 1;
  visibility: visible;
  pointer-events: auto;
  transform: translateY(0);
  transition-delay: 0s;
}

@media (hover: hover) {
  .mm-05__item:hover > .mm-05__panel {
    opacity: 1;
    visibility: visible;
    pointer-events: auto;
    transform: translateY(0);
    transition-delay: 0s;
  }
}

@supports (anchor-name: --mm-05-a) {
  .mm-05__trigger {
    anchor-name: --mm-05-a;
  }
  /* position:fixed pairs with the physical anchor() keywords — anchor(block-end)
       resolves to 0 here and drops the panel to the foot of the viewport, so the
       block axis uses anchor(bottom).
       Anchored to the trigger, so the panel's right edge lines up with the
       trigger's right edge. With position-anchor set, inset-inline-end
       resolves against the anchor itself, so anchor(right) alone aligns the
       two right edges. Writing calc(100% - anchor(right)) here double-counts
       and pushes the panel one trigger-width to the left. */

  .mm-05__item--open > .mm-05__panel,
    .mm-05__item:hover > .mm-05__panel,
    .mm-05__item:focus-within > .mm-05__panel {
    position: fixed;
    position-anchor: --mm-05-a;
    inset-block-start: calc(anchor(bottom) + 8px);
    inset-inline-start: auto;
    inset-inline-end: anchor(right);
    max-inline-size: min(var(--mm-05-panel-w), calc(100vw - 2rem));
    /* Keep the panel inside the viewport when the trigger sits near the
           right edge — the collision case this demo is about. */
    position-try-fallbacks: flip-inline;
  }
}

.mm-05__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 9rem), 1fr));
  gap: 0.5rem 1.25rem;
}

.mm-05__col {
  min-inline-size: 0;
}

.mm-05__col-head {
  margin: 0 0 0.25rem;
  font: 700 0.66rem/1 var(--mm-05-font-display);
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--mm-05-mut);
}

.mm-05__links {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 1px;
}

.mm-05__links a {
  display: flex;
  align-items: center;
  min-block-size: 44px;
  padding-inline: 0.45rem;
  margin-inline: -0.45rem;
  border-radius: 6px;
  color: var(--mm-05-ink);
  text-decoration: none;
  font-size: 0.88rem;
}

.mm-05__links a:hover {
  background: color-mix(in oklab, var(--mm-05-acc) 10%, transparent);
  color: var(--mm-05-acc);
}

.mm-05__panel-cta {
  display: grid;
  gap: 2px;
  padding: 0.75rem 0.85rem;
  border-radius: 10px;
  background: color-mix(in oklab, var(--mm-05-acc) 12%, transparent);
  color: var(--mm-05-ink);
  text-decoration: none;
}

.mm-05__panel-cta b {
  font: 600 0.88rem/1.2 var(--mm-05-font-display);
  color: var(--mm-05-acc);
}

.mm-05__panel-cta span {
  font-size: 0.8rem;
  color: var(--mm-05-mut);
  text-wrap: pretty;
}

.mm-05__page {
  inline-size: min(48rem, calc(100% - 2rem));
  margin-inline: auto;
  padding-block: clamp(2.5rem, 8vw, 5rem);
  display: grid;
  gap: 0.9rem;
}

.mm-05__crumbs {
  margin: 0;
  font: 500 0.8rem/1 var(--mm-05-font-display);
  color: var(--mm-05-mut);
}

.mm-05__crumbs a {
  color: var(--mm-05-mut);
  text-decoration: none;
}

.mm-05__crumbs a:hover {
  color: var(--mm-05-acc);
}

.mm-05__h1 {
  margin: 0;
  font: 700 clamp(1.9rem, 5.5vw, 3rem)/1.08 var(--mm-05-font-display);
  letter-spacing: -0.035em;
  text-wrap: balance;
}

.mm-05__lede {
  margin: 0;
  color: var(--mm-05-mut);
  font-size: clamp(0.95rem, 2.2vw, 1.08rem);
  text-wrap: pretty;
}

.mm-05__pre {
  margin: 0.4rem 0 0;
  padding: 1rem 1.1rem;
  overflow-x: auto;
  border: 1px solid var(--mm-05-line);
  border-radius: 10px;
  background: var(--mm-05-surf);
  font: 500 0.85rem/1.6 ui-monospace, SFMono-Regular, Menlo, monospace;
  color: var(--mm-05-acc);
}

@media (max-width: 56rem) {
  .mm-05__bar {
    flex-direction: column;
    align-items: stretch;
    padding-block: 0.6rem;
  }

  .mm-05__nav {
    margin-inline-start: 0;
  }

  .mm-05__list {
    flex-direction: column;
  }

  .mm-05__panel {
    position: static;
    inline-size: 100%;
    max-inline-size: 100%;
    opacity: 1;
    visibility: visible;
    transform: none;
    box-shadow: none;
    display: none;
    margin-block-start: 0.5rem;
  }

  .mm-05__item--open > .mm-05__panel,
    .mm-05__item:focus-within > .mm-05__panel {
    display: grid;
  }

  @supports (anchor-name: --mm-05-a) {
    .mm-05__item:hover > .mm-05__panel,
        .mm-05__item:focus-within > .mm-05__panel {
      position: static;
      inset: auto;
    }
  }
}

@media (prefers-reduced-motion: reduce) {
  .mm-05__panel {
    transition-duration: 1ms;
  }
}
/* Entry signature — the panel body scales out of the anchored corner; no per-row stagger */

.mm-05__grid {
  opacity: 0;
  scale: 0.97;
  transform-origin: 100% 0;
  transition: opacity 180ms ease, scale 300ms cubic-bezier(0.22, 1, 0.36, 1);
}

.mm-05__panel-cta {
  opacity: 0;
  transition: opacity 220ms ease 90ms;
}

.mm-05__item:hover > .mm-05__panel .mm-05__grid,
.mm-05__item:focus-within > .mm-05__panel .mm-05__grid,
.mm-05__item--open > .mm-05__panel .mm-05__grid {
  opacity: 1;
  scale: 1;
}

.mm-05__item:hover > .mm-05__panel .mm-05__panel-cta,
.mm-05__item:focus-within > .mm-05__panel .mm-05__panel-cta,
.mm-05__item--open > .mm-05__panel .mm-05__panel-cta {
  opacity: 1;
}

@media (prefers-reduced-motion: reduce) {
  .mm-05__grid,
    .mm-05__panel-cta {
    transition-duration: 1ms;
    transition-delay: 0s;
    animation: none;
  }

  .mm-05__grid {
    opacity: 1;
    scale: 1;
  }

  .mm-05__panel-cta {
    opacity: 1;
  }
}
```
