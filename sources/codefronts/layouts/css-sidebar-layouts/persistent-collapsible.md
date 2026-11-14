---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sidebar-layouts/persistent-collapsible/"
title: "Persistent Collapsible State Sidebar with CSS Variables"
section: "layouts"
category: "css-sidebar-layouts"
category_name: "CSS Sidebar Layouts"
description: "The collapse that survives a refresh: sidebar state lives in a data-state attribute, all geometry derives from one --sidebar-width variable that the…"
has_js: "true"
---

Here's a working CSS Sidebar Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Persistent Collapsible State Sidebar with CSS Variables
Source: https://codefronts.com/layouts/css-sidebar-layouts/persistent-collapsible/

The collapse that survives a refresh: sidebar state lives in a data-state attribute, all geometry derives from one --sidebar-width variable that the attribute swaps, and six lines of JavaScript persist the choice to localStorage — restored BEFORE first paint so returning users never see the wrong-width flash.
## HTML
```html
<section class="sbl-20" id="sbl20" data-state="expanded">
  <aside class="sbl-20__rail">
    <div class="sbl-20__brand"><span class="sbl-20__mark" aria-hidden="true"></span><span class="sbl-20__txt sbl-20__word">Keystone</span></div>
    <nav class="sbl-20__nav" aria-label="Main">
      <a href="#" aria-current="page"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="7.5" height="7.5" rx="1.5"/><rect x="13.5" y="3" width="7.5" height="7.5" rx="1.5"/><rect x="3" y="13.5" width="7.5" height="7.5" rx="1.5"/><rect x="13.5" y="13.5" width="7.5" height="7.5" rx="1.5"/></svg><span class="sbl-20__txt">Home</span></a>
      <a href="#"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20V10m6 10V4m6 16v-7"/></svg><span class="sbl-20__txt">Metrics</span></a>
      <a href="#"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span class="sbl-20__txt">Files</span></a>
      <a href="#"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="3"/><path d="M12 2v3m0 14v3M2 12h3m14 0h3M4.9 4.9l2.1 2.1m10 10 2.1 2.1m0-14.2-2.1 2.1m-10 10-2.1 2.1"/></svg><span class="sbl-20__txt">Settings</span></a>
    </nav>
    <button class="sbl-20__toggle" type="button" aria-expanded="true" aria-controls="sbl20"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="m14 6-6 6 6 6"/></svg><span class="sbl-20__txt">Collapse</span></button>
  </aside>
  <main class="sbl-20__main"><h1>Home</h1><p>Collapse the rail, then reload the page — the state restores from localStorage before first paint. No wrong-width flash.</p></main>
</section>
```
## CSS
```css
.sbl-20,
.sbl-20 *,
.sbl-20 *::before,
.sbl-20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sbl-20 {
  --sidebar-width: 264px;
  --panel: oklch(0.17 0.015 195);
  --ink: oklch(0.94 0.005 195);
  --mut: oklch(0.64 0.012 195);
  --line: oklch(0.28 0.016 195);
  --accent: oklch(0.78 0.13 185);
  display: grid;
  grid-template-columns: var(--sidebar-width) 1fr;
  height: 100vh;
  height: 100dvh;
  font-family: system-ui,'Segoe UI',sans-serif;
  background: oklch(0.13 0.012 195);
  color: var(--ink);
  transition: grid-template-columns .3s cubic-bezier(.4,0,.2,1);
}

.sbl-20[data-state="collapsed"] {
  --sidebar-width: 72px;
}

.sbl-20__rail {
  display: flex;
  flex-direction: column;
  gap: 2px;
  background: var(--panel);
  border-right: 1px solid var(--line);
  padding: 16px 12px;
  overflow: hidden;
}

.sbl-20__brand {
  display: grid;
  grid-template-columns: 26px 1fr;
  align-items: center;
  gap: 11px;
  padding: 4px 10px 18px;
  white-space: nowrap;
}

.sbl-20__mark {
  width: 26px;
  height: 26px;
  border-radius: 8px;
  background: conic-gradient(from 160deg,var(--accent),oklch(0.6 0.15 250));
}

.sbl-20__word {
  font: 700 15px/1 system-ui,sans-serif;
}

.sbl-20__nav {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.sbl-20__nav a,
.sbl-20__toggle {
  display: grid;
  grid-template-columns: 19px 1fr;
  align-items: center;
  gap: 12px;
  min-height: 44px;
  padding: 0 14px;
  border-radius: 10px;
  border: none;
  background: none;
  text-align: left;
  font: 500 14px/1 system-ui,sans-serif;
  color: var(--mut);
  text-decoration: none;
  cursor: pointer;
  white-space: nowrap;
  transition: background-color .2s ease,color .2s ease;
}

.sbl-20__nav svg,
.sbl-20__toggle svg {
  width: 19px;
  height: 19px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.8;
  stroke-linecap: round;
  stroke-linejoin: round;
  transition: rotate .3s ease;
}

.sbl-20__txt {
  opacity: 1;
  transition: opacity .18s ease .1s;
}

.sbl-20[data-state="collapsed"] .sbl-20__txt {
  opacity: 0;
  transition: opacity .15s ease;
}

.sbl-20[data-state="collapsed"] .sbl-20__toggle svg {
  rotate: 180deg;
}

.sbl-20__nav a:hover,
.sbl-20__toggle:hover {
  color: var(--ink);
  background: color-mix(in oklab,var(--ink) 7%,transparent);
}

.sbl-20__nav a[aria-current="page"] {
  color: var(--accent);
  background: color-mix(in oklab,var(--accent) 14%,transparent);
}

.sbl-20__nav a:focus-visible,
.sbl-20__toggle:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.sbl-20__toggle {
  margin-top: auto;
}

.sbl-20__main {
  padding: 32px;
  overflow-y: auto;
}

.sbl-20__main h1 {
  font: 600 22px/1.2 system-ui,sans-serif;
  margin-bottom: 10px;
}

.sbl-20__main p {
  color: var(--mut);
  font-size: 14px;
  line-height: 1.6;
  max-width: 47ch;
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .sbl-20,
    .sbl-20 .sbl-20__txt,
    .sbl-20 .sbl-20__toggle svg {
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  const KEY = 'sbl20-sidebar';
  const shell = document.getElementById('sbl20');
  const btn = shell?.querySelector('.sbl-20__toggle');
  if (!shell || !btn) return;
  // Restore before paint: in production, inline this expression in a <script> right after the shell's opening tag.
  let saved = null;
  try { saved = localStorage.getItem(KEY); } catch (e) {}
  if (saved === 'collapsed' || saved === 'expanded') apply(saved);
  btn.addEventListener('click', () => {
    apply(shell.dataset.state === 'expanded' ? 'collapsed' : 'expanded');
  });
  function apply(state) {
    shell.dataset.state = state;                       // CSS reads this
    btn.setAttribute('aria-expanded', state === 'expanded'); // AT reads this
    try { localStorage.setItem(KEY, state); } catch (e) {}   // tomorrow reads this
  }
})();
```
