---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-hover-effects/animated-border-encased-text-hover/"
title: "Animated Border / Encased Text Hover"
section: "motion"
category: "css-text-hover-effects"
category_name: "CSS Text Hover Effects"
description: "Two grades of 'the text draws a box around itself': the TRACE — two corner pseudo-elements whose width and height tween in sequence, so a hairline visibly…"
has_js: "false"
---

Here's a working CSS Text Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Animated Border / Encased Text Hover
Source: https://codefronts.com/motion/css-text-hover-effects/animated-border-encased-text-hover/

Two grades of 'the text draws a box around itself': the TRACE — two corner pseudo-elements whose width and height tween in sequence, so a hairline visibly runs around the CTA clockwise, corner meeting corner — and the ORBIT — a conic-gradient ring rotating behind a padded inner panel, its angle driven by a registered @property so a comet of light laps the button under the cursor. Trace for editorial ghost buttons, orbit for the glowing tech CTA; both are markup you already have plus pseudo-elements.
## HTML
```html
<section class="cth-18" aria-label="Animated border encased text demo">
  <div class="cth-18__stage">
    <div class="cth-18__scene">
      <p class="cth-18__eyebrow">Helio deploy &mdash; private beta</p>
      <h1 class="cth-18__title">Ship the edge build</h1>
      <p class="cth-18__sub">Zero-config previews on every push. Two seats left in the winter cohort.</p>
      <div class="cth-18__row">
        <a class="cth-18__trace" href="#cth18-top" id="cth18-top"><span>Read the runbook</span></a>
        <a class="cth-18__orbit" href="#cth18-top"><span>Request access</span></a>
      </div>
      <p class="cth-18__hint">Left: two corner pseudo-elements trace the frame (width, then height &mdash; watch the corners meet). Right: a <code>@property</code> angle spins a conic comet around the text.</p>
    </div>
  </div>
</section>
```
## CSS
```css
@property --cth18-a {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

.cth-18,
.cth-18 *,
.cth-18 *::before,
.cth-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cth-18 {
  --bg: oklch(0.17 0.012 260);
  --ink: oklch(0.95 0.008 250);
  --mut: oklch(0.62 0.02 255);
  --acc: oklch(0.85 0.17 130);
  --line: oklch(0.32 0.02 258);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cth-18__stage {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  background: radial-gradient(90% 70% at 50% 25%,oklch(0.21 0.018 262),var(--bg) 72%);
  padding: clamp(20px,4vw,56px);
  container: cth18/inline-size;
}

.cth-18__scene {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: clamp(14px,2.6cqi,20px);
}

.cth-18__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .26em;
  text-transform: uppercase;
  color: var(--acc);
}

.cth-18__title {
  font-size: clamp(34px,6.6cqi,62px);
  font-weight: 850;
  letter-spacing: -.025em;
  line-height: 1.06;
}

.cth-18__sub {
  font-size: 15px;
  line-height: 1.65;
  color: var(--mut);
  max-width: 46ch;
}

.cth-18__row {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: clamp(14px,3cqi,24px);
  margin-top: 10px;
}

.cth-18__trace {
  position: relative;
  display: grid;
  place-items: center;
  min-height: 56px;
  padding: 0 30px;
  font-size: 15.5px;
  font-weight: 750;
  letter-spacing: .02em;
  color: var(--ink);
  text-decoration: none;
  background: oklch(0.2 0.014 260);
}

.cth-18__trace::before,
.cth-18__trace::after {
  content: '';
  position: absolute;
  width: 0;
  height: 0;
  pointer-events: none;
}

.cth-18__trace::before {
  top: 0;
  left: 0;
  border-top: 1.5px solid var(--acc);
  border-right: 1.5px solid var(--acc);
  transition: width .2s ease-out,height .2s ease-out .2s;
}

.cth-18__trace::after {
  bottom: 0;
  right: 0;
  border-bottom: 1.5px solid var(--acc);
  border-left: 1.5px solid var(--acc);
  transition: width .2s ease-out,height .2s ease-out .2s;
}

.cth-18__trace:hover::before,
.cth-18__trace:hover::after,
.cth-18__trace:focus-visible::before,
.cth-18__trace:focus-visible::after {
  width: 100%;
  height: 100%;
}

.cth-18__trace:hover span,
.cth-18__trace:focus-visible span {
  color: var(--acc);
}

.cth-18__trace span {
  transition: color .3s ease .25s;
}

.cth-18__trace:focus-visible {
  outline: 1.5px solid var(--acc);
  outline-offset: 5px;
}

.cth-18__orbit {
  position: relative;
  display: grid;
  place-items: center;
  min-height: 56px;
  padding: 0 2px;
  border-radius: 14px;
  text-decoration: none;
  background: conic-gradient(from var(--cth18-a),transparent 0 78%,var(--acc) 92%,transparent 100%);
  --cth18-a: 40deg;
}

.cth-18__orbit span {
  display: grid;
  place-items: center;
  min-height: calc(56px - 3px);
  margin: 1.5px;
  padding: 0 30px;
  border-radius: 12.5px;
  background: oklch(0.22 0.016 260);
  color: var(--ink);
  font-size: 15.5px;
  font-weight: 750;
  letter-spacing: .02em;
  transition: background .3s,color .3s;
}

.cth-18__orbit:hover,
.cth-18__orbit:focus-visible {
  animation: cth18-spin 1.6s linear infinite;
}

.cth-18__orbit:hover span,
.cth-18__orbit:focus-visible span {
  color: var(--acc);
  background: oklch(0.19 0.014 260);
}

.cth-18__orbit:focus-visible {
  outline: 1.5px solid var(--acc);
  outline-offset: 4px;
}

@keyframes cth18-spin {
  to {
    --cth18-a: 400deg;
  }
}

.cth-18__hint {
  margin-top: 8px;
  font-size: 12.5px;
  line-height: 1.7;
  color: var(--mut);
  max-width: 60ch;
}

.cth-18__hint code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .9em;
  background: oklch(0.25 0.016 260);
  padding: 1px 6px;
  border-radius: 4px;
  color: var(--acc);
}

@media (prefers-reduced-motion: reduce) {
  .cth-18 *,
    .cth-18 *::before,
    .cth-18 *::after {
    transition-duration: .01ms !important;
    animation: none !important;
  }
}
```
