---
source: "codefronts"
url: "https://codefronts.com/snippets/css-image-gallery/css-glassmorphism-hover-cards/"
title: "CSS Glassmorphism Hover Cards"
section: "snippets"
category: "css-image-gallery"
category_name: "CSS Image Galleries"
description: "Frosted-glass image cards floating over a vivid backdrop, each lifting and brightening its blur as you hover — the glassmorphism gallery look SaaS, music and…"
has_js: "false"
---

Here's a working CSS Image Gallerie from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Glassmorphism Hover Cards
Source: https://codefronts.com/snippets/css-image-gallery/css-glassmorphism-hover-cards/

Frosted-glass image cards floating over a vivid backdrop, each lifting and brightening its blur as you hover — the glassmorphism gallery look SaaS, music and Web3 sites search for. Powered by backdrop-filter.
## HTML
```html
<section class="gl-11" aria-label="Glassmorphism hover cards gallery">
  <div class="gl-11__row">
    <article class="gl-11__card"><div class="gl-11__well"><img src="https://images.unsplash.com/photo-1483058712412-4245e9b90334?q=80&w=400&h=400&auto=format&fit=crop" alt="Tropical sunset" loading="lazy" decoding="async"></div><h3>Golden Hour</h3><p>Maldives · 2025</p></article>
    <article class="gl-11__card"><div class="gl-11__well"><img src="https://images.unsplash.com/photo-1524985069026-dd778a71c7b4?q=80&w=400&h=400&auto=format&fit=crop" alt="Northern lights" loading="lazy" decoding="async"></div><h3>Aurora</h3><p>Tromsø · 2025</p></article>
    <article class="gl-11__card"><div class="gl-11__well"><img src="https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?q=80&w=400&h=400&auto=format&fit=crop" alt="Red canyon" loading="lazy" decoding="async"></div><h3>Red Rock</h3><p>Arizona · 2024</p></article>
  </div>
</section>
```
## CSS
```css
.gl-11,
.gl-11 *,
.gl-11 *::before,
.gl-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gl-11 ::selection {
  background: rgba(255,255,255,.85);
  color: #2a1a4a;
}

.gl-11 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: radial-gradient(45% 55% at 12% 20%,oklch(0.72 0.2 25 / .95),transparent 60%), radial-gradient(45% 55% at 88% 25%,oklch(0.72 0.2 280 / .95),transparent 60%), radial-gradient(55% 65% at 55% 95%,oklch(0.76 0.19 190 / .9),transparent 60%), linear-gradient(135deg,#2a1550,#0e1230);
}

.gl-11__row {
  display: flex;
  gap: 22px;
  flex-wrap: wrap;
  justify-content: center;
  width: min(900px,100%);
}

.gl-11__card {
  position: relative;
  width: 250px;
  padding: 16px;
  border-radius: 22px;
  background: rgba(255,255,255,.14);
  -webkit-backdrop-filter: blur(16px) saturate(1.4);
  backdrop-filter: blur(16px) saturate(1.4);
  border: 1px solid rgba(255,255,255,.28);
  box-shadow: 0 24px 50px -26px rgba(0,0,0,.55),inset 0 1px 0 rgba(255,255,255,.4);
  transition: transform .4s,box-shadow .4s,border-color .4s;
}

.gl-11__card::before {
  content: "";
  position: absolute;
  top: 0;
  left: 14%;
  right: 14%;
  height: 1px;
  background: linear-gradient(90deg,transparent,rgba(255,255,255,.85),transparent);
}

.gl-11__card:hover {
  transform: translateY(-8px);
  border-color: rgba(255,255,255,.5);
  box-shadow: 0 36px 64px -26px rgba(0,0,0,.6),inset 0 1px 0 rgba(255,255,255,.55);
}

.gl-11__well {
  border-radius: 14px;
  overflow: hidden;
  border: 1px solid rgba(255,255,255,.25);
  background: rgba(255,255,255,.1);
}

.gl-11__well img {
  display: block;
  width: 100%;
  aspect-ratio: 1/1;
  object-fit: cover;
}

.gl-11__card h3 {
  margin-top: 14px;
  font-size: 18px;
  font-weight: 700;
  color: #fff;
  text-shadow: 0 1px 6px rgba(0,0,0,.25);
}

.gl-11__card p {
  margin-top: 2px;
  font-size: 13px;
  color: rgba(255,255,255,.82);
}

@media (prefers-reduced-motion: reduce) {
  .gl-11__card {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — backdrop-filter frosts the gradient scene; hover lifts the glass. */
```
