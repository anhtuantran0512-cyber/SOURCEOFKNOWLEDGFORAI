---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-3d/perspective-property-versus-perspective-function/"
title: "Perspective Property Versus Perspective Function"
section: "design-styles"
category: "css-3d"
category_name: "CSS 3D Effects"
description: "Two ways to write perspective that are not equivalent, rendered side by side."
has_js: "false"
---

Here's a working CSS 3D Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Perspective Property Versus Perspective Function
Source: https://codefronts.com/design-styles/css-3d/perspective-property-versus-perspective-function/

Two ways to write perspective that are not equivalent, rendered side by side. perspective: 800px on a parent gives four panels one shared vanishing point and they read as a single scene; transform: perspective(800px) rotateY(30deg) gives each panel a private camera and they read as four unrelated objects. Both rows are labelled, and the ordering trap is built in.
## HTML
```html
<section class="d3-02" aria-labelledby="d3-02-title">
  <h2 class="d3-02__sr" id="d3-02-title">Shared versus private vanishing point</h2>

  <div class="d3-02__theme">
    <input class="d3-02__theme-input" type="checkbox" id="d3-02-theme">
    <label class="d3-02__theme-label" for="d3-02-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="d3-02__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="d3-02__stage">
    <div class="d3-02__viewport">
      <header class="d3-02__head">
        <strong>Lumen Festival &mdash; day passes</strong>
        <span>same four tickets, two ways of declaring the camera</span>
      </header>

      <section class="d3-02__block">
        <p class="d3-02__cap"><b class="d3-02__badge d3-02__badge--ok">Correct</b> <code>perspective</code> on the rail &mdash; one shared vanishing point</p>
        <div class="d3-02__rail d3-02__rail--shared">
          <article class="d3-02__pass d3-02__pass--a"><span class="d3-02__day">Fri</span><b>Aurora</b><span class="d3-02__meta">18:00 &middot; Main</span><i class="d3-02__code" aria-hidden="true"></i></article>
          <article class="d3-02__pass d3-02__pass--b"><span class="d3-02__day">Sat</span><b>Nocturne</b><span class="d3-02__meta">20:30 &middot; Dome</span><i class="d3-02__code" aria-hidden="true"></i></article>
          <article class="d3-02__pass d3-02__pass--c"><span class="d3-02__day">Sun</span><b>Solstice</b><span class="d3-02__meta">15:00 &middot; Garden</span><i class="d3-02__code" aria-hidden="true"></i></article>
          <article class="d3-02__pass d3-02__pass--d"><span class="d3-02__day">All</span><b>Full run</b><span class="d3-02__meta">3 days &middot; VIP</span><i class="d3-02__code" aria-hidden="true"></i></article>
        </div>
      </section>

      <section class="d3-02__block">
        <p class="d3-02__cap"><b class="d3-02__badge d3-02__badge--no">Wrong</b> <code>perspective()</code> inside each ticket's own transform &mdash; four cameras</p>
        <div class="d3-02__rail d3-02__rail--private">
          <article class="d3-02__pass d3-02__pass--a"><span class="d3-02__day">Fri</span><b>Aurora</b><span class="d3-02__meta">18:00 &middot; Main</span><i class="d3-02__code" aria-hidden="true"></i></article>
          <article class="d3-02__pass d3-02__pass--b"><span class="d3-02__day">Sat</span><b>Nocturne</b><span class="d3-02__meta">20:30 &middot; Dome</span><i class="d3-02__code" aria-hidden="true"></i></article>
          <article class="d3-02__pass d3-02__pass--c"><span class="d3-02__day">Sun</span><b>Solstice</b><span class="d3-02__meta">15:00 &middot; Garden</span><i class="d3-02__code" aria-hidden="true"></i></article>
          <article class="d3-02__pass d3-02__pass--d"><span class="d3-02__day">All</span><b>Full run</b><span class="d3-02__meta">3 days &middot; VIP</span><i class="d3-02__code" aria-hidden="true"></i></article>
        </div>
      </section>
    </div>
  </div>
</section>
```
## CSS
```css
.d3-02 {
  --d3-02-bg: #eef1f6;
  --d3-02-surf: #ffffff;
  --d3-02-line: #d5dbe6;
  --d3-02-ink: #0e1420;
  --d3-02-mut: #5c6779;
  --d3-02-acc: #1f4fd8;
  --d3-02-acc: oklch(50% 0.21 264);
  --d3-02-p1: #ff5d7a;
  --d3-02-p1: oklch(68% 0.19 15);
  --d3-02-p2: #ff9f1c;
  --d3-02-p2: oklch(78% 0.16 68);
  --d3-02-p3: #12b6a0;
  --d3-02-p3: oklch(70% 0.13 178);
  --d3-02-p4: #7a5cff;
  --d3-02-p4: oklch(62% 0.2 287);
  --d3-02-no: #d92d20;
  --d3-02-no: oklch(56% 0.2 27);
  --d3-02-depth: 760px;
  --d3-02-font-display: "Avenir Next", "Segoe UI", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: radial-gradient(70rem 34rem at 88% -12%, color-mix(in oklab, var(--d3-02-p4) 18%, transparent), transparent 62%), radial-gradient(58rem 30rem at -6% 108%, color-mix(in oklab, var(--d3-02-p3) 18%, transparent), transparent 60%), var(--d3-02-bg);
  color: var(--d3-02-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.5;
}

.d3-02 *,
.d3-02 *::before,
.d3-02 *::after {
  box-sizing: border-box;
}

.d3-02__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.d3-02:has(.d3-02__theme-input:checked) {
  --d3-02-bg: #0a0e16;
  --d3-02-surf: #141b27;
  --d3-02-line: #29344a;
  --d3-02-ink: #eef2f8;
  --d3-02-mut: #9aa7bb;
  --d3-02-acc: #86a4ff;
  --d3-02-acc: oklch(76% 0.15 264);
  --d3-02-no: #ff7a6b;
  --d3-02-no: oklch(72% 0.17 27);
}

@media (prefers-color-scheme: dark) {
  .d3-02 {
    --d3-02-bg: #0a0e16;
    --d3-02-surf: #141b27;
    --d3-02-line: #29344a;
    --d3-02-ink: #eef2f8;
    --d3-02-mut: #9aa7bb;
    --d3-02-acc: #86a4ff;
    --d3-02-acc: oklch(76% 0.15 264);
    --d3-02-no: #ff7a6b;
    --d3-02-no: oklch(72% 0.17 27);
  }

  .d3-02:has(.d3-02__theme-input:checked) {
    --d3-02-bg: #eef1f6;
    --d3-02-surf: #ffffff;
    --d3-02-line: #d5dbe6;
    --d3-02-ink: #0e1420;
    --d3-02-mut: #5c6779;
    --d3-02-acc: #1f4fd8;
    --d3-02-acc: oklch(50% 0.21 264);
    --d3-02-no: #d92d20;
    --d3-02-no: oklch(56% 0.2 27);
  }
}

@media (prefers-color-scheme: light) {
  .d3-02:has(.d3-02__theme-input:checked) {
    --d3-02-bg: #0a0e16;
    --d3-02-surf: #141b27;
    --d3-02-line: #29344a;
    --d3-02-ink: #eef2f8;
    --d3-02-mut: #9aa7bb;
    --d3-02-acc: #86a4ff;
    --d3-02-acc: oklch(76% 0.15 264);
    --d3-02-no: #ff7a6b;
    --d3-02-no: oklch(72% 0.17 27);
  }
}

.d3-02__theme {
  position: absolute;
  inset-block-start: clamp(0.75rem, 3vw, 1.5rem);
  inset-inline-end: clamp(0.75rem, 3vw, 1.5rem);
  z-index: 20;
}

.d3-02__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.d3-02__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--d3-02-line);
  border-radius: 14px;
  background: var(--d3-02-surf);
  color: var(--d3-02-ink);
  cursor: pointer;
  box-shadow: 0 6px 18px rgba(14, 20, 32, 0.12);
}

.d3-02__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.d3-02__theme-input:focus-visible + .d3-02__theme-label {
  outline: 2px solid var(--d3-02-acc);
  outline-offset: 3px;
}

.d3-02__stage {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  place-items: center;
  min-block-size: 100vh;
  padding: clamp(3.5rem, 9vw, 5rem) clamp(0.75rem, 4vw, 2.5rem);
}

.d3-02__viewport {
  inline-size: 100%;
  max-inline-size: 64rem;
  overflow: hidden;
  display: grid;
  gap: clamp(1.1rem, 3.5vw, 2rem);
  padding: clamp(1rem, 3.5vw, 2rem);
  border: 1px solid var(--d3-02-line);
  border-radius: 26px;
  background: color-mix(in oklab, var(--d3-02-surf) 70%, transparent);
  box-shadow: 0 34px 80px -40px rgba(10, 14, 22, 0.6);
}

.d3-02__head {
  display: grid;
  gap: 0.2rem;
}

.d3-02__head strong {
  font: 800 clamp(1.1rem, 3.4vw, 1.6rem)/1.1 var(--d3-02-font-display);
  letter-spacing: -0.02em;
}

.d3-02__head span {
  font: 500 clamp(0.72rem, 2vw, 0.85rem)/1.3 system-ui, sans-serif;
  color: var(--d3-02-mut);
}

.d3-02__block {
  display: grid;
  gap: 0.75rem;
}

.d3-02__cap {
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.45rem;
  font: 500 clamp(0.7rem, 1.95vw, 0.8rem)/1.3 system-ui, sans-serif;
  color: var(--d3-02-mut);
}

.d3-02__cap code {
  font: 600 0.95em/1 ui-monospace, Menlo, monospace;
  color: var(--d3-02-ink);
}

.d3-02__badge {
  padding: 0.18rem 0.5rem;
  border-radius: 999px;
  font: 800 0.62rem/1.5 ui-monospace, Menlo, monospace;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #fff;
}

.d3-02__badge--ok {
  background: var(--d3-02-acc);
}

.d3-02__badge--no {
  background: var(--d3-02-no);
}

.d3-02__rail {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 8.5rem), 1fr));
  gap: clamp(0.6rem, 2.2vw, 1rem);
}

.d3-02__rail--shared {
  perspective: var(--d3-02-depth);
  perspective-origin: 50% 50%;
}

.d3-02__rail--shared .d3-02__pass {
  transform: rotateY(28deg);
}

.d3-02__rail--private .d3-02__pass {
  transform: perspective(var(--d3-02-depth)) rotateY(28deg);
}

.d3-02__pass {
  position: relative;
  overflow: hidden;
  min-block-size: clamp(8rem, 22vw, 10.5rem);
  padding: clamp(0.7rem, 2.4vw, 1rem);
  display: grid;
  align-content: start;
  gap: 0.15rem;
  border-radius: 16px;
  color: #fff;
  box-shadow: 0 18px 40px -18px rgba(10, 14, 22, 0.65);
}

.d3-02__pass::after {
  content: "";
  position: absolute;
  inset-inline: 0;
  inset-block-end: 2.4rem;
  block-size: 0;
  border-block-start: 2px dashed rgba(255, 255, 255, 0.45);
}

.d3-02__pass--a {
  background: linear-gradient(155deg, var(--d3-02-p1), color-mix(in oklab, var(--d3-02-p1) 55%, #2b0b18));
}

.d3-02__pass--b {
  background: linear-gradient(155deg, var(--d3-02-p2), color-mix(in oklab, var(--d3-02-p2) 50%, #3a1c00));
}

.d3-02__pass--c {
  background: linear-gradient(155deg, var(--d3-02-p3), color-mix(in oklab, var(--d3-02-p3) 50%, #04302b));
}

.d3-02__pass--d {
  background: linear-gradient(155deg, var(--d3-02-p4), color-mix(in oklab, var(--d3-02-p4) 50%, #1a1040));
}

.d3-02__day {
  font: 800 0.62rem/1.5 ui-monospace, Menlo, monospace;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  opacity: 0.85;
}

.d3-02__pass b {
  font: 800 clamp(0.95rem, 2.8vw, 1.15rem)/1.15 var(--d3-02-font-display);
  letter-spacing: -0.01em;
}

.d3-02__meta {
  font: 500 clamp(0.66rem, 1.8vw, 0.74rem)/1.2 ui-monospace, Menlo, monospace;
  opacity: 0.82;
}

.d3-02__code {
  position: absolute;
  inset-inline: clamp(0.7rem, 2.4vw, 1rem);
  inset-block-end: clamp(0.7rem, 2.4vw, 1rem);
  block-size: 1.4rem;
  border-radius: 3px;
  background-image: repeating-linear-gradient(90deg, rgba(255, 255, 255, 0.92) 0 2px, transparent 2px 4px, rgba(255, 255, 255, 0.92) 4px 5px, transparent 5px 8px);
  opacity: 0.9;
}
```
