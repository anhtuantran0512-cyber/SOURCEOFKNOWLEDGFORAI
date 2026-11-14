---
source: "codefronts"
url: "https://codefronts.com/motion/css-link-effects/brutalist-block/"
title: "CSS Brutalist Block Shadow Hover Effect"
section: "motion"
category: "css-link-effects"
category_name: "CSS Link Effects"
description: "Neo-brutalism's whole physics engine is one equation: translate the box toward or away from its hard shadow."
has_js: "false"
---

Here's a working CSS Link Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Brutalist Block Shadow Hover Effect
Source: https://codefronts.com/motion/css-link-effects/brutalist-block/

Neo-brutalism's whole physics engine is one equation: translate the box toward or away from its hard shadow. Hover lifts the card off the page (shadow grows), :active slams it flat (shadow zero) — a click you can feel. Three builds: the standard lift, the inverted press-in, and a rotated double-shadow stack that swaps colors mid-hover.
## HTML
```html
<section class="cle-24" aria-label="Brutalist shadow hover demo">
  <div class="cle-24__stage">
    <div class="cle-24__var"><a href="#a" class="cle-24__lift">READ THE ZINE</a><small class="cle-24__cap">A · lift, then slam (:active)</small></div>
    <div class="cle-24__var"><a href="#b" class="cle-24__press">RSVP → ISSUE 07</a><small class="cle-24__cap">B · press-in</small></div>
    <div class="cle-24__var"><a href="#c" class="cle-24__stack">SHOP PRINTS</a><small class="cle-24__cap">C · double stack + tilt</small></div>
  </div>
</section>
```
## CSS
```css
.cle-24,
.cle-24 *,
.cle-24 *::before,
.cle-24 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cle-24 {
  width: 100%;
  min-height: 100vh;
  --blk: oklch(0.22 0.01 90);
  --yel: oklch(0.86 0.16 95);
  --pnk: oklch(0.78 0.15 5);
  --blu: oklch(0.75 0.11 230);
  font-family: ui-monospace,'Cascadia Code',Menlo,Consolas,monospace;
}

.cle-24__stage {
  width: 100%;
  height: 100vh;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  gap: 48px 56px;
  border: 1px solid oklch(0.88 0.03 90);
  background: oklch(0.955 0.02 90);
  background-image: radial-gradient(oklch(0.85 0.03 90) 1px,transparent 1px);
  background-size: 22px 22px;
  padding: 44px 36px;
}

.cle-24__var {
  display: grid;
  gap: 16px;
  justify-items: center;
}

.cle-24__cap {
  font-size: 10.5px;
  font-weight: 600;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: oklch(0.48 0.03 90);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.cle-24 a {
  display: inline-block;
  padding: 16px 26px;
  border: 3px solid var(--blk);
  color: var(--blk);
  text-decoration: none;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: .04em;
}

.cle-24 a:focus-visible {
  outline: 3px dashed var(--blk);
  outline-offset: 4px;
}

.cle-24__lift {
  background: var(--yel);
  box-shadow: 5px 5px 0 var(--blk);
  transition: translate .15s ease-out,box-shadow .15s ease-out;
}

.cle-24__lift:hover,
.cle-24__lift:focus-visible {
  translate: -3px -3px;
  box-shadow: 8px 8px 0 var(--blk);
}

.cle-24__lift:active {
  translate: 2px 2px;
  box-shadow: 0 0 0 var(--blk);
}

.cle-24__press {
  background: var(--blu);
  box-shadow: 6px 6px 0 var(--blk);
  transition: translate .15s ease-out,box-shadow .15s ease-out;
}

.cle-24__press:hover,
.cle-24__press:focus-visible {
  translate: 4px 4px;
  box-shadow: 2px 2px 0 var(--blk);
}

.cle-24__press:active {
  translate: 6px 6px;
  box-shadow: 0 0 0 var(--blk);
}

.cle-24__stack {
  background: oklch(0.97 0.01 90);
  box-shadow: 5px 5px 0 var(--pnk),10px 10px 0 var(--blk);
  transition: translate .15s ease-out,box-shadow .15s ease-out,rotate .15s ease-out,background-color .15s;
}

.cle-24__stack:hover,
.cle-24__stack:focus-visible {
  translate: -3px -3px;
  rotate: -1.2deg;
  background: var(--pnk);
  box-shadow: 7px 7px 0 var(--yel),14px 14px 0 var(--blk);
}

.cle-24__stack:active {
  translate: 4px 4px;
  rotate: 0deg;
  box-shadow: 0 0 0 var(--yel),0 0 0 var(--blk);
}

@media (prefers-reduced-motion: reduce) {
  .cle-24 * {
    transition-duration: .01s !important;
  }
}
```
