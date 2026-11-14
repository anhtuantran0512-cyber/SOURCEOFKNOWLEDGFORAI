---
source: "codefronts"
url: "https://codefronts.com/snippets/css-tags-chips/sliding-border/"
title: "Animated Border Outline Tag Effect"
section: "snippets"
category: "css-tags-chips"
category_name: "CSS Tags & Chips"
description: "Borders that draw themselves."
has_js: "false"
---

Here's a working CSS Tags & Chip from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Animated Border Outline Tag Effect
Source: https://codefronts.com/snippets/css-tags-chips/sliding-border/

Borders that draw themselves. Hover any tag and a conic-gradient ring sweeps 0°→360° around it like a pen tracing the outline — a real transition on a registered @property angle, not a keyframe hack. A second variant keeps a comet segment orbiting forever, and a third fills the ring as a progress indicator. The ring itself is carved with the mask-composite trick, so the center stays perfectly transparent over any background.
## HTML
```html
<section class="ctc-07" aria-label="Animated border outline tag demo">
  <div class="ctc-07__stage">
    <div class="ctc-07__wrap">
      <header class="ctc-07__head">
        <p class="ctc-07__kicker">Border draw · @property + conic + mask</p>
        <h1>Hover. Watch the ink go around.</h1>
      </header>
      <div class="ctc-07__panel">
        <p class="ctc-07__lab">01 · Draw on hover — <code>transition: --angle .7s</code></p>
        <div class="ctc-07__row">
          <a class="ctc-07__tag" style="--h:200" href="#ctc07">css</a>
          <a class="ctc-07__tag" style="--h:292" href="#ctc07">houdini</a>
          <a class="ctc-07__tag" style="--h:150" href="#ctc07">@property</a>
          <a class="ctc-07__tag" style="--h:40" href="#ctc07">conic-gradient</a>
          <a class="ctc-07__tag" style="--h:330" href="#ctc07">mask-composite</a>
        </div>
      </div>
      <div class="ctc-07__panel">
        <p class="ctc-07__lab">02 · Orbiting comet — keyframes on the gradient's <code>from</code> angle</p>
        <div class="ctc-07__row">
          <span class="ctc-07__tag ctc-07__tag--orbit" style="--h:200">scanning…</span>
          <span class="ctc-07__tag ctc-07__tag--orbit" style="--h:292">syncing</span>
          <span class="ctc-07__tag ctc-07__tag--orbit ctc-07__tag--slow" style="--h:150">background job</span>
        </div>
      </div>
      <div class="ctc-07__panel">
        <p class="ctc-07__lab">03 · Determinate ring — same CSS, angle set inline as progress</p>
        <div class="ctc-07__row">
          <span class="ctc-07__tag ctc-07__tag--set" style="--h:150;--ctc07a:90deg">25% uploaded</span>
          <span class="ctc-07__tag ctc-07__tag--set" style="--h:200;--ctc07a:216deg">60% uploaded</span>
          <span class="ctc-07__tag ctc-07__tag--set" style="--h:292;--ctc07a:342deg">95% uploaded</span>
        </div>
      </div>
      <p class="ctc-07__note">The ring is a pseudo-element hollowed by <code>mask-composite:exclude</code> — the center stays truly transparent, so this works over photos and gradients, not just flat fills.</p>
    </div>
  </div>
</section>
```
## CSS
```css
@property --ctc07a {
  syntax: "<angle>";
  inherits: false;
  initial-value: 0deg;
}

@property --ctc07f {
  syntax: "<angle>";
  inherits: false;
  initial-value: 0deg;
}

.ctc-07,
.ctc-07 *,
.ctc-07 *::before,
.ctc-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ctc-07 {
  --bg: oklch(0.19 0.02 265);
  --ink: oklch(0.95 0.008 265);
  --mut: oklch(0.66 0.02 265);
  --line: oklch(0.32 0.025 265);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
}

.ctc-07__stage {
  width: 100%;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  display: grid;
  place-items: center;
  padding: clamp(16px,4cqi,48px);
  background: radial-gradient(70cqi 55cqi at 85% -10%,oklch(0.32 0.08 292/.5),transparent 62%),radial-gradient(60cqi 50cqi at -5% 110%,oklch(0.3 0.07 200/.5),transparent 60%),var(--bg);
  container: ctc07/inline-size;
}

.ctc-07__wrap {
  width: min(700px,100%);
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.ctc-07__kicker {
  font-size: 11.5px;
  font-weight: 800;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: oklch(0.75 0.12 200);
}

.ctc-07__head h1 {
  font-size: clamp(24px,3.8cqi,38px);
  font-weight: 800;
  letter-spacing: -.03em;
  margin: 8px 0 8px;
}

.ctc-07__panel {
  background: oklch(1 0 0/.045);
  border: 1px solid var(--line);
  border-radius: 18px;
  padding: 16px 18px;
}

.ctc-07__lab {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .05em;
  text-transform: uppercase;
  color: var(--mut);
  margin-bottom: 12px;
}

.ctc-07__lab code,
.ctc-07__note code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .95em;
  letter-spacing: 0;
  text-transform: none;
  background: oklch(1 0 0/.09);
  padding: 1px 5px;
  border-radius: 4px;
  color: var(--ink);
}

.ctc-07__row {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

.ctc-07__tag {
  --c: oklch(0.78 0.14 var(--h,200));
  position: relative;
  display: inline-flex;
  align-items: center;
  min-height: 44px;
  padding: 0 20px;
  border-radius: 99px;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 13.5px;
  font-weight: 600;
  text-decoration: none;
  color: var(--ink);
  background: oklch(1 0 0/.05);
  box-shadow: inset 0 0 0 1px var(--line);
  transition: color .25s,box-shadow .25s;
}

.ctc-07__tag::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
  padding: 2px;
  background: conic-gradient(from calc(var(--ctc07f) - 90deg),var(--c) var(--ctc07a),transparent 0);
  -webkit-mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  transition: --ctc07a .7s ease;
}

a.ctc-07__tag:hover,
a.ctc-07__tag:focus-visible {
  --ctc07a: 360deg;
  color: var(--c);
  box-shadow: inset 0 0 0 1px transparent;
}

a.ctc-07__tag:hover::before,
a.ctc-07__tag:focus-visible::before {
  --ctc07a: 360deg;
}

a.ctc-07__tag:focus-visible {
  outline: 2px solid var(--c);
  outline-offset: 3px;
}

.ctc-07__tag--orbit {
  color: var(--mut);
}

.ctc-07__tag--orbit::before {
  background: conic-gradient(from var(--ctc07f),transparent 0 82%,var(--c) 96%,oklch(0.98 0.01 var(--h)) 100%);
  animation: ctc07-orbit 2.6s linear infinite;
}

.ctc-07__tag--slow::before {
  animation-duration: 5s;
}

@keyframes ctc07-orbit {
  to {
    --ctc07f: 360deg;
  }
}

.ctc-07__tag--set {
  color: var(--c);
}

.ctc-07__tag--set::before {
  transition: none;
}

.ctc-07__note {
  font-size: 12.5px;
  line-height: 1.6;
  color: var(--mut);
  border-left: 3px solid oklch(0.75 0.12 200);
  padding-left: 12px;
}

@media (prefers-reduced-motion: reduce) {
  .ctc-07 * {
    transition-duration: .01ms !important;
  }

  .ctc-07__tag--orbit::before {
    animation: none;
    background: conic-gradient(var(--c) 30deg,transparent 0);
  }
}
```
