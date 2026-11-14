---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-neumorphism/nexus/"
title: "Soft UI Navigation Rail with Active State"
section: "design-styles"
category: "css-neumorphism"
category_name: "CSS Neumorphism"
description: "A vertical rail and a mobile bottom bar where the current page is a pressed-in well and everything else sits flush."
has_js: "false"
---

Here's a working CSS Neumorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Soft UI Navigation Rail with Active State
Source: https://codefronts.com/design-styles/css-neumorphism/nexus/

A vertical rail and a mobile bottom bar where the current page is a pressed-in well and everything else sits flush. The active state is carried by depth, an accent bar, colour and aria-current together — because on a nav, getting the current-page indicator wrong is the difference between an interface and a maze.
## HTML
```html
<section class="nm-15" aria-labelledby="nm-15-heading">
      <input type="checkbox" id="nm-15-theme" class="nm-15__themeinput">
      <label for="nm-15-theme" class="nm-15__themebtn">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 3a9 9 0 1 0 9 9 7 7 0 0 1-9-9Z"/></svg>
        Theme
      </label>
  <div class="nm-15__stage">
    <header class="nm-15__head">
      <p class="nm-15__kicker">Pattern · navigation</p>
      <h2 class="nm-15__heading" id="nm-15-heading">The current page is the one pushed in</h2>
      <p class="nm-15__sub">Depth, an accent bar, colour and <code>aria-current</code> — four signals, because a nav that lies is worse than no nav.</p>
    </header>

    <div class="nm-15__demo">
      <nav class="nm-15__rail" aria-label="Workspace">
        <p class="nm-15__brand">Meridian</p>
        <ul class="nm-15__list">
          <li><a class="nm-15__item" href="#nm-15-heading">
            <span class="nm-15__ico" aria-hidden="true"><svg viewBox="0 0 24 24" width="19" height="19"><path d="M4 11 12 4l8 7v8a1 1 0 0 1-1 1h-4v-6H9v6H5a1 1 0 0 1-1-1v-8z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg></span>Overview</a></li>
          <li><a class="nm-15__item" href="#nm-15-heading" aria-current="page">
            <span class="nm-15__ico" aria-hidden="true"><svg viewBox="0 0 24 24" width="19" height="19"><path d="M5 19V9M10 19V5M15 19v-7M20 19v-4" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></span>Reports</a></li>
          <li><a class="nm-15__item" href="#nm-15-heading">
            <span class="nm-15__ico" aria-hidden="true"><svg viewBox="0 0 24 24" width="19" height="19"><rect x="4" y="5" width="16" height="14" rx="2" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M4 10h16M9 5v14" fill="none" stroke="currentColor" stroke-width="1.8"/></svg></span>Ledger</a></li>
          <li><a class="nm-15__item" href="#nm-15-heading">
            <span class="nm-15__ico" aria-hidden="true"><svg viewBox="0 0 24 24" width="19" height="19"><circle cx="12" cy="8.5" r="3.6" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M5 19.5c1.4-3.4 4-5.1 7-5.1s5.6 1.7 7 5.1" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg></span>Clients</a></li>
          <li><a class="nm-15__item" href="#nm-15-heading">
            <span class="nm-15__ico" aria-hidden="true"><svg viewBox="0 0 24 24" width="19" height="19"><circle cx="12" cy="12" r="3.2" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M12 3.5v2.4M12 18.1v2.4M20.5 12h-2.4M5.9 12H3.5M18 6l-1.7 1.7M7.7 16.3 6 18M18 18l-1.7-1.7M7.7 7.7 6 6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg></span>Settings</a></li>
        </ul>
      </nav>

      <div class="nm-15__content">
        <div class="nm-15__panel">
          <h3 class="nm-15__ptitle">Reports</h3>
          <p class="nm-15__pbody">The rail's active item is inset, accented and marked <code>aria-current="page"</code>. Everything else sits flush with the rail — depth is spent where it carries meaning.</p>
        </div>

        <nav class="nm-15__bar" aria-label="Sections">
          <a class="nm-15__tab" href="#nm-15-heading">
            <span class="nm-15__ico" aria-hidden="true"><svg viewBox="0 0 24 24" width="19" height="19"><path d="M4 11 12 4l8 7v8a1 1 0 0 1-1 1h-4v-6H9v6H5a1 1 0 0 1-1-1v-8z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg></span>Home</a>
          <a class="nm-15__tab" href="#nm-15-heading" aria-current="page">
            <span class="nm-15__ico" aria-hidden="true"><svg viewBox="0 0 24 24" width="19" height="19"><path d="M5 19V9M10 19V5M15 19v-7M20 19v-4" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></span>Reports</a>
          <a class="nm-15__tab" href="#nm-15-heading">
            <span class="nm-15__ico" aria-hidden="true"><svg viewBox="0 0 24 24" width="19" height="19"><circle cx="11" cy="11" r="6.4" fill="none" stroke="currentColor" stroke-width="1.9"/><path d="M15.8 15.8 20 20" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg></span>Search</a>
          <a class="nm-15__tab" href="#nm-15-heading">
            <span class="nm-15__ico" aria-hidden="true"><svg viewBox="0 0 24 24" width="19" height="19"><circle cx="12" cy="8.5" r="3.6" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M5 19.5c1.4-3.4 4-5.1 7-5.1s5.6 1.7 7 5.1" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg></span>You</a>
        </nav>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.nm-15 {
  position: relative;
  --nm-15-surface: #e7e5e9;
  --nm-15-dark: rgba(174,170,180,0.62);
  --nm-15-light: rgba(255,255,255,0.94);
  --nm-15-ink: #282630;
  --nm-15-muted: #5c5867;
  --nm-15-border: #9a95a4;
  --nm-15-accent: #6a4b8f;
  --nm-15-railw: 214px;
  --nm-15-font-display: "Public Sans", "Helvetica Neue", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--nm-15-surface);
  color: var(--nm-15-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

@supports (color: oklch(0.9 0.01 300)) {
  .nm-15 {
    --nm-15-surface: oklch(0.916 0.008 300);
    --nm-15-ink: oklch(0.27 0.018 300);
    --nm-15-muted: oklch(0.46 0.02 300);
    --nm-15-accent: oklch(0.47 0.11 300);
  }
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-15 {
    --nm-15-dark: color-mix(in oklab, var(--nm-15-surface), #000 19%);
    --nm-15-light: color-mix(in oklab, var(--nm-15-surface), #fff 92%);
    --nm-15-border: color-mix(in oklab, var(--nm-15-surface), var(--nm-15-ink) 33%);
  }
}

.nm-15 *,
.nm-15 *::before,
.nm-15 *::after {
  box-sizing: border-box;
}

.nm-15__stage {
  max-width: 1000px;
  margin: 0 auto;
  min-height: 100vh;
  padding: clamp(26px, 5vw, 56px) clamp(16px, 4vw, 40px);
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: clamp(22px, 3.6vw, 34px);
}

.nm-15__head {
  max-width: 58ch;
  display: flex;
  flex-direction: column;
  gap: 9px;
}

.nm-15__kicker {
  margin: 0;
  font-size: 0.7rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--nm-15-muted);
}

.nm-15__heading {
  margin: 0;
  font-family: var(--nm-15-font-display);
  font-size: clamp(1.5rem, 4.2vw, 2.2rem);
  font-weight: 650;
  letter-spacing: -0.025em;
  line-height: 1.12;
  text-wrap: balance;
}

.nm-15__sub {
  margin: 0;
  font-size: 0.94rem;
  line-height: 1.6;
  color: var(--nm-15-muted);
  text-wrap: pretty;
}

.nm-15__sub code,
.nm-15__pbody code {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.88em;
  color: var(--nm-15-ink);
  overflow-wrap: anywhere;
}

.nm-15__demo {
  display: grid;
  grid-template-columns: 1fr;
  gap: clamp(18px, 3vw, 28px);
  align-items: start;
}

@media (min-width: 720px) {
  .nm-15__demo {
    grid-template-columns: var(--nm-15-railw) minmax(0, 1fr);
  }
}

.nm-15__rail {
  border-radius: 22px;
  padding: 18px 14px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  min-inline-size: 0;
  background: var(--nm-15-surface);
  border: 1px solid var(--nm-15-border);
  box-shadow: 10px 10px 22px var(--nm-15-dark), -10px -10px 22px var(--nm-15-light);
}

.nm-15__brand {
  margin: 0 6px;
  font-family: var(--nm-15-font-display);
  font-size: 0.86rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--nm-15-accent);
}

.nm-15__list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 6px;
}

.nm-15__item {
  position: relative;
  display: flex;
  align-items: center;
  gap: 12px;
  min-height: 46px;
  padding: 0 14px;
  border-radius: 13px;
  color: var(--nm-15-muted);
  text-decoration: none;
  font-family: var(--nm-15-font-display);
  font-size: 0.88rem;
  font-weight: 500;
  min-inline-size: 0;
  transition: box-shadow 160ms ease, color 160ms ease;
}

.nm-15__item:hover {
  color: var(--nm-15-ink);
  box-shadow: 4px 4px 10px var(--nm-15-dark), -4px -4px 10px var(--nm-15-light);
}

.nm-15__item:focus-visible {
  outline: 2px solid var(--nm-15-accent);
  outline-offset: -2px;
}

.nm-15__item[aria-current="page"] {
  color: var(--nm-15-ink);
  font-weight: 650;
  box-shadow: inset 4px 4px 9px var(--nm-15-dark), inset -4px -4px 9px var(--nm-15-light);
}

.nm-15__item[aria-current="page"]::before {
  content: "";
  position: absolute;
  inset-inline-start: 5px;
  inset-block: 12px;
  width: 3px;
  border-radius: 999px;
  background: var(--nm-15-accent);
}

.nm-15__item[aria-current="page"] .nm-15__ico {
  color: var(--nm-15-accent);
}

.nm-15__ico {
  display: inline-flex;
  flex: none;
}

.nm-15__content {
  display: flex;
  flex-direction: column;
  gap: clamp(16px, 3vw, 24px);
  min-inline-size: 0;
}

.nm-15__panel {
  border-radius: 20px;
  padding: clamp(18px, 3vw, 26px);
  min-inline-size: 0;
  background: var(--nm-15-surface);
  border: 1px solid var(--nm-15-border);
  box-shadow: inset 5px 5px 12px var(--nm-15-dark), inset -5px -5px 12px var(--nm-15-light);
}

.nm-15__ptitle {
  margin: 0 0 8px;
  font-family: var(--nm-15-font-display);
  font-size: 1.1rem;
  font-weight: 650;
  letter-spacing: -0.015em;
}

.nm-15__pbody {
  margin: 0;
  font-size: 0.86rem;
  line-height: 1.62;
  color: var(--nm-15-muted);
  text-wrap: pretty;
}

.nm-15__bar {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 6px;
  padding: 8px;
  border-radius: 20px;
  background: var(--nm-15-surface);
  border: 1px solid var(--nm-15-border);
  box-shadow: 8px 8px 18px var(--nm-15-dark), -8px -8px 18px var(--nm-15-light);
}

.nm-15__tab {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 5px;
  min-height: 58px;
  border-radius: 14px;
  color: var(--nm-15-muted);
  text-decoration: none;
  font-family: var(--nm-15-font-display);
  font-size: 0.72rem;
  font-weight: 500;
  min-inline-size: 0;
  transition: box-shadow 160ms ease, color 160ms ease;
}

.nm-15__tab:hover {
  color: var(--nm-15-ink);
}

.nm-15__tab:focus-visible {
  outline: 2px solid var(--nm-15-accent);
  outline-offset: -2px;
}

.nm-15__tab[aria-current="page"] {
  color: var(--nm-15-accent);
  font-weight: 650;
  box-shadow: inset 4px 4px 9px var(--nm-15-dark), inset -4px -4px 9px var(--nm-15-light);
}

@media (prefers-reduced-motion: reduce) {
  .nm-15__item,
    .nm-15__tab {
    transition: none;
  }
}

@media (prefers-color-scheme: dark) {
  .nm-15 {
    --nm-15-surface: #292730;
    --nm-15-dark: rgba(11,11,14,0.72);
    --nm-15-light: rgba(90,87,100,0.44);
    --nm-15-ink: #e9e7ef;
    --nm-15-muted: #a09baf;
    --nm-15-border: #888196;
    --nm-15-accent: #b394e0;
  }

  @supports (color: color-mix(in oklab, #fff, #000)) {
    .nm-15 {
      --nm-15-dark: color-mix(in oklab, var(--nm-15-surface), #000 55%);
      --nm-15-light: color-mix(in oklab, var(--nm-15-surface), #fff 14%);
    }
  }
}

.nm-15[data-theme="dark"] {
  --nm-15-surface: #292730;
  --nm-15-dark: rgba(11,11,14,0.72);
  --nm-15-light: rgba(90,87,100,0.44);
  --nm-15-ink: #e9e7ef;
  --nm-15-muted: #a09baf;
  --nm-15-border: #888196;
  --nm-15-accent: #b394e0;
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-15[data-theme="dark"] {
    --nm-15-dark: color-mix(in oklab, var(--nm-15-surface), #000 55%);
    --nm-15-light: color-mix(in oklab, var(--nm-15-surface), #fff 14%);
  }
}
/* Pure-CSS theme toggle. Mirrors the [data-theme="dark"] rules above so
   the demo's own dark palette is reachable from inside the demo. */

.nm-15__themeinput {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: 0;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.nm-15__themebtn {
  position: absolute;
  inset-block-start: clamp(10px, 2vw, 18px);
  inset-inline-end: clamp(10px, 2vw, 18px);
  z-index: 5;
  display: inline-flex;
  align-items: center;
  gap: 7px;
  min-height: 44px;
  padding: 0 14px;
  border-radius: 999px;
  background: var(--nm-15-surface);
  color: var(--nm-15-ink);
  border: 1px solid var(--nm-15-line);
  font: 600 11px/1 var(--nm-15-font-display, system-ui);
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
  box-shadow: var(--nm-15-distance, 6px) var(--nm-15-distance, 6px) var(--nm-15-blur, 14px) var(--nm-15-dark), calc(-1 * var(--nm-15-distance, 6px)) calc(-1 * var(--nm-15-distance, 6px)) var(--nm-15-blur, 14px) var(--nm-15-light);
  transition: box-shadow 180ms ease, color 180ms ease;
}

.nm-15__themebtn:hover {
  color: var(--nm-15-ink);
}

.nm-15__themeinput:focus-visible + .nm-15__themebtn {
  outline: 2px solid var(--nm-15-ink);
  outline-offset: 3px;
}

.nm-15:has(#nm-15-theme:checked) .nm-15__themebtn {
  box-shadow: inset var(--nm-15-distance, 6px) var(--nm-15-distance, 6px) var(--nm-15-blur, 14px) var(--nm-15-dark), inset calc(-1 * var(--nm-15-distance, 6px)) calc(-1 * var(--nm-15-distance, 6px)) var(--nm-15-blur, 14px) var(--nm-15-light);
}

.nm-15__themebtn svg {
  inline-size: 13px;
  block-size: 13px;
  flex: none;
}

.nm-15:has(#nm-15-theme:checked) {
  --nm-15-surface: #292730;
  --nm-15-dark: rgba(11,11,14,0.72);
  --nm-15-light: rgba(90,87,100,0.44);
  --nm-15-ink: #e9e7ef;
  --nm-15-muted: #a09baf;
  --nm-15-border: #888196;
  --nm-15-accent: #b394e0;
}

@media (prefers-color-scheme: light) {
  .nm-15:has(#nm-15-theme:checked) {
    --nm-15-surface: #292730;
    --nm-15-dark: rgba(11,11,14,0.72);
    --nm-15-light: rgba(90,87,100,0.44);
    --nm-15-ink: #e9e7ef;
    --nm-15-muted: #a09baf;
    --nm-15-border: #888196;
    --nm-15-accent: #b394e0;
  }
}

@media (prefers-color-scheme: dark) {
  /* Base already resolves dark here, so :checked restores light —
       without this the toggle is inert for dark-OS visitors. */

  .nm-15:has(#nm-15-theme:checked) {
    --nm-15-surface: #e7e5e9;
    --nm-15-dark: rgba(174,170,180,0.62);
    --nm-15-light: rgba(255,255,255,0.94);
    --nm-15-ink: #282630;
    --nm-15-muted: #5c5867;
    --nm-15-border: #9a95a4;
    --nm-15-accent: #6a4b8f;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nm-15__themebtn {
    transition: none;
  }
}
```
