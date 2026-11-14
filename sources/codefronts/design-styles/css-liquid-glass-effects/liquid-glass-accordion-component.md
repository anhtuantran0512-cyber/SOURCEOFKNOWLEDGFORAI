---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-liquid-glass-effects/liquid-glass-accordion-component/"
title: "Liquid Glass Accordion Component"
section: "design-styles"
category: "css-liquid-glass-effects"
category_name: "CSS Liquid Glass Effects"
description: "An FAQ accordion where every panel is a Liquid Glass card that expands with a fluid grid-rows transition — no clipping, no backdrop-filter paint jank."
has_js: "false"
---

Here's a working CSS Liquid Glass Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Liquid Glass Accordion Component
Source: https://codefronts.com/design-styles/css-liquid-glass-effects/liquid-glass-accordion-component/

An FAQ accordion where every panel is a Liquid Glass card that expands with a fluid grid-rows transition — no clipping, no backdrop-filter paint jank. Built on native details/summary so it's keyboard-operable and screen-reader friendly out of the box.
## HTML
```html
<section class="lg-16" aria-label="Liquid glass FAQ accordion">
  <div class="lg-16__list">
    <details class="lg-16__item" open><summary class="lg-16__q">What is Liquid Glass?<span class="lg-16__mk" aria-hidden="true"></span></summary><div class="lg-16__wrap"><div class="lg-16__a">A translucent material that samples and refracts what's behind it — frosted blur plus specular light and, at its richest, real SVG displacement. It's the design language Apple introduced at WWDC 2025.</div></div></details>
    <details class="lg-16__item"><summary class="lg-16__q">Is it good for performance?<span class="lg-16__mk" aria-hidden="true"></span></summary><div class="lg-16__wrap"><div class="lg-16__a">Yes, when disciplined: animate transform/opacity/filter only, cap blur radii, isolate paint with contain/isolation, and reserve boxes for zero CLS. This demo is pure CSS with no bundle.</div></div></details>
    <details class="lg-16__item"><summary class="lg-16__q">Is it accessible?<span class="lg-16__mk" aria-hidden="true"></span></summary><div class="lg-16__wrap"><div class="lg-16__a">Built on native details/summary, so keyboard toggling and disclosure semantics come free. Keep text on a solid-enough tint to hold WCAG contrast over busy backdrops.</div></div></details>
    <details class="lg-16__item"><summary class="lg-16__q">Does it work with Tailwind?<span class="lg-16__mk" aria-hidden="true"></span></summary><div class="lg-16__wrap"><div class="lg-16__a">Completely — the rules map to utilities like backdrop-blur-xl, bg-white/10, ring-1 ring-white/20 and rounded-2xl. Copy-paste, no external dependencies.</div></div></details>
  </div>
</section>
```
## CSS
```css
.lg-16,
.lg-16 *,
.lg-16 *::before,
.lg-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lg-16 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background: url('https://picsum.photos/seed/lgfaq/1100/800') center/cover fixed,#141024;
}

.lg-16__list {
  display: flex;
  flex-direction: column;
  gap: 14px;
  width: min(560px,94vw);
}

.lg-16__item {
  border-radius: 18px;
  overflow: hidden;
  background: color-mix(in oklab,white 10%,transparent);
  border: 1px solid rgba(255,255,255,.28);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.4),0 16px 34px -22px rgba(0,0,0,.6);
  backdrop-filter: blur(18px) saturate(170%);
  -webkit-backdrop-filter: blur(18px) saturate(170%);
  transition: border-color .3s;
}

.lg-16__item[open] {
  border-color: rgba(255,255,255,.5);
  will-change: transform;
}

.lg-16__q {
  list-style: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  font-size: 16px;
  font-weight: 700;
  color: #fff;
  padding: 18px 20px;
}

.lg-16__q::-webkit-details-marker {
  display: none;
}

.lg-16__q:focus-visible {
  outline: 3px solid #fff;
  outline-offset: -3px;
}

.lg-16__mk {
  position: relative;
  flex: none;
  width: 20px;
  height: 20px;
}

.lg-16__mk::before,
.lg-16__mk::after {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  width: 14px;
  height: 2px;
  background: #fff;
  transform: translate(-50%,-50%);
  transition: transform .3s;
}

.lg-16__mk::after {
  transform: translate(-50%,-50%) rotate(90deg);
}

.lg-16__item[open] .lg-16__mk::after {
  transform: translate(-50%,-50%) rotate(0);
}

.lg-16__wrap {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows .35s cubic-bezier(.4,0,.2,1);
}

.lg-16__item[open] .lg-16__wrap {
  grid-template-rows: 1fr;
}

.lg-16__a {
  overflow: hidden;
  font-size: 15px;
  line-height: 1.65;
  color: rgba(255,255,255,.9);
  padding: 0 20px;
}

.lg-16__item[open] .lg-16__a {
  padding: 0 20px 20px;
}

@media (prefers-reduced-motion: reduce) {
  .lg-16__wrap {
    transition: none;
  }

  .lg-16__mk::before,
    .lg-16__mk::after {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — native details/summary handles disclosure + keyboard; the answer animates open via a grid-template-rows 0fr→1fr transition so height:auto tweens smoothly without clipping the glass. */
```
