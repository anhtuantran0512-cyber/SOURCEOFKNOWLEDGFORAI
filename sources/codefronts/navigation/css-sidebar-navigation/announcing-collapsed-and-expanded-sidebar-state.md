---
source: "codefronts"
url: "https://codefronts.com/navigation/css-sidebar-navigation/announcing-collapsed-and-expanded-sidebar-state/"
title: "Announcing Collapsed and Expanded Sidebar State"
section: "navigation"
category: "css-sidebar-navigation"
category_name: "CSS Sidebar Navigation"
description: "Collapsing a sidebar to an icon rail is a visual change that assistive technology has to perceive too."
has_js: "true"
---

Here's a working CSS Sidebar Navigation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Announcing Collapsed and Expanded Sidebar State
Source: https://codefronts.com/navigation/css-sidebar-navigation/announcing-collapsed-and-expanded-sidebar-state/

Collapsing a sidebar to an icon rail is a visual change that assistive technology has to perceive too. aria-expanded on the toggle covers the state, but once the labels are gone the icons need accessible names of their own &mdash; visually hidden text or aria-label, never a title attribute, which is announced inconsistently and not at all on touch. The label text stays in the DOM and is clipped rather than removed, so the names survive the collapse.
## HTML
```html
<section class="sdb-05" aria-label="Nova player">
  <div class="sdb-05__theme">
    <input class="sdb-05__theme-input" type="checkbox" id="sdb-05-theme">
    <label class="sdb-05__theme-label" for="sdb-05-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="sdb-05__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="sdb-05__app" data-sdb-05-state="expanded">
    <div class="sdb-05__rail" id="sdb-05-rail">
      <div class="sdb-05__rail-head">
        <p class="sdb-05__brand"><span aria-hidden="true">&#9679;</span><span class="sdb-05__label">Nova</span></p>
        <button class="sdb-05__collapse" type="button" id="sdb-05-toggle" aria-expanded="true" aria-controls="sdb-05-rail">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M14 6l-6 6 6 6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
          <span class="sdb-05__sr">Collapse sidebar</span>
        </button>
      </div>
      <nav class="sdb-05__nav" aria-label="Nova library">
        <ul class="sdb-05__list">
          <li><a class="sdb-05__link" href="#sdb-05-main" aria-current="page">
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 6h16M4 12h16M4 18h9" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
            <span class="sdb-05__label">Listen now</span></a></li>
          <li><a class="sdb-05__link" href="#sdb-05-main">
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="12" r="2.4" fill="currentColor"/></svg>
            <span class="sdb-05__label">Albums</span></a></li>
          <li><a class="sdb-05__link" href="#sdb-05-main">
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6 19V7l12-2v12" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><circle cx="6" cy="19" r="2.2" fill="currentColor"/><circle cx="18" cy="17" r="2.2" fill="currentColor"/></svg>
            <span class="sdb-05__label">Playlists</span></a></li>
          <li><a class="sdb-05__link" href="#sdb-05-main">
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 20s-7-4.6-7-9a4 4 0 0 1 7-2.6A4 4 0 0 1 19 11c0 4.4-7 9-7 9Z" fill="none" stroke="currentColor" stroke-width="1.8"/></svg>
            <span class="sdb-05__label">Favourites</span></a></li>
          <li><a class="sdb-05__link" href="#sdb-05-main">
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 18V9m5 9V5m5 13v-7m5 7V7" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
            <span class="sdb-05__label">Recently played</span></a></li>
        </ul>
      </nav>
    </div>

    <main class="sdb-05__main" id="sdb-05-main">
      <p class="sdb-05__eyebrow">Now playing</p>
      <h2 class="sdb-05__title">Field Recordings, Vol. 2</h2>
      <p class="sdb-05__meta">Basalt Ensemble &middot; 11 tracks &middot; 48 min</p>
      <ol class="sdb-05__tracks">
        <li><span>1</span> Low Tide <em>4:12</em></li>
        <li><span>2</span> Harbour Wall <em>3:48</em></li>
        <li><span>3</span> Kestrel <em>5:31</em></li>
        <li><span>4</span> Slack Water <em>4:02</em></li>
        <li><span>5</span> Two Bells <em>3:19</em></li>
        <li><span>6</span> Ebb <em>6:07</em></li>
      </ol>
    </main>
  </div>
</section>
```
## CSS
```css
.sdb-05 {
  --sdb-05-bg: #f4f5f3;
  --sdb-05-surf: #ffffff;
  --sdb-05-surf2: #e9ebe6;
  --sdb-05-rail: #16181a;
  --sdb-05-line: #d6d9d3;
  --sdb-05-ink: #14161a;
  --sdb-05-mut: #5d6268;
  --sdb-05-on-rail: #e8ebe4;
  --sdb-05-acc: #4f7a15;
  --sdb-05-acc: oklch(56% 0.16 128);
  --sdb-05-acc-soft: #e6f0d6;
  --sdb-05-w-open: 15rem;
  --sdb-05-w-rail: 4.25rem;
  --sdb-05-font-display: "Avenir Next Rounded", "Nunito", "Trebuchet MS", ui-rounded, system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--sdb-05-bg);
  color: var(--sdb-05-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.sdb-05 *,
.sdb-05 *::before,
.sdb-05 *::after {
  box-sizing: border-box;
}

.sdb-05:has(.sdb-05__theme-input:checked) {
  --sdb-05-bg: #050506;
  --sdb-05-surf: #0e0f11;
  --sdb-05-surf2: #16181b;
  --sdb-05-rail: #0a0b0c;
  --sdb-05-line: #23262a;
  --sdb-05-ink: #eef0ec;
  --sdb-05-mut: #949a9f;
  --sdb-05-on-rail: #eef0ec;
  --sdb-05-acc: #b6f24a;
  --sdb-05-acc: oklch(90% 0.22 128);
  --sdb-05-acc-soft: #1d2a10;
}

@media (prefers-color-scheme: dark) {
  .sdb-05 {
    --sdb-05-bg: #050506;
    --sdb-05-surf: #0e0f11;
    --sdb-05-surf2: #16181b;
    --sdb-05-rail: #0a0b0c;
    --sdb-05-line: #23262a;
    --sdb-05-ink: #eef0ec;
    --sdb-05-mut: #949a9f;
    --sdb-05-on-rail: #eef0ec;
    --sdb-05-acc: #b6f24a;
    --sdb-05-acc: oklch(90% 0.22 128);
    --sdb-05-acc-soft: #1d2a10;
  }

  .sdb-05:has(.sdb-05__theme-input:checked) {
    --sdb-05-bg: #f4f5f3;
    --sdb-05-surf: #ffffff;
    --sdb-05-surf2: #e9ebe6;
    --sdb-05-rail: #16181a;
    --sdb-05-line: #d6d9d3;
    --sdb-05-ink: #14161a;
    --sdb-05-mut: #5d6268;
    --sdb-05-on-rail: #e8ebe4;
    --sdb-05-acc: #4f7a15;
    --sdb-05-acc: oklch(56% 0.16 128);
    --sdb-05-acc-soft: #e6f0d6;
  }
}

@media (prefers-color-scheme: light) {
  .sdb-05:has(.sdb-05__theme-input:checked) {
    --sdb-05-bg: #050506;
    --sdb-05-surf: #0e0f11;
    --sdb-05-surf2: #16181b;
    --sdb-05-rail: #0a0b0c;
    --sdb-05-line: #23262a;
    --sdb-05-ink: #eef0ec;
    --sdb-05-mut: #949a9f;
    --sdb-05-on-rail: #eef0ec;
    --sdb-05-acc: #b6f24a;
    --sdb-05-acc: oklch(90% 0.22 128);
    --sdb-05-acc-soft: #1d2a10;
  }
}

.sdb-05__theme {
  position: absolute;
  inset-block-start: 0.85rem;
  inset-inline-end: 0.85rem;
  z-index: 60;
}

.sdb-05__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.sdb-05__theme-label {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border-radius: 1.4rem;
  border: 1px solid var(--sdb-05-line);
  background: var(--sdb-05-surf);
  color: var(--sdb-05-ink);
  cursor: pointer;
}

.sdb-05__theme-label svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.sdb-05__theme-input:focus-visible + .sdb-05__theme-label {
  outline: 2px solid var(--sdb-05-acc);
  outline-offset: 2px;
}

.sdb-05__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sdb-05__app {
  display: flex;
  min-inline-size: 0;
  min-block-size: 100vh;
  background: var(--sdb-05-surf);
}

.sdb-05__rail {
  flex: none;
  inline-size: var(--sdb-05-w-open);
  min-inline-size: 0;
  display: flex;
  flex-direction: column;
  background: var(--sdb-05-rail);
  color: var(--sdb-05-on-rail);
  transition: inline-size 220ms ease;
}

.sdb-05__app[data-sdb-05-state="collapsed"] .sdb-05__rail {
  inline-size: var(--sdb-05-w-rail);
}

.sdb-05__rail-head {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.6rem 0.65rem;
}

.sdb-05__brand {
  margin: 0 auto 0 0;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-family: var(--sdb-05-font-display);
  font-weight: 700;
  font-size: 1.05rem;
  color: var(--sdb-05-acc);
  min-inline-size: 0;
}

.sdb-05__collapse {
  flex: none;
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border-radius: 1.4rem;
  border: 0;
  background: rgba(255, 255, 255, 0.08);
  color: inherit;
  cursor: pointer;
}

.sdb-05__collapse svg {
  inline-size: 1.1rem;
  block-size: 1.1rem;
  transition: transform 200ms ease;
}

.sdb-05__app[data-sdb-05-state="collapsed"] .sdb-05__collapse svg {
  transform: rotate(180deg);
}

.sdb-05__nav {
  padding: 0.35rem 0.5rem 0.8rem;
  min-inline-size: 0;
}

.sdb-05__list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 0.2rem;
}

.sdb-05__link {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  min-block-size: 2.75rem;
  padding: 0.5rem 0.7rem;
  border-radius: 1.4rem;
  color: inherit;
  text-decoration: none;
  font-size: 0.93rem;
  min-inline-size: 0;
  white-space: nowrap;
}

.sdb-05__link svg {
  inline-size: 1.2rem;
  block-size: 1.2rem;
  flex: none;
  opacity: 0.75;
}

.sdb-05__link:hover {
  background: rgba(255, 255, 255, 0.09);
}

.sdb-05__link[aria-current="page"] {
  background: var(--sdb-05-acc);
  color: #10140a;
  font-weight: 650;
}

.sdb-05__link[aria-current="page"] svg {
  opacity: 1;
}

.sdb-05__link:focus-visible,
.sdb-05__collapse:focus-visible {
  outline: 2px solid var(--sdb-05-acc);
  outline-offset: 2px;
}

.sdb-05__label {
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
}

.sdb-05__app[data-sdb-05-state="collapsed"] .sdb-05__label {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sdb-05__app[data-sdb-05-state="collapsed"] .sdb-05__link {
  justify-content: center;
  gap: 0;
}

.sdb-05__main {
  flex: 1;
  min-inline-size: 0;
  padding: 1.5rem 1.25rem 2.5rem;
}

@media (min-width: 46rem) {
  .sdb-05__main {
    padding: 2.5rem 2.25rem 3rem;
  }
}

.sdb-05__eyebrow {
  margin: 0 0 0.3rem;
  font-size: 0.72rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--sdb-05-acc);
}

.sdb-05__title {
  margin: 0 0 0.25rem;
  font-family: var(--sdb-05-font-display);
  font-size: clamp(1.35rem, 3.4vw, 1.9rem);
  line-height: 1.15;
}

.sdb-05__meta {
  margin: 0 0 1.2rem;
  font-size: 0.85rem;
  color: var(--sdb-05-mut);
}

.sdb-05__tracks {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 1px;
  background: var(--sdb-05-line);
  border-radius: 0.7rem;
  overflow: hidden;
  max-inline-size: 34rem;
}

.sdb-05__tracks li {
  display: flex;
  align-items: center;
  gap: 0.7rem;
  padding: 0.6rem 0.85rem;
  background: var(--sdb-05-surf);
  font-size: 0.9rem;
  min-inline-size: 0;
}

.sdb-05__tracks span {
  color: var(--sdb-05-mut);
  font-variant-numeric: tabular-nums;
  font-size: 0.8rem;
}

.sdb-05__tracks em {
  margin-inline-start: auto;
  font-style: normal;
  color: var(--sdb-05-mut);
  font-size: 0.82rem;
  font-variant-numeric: tabular-nums;
}

@media (max-width: 30rem) {
  .sdb-05__app {
    flex-direction: column;
  }

  .sdb-05__rail,
    .sdb-05__app[data-sdb-05-state="collapsed"] .sdb-05__rail {
    inline-size: 100%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sdb-05__rail {
    transition: none;
  }

  .sdb-05__collapse svg {
    transition: none;
  }
}
/* The theme toggle is pinned top-right of the demo root, and on narrow
   viewports the rail head reaches under it — the toggle then intercepts
   every click meant for the collapse button. Reserve the toggle its own
   lane. Must sit at the END of the block: the base rail-head rule has
   equal specificity and would otherwise win on source order. */

@media (max-width: 30rem) {
  .sdb-05__rail-head,
    .sdb-05__head {
    padding-inline-end: 3.4rem;
  }
}
```

## JavaScript
```js
const root = document.querySelector('.sdb-05');
const app = root.querySelector('.sdb-05__app');
const btn = root.querySelector('#sdb-05-toggle');
function toggle() {
  const next = btn.getAttribute('aria-expanded') !== 'true';
  btn.setAttribute('aria-expanded', String(next));
  app.setAttribute('data-sdb-05-state', next ? 'expanded' : 'collapsed');
  btn.querySelector('.sdb-05__sr').textContent = next ? 'Collapse sidebar' : 'Expand sidebar';
}
btn.addEventListener('click', toggle);
root.__sdbCleanup = () => { btn.removeEventListener('click', toggle); };
```
