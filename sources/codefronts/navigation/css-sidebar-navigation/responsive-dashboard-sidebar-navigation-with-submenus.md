---
source: "codefronts"
url: "https://codefronts.com/navigation/css-sidebar-navigation/responsive-dashboard-sidebar-navigation-with-submenus/"
title: "Dashboard Sidebar with Current Page State"
section: "navigation"
category: "css-sidebar-navigation"
category_name: "CSS Sidebar Navigation"
description: "aria-current=\"page\" as the single source of truth for the active item, with every visual affordance derived from the attribute instead of a parallel class."
has_js: "false"
---

Here's a working CSS Sidebar Navigation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dashboard Sidebar with Current Page State
Source: https://codefronts.com/navigation/css-sidebar-navigation/responsive-dashboard-sidebar-navigation-with-submenus/

aria-current="page" as the single source of truth for the active item, with every visual affordance derived from the attribute instead of a parallel class. One state, not two that can disagree: the row fill, the inset marker, the icon colour, the breadcrumb and the group's containment dot all read the same attribute.
## HTML
```html
<section class="sdb-14" aria-label="Meridian admin">
  <div class="sdb-14__theme">
    <input class="sdb-14__theme-input" type="checkbox" id="sdb-14-theme">
    <label class="sdb-14__theme-label" for="sdb-14-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sdb-14__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="sdb-14__app">
    <nav class="sdb-14__rail" aria-label="Meridian admin">
      <p class="sdb-14__rail-title">Meridian</p>
      <ul class="sdb-14__list">
        <li><a class="sdb-14__link" href="#sdb-14-main"><span class="sdb-14__ico" aria-hidden="true">&#9633;</span>Overview</a></li>
      </ul>
      <details class="sdb-14__group" open>
        <summary class="sdb-14__summary"><span class="sdb-14__ico" aria-hidden="true">&#9660;</span>Infrastructure</summary>
        <ul class="sdb-14__list sdb-14__list--sub">
          <li><a class="sdb-14__link sdb-14__link--sub" href="#sdb-14-main">Regions</a></li>
          <li><a class="sdb-14__link sdb-14__link--sub" href="#sdb-14-main" aria-current="page">Deployments</a></li>
          <li><a class="sdb-14__link sdb-14__link--sub" href="#sdb-14-main">Certificates</a></li>
        </ul>
      </details>
      <details class="sdb-14__group">
        <summary class="sdb-14__summary"><span class="sdb-14__ico" aria-hidden="true">&#9660;</span>Access</summary>
        <ul class="sdb-14__list sdb-14__list--sub">
          <li><a class="sdb-14__link sdb-14__link--sub" href="#sdb-14-main">Members</a></li>
          <li><a class="sdb-14__link sdb-14__link--sub" href="#sdb-14-main">API keys</a></li>
          <li><a class="sdb-14__link sdb-14__link--sub" href="#sdb-14-main">Audit log</a></li>
        </ul>
      </details>
      <ul class="sdb-14__list">
        <li><a class="sdb-14__link" href="#sdb-14-main"><span class="sdb-14__ico" aria-hidden="true">&#9633;</span>Billing</a></li>
      </ul>
    </nav>

    <main class="sdb-14__main" id="sdb-14-main">
      <p class="sdb-14__crumb">Infrastructure &rarr; <span class="sdb-14__crumb-here">Deployments</span></p>
      <h2 class="sdb-14__main-h">Deployments</h2>
      <ul class="sdb-14__rows">
        <li><span class="sdb-14__sha">4c19f2a</span><span>eu-west-1</span><em>Promoted 09:14 &middot; Alex Chen</em></li>
        <li><span class="sdb-14__sha">9ab7d10</span><span>eu-west-1</span><em>Building &middot; Priya Sharma</em></li>
        <li><span class="sdb-14__sha">17c40be</span><span>us-east-1</span><em>Rolled back &middot; Jordan Lee</em></li>
        <li><span class="sdb-14__sha">08e5cc1</span><span>ap-south-1</span><em>Promoted 07:41 &middot; Ada Okafor</em></li>
        <li><span class="sdb-14__sha">b7712fd</span><span>eu-west-1</span><em>Superseded &middot; Sam Rivera</em></li>
      </ul>
    </main>
  </div>
</section>
```
## CSS
```css
.sdb-14 {
  --sdb-14-bg: #f2f3f2;
  --sdb-14-surf: #fbfbfa;
  --sdb-14-surf2: #e7e9e7;
  --sdb-14-surf3: #dcdfdc;
  --sdb-14-line: #cdd1cd;
  --sdb-14-ink: #161a18;
  --sdb-14-mut: #5c625f;
  --sdb-14-acc: #0d6b62;
  --sdb-14-acc: oklch(46% 0.09 190);
  --sdb-14-acc-soft: #d5e8e5;
  --sdb-14-font-display: "Iowan Old Style", "Palatino Linotype", Palatino, Georgia, serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--sdb-14-bg);
  color: var(--sdb-14-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.sdb-14 *,
.sdb-14 *::before,
.sdb-14 *::after {
  box-sizing: border-box;
}

.sdb-14:has(.sdb-14__theme-input:checked) {
  --sdb-14-bg: #0c100e;
  --sdb-14-surf: #141917;
  --sdb-14-surf2: #1b211f;
  --sdb-14-surf3: #232b28;
  --sdb-14-line: #2b3532;
  --sdb-14-ink: #e9efec;
  --sdb-14-mut: #94a09c;
  --sdb-14-acc: #6fd2c6;
  --sdb-14-acc: oklch(82% 0.1 190);
  --sdb-14-acc-soft: #14302c;
}

@media (prefers-color-scheme: dark) {
  .sdb-14 {
    --sdb-14-bg: #0c100e;
    --sdb-14-surf: #141917;
    --sdb-14-surf2: #1b211f;
    --sdb-14-surf3: #232b28;
    --sdb-14-line: #2b3532;
    --sdb-14-ink: #e9efec;
    --sdb-14-mut: #94a09c;
    --sdb-14-acc: #6fd2c6;
    --sdb-14-acc: oklch(82% 0.1 190);
    --sdb-14-acc-soft: #14302c;
  }

  .sdb-14:has(.sdb-14__theme-input:checked) {
    --sdb-14-bg: #f2f3f2;
    --sdb-14-surf: #fbfbfa;
    --sdb-14-surf2: #e7e9e7;
    --sdb-14-surf3: #dcdfdc;
    --sdb-14-line: #cdd1cd;
    --sdb-14-ink: #161a18;
    --sdb-14-mut: #5c625f;
    --sdb-14-acc: #0d6b62;
    --sdb-14-acc: oklch(46% 0.09 190);
    --sdb-14-acc-soft: #d5e8e5;
  }
}

@media (prefers-color-scheme: light) {
  .sdb-14:has(.sdb-14__theme-input:checked) {
    --sdb-14-bg: #0c100e;
    --sdb-14-surf: #141917;
    --sdb-14-surf2: #1b211f;
    --sdb-14-surf3: #232b28;
    --sdb-14-line: #2b3532;
    --sdb-14-ink: #e9efec;
    --sdb-14-mut: #94a09c;
    --sdb-14-acc: #6fd2c6;
    --sdb-14-acc: oklch(82% 0.1 190);
    --sdb-14-acc-soft: #14302c;
  }
}

.sdb-14__theme {
  position: absolute;
  inset-block-start: 0.85rem;
  inset-inline-end: 0.85rem;
  z-index: 60;
}

.sdb-14__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.sdb-14__theme-label {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border-radius: 0.35rem;
  border: 1px solid var(--sdb-14-line);
  background: var(--sdb-14-surf);
  color: var(--sdb-14-ink);
  cursor: pointer;
}

.sdb-14__theme-label svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.sdb-14__theme-input:focus-visible + .sdb-14__theme-label {
  outline: 2px solid var(--sdb-14-acc);
  outline-offset: 2px;
}

.sdb-14__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sdb-14__app {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  min-block-size: 100vh;
  background: var(--sdb-14-surf);
}

@media (min-width: 46rem) {
  .sdb-14__app {
    grid-template-columns: minmax(0, 15rem) minmax(0, 1fr);
  }
}

.sdb-14__rail {
  min-inline-size: 0;
  padding: 1rem 0.55rem 1.2rem;
  background: var(--sdb-14-surf2);
  border-block-end: 1px solid var(--sdb-14-line);
}

@media (min-width: 46rem) {
  .sdb-14__rail {
    border-block-end: 0;
    border-inline-end: 1px solid var(--sdb-14-line);
  }
}

.sdb-14__rail-title {
  margin: 0 0 0.7rem;
  padding-inline: 0.6rem;
  font-family: var(--sdb-14-font-display);
  font-size: 1.15rem;
}

.sdb-14__list {
  list-style: none;
  margin: 0;
  padding: 0;
}

.sdb-14__link {
  position: relative;
  display: flex;
  align-items: center;
  gap: 0.55rem;
  min-block-size: 2.75rem;
  padding: 0.5rem 0.65rem;
  border-radius: 0.3rem;
  color: var(--sdb-14-ink);
  text-decoration: none;
  font-size: 0.91rem;
  min-inline-size: 0;
}

.sdb-14__link--sub {
  padding-inline-start: 1.9rem;
  font-size: 0.88rem;
  color: var(--sdb-14-mut);
}

.sdb-14__ico {
  flex: none;
  font-size: 0.7rem;
  color: var(--sdb-14-mut);
}

.sdb-14__link:hover {
  background: var(--sdb-14-surf3);
}

.sdb-14__link:focus-visible,
.sdb-14__summary:focus-visible {
  outline: 2px solid var(--sdb-14-acc);
  outline-offset: -2px;
}

.sdb-14__link[aria-current="page"] {
  background: var(--sdb-14-acc-soft);
  color: var(--sdb-14-acc);
  font-weight: 650;
  box-shadow: inset 3px 0 0 var(--sdb-14-acc);
}

.sdb-14__link[aria-current="page"] .sdb-14__ico {
  color: var(--sdb-14-acc);
}

.sdb-14__group {
  margin-block: 0.15rem;
}

.sdb-14__summary {
  display: flex;
  align-items: center;
  gap: 0.55rem;
  min-block-size: 2.75rem;
  padding: 0.5rem 0.65rem;
  border-radius: 0.3rem;
  cursor: pointer;
  font-size: 0.91rem;
  font-weight: 600;
  list-style: none;
}

.sdb-14__summary::-webkit-details-marker {
  display: none;
}

.sdb-14__summary .sdb-14__ico {
  transition: transform 150ms ease;
}

.sdb-14__group:not([open]) .sdb-14__summary .sdb-14__ico {
  transform: rotate(-90deg);
}

.sdb-14__group:has([aria-current="page"]) > .sdb-14__summary::after {
  content: "";
  margin-inline-start: auto;
  inline-size: 0.4rem;
  block-size: 0.4rem;
  border-radius: 50%;
  background: var(--sdb-14-acc);
  flex: none;
}

.sdb-14__main {
  min-inline-size: 0;
  padding: 1.5rem 1.25rem 2.5rem;
  align-content: start;
}

@media (min-width: 46rem) {
  .sdb-14__main {
    padding: 2.4rem 2.25rem 3rem;
  }
}

.sdb-14__crumb {
  margin: 0 0 0.25rem;
  font-size: 0.82rem;
  color: var(--sdb-14-mut);
}

.sdb-14__crumb-here {
  color: var(--sdb-14-acc);
  font-weight: 650;
}

.sdb-14__main-h {
  margin: 0 0 1.2rem;
  font-family: var(--sdb-14-font-display);
  font-size: clamp(1.45rem, 3.6vw, 2.1rem);
  line-height: 1.1;
}

.sdb-14__rows {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 1px;
  background: var(--sdb-14-line);
  border: 1px solid var(--sdb-14-line);
  max-inline-size: 48rem;
}

.sdb-14__rows li {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: 0.6rem;
  padding: 0.7rem 0.85rem;
  background: var(--sdb-14-surf);
  font-size: 0.88rem;
  min-inline-size: 0;
}

.sdb-14__sha {
  font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
  font-size: 0.82rem;
  color: var(--sdb-14-acc);
}

.sdb-14__rows em {
  margin-inline-start: auto;
  font-style: normal;
  font-size: 0.8rem;
  color: var(--sdb-14-mut);
}

@media (prefers-reduced-motion: reduce) {
  .sdb-14__summary .sdb-14__ico {
    transition: none;
  }
}
```
