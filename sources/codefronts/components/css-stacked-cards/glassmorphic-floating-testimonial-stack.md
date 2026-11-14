---
source: "codefronts"
url: "https://codefronts.com/components/css-stacked-cards/glassmorphic-floating-testimonial-stack/"
title: "Glassmorphic Floating Testimonial Stack"
section: "components"
category: "css-stacked-cards"
category_name: "CSS Stacked Cards"
description: "An ultra-premium frosted-glass pile of testimonials floating over a vibrant gradient."
has_js: "false"
---

Here's a working CSS Stacked Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphic Floating Testimonial Stack
Source: https://codefronts.com/components/css-stacked-cards/glassmorphic-floating-testimonial-stack/

An ultra-premium frosted-glass pile of testimonials floating over a vibrant gradient. Real backdrop-filter blur, hairline white borders and depth-shadows that lift on hover — the top card rises while the pile behind it settles.
## HTML
```html
<section class="scd-03" aria-label="Glassmorphic testimonial stack">
  <div class="scd-03__pile" tabindex="0">
    <figure class="scd-03__card" style="--x:0px;--y:0px;--r:0deg">
      <blockquote>"This shipped our redesign a full sprint early. The polish is unreal."</blockquote>
      <figcaption><span class="scd-03__ava" style="background:oklch(0.7 0.18 20)">MK</span><span><b>Maya K.</b><i>Head of Design, Northwind</i></span></figcaption>
    </figure>
    <figure class="scd-03__card" style="--x:22px;--y:14px;--r:4deg">
      <blockquote>"Dependency-free and gorgeous. Our Lighthouse score didn't budge."</blockquote>
      <figcaption><span class="scd-03__ava" style="background:oklch(0.7 0.16 200)">JL</span><span><b>Jon L.</b><i>Staff Engineer, Fathom</i></span></figcaption>
    </figure>
    <figure class="scd-03__card" style="--x:-20px;--y:26px;--r:-5deg">
      <blockquote>"Clients think we hired a motion studio. It's one CSS file."</blockquote>
      <figcaption><span class="scd-03__ava" style="background:oklch(0.72 0.16 140)">RA</span><span><b>Reese A.</b><i>Founder, Studio Arc</i></span></figcaption>
    </figure>
  </div>
</section>
```
## CSS
```css
.scd-03,
.scd-03 *,
.scd-03 *::before,
.scd-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.scd-03 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background: linear-gradient(125deg,oklch(0.6 0.2 300),oklch(0.68 0.19 210),oklch(0.72 0.18 30));
  background-size: 220% 220%;
  animation: scd-03-flow 16s ease infinite;
}

.scd-03__pile {
  position: relative;
  width: min(360px,100%);
  height: 300px;
}

.scd-03__card {
  position: absolute;
  inset: 0;
  padding: 26px 24px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  border-radius: 22px;
  background: rgba(255,255,255,.16);
  backdrop-filter: blur(16px) saturate(150%);
  -webkit-backdrop-filter: blur(16px) saturate(150%);
  border: 1px solid rgba(255,255,255,.4);
  box-shadow: 0 20px 45px -22px rgba(20,10,50,.5);
  color: #fff;
  transform: translate(var(--x),var(--y)) rotate(var(--r));
  transition: transform .5s cubic-bezier(.2,.8,.2,1),box-shadow .5s;
}

.scd-03__card:nth-child(1) {
  z-index: 3;
}

.scd-03__card:nth-child(2) {
  z-index: 2;
}

.scd-03__card:nth-child(3) {
  z-index: 1;
}

.scd-03__pile:hover .scd-03__card:nth-child(1),
.scd-03__pile:focus-visible .scd-03__card:nth-child(1) {
  transform: translate(0,-14px) rotate(0);
  box-shadow: 0 34px 60px -26px rgba(20,10,50,.7);
}

.scd-03__pile:hover .scd-03__card:nth-child(2) {
  transform: translate(46px,30px) rotate(7deg);
}

.scd-03__pile:hover .scd-03__card:nth-child(3) {
  transform: translate(-44px,44px) rotate(-8deg);
}

.scd-03__card blockquote {
  font-size: 17px;
  line-height: 1.5;
  font-weight: 600;
  text-shadow: 0 1px 12px rgba(30,10,60,.35);
}

.scd-03__card figcaption {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 13px;
}

.scd-03__card figcaption b {
  display: block;
  font-weight: 700;
}

.scd-03__card figcaption i {
  font-style: normal;
  opacity: .82;
  font-size: 12px;
}

.scd-03__ava {
  width: 38px;
  height: 38px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  font-weight: 800;
  font-size: 13px;
  color: #fff;
  flex: none;
  box-shadow: inset 0 0 0 1px rgba(255,255,255,.5);
}

.scd-03__pile:focus-visible {
  outline: 3px solid rgba(255,255,255,.9);
  outline-offset: 8px;
  border-radius: 26px;
}

@keyframes scd-03-flow {
  0%,
    100% {
    background-position: 0% 50%;
  }

  50% {
    background-position: 100% 50%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .scd-03 {
    width: 100%;
    min-height: 100vh;
    animation: none;
  }

  .scd-03__card {
    transition: transform .2s;
  }
}
```

## JavaScript
```js
/* No JavaScript — backdrop-filter builds the frosted glass; :hover/:focus-visible on the pile lifts the front card and eases the others apart. */
```
