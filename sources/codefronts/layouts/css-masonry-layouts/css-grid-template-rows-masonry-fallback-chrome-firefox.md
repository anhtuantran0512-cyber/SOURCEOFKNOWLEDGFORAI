---
source: "codefronts"
url: "https://codefronts.com/layouts/css-masonry-layouts/css-grid-template-rows-masonry-fallback-chrome-firefox/"
title: "CSS Grid Template Rows Masonry Fallback Chrome Firefox"
section: "layouts"
category: "css-masonry-layouts"
category_name: "CSS Masonry Layouts"
description: "The spec-watch demo: one wall of numbered tiles, three layout engines layered by @supports — CSS columns as the universal base, grid-template-rows: masonry…"
has_js: "false"
---

Here's a working CSS Masonry Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Grid Template Rows Masonry Fallback Chrome Firefox
Source: https://codefronts.com/layouts/css-masonry-layouts/css-grid-template-rows-masonry-fallback-chrome-firefox/

The spec-watch demo: one wall of numbered tiles, three layout engines layered by @supports — CSS columns as the universal base, grid-template-rows: masonry where the Firefox-lineage syntax runs, display: masonry where the newer proposal runs. A live status panel tells you which engine YOUR browser chose (pure CSS feature detection — the badges flip inside the same @supports blocks), and the numbered tiles make the item-order difference between engines visible instead of theoretical.
## HTML
```html
<section class="msn-12" aria-label="Native CSS masonry with fallback demo">
  <div class="msn-12__stage" tabindex="0">
    <header class="msn-12__head">
      <div><h2>Engine check</h2><p>One wall · three layout engines · zero broken browsers</p></div>
    </header>
    <div class="msn-12__panel" role="status">
      <div class="msn-12__badge msn-12__badge--cols"><strong>CSS columns</strong><span></span></div>
      <div class="msn-12__badge msn-12__badge--gtr"><strong>grid-template-rows: masonry</strong><span></span></div>
      <div class="msn-12__badge msn-12__badge--disp"><strong>display: masonry</strong><span></span></div>
    </div>
    <div class="msn-12__wall">
      <article class="msn-12__tile" style="--h:1;--a:oklch(0.7 0.12 300);--b:oklch(0.48 0.14 330)"><b>01</b><h3>Watch the numbers</h3><p>Columns snake them down each lane; native masonry marches them left-to-right into the shortest track.</p></article>
      <article class="msn-12__tile" style="--h:0;--a:oklch(0.75 0.1 200);--b:oklch(0.5 0.12 230)"><b>02</b><h3>Base layer</h3><p>Multicol serves everyone.</p></article>
      <article class="msn-12__tile" style="--h:2;--a:oklch(0.78 0.1 85);--b:oklch(0.55 0.13 60)"><b>03</b><h3>First upgrade</h3><p>grid-template-rows: masonry — the Firefox-lineage syntax, in Nightly behind layout.css.grid-template-masonry-value.enabled. Order-preserving packing, real grid tracks, subgrid-friendly.</p></article>
      <article class="msn-12__tile" style="--h:0;--a:oklch(0.72 0.11 150);--b:oklch(0.48 0.12 170)"><b>04</b><h3>Second upgrade</h3><p>display: masonry, per the newer proposal.</p></article>
      <article class="msn-12__tile" style="--h:1;--a:oklch(0.68 0.12 20);--b:oklch(0.45 0.13 0)"><b>05</b><h3>The reset rule</h3><p>When grid wins, margin-bottom must yield to gap — or Nightly double-spaces.</p></article>
      <article class="msn-12__tile" style="--h:2;--a:oklch(0.65 0.1 260);--b:oklch(0.42 0.11 280)"><b>06</b><h3>Why bother?</h3><p>Native masonry is the only engine that packs unknown heights AND keeps reading order — the thing demos 01 and 03 each give up half of. That's worth a three-line bet on the future.</p></article>
      <article class="msn-12__tile" style="--h:0;--a:oklch(0.8 0.08 330);--b:oklch(0.58 0.11 350)"><b>07</b><h3>Flags flip off</h3><p>Never ship the bet without the base.</p></article>
      <article class="msn-12__tile" style="--h:1;--a:oklch(0.74 0.09 110);--b:oklch(0.5 0.11 130)"><b>08</b><h3>@supports tests parsing</h3><p>Accepted syntax behind a disabled flag can style anyway — the cascade survives it.</p></article>
      <article class="msn-12__tile" style="--h:0;--a:oklch(0.7 0.1 240);--b:oklch(0.46 0.11 260)"><b>09</b><h3>Test it today</h3><p>Firefox Nightly or Chrome Canary.</p></article>
      <article class="msn-12__tile" style="--h:1;--a:oklch(0.76 0.11 45);--b:oklch(0.52 0.13 25)"><b>10</b><h3>Cleanup path</h3><p>When support crosses your floor, deleting the fallback is a six-line diff.</p></article>
      <article class="msn-12__tile" style="--h:0;--a:oklch(0.66 0.12 310);--b:oklch(0.44 0.13 290)"><b>11</b><h3>Shared core only</h3><p>Tracks + gap; skip proposal-specific extras.</p></article>
      <article class="msn-12__tile" style="--h:1;--a:oklch(0.72 0.1 180);--b:oklch(0.48 0.11 200)"><b>12</b><h3>The endgame</h3><p>One wall, one syntax, no JavaScript. We're one WG resolution away.</p></article>
    </div>
  </div>
</section>
```
## CSS
```css
.msn-12,
.msn-12 *,
.msn-12 *::before,
.msn-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.msn-12 {
  --bg: oklch(0.975 0.005 260);
  --card: oklch(0.995 0.002 260);
  --ink: oklch(0.23 0.015 270);
  --mut: oklch(0.53 0.015 270);
  --line: oklch(0.89 0.008 260);
  --acc: oklch(0.55 0.19 265);
  --on: oklch(0.55 0.15 155);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
  display: block;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: var(--bg);
}

.msn-12__stage {
  width: 100%;
  container: msn12/inline-size;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  background: var(--bg);
}

.msn-12__head {
  padding: 20px clamp(16px,3cqi,28px) 0;
}

.msn-12__head h2 {
  font-size: clamp(18px,2.6cqi,24px);
  letter-spacing: -.02em;
}

.msn-12__head p {
  font-size: 12.5px;
  color: var(--mut);
  margin-top: 3px;
}

.msn-12__panel {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  padding: 14px clamp(16px,3cqi,28px);
}

.msn-12__badge {
  display: grid;
  gap: 2px;
  padding: 10px 14px;
  border-radius: 11px;
  border: 1px solid var(--line);
  background: var(--card);
}

.msn-12__badge strong {
  font-size: 12px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  letter-spacing: -.01em;
}

.msn-12__badge span {
  font-size: 11px;
  font-weight: 700;
  color: var(--mut);
}

.msn-12__badge--cols span::after {
  content: "active — serving this browser";
  color: var(--on);
}

.msn-12__badge--gtr span::after {
  content: "not supported here";
}

.msn-12__badge--disp span::after {
  content: "not supported here";
}

.msn-12__wall {
  columns: 220px;
  column-gap: 12px;
  padding: 4px clamp(16px,3cqi,28px) clamp(18px,3cqi,30px);
}

.msn-12__tile {
  break-inside: avoid;
  margin-bottom: 12px;
  border-radius: 14px;
  border: 1px solid var(--line);
  background: var(--card);
  padding: 16px;
  display: grid;
  gap: 7px;
  position: relative;
  overflow: clip;
}

.msn-12__tile::before {
  content: "";
  position: absolute;
  inset: 0 0 auto 0;
  height: 4px;
  background: linear-gradient(90deg,var(--a),var(--b));
}

.msn-12__tile b {
  font-size: 12px;
  font-weight: 800;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  color: var(--acc);
}

.msn-12__tile h3 {
  font-size: 14.5px;
  letter-spacing: -.01em;
}

.msn-12__tile p {
  font-size: 12.5px;
  line-height: 1.55;
  color: var(--mut);
  text-wrap: pretty;
}

.msn-12__tile[style*="--h:1"] p {
  min-height: 3.2em;
}

.msn-12__tile[style*="--h:2"] p {
  min-height: 6.4em;
}

@supports (grid-template-rows: masonry) {
  .msn-12__wall {
    display: grid;
    grid-template-columns: repeat(auto-fill,minmax(min(220px,100%),1fr));
    grid-template-rows: masonry;
    gap: 12px;
  }

  .msn-12__tile {
    margin-bottom: 0;
  }

  .msn-12__badge--gtr span::after {
    content: "ACTIVE — packing this wall";
    color: var(--on);
  }

  .msn-12__badge--cols span::after {
    content: "standing by (fallback)";
    color: var(--mut);
  }
}

@supports (display: masonry) {
  .msn-12__wall {
    display: masonry;
  }

  .msn-12__badge--disp span::after {
    content: "ACTIVE — packing this wall";
    color: var(--on);
  }

  .msn-12__badge--gtr span::after {
    content: "standing by";
    color: var(--mut);
  }

  .msn-12__badge--cols span::after {
    content: "standing by (fallback)";
    color: var(--mut);
  }
}

@container msn12 (width < 480px) {
  .msn-12__wall {
    columns: 1;
  }

  .msn-12__panel {
    gap: 6px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .msn-12 * {
    transition-duration: .01ms !important;
  }
}
```
