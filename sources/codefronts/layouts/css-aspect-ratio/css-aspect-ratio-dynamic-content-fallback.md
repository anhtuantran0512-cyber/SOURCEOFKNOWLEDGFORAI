---
source: "codefronts"
url: "https://codefronts.com/layouts/css-aspect-ratio/css-aspect-ratio-dynamic-content-fallback/"
title: "CSS Aspect Ratio Dynamic Content Fallback"
section: "layouts"
category: "css-aspect-ratio"
category_name: "CSS Aspect Ratio Demos"
description: "What happens when the words don't fit the ratio?"
has_js: "false"
---

Here's a working CSS Aspect Ratio Demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Aspect Ratio Dynamic Content Fallback
Source: https://codefronts.com/layouts/css-aspect-ratio/css-aspect-ratio-dynamic-content-fallback/

What happens when the words don't fit the ratio? This demo makes the aspect-ratio contract legible: it's a preferred size, not a promise. Default tiles bend — content-based minimum sizing lets long CMS copy grow the box past 16:9 instead of spilling. Strict tiles (min-height: 0) hold the ratio and scroll inside. And aspect-ratio: auto 3/2 gives images a placeholder shape that yields to their intrinsic one on arrival. Flip the 'verbose CMS' switch and watch each policy respond.
## HTML
```html
<section class="car-09" aria-label="Aspect ratio dynamic content fallback demo">
  <div class="car-09__stage" id="car09-top">
    <header class="car-09__bar">
      <div>
        <h1>The ratio is a preference, not a promise</h1>
        <p>Three fallback policies for content nobody proofread. Flip the switch to simulate a chatty CMS.</p>
      </div>
      <label class="car-09__toggle" for="car09-verbose">
        <input type="checkbox" id="car09-verbose">
        <i aria-hidden="true"></i>
        <span>Verbose CMS content</span>
      </label>
    </header>
    <main class="car-09__grid">
      <article class="car-09__tile car-09__tile--bend">
        <header><b>A</b><h2>Default — the box bends</h2><code>aspect-ratio:16/9</code></header>
        <p>Short copy: this tile is exactly 16:9.<span class="car-09__extra"> But the moment an editor pastes a second paragraph — like this one — the automatic content-based minimum kicks in and the box grows taller than its ratio instead of clipping or overflowing. No CSS changed; the contract simply yielded to the content, which is exactly what the spec intends for unpredictable text.</span></p>
        <footer class="car-09__verdict car-09__verdict--ok">never clips · grows past 16:9 when needed</footer>
      </article>
      <article class="car-09__tile car-09__tile--strict">
        <header><b>B</b><h2>Strict — the ratio wins</h2><code>min-height:0; overflow:auto</code></header>
        <div class="car-09__scrollbox" tabindex="0">
          <p>This tile waives the content floor, so it stays 16:9 no matter what.<span class="car-09__extra"> Feed it a novel and it will not budge: the extra text you're reading right now scrolls inside the fixed box instead of growing it. Dashboards, bento grids and anything pixel-budgeted use this posture — the geometry is law and the scrollbar is the pressure valve.</span></p>
        </div>
        <footer class="car-09__verdict car-09__verdict--warn">holds 16:9 · excess scrolls inside</footer>
      </article>
      <article class="car-09__tile car-09__tile--auto">
        <header><b>C</b><h2>Replaced — auto 3/2</h2><code>aspect-ratio:auto 3/2</code></header>
        <figure class="car-09__autofig">
          <img src="https://images.unsplash.com/photo-1493246507139-91e8fad9978e?q=80&w=1200&auto=format&fit=crop" alt="Wide valley panorama — intrinsically wider than 3:2" loading="lazy">
          <figcaption>Placeholder shape 3:2 → intrinsic shape on load. The fallback ratio only governs the wait.</figcaption>
        </figure>
        <footer class="car-09__verdict car-09__verdict--info">3:2 while loading · truth after</footer>
      </article>
    </main>
    <section class="car-09__wall" aria-label="Testimonial wall using the default policy">
      <h2>The default policy, deployed: a testimonial wall</h2>
      <div class="car-09__quotes">
        <blockquote><p>“We put <code>aspect-ratio:16/9</code> on every quote card and stopped auditing lengths.”<span class="car-09__extra"> The long ones grow, the short ones hold the line, and the grid keeps its rhythm either way — this sentence only exists to prove it.”</span></p><cite>— Priya N., design systems lead</cite></blockquote>
        <blockquote><p>“Short quote. Perfect 16:9.”</p><cite>— Tom A., front-end engineer</cite></blockquote>
        <blockquote><p>“The box is a preference the content can veto.”<span class="car-09__extra"> Toggle the switch above and watch this card and its neighbors negotiate independently — each tile only grows as much as its own words demand.”</span></p><cite>— June P., CSS instructor</cite></blockquote>
        <blockquote><p>“Nothing clipped since migration.”</p><cite>— Marcus B., publisher</cite></blockquote>
      </div>
    </section>
    <footer class="car-09__foot">Rule of thumb: let marketing tiles bend, make dashboards strict, give feed media <code>auto &lt;ratio&gt;</code>. A demo from the CodeFronts aspect-ratio collection.</footer>
  </div>
</section>
```
## CSS
```css
.car-09,
.car-09 *,
.car-09 *::before,
.car-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.car-09 {
  --bg: oklch(0.975 0.008 95);
  --ink: oklch(0.24 0.02 80);
  --mut: oklch(0.5 0.02 80);
  --line: oklch(0.88 0.015 95);
  --acc: oklch(0.55 0.13 145);
  --warn: oklch(0.62 0.14 70);
  --info: oklch(0.56 0.13 240);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
  display: block;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: var(--bg);
}

.car-09__stage {
  width: 100%;
  container: car09/inline-size;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  background: var(--bg);
}

.car-09__bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 18px;
  flex-wrap: wrap;
  padding: 22px clamp(16px,4cqi,44px);
  border-bottom: 1px solid var(--line);
}

.car-09__bar h1 {
  font-size: clamp(18px,2.8cqi,26px);
  letter-spacing: -.02em;
  font-weight: 800;
}

.car-09__bar p {
  font-size: 13px;
  color: var(--mut);
  margin-top: 4px;
}

.car-09__toggle {
  display: flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
  font-size: 13.5px;
  font-weight: 700;
  min-height: 44px;
}

.car-09__toggle input {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.car-09__toggle i {
  width: 46px;
  height: 26px;
  border-radius: 99px;
  background: oklch(0.82 0.02 95);
  position: relative;
  transition: background .25s;
  flex: none;
}

.car-09__toggle i::after {
  content: "";
  position: absolute;
  left: 3px;
  top: 3px;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: oklch(0.99 0 0);
  box-shadow: 0 1px 4px oklch(0.3 0.02 80/.4);
  transition: translate .25s cubic-bezier(.34,1.56,.64,1);
}

.car-09__toggle input:checked + i {
  background: var(--acc);
}

.car-09__toggle input:checked + i::after {
  translate: 20px 0;
}

.car-09__toggle input:focus-visible + i {
  outline: 3px solid var(--acc);
  outline-offset: 2px;
}

.car-09__extra {
  display: none;
}

.car-09:has(#car09-verbose:checked) .car-09__extra {
  display: inline;
}

.car-09__grid {
  display: grid;
  gap: clamp(14px,2.5cqi,22px);
  grid-template-columns: repeat(auto-fit,minmax(min(290px,100%),1fr));
  align-items: start;
  padding: clamp(18px,3.5cqi,32px) clamp(16px,4cqi,44px);
}

.car-09__tile {
  display: flex;
  flex-direction: column;
  border: 1px solid var(--line);
  border-radius: 16px;
  background: oklch(1 0 0);
  box-shadow: 0 1px 3px oklch(0.3 0.02 80/.06);
}

.car-09__tile--bend,
.car-09__wall blockquote {
  aspect-ratio: 16/9;
}

.car-09__tile--strict {
  aspect-ratio: 16/9;
  min-height: 0;
}

.car-09__tile header {
  display: flex;
  align-items: center;
  gap: 9px;
  padding: 13px 16px 0;
  flex-wrap: wrap;
}

.car-09__tile header b {
  display: grid;
  place-items: center;
  width: 24px;
  height: 24px;
  border-radius: 8px;
  background: var(--ink);
  color: var(--bg);
  font-size: 12px;
  font-weight: 800;
  flex: none;
}

.car-09__tile h2 {
  font-size: 14.5px;
  font-weight: 800;
  letter-spacing: -.01em;
}

.car-09__tile header code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10.5px;
  color: var(--mut);
  margin-left: auto;
}

.car-09__tile > p,
.car-09__scrollbox p {
  padding: 10px 16px 12px;
  font-size: 13.5px;
  line-height: 1.6;
  color: var(--mut);
}

.car-09__scrollbox {
  flex: 1;
  min-height: 0;
  overflow: auto;
  scrollbar-width: thin;
}

.car-09__scrollbox:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
  border-radius: 8px;
}

.car-09__autofig {
  padding: 10px 16px 12px;
}

.car-09__autofig img {
  width: 100%;
  height: auto;
  aspect-ratio: auto 3/2;
  object-fit: cover;
  border-radius: 10px;
  background: linear-gradient(130deg,oklch(0.85 0.03 95),oklch(0.75 0.05 145));
}

.car-09__autofig figcaption {
  font-size: 11.5px;
  color: var(--mut);
  margin-top: 8px;
  line-height: 1.5;
}

.car-09__verdict {
  margin-top: auto;
  padding: 9px 16px;
  border-top: 1px dashed var(--line);
  font-family: ui-monospace,Menlo,monospace;
  font-size: 10.5px;
  letter-spacing: .02em;
}

.car-09__verdict--ok {
  color: var(--acc);
}

.car-09__verdict--warn {
  color: var(--warn);
}

.car-09__verdict--info {
  color: var(--info);
}

.car-09__wall {
  padding: 6px clamp(16px,4cqi,44px) 10px;
}

.car-09__wall h2 {
  font-size: clamp(16px,2.4cqi,21px);
  letter-spacing: -.015em;
  font-weight: 800;
  margin-bottom: 14px;
}

.car-09__quotes {
  display: grid;
  gap: 14px;
  grid-template-columns: repeat(auto-fit,minmax(min(240px,100%),1fr));
  align-items: start;
}

.car-09__wall blockquote {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 10px;
  padding: 16px;
  border: 1px solid var(--line);
  border-radius: 14px;
  background: linear-gradient(160deg,oklch(1 0 0),oklch(0.97 0.01 95));
}

.car-09__wall blockquote p {
  font-size: 13.5px;
  line-height: 1.55;
  text-wrap: pretty;
}

.car-09__wall code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .9em;
  background: oklch(0.93 0.015 95);
  padding: 1px 5px;
  border-radius: 4px;
}

.car-09__wall cite {
  font-style: normal;
  font-size: 11.5px;
  color: var(--mut);
}

.car-09__foot {
  padding: 18px clamp(16px,4cqi,44px) 32px;
  font-size: 12.5px;
  line-height: 1.7;
  color: var(--mut);
  border-top: 1px solid var(--line);
  margin-top: 16px;
}

.car-09__foot code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .9em;
  background: oklch(0.92 0.015 95);
  padding: 2px 6px;
  border-radius: 5px;
}

@media (prefers-reduced-motion: reduce) {
  .car-09 * {
    transition-duration: .01ms !important;
  }
}
```
