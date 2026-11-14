---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-hover-effects/distorted-wave-ripple-effect/"
title: "Distorted Wave / Ripple Effect"
section: "motion"
category: "css-text-hover-effects"
category_name: "CSS Text Hover Effects"
description: "Type seen through moving water: an SVG filter — feTurbulence generating animated noise, feDisplacementMap pushing the glyph pixels around by it — does…"
has_js: "false"
---

Here's a working CSS Text Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Distorted Wave / Ripple Effect
Source: https://codefronts.com/motion/css-text-hover-effects/distorted-wave-ripple-effect/

Type seen through moving water: an SVG filter — feTurbulence generating animated noise, feDisplacementMap pushing the glyph pixels around by it — does distortion CSS alone cannot, and a SMIL <animate> keeps the wave rolling with zero JavaScript. The integration trick is the crossfade: filter:url() can't transition, so the headline keeps a crisp copy and a permanently-rippling aria-hidden clone stacked on it, and hover simply fades between them — the water rises smoothly over the word instead of snapping on.
## HTML
```html
<section class="cth-29" aria-label="Ripple distortion text demo">
  <div class="cth-29__stage">
    <svg width="0" height="0" aria-hidden="true" focusable="false"><filter id="cth29-ripple" x="-25%" y="-25%" width="150%" height="150%"><feTurbulence type="turbulence" baseFrequency="0.012 0.05" numOctaves="2" seed="4" result="n"><animate attributeName="baseFrequency" dur="7s" values="0.012 0.05; 0.017 0.09; 0.012 0.05" repeatCount="indefinite"/></feTurbulence><feDisplacementMap in="SourceGraphic" in2="n" scale="16" xChannelSelector="R" yChannelSelector="G"/></filter></svg>
    <div class="cth-29__scene">
      <p class="cth-29__eyebrow">Undertow &mdash; surf &amp; swell reports, delivered at dawn</p>
      <a class="cth-29__word" href="#cth29-top" id="cth29-top">
        <span class="cth-29__crisp">UNDERTOW</span>
        <span class="cth-29__clone" aria-hidden="true">UNDERTOW</span>
      </a>
      <svg class="cth-29__waveline" viewBox="0 0 220 14" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" d="M2 7 Q 15 1, 28 7 T 54 7 T 80 7 T 106 7 T 132 7 T 158 7 T 184 7 T 210 7"><animate attributeName="d" dur="2.6s" repeatCount="indefinite" values="M2 7 Q 15 1, 28 7 T 54 7 T 80 7 T 106 7 T 132 7 T 158 7 T 184 7 T 210 7; M2 7 Q 15 13, 28 7 T 54 7 T 80 7 T 106 7 T 132 7 T 158 7 T 184 7 T 210 7; M2 7 Q 15 1, 28 7 T 54 7 T 80 7 T 106 7 T 132 7 T 158 7 T 184 7 T 210 7"/></path></svg>
      <p class="cth-29__hint">Hover the wordmark &mdash; it slips underwater. <code>feTurbulence</code> + <code>feDisplacementMap</code> do the physics; a crossfaded clone hides that <code>filter:url()</code> can't transition.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.cth-29,
.cth-29 *,
.cth-29 *::before,
.cth-29 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cth-29 {
  --bg: oklch(0.17 0.025 230);
  --ink: oklch(0.93 0.02 210);
  --mut: oklch(0.6 0.04 220);
  --acc: oklch(0.78 0.12 195);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cth-29__stage {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  background: radial-gradient(100% 85% at 50% 100%,oklch(0.23 0.05 220),var(--bg) 70%);
  padding: clamp(20px,4vw,56px);
  container: cth29/inline-size;
}

.cth-29__scene {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: clamp(16px,3cqi,26px);
}

.cth-29__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .26em;
  text-transform: uppercase;
  color: var(--mut);
}

.cth-29__word {
  position: relative;
  display: inline-block;
  text-decoration: none;
  font-size: clamp(50px,11.5cqi,118px);
  font-weight: 900;
  letter-spacing: -.015em;
  line-height: 1;
  padding: .15em .12em;
}

.cth-29__word:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 8px;
  border-radius: 6px;
}

.cth-29__crisp {
  display: block;
  color: var(--ink);
  opacity: 1;
  transition: opacity .6s ease;
}

.cth-29__clone {
  position: absolute;
  inset: .15em .12em;
  display: block;
  color: var(--acc);
  opacity: 0;
  filter: url(#cth29-ripple);
  transition: opacity .6s ease;
}

.cth-29__word:hover .cth-29__crisp,
.cth-29__word:focus-visible .cth-29__crisp {
  opacity: .06;
}

.cth-29__word:hover .cth-29__clone,
.cth-29__word:focus-visible .cth-29__clone {
  opacity: 1;
}

.cth-29__waveline {
  width: min(220px,60%);
  color: color-mix(in oklch,var(--acc) 55%,transparent);
}

.cth-29__hint {
  font-size: 12.5px;
  line-height: 1.7;
  color: var(--mut);
  max-width: 58ch;
}

.cth-29__hint code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .9em;
  background: oklch(0.24 0.03 225);
  padding: 1px 6px;
  border-radius: 4px;
  color: var(--acc);
}

@media (prefers-reduced-motion: reduce) {
  .cth-29__clone {
    transition: none;
    opacity: 0 !important;
  }

  .cth-29__crisp {
    opacity: 1 !important;
    transition: none;
  }

  .cth-29__word:hover .cth-29__crisp {
    color: var(--acc);
  }
}
```
