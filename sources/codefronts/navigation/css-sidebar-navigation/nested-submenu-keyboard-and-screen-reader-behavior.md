---
source: "codefronts"
url: "https://codefronts.com/navigation/css-sidebar-navigation/nested-submenu-keyboard-and-screen-reader-behavior/"
title: "Nested Submenu Keyboard and Screen Reader Behavior"
section: "navigation"
category: "css-sidebar-navigation"
category_name: "CSS Sidebar Navigation"
description: "Expandable groups done properly."
has_js: "false"
---

Here's a working CSS Sidebar Navigation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Nested Submenu Keyboard and Screen Reader Behavior
Source: https://codefronts.com/navigation/css-sidebar-navigation/nested-submenu-keyboard-and-screen-reader-behavior/

Expandable groups done properly. The group header is a control, not a link that goes nowhere; a collapsed submenu is hidden rather than merely invisible, so its links leave the tab order; and aria-current on a nested item also has to tell the user that the collapsed parent group contains the current page &mdash; otherwise the only signal that you are somewhere inside it disappears the moment it closes.
## HTML
```html
<section class="sdb-09" aria-label="Fern CMS">
  <div class="sdb-09__theme">
    <input class="sdb-09__theme-input" type="checkbox" id="sdb-09-theme">
    <label class="sdb-09__theme-label" for="sdb-09-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sdb-09__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="sdb-09__app">
    <nav class="sdb-09__rail" aria-label="Fern workspace">
      <p class="sdb-09__rail-title">Fern &mdash; Meridian site</p>
      <ul class="sdb-09__list">
        <li><a class="sdb-09__link" href="#sdb-09-main">Dashboard</a></li>
      </ul>

      <details class="sdb-09__group" open>
        <summary class="sdb-09__summary">
          <svg class="sdb-09__chev" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M9 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>
          Content
          <span class="sdb-09__has">contains the current page</span>
        </summary>
        <ul class="sdb-09__list sdb-09__list--sub">
          <li><a class="sdb-09__link sdb-09__link--sub" href="#sdb-09-main">Pages</a></li>
          <li><a class="sdb-09__link sdb-09__link--sub" href="#sdb-09-main" aria-current="page">Articles</a></li>
          <li><a class="sdb-09__link sdb-09__link--sub" href="#sdb-09-main">Media library</a></li>
          <li><a class="sdb-09__link sdb-09__link--sub" href="#sdb-09-main">Redirects</a></li>
        </ul>
      </details>

      <details class="sdb-09__group">
        <summary class="sdb-09__summary">
          <svg class="sdb-09__chev" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M9 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>
          Team settings
          <span class="sdb-09__has">contains the current page</span>
        </summary>
        <ul class="sdb-09__list sdb-09__list--sub">
          <li><a class="sdb-09__link sdb-09__link--sub" href="#sdb-09-main">Members</a></li>
          <li><a class="sdb-09__link sdb-09__link--sub" href="#sdb-09-main">Roles</a></li>
          <li><a class="sdb-09__link sdb-09__link--sub" href="#sdb-09-main">Audit log</a></li>
        </ul>
      </details>

      <ul class="sdb-09__list">
        <li><a class="sdb-09__link" href="#sdb-09-main">API keys</a></li>
        <li><a class="sdb-09__link" href="#sdb-09-main">Billing</a></li>
      </ul>
    </nav>

    <main class="sdb-09__main" id="sdb-09-main">
      <p class="sdb-09__crumb">Content / Articles</p>
      <h2 class="sdb-09__title">Articles</h2>
      <table class="sdb-09__table">
        <caption>Recently edited</caption>
        <thead><tr><th scope="col">Title</th><th scope="col">Editor</th><th scope="col">State</th></tr></thead>
        <tbody>
          <tr><td>Deployment regions</td><td>Alex Chen</td><td>Published</td></tr>
          <tr><td>Token rotation policy</td><td>Priya Sharma</td><td>In review</td></tr>
          <tr><td>Audit log retention</td><td>Sam Rivera</td><td>Draft</td></tr>
          <tr><td>Media naming rules</td><td>Ada Okafor</td><td>Published</td></tr>
        </tbody>
      </table>
    </main>
  </div>
</section>
```
## CSS
```css
.sdb-09 {
  --sdb-09-bg: #f4f7fc;
  --sdb-09-surf: #ffffff;
  --sdb-09-surf2: #eaf0f9;
  --sdb-09-line: #d2dcec;
  --sdb-09-ink: #101a2b;
  --sdb-09-mut: #56658a;
  --sdb-09-acc: #1554c8;
  --sdb-09-acc: oklch(48% 0.17 258);
  --sdb-09-acc-soft: #dfe9fc;
  --sdb-09-font-display: "Segoe UI", system-ui, -apple-system, "Helvetica Neue", sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--sdb-09-bg);
  color: var(--sdb-09-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.sdb-09 *,
.sdb-09 *::before,
.sdb-09 *::after {
  box-sizing: border-box;
}

.sdb-09:has(.sdb-09__theme-input:checked) {
  --sdb-09-bg: #080d16;
  --sdb-09-surf: #0f1725;
  --sdb-09-surf2: #16202f;
  --sdb-09-line: #24303f;
  --sdb-09-ink: #e9eef8;
  --sdb-09-mut: #92a1bd;
  --sdb-09-acc: #7fa6ff;
  --sdb-09-acc: oklch(78% 0.13 260);
  --sdb-09-acc-soft: #172441;
}

@media (prefers-color-scheme: dark) {
  .sdb-09 {
    --sdb-09-bg: #080d16;
    --sdb-09-surf: #0f1725;
    --sdb-09-surf2: #16202f;
    --sdb-09-line: #24303f;
    --sdb-09-ink: #e9eef8;
    --sdb-09-mut: #92a1bd;
    --sdb-09-acc: #7fa6ff;
    --sdb-09-acc: oklch(78% 0.13 260);
    --sdb-09-acc-soft: #172441;
  }

  .sdb-09:has(.sdb-09__theme-input:checked) {
    --sdb-09-bg: #f4f7fc;
    --sdb-09-surf: #ffffff;
    --sdb-09-surf2: #eaf0f9;
    --sdb-09-line: #d2dcec;
    --sdb-09-ink: #101a2b;
    --sdb-09-mut: #56658a;
    --sdb-09-acc: #1554c8;
    --sdb-09-acc: oklch(48% 0.17 258);
    --sdb-09-acc-soft: #dfe9fc;
  }
}

@media (prefers-color-scheme: light) {
  .sdb-09:has(.sdb-09__theme-input:checked) {
    --sdb-09-bg: #080d16;
    --sdb-09-surf: #0f1725;
    --sdb-09-surf2: #16202f;
    --sdb-09-line: #24303f;
    --sdb-09-ink: #e9eef8;
    --sdb-09-mut: #92a1bd;
    --sdb-09-acc: #7fa6ff;
    --sdb-09-acc: oklch(78% 0.13 260);
    --sdb-09-acc-soft: #172441;
  }
}

.sdb-09__theme {
  position: absolute;
  inset-block-start: 0.85rem;
  inset-inline-end: 0.85rem;
  z-index: 60;
}

.sdb-09__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.sdb-09__theme-label {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border-radius: 0.5rem;
  border: 1px solid var(--sdb-09-line);
  background: var(--sdb-09-surf);
  color: var(--sdb-09-ink);
  cursor: pointer;
}

.sdb-09__theme-label svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.sdb-09__theme-input:focus-visible + .sdb-09__theme-label {
  outline: 2px solid var(--sdb-09-acc);
  outline-offset: 2px;
}

.sdb-09__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sdb-09__app {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  min-block-size: 100vh;
  background: var(--sdb-09-surf);
}

@media (min-width: 46rem) {
  .sdb-09__app {
    grid-template-columns: minmax(0, 18.5rem) minmax(0, 1fr);
  }
}

.sdb-09__rail {
  min-inline-size: 0;
  padding: 1rem 0.6rem 1.2rem;
  background: var(--sdb-09-surf2);
  border-block-end: 1px solid var(--sdb-09-line);
}

@media (min-width: 46rem) {
  .sdb-09__rail {
    border-block-end: 0;
    border-inline-end: 1px solid var(--sdb-09-line);
  }
}

.sdb-09__rail-title {
  margin: 0 0 0.7rem;
  padding-inline: 0.6rem;
  font-size: 0.74rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--sdb-09-mut);
}

.sdb-09__list {
  list-style: none;
  margin: 0;
  padding: 0;
}

.sdb-09__link {
  display: flex;
  align-items: center;
  min-block-size: 2.75rem;
  padding: 0.5rem 0.7rem;
  border-radius: 0.4rem;
  color: var(--sdb-09-ink);
  text-decoration: none;
  font-size: 0.92rem;
  min-inline-size: 0;
}

.sdb-09__link--sub {
  padding-inline-start: 2.1rem;
  font-size: 0.89rem;
  color: var(--sdb-09-mut);
}

.sdb-09__link:hover {
  background: var(--sdb-09-surf);
}

.sdb-09__link:focus-visible,
.sdb-09__summary:focus-visible {
  outline: 2px solid var(--sdb-09-acc);
  outline-offset: -2px;
}

.sdb-09__link[aria-current="page"] {
  background: var(--sdb-09-acc-soft);
  color: var(--sdb-09-acc);
  font-weight: 650;
}

.sdb-09__group {
  margin-block: 0.15rem;
}

.sdb-09__summary {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  min-block-size: 2.75rem;
  padding: 0.5rem 0.7rem;
  border-radius: 0.4rem;
  cursor: pointer;
  font-size: 0.92rem;
  font-weight: 600;
  list-style: none;
}

.sdb-09__summary::-webkit-details-marker {
  display: none;
}

.sdb-09__summary:hover {
  background: var(--sdb-09-surf);
}

.sdb-09__chev {
  inline-size: 1rem;
  block-size: 1rem;
  flex: none;
  color: var(--sdb-09-mut);
  transition: transform 150ms ease;
}

.sdb-09__group[open] > .sdb-09__summary .sdb-09__chev {
  transform: rotate(90deg);
}

.sdb-09__has {
  display: none;
}

.sdb-09__group:has([aria-current="page"]) > .sdb-09__summary .sdb-09__has {
  display: block;
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sdb-09__group:has([aria-current="page"]) > .sdb-09__summary::after {
  content: "";
  margin-inline-start: auto;
  inline-size: 0.45rem;
  block-size: 0.45rem;
  border-radius: 50%;
  background: var(--sdb-09-acc);
  flex: none;
}

.sdb-09__main {
  min-inline-size: 0;
  padding: 1.5rem 1.25rem 2.5rem;
  align-content: start;
}

@media (min-width: 46rem) {
  .sdb-09__main {
    padding: 2.4rem 2.25rem 3rem;
  }
}

.sdb-09__crumb {
  margin: 0 0 0.25rem;
  font-size: 0.78rem;
  color: var(--sdb-09-mut);
}

.sdb-09__title {
  margin: 0 0 1.2rem;
  font-family: var(--sdb-09-font-display);
  font-size: clamp(1.35rem, 3.4vw, 1.9rem);
  line-height: 1.15;
  letter-spacing: -0.015em;
}

.sdb-09__table {
  inline-size: 100%;
  border-collapse: collapse;
  font-size: 0.9rem;
  max-inline-size: 48rem;
}

.sdb-09__table caption {
  text-align: start;
  padding-block-end: 0.5rem;
  font-size: 0.74rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--sdb-09-mut);
}

.sdb-09__table th,
.sdb-09__table td {
  padding: 0.6rem 0.6rem;
  text-align: start;
  border-block-end: 1px solid var(--sdb-09-line);
  min-inline-size: 0;
}

.sdb-09__table th {
  font-size: 0.74rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--sdb-09-mut);
}

@media (prefers-reduced-motion: reduce) {
  .sdb-09__chev {
    transition: none;
  }
}
```
