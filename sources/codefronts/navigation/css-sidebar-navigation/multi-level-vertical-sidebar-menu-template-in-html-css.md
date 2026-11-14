---
source: "codefronts"
url: "https://codefronts.com/navigation/css-sidebar-navigation/multi-level-vertical-sidebar-menu-template-in-html-css/"
title: "Multi Level Sidebar Menu Disclosure Pattern"
section: "navigation"
category: "css-sidebar-navigation"
category_name: "CSS Sidebar Navigation"
description: "Two-level nesting using the disclosure pattern from demo 09, with the depth limit stated out loud: past two levels a sidebar stops being navigable and the…"
has_js: "false"
---

Here's a working CSS Sidebar Navigation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Multi Level Sidebar Menu Disclosure Pattern
Source: https://codefronts.com/navigation/css-sidebar-navigation/multi-level-vertical-sidebar-menu-template-in-html-css/

Two-level nesting using the disclosure pattern from demo 09, with the depth limit stated out loud: past two levels a sidebar stops being navigable and the information architecture is the real problem, not the component. The rail here stops at two levels, and the third is promoted into the page as an on-this-page navigation.
## HTML
```html
<section class="sdb-15" aria-label="Basalt knowledge base">
  <div class="sdb-15__theme">
    <input class="sdb-15__theme-input" type="checkbox" id="sdb-15-theme">
    <label class="sdb-15__theme-label" for="sdb-15-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sdb-15__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="sdb-15__app">
    <nav class="sdb-15__rail" aria-label="Basalt knowledge base">
      <p class="sdb-15__rail-title">Handbook</p>
      <ul class="sdb-15__list">
        <li><a class="sdb-15__link" href="#sdb-15-main">Start here</a></li>
      </ul>

      <details class="sdb-15__l1" open>
        <summary class="sdb-15__sum sdb-15__sum--l1">Operations</summary>
        <div class="sdb-15__branch">
          <details class="sdb-15__l2" open>
            <summary class="sdb-15__sum sdb-15__sum--l2">Deployments</summary>
            <ul class="sdb-15__list sdb-15__list--l3">
              <li><a class="sdb-15__link sdb-15__link--leaf" href="#sdb-15-main">Promotion policy</a></li>
              <li><a class="sdb-15__link sdb-15__link--leaf" href="#sdb-15-main" aria-current="page">Rollback runbook</a></li>
              <li><a class="sdb-15__link sdb-15__link--leaf" href="#sdb-15-main">Region failover</a></li>
            </ul>
          </details>
          <details class="sdb-15__l2">
            <summary class="sdb-15__sum sdb-15__sum--l2">On call</summary>
            <ul class="sdb-15__list sdb-15__list--l3">
              <li><a class="sdb-15__link sdb-15__link--leaf" href="#sdb-15-main">Escalation ladder</a></li>
              <li><a class="sdb-15__link sdb-15__link--leaf" href="#sdb-15-main">Incident review</a></li>
            </ul>
          </details>
        </div>
      </details>

      <details class="sdb-15__l1">
        <summary class="sdb-15__sum sdb-15__sum--l1">People</summary>
        <div class="sdb-15__branch">
          <details class="sdb-15__l2">
            <summary class="sdb-15__sum sdb-15__sum--l2">Onboarding</summary>
            <ul class="sdb-15__list sdb-15__list--l3">
              <li><a class="sdb-15__link sdb-15__link--leaf" href="#sdb-15-main">First week</a></li>
              <li><a class="sdb-15__link sdb-15__link--leaf" href="#sdb-15-main">Access requests</a></li>
            </ul>
          </details>
          <details class="sdb-15__l2">
            <summary class="sdb-15__sum sdb-15__sum--l2">Reviews</summary>
            <ul class="sdb-15__list sdb-15__list--l3">
              <li><a class="sdb-15__link sdb-15__link--leaf" href="#sdb-15-main">Cycle calendar</a></li>
              <li><a class="sdb-15__link sdb-15__link--leaf" href="#sdb-15-main">Writing feedback</a></li>
            </ul>
          </details>
        </div>
      </details>
    </nav>

    <main class="sdb-15__main" id="sdb-15-main">
      <p class="sdb-15__crumb">Operations / Deployments</p>
      <h2 class="sdb-15__main-h">Rollback runbook</h2>
      <nav class="sdb-15__sub" aria-label="On this page">
        <p class="sdb-15__sub-title">On this page</p>
        <ul class="sdb-15__sub-list">
          <li><a class="sdb-15__sub-link" href="#sdb-15-main" aria-current="page">Before you start</a></li>
          <li><a class="sdb-15__sub-link" href="#sdb-15-main">Pointer move</a></li>
          <li><a class="sdb-15__sub-link" href="#sdb-15-main">Verifying</a></li>
          <li><a class="sdb-15__sub-link" href="#sdb-15-main">Post-mortem</a></li>
        </ul>
      </nav>
      <p class="sdb-15__body">Promotion is a pointer move, so a rollback is the same operation in reverse and completes in under a second. The slow part is verification &mdash; confirm the health checks on the previous build before you announce it.</p>
      <p class="sdb-15__body">Announce in the incident channel first, then update the status page. If the previous build is more than seven days old, check the migration log before promoting it.</p>
    </main>
  </div>
</section>
```
## CSS
```css
.sdb-15 {
  --sdb-15-bg: #f7f4ee;
  --sdb-15-surf: #fffdf8;
  --sdb-15-surf2: #efeade;
  --sdb-15-line: #ddd6c6;
  --sdb-15-ink: #201d16;
  --sdb-15-mut: #6a6252;
  --sdb-15-acc: #4c5f2a;
  --sdb-15-acc: oklch(45% 0.1 122);
  --sdb-15-acc-soft: #e4ead2;
  --sdb-15-font-display: Optima, Candara, "Gill Sans", "Segoe UI", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--sdb-15-bg);
  color: var(--sdb-15-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.sdb-15 *,
.sdb-15 *::before,
.sdb-15 *::after {
  box-sizing: border-box;
}

.sdb-15:has(.sdb-15__theme-input:checked) {
  --sdb-15-bg: #14130f;
  --sdb-15-surf: #1b1a14;
  --sdb-15-surf2: #23211a;
  --sdb-15-line: #332f25;
  --sdb-15-ink: #f0ece1;
  --sdb-15-mut: #a49b87;
  --sdb-15-acc: #b6cf80;
  --sdb-15-acc: oklch(82% 0.12 122);
  --sdb-15-acc-soft: #262d17;
}

@media (prefers-color-scheme: dark) {
  .sdb-15 {
    --sdb-15-bg: #14130f;
    --sdb-15-surf: #1b1a14;
    --sdb-15-surf2: #23211a;
    --sdb-15-line: #332f25;
    --sdb-15-ink: #f0ece1;
    --sdb-15-mut: #a49b87;
    --sdb-15-acc: #b6cf80;
    --sdb-15-acc: oklch(82% 0.12 122);
    --sdb-15-acc-soft: #262d17;
  }

  .sdb-15:has(.sdb-15__theme-input:checked) {
    --sdb-15-bg: #f7f4ee;
    --sdb-15-surf: #fffdf8;
    --sdb-15-surf2: #efeade;
    --sdb-15-line: #ddd6c6;
    --sdb-15-ink: #201d16;
    --sdb-15-mut: #6a6252;
    --sdb-15-acc: #4c5f2a;
    --sdb-15-acc: oklch(45% 0.1 122);
    --sdb-15-acc-soft: #e4ead2;
  }
}

@media (prefers-color-scheme: light) {
  .sdb-15:has(.sdb-15__theme-input:checked) {
    --sdb-15-bg: #14130f;
    --sdb-15-surf: #1b1a14;
    --sdb-15-surf2: #23211a;
    --sdb-15-line: #332f25;
    --sdb-15-ink: #f0ece1;
    --sdb-15-mut: #a49b87;
    --sdb-15-acc: #b6cf80;
    --sdb-15-acc: oklch(82% 0.12 122);
    --sdb-15-acc-soft: #262d17;
  }
}

.sdb-15__theme {
  position: absolute;
  inset-block-start: 0.85rem;
  inset-inline-end: 0.85rem;
  z-index: 60;
}

.sdb-15__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.sdb-15__theme-label {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border: 1px solid var(--sdb-15-line);
  background: var(--sdb-15-surf);
  color: var(--sdb-15-ink);
  cursor: pointer;
}

.sdb-15__theme-label svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.sdb-15__theme-input:focus-visible + .sdb-15__theme-label {
  outline: 2px solid var(--sdb-15-acc);
  outline-offset: 2px;
}

.sdb-15__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sdb-15__app {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  min-block-size: 100vh;
  background: var(--sdb-15-surf);
}

@media (min-width: 48rem) {
  .sdb-15__app {
    grid-template-columns: minmax(0, 17.5rem) minmax(0, 1fr);
  }
}

.sdb-15__rail {
  min-inline-size: 0;
  padding: 1rem 0.6rem 1.2rem;
  border-block-end: 1px solid var(--sdb-15-line);
}

@media (min-width: 48rem) {
  .sdb-15__rail {
    border-block-end: 0;
    border-inline-end: 1px solid var(--sdb-15-line);
  }
}

.sdb-15__rail-title {
  margin: 0 0 0.7rem;
  padding-inline: 0.5rem;
  font-family: var(--sdb-15-font-display);
  font-size: 1.05rem;
  letter-spacing: 0.02em;
}

.sdb-15__list {
  list-style: none;
  margin: 0;
  padding: 0;
}

.sdb-15__link {
  display: flex;
  align-items: center;
  min-block-size: 2.75rem;
  padding: 0.5rem 0.6rem;
  color: var(--sdb-15-ink);
  text-decoration: none;
  font-size: 0.91rem;
  min-inline-size: 0;
}

.sdb-15__link:hover {
  background: var(--sdb-15-surf2);
}

.sdb-15__link:focus-visible,
.sdb-15__sum:focus-visible,
.sdb-15__sub-link:focus-visible {
  outline: 2px solid var(--sdb-15-acc);
  outline-offset: -2px;
}

.sdb-15__link--leaf {
  padding-inline-start: 1.9rem;
  font-size: 0.88rem;
  color: var(--sdb-15-mut);
}

.sdb-15__link[aria-current="page"] {
  color: var(--sdb-15-acc);
  font-weight: 650;
  background: var(--sdb-15-acc-soft);
}

.sdb-15__sum {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  min-block-size: 2.75rem;
  padding: 0.5rem 0.6rem;
  cursor: pointer;
  list-style: none;
  font-size: 0.91rem;
  font-weight: 600;
}

.sdb-15__sum::-webkit-details-marker {
  display: none;
}

.sdb-15__sum::before {
  content: "";
  flex: none;
  inline-size: 0.4rem;
  block-size: 0.4rem;
  border-inline-end: 1.5px solid var(--sdb-15-mut);
  border-block-end: 1.5px solid var(--sdb-15-mut);
  transform: rotate(-45deg);
  transition: transform 150ms ease;
}

.sdb-15__l1[open] > .sdb-15__sum::before,
.sdb-15__l2[open] > .sdb-15__sum::before {
  transform: rotate(45deg);
}

.sdb-15__sum--l2 {
  padding-inline-start: 1.1rem;
  font-size: 0.89rem;
  font-weight: 500;
}

.sdb-15__sum:hover {
  background: var(--sdb-15-surf2);
}

.sdb-15__l1:has([aria-current="page"]) > .sdb-15__sum,
.sdb-15__l2:has([aria-current="page"]) > .sdb-15__sum {
  color: var(--sdb-15-acc);
}

.sdb-15__branch {
  border-inline-start: 1px solid var(--sdb-15-line);
  margin-inline-start: 0.6rem;
}

.sdb-15__main {
  min-inline-size: 0;
  padding: 1.5rem 1.25rem 2.5rem;
  align-content: start;
}

@media (min-width: 48rem) {
  .sdb-15__main {
    padding: 2.4rem 2.25rem 3rem;
  }
}

.sdb-15__crumb {
  margin: 0 0 0.25rem;
  font-size: 0.82rem;
  color: var(--sdb-15-mut);
}

.sdb-15__main-h {
  margin: 0 0 1.1rem;
  font-family: var(--sdb-15-font-display);
  font-size: clamp(1.45rem, 3.6vw, 2rem);
  line-height: 1.1;
}

.sdb-15__sub {
  margin-block-end: 1.2rem;
  padding: 0.8rem 0.9rem;
  background: var(--sdb-15-surf2);
  max-inline-size: 44rem;
}

.sdb-15__sub-title {
  margin: 0 0 0.5rem;
  font-size: 0.7rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--sdb-15-mut);
}

.sdb-15__sub-list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 0.35rem;
}

.sdb-15__sub-link {
  display: inline-flex;
  align-items: center;
  min-block-size: 2.75rem;
  padding-inline: 0.85rem;
  background: var(--sdb-15-surf);
  color: var(--sdb-15-ink);
  text-decoration: none;
  font-size: 0.87rem;
  border: 1px solid var(--sdb-15-line);
}

.sdb-15__sub-link[aria-current="page"] {
  background: var(--sdb-15-acc);
  border-color: var(--sdb-15-acc);
  color: var(--sdb-15-surf);
  font-weight: 650;
}

.sdb-15__body {
  margin: 0 0 0.8rem;
  font-size: 0.94rem;
  color: var(--sdb-15-mut);
  max-inline-size: 40rem;
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .sdb-15__sum::before {
    transition: none;
  }
}
```
