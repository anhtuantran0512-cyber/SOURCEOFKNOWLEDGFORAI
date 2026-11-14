---
source: "codefronts"
url: "https://codefronts.com/components/css-image-slider/has-shuffling-card-deck/"
title: ":has() Shuffling Card Deck"
section: "components"
category: "css-image-slider"
category_name: "CSS Image Sliders"
description: ":has() shuffling card deck slider — a fanned stack of image cards where hovering any card lifts it to the front in focus while its neighbours slide aside,…"
has_js: "false"
---

Here's a working CSS Image Slider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: :has() Shuffling Card Deck
Source: https://codefronts.com/components/css-image-slider/has-shuffling-card-deck/

:has() shuffling card deck slider — a fanned stack of image cards where hovering any card lifts it to the front in focus while its neighbours slide aside, blur, and recede. All state managed by the CSS :has() relational selector, no JavaScript, no class-toggling. The exact pattern portfolio agencies and creative studios ship on their team pages.
## HTML
```html
<div class="cis-09">
  <div class="cis-09__deck">
    <figure class="cis-09__card" tabindex="0"><img src="https://picsum.photos/seed/cis09a/500/640" alt="Portrait one"><figcaption>Atlas</figcaption></figure>
    <figure class="cis-09__card" tabindex="0"><img src="https://picsum.photos/seed/cis09b/500/640" alt="Portrait two"><figcaption>Marlow</figcaption></figure>
    <figure class="cis-09__card" tabindex="0"><img src="https://picsum.photos/seed/cis09c/500/640" alt="Portrait three"><figcaption>Vesper</figcaption></figure>
    <figure class="cis-09__card" tabindex="0"><img src="https://picsum.photos/seed/cis09d/500/640" alt="Portrait four"><figcaption>Corvo</figcaption></figure>
    <figure class="cis-09__card" tabindex="0"><img src="https://picsum.photos/seed/cis09e/500/640" alt="Portrait five"><figcaption>Wren</figcaption></figure>
  </div>
  <p class="cis-09__hint">hover a card</p>
</div>
```
## CSS
```css
.cis-09,
.cis-09 *,
.cis-09 *::before,
.cis-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cis-09 ::selection {
  background: oklch(0.85 0.15 60);
  color: #1a1204;
}

.cis-09 {
  --accent: oklch(0.82 0.14 60);
  --text: #f4efe6;
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--text);
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 30px;
  background: radial-gradient(120% 120% at 50% 30%,#191309,#0a0805);
}

.cis-09__deck {
  position: relative;
  width: 260px;
  height: 340px;
}

.cis-09__card {
  position: absolute;
  inset: 0;
  border-radius: 18px;
  overflow: hidden;
  cursor: pointer;
  border: 1px solid rgba(255,255,255,.12);
  box-shadow: 0 24px 50px -24px rgba(0,0,0,.85);
  transition: transform .5s cubic-bezier(.2,.8,.2,1),filter .4s,box-shadow .4s;
  transform-origin: bottom center;
}

.cis-09__card img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.cis-09__card figcaption {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  padding: 38px 16px 14px;
  font-size: 16px;
  font-weight: 700;
  background: linear-gradient(transparent,rgba(6,5,3,.85));
}

.cis-09__card:nth-child(1) {
  transform: rotate(-16deg) translate(-96px,14px);
}

.cis-09__card:nth-child(2) {
  transform: rotate(-8deg) translate(-48px,4px);
}

.cis-09__card:nth-child(3) {
  transform: rotate(0deg) translate(0,0);
}

.cis-09__card:nth-child(4) {
  transform: rotate(8deg) translate(48px,4px);
}

.cis-09__card:nth-child(5) {
  transform: rotate(16deg) translate(96px,14px);
}
/* :has() — recede siblings when any card is engaged */

.cis-09__deck:has(.cis-09__card:hover) .cis-09__card,
.cis-09__deck:has(.cis-09__card:focus-visible) .cis-09__card {
  filter: brightness(.6) blur(2px);
  transform: scale(.94) translateY(10px) rotate(0);
}

.cis-09__card:hover,
.cis-09__card:focus-visible {
  filter: none !important;
  transform: translateY(-26px) scale(1.08) rotate(0) !important;
  z-index: 10;
  box-shadow: 0 40px 70px -20px rgba(0,0,0,.9),0 0 0 2px var(--accent);
  outline: none;
}

.cis-09__hint {
  font: 11px ui-monospace,Menlo,monospace;
  letter-spacing: .28em;
  text-transform: uppercase;
  color: #7a6b4f;
}

@media (prefers-reduced-motion: reduce) {
  .cis-09__card {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — :has() restyles sibling cards on hover/focus. */
```
