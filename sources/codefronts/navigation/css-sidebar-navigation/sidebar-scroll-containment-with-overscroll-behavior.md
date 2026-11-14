---
source: "codefronts"
url: "https://codefronts.com/navigation/css-sidebar-navigation/sidebar-scroll-containment-with-overscroll-behavior/"
title: "Sidebar Scroll Containment with Overscroll Behavior"
section: "navigation"
category: "css-sidebar-navigation"
category_name: "CSS Sidebar Navigation"
description: "Scroll to the bottom of a long sidebar and keep going, and the scroll chains to the page behind it &mdash; on an open drawer that means the background moves…"
has_js: "false"
---

Here's a working CSS Sidebar Navigation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sidebar Scroll Containment with Overscroll Behavior
Source: https://codefronts.com/navigation/css-sidebar-navigation/sidebar-scroll-containment-with-overscroll-behavior/

Scroll to the bottom of a long sidebar and keep going, and the scroll chains to the page behind it &mdash; on an open drawer that means the background moves while the drawer sits still. overscroll-behavior: contain stops the chain in one declaration. The rail here contains its own scroll, and the thread beside it does the same. Includes the related iOS problem, where the body still scrolls behind a fixed overlay, and what actually fixes it.
## HTML
```html
<section class="sdb-08" aria-label="Talon chat">
  <div class="sdb-08__theme">
    <input class="sdb-08__theme-input" type="checkbox" id="sdb-08-theme">
    <label class="sdb-08__theme-label" for="sdb-08-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sdb-08__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="sdb-08__app">
    <nav class="sdb-08__rail" aria-label="Talon channels">
      <p class="sdb-08__rail-title">Channels</p>
      <ul class="sdb-08__list">
        <li><a class="sdb-08__link" href="#sdb-08-thread" aria-current="page">#deployments</a></li>
        <li><a class="sdb-08__link" href="#sdb-08-thread">#incidents</a></li>
        <li><a class="sdb-08__link" href="#sdb-08-thread">#billing</a></li>
        <li><a class="sdb-08__link" href="#sdb-08-thread">#design-review</a></li>
        <li><a class="sdb-08__link" href="#sdb-08-thread">#hiring</a></li>
        <li><a class="sdb-08__link" href="#sdb-08-thread">#audit-log</a></li>
        <li><a class="sdb-08__link" href="#sdb-08-thread">#api-keys</a></li>
        <li><a class="sdb-08__link" href="#sdb-08-thread">#field-notes</a></li>
        <li><a class="sdb-08__link" href="#sdb-08-thread">#vendor-desk</a></li>
        <li><a class="sdb-08__link" href="#sdb-08-thread">#support-escalations</a></li>
        <li><a class="sdb-08__link" href="#sdb-08-thread">#release-notes</a></li>
        <li><a class="sdb-08__link" href="#sdb-08-thread">#retro</a></li>
        <li><a class="sdb-08__link" href="#sdb-08-thread">#status-page</a></li>
        <li><a class="sdb-08__link" href="#sdb-08-thread">#certificates</a></li>
        <li><a class="sdb-08__link" href="#sdb-08-thread">#on-call</a></li>
        <li><a class="sdb-08__link" href="#sdb-08-thread">#runbooks</a></li>
        <li><a class="sdb-08__link" href="#sdb-08-thread">#postmortems</a></li>
        <li><a class="sdb-08__link" href="#sdb-08-thread">#capacity</a></li>
        <li><a class="sdb-08__link" href="#sdb-08-thread">#data-platform</a></li>
        <li><a class="sdb-08__link" href="#sdb-08-thread">#mobile</a></li>
        <li><a class="sdb-08__link" href="#sdb-08-thread">#design-system</a></li>
        <li><a class="sdb-08__link" href="#sdb-08-thread">#localisation</a></li>
        <li><a class="sdb-08__link" href="#sdb-08-thread">#partners</a></li>
        <li><a class="sdb-08__link" href="#sdb-08-thread">#recruiting</a></li>
        <li><a class="sdb-08__link" href="#sdb-08-thread">#social</a></li>
        <li><a class="sdb-08__link" href="#sdb-08-thread">#random</a></li>
      </ul>
    </nav>

    <main class="sdb-08__thread" id="sdb-08-thread">
      <p class="sdb-08__channel">#deployments</p>
      <p class="sdb-08__msg"><b>Priya Sharma</b> Rollback finished, pointer is back on 4c19f.</p>
      <p class="sdb-08__msg"><b>Jordan Lee</b> Confirmed on the status page.</p>
      <p class="sdb-08__msg"><b>Sam Rivera</b> Retention window is 90 days now &mdash; runbook updated.</p>
      <p class="sdb-08__msg"><b>Ada Okafor</b> Token exchange p99 is back under 200ms.</p>
      <p class="sdb-08__msg"><b>Tomas Vidal</b> Staging snapshot is rebuilding, ETA 10 minutes.</p>
      <p class="sdb-08__msg"><b>Priya Sharma</b> Nice. I'll close the incident once staging is green.</p>
    </main>
  </div>
</section>
```
## CSS
```css
.sdb-08 {
  --sdb-08-bg: #211d19;
  --sdb-08-surf: #2b2521;
  --sdb-08-surf2: #362e28;
  --sdb-08-line: #453b33;
  --sdb-08-ink: #f4ece3;
  --sdb-08-mut: #b3a496;
  --sdb-08-acc: #e0a13c;
  --sdb-08-acc: oklch(76% 0.14 72);
  --sdb-08-acc-soft: #3d3021;
  --sdb-08-font-display: Rockwell, "Bookman Old Style", "Roboto Slab", Georgia, serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--sdb-08-bg);
  color: var(--sdb-08-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.sdb-08 *,
.sdb-08 *::before,
.sdb-08 *::after {
  box-sizing: border-box;
}

.sdb-08:has(.sdb-08__theme-input:checked) {
  --sdb-08-bg: #f7f2ea;
  --sdb-08-surf: #ffffff;
  --sdb-08-surf2: #efe7dc;
  --sdb-08-line: #ddd0c0;
  --sdb-08-ink: #241d17;
  --sdb-08-mut: #6c5c4e;
  --sdb-08-acc: #8a5210;
  --sdb-08-acc: oklch(48% 0.11 68);
  --sdb-08-acc-soft: #f2e3cf;
}

@media (prefers-color-scheme: light) {
  .sdb-08 {
    --sdb-08-bg: #f7f2ea;
    --sdb-08-surf: #ffffff;
    --sdb-08-surf2: #efe7dc;
    --sdb-08-line: #ddd0c0;
    --sdb-08-ink: #241d17;
    --sdb-08-mut: #6c5c4e;
    --sdb-08-acc: #8a5210;
    --sdb-08-acc: oklch(48% 0.11 68);
    --sdb-08-acc-soft: #f2e3cf;
  }

  .sdb-08:has(.sdb-08__theme-input:checked) {
    --sdb-08-bg: #211d19;
    --sdb-08-surf: #2b2521;
    --sdb-08-surf2: #362e28;
    --sdb-08-line: #453b33;
    --sdb-08-ink: #f4ece3;
    --sdb-08-mut: #b3a496;
    --sdb-08-acc: #e0a13c;
    --sdb-08-acc: oklch(76% 0.14 72);
    --sdb-08-acc-soft: #3d3021;
  }
}

@media (prefers-color-scheme: dark) {
  .sdb-08:has(.sdb-08__theme-input:checked) {
    --sdb-08-bg: #f7f2ea;
    --sdb-08-surf: #ffffff;
    --sdb-08-surf2: #efe7dc;
    --sdb-08-line: #ddd0c0;
    --sdb-08-ink: #241d17;
    --sdb-08-mut: #6c5c4e;
    --sdb-08-acc: #8a5210;
    --sdb-08-acc: oklch(48% 0.11 68);
    --sdb-08-acc-soft: #f2e3cf;
  }
}

.sdb-08__theme {
  position: absolute;
  inset-block-start: 0.85rem;
  inset-inline-end: 0.85rem;
  z-index: 60;
}

.sdb-08__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.sdb-08__theme-label {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border: 2px solid var(--sdb-08-ink);
  background: var(--sdb-08-surf);
  color: var(--sdb-08-ink);
  box-shadow: 4px 4px 0 var(--sdb-08-ink);
  cursor: pointer;
}

.sdb-08__theme-label svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.sdb-08__theme-input:focus-visible + .sdb-08__theme-label {
  outline: 2px solid var(--sdb-08-acc);
  outline-offset: 3px;
}

.sdb-08__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sdb-08__app {
  display: flex;
  min-inline-size: 0;
  block-size: 100vh;
  background: var(--sdb-08-surf);
}

.sdb-08__rail {
  flex: none;
  inline-size: 13rem;
  min-inline-size: 0;
  min-block-size: 0;
  display: flex;
  flex-direction: column;
  border-inline-end: 2px solid var(--sdb-08-ink);
  background: var(--sdb-08-surf2);
  overflow-y: auto;
  overscroll-behavior: contain;
  scrollbar-gutter: stable;
}

.sdb-08__rail-title {
  position: sticky;
  inset-block-start: 0;
  margin: 0;
  padding: 0.6rem 0.7rem;
  z-index: 2;
  background: var(--sdb-08-surf2);
  border-block-end: 1px solid var(--sdb-08-line);
  font-family: var(--sdb-08-font-display);
  font-size: 0.78rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--sdb-08-mut);
}

.sdb-08__list {
  list-style: none;
  margin: 0;
  padding: 0.25rem;
}

.sdb-08__link {
  display: flex;
  align-items: center;
  min-block-size: 2.75rem;
  padding: 0.4rem 0.55rem;
  color: var(--sdb-08-ink);
  text-decoration: none;
  font-size: 0.88rem;
  min-inline-size: 0;
  font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
}

.sdb-08__link:hover {
  background: var(--sdb-08-acc-soft);
}

.sdb-08__link[aria-current="page"] {
  background: var(--sdb-08-acc);
  color: var(--sdb-08-bg);
  font-weight: 700;
}

.sdb-08__link:focus-visible {
  outline: 2px solid var(--sdb-08-acc);
  outline-offset: -2px;
}

.sdb-08__thread {
  flex: 1;
  min-inline-size: 0;
  min-block-size: 0;
  overflow-y: auto;
  overscroll-behavior: contain;
  padding: 1.1rem 1.25rem 2rem;
  display: grid;
  gap: 0.75rem;
  align-content: start;
}

@media (min-width: 46rem) {
  .sdb-08__thread {
    padding: 1.6rem 2rem 2.5rem;
  }
}

.sdb-08__channel {
  margin: 0 0 0.4rem;
  font-family: var(--sdb-08-font-display);
  font-size: 1.15rem;
  letter-spacing: 0.02em;
  color: var(--sdb-08-acc);
}

.sdb-08__msg {
  margin: 0;
  font-size: 0.92rem;
  color: var(--sdb-08-mut);
  max-inline-size: 44rem;
  text-wrap: pretty;
}

.sdb-08__msg b {
  color: var(--sdb-08-ink);
  display: block;
  font-size: 0.82rem;
  letter-spacing: 0.02em;
}
```
