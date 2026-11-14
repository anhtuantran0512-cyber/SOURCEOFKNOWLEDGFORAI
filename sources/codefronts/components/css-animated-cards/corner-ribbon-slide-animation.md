---
source: "codefronts"
url: "https://codefronts.com/components/css-animated-cards/corner-ribbon-slide-animation/"
title: "Corner Ribbon Slide Animation"
section: "components"
category: "css-animated-cards"
category_name: "CSS Animated Cards"
description: "Corner ribbons that arrive instead of just existing: a diagonal banner sliding out of the card corner on load, folded end-tabs cut with clip-path, and a…"
has_js: "false"
---

Here's a working CSS Animated Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Corner Ribbon Slide Animation
Source: https://codefronts.com/components/css-animated-cards/corner-ribbon-slide-animation/

Corner ribbons that arrive instead of just existing: a diagonal banner sliding out of the card corner on load, folded end-tabs cut with clip-path, and a hover wiggle with a light sweep running along the fabric. Pure CSS, no images, and the ribbon text stays readable to screen readers rather than being baked into a background.
## HTML
```html
<section class="ac-23" aria-label="Corner ribbon slide animation demo">
  <div class="ac-23__stage">
    <header class="ac-23__head">
      <p class="ac-23__eyebrow">Merchandising</p>
      <h2 class="ac-23__title">Ribbons that unfurl from the corner</h2>
    </header>
    <ul class="ac-23__grid" role="list">
      <li class="ac-23__card" style="--ac-23-i:0;--ac-23-c:oklch(0.62 0.21 25)">
        <span class="ac-23__corner"><span class="ac-23__ribbon">Sale</span></span>
        <span class="ac-23__media"><img src="https://images.unsplash.com/photo-1505740420928-5e560c06d30e?q=80&w=600&auto=format&fit=crop" alt="Over-ear headphones on a plain background" loading="lazy" decoding="async" width="600" height="600"></span>
        <div class="ac-23__body">
          <h3 class="ac-23__name">Studio Over-Ear</h3>
          <p class="ac-23__price"><b>$199</b><s>$249</s></p>
        </div>
      </li>
      <li class="ac-23__card" style="--ac-23-i:1;--ac-23-c:oklch(0.68 0.18 152)">
        <span class="ac-23__corner"><span class="ac-23__ribbon">New</span></span>
        <span class="ac-23__media"><img src="https://images.unsplash.com/photo-1546868871-7041f2a55e12?q=80&w=600&auto=format&fit=crop" alt="Smartwatch with a woven band" loading="lazy" decoding="async" width="600" height="600"></span>
        <div class="ac-23__body">
          <h3 class="ac-23__name">Pace Watch S2</h3>
          <p class="ac-23__price"><b>$219</b></p>
        </div>
      </li>
      <li class="ac-23__card" style="--ac-23-i:2;--ac-23-c:oklch(0.78 0.16 82)">
        <span class="ac-23__corner"><span class="ac-23__ribbon">Limited</span></span>
        <span class="ac-23__media"><img src="https://images.unsplash.com/photo-1523275335684-37898b6baf30?q=80&w=600&auto=format&fit=crop" alt="Analogue wristwatch on a light surface" loading="lazy" decoding="async" width="600" height="600"></span>
        <div class="ac-23__body">
          <h3 class="ac-23__name">Field Watch 38</h3>
          <p class="ac-23__price"><b>$390</b></p>
        </div>
      </li>
      <li class="ac-23__card" style="--ac-23-i:3;--ac-23-c:oklch(0.58 0.19 285)">
        <span class="ac-23__corner"><span class="ac-23__ribbon">Bundle</span></span>
        <span class="ac-23__media"><img src="https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?q=80&w=600&auto=format&fit=crop" alt="Compact camera body on a table" loading="lazy" decoding="async" width="600" height="600"></span>
        <div class="ac-23__body">
          <h3 class="ac-23__name">Rangefinder M</h3>
          <p class="ac-23__price"><b>$1,180</b></p>
        </div>
      </li>
    </ul>
    <p class="ac-23__chip" aria-hidden="true">clipped corner wrapper · rotate(45deg) + diagonal translate unfurl · clip-path fold tabs · hover wiggle + sheen · real text</p>
  </div>
</section>
```
## CSS
```css
.ac-23,
.ac-23 *,
.ac-23 *::before,
.ac-23 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ac-23 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --ac-23-bg: oklch(0.97 0.006 250);
  --ac-23-card: oklch(1 0 0);
  --ac-23-ink: oklch(0.23 0.02 260);
  --ac-23-mut: oklch(0.55 0.02 260);
  --ac-23-line: oklch(0.23 0.02 260/.11);
  background: var(--ac-23-bg);
  color: var(--ac-23-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.ac-23__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(16px,2.6vw,28px);
  padding: clamp(20px,5vw,58px);
}

.ac-23__head {
  display: grid;
  justify-items: center;
  gap: 9px;
  text-align: center;
}

.ac-23__eyebrow {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: oklch(0.55 0.16 25);
}

.ac-23__title {
  font-size: clamp(23px,3.4vw,38px);
  font-weight: 650;
  line-height: 1.12;
  letter-spacing: -.03em;
  text-wrap: balance;
}

.ac-23__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(196px,1fr));
  gap: 16px;
  width: min(100%,900px);
  list-style: none;
}

.ac-23__card {
  position: relative;
  display: grid;
  border: 1px solid var(--ac-23-line);
  border-radius: 18px;
  background: var(--ac-23-card);
  box-shadow: 0 1px 2px oklch(0.23 0.02 260/.05);
  overflow: hidden;
  transition: transform .35s cubic-bezier(.16,1,.3,1),box-shadow .35s;
}

.ac-23__card:hover {
  transform: translateY(-4px);
  box-shadow: 0 22px 44px -26px oklch(0.23 0.02 260/.6);
}

.ac-23__corner {
  position: absolute;
  top: 0;
  right: 0;
  width: 124px;
  height: 124px;
  overflow: hidden;
  border-radius: 0 18px 0 0;
  z-index: 2;
  pointer-events: none;
}

.ac-23__ribbon {
  position: absolute;
  top: 26px;
  right: -44px;
  width: 186px;
  padding: 7px 0;
  rotate: 45deg;
  text-align: center;
  background: var(--ac-23-c);
  color: oklch(0.99 0 0);
  font-size: 11.5px;
  font-weight: 750;
  letter-spacing: .15em;
  text-transform: uppercase;
  box-shadow: 0 6px 16px -8px color-mix(in oklch,var(--ac-23-c) 90%,oklch(0 0 0));
  animation: ac-23-unfurl .72s cubic-bezier(.16,1,.3,1) both;
  animation-delay: calc(.3s + var(--ac-23-i,0) * 110ms);
}

@keyframes ac-23-unfurl {
  from {
    translate: 62px -62px;
    opacity: 0;
  }

  60% {
    opacity: 1;
  }

  to {
    translate: 0 0;
    opacity: 1;
  }
}

.ac-23__ribbon::before,
.ac-23__ribbon::after {
  content: '';
  position: absolute;
  top: 100%;
  width: 0;
  height: 0;
  border-style: solid;
  border-color: color-mix(in oklch,var(--ac-23-c) 70%,oklch(0 0 0)) transparent transparent;
}

.ac-23__ribbon::before {
  left: 34px;
  border-width: 7px 7px 0 0;
}

.ac-23__ribbon::after {
  right: 34px;
  border-width: 7px 0 0 7px;
}

.ac-23__card:hover .ac-23__ribbon {
  animation: ac-23-wiggle .55s cubic-bezier(.3,0,.3,1);
}

@keyframes ac-23-wiggle {
  0%,
    100% {
    rotate: 45deg;
  }

  30% {
    rotate: 43.6deg;
  }

  65% {
    rotate: 46.2deg;
  }
}

.ac-23__card:hover .ac-23__corner::after {
  content: '';
  position: absolute;
  top: 26px;
  right: -44px;
  width: 186px;
  height: 31px;
  rotate: 45deg;
  background: linear-gradient(105deg,transparent 36%,oklch(1 0 0/.5) 50%,transparent 64%);
  animation: ac-23-sheen .8s ease-out;
  pointer-events: none;
}

@keyframes ac-23-sheen {
  from {
    translate: -120px 0;
    opacity: 0;
  }

  30% {
    opacity: 1;
  }

  to {
    translate: 120px 0;
    opacity: 0;
  }
}

.ac-23__media {
  display: block;
  aspect-ratio: 1;
  background: linear-gradient(135deg,oklch(0.92 0.02 250),oklch(0.86 0.03 220));
}

.ac-23__media img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: scale .5s cubic-bezier(.16,1,.3,1);
}

.ac-23__card:hover .ac-23__media img {
  scale: 1.06;
}

.ac-23__body {
  display: grid;
  gap: 5px;
  padding: 14px 15px 17px;
}

.ac-23__name {
  font-size: 14.5px;
  font-weight: 640;
  letter-spacing: -.02em;
}

.ac-23__price {
  display: flex;
  align-items: baseline;
  gap: 8px;
  font-variant-numeric: tabular-nums;
}

.ac-23__price b {
  font-size: 16px;
  font-weight: 700;
  letter-spacing: -.025em;
}

.ac-23__price s {
  font-size: 13px;
  color: var(--ac-23-mut);
}

.ac-23__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  line-height: 1.6;
  color: var(--ac-23-mut);
  padding: 8px 15px;
  border: 1px dashed var(--ac-23-line);
  border-radius: 99px;
  text-align: center;
  max-width: min(100%,820px);
}

@media (prefers-reduced-motion: reduce) {
  .ac-23__ribbon {
    animation-duration: 1ms;
  }

  .ac-23__card:hover .ac-23__ribbon {
    animation: none;
  }

  .ac-23__card:hover .ac-23__corner::after {
    display: none;
  }

  .ac-23__card,
    .ac-23__media img {
    transition: none;
  }
}
```
