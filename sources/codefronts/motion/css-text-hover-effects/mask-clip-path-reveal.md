---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-hover-effects/mask-clip-path-reveal/"
title: "Mask Clip Path Reveal"
section: "motion"
category: "css-text-hover-effects"
category_name: "CSS Text Hover Effects"
description: "The geometry chapter that closes the collection: three reveal shapes on one board, all riding clip-path's native interpolation."
has_js: "false"
---

Here's a working CSS Text Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Mask Clip Path Reveal
Source: https://codefronts.com/motion/css-text-hover-effects/mask-clip-path-reveal/

The geometry chapter that closes the collection: three reveal shapes on one board, all riding clip-path's native interpolation. A DIAGONAL WIPE — an accent-colored clone clipped to a 4-point polygon that sweeps corner-to-corner (the parallelogram's leading edge stays angled mid-flight). A CIRCLE BLOOM — a photograph clipped inside the glyphs (background-clip:text) revealed by circle(0%) growing to circle(75%). And BLINDS — a 12-point polygon whose three zero-width slats grow open into thirds of the word. The one law under all three: shapes interpolate only between the SAME function with the SAME point count.
## HTML
```html
<section class="cth-30" aria-label="Clip path reveal demo">
  <div class="cth-30__stage">
    <div class="cth-30__scene">
      <header class="cth-30__head">
        <p class="cth-30__eyebrow">Studio Meridian &mdash; title sequences &amp; type systems</p>
        <span class="cth-30__chip">same shape, same points &rarr; it tweens</span>
      </header>
      <div class="cth-30__rows">
        <a class="cth-30__row cth-30__wipe" href="#cth30-top" id="cth30-top">
          <span class="cth-30__tag">01 &middot; diagonal wipe &middot; polygon()</span>
          <span class="cth-30__stackword"><span class="cth-30__base">SEQUENCE</span><span class="cth-30__clone cth-30__clone--wipe" aria-hidden="true">SEQUENCE</span></span>
        </a>
        <a class="cth-30__row cth-30__bloom" href="#cth30-top">
          <span class="cth-30__tag">02 &middot; circle bloom &middot; circle() + photo-in-text</span>
          <span class="cth-30__stackword"><span class="cth-30__base">HORIZON</span><span class="cth-30__clone cth-30__clone--bloom" aria-hidden="true" style="--photo:url('https://images.unsplash.com/photo-1506905925346-21bda4d32df4?q=80&w=1400&auto=format&fit=crop')">HORIZON</span></span>
        </a>
        <a class="cth-30__row cth-30__blinds" href="#cth30-top">
          <span class="cth-30__tag">03 &middot; blinds &middot; 12-point polygon</span>
          <span class="cth-30__stackword"><span class="cth-30__base">INTERVAL</span><span class="cth-30__clone cth-30__clone--blinds" aria-hidden="true">INTERVAL</span></span>
        </a>
      </div>
      <p class="cth-30__hint">Hover each row. Three shapes, one law: clip-path only interpolates between the same function with the same point count &mdash; design the two states as siblings first.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.cth-30,
.cth-30 *,
.cth-30 *::before,
.cth-30 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cth-30 {
  --bg: oklch(0.2 0.012 285);
  --ink: oklch(0.94 0.008 280);
  --mut: oklch(0.62 0.02 285);
  --acc: oklch(0.75 0.17 65);
  --line: oklch(0.34 0.02 285);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cth-30__stage {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  background: radial-gradient(90% 75% at 50% 15%,oklch(0.24 0.016 290),var(--bg) 72%);
  padding: clamp(20px,4vw,56px);
  container: cth30/inline-size;
}

.cth-30__scene {
  width: min(100%,780px);
  display: flex;
  flex-direction: column;
  gap: clamp(16px,3cqi,26px);
}

.cth-30__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
  flex-wrap: wrap;
  padding-bottom: 14px;
  border-bottom: 1px solid var(--line);
}

.cth-30__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: var(--mut);
}

.cth-30__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--acc);
  border: 1px solid color-mix(in oklch,var(--acc) 40%,transparent);
  border-radius: 99px;
  padding: 5px 11px;
}

.cth-30__rows {
  display: flex;
  flex-direction: column;
}

.cth-30__row {
  display: flex;
  flex-direction: column;
  gap: 6px;
  padding: clamp(14px,2.6cqi,22px) 4px;
  border-bottom: 1px solid var(--line);
  text-decoration: none;
  color: inherit;
}

.cth-30__row:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
  border-radius: 6px;
}

.cth-30__tag {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10.5px;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--mut);
}

.cth-30__stackword {
  position: relative;
  display: inline-block;
  width: fit-content;
  font-size: clamp(38px,7.6cqi,74px);
  font-weight: 900;
  letter-spacing: .01em;
  line-height: 1.08;
}

.cth-30__base {
  display: block;
  color: color-mix(in oklch,var(--ink) 34%,transparent);
}

.cth-30__clone {
  position: absolute;
  inset: 0;
  display: block;
  pointer-events: none;
}

.cth-30__clone--wipe {
  color: var(--acc);
  clip-path: polygon(-15% 0%,0% 0%,-15% 100%,-30% 100%);
  transition: clip-path .65s cubic-bezier(.7,0,.2,1);
}

.cth-30__wipe:hover .cth-30__clone--wipe,
.cth-30__wipe:focus-visible .cth-30__clone--wipe {
  clip-path: polygon(0% 0%,130% 0%,115% 100%,-15% 100%);
}

.cth-30__clone--bloom {
  background-image: linear-gradient(oklch(0.6 0.1 260/.15),oklch(0.6 0.1 260/.15)),var(--photo);
  background-size: cover;
  background-position: center;
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  clip-path: circle(0% at 50% 55%);
  transition: clip-path .7s cubic-bezier(.3,.85,.25,1);
}

.cth-30__bloom:hover .cth-30__clone--bloom,
.cth-30__bloom:focus-visible .cth-30__clone--bloom {
  clip-path: circle(75% at 50% 55%);
}

.cth-30__clone--blinds {
  color: var(--acc);
  clip-path: polygon(0% 100%,0% 0%,0% 0%,0% 100%,33.3% 100%,33.3% 0%,33.3% 0%,33.3% 100%,66.6% 100%,66.6% 0%,66.6% 0%,66.6% 100%);
  transition: clip-path .6s cubic-bezier(.6,0,.25,1);
}

.cth-30__blinds:hover .cth-30__clone--blinds,
.cth-30__blinds:focus-visible .cth-30__clone--blinds {
  clip-path: polygon(0% 100%,0% 0%,33.3% 0%,33.3% 100%,33.3% 100%,33.3% 0%,66.6% 0%,66.6% 100%,66.6% 100%,66.6% 0%,100% 0%,100% 100%);
}

.cth-30__hint {
  font-size: 12.5px;
  line-height: 1.7;
  color: var(--mut);
  max-width: 62ch;
}

@media (prefers-reduced-motion: reduce) {
  .cth-30 * {
    transition-duration: .01ms !important;
  }
}
```
