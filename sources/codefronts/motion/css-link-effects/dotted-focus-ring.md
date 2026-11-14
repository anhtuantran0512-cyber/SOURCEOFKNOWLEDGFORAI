---
source: "codefronts"
url: "https://codefronts.com/motion/css-link-effects/dotted-focus-ring/"
title: "CSS Animated Dotted Focus Ring Hover"
section: "motion"
category: "css-link-effects"
category_name: "CSS Link Effects"
description: "Focus rings that are designed, not default: a dotted outline that breathes outward as it tints (pure outline-offset animation — yes, outline animates), a…"
has_js: "false"
---

Here's a working CSS Link Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Animated Dotted Focus Ring Hover
Source: https://codefronts.com/motion/css-link-effects/dotted-focus-ring/

Focus rings that are designed, not default: a dotted outline that breathes outward as it tints (pure outline-offset animation — yes, outline animates), a marching-ants frame whose dashes circulate clockwise around the link, and a dashed halo that slowly orbits an icon button. The same states style :hover and :focus-visible, so this doubles as a focus-styling tutorial.
## HTML
```html
<section class="cle-09" aria-label="Animated dotted focus ring demo">
  <div class="cle-09__stage">
    <div class="cle-09__var"><a href="#a" class="cle-09__ring">Breathing ring</a><small class="cle-09__cap">A · outline-offset expands</small></div>
    <div class="cle-09__var"><a href="#b" class="cle-09__ants">Marching ants</a><small class="cle-09__cap">B · dashes circulate</small></div>
    <div class="cle-09__var">
      <a href="#c" class="cle-09__halo" aria-label="Open settings"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M19.1 4.9L17 7M7 17l-2.1 2.1"/></svg></a>
      <small class="cle-09__cap">C · dashed halo orbits</small>
    </div>
  </div>
</section>
```
## CSS
```css
.cle-09,
.cle-09 *,
.cle-09 *::before,
.cle-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cle-09 {
  width: 100%;
  min-height: 100vh;
  --ink: oklch(0.25 0.02 300);
  --brand: oklch(0.56 0.2 300);
  --dim: oklch(0.78 0.03 300);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.cle-09__stage {
  width: 100%;
  height: 100vh;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  gap: 48px 64px;
  border: 1px solid oklch(0.9 0.015 300);
  background: linear-gradient(165deg,oklch(0.98 0.006 300),oklch(0.95 0.015 300));
  padding: 44px 36px;
}

.cle-09__var {
  display: grid;
  gap: 16px;
  justify-items: center;
}

.cle-09__cap {
  font-size: 10.5px;
  font-weight: 600;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: oklch(0.55 0.03 300);
}

.cle-09 a {
  color: var(--ink);
  text-decoration: none;
  font-size: 16px;
  font-weight: 650;
}

.cle-09__ring {
  padding: 13px 26px;
  border-radius: 12px;
  background: oklch(1 0 0 / .7);
  outline: 2px dotted var(--dim);
  outline-offset: 3px;
  transition: outline-offset .3s cubic-bezier(.3,1.4,.4,1),outline-color .3s,color .3s;
}

.cle-09__ring:hover,
.cle-09__ring:focus-visible {
  outline-color: var(--brand);
  outline-offset: 8px;
  color: var(--brand);
}

.cle-09__ants {
  --c: var(--dim);
  padding: 13px 26px;
  background-image: repeating-linear-gradient(90deg,var(--c) 0 5px,transparent 5px 10px),repeating-linear-gradient(90deg,var(--c) 0 5px,transparent 5px 10px),repeating-linear-gradient(180deg,var(--c) 0 5px,transparent 5px 10px),repeating-linear-gradient(180deg,var(--c) 0 5px,transparent 5px 10px);
  background-size: 100% 2px,100% 2px,2px 100%,2px 100%;
  background-position: 0 0,0 100%,0 0,100% 0;
  background-repeat: no-repeat;
  transition: color .3s;
}

.cle-09__ants:hover,
.cle-09__ants:focus-visible {
  --c: var(--brand);
  color: var(--brand);
  animation: clh09-ants .9s linear infinite;
}

.cle-09__ants:focus-visible {
  outline: none;
}

@keyframes clh09-ants {
  to {
    background-position: 10px 0,-10px 100%,0 -10px,100% 10px;
  }
}

.cle-09__halo {
  position: relative;
  display: grid;
  place-items: center;
  width: 54px;
  height: 54px;
  border-radius: 50%;
  background: oklch(1 0 0 / .8);
  box-shadow: 0 8px 22px -14px oklch(0.4 0.1 300 / .6);
  transition: color .3s;
}

.cle-09__halo svg {
  width: 22px;
  height: 22px;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.8;
  stroke-linecap: round;
}

.cle-09__halo::before {
  content: "";
  position: absolute;
  inset: -7px;
  border-radius: 50%;
  border: 2px dashed var(--brand);
  opacity: 0;
  transition: opacity .3s;
  animation: clh09-orbit 9s linear infinite;
}

.cle-09__halo:hover,
.cle-09__halo:focus-visible {
  color: var(--brand);
}

.cle-09__halo:hover::before,
.cle-09__halo:focus-visible::before {
  opacity: 1;
}

.cle-09__halo:focus-visible {
  outline: none;
}

@keyframes clh09-orbit {
  to {
    rotate: 360deg;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cle-09 * {
    transition-duration: .01s !important;
    animation: none !important;
  }

  .cle-09__ants:hover {
    --c: var(--brand);
  }

  .cle-09__halo:hover::before {
    opacity: 1;
  }
}
```
