---
source: "codefronts"
url: "https://codefronts.com/snippets/css-tags-chips/gradient-edge/"
title: "Animated Gradient Border Chip CSS"
section: "snippets"
category: "css-tags-chips"
category_name: "CSS Tags & Chips"
description: "The gradient border that works in every browser shipped this decade: two stacked backgrounds — an opaque fill clipped to padding-box laid over an oversized…"
has_js: "false"
---

Here's a working CSS Tags & Chip from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Animated Gradient Border Chip CSS
Source: https://codefronts.com/snippets/css-tags-chips/gradient-edge/

The gradient border that works in every browser shipped this decade: two stacked backgrounds — an opaque fill clipped to padding-box laid over an oversized moving gradient clipped to border-box — with a transparent border letting the gradient peek through as the ring. No pseudo-elements, no masks, no @property, which makes this the technique to reach for when demo 07's Houdini approach is off the table. The motion is a background-position slide across a 300%-wide gradient.
## HTML
```html
<section class="ctc-15" aria-label="Animated gradient border chip demo">
  <div class="ctc-15__stage">
    <div class="ctc-15__wrap">
      <header class="ctc-15__head">
        <p class="ctc-15__kicker">Gradient borders · the everywhere technique</p>
        <h1>Two backgrounds, one transparent border</h1>
      </header>
      <div class="ctc-15__panel">
        <p class="ctc-15__lab">01 · Always running — 300% gradient sliding underneath</p>
        <div class="ctc-15__row">
          <a class="ctc-15__chip" href="#ctc15">Featured drop</a>
          <a class="ctc-15__chip" href="#ctc15">Trending #1</a>
          <a class="ctc-15__chip ctc-15__chip--fast" href="#ctc15">Processing…</a>
        </div>
      </div>
      <div class="ctc-15__panel">
        <p class="ctc-15__lab">02 · Runs on hover — paused, not removed, so it freezes mid-slide</p>
        <div class="ctc-15__row">
          <a class="ctc-15__chip ctc-15__chip--hover" href="#ctc15">Hover to ignite</a>
          <a class="ctc-15__chip ctc-15__chip--hover" href="#ctc15">Me too</a>
          <a class="ctc-15__chip ctc-15__chip--hover ctc-15__chip--duo" href="#ctc15">Duotone brand pair</a>
        </div>
      </div>
      <div class="ctc-15__panel">
        <p class="ctc-15__lab">03 · Shape-proof — real border, any radius, per-side widths</p>
        <div class="ctc-15__row">
          <span class="ctc-15__chip ctc-15__chip--sq">radius 10px</span>
          <span class="ctc-15__chip ctc-15__chip--thick">3px ring</span>
          <span class="ctc-15__chip ctc-15__chip--under">underline only</span>
        </div>
      </div>
      <p class="ctc-15__note">The fill is written as <code>linear-gradient(c, c) padding-box</code> — a plain <code>background-color</code> would paint under both clips and cover the ring. First layer in the list paints on top.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.ctc-15,
.ctc-15 *,
.ctc-15 *::before,
.ctc-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ctc-15 {
  --bg: oklch(0.965 0.008 260);
  --card: oklch(0.995 0.002 260);
  --ink: oklch(0.25 0.025 265);
  --mut: oklch(0.5 0.02 265);
  --line: oklch(0.89 0.012 260);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
}

.ctc-15__stage {
  width: 100%;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  display: grid;
  place-items: center;
  padding: clamp(16px,4cqi,48px);
  background: radial-gradient(70cqi 55cqi at 88% -10%,oklch(0.9 0.05 20/.5),transparent 62%),radial-gradient(60cqi 50cqi at -5% 112%,oklch(0.9 0.05 200/.5),transparent 60%),var(--bg);
  container: ctc15/inline-size;
}

.ctc-15__wrap {
  width: min(680px,100%);
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.ctc-15__kicker {
  font-size: 11.5px;
  font-weight: 800;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: oklch(0.6 0.17 20);
}

.ctc-15__head h1 {
  font-size: clamp(23px,3.6cqi,36px);
  font-weight: 800;
  letter-spacing: -.03em;
  margin: 8px 0 8px;
}

.ctc-15__panel {
  background: oklch(1 0 0/.6);
  border: 1px solid var(--line);
  border-radius: 18px;
  padding: 16px 18px;
}

.ctc-15__lab {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .05em;
  text-transform: uppercase;
  color: var(--mut);
  margin-bottom: 13px;
}

.ctc-15__row {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  align-items: center;
}

.ctc-15__chip {
  display: inline-flex;
  align-items: center;
  min-height: 44px;
  padding: 0 20px;
  border: 2px solid transparent;
  border-radius: 99px;
  font-size: 13.5px;
  font-weight: 750;
  text-decoration: none;
  color: var(--ink);
  background: linear-gradient(var(--card),var(--card)) padding-box,linear-gradient(60deg,oklch(0.7 0.19 20),oklch(0.75 0.16 85),oklch(0.72 0.17 200),oklch(0.7 0.19 20)) border-box;
  background-size: auto,300% 100%;
  animation: ctc15-slide 4s linear infinite;
  transition: translate .2s,box-shadow .25s;
}

@keyframes ctc15-slide {
  to {
    background-position: 0 0,300% 0;
  }
}

a.ctc-15__chip:hover,
a.ctc-15__chip:focus-visible {
  translate: 0 -2px;
  box-shadow: 0 10px 22px -12px oklch(0.6 0.15 40);
}

a.ctc-15__chip:focus-visible {
  outline: 2px solid oklch(0.6 0.17 20);
  outline-offset: 3px;
}

.ctc-15__chip--fast {
  animation-duration: 1.4s;
}

.ctc-15__chip--hover {
  animation-play-state: paused;
}

.ctc-15__chip--hover:hover,
.ctc-15__chip--hover:focus-visible {
  animation-play-state: running;
}

.ctc-15__chip--duo {
  background: linear-gradient(var(--card),var(--card)) padding-box,linear-gradient(60deg,oklch(0.55 0.19 262),oklch(0.7 0.17 320),oklch(0.55 0.19 262)) border-box;
  background-size: auto,300% 100%;
}

.ctc-15__chip--sq {
  border-radius: 10px;
}

.ctc-15__chip--thick {
  border-width: 3px;
}

.ctc-15__chip--under {
  border-width: 0 0 3px;
  border-radius: 4px;
}

.ctc-15__note {
  font-size: 12.5px;
  line-height: 1.6;
  color: var(--mut);
  border-left: 3px solid oklch(0.6 0.17 20);
  padding-left: 12px;
}

.ctc-15__note code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .9em;
  background: oklch(0.92 0.01 260);
  padding: 1px 5px;
  border-radius: 4px;
  color: var(--ink);
}

@media (prefers-reduced-motion: reduce) {
  .ctc-15__chip {
    animation: none;
  }
}
```
