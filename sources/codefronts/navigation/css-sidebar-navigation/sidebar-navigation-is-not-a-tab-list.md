---
source: "codefronts"
url: "https://codefronts.com/navigation/css-sidebar-navigation/sidebar-navigation-is-not-a-tab-list/"
title: "Sidebar Navigation Is Not a Tab List"
section: "navigation"
category: "css-sidebar-navigation"
category_name: "CSS Sidebar Navigation"
description: "Applying role=\"tablist\" to site navigation because it looks like a vertical strip is a frequent and serious mistake."
has_js: "false"
---

Here's a working CSS Sidebar Navigation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sidebar Navigation Is Not a Tab List
Source: https://codefronts.com/navigation/css-sidebar-navigation/sidebar-navigation-is-not-a-tab-list/

Applying role="tablist" to site navigation because it looks like a vertical strip is a frequent and serious mistake. Tabs promise that activating an item swaps a panel in place; navigation promises a page change. Get it wrong and a screen-reader user is told the wrong thing about what will happen, and inherits arrow-key conventions navigation should not have. The rail here is the navigation build: a named landmark, a list of links, and aria-current="page" on the active one.
## HTML
```html
<section class="sdb-04" aria-label="Quill learning centre">
  <div class="sdb-04__theme">
    <input class="sdb-04__theme-input" type="checkbox" id="sdb-04-theme">
    <label class="sdb-04__theme-label" for="sdb-04-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sdb-04__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="sdb-04__app">
    <nav class="sdb-04__rail" aria-label="Quill learning centre">
      <p class="sdb-04__brand">Quill</p>
      <ul class="sdb-04__list">
        <li><a class="sdb-04__link" href="#sdb-04-main" aria-current="page">Getting started</a></li>
        <li><a class="sdb-04__link" href="#sdb-04-main">Deployments</a></li>
        <li><a class="sdb-04__link" href="#sdb-04-main">Billing</a></li>
        <li><a class="sdb-04__link" href="#sdb-04-main">Audit log</a></li>
        <li><a class="sdb-04__link" href="#sdb-04-main">Integrations</a></li>
        <li><a class="sdb-04__link" href="#sdb-04-main">Certification</a></li>
      </ul>
    </nav>

    <main class="sdb-04__main" id="sdb-04-main">
      <p class="sdb-04__eyebrow">Course &middot; 6 lessons</p>
      <h2 class="sdb-04__title">Getting started</h2>
      <div class="sdb-04__lessons">
        <article class="sdb-04__lesson">
          <p class="sdb-04__lesson-n">01</p>
          <h3 class="sdb-04__lesson-h">Create your first workspace</h3>
          <p class="sdb-04__lesson-m">8 min &middot; video</p>
        </article>
        <article class="sdb-04__lesson">
          <p class="sdb-04__lesson-n">02</p>
          <h3 class="sdb-04__lesson-h">Invite a teammate and set roles</h3>
          <p class="sdb-04__lesson-m">5 min &middot; reading</p>
        </article>
        <article class="sdb-04__lesson">
          <p class="sdb-04__lesson-n">03</p>
          <h3 class="sdb-04__lesson-h">Connect a repository</h3>
          <p class="sdb-04__lesson-m">11 min &middot; walkthrough</p>
        </article>
        <article class="sdb-04__lesson">
          <p class="sdb-04__lesson-n">04</p>
          <h3 class="sdb-04__lesson-h">Ship a preview environment</h3>
          <p class="sdb-04__lesson-m">14 min &middot; walkthrough</p>
        </article>
      </div>
    </main>
  </div>
</section>
```
## CSS
```css
.sdb-04 {
  --sdb-04-bg: #f4f4f5;
  --sdb-04-surf: #ffffff;
  --sdb-04-surf2: #ebebed;
  --sdb-04-line: #d4d4d8;
  --sdb-04-ink: #18181b;
  --sdb-04-mut: #5f5f68;
  --sdb-04-acc: #6d3ce0;
  --sdb-04-acc: oklch(52% 0.22 291);
  --sdb-04-acc-soft: #ece4fd;
  --sdb-04-font-display: "Archivo Narrow", "Roboto Condensed", "Helvetica Neue Condensed", ui-sans-serif, system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--sdb-04-bg);
  color: var(--sdb-04-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.sdb-04 *,
.sdb-04 *::before,
.sdb-04 *::after {
  box-sizing: border-box;
}

.sdb-04:has(.sdb-04__theme-input:checked) {
  --sdb-04-bg: #0e0e11;
  --sdb-04-surf: #17171b;
  --sdb-04-surf2: #1f1f25;
  --sdb-04-line: #2c2c33;
  --sdb-04-ink: #f2f2f5;
  --sdb-04-mut: #9d9da8;
  --sdb-04-acc: #b79bff;
  --sdb-04-acc: oklch(80% 0.13 292);
  --sdb-04-acc-soft: #241a3d;
}

@media (prefers-color-scheme: dark) {
  .sdb-04 {
    --sdb-04-bg: #0e0e11;
    --sdb-04-surf: #17171b;
    --sdb-04-surf2: #1f1f25;
    --sdb-04-line: #2c2c33;
    --sdb-04-ink: #f2f2f5;
    --sdb-04-mut: #9d9da8;
    --sdb-04-acc: #b79bff;
    --sdb-04-acc: oklch(80% 0.13 292);
    --sdb-04-acc-soft: #241a3d;
  }

  .sdb-04:has(.sdb-04__theme-input:checked) {
    --sdb-04-bg: #f4f4f5;
    --sdb-04-surf: #ffffff;
    --sdb-04-surf2: #ebebed;
    --sdb-04-line: #d4d4d8;
    --sdb-04-ink: #18181b;
    --sdb-04-mut: #5f5f68;
    --sdb-04-acc: #6d3ce0;
    --sdb-04-acc: oklch(52% 0.22 291);
    --sdb-04-acc-soft: #ece4fd;
  }
}

@media (prefers-color-scheme: light) {
  .sdb-04:has(.sdb-04__theme-input:checked) {
    --sdb-04-bg: #0e0e11;
    --sdb-04-surf: #17171b;
    --sdb-04-surf2: #1f1f25;
    --sdb-04-line: #2c2c33;
    --sdb-04-ink: #f2f2f5;
    --sdb-04-mut: #9d9da8;
    --sdb-04-acc: #b79bff;
    --sdb-04-acc: oklch(80% 0.13 292);
    --sdb-04-acc-soft: #241a3d;
  }
}

.sdb-04__theme {
  position: absolute;
  inset-block-start: 0.85rem;
  inset-inline-end: 0.85rem;
  z-index: 60;
}

.sdb-04__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.sdb-04__theme-label {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border: 0;
  background: var(--sdb-04-surf2);
  color: var(--sdb-04-ink);
  cursor: pointer;
}

.sdb-04__theme-label svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.sdb-04__theme-input:focus-visible + .sdb-04__theme-label {
  outline: 2px solid var(--sdb-04-acc);
  outline-offset: 2px;
}

.sdb-04__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sdb-04__app {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  min-block-size: 100vh;
}

@media (min-width: 46rem) {
  .sdb-04__app {
    grid-template-columns: 15rem minmax(0, 1fr);
  }
}

.sdb-04__rail {
  min-inline-size: 0;
  padding: 1rem 0.5rem;
  background: var(--sdb-04-surf);
  border-block-end: 1px solid var(--sdb-04-line);
}

@media (min-width: 46rem) {
  .sdb-04__rail {
    border-block-end: 0;
    border-inline-end: 1px solid var(--sdb-04-line);
  }
}

.sdb-04__brand {
  margin: 0 0 0.9rem;
  padding-inline: 0.8rem;
  font-family: var(--sdb-04-font-display);
  font-size: 1.05rem;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
}

.sdb-04__list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 2px;
}

.sdb-04__link {
  display: flex;
  align-items: center;
  min-block-size: 2.75rem;
  padding: 0.5rem 0.8rem;
  background: var(--sdb-04-surf);
  color: var(--sdb-04-ink);
  text-decoration: none;
  font-size: 0.92rem;
  min-inline-size: 0;
}

.sdb-04__link:hover {
  background: var(--sdb-04-acc-soft);
}

.sdb-04__link:focus-visible {
  outline: 2px solid var(--sdb-04-acc);
  outline-offset: -2px;
}

.sdb-04__link[aria-current="page"] {
  background: var(--sdb-04-acc-soft);
  color: var(--sdb-04-acc);
  font-weight: 650;
  box-shadow: inset 3px 0 0 var(--sdb-04-acc);
}

.sdb-04__main {
  min-inline-size: 0;
  padding: 1.5rem 1.25rem 2.5rem;
  align-content: start;
}

@media (min-width: 46rem) {
  .sdb-04__main {
    padding: 2.5rem 2.25rem 3rem;
  }
}

.sdb-04__eyebrow {
  margin: 0 0 0.35rem;
  font-family: var(--sdb-04-font-display);
  font-size: 0.8rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--sdb-04-mut);
}

.sdb-04__title {
  margin: 0 0 1.4rem;
  font-family: var(--sdb-04-font-display);
  font-size: clamp(1.6rem, 4.4vw, 2.4rem);
  line-height: 1.05;
  text-transform: uppercase;
}

.sdb-04__lessons {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 2px;
  background: var(--sdb-04-line);
  border: 1px solid var(--sdb-04-line);
}

@media (min-width: 52rem) {
  .sdb-04__lessons {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

.sdb-04__lesson {
  min-inline-size: 0;
  padding: 1rem;
  background: var(--sdb-04-surf);
}

.sdb-04__lesson-n {
  margin: 0 0 0.4rem;
  font-family: var(--sdb-04-font-display);
  font-size: 0.8rem;
  letter-spacing: 0.12em;
  color: var(--sdb-04-acc);
}

.sdb-04__lesson-h {
  margin: 0 0 0.3rem;
  font-size: 1rem;
  line-height: 1.25;
}

.sdb-04__lesson-m {
  margin: 0;
  font-size: 0.83rem;
  color: var(--sdb-04-mut);
}
```
