---
source: "codefronts"
url: "https://codefronts.com/motion/css-link-effects/tilde-morph/"
title: "CSS Morphing Symbol / Tilde Hover Effect"
section: "motion"
category: "css-link-effects"
category_name: "CSS Link Effects"
description: "The editorial-site signature: a small glyph before the label that becomes a different glyph on hover."
has_js: "false"
---

Here's a working CSS Link Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Morphing Symbol / Tilde Hover Effect
Source: https://codefronts.com/motion/css-link-effects/tilde-morph/

The editorial-site signature: a small glyph before the label that becomes a different glyph on hover. A tilde that rolls up into an arrow, a plus that spins into a crossmark, and a download arrow that drops away as a checkmark pops in. Pure CSS — no icon font, no SVG sprite, just two stacked characters and a transform.
## HTML
```html
<section class="cle-08" aria-label="Morphing symbol hover demo">
  <div class="cle-08__stage">
    <div class="cle-08__var">
      <a href="#a" class="cle-08__roll"><span class="cle-08__slot" aria-hidden="true"><span class="cle-08__gA">~</span><span class="cle-08__gB">→</span></span>Explore the archive</a>
      <small class="cle-08__cap">A · tilde rolls into arrow</small>
    </div>
    <div class="cle-08__var">
      <a href="#b" class="cle-08__spin"><span class="cle-08__slot" aria-hidden="true"><span class="cle-08__gC">+</span></span>Expand details</a>
      <small class="cle-08__cap">B · plus spins to cross</small>
    </div>
    <div class="cle-08__var">
      <a href="#c" class="cle-08__drop"><span class="cle-08__slot" aria-hidden="true"><span class="cle-08__gA">↓</span><span class="cle-08__gB">✓</span></span>Download kit</a>
      <small class="cle-08__cap">C · arrow drops, check lands</small>
    </div>
  </div>
</section>
```
## CSS
```css
.cle-08,
.cle-08 *,
.cle-08 *::before,
.cle-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cle-08 {
  width: 100%;
  min-height: 100vh;
  --ink: oklch(0.27 0.02 150);
  --brand: oklch(0.55 0.16 150);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.cle-08__stage {
  width: 100%;
  height: 100vh;
  display: grid;
  align-content: center;
  justify-items: start;
  gap: 38px;
  border: 1px solid oklch(0.9 0.015 150);
  background: linear-gradient(170deg,oklch(0.98 0.008 140),oklch(0.95 0.018 155));
  padding: 44px clamp(36px,12%,140px);
}

.cle-08__var {
  display: grid;
  gap: 11px;
}

.cle-08__cap {
  font-size: 10.5px;
  font-weight: 600;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: oklch(0.55 0.04 150);
  padding-left: calc(1.1em + 10px);
}

.cle-08 a {
  display: inline-flex;
  align-items: baseline;
  gap: 10px;
  font-size: 22px;
  font-weight: 650;
  letter-spacing: -.01em;
  color: var(--ink);
  text-decoration: none;
  transition: color .3s;
}

.cle-08 a:hover,
.cle-08 a:focus-visible {
  color: var(--brand);
}

.cle-08 a:focus-visible {
  outline: 2px solid var(--brand);
  outline-offset: 5px;
  border-radius: 3px;
}

.cle-08__slot {
  display: inline-grid;
  width: 1.1em;
  justify-items: center;
  overflow: hidden;
  color: var(--brand);
}

.cle-08__slot span {
  grid-area: 1/1;
  transition: translate .35s cubic-bezier(.3,1.3,.4,1),opacity .25s,rotate .4s cubic-bezier(.3,1.3,.4,1),scale .35s cubic-bezier(.3,1.3,.4,1);
}

.cle-08__gB {
  translate: 0 70%;
  opacity: 0;
}

.cle-08__roll:hover .cle-08__gA,
.cle-08__roll:focus-visible .cle-08__gA {
  translate: 0 -70%;
  opacity: 0;
}

.cle-08__roll:hover .cle-08__gB,
.cle-08__roll:focus-visible .cle-08__gB {
  translate: 0 0;
  opacity: 1;
}

.cle-08__spin:hover .cle-08__gC,
.cle-08__spin:focus-visible .cle-08__gC {
  rotate: 135deg;
}

.cle-08__drop .cle-08__gB {
  translate: 0 0;
  scale: .3;
  opacity: 0;
}

.cle-08__drop:hover .cle-08__gA,
.cle-08__drop:focus-visible .cle-08__gA {
  translate: 0 90%;
  opacity: 0;
}

.cle-08__drop:hover .cle-08__gB,
.cle-08__drop:focus-visible .cle-08__gB {
  scale: 1;
  opacity: 1;
  transition-delay: 90ms;
}

@media (prefers-reduced-motion: reduce) {
  .cle-08 * {
    transition-duration: .01s !important;
    transition-delay: 0s !important;
  }
}
```
