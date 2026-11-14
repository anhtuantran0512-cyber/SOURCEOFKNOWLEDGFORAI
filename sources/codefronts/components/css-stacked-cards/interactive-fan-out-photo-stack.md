---
source: "codefronts"
url: "https://codefronts.com/components/css-stacked-cards/interactive-fan-out-photo-stack/"
title: "Interactive Fan-Out Photo Stack"
section: "components"
category: "css-stacked-cards"
category_name: "CSS Stacked Cards"
description: "A tidy pile of photos that fans into a graceful arc on hover — like spreading a handful of prints across a table."
has_js: "false"
---

Here's a working CSS Stacked Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Interactive Fan-Out Photo Stack
Source: https://codefronts.com/components/css-stacked-cards/interactive-fan-out-photo-stack/

A tidy pile of photos that fans into a graceful arc on hover — like spreading a handful of prints across a table. Each card rotates and translates to its own place in the fan, then snaps back into a neat stack when the pointer leaves.
## HTML
```html
<section class="scd-05" aria-label="Fan-out photo stack">
  <div class="scd-05__fan">
    <a class="scd-05__card" href="#" style="--n:-2"><img src="https://picsum.photos/seed/fan-1/300/380" width="300" height="380" alt="Coastline"></a>
    <a class="scd-05__card" href="#" style="--n:-1"><img src="https://picsum.photos/seed/fan-2/300/380" width="300" height="380" alt="Old town street"></a>
    <a class="scd-05__card" href="#" style="--n:0"><img src="https://picsum.photos/seed/fan-3/300/380" width="300" height="380" alt="Mountain hut"></a>
    <a class="scd-05__card" href="#" style="--n:1"><img src="https://picsum.photos/seed/fan-4/300/380" width="300" height="380" alt="Harbour at dusk"></a>
    <a class="scd-05__card" href="#" style="--n:2"><img src="https://picsum.photos/seed/fan-5/300/380" width="300" height="380" alt="Desert dunes"></a>
  </div>
  <p class="scd-05__cap">Hover to fan · Tab to spread</p>
</section>
```
## CSS
```css
.scd-05,
.scd-05 *,
.scd-05 *::before,
.scd-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.scd-05 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 34px;
  padding: 60px 20px;
  background: #e9e4db;
}

.scd-05__fan {
  position: relative;
  width: 220px;
  height: 300px;
}

.scd-05__card {
  position: absolute;
  left: 50%;
  top: 0;
  width: 180px;
  margin-left: -90px;
  border-radius: 14px;
  overflow: hidden;
  background: #fff;
  padding: 8px 8px 22px;
  box-shadow: 0 16px 34px -20px rgba(60,40,20,.6);
  transform-origin: 50% 130%;
  transform: rotate(0deg);
  transition: transform .5s cubic-bezier(.2,.85,.2,1);
  will-change: transform;
}

.scd-05__card img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 8px;
  display: block;
  aspect-ratio: 3/4;
}

.scd-05__fan:hover .scd-05__card,
.scd-05__fan:focus-within .scd-05__card {
  transform: rotate(calc(var(--n) * 15deg)) translateY(calc(var(--n) * var(--n) * -2px));
}

.scd-05__card:nth-child(1) {
  transition-delay: 0s;
}

.scd-05__card:nth-child(2) {
  transition-delay: .04s;
}

.scd-05__card:nth-child(3) {
  transition-delay: .08s;
}

.scd-05__card:nth-child(4) {
  transition-delay: .04s;
}

.scd-05__card:nth-child(5) {
  transition-delay: 0s;
}

.scd-05__card:hover,
.scd-05__card:focus-visible {
  outline: none;
  transform: rotate(calc(var(--n) * 15deg)) translateY(-24px)!important;
  z-index: 5;
}

.scd-05__card:focus-visible {
  box-shadow: 0 0 0 3px oklch(0.6 0.17 260),0 20px 40px -18px rgba(60,40,20,.7);
}

.scd-05__cap {
  font-size: 12px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: #9a8f80;
}

@media (prefers-reduced-motion: reduce) {
  .scd-05__card {
    transition: transform .2s;
  }

  .scd-05__fan:hover .scd-05__card {
    transform: translateX(calc(var(--n) * 48px));
  }
}
```

## JavaScript
```js
/* No JavaScript — a shared low transform-origin plus a progressive per-card rotate() fans the pile out on :hover / :focus-within. */
```
