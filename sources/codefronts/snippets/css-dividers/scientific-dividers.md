---
source: "codefronts"
url: "https://codefronts.com/snippets/css-dividers/scientific-dividers/"
title: "Data Dashboard Dotted Grid Divider CSS"
section: "snippets"
category: "css-dividers"
category_name: "CSS Dividers"
description: "Dashboards live and die by their rules."
has_js: "false"
---

Here's a working CSS Divider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Data Dashboard Dotted Grid Divider CSS
Source: https://codefronts.com/snippets/css-dividers/scientific-dividers/

Dashboards live and die by their rules. This demo shows the correct way to divide a responsive metric grid — not borders on every card (which double up and break at wrap points), but a gap filled by the container's own background, plus dotted rules drawn with radial-gradient so the dot pitch is exact rather than whatever the browser's dashed algorithm decides.
## HTML
```html
<section class="div-15" aria-label="Dashboard dotted grid divider demo">
  <div class="div-15__stage">
    <div class="div-15__panel">
      <header class="div-15__head">
        <h2 class="div-15__title">Traffic overview</h2>
        <span class="div-15__badge">Last 7 days</span>
      </header>
      <div class="div-15__dots" role="separator" aria-label="Section divider"></div>
      <div class="div-15__grid">
        <div class="div-15__cell"><p class="div-15__k">Sessions</p><p class="div-15__v">48,210</p><p class="div-15__d div-15__d--up">▲ 12.4%</p></div>
        <div class="div-15__cell"><p class="div-15__k">Bounce</p><p class="div-15__v">31.8%</p><p class="div-15__d div-15__d--down">▼ 2.1%</p></div>
        <div class="div-15__cell"><p class="div-15__k">Avg. time</p><p class="div-15__v">3m 04s</p><p class="div-15__d div-15__d--up">▲ 0.6%</p></div>
        <div class="div-15__cell"><p class="div-15__k">Signups</p><p class="div-15__v">1,942</p><p class="div-15__d div-15__d--up">▲ 8.9%</p></div>
      </div>
      <div class="div-15__dash" role="separator" aria-label="Section divider"></div>
      <ul class="div-15__rows">
        <li><span>/css-dividers</span><span>18,402</span></li>
        <li><span>/css-blockquotes</span><span>12,118</span></li>
        <li><span>/css-buttons</span><span>9,650</span></li>
      </ul>
    </div>
    <p class="div-15__chip">gap:1px grid rules · radial-gradient dot pitch · 3 rule weights</p>
  </div>
</section>
```
## CSS
```css
.div-15 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--div-15-bg);
  --div-15-bg: oklch(0.17 0.014 255);
  --div-15-card: oklch(0.22 0.016 255);
  --div-15-panel: oklch(0.2 0.015 255);
  --div-15-ink: oklch(0.95 0.008 250);
  --div-15-mut: oklch(0.64 0.018 252);
  --div-15-line: oklch(1 0 0/.11);
  --div-15-dot: oklch(1 0 0/.28);
  --div-15-acc: oklch(0.75 0.15 175);
  --div-15-warn: oklch(0.72 0.16 30);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--div-15-ink);
}

.div-15 *,
.div-15 *::before,
.div-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  list-style: none;
}

.div-15__stage {
  min-height: 100svh;
  display: grid;
  place-content: center;
  justify-items: center;
  gap: 20px;
  padding: clamp(24px,5vw,60px) clamp(18px,4vw,48px);
}

.div-15__panel {
  width: min(94vw,720px);
  background: var(--div-15-panel);
  border: 1px solid var(--div-15-line);
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 24px 60px oklch(0 0 0/.4);
}

.div-15__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
  padding: 18px 22px;
}

.div-15__title {
  font-size: 16px;
  font-weight: 650;
  letter-spacing: -.01em;
}

.div-15__badge {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--div-15-mut);
  border: 1px solid var(--div-15-line);
  border-radius: 99px;
  padding: 5px 11px;
}

.div-15__dots {
  height: 3px;
  background: radial-gradient(circle at 1.5px 50%,var(--div-15-dot) 1.5px,transparent 1.6px) 0 0/9px 3px repeat-x;
}

.div-15__dash {
  height: 1px;
  background: repeating-linear-gradient(90deg,var(--div-15-dot) 0 7px,transparent 7px 14px);
}

.div-15__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(150px,1fr));
  gap: 1px;
  background: var(--div-15-line);
}

.div-15__cell {
  background: var(--div-15-card);
  padding: 18px 20px 20px;
  display: grid;
  gap: 5px;
  transition: background .2s ease;
}

.div-15__cell:hover {
  background: color-mix(in oklch,var(--div-15-acc) 7%,var(--div-15-card));
}

.div-15__k {
  font-size: 11.5px;
  letter-spacing: .09em;
  text-transform: uppercase;
  color: var(--div-15-mut);
}

.div-15__v {
  font-size: clamp(21px,3.2vw,27px);
  font-weight: 680;
  letter-spacing: -.025em;
  font-variant-numeric: tabular-nums;
}

.div-15__d {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
}

.div-15__d--up {
  color: var(--div-15-acc);
}

.div-15__d--down {
  color: var(--div-15-warn);
}

.div-15__rows li {
  display: flex;
  justify-content: space-between;
  gap: 16px;
  padding: 13px 22px;
  font-size: 13.5px;
  color: var(--div-15-mut);
  font-variant-numeric: tabular-nums;
}

.div-15__rows li+li {
  border-top: 1px solid oklch(1 0 0/.06);
}

.div-15__rows li span:last-child {
  color: var(--div-15-ink);
  font-weight: 600;
}

.div-15__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--div-15-mut);
  padding: 8px 14px;
  border: 1px solid var(--div-15-line);
  border-radius: 99px;
  text-align: center;
  max-width: 94vw;
}

@media (prefers-reduced-motion: reduce) {
  .div-15 * {
    transition-duration: .01ms !important;
  }
}
```
