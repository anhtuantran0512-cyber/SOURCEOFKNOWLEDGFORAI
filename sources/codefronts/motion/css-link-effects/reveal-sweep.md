---
source: "codefronts"
url: "https://codefronts.com/motion/css-link-effects/reveal-sweep/"
title: "CSS Sweep / Wipe Text Reveal Hover"
section: "motion"
category: "css-link-effects"
category_name: "CSS Link Effects"
description: "Clip-path is the cleanest reveal machine in CSS: a recolored copy of the label wipes across the original, edge razor-sharp, no gradients, no measuring."
has_js: "false"
---

Here's a working CSS Link Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Sweep / Wipe Text Reveal Hover
Source: https://codefronts.com/motion/css-link-effects/reveal-sweep/

Clip-path is the cleanest reveal machine in CSS: a recolored copy of the label wipes across the original, edge razor-sharp, no gradients, no measuring. Ships as a straight left-to-right recolor, a slanted-edge diagonal curtain, and the show-off variant — the label wipes into a completely different word ('Pricing' becomes 'From $0/mo').
## HTML
```html
<section class="cle-15" aria-label="Sweep reveal hover demo">
  <div class="cle-15__stage">
    <div class="cle-15__var"><a href="#a" class="cle-15__wipe" data-text="Manifesto">Manifesto</a><small class="cle-15__cap">A · straight recolor wipe</small></div>
    <div class="cle-15__var"><a href="#b" class="cle-15__blade" data-text="Collections">Collections</a><small class="cle-15__cap">B · slanted curtain</small></div>
    <div class="cle-15__var"><a href="#c" class="cle-15__swap"><span class="cle-15__base">Pricing</span><span class="cle-15__alt" aria-hidden="true">From $0/mo</span></a><small class="cle-15__cap">C · wipes to a new word</small></div>
  </div>
</section>
```
## CSS
```css
.cle-15,
.cle-15 *,
.cle-15 *::before,
.cle-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cle-15 {
  width: 100%;
  min-height: 100vh;
  --paper: oklch(0.96 0.01 85);
  --ink: oklch(0.24 0.02 60);
  --accent: oklch(0.68 0.19 45);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.cle-15__stage {
  width: 100%;
  height: 100vh;
  display: grid;
  align-content: center;
  justify-items: center;
  gap: 44px;
  background: linear-gradient(165deg,oklch(0.3 0.025 55),oklch(0.21 0.02 50));
  padding: 44px 32px;
}

.cle-15__var {
  display: grid;
  gap: 13px;
  justify-items: center;
}

.cle-15__cap {
  font-size: 10.5px;
  font-weight: 600;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: oklch(0.6 0.04 55);
}

.cle-15 a {
  position: relative;
  color: var(--paper);
  text-decoration: none;
  font-size: clamp(30px,4.6vw,42px);
  font-weight: 800;
  letter-spacing: -.02em;
}

.cle-15 a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 6px;
  border-radius: 4px;
}

.cle-15__wipe::after,
.cle-15__blade::after {
  content: attr(data-text);
  position: absolute;
  inset: 0;
  color: var(--accent);
  transition: clip-path .45s cubic-bezier(.3,.8,.2,1);
}

.cle-15__wipe::after {
  clip-path: inset(0 100% 0 0);
}

.cle-15__wipe:hover::after,
.cle-15__wipe:focus-visible::after {
  clip-path: inset(0 0 0 0);
}

.cle-15__blade::after {
  clip-path: polygon(-20% 0,-5% 0,-20% 100%,-35% 100%);
  transition-duration: .5s;
}

.cle-15__blade:hover::after,
.cle-15__blade:focus-visible::after {
  clip-path: polygon(-20% 0,115% 0,100% 100%,-35% 100%);
}

.cle-15__swap {
  display: inline-grid;
  text-align: center;
}

.cle-15__swap > span {
  grid-area: 1/1;
  white-space: nowrap;
}

.cle-15__alt {
  color: oklch(0.2 0.02 50);
  background: var(--accent);
  border-radius: 10px;
  padding: 0 .35em;
  clip-path: inset(0 100% 0 0 round 10px);
  transition: clip-path .45s cubic-bezier(.3,.8,.2,1);
}

.cle-15__swap:hover .cle-15__alt,
.cle-15__swap:focus-visible .cle-15__alt {
  clip-path: inset(0 0 0 0 round 10px);
}

@media (prefers-reduced-motion: reduce) {
  .cle-15 * {
    transition-duration: .01s !important;
  }
}
```
