---
source: "codefronts"
url: "https://codefronts.com/layouts/css-dashboard-layouts/mobile-responsive-off-canvas-drawer-dashboard/"
title: "Mobile-Responsive Off-Canvas Drawer Dashboard"
section: "layouts"
category: "css-dashboard-layouts"
category_name: "CSS Dashboard Layouts"
description: "One markup, two behaviors, shown side by side: the same dashboard component rendered in a desktop panel (sidebar in-flow) and a phone frame (sidebar…"
has_js: "true"
---

Here's a working CSS Dashboard Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Mobile-Responsive Off-Canvas Drawer Dashboard
Source: https://codefronts.com/layouts/css-dashboard-layouts/mobile-responsive-off-canvas-drawer-dashboard/

One markup, two behaviors, shown side by side: the same dashboard component rendered in a desktop panel (sidebar in-flow) and a phone frame (sidebar off-canvas behind a hamburger). A container query — not a media query — decides which mode applies, so the component responds to the panel it lives in. The drawer slides on translate, dims behind a click-to-close backdrop, and closes on Esc; 10 lines of JS run the button because a drawer is a disclosure widget and needs aria-expanded.
## HTML
```html
<section class="cdl-07" aria-label="Off-canvas drawer demo — same component at two container widths">
  <div class="cdl-07__duo">
    <figure class="cdl-07__device cdl-07__device--desktop">
      <figcaption>Container ≥ 560px → sidebar in-flow</figcaption>
      <div class="cdl-07__app">
        <div class="cdl-07__veil" aria-hidden="true"></div>
        <nav class="cdl-07__side" id="cdl07-nav-a" aria-label="Primary">
          <strong><span class="cdl-07__logo" aria-hidden="true"></span>Fieldkit</strong>
          <a href="#home" aria-current="page" class="cdl-07__on">Home</a><a href="#jobs">Jobs</a><a href="#crew">Crew</a><a href="#invoices">Invoices</a><a href="#settings">Settings</a>
        </nav>
        <div class="cdl-07__main">
          <header class="cdl-07__bar">
            <button class="cdl-07__burger" type="button" aria-expanded="false" aria-controls="cdl07-nav-a" aria-label="Open navigation"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 6h16M4 12h16M4 18h16"/></svg></button>
            <h2>Today's jobs</h2><span class="cdl-07__count">6</span>
          </header>
          <div class="cdl-07__cards">
            <article><b>Deck repair — Hartley</b><span>08:30 · Crew A</span><i class="cdl-07__st cdl-07__go">On site</i></article>
            <article><b>Gutter install — Novak</b><span>10:00 · Crew B</span><i class="cdl-07__st">Scheduled</i></article>
            <article><b>Fence quote — Ellis</b><span>13:30 · Sam</span><i class="cdl-07__st">Scheduled</i></article>
            <article><b>Roof check — Winter Rd</b><span>15:00 · Crew A</span><i class="cdl-07__st cdl-07__hold">Weather hold</i></article>
          </div>
        </div>
      </div>
    </figure>
    <figure class="cdl-07__device cdl-07__device--phone">
      <figcaption>Container &lt; 560px → off-canvas drawer</figcaption>
      <div class="cdl-07__app">
        <div class="cdl-07__veil" aria-hidden="true"></div>
        <nav class="cdl-07__side" id="cdl07-nav-b" aria-label="Primary">
          <strong><span class="cdl-07__logo" aria-hidden="true"></span>Fieldkit</strong>
          <a href="#home" aria-current="page" class="cdl-07__on">Home</a><a href="#jobs">Jobs</a><a href="#crew">Crew</a><a href="#invoices">Invoices</a><a href="#settings">Settings</a>
        </nav>
        <div class="cdl-07__main">
          <header class="cdl-07__bar">
            <button class="cdl-07__burger" type="button" aria-expanded="false" aria-controls="cdl07-nav-b" aria-label="Open navigation"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 6h16M4 12h16M4 18h16"/></svg></button>
            <h2>Today's jobs</h2><span class="cdl-07__count">6</span>
          </header>
          <div class="cdl-07__cards">
            <article><b>Deck repair — Hartley</b><span>08:30 · Crew A</span><i class="cdl-07__st cdl-07__go">On site</i></article>
            <article><b>Gutter install — Novak</b><span>10:00 · Crew B</span><i class="cdl-07__st">Scheduled</i></article>
            <article><b>Fence quote — Ellis</b><span>13:30 · Sam</span><i class="cdl-07__st">Scheduled</i></article>
          </div>
        </div>
      </div>
    </figure>
  </div>
</section>
```
## CSS
```css
.cdl-07,
.cdl-07 *,
.cdl-07 *::before,
.cdl-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cdl-07 {
  background: var(--bg);
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
  --bg: oklch(0.975 0.006 145);
  --panel: oklch(1 0 0);
  --edge: oklch(0.9 0.015 145);
  --ink: oklch(0.27 0.02 155);
  --mut: oklch(0.53 0.03 155);
  --acc: oklch(0.55 0.14 160);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cdl-07__duo {
  width: 100%;
  height: 100vh;
  display: flex;
  gap: 22px;
  align-items: flex-start;
  flex-wrap: wrap;
}

.cdl-07__device {
  flex: 1 1 380px;
  min-width: 0;
  display: grid;
  gap: 10px;
}

.cdl-07__device--phone {
  flex: 0 0 300px;
}

.cdl-07__device figcaption {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .09em;
  text-transform: uppercase;
  color: var(--mut);
}

.cdl-07__app {
  container-type: inline-size;
  position: relative;
  overflow: hidden;
  height: 440px;
  display: flex;
  border-radius: 18px;
  border: 1px solid var(--edge);
  background: var(--bg);
  box-shadow: 0 20px 44px -28px oklch(0.35 0.05 155 / .4);
}

.cdl-07__side {
  flex: 0 0 220px;
  display: flex;
  flex-direction: column;
  gap: 4px;
  padding: 16px 12px;
  background: oklch(0.24 0.04 165);
  color: oklch(0.95 0.01 165);
}

.cdl-07__side strong {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 14.5px;
  padding: 0 10px;
  margin-bottom: 14px;
}

.cdl-07__logo {
  width: 18px;
  height: 18px;
  border-radius: 6px;
  background: conic-gradient(from 210deg,oklch(0.75 0.15 160),oklch(0.85 0.14 110));
}

.cdl-07__side a {
  display: flex;
  align-items: center;
  min-height: 44px;
  padding: 0 12px;
  border-radius: 10px;
  text-decoration: none;
  font-size: 13.5px;
  font-weight: 600;
  color: oklch(0.78 0.03 165);
  transition: background .15s,color .15s;
}

.cdl-07__side a:hover {
  background: oklch(0.3 0.04 165);
  color: oklch(0.97 0 0);
}

.cdl-07__side a:focus-visible {
  outline: 2px solid oklch(0.8 0.14 160);
  outline-offset: -2px;
}

.cdl-07__side a.cdl-07__on {
  background: oklch(0.33 0.05 165);
  color: oklch(0.98 0 0);
  box-shadow: inset 3px 0 0 oklch(0.75 0.15 160);
}

.cdl-07__main {
  flex: 1;
  min-width: 0;
  display: flex;
  flex-direction: column;
}

.cdl-07__bar {
  display: flex;
  align-items: center;
  gap: 12px;
  height: 54px;
  padding: 0 16px;
  background: var(--panel);
  border-bottom: 1px solid var(--edge);
}

.cdl-07__bar h2 {
  font-size: 15px;
  letter-spacing: -.01em;
}

.cdl-07__count {
  font-size: 11px;
  font-weight: 700;
  color: var(--acc);
  background: color-mix(in oklch,var(--acc) 12%,transparent);
  border-radius: 999px;
  padding: 3px 9px;
}

.cdl-07__burger {
  display: none;
  place-items: center;
  width: 40px;
  height: 40px;
  border: none;
  border-radius: 10px;
  background: transparent;
  color: var(--ink);
  cursor: pointer;
}

.cdl-07__burger:hover {
  background: oklch(0.94 0.01 145);
}

.cdl-07__burger:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.cdl-07__cards {
  padding: 14px;
  display: grid;
  gap: 10px;
  overflow-y: auto;
  overscroll-behavior: contain;
  min-height: 0;
}

.cdl-07__cards article {
  display: grid;
  grid-template-columns: minmax(0,1fr) auto;
  gap: 2px 10px;
  align-items: center;
  background: var(--panel);
  border: 1px solid var(--edge);
  border-radius: 12px;
  padding: 13px 15px;
}

.cdl-07__cards b {
  font-size: 13.5px;
}

.cdl-07__cards span {
  font-size: 11.5px;
  color: var(--mut);
  grid-column: 1;
}

.cdl-07__st {
  grid-row: 1/3;
  grid-column: 2;
  font-style: normal;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .04em;
  color: var(--mut);
  border: 1px solid var(--edge);
  border-radius: 999px;
  padding: 4px 10px;
  background: var(--bg);
}

.cdl-07__go {
  color: var(--acc);
  border-color: color-mix(in oklch,var(--acc) 40%,transparent);
  background: color-mix(in oklch,var(--acc) 10%,white);
}

.cdl-07__hold {
  color: oklch(0.55 0.13 70);
  border-color: oklch(0.8 0.1 80);
  background: oklch(0.97 0.03 90);
}

.cdl-07__veil {
  position: absolute;
  inset: 0;
  z-index: 1;
  background: oklch(0.2 0.03 165 / .45);
  backdrop-filter: blur(2px);
  opacity: 0;
  visibility: hidden;
  transition: opacity .3s ease,visibility 0s linear .3s;
}

[data-open] .cdl-07__veil {
  opacity: 1;
  visibility: visible;
  transition-delay: 0s,0s;
}

@container (max-width: 560px) {
  .cdl-07__burger {
    display: grid;
  }

  .cdl-07__side {
    position: absolute;
    inset: 0 auto 0 0;
    width: min(78%,300px);
    translate: -105% 0;
    transition: translate .32s cubic-bezier(.2,.7,.2,1);
    box-shadow: 0 0 60px oklch(0 0 0 / .35);
    z-index: 2;
  }

  [data-open] .cdl-07__side {
    translate: 0 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cdl-07 * {
    transition-duration: .01s !important;
  }
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.cdl-07__app').forEach(function (app) {
    if (app.dataset.bound) return; app.dataset.bound = '1';
    var btn = app.querySelector('.cdl-07__burger');
    var veil = app.querySelector('.cdl-07__veil');
    function set(open) {
      app.toggleAttribute('data-open', open);
      btn.setAttribute('aria-expanded', String(open));
      // production: also toggle inert on the nav + move focus in/out here
    }
    btn.addEventListener('click', function () { set(!app.hasAttribute('data-open')); });
    veil.addEventListener('click', function () { set(false); });
    app.addEventListener('keydown', function (e) { if (e.key === 'Escape') set(false); });
  });
})();
```
