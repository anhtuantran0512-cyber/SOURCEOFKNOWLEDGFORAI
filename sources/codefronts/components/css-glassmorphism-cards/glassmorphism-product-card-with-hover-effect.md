---
source: "codefronts"
url: "https://codefronts.com/components/css-glassmorphism-cards/glassmorphism-product-card-with-hover-effect/"
title: "Glassmorphism Product Card with Hover Effect"
section: "components"
category: "css-glassmorphism-cards"
category_name: "CSS Glassmorphism Cards"
description: "Two shop-ready cards: a sneaker that levitates out of its glass frame (drop-shadow doing the physics) and rotates on hover, and a headphones card whose…"
has_js: "false"
---

Here's a working CSS Glassmorphism Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Product Card with Hover Effect
Source: https://codefronts.com/components/css-glassmorphism-cards/glassmorphism-product-card-with-hover-effect/

Two shop-ready cards: a sneaker that levitates out of its glass frame (drop-shadow doing the physics) and rotates on hover, and a headphones card whose frosted “quick add” tray slides up over the photo — the two hover patterns every store page asks for.
## HTML
```html
<div class="glz-03-group">
<link href="https://fonts.googleapis.com/css2?family=Archivo:ital,wght@0,400..900;1,400..900&display=swap" rel="stylesheet">
<section class="glz-03a" aria-label="Glassmorphism sneaker product card demo">
  <article class="glz-03a__card">
    <div class="glz-03a__hero">
      <img class="glz-03a__shoe" src="https://images.unsplash.com/photo-1542291026-7eec264c27ff?q=80&w=760&auto=format&fit=crop" alt="Crimson Court One sneaker, red and black colourway" loading="lazy">
      <span class="glz-03a__badge">New drop</span>
    </div>
    <h3 class="glz-03a__name">Crimson Court One</h3>
    <p class="glz-03a__meta"><span aria-label="Rated 4.9 out of 5">★ 4.9</span> · 2.1k reviews</p>
    <div class="glz-03a__swatches" role="radiogroup" aria-label="Colourway">
      <label style="--c:oklch(0.55 0.22 25)"><input type="radio" name="glz-03a-c" checked><span class="glz-03a__sr">Crimson</span></label>
      <label style="--c:oklch(0.3 0.02 260)"><input type="radio" name="glz-03a-c"><span class="glz-03a__sr">Onyx</span></label>
      <label style="--c:oklch(0.85 0.06 90)"><input type="radio" name="glz-03a-c"><span class="glz-03a__sr">Bone</span></label>
    </div>
    <div class="glz-03a__row"><p class="glz-03a__price">$149</p><button type="button" class="glz-03a__cta">Add to cart</button></div>
  </article>
</section>
<link href="https://fonts.googleapis.com/css2?family=Archivo:ital,wght@0,400..900;1,400..900&display=swap" rel="stylesheet">
<section class="glz-03b" aria-label="Product card with slide-up quick add tray">
  <article class="glz-03b__card">
    <div class="glz-03b__media">
      <img src="https://images.unsplash.com/photo-1505740420928-5e560c06d30e?q=80&w=760&auto=format&fit=crop" alt="Studio wireless headphones on a yellow background" loading="lazy">
      <button type="button" class="glz-03b__wish" aria-label="Save to wishlist">♡</button>
      <div class="glz-03b__tray">
        <div class="glz-03b__sizes" role="radiogroup" aria-label="Finish">
          <label><input type="radio" name="glz-03b-f" checked><span>Slate</span></label>
          <label><input type="radio" name="glz-03b-f"><span>Sand</span></label>
        </div>
        <button type="button" class="glz-03b__add">Quick add — $229</button>
      </div>
    </div>
    <div class="glz-03b__body">
      <h3>Aria Studio ANC</h3>
      <p>Over-ear · 40h battery · USB-C</p>
      <span class="glz-03b__stock">● In stock</span>
    </div>
  </article>
</section>
</div>
```
## CSS
```css
.glz-03-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.glz-03-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.glz-03a,
.glz-03a *,
.glz-03a *::before,
.glz-03a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.glz-03a {
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 110px 24px 48px;
  background: #0c0a12;
  font-family: 'Archivo',system-ui,sans-serif;
}

.glz-03a::before {
  content: "";
  position: absolute;
  width: 60vmin;
  height: 60vmin;
  border-radius: 50%;
  background: radial-gradient(circle,oklch(0.6 0.24 25),transparent 70%);
  top: -12%;
  right: 8%;
  filter: blur(50px);
  opacity: .8;
}

.glz-03a::after {
  content: "";
  position: absolute;
  width: 44vmin;
  height: 44vmin;
  border-radius: 50%;
  background: radial-gradient(circle,oklch(0.55 0.2 300),transparent 70%);
  bottom: -8%;
  left: 6%;
  filter: blur(60px);
  opacity: .7;
}

.glz-03a__card {
  position: relative;
  z-index: 1;
  width: min(330px,100%);
  border-radius: 26px;
  padding: 26px;
  color: #f4f2f8;
  background: linear-gradient(160deg,rgba(255,255,255,.14),rgba(255,255,255,.05));
  backdrop-filter: blur(22px) saturate(170%);
  -webkit-backdrop-filter: blur(22px) saturate(170%);
  border: 1px solid rgba(255,255,255,.2);
  box-shadow: 0 30px 60px -22px rgba(0,0,0,.7),inset 0 1px 0 rgba(255,255,255,.22);
}

.glz-03a__hero {
  position: relative;
  aspect-ratio: 19/13;
  margin: -70px -8px 24px;
  transition: transform .55s cubic-bezier(.2,.8,.25,1.2);
}

.glz-03a__card:hover .glz-03a__hero {
  transform: translateY(-6px);
}

.glz-03a__shoe {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 20px;
  transform: rotate(-6deg);
  transform-origin: center;
  filter: drop-shadow(0 36px 24px rgba(4,6,16,.6)) saturate(1.15);
  transition: transform .55s cubic-bezier(.2,.8,.25,1.2),filter .55s ease;
}

.glz-03a__card:hover .glz-03a__shoe {
  transform: rotate(-2deg) scale(1.03);
  filter: drop-shadow(0 52px 30px rgba(4,6,16,.65)) saturate(1.25);
}

.glz-03a__badge {
  position: absolute;
  bottom: 14px;
  left: 16px;
  z-index: 2;
  font-size: 10px;
  font-weight: 800;
  letter-spacing: .2em;
  text-transform: uppercase;
  padding: 6px 11px;
  border-radius: 99px;
  background: oklch(0.62 0.24 25);
  color: #fff;
  box-shadow: 0 6px 14px -4px rgba(0,0,0,.4);
}

.glz-03a__name {
  font-size: 22px;
  font-weight: 800;
  letter-spacing: -.01em;
  margin-top: 6px;
}

.glz-03a__meta {
  font-size: 12.5px;
  color: rgba(244,242,248,.6);
  margin-top: 5px;
}

.glz-03a__meta span {
  color: oklch(0.85 0.14 85);
}

.glz-03a__swatches {
  display: flex;
  gap: 10px;
  margin-top: 16px;
}

.glz-03a__swatches label {
  width: 26px;
  height: 26px;
  border-radius: 50%;
  background: var(--c);
  border: 2px solid rgba(255,255,255,.35);
  cursor: pointer;
  position: relative;
  transition: transform .2s ease;
}

.glz-03a__swatches label:hover {
  transform: scale(1.12);
}

.glz-03a__swatches input {
  position: absolute;
  inset: 0;
  opacity: 0;
  cursor: pointer;
}

.glz-03a__swatches label:has(input:checked) {
  outline: 2px solid #fff;
  outline-offset: 3px;
}

.glz-03a__swatches label:has(input:focus-visible) {
  outline: 2px dashed #fff;
  outline-offset: 3px;
}

.glz-03a__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.glz-03a__row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 22px;
}

.glz-03a__price {
  font-size: 26px;
  font-weight: 900;
  letter-spacing: -.02em;
}

.glz-03a__cta {
  padding: 13px 20px;
  border: none;
  border-radius: 13px;
  background: #fff;
  color: #14101e;
  font: 800 13.5px 'Archivo',sans-serif;
  letter-spacing: .02em;
  cursor: pointer;
  transition: transform .2s ease,box-shadow .2s ease;
}

.glz-03a__cta:hover {
  transform: translateY(-2px);
  box-shadow: 0 14px 26px -10px rgba(255,255,255,.45);
}

.glz-03a__cta:focus-visible {
  outline: 2px solid oklch(0.7 0.2 25);
  outline-offset: 3px;
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-03a__card {
    background: rgba(24,20,34,.93);
  }
}

@media (prefers-reduced-motion: reduce) {
  .glz-03a__shoe,
    .glz-03a__swatches label,
    .glz-03a__cta {
    transition: none;
  }
}

.glz-03b,
.glz-03b *,
.glz-03b *::before,
.glz-03b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.glz-03b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(130% 100% at 80% 0%,oklch(0.85 0.12 85),transparent 55%),radial-gradient(120% 100% at 10% 100%,oklch(0.78 0.11 250),transparent 60%),#efece6;
  font-family: 'Archivo',system-ui,sans-serif;
}

.glz-03b__card {
  width: min(330px,100%);
  border-radius: 24px;
  overflow: hidden;
  background: linear-gradient(160deg,rgba(255,255,255,.6),rgba(255,255,255,.32));
  backdrop-filter: blur(18px) saturate(160%);
  -webkit-backdrop-filter: blur(18px) saturate(160%);
  border: 1px solid rgba(255,255,255,.8);
  box-shadow: 0 28px 56px -24px rgba(70,60,30,.5),inset 0 1px 0 rgba(255,255,255,.9);
  transition: transform .35s ease,box-shadow .35s ease;
}

.glz-03b__card:hover {
  transform: translateY(-6px);
  box-shadow: 0 40px 70px -26px rgba(70,60,30,.55),inset 0 1px 0 rgba(255,255,255,.9);
}

.glz-03b__media {
  position: relative;
  aspect-ratio: 1/0.86;
  overflow: hidden;
  background: linear-gradient(140deg,#e8c65a,#d9a13d);
}

.glz-03b__media img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform .6s ease;
}

.glz-03b__card:hover .glz-03b__media img {
  transform: scale(1.06);
}

.glz-03b__wish {
  position: absolute;
  top: 12px;
  right: 12px;
  width: 38px;
  height: 38px;
  border-radius: 50%;
  border: 1px solid rgba(255,255,255,.7);
  background: rgba(255,255,255,.4);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  color: #2c2416;
  font-size: 17px;
  cursor: pointer;
  transition: background .25s ease,transform .2s ease;
}

.glz-03b__wish:hover {
  background: rgba(255,255,255,.75);
  transform: scale(1.08);
}

.glz-03b__wish:focus-visible {
  outline: 2px solid #2c2416;
  outline-offset: 2px;
}

.glz-03b__tray {
  position: absolute;
  inset: auto 10px 10px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  padding: 14px;
  border-radius: 16px;
  background: rgba(28,24,16,.55);
  backdrop-filter: blur(14px) saturate(150%);
  -webkit-backdrop-filter: blur(14px) saturate(150%);
  border: 1px solid rgba(255,255,255,.25);
  transform: translateY(calc(100% + 12px));
  transition: transform .45s cubic-bezier(.2,.8,.25,1.05);
}

.glz-03b__card:hover .glz-03b__tray,
.glz-03b__card:focus-within .glz-03b__tray {
  transform: none;
}

.glz-03b__sizes {
  display: flex;
  gap: 8px;
}

.glz-03b__sizes label {
  position: relative;
  flex: 1;
}

.glz-03b__sizes input {
  position: absolute;
  inset: 0;
  opacity: 0;
  cursor: pointer;
}

.glz-03b__sizes span {
  display: block;
  text-align: center;
  padding: 8px 0;
  border-radius: 9px;
  font-size: 12px;
  font-weight: 600;
  color: #fff;
  border: 1px solid rgba(255,255,255,.3);
  transition: background .2s ease;
}

.glz-03b__sizes label:has(input:checked) span {
  background: rgba(255,255,255,.92);
  color: #221c10;
  border-color: transparent;
}

.glz-03b__sizes label:has(input:focus-visible) span {
  outline: 2px solid #fff;
  outline-offset: 2px;
}

.glz-03b__add {
  padding: 12px;
  border: none;
  border-radius: 11px;
  background: oklch(0.8 0.15 85);
  color: #241c06;
  font: 800 13px 'Archivo',sans-serif;
  cursor: pointer;
  transition: filter .2s ease;
}

.glz-03b__add:hover {
  filter: brightness(1.08);
}

.glz-03b__add:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
}

.glz-03b__body {
  padding: 18px 20px 20px;
  color: #241d10;
}

.glz-03b__body h3 {
  font-size: 18px;
  font-weight: 800;
}

.glz-03b__body p {
  font-size: 12.5px;
  color: rgba(36,29,16,.6);
  margin-top: 4px;
}

.glz-03b__stock {
  display: inline-block;
  margin-top: 10px;
  font-size: 11px;
  font-weight: 700;
  color: oklch(0.55 0.16 155);
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-03b__card {
    background: rgba(255,255,255,.93);
  }

  .glz-03b__tray {
    background: rgba(28,24,16,.88);
  }
}

@media (prefers-reduced-motion: reduce) {
  .glz-03b__card,
    .glz-03b__media img,
    .glz-03b__tray {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the sneaker photo is translated/rotated out of the card (overflow stays visible) with a silhouette-hugging drop-shadow(); hover re-poses it. */

/* No JavaScript — the frosted tray slides up on card :hover AND :focus-within, so tabbing into the finish picker or the add button reveals it for keyboard users too. */
```
