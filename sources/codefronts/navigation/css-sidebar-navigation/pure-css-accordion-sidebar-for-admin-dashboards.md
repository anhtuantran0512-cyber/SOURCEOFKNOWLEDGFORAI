---
source: "codefronts"
url: "https://codefronts.com/navigation/css-sidebar-navigation/pure-css-accordion-sidebar-for-admin-dashboards/"
title: "Accordion Sidebar with Details and Summary"
section: "navigation"
category: "css-sidebar-navigation"
category_name: "CSS Sidebar Navigation"
description: "Native <details> and <summary> groups, including the name attribute that makes them behave as an exclusive accordion with no script at all."
has_js: "false"
---

Here's a working CSS Sidebar Navigation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Accordion Sidebar with Details and Summary
Source: https://codefronts.com/navigation/css-sidebar-navigation/pure-css-accordion-sidebar-for-admin-dashboards/

Native <details> and <summary> groups, including the name attribute that makes them behave as an exclusive accordion with no script at all. What you get free: a real disclosure control, keyboard operation, and expanded state exposed by the browser. Where it stops: animation, exclusive behaviour on older engines, and the fact that closing a group as another opens can move the item a user was aiming at.
## HTML
```html
<section class="sdb-16" aria-label="Quill mail">
  <div class="sdb-16__theme">
    <input class="sdb-16__theme-input" type="checkbox" id="sdb-16-theme">
    <label class="sdb-16__theme-label" for="sdb-16-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sdb-16__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="sdb-16__app">
    <nav class="sdb-16__rail" aria-label="Quill mailboxes">
      <div class="sdb-16__rail-head">
        <p class="sdb-16__brand">Quill</p>
        <p class="sdb-16__who">Sam Rivera</p>
      </div>

      <details class="sdb-16__group" name="sdb-16-accordion" open>
        <summary class="sdb-16__sum">
          <svg class="sdb-16__chev" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M9 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>
          Mail
        </summary>
        <ul class="sdb-16__list">
          <li><a class="sdb-16__link" href="#sdb-16-main" aria-current="page">Inbox <span class="sdb-16__n">12 unread</span></a></li>
          <li><a class="sdb-16__link" href="#sdb-16-main">Starred</a></li>
          <li><a class="sdb-16__link" href="#sdb-16-main">Sent</a></li>
          <li><a class="sdb-16__link" href="#sdb-16-main">Drafts <span class="sdb-16__n">3</span></a></li>
        </ul>
      </details>

      <details class="sdb-16__group" name="sdb-16-accordion">
        <summary class="sdb-16__sum">
          <svg class="sdb-16__chev" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M9 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>
          Shared inboxes
        </summary>
        <ul class="sdb-16__list">
          <li><a class="sdb-16__link" href="#sdb-16-main">Support <span class="sdb-16__n">41 unread</span></a></li>
          <li><a class="sdb-16__link" href="#sdb-16-main">Billing</a></li>
          <li><a class="sdb-16__link" href="#sdb-16-main">Security reports</a></li>
        </ul>
      </details>

      <details class="sdb-16__group" name="sdb-16-accordion">
        <summary class="sdb-16__sum">
          <svg class="sdb-16__chev" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M9 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>
          Settings
        </summary>
        <ul class="sdb-16__list">
          <li><a class="sdb-16__link" href="#sdb-16-main">Filters</a></li>
          <li><a class="sdb-16__link" href="#sdb-16-main">Signatures</a></li>
          <li><a class="sdb-16__link" href="#sdb-16-main">Forwarding</a></li>
        </ul>
      </details>
    </nav>

    <main class="sdb-16__main" id="sdb-16-main">
      <h2 class="sdb-16__main-h">Inbox</h2>
      <ul class="sdb-16__mail">
        <li><p class="sdb-16__from">Priya Sharma</p><p class="sdb-16__subj">Rollback runbook &mdash; review before Thursday</p><p class="sdb-16__prev">I have added the verification step we discussed&hellip;</p></li>
        <li><p class="sdb-16__from">Vale Operations</p><p class="sdb-16__subj">Access request: audit log export</p><p class="sdb-16__prev">Jordan needs read access for the quarter&hellip;</p></li>
        <li><p class="sdb-16__from">Basalt Hosting</p><p class="sdb-16__subj">Certificate renewal completed</p><p class="sdb-16__prev">No action needed. The new certificate&hellip;</p></li>
        <li><p class="sdb-16__from">Ada Okafor</p><p class="sdb-16__subj">Region failover drill, Friday 14:00</p><p class="sdb-16__prev">Adding you as the observer for eu-west&hellip;</p></li>
        <li><p class="sdb-16__from">Fern Studio</p><p class="sdb-16__subj">Invoice 4471 attached</p><p class="sdb-16__prev">Net 30, payable on the usual account&hellip;</p></li>
      </ul>
    </main>
  </div>
</section>
```
## CSS
```css
.sdb-16 {
  --sdb-16-bg: #f1f3f5;
  --sdb-16-surf: #ffffff;
  --sdb-16-surf2: #e7eaee;
  --sdb-16-surf3: #dde1e7;
  --sdb-16-line: #cfd5dc;
  --sdb-16-ink: #131720;
  --sdb-16-mut: #59616e;
  --sdb-16-acc: #2b4a8f;
  --sdb-16-acc: oklch(42% 0.13 264);
  --sdb-16-acc-soft: #e0e7f6;
  --sdb-16-font-display: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--sdb-16-bg);
  color: var(--sdb-16-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.sdb-16 *,
.sdb-16 *::before,
.sdb-16 *::after {
  box-sizing: border-box;
}

.sdb-16:has(.sdb-16__theme-input:checked) {
  --sdb-16-bg: #0b0e14;
  --sdb-16-surf: #12161f;
  --sdb-16-surf2: #191e29;
  --sdb-16-surf3: #202634;
  --sdb-16-line: #262d3b;
  --sdb-16-ink: #e8ecf3;
  --sdb-16-mut: #909aab;
  --sdb-16-acc: #8fabf0;
  --sdb-16-acc: oklch(78% 0.11 264);
  --sdb-16-acc-soft: #1a2238;
}

@media (prefers-color-scheme: dark) {
  .sdb-16 {
    --sdb-16-bg: #0b0e14;
    --sdb-16-surf: #12161f;
    --sdb-16-surf2: #191e29;
    --sdb-16-surf3: #202634;
    --sdb-16-line: #262d3b;
    --sdb-16-ink: #e8ecf3;
    --sdb-16-mut: #909aab;
    --sdb-16-acc: #8fabf0;
    --sdb-16-acc: oklch(78% 0.11 264);
    --sdb-16-acc-soft: #1a2238;
  }

  .sdb-16:has(.sdb-16__theme-input:checked) {
    --sdb-16-bg: #f1f3f5;
    --sdb-16-surf: #ffffff;
    --sdb-16-surf2: #e7eaee;
    --sdb-16-surf3: #dde1e7;
    --sdb-16-line: #cfd5dc;
    --sdb-16-ink: #131720;
    --sdb-16-mut: #59616e;
    --sdb-16-acc: #2b4a8f;
    --sdb-16-acc: oklch(42% 0.13 264);
    --sdb-16-acc-soft: #e0e7f6;
  }
}

@media (prefers-color-scheme: light) {
  .sdb-16:has(.sdb-16__theme-input:checked) {
    --sdb-16-bg: #0b0e14;
    --sdb-16-surf: #12161f;
    --sdb-16-surf2: #191e29;
    --sdb-16-surf3: #202634;
    --sdb-16-line: #262d3b;
    --sdb-16-ink: #e8ecf3;
    --sdb-16-mut: #909aab;
    --sdb-16-acc: #8fabf0;
    --sdb-16-acc: oklch(78% 0.11 264);
    --sdb-16-acc-soft: #1a2238;
  }
}

.sdb-16__theme {
  position: absolute;
  inset-block-start: 0.85rem;
  inset-inline-end: 0.85rem;
  z-index: 60;
}

.sdb-16__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.sdb-16__theme-label {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border-radius: 0.6rem;
  border: 1px solid var(--sdb-16-line);
  background: var(--sdb-16-surf);
  color: var(--sdb-16-ink);
  cursor: pointer;
}

.sdb-16__theme-label svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.sdb-16__theme-input:focus-visible + .sdb-16__theme-label {
  outline: 2px solid var(--sdb-16-acc);
  outline-offset: 2px;
}

.sdb-16__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sdb-16__app {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  min-block-size: 100vh;
  background: var(--sdb-16-bg);
}

@media (min-width: 46rem) {
  .sdb-16__app {
    grid-template-columns: minmax(0, 16.5rem) minmax(0, 1fr);
  }
}

.sdb-16__rail {
  min-inline-size: 0;
  align-content: start;
  padding: 0.75rem 0.6rem;
  background: var(--sdb-16-surf2);
}

@media (min-width: 46rem) {
  .sdb-16__rail {
    border-inline-end: 1px solid var(--sdb-16-line);
  }
}

.sdb-16__rail-head {
  padding: 0.5rem 0.6rem 0.8rem;
}

.sdb-16__brand {
  margin: 0;
  font-family: var(--sdb-16-font-display);
  font-size: 1.2rem;
  font-weight: 700;
  letter-spacing: -0.02em;
  color: var(--sdb-16-acc);
}

.sdb-16__who {
  margin: 0;
  font-size: 0.78rem;
  color: var(--sdb-16-mut);
}

.sdb-16__group {
  margin-block-end: 0.3rem;
  border-radius: 0.6rem;
  background: var(--sdb-16-surf);
  overflow: hidden;
}

.sdb-16__sum {
  display: flex;
  align-items: center;
  gap: 0.55rem;
  min-block-size: 2.75rem;
  padding: 0.5rem 0.7rem;
  cursor: pointer;
  list-style: none;
  font-size: 0.92rem;
  font-weight: 600;
}

.sdb-16__sum::-webkit-details-marker {
  display: none;
}

.sdb-16__sum:hover {
  background: var(--sdb-16-surf3);
}

.sdb-16__sum:focus-visible,
.sdb-16__link:focus-visible {
  outline: 2px solid var(--sdb-16-acc);
  outline-offset: -2px;
}

.sdb-16__chev {
  inline-size: 1rem;
  block-size: 1rem;
  flex: none;
  color: var(--sdb-16-mut);
  transition: transform 150ms ease;
}

.sdb-16__group[open] .sdb-16__chev {
  transform: rotate(90deg);
}

.sdb-16__group:has([aria-current="page"]) .sdb-16__sum {
  color: var(--sdb-16-acc);
}

.sdb-16__list {
  list-style: none;
  margin: 0;
  padding: 0 0.35rem 0.4rem;
}

.sdb-16__link {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  min-block-size: 2.75rem;
  padding: 0.45rem 0.6rem;
  border-radius: 0.45rem;
  color: var(--sdb-16-ink);
  text-decoration: none;
  font-size: 0.89rem;
  min-inline-size: 0;
}

.sdb-16__link:hover {
  background: var(--sdb-16-surf2);
}

.sdb-16__link[aria-current="page"] {
  background: var(--sdb-16-acc-soft);
  color: var(--sdb-16-acc);
  font-weight: 650;
}

.sdb-16__n {
  margin-inline-start: auto;
  font-size: 0.74rem;
  color: var(--sdb-16-mut);
  font-variant-numeric: tabular-nums;
}

.sdb-16__link[aria-current="page"] .sdb-16__n {
  color: var(--sdb-16-acc);
}

.sdb-16__main {
  min-inline-size: 0;
  padding: 1.4rem 1.25rem 2.5rem;
  align-content: start;
  background: var(--sdb-16-surf);
}

@media (min-width: 46rem) {
  .sdb-16__main {
    padding: 2.2rem 2rem 3rem;
  }
}

.sdb-16__main-h {
  margin: 0 0 1rem;
  font-size: clamp(1.3rem, 3.2vw, 1.7rem);
  letter-spacing: -0.015em;
}

.sdb-16__mail {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 0.55rem;
  max-inline-size: 46rem;
}

.sdb-16__mail li {
  min-inline-size: 0;
  padding: 0.75rem 0.85rem;
  border-radius: 0.6rem;
  background: var(--sdb-16-surf2);
}

.sdb-16__from {
  margin: 0;
  font-size: 0.78rem;
  color: var(--sdb-16-acc);
  font-weight: 650;
}

.sdb-16__subj {
  margin: 0.05rem 0;
  font-size: 0.94rem;
  font-weight: 600;
  min-inline-size: 0;
}

.sdb-16__prev {
  margin: 0;
  font-size: 0.82rem;
  color: var(--sdb-16-mut);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

@media (prefers-reduced-motion: reduce) {
  .sdb-16__chev {
    transition: none;
  }
}
```
