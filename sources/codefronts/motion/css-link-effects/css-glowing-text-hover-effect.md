---
source: "codefronts"
url: "https://codefronts.com/motion/css-link-effects/css-glowing-text-hover-effect/"
title: "CSS Glowing Text Hover Effect"
section: "motion"
category: "css-link-effects"
category_name: "CSS Link Effects"
description: "Three grades of luminosity for dark UIs: a soft halo that breathes in through layered text-shadows, a hard phosphor glow with a white-hot core, and the aura…"
has_js: "false"
---

Here's a working CSS Link Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Glowing Text Hover Effect
Source: https://codefronts.com/motion/css-link-effects/css-glowing-text-hover-effect/

Three grades of luminosity for dark UIs: a soft halo that breathes in through layered text-shadows, a hard phosphor glow with a white-hot core, and the aura trick — a blurred duplicate of the label glowing behind the real one, which produces the cleanest big-radius bloom text-shadow can't match.
## HTML
```html
<section class="cle-06" aria-label="Glowing text hover demo">
  <div class="cle-06__stage">
    <div class="cle-06__var"><a href="#a" class="cle-06__halo">Night mode</a><small class="cle-06__cap">A · soft halo</small></div>
    <div class="cle-06__var"><a href="#b" class="cle-06__phosphor">Powered up</a><small class="cle-06__cap">B · phosphor core</small></div>
    <div class="cle-06__var"><a href="#c" class="cle-06__aura" data-text="Aurora lane">Aurora lane</a><small class="cle-06__cap">C · blurred-clone aura</small></div>
  </div>
</section>
```
## CSS
```css
.cle-06,
.cle-06 *,
.cle-06 *::before,
.cle-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cle-06 {
  width: 100%;
  min-height: 100vh;
  --glow: oklch(0.78 0.16 190);
  --glow2: oklch(0.72 0.19 310);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.cle-06__stage {
  width: 100%;
  height: 100vh;
  display: grid;
  align-content: center;
  justify-items: center;
  gap: 46px;
  background: radial-gradient(90% 120% at 50% 0%,oklch(0.21 0.03 260),oklch(0.14 0.015 260) 70%);
  padding: 44px 32px;
}

.cle-06__var {
  display: grid;
  gap: 13px;
  justify-items: center;
}

.cle-06__cap {
  font-size: 10.5px;
  font-weight: 600;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: oklch(0.56 0.02 250);
}

.cle-06 a {
  position: relative;
  font-size: clamp(26px,4vw,36px);
  font-weight: 750;
  letter-spacing: -.01em;
  text-decoration: none;
  color: oklch(0.62 0.03 250);
}

.cle-06 a:focus-visible {
  outline: 2px solid var(--glow);
  outline-offset: 6px;
  border-radius: 4px;
}

.cle-06__halo {
  text-shadow: 0 0 0 oklch(0.78 0.16 190 / 0),0 0 0 oklch(0.78 0.16 190 / 0),0 0 0 oklch(0.78 0.16 190 / 0);
  transition: text-shadow .45s,color .45s;
}

.cle-06__halo:hover,
.cle-06__halo:focus-visible {
  color: oklch(0.93 0.05 190);
  text-shadow: 0 0 12px color-mix(in oklch,var(--glow),transparent 40%),0 0 34px color-mix(in oklch,var(--glow),transparent 60%),0 0 70px color-mix(in oklch,var(--glow),transparent 75%);
}

.cle-06__phosphor {
  text-shadow: 0 0 0 oklch(0.72 0.19 310 / 0),0 0 0 oklch(0.72 0.19 310 / 0),0 0 0 oklch(0.72 0.19 310 / 0),0 0 0 oklch(0.72 0.19 310 / 0);
  transition: text-shadow .3s,color .3s;
}

.cle-06__phosphor:hover,
.cle-06__phosphor:focus-visible {
  color: oklch(0.98 0.01 310);
  text-shadow: 0 0 4px color-mix(in oklch,var(--glow2),transparent 15%),0 0 12px color-mix(in oklch,var(--glow2),transparent 25%),0 0 32px color-mix(in oklch,var(--glow2),transparent 45%),0 0 80px color-mix(in oklch,var(--glow2),transparent 60%);
}

.cle-06__aura {
  isolation: isolate;
  transition: color .4s;
}

.cle-06__aura::after {
  content: attr(data-text);
  position: absolute;
  inset: 0;
  z-index: -1;
  color: var(--glow);
  filter: blur(14px);
  opacity: 0;
  scale: 1;
  transition: opacity .4s,scale .4s;
  pointer-events: none;
}

.cle-06__aura:hover,
.cle-06__aura:focus-visible {
  color: oklch(0.97 0.02 190);
}

.cle-06__aura:hover::after,
.cle-06__aura:focus-visible::after {
  opacity: .95;
  scale: 1.05;
}

@media (prefers-reduced-motion: reduce) {
  .cle-06 * {
    transition-duration: .01s !important;
  }
}
```
