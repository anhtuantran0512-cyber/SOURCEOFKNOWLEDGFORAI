---
source: "codefronts"
url: "https://codefronts.com/layouts/css-dashboard-layouts/dark-mode-native-css-variable-dashboard/"
title: "Dark Mode Native CSS Variable Dashboard"
section: "layouts"
category: "css-dashboard-layouts"
category_name: "CSS Dashboard Layouts"
description: "A dashboard where dark mode is a data change, not a redesign: every component reads semantic tokens (--bg, --card, --ink, --accent), the root swaps one token…"
has_js: "false"
---

Here's a working CSS Dashboard Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark Mode Native CSS Variable Dashboard
Source: https://codefronts.com/layouts/css-dashboard-layouts/dark-mode-native-css-variable-dashboard/

A dashboard where dark mode is a data change, not a redesign: every component reads semantic tokens (--bg, --card, --ink, --accent), the root swaps one token set for another when :has() sees the toggle checked, and the live token strip at the bottom shows the swatches flipping in real time. color-scheme keeps native checkboxes and scrollbars in sync. Flip the switch — the entire theme is 10 lines of CSS, and no component file ever mentions a color twice.
## HTML
```html
<section class="cdl-10" aria-label="Dark mode token dashboard demo">
  <div class="cdl-10__app">
    <header class="cdl-10__bar">
      <strong><span class="cdl-10__logo" aria-hidden="true"></span>Nightshift</strong>
      <label class="cdl-10__switch">
        <input type="checkbox" id="cdl10-t" role="switch">
        <span class="cdl-10__track" aria-hidden="true"><i class="cdl-10__sun"></i><i class="cdl-10__moon"></i><b class="cdl-10__thumb"></b></span>
        <span class="cdl-10__swlabel">Dark mode</span>
      </label>
    </header>
    <div class="cdl-10__grid">
      <article class="cdl-10__card"><h3>Sessions</h3><p>24,981</p><small>▲ 6.1% this week</small></article>
      <article class="cdl-10__card"><h3>Bounce rate</h3><p>31.4%</p><small>▼ 1.2 pts this week</small></article>
      <article class="cdl-10__card"><h3>Avg. duration</h3><p>4m 12s</p><small>▲ 18s this week</small></article>
      <article class="cdl-10__card cdl-10__chartcard"><h3>Traffic by hour</h3><div class="cdl-10__chart" aria-hidden="true"><i style="--h:30%"></i><i style="--h:44%"></i><i style="--h:38%"></i><i style="--h:58%"></i><i style="--h:50%"></i><i style="--h:72%"></i><i style="--h:64%"></i><i style="--h:86%"></i><i style="--h:76%"></i><i style="--h:94%"></i><i style="--h:68%"></i><i style="--h:52%"></i></div></article>
      <article class="cdl-10__card cdl-10__notes"><h3>Release notes</h3><p class="cdl-10__body">Theme tokens now cover charts, borders and native controls. Scrollbars follow <code>color-scheme</code> automatically.</p><a class="cdl-10__link" href="#changelog">View changelog →</a></article>
    </div>
    <footer class="cdl-10__tokens" aria-label="Live token values">
      <span><i class="cdl-10__sw cdl-10__sw1" aria-hidden="true"></i>--bg</span>
      <span><i class="cdl-10__sw cdl-10__sw2" aria-hidden="true"></i>--card</span>
      <span><i class="cdl-10__sw cdl-10__sw3" aria-hidden="true"></i>--ink</span>
      <span><i class="cdl-10__sw cdl-10__sw4" aria-hidden="true"></i>--accent</span>
      <em>one checkbox re-themes everything above</em>
    </footer>
  </div>
</section>
```
## CSS
```css
.cdl-10,
.cdl-10 *,
.cdl-10 *::before,
.cdl-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cdl-10__app {
  width: 100%;
  height: 100vh;
  --bg: oklch(0.975 0.005 260);
  --card: oklch(1 0 0);
  --ink: oklch(0.25 0.02 260);
  --mut: oklch(0.54 0.02 260);
  --edge: oklch(0.9 0.01 260);
  --accent: oklch(0.55 0.18 265);
  --shadow: 0 18px 40px -26px oklch(0.4 0.05 260 / .45);
  color-scheme: light;
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  border: 1px solid var(--edge);
  background: var(--bg);
  padding: 16px;
  display: grid;
  gap: 14px;
  transition: background .35s,border-color .35s;
}

.cdl-10__app:has(#cdl10-t:checked) {
  --bg: oklch(0.17 0.02 260);
  --card: oklch(0.22 0.025 260);
  --ink: oklch(0.93 0.01 260);
  --mut: oklch(0.65 0.02 260);
  --edge: oklch(0.32 0.02 260);
  --accent: oklch(0.72 0.16 265);
  --shadow: 0 18px 40px -22px oklch(0 0 0 / .8);
  color-scheme: dark;
}

.cdl-10__bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
}

.cdl-10__bar strong {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 15px;
}

.cdl-10__logo {
  width: 20px;
  height: 20px;
  border-radius: 7px;
  background: conic-gradient(from 200deg,var(--accent),oklch(0.7 0.13 320));
}

.cdl-10__switch {
  display: flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
}

.cdl-10__switch input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.cdl-10__swlabel {
  font-size: 12.5px;
  font-weight: 600;
  color: var(--mut);
}

.cdl-10__track {
  position: relative;
  width: 58px;
  height: 30px;
  border-radius: 999px;
  background: color-mix(in oklch,var(--accent) 14%,var(--card));
  border: 1px solid var(--edge);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 8px;
  transition: background .35s,border-color .35s;
}

.cdl-10__sun,
.cdl-10__moon {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  z-index: 0;
}

.cdl-10__sun {
  background: radial-gradient(circle,oklch(0.8 0.15 85) 40%,transparent 41%),repeating-conic-gradient(oklch(0.8 0.15 85) 0 8deg,transparent 8deg 45deg);
}

.cdl-10__moon {
  background: radial-gradient(circle at 65% 35%,transparent 42%,oklch(0.75 0.05 280) 43%);
}

.cdl-10__thumb {
  position: absolute;
  left: 3px;
  top: 3px;
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: var(--card);
  border: 1px solid var(--edge);
  box-shadow: 0 2px 6px oklch(0 0 0 / .25);
  transition: translate .3s cubic-bezier(.2,.7,.2,1);
}

.cdl-10__app:has(#cdl10-t:checked) .cdl-10__thumb {
  translate: 28px 0;
}

.cdl-10__switch:has(:focus-visible) .cdl-10__track {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.cdl-10__grid {
  display: grid;
  gap: 12px;
  grid-template-columns: repeat(auto-fit,minmax(min(180px,100%),1fr));
}

.cdl-10__card {
  background: var(--card);
  border: 1px solid var(--edge);
  border-radius: 14px;
  padding: 15px 17px;
  box-shadow: var(--shadow);
  transition: background .35s,border-color .35s,color .35s;
}

.cdl-10__card h3 {
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .11em;
  text-transform: uppercase;
  color: var(--mut);
  transition: color .35s;
}

.cdl-10__card p {
  font-size: 22px;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
  letter-spacing: -.01em;
  margin: 5px 0 2px;
}

.cdl-10__card small {
  font-size: 11px;
  font-weight: 600;
  color: oklch(0.55 0.13 155);
}

.cdl-10__chartcard {
  grid-column: 1/-1;
}

.cdl-10__chart {
  display: flex;
  align-items: flex-end;
  gap: 7px;
  height: 88px;
  margin-top: 12px;
}

.cdl-10__chart i {
  flex: 1;
  height: var(--h);
  border-radius: 4px 4px 0 0;
  background: linear-gradient(to top,color-mix(in oklch,var(--accent) 25%,transparent),var(--accent));
  transition: background .35s;
}

.cdl-10__notes {
  grid-column: 1/-1;
  display: grid;
  gap: 6px;
}

.cdl-10__body {
  font-size: 13px !important;
  font-weight: 400 !important;
  line-height: 1.55;
  color: var(--mut);
  letter-spacing: 0 !important;
}

.cdl-10__body code {
  font: 600 11.5px ui-monospace,Menlo,Consolas,monospace;
  background: var(--bg);
  border: 1px solid var(--edge);
  border-radius: 5px;
  padding: 1px 5px;
}

.cdl-10__link {
  font-size: 12.5px;
  font-weight: 700;
  color: var(--accent);
  text-decoration: none;
  justify-self: start;
}

.cdl-10__link:hover {
  text-decoration: underline;
  text-underline-offset: 3px;
}

.cdl-10__link:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
  border-radius: 2px;
}

.cdl-10__tokens {
  display: flex;
  align-items: center;
  gap: 16px;
  flex-wrap: wrap;
  font: 600 11px ui-monospace,Menlo,Consolas,monospace;
  color: var(--mut);
  border-top: 1px dashed var(--edge);
  padding-top: 13px;
}

.cdl-10__tokens span {
  display: flex;
  align-items: center;
  gap: 7px;
}

.cdl-10__tokens em {
  margin-left: auto;
  font: italic 11px 'Segoe UI',system-ui,sans-serif;
}

.cdl-10__sw {
  width: 14px;
  height: 14px;
  border-radius: 4px;
  border: 1px solid var(--edge);
  transition: background .35s;
}

.cdl-10__sw1 {
  background: var(--bg);
}

.cdl-10__sw2 {
  background: var(--card);
}

.cdl-10__sw3 {
  background: var(--ink);
}

.cdl-10__sw4 {
  background: var(--accent);
}

@media (prefers-reduced-motion: reduce) {
  .cdl-10 * {
    transition-duration: .01s !important;
  }
}
```
