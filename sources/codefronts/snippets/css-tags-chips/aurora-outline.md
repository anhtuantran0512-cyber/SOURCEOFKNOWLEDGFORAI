---
source: "codefronts"
url: "https://codefronts.com/snippets/css-tags-chips/aurora-outline/"
title: "Glowing Aurora Gradient Border Tag"
section: "snippets"
category: "css-tags-chips"
category_name: "CSS Tags & Chips"
description: "The border every AI product shipped in 2025, taken apart properly: a multi-stop conic gradient rotating through a registered @property angle, carved into a…"
has_js: "false"
---

Here's a working CSS Tags & Chip from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glowing Aurora Gradient Border Tag
Source: https://codefronts.com/snippets/css-tags-chips/aurora-outline/

The border every AI product shipped in 2025, taken apart properly: a multi-stop conic gradient rotating through a registered @property angle, carved into a ring with mask-composite, and duplicated on a second pseudo-element that is blurred 14px behind the tag — that blurred twin IS the aurora. Idle tags drift slowly; hover snaps the rotation faster and doubles the glow's opacity, like breathing on embers.
## HTML
```html
<section class="ctc-12" aria-label="Aurora gradient border tag demo">
  <div class="ctc-12__stage">
    <div class="ctc-12__wrap">
      <header class="ctc-12__head">
        <p class="ctc-12__kicker">Aurora borders · one gradient, ring + glow</p>
        <h1>The border and its light<br>are the same paint</h1>
      </header>
      <div class="ctc-12__panel">
        <p class="ctc-12__lab">01 · Idle drift — hover to make it breathe</p>
        <div class="ctc-12__row">
          <a class="ctc-12__tag" href="#ctc12">✦ New: AI review</a>
          <a class="ctc-12__tag" href="#ctc12">GPT-5 ready</a>
          <a class="ctc-12__tag" href="#ctc12">Early access</a>
        </div>
      </div>
      <div class="ctc-12__panel">
        <p class="ctc-12__lab">02 · Variants — same engine, three dials</p>
        <div class="ctc-12__row">
          <span class="ctc-12__tag ctc-12__tag--static">static halo</span>
          <span class="ctc-12__tag ctc-12__tag--text"><b>gradient text twin</b></span>
          <span class="ctc-12__tag ctc-12__tag--wide">corona · inset -3px</span>
        </div>
      </div>
      <div class="ctc-12__panel">
        <p class="ctc-12__lab">03 · In context — one aurora tag per card, no more</p>
        <div class="ctc-12__cards">
          <article><span class="ctc-12__tag ctc-12__tag--sm">✦ Pro</span><h3>Semantic search</h3><p>Embeddings across your whole workspace, reranked per query.</p></article>
          <article><span class="ctc-12__tag ctc-12__tag--sm ctc-12__tag--static">Beta</span><h3>Auto-summaries</h3><p>Every thread condensed to three bullets, on arrival.</p></article>
        </div>
      </div>
      <p class="ctc-12__note">Ring = <code>mask-composite:exclude</code>. Aurora = the same conic on <code>::after</code>, <code>blur(14px)</code>, behind. Hover animates <em>opacity</em>, never the blur radius.</p>
    </div>
  </div>
</section>
```
## CSS
```css
@property --ctc12a {
  syntax: "<angle>";
  inherits: false;
  initial-value: 0deg;
}

.ctc-12,
.ctc-12 *,
.ctc-12 *::before,
.ctc-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ctc-12 {
  --bg: oklch(0.17 0.02 290);
  --ink: oklch(0.95 0.008 290);
  --mut: oklch(0.65 0.02 290);
  --line: oklch(0.3 0.03 290);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
}

.ctc-12__stage {
  width: 100%;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  display: grid;
  place-items: center;
  padding: clamp(16px,4cqi,48px);
  background: radial-gradient(70cqi 55cqi at 15% -10%,oklch(0.3 0.09 320/.45),transparent 60%),radial-gradient(60cqi 50cqi at 105% 112%,oklch(0.28 0.08 200/.5),transparent 60%),var(--bg);
  container: ctc12/inline-size;
}

.ctc-12__wrap {
  width: min(680px,100%);
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.ctc-12__kicker {
  font-size: 11.5px;
  font-weight: 800;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: oklch(0.75 0.15 320);
}

.ctc-12__head h1 {
  font-size: clamp(24px,3.8cqi,38px);
  font-weight: 800;
  letter-spacing: -.03em;
  line-height: 1.12;
  margin: 8px 0 8px;
}

.ctc-12__panel {
  background: oklch(1 0 0/.045);
  border: 1px solid var(--line);
  border-radius: 18px;
  padding: 16px 18px;
}

.ctc-12__lab {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .05em;
  text-transform: uppercase;
  color: var(--mut);
  margin-bottom: 14px;
}

.ctc-12__row {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  align-items: center;
}

.ctc-12__tag {
  --spin: 6s;
  --glow: .35;
  position: relative;
  display: inline-flex;
  align-items: center;
  min-height: 44px;
  padding: 0 20px;
  border-radius: 99px;
  font-size: 13.5px;
  font-weight: 700;
  text-decoration: none;
  color: var(--ink);
  background: oklch(0.21 0.025 290);
  isolation: isolate;
  transition: translate .25s;
}

.ctc-12__tag::before,
.ctc-12__tag::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
  background: conic-gradient(from var(--ctc12a),oklch(0.75 0.18 320),oklch(0.72 0.19 200),oklch(0.78 0.17 140),oklch(0.75 0.18 320));
  animation: ctc12-spin var(--spin) linear infinite;
}

.ctc-12__tag::before {
  padding: 1.5px;
  -webkit-mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
}

.ctc-12__tag::after {
  z-index: -1;
  filter: blur(14px);
  opacity: var(--glow);
  transition: opacity .4s;
}

@keyframes ctc12-spin {
  to {
    --ctc12a: 360deg;
  }
}

a.ctc-12__tag:hover,
a.ctc-12__tag:focus-visible {
  --spin: 2.5s;
  translate: 0 -2px;
}

a.ctc-12__tag:hover::after,
a.ctc-12__tag:focus-visible::after {
  opacity: .7;
}

a.ctc-12__tag:focus-visible {
  outline: 2px solid oklch(0.75 0.18 320);
  outline-offset: 3px;
}

.ctc-12__tag--static::before,
.ctc-12__tag--static::after {
  animation: none;
}

.ctc-12__tag--text b {
  background: conic-gradient(from 40deg,oklch(0.78 0.18 320),oklch(0.75 0.19 200),oklch(0.8 0.17 140),oklch(0.78 0.18 320));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  font-weight: 800;
}

.ctc-12__tag--wide::after {
  inset: -3px;
}

.ctc-12__tag--sm {
  min-height: 34px;
  padding: 0 14px;
  font-size: 12px;
}

.ctc-12__cards {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}

.ctc-12__cards article {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 10px;
  padding: 16px;
  border-radius: 14px;
  border: 1px solid var(--line);
  background: oklch(0.2 0.022 290);
}

.ctc-12__cards h3 {
  font-size: 15px;
  font-weight: 750;
  letter-spacing: -.01em;
}

.ctc-12__cards p {
  font-size: 12.5px;
  line-height: 1.55;
  color: var(--mut);
}

.ctc-12__note {
  font-size: 12.5px;
  line-height: 1.6;
  color: var(--mut);
  border-left: 3px solid oklch(0.75 0.18 320);
  padding-left: 12px;
}

.ctc-12__note code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .9em;
  background: oklch(1 0 0/.09);
  padding: 1px 5px;
  border-radius: 4px;
  color: var(--ink);
}

@supports (not (transition: --ctc12a 1s)) and (selector(:has(a))) {
  .ctc-12__tag::after {
    animation: ctc12-pulse 3.2s ease-in-out infinite;
  }

  @keyframes ctc12-pulse {
    50% {
      opacity: calc(var(--glow) + .2);
    }
  }
}

@container ctc12 (width < 520px) {
  .ctc-12__cards {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ctc-12__tag::before,
    .ctc-12__tag::after {
    animation: none !important;
  }

  .ctc-12 * {
    transition-duration: .01ms !important;
  }
}
```
