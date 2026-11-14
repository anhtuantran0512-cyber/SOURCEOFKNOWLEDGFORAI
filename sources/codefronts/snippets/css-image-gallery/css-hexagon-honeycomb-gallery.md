---
source: "codefronts"
url: "https://codefronts.com/snippets/css-image-gallery/css-hexagon-honeycomb-gallery/"
title: "CSS Hexagon Honeycomb Gallery"
section: "snippets"
category: "css-image-gallery"
category_name: "CSS Image Galleries"
description: "An interlocking honeycomb where square photos are clipped into hexagons and packed into offset rows with no gaps — a dense, geometric gallery for teams,…"
has_js: "false"
---

Here's a working CSS Image Gallerie from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Hexagon Honeycomb Gallery
Source: https://codefronts.com/snippets/css-image-gallery/css-hexagon-honeycomb-gallery/

An interlocking honeycomb where square photos are clipped into hexagons and packed into offset rows with no gaps — a dense, geometric gallery for teams, portfolios and product ranges. Built entirely with clip-path.
## HTML
```html
<section class="gl-04" aria-label="Hexagon honeycomb gallery">
  <div class="gl-04__comb">
    <div class="gl-04__row">
      <a class="gl-04__hex" href="#"><img src="https://images.unsplash.com/photo-1483728642387-6c3bdd6c93e5?q=80&w=300&h=300&auto=format&fit=crop" alt="Team member portrait" loading="lazy" decoding="async"><span class="gl-04__lbl">Ava</span></a>
      <a class="gl-04__hex" href="#"><img src="https://images.unsplash.com/photo-1439853949127-fa647821eba0?q=80&w=300&h=300&auto=format&fit=crop" alt="Team member portrait" loading="lazy" decoding="async"><span class="gl-04__lbl">Liam</span></a>
      <a class="gl-04__hex" href="#"><img src="https://images.unsplash.com/photo-1524805444758-089113d48a6d?q=80&w=300&h=300&auto=format&fit=crop" alt="Team member portrait" loading="lazy" decoding="async"><span class="gl-04__lbl">Noa</span></a>
      <a class="gl-04__hex" href="#"><img src="https://images.unsplash.com/photo-1459749411175-04bf5292ceea?q=80&w=300&h=300&auto=format&fit=crop" alt="Team member portrait" loading="lazy" decoding="async"><span class="gl-04__lbl">Kai</span></a>
    </div>
    <div class="gl-04__row gl-04__row--offset">
      <a class="gl-04__hex" href="#"><img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?q=80&w=300&h=300&auto=format&fit=crop" alt="Team member portrait" loading="lazy" decoding="async"><span class="gl-04__lbl">Mia</span></a>
      <a class="gl-04__hex" href="#"><img src="https://images.unsplash.com/photo-1517336714731-489689fd1ca8?q=80&w=300&h=300&auto=format&fit=crop" alt="Team member portrait" loading="lazy" decoding="async"><span class="gl-04__lbl">Eli</span></a>
      <a class="gl-04__hex" href="#"><img src="https://images.unsplash.com/photo-1536440136628-849c177e76a1?q=80&w=300&h=300&auto=format&fit=crop" alt="Team member portrait" loading="lazy" decoding="async"><span class="gl-04__lbl">Zoe</span></a>
    </div>
    <div class="gl-04__row">
      <a class="gl-04__hex" href="#"><img src="https://images.unsplash.com/photo-1600566753086-00f18fb6b3ea?q=80&w=300&h=300&auto=format&fit=crop" alt="Team member portrait" loading="lazy" decoding="async"><span class="gl-04__lbl">Ivo</span></a>
      <a class="gl-04__hex" href="#"><img src="https://images.unsplash.com/photo-1434389677669-e08b4cac3105?q=80&w=300&h=300&auto=format&fit=crop" alt="Team member portrait" loading="lazy" decoding="async"><span class="gl-04__lbl">Ana</span></a>
      <a class="gl-04__hex" href="#"><img src="https://images.unsplash.com/photo-1503602642458-232111445657?q=80&w=300&h=300&auto=format&fit=crop" alt="Team member portrait" loading="lazy" decoding="async"><span class="gl-04__lbl">Ben</span></a>
      <a class="gl-04__hex" href="#"><img src="https://images.unsplash.com/photo-1591047139829-d91aecb6caea?q=80&w=300&h=300&auto=format&fit=crop" alt="Team member portrait" loading="lazy" decoding="async"><span class="gl-04__lbl">Uma</span></a>
    </div>
  </div>
</section>
```
## CSS
```css
.gl-04,
.gl-04 *,
.gl-04 *::before,
.gl-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gl-04 ::selection {
  background: oklch(0.65 0.18 45);
  color: #fff;
}

.gl-04 {
  --hex: 132px;
  --accent: oklch(0.62 0.19 45);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #161318;
  display: flex;
  align-items: center;
  justify-content: center;
}

.gl-04__comb {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.gl-04__row {
  display: flex;
  gap: 8px;
}

.gl-04__row+.gl-04__row {
  margin-top: calc(var(--hex) * -0.28);
}
/* Middle row auto-centres via align-items:center on .gl-04__comb.
   The row-width difference (4-hex row is one hex + one gap wider than
   3-hex row) creates the honeycomb offset for free — no margin-left
   push needed. Adding one caused a visible right-shift. */

.gl-04__hex {
  position: relative;
  width: var(--hex);
  aspect-ratio: 1/1.1547;
  clip-path: polygon(50% 0,100% 25%,100% 75%,50% 100%,0 75%,0 25%);
  background: #241f28;
  overflow: hidden;
  text-decoration: none;
  display: block;
}

.gl-04__hex img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  transform: scale(1);
  transition: transform .45s;
}

.gl-04__hex::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(160deg,color-mix(in oklch,var(--accent) 70%,transparent),transparent 60%);
  opacity: 0;
  transition: opacity .35s;
}

.gl-04__lbl {
  position: absolute;
  inset: auto 0 22% 0;
  text-align: center;
  color: #fff;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: .04em;
  z-index: 2;
  opacity: 0;
  transform: translateY(6px);
  transition: opacity .35s,transform .35s;
  text-shadow: 0 1px 4px rgba(0,0,0,.6);
}

.gl-04__hex:hover img,
.gl-04__hex:focus-visible img {
  transform: scale(1.12);
}

.gl-04__hex:hover::after,
.gl-04__hex:focus-visible::after {
  opacity: 1;
}

.gl-04__hex:hover .gl-04__lbl,
.gl-04__hex:focus-visible .gl-04__lbl {
  opacity: 1;
  transform: translateY(0);
}

.gl-04__hex:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

@media (max-width: 520px) {
  .gl-04 {
    --hex: 96px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .gl-04__hex img,
    .gl-04__hex::after,
    .gl-04__lbl {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — clip-path hexagons packed into offset rows with negative margins. */
```
