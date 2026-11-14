---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sidebar-layouts/floating-sidebar/"
title: "Modern Floating Glassmorphism Sidebar UI Component"
section: "layouts"
category: "css-sidebar-layouts"
category_name: "CSS Sidebar Layouts"
description: "The elevated dashboard rail: detached from the viewport edges, floating on a 16px inset with soft depth shadows, frosted with backdrop-filter so the app's…"
has_js: "false"
---

Here's a working CSS Sidebar Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Modern Floating Glassmorphism Sidebar UI Component
Source: https://codefronts.com/layouts/css-sidebar-layouts/floating-sidebar/

The elevated dashboard rail: detached from the viewport edges, floating on a 16px inset with soft depth shadows, frosted with backdrop-filter so the app's ambient color bleeds through, and finished with the gradient hairline border that makes glass read as glass instead of gray plastic.
## HTML
```html
<section class="sbl-16">
  <aside class="sbl-16__glass" aria-label="Main">
    <div class="sbl-16__brand"><span aria-hidden="true"></span>Prism</div>
    <nav class="sbl-16__nav">
      <a href="#" aria-current="page"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="7.5" height="7.5" rx="1.5"/><rect x="13.5" y="3" width="7.5" height="7.5" rx="1.5"/><rect x="3" y="13.5" width="7.5" height="7.5" rx="1.5"/><rect x="13.5" y="13.5" width="7.5" height="7.5" rx="1.5"/></svg>Overview</a>
      <a href="#"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M21 12a9 9 0 1 1-9-9"/><path d="M12 3a9 9 0 0 1 9 9h-9z"/></svg>Reports</a>
      <a href="#"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="9" cy="8" r="3.5"/><path d="M3 20c0-3.3 2.7-5.5 6-5.5s6 2.2 6 5.5m1-13.5a3.5 3.5 0 0 1 0 7"/></svg>Audience</a>
      <a href="#"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="3"/><path d="M12 2v3m0 14v3M2 12h3m14 0h3M4.9 4.9l2.1 2.1m10 10 2.1 2.1m0-14.2-2.1 2.1m-10 10-2.1 2.1"/></svg>Settings</a>
    </nav>
    <div class="sbl-16__cta"><strong>Prism Pro</strong><small>Unlock cohort analysis</small><button type="button">Upgrade</button></div>
  </aside>
  <main class="sbl-16__main"><h1>Overview</h1><p>The rail floats on a 16px inset — frosted, gradient-edged, shadow-lifted. The aurora behind it is what the backdrop-filter is sampling.</p></main>
</section>
```
## CSS
```css
.sbl-16,
.sbl-16 *,
.sbl-16 *::before,
.sbl-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sbl-16 {
  --ink: oklch(0.96 0.005 280);
  --mut: oklch(0.78 0.02 280);
  --accent: oklch(0.75 0.14 200);
  display: grid;
  grid-template-columns: auto 1fr;
  height: 100vh;
  height: 100dvh;
  font-family: system-ui,'Segoe UI',sans-serif;
  color: var(--ink);
  background: radial-gradient(55% 65% at 18% 22%,oklch(0.45 0.16 300 / .65),transparent 60%),radial-gradient(50% 60% at 85% 75%,oklch(0.5 0.15 220 / .55),transparent 65%),radial-gradient(40% 50% at 65% 15%,oklch(0.55 0.12 170 / .35),transparent 60%),oklch(0.16 0.025 280);
}

.sbl-16__glass {
  width: 248px;
  margin: 16px;
  display: flex;
  flex-direction: column;
  gap: 4px;
  padding: 20px 14px;
  border-radius: 20px;
  border: 1px solid transparent;
  background: linear-gradient(rgba(255,255,255,.07),rgba(255,255,255,.07)) padding-box,linear-gradient(160deg,rgba(255,255,255,.5),rgba(255,255,255,.12) 40%,rgba(255,255,255,.03)) border-box;
  -webkit-backdrop-filter: blur(18px) saturate(1.5);
  backdrop-filter: blur(18px) saturate(1.5);
  box-shadow: 0 8px 32px oklch(0 0 0 / .3),0 2px 8px oklch(0 0 0 / .2);
}

.sbl-16__brand {
  display: flex;
  align-items: center;
  gap: 10px;
  font: 700 16px/1 system-ui,sans-serif;
  padding: 4px 10px 18px;
}

.sbl-16__brand span {
  width: 26px;
  height: 26px;
  border-radius: 8px;
  background: conic-gradient(from 200deg,oklch(0.75 0.14 200),oklch(0.65 0.17 300),oklch(0.75 0.14 200));
}

.sbl-16__nav {
  display: flex;
  flex-direction: column;
  gap: 3px;
}

.sbl-16__nav a {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 11px 12px;
  border-radius: 12px;
  font: 500 14px/1 system-ui,sans-serif;
  color: var(--mut);
  text-decoration: none;
  transition: background-color .2s ease,color .2s ease;
}

.sbl-16__nav svg {
  width: 18px;
  height: 18px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.8;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.sbl-16__nav a:hover {
  color: var(--ink);
  background: rgba(255,255,255,.09);
}

.sbl-16__nav a[aria-current="page"] {
  color: var(--ink);
  background: rgba(255,255,255,.14);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.15);
}

.sbl-16__nav a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.sbl-16__cta {
  margin-top: auto;
  display: grid;
  gap: 6px;
  padding: 14px;
  border-radius: 14px;
  background: rgba(255,255,255,.08);
  border: 1px solid rgba(255,255,255,.14);
}

.sbl-16__cta strong {
  font: 650 13.5px/1 system-ui,sans-serif;
}

.sbl-16__cta small {
  font: 400 11.5px/1.4 system-ui,sans-serif;
  color: var(--mut);
}

.sbl-16__cta button {
  margin-top: 4px;
  padding: 9px;
  border: none;
  border-radius: 9px;
  background: var(--accent);
  color: oklch(0.18 0.03 220);
  font: 700 12.5px/1 system-ui,sans-serif;
  cursor: pointer;
  transition: filter .2s ease;
}

.sbl-16__cta button:hover {
  filter: brightness(1.08);
}

.sbl-16__cta button:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
}

.sbl-16__main {
  padding: 36px 32px;
  overflow-y: auto;
}

.sbl-16__main h1 {
  font: 600 22px/1.2 system-ui,sans-serif;
  margin-bottom: 10px;
}

.sbl-16__main p {
  color: var(--mut);
  font-size: 14px;
  line-height: 1.65;
  max-width: 48ch;
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .sbl-16__nav a,
    .sbl-16__cta button {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — an inset, radius-20 rail with backdrop-filter frost and a padding-box/border-box gradient hairline that fades like lit glass. */
```
