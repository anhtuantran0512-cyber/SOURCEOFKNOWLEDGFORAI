---
source: "codefronts"
url: "https://codefronts.com/components/css-glassmorphism-cards/glassmorphism-testimonial-card-codepen/"
title: "Glassmorphism Testimonial Card Codepen"
section: "components"
category: "css-glassmorphism-cards"
category_name: "CSS Glassmorphism Cards"
description: "Social proof, glass edition: a floating single-quote card with an oversized serif ligature quote, star rating and author strip — gently bobbing on a slow…"
has_js: "false"
---

Here's a working CSS Glassmorphism Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Testimonial Card Codepen
Source: https://codefronts.com/components/css-glassmorphism-cards/glassmorphism-testimonial-card-codepen/

Social proof, glass edition: a floating single-quote card with an oversized serif ligature quote, star rating and author strip — gently bobbing on a slow keyframe — and a fanned pair of overlapping mini-testimonials where the top card straightens on hover.
## HTML
```html
<div class="glz-08-group">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&family=DM+Sans:opsz,[email protected],300..800&display=swap" rel="stylesheet">
<section class="glz-08a" aria-label="Glassmorphism testimonial card demo">
  <figure class="glz-08a__card">
    <p class="glz-08a__stars" aria-label="Rated 5 out of 5 stars">★★★★★</p>
    <blockquote class="glz-08a__quote">We swapped a 40-screen design file for one link. Clients stopped asking “is this the latest version?” — that alone paid for the year.</blockquote>
    <figcaption class="glz-08a__who">
      <img src="https://images.unsplash.com/photo-1438761681033-6461ffad8d80?q=80&w=240&auto=format&fit=crop" alt="" loading="lazy">
      <span><b>Priya Anand</b><em>Design Director, Fieldnote</em></span>
      <svg viewBox="0 0 24 24" aria-label="Verified review" class="glz-08a__badge"><path d="M12 2l2.6 2.1 3.3-.4 1 3.2 3 1.5-1.5 3 1.5 3-3 1.5-1 3.2-3.3-.4L12 22l-2.6-2.3-3.3.4-1-3.2-3-1.5 1.5-3-1.5-3 3-1.5 1-3.2 3.3.4z" fill="oklch(0.75 0.14 210)"/><path d="M8.5 12.2l2.3 2.3 4.7-4.9" fill="none" stroke="#08131c" stroke-width="2" stroke-linecap="round"/></svg>
    </figcaption>
  </figure>
</section>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&family=DM+Sans:opsz,[email protected],300..800&display=swap" rel="stylesheet">
<section class="glz-08b" aria-label="Fanned testimonial cards demo">
  <div class="glz-08b__fan">
    <figure class="glz-08b__card glz-08b__card--back">
      <blockquote>“Shipped our rebrand two weeks early.”</blockquote>
      <figcaption><img src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?q=80&w=200&auto=format&fit=crop" alt="" loading="lazy"><span><b>Sam Whitmore</b><em>Founder, Arc & Pine</em></span></figcaption>
    </figure>
    <figure class="glz-08b__card glz-08b__card--front">
      <p class="glz-08b__stars" aria-label="Rated 5 out of 5 stars">★★★★★</p>
      <blockquote>“The first tool my whole team actually opened twice. Feedback lives next to the work now, not in eleven Slack threads.”</blockquote>
      <figcaption><img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?q=80&w=200&auto=format&fit=crop" alt="" loading="lazy"><span><b>Elena Marsh</b><em>Head of Product, Waveform</em></span></figcaption>
    </figure>
  </div>
  <p class="glz-08b__hint" aria-hidden="true">hover the stack</p>
</section>
</div>
```
## CSS
```css
.glz-08-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.glz-08-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.glz-08a,
.glz-08a *,
.glz-08a *::before,
.glz-08a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.glz-08a {
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #0b1220;
  font-family: 'DM Sans',system-ui,sans-serif;
}

.glz-08a::before {
  content: "";
  position: absolute;
  width: 60vmin;
  height: 60vmin;
  border-radius: 50%;
  background: oklch(0.6 0.16 230);
  filter: blur(90px);
  opacity: .5;
  top: -16%;
  right: -6%;
}

.glz-08a::after {
  content: "";
  position: absolute;
  width: 46vmin;
  height: 46vmin;
  border-radius: 50%;
  background: oklch(0.65 0.14 330);
  filter: blur(90px);
  opacity: .4;
  bottom: -14%;
  left: -4%;
}

.glz-08a__card {
  position: relative;
  z-index: 1;
  width: min(440px,100%);
  padding: 36px 34px 30px;
  border-radius: 26px;
  color: #eef3fc;
  background: linear-gradient(165deg,rgba(255,255,255,.13),rgba(255,255,255,.04));
  backdrop-filter: blur(22px) saturate(170%);
  -webkit-backdrop-filter: blur(22px) saturate(170%);
  border: 1px solid rgba(255,255,255,.2);
  box-shadow: 0 36px 72px -28px rgba(0,0,0,.8),inset 0 1px 0 rgba(255,255,255,.24);
  overflow: hidden;
  animation: glz-08a-float 6s ease-in-out infinite;
}

.glz-08a__card::before {
  content: "\201C";
  position: absolute;
  top: -24px;
  left: 12px;
  font: 400 9.5rem/1 'Playfair Display',Georgia,serif;
  color: rgba(255,255,255,.09);
  pointer-events: none;
}

.glz-08a__stars {
  font-size: 15px;
  letter-spacing: .2em;
  color: oklch(0.85 0.14 85);
}

.glz-08a__quote {
  margin-top: 16px;
  font-family: 'Playfair Display',Georgia,serif;
  font-size: clamp(18px,2.6vw,21.5px);
  line-height: 1.5;
  font-weight: 500;
  letter-spacing: .005em;
  text-wrap: pretty;
}

.glz-08a__who {
  display: flex;
  align-items: center;
  gap: 13px;
  margin-top: 24px;
  padding-top: 20px;
  border-top: 1px solid rgba(255,255,255,.14);
}

.glz-08a__who img {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  object-fit: cover;
  border: 2px solid rgba(255,255,255,.4);
  background: #233;
}

.glz-08a__who b {
  display: block;
  font-size: 14.5px;
  font-weight: 700;
}

.glz-08a__who em {
  display: block;
  font-style: normal;
  font-size: 12px;
  color: rgba(238,243,252,.55);
  margin-top: 2px;
}

.glz-08a__badge {
  width: 26px;
  height: 26px;
  margin-left: auto;
}

@keyframes glz-08a-float {
  0%,
    100% {
    transform: translateY(0);
  }

  50% {
    transform: translateY(-7px);
  }
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-08a__card {
    background: rgba(17,25,42,.94);
  }
}

@media (prefers-reduced-motion: reduce) {
  .glz-08a__card {
    animation: none;
  }
}

.glz-08b,
.glz-08b *,
.glz-08b *::before,
.glz-08b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.glz-08b {
  --r1: -4deg;
  --r2: 3deg;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 26px;
  padding: 48px 24px;
  background: linear-gradient(170deg,#f2ede4,#e7e3f2 60%,#e2ecec);
  font-family: 'DM Sans',system-ui,sans-serif;
}

.glz-08b__fan {
  position: relative;
  width: min(420px,92vw);
  min-height: 300px;
}

.glz-08b__card {
  position: absolute;
  inset: 0;
  padding: 30px 30px 24px;
  border-radius: 24px;
  color: #292235;
  background: linear-gradient(160deg,rgba(255,255,255,.66),rgba(255,255,255,.38));
  backdrop-filter: blur(18px) saturate(155%);
  -webkit-backdrop-filter: blur(18px) saturate(155%);
  border: 1px solid rgba(255,255,255,.9);
  box-shadow: 0 30px 60px -26px rgba(90,80,130,.45),inset 0 1px 0 rgba(255,255,255,.95);
  display: flex;
  flex-direction: column;
  transition: transform .5s cubic-bezier(.2,.8,.25,1.1);
}

.glz-08b__card--back {
  transform: rotate(var(--r2)) translate(7%,-9%) scale(.96);
  background: linear-gradient(160deg,oklch(0.85 0.09 300/.55),rgba(255,255,255,.3));
}

.glz-08b__card--front {
  transform: rotate(var(--r1));
}

.glz-08b__fan:hover .glz-08b__card--front {
  transform: rotate(0) translateY(-4%);
}

.glz-08b__fan:hover .glz-08b__card--back {
  transform: rotate(6deg) translate(11%,-14%) scale(.96);
}

.glz-08b__stars {
  font-size: 13.5px;
  letter-spacing: .2em;
  color: oklch(0.68 0.16 60);
}

.glz-08b__card blockquote {
  margin-top: 12px;
  font-family: 'Playfair Display',Georgia,serif;
  font-size: clamp(16.5px,2.4vw,19.5px);
  line-height: 1.45;
  font-weight: 500;
  text-wrap: pretty;
}

.glz-08b__card--back blockquote {
  font-size: 15.5px;
  opacity: .8;
}

.glz-08b__card figcaption {
  display: flex;
  align-items: center;
  gap: 11px;
  margin-top: auto;
  padding-top: 18px;
}

.glz-08b__card img {
  width: 38px;
  height: 38px;
  border-radius: 50%;
  object-fit: cover;
  border: 2px solid rgba(255,255,255,.85);
  background: #cbc7dd;
}

.glz-08b__card b {
  display: block;
  font-size: 13.5px;
  font-weight: 700;
}

.glz-08b__card em {
  display: block;
  font-style: normal;
  font-size: 11.5px;
  color: rgba(41,34,53,.55);
  margin-top: 1px;
}

.glz-08b__hint {
  font: 600 11px 'DM Sans',sans-serif;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: rgba(60,50,80,.45);
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-08b__card {
    background: rgba(255,255,255,.93);
  }
}

@media (prefers-reduced-motion: reduce) {
  .glz-08b__card {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the watermark quote is a ::before glyph, the bob is one 6s transform keyframe, removed for reduced-motion users. */

/* No JavaScript — two absolutely-stacked cards with base rotations; hovering the group re-poses both (front straightens, back fans wider). */
```
