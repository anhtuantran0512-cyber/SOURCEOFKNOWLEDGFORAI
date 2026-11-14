---
source: "codefronts"
url: "https://codefronts.com/navigation/css-sidebar-navigation/pure-css-collapsible-sidebar-navigation-snippet/"
title: "Collapsible Sidebar with Checkbox State"
section: "navigation"
category: "css-sidebar-navigation"
category_name: "CSS Sidebar Navigation"
description: "The no-script collapse: a visually hidden checkbox, :has(:checked) on the root, and one width custom property doing all the work."
has_js: "false"
---

Here's a working CSS Sidebar Navigation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Collapsible Sidebar with Checkbox State
Source: https://codefronts.com/navigation/css-sidebar-navigation/pure-css-collapsible-sidebar-navigation-snippet/

The no-script collapse: a visually hidden checkbox, :has(:checked) on the root, and one width custom property doing all the work. One honest limitation: a checkbox cannot carry aria-expanded, so the pattern needs a clearly labelled control, and the scripted version in demo 05 is the accessible ceiling. css-side-menu covers the look; this is the state mechanism under it.
## HTML
```html
<section class="sdb-11" aria-label="Vale account settings">
  <div class="sdb-11__theme">
    <input class="sdb-11__theme-input" type="checkbox" id="sdb-11-theme">
    <label class="sdb-11__theme-label" for="sdb-11-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sdb-11__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="sdb-11__app">
    <input class="sdb-11__state" type="checkbox" id="sdb-11-collapse">
    <aside class="sdb-11__rail">
      <div class="sdb-11__rail-head">
        <label class="sdb-11__toggle" for="sdb-11-collapse">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 6h16M4 12h16M4 18h16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
          <span class="sdb-11__toggle-open">Collapse</span>
          <span class="sdb-11__toggle-shut">Expand</span>
        </label>
      </div>
      <nav class="sdb-11__nav" aria-label="Vale account settings">
        <ul class="sdb-11__list">
          <li><a class="sdb-11__link" href="#sdb-11-main" aria-current="page"><span class="sdb-11__glyph" aria-hidden="true">&#9679;</span><span class="sdb-11__label">Profile</span></a></li>
          <li><a class="sdb-11__link" href="#sdb-11-main"><span class="sdb-11__glyph" aria-hidden="true">&#9679;</span><span class="sdb-11__label">Notifications</span></a></li>
          <li><a class="sdb-11__link" href="#sdb-11-main"><span class="sdb-11__glyph" aria-hidden="true">&#9679;</span><span class="sdb-11__label">Security</span></a></li>
          <li><a class="sdb-11__link" href="#sdb-11-main"><span class="sdb-11__glyph" aria-hidden="true">&#9679;</span><span class="sdb-11__label">Billing</span></a></li>
          <li><a class="sdb-11__link" href="#sdb-11-main"><span class="sdb-11__glyph" aria-hidden="true">&#9679;</span><span class="sdb-11__label">API keys</span></a></li>
        </ul>
      </nav>
      <p class="sdb-11__rail-foot"><span class="sdb-11__label">Signed in as Priya Sharma</span></p>
    </aside>

    <main class="sdb-11__main" id="sdb-11-main">
      <h2 class="sdb-11__main-h">Profile</h2>
      <dl class="sdb-11__fields">
        <div><dt>Display name</dt><dd>Priya Sharma</dd></div>
        <div><dt>Workspace</dt><dd>Vale &middot; Operations</dd></div>
        <div><dt>Time zone</dt><dd>Europe/Lisbon (UTC+1)</dd></div>
        <div><dt>Two-factor</dt><dd>Authenticator app</dd></div>
        <div><dt>Recovery email</dt><dd>[email protected]</dd></div>
        <div><dt>Member since</dt><dd>March 2024</dd></div>
      </dl>
    </main>
  </div>
</section>
```
## CSS
```css
.sdb-11 {
  --sdb-11-bg: #f5f1ee;
  --sdb-11-surf: #fffcfa;
  --sdb-11-surf2: #ebe3dd;
  --sdb-11-line: #d9cdc4;
  --sdb-11-ink: #241c17;
  --sdb-11-mut: #6d5c52;
  --sdb-11-acc: #7d4a35;
  --sdb-11-acc: oklch(46% 0.09 40);
  --sdb-11-acc-soft: #eee0d8;
  --sdb-11-w-open: 15rem;
  --sdb-11-w-rail: 4.5rem;
  --sdb-11-w: var(--sdb-11-w-open);
  --sdb-11-font-display: "Avenir Next Rounded", Nunito, "Trebuchet MS", ui-rounded, system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--sdb-11-bg);
  color: var(--sdb-11-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.sdb-11 *,
.sdb-11 *::before,
.sdb-11 *::after {
  box-sizing: border-box;
}

.sdb-11:has(.sdb-11__state:checked) {
  --sdb-11-w: var(--sdb-11-w-rail);
}

.sdb-11:has(.sdb-11__theme-input:checked) {
  --sdb-11-bg: #14100e;
  --sdb-11-surf: #1c1714;
  --sdb-11-surf2: #251e1a;
  --sdb-11-line: #362c26;
  --sdb-11-ink: #f1e9e3;
  --sdb-11-mut: #a89689;
  --sdb-11-acc: #dda183;
  --sdb-11-acc: oklch(78% 0.09 45);
  --sdb-11-acc-soft: #32241d;
}

@media (prefers-color-scheme: dark) {
  .sdb-11 {
    --sdb-11-bg: #14100e;
    --sdb-11-surf: #1c1714;
    --sdb-11-surf2: #251e1a;
    --sdb-11-line: #362c26;
    --sdb-11-ink: #f1e9e3;
    --sdb-11-mut: #a89689;
    --sdb-11-acc: #dda183;
    --sdb-11-acc: oklch(78% 0.09 45);
    --sdb-11-acc-soft: #32241d;
  }

  .sdb-11:has(.sdb-11__theme-input:checked) {
    --sdb-11-bg: #f5f1ee;
    --sdb-11-surf: #fffcfa;
    --sdb-11-surf2: #ebe3dd;
    --sdb-11-line: #d9cdc4;
    --sdb-11-ink: #241c17;
    --sdb-11-mut: #6d5c52;
    --sdb-11-acc: #7d4a35;
    --sdb-11-acc: oklch(46% 0.09 40);
    --sdb-11-acc-soft: #eee0d8;
  }
}

@media (prefers-color-scheme: light) {
  .sdb-11:has(.sdb-11__theme-input:checked) {
    --sdb-11-bg: #14100e;
    --sdb-11-surf: #1c1714;
    --sdb-11-surf2: #251e1a;
    --sdb-11-line: #362c26;
    --sdb-11-ink: #f1e9e3;
    --sdb-11-mut: #a89689;
    --sdb-11-acc: #dda183;
    --sdb-11-acc: oklch(78% 0.09 45);
    --sdb-11-acc-soft: #32241d;
  }
}

.sdb-11__theme {
  position: absolute;
  inset-block-start: 0.85rem;
  inset-inline-end: 0.85rem;
  z-index: 60;
}

.sdb-11__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.sdb-11__theme-label {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border-radius: 1.4rem;
  border: 0;
  background: var(--sdb-11-surf2);
  color: var(--sdb-11-ink);
  cursor: pointer;
}

.sdb-11__theme-label svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.sdb-11__theme-input:focus-visible + .sdb-11__theme-label {
  outline: 2px solid var(--sdb-11-acc);
  outline-offset: 2px;
}

.sdb-11__sr,
.sdb-11__state {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  margin: 0;
}

.sdb-11__app {
  display: flex;
  min-inline-size: 0;
  min-block-size: 100vh;
  background: var(--sdb-11-surf);
}

.sdb-11__rail {
  flex: none;
  inline-size: var(--sdb-11-w);
  min-inline-size: 0;
  display: flex;
  flex-direction: column;
  background: var(--sdb-11-surf2);
  transition: inline-size 200ms ease;
}

.sdb-11__rail-head {
  padding: 0.6rem;
}

.sdb-11__toggle {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  min-block-size: 2.75rem;
  padding-inline: 0.7rem;
  border-radius: 1.4rem;
  background: var(--sdb-11-surf);
  cursor: pointer;
  font-size: 0.86rem;
  font-weight: 600;
  white-space: nowrap;
  min-inline-size: 2.75rem;
}

.sdb-11__toggle svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
  flex: none;
}

.sdb-11__state:focus-visible ~ .sdb-11__rail .sdb-11__toggle {
  outline: 2px solid var(--sdb-11-acc);
  outline-offset: 2px;
}

.sdb-11__toggle-shut {
  display: none;
}

.sdb-11:has(.sdb-11__state:checked) .sdb-11__toggle-open {
  display: none;
}

.sdb-11:has(.sdb-11__state:checked) .sdb-11__toggle-shut,
.sdb-11:has(.sdb-11__state:checked) .sdb-11__toggle span {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sdb-11:has(.sdb-11__state:checked) .sdb-11__toggle {
  justify-content: center;
  padding-inline: 0;
}

.sdb-11__nav {
  flex: 1;
  min-block-size: 0;
  padding: 0.2rem 0.6rem;
}

.sdb-11__list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 0.15rem;
}

.sdb-11__link {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  min-block-size: 2.75rem;
  padding: 0.5rem 0.7rem;
  border-radius: 1.4rem;
  color: var(--sdb-11-ink);
  text-decoration: none;
  font-size: 0.92rem;
  white-space: nowrap;
  min-inline-size: 0;
}

.sdb-11__glyph {
  flex: none;
  font-size: 0.6rem;
  color: var(--sdb-11-mut);
}

.sdb-11__link:hover {
  background: var(--sdb-11-surf);
}

.sdb-11__link[aria-current="page"] {
  background: var(--sdb-11-acc);
  color: var(--sdb-11-surf);
  font-weight: 650;
}

.sdb-11__link[aria-current="page"] .sdb-11__glyph {
  color: inherit;
}

.sdb-11__link:focus-visible {
  outline: 2px solid var(--sdb-11-acc);
  outline-offset: 2px;
}

.sdb-11__rail-foot {
  margin: 0;
  padding: 0.7rem 1rem 0.9rem;
  font-size: 0.78rem;
  color: var(--sdb-11-mut);
  white-space: nowrap;
  overflow: hidden;
}

.sdb-11__label {
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
}

.sdb-11:has(.sdb-11__state:checked) .sdb-11__label {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sdb-11:has(.sdb-11__state:checked) .sdb-11__link {
  justify-content: center;
  gap: 0;
}

.sdb-11__main {
  flex: 1;
  min-inline-size: 0;
  padding: 1.5rem 1.25rem 2.5rem;
}

@media (min-width: 46rem) {
  .sdb-11__main {
    padding: 2.4rem 2.25rem 3rem;
  }
}

.sdb-11__main-h {
  margin: 0 0 1.2rem;
  font-family: var(--sdb-11-font-display);
  font-size: clamp(1.35rem, 3.4vw, 1.9rem);
  line-height: 1.15;
}

.sdb-11__fields {
  margin: 0;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 0.6rem;
  max-inline-size: 44rem;
}

@media (min-width: 34rem) {
  .sdb-11__fields {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

.sdb-11__fields div {
  min-inline-size: 0;
  padding: 0.75rem 0.9rem;
  border-radius: 0.9rem;
  background: var(--sdb-11-surf2);
}

.sdb-11__fields dt {
  font-size: 0.72rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--sdb-11-mut);
}

.sdb-11__fields dd {
  margin: 0.15rem 0 0;
  font-size: 0.92rem;
}

@media (max-width: 30rem) {
  .sdb-11__app {
    flex-direction: column;
  }

  .sdb-11__rail,
    .sdb-11:has(.sdb-11__state:checked) .sdb-11__rail {
    inline-size: 100%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sdb-11__rail {
    transition: none;
  }
}
```
