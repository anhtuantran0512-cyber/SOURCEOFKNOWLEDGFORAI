---
source: "codefronts"
url: "https://codefronts.com/components/css-glassmorphism-cards/glassmorphism-card-with-gradient-border-blur/"
title: "Glassmorphism Card with Gradient Border Blur"
section: "components"
category: "css-glassmorphism-cards"
category_name: "CSS Glassmorphism Cards"
description: "The two canonical gradient-border constructions, side by side on one page: the double-background trick (opaque-ish padding-box fill under a gradient…"
has_js: "false"
---

Here's a working CSS Glassmorphism Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Card with Gradient Border Blur
Source: https://codefronts.com/components/css-glassmorphism-cards/glassmorphism-card-with-gradient-border-blur/

The two canonical gradient-border constructions, side by side on one page: the double-background trick (opaque-ish padding-box fill under a gradient border-box) with a blurred duplicate glow floating beneath, and the mask-composite hairline — a true 1px gradient ring on fully transparent glass, plus an iridescent frosted-edge treatment.
## HTML
```html
<div class="glz-25-group">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="glz-25a" aria-label="Gradient border card with blurred glow">
  <article class="glz-25a__card">
    <span class="glz-25a__ic" aria-hidden="true">✺</span>
    <h3>Prism Tier</h3>
    <p>The border gradient and the glow under the card are the same paint — one is just blurred 26px and pushed behind.</p>
    <div class="glz-25a__meta"><span>Construction A</span><b>padding-box / border-box</b></div>
  </article>
</section>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="glz-25b" aria-label="Hairline gradient ring on transparent glass">
  <article class="glz-25b__card">
    <span class="glz-25b__badge">Construction B</span>
    <h3>1px of iridescence</h3>
    <p>The centre stays fully transparent — the frost keeps sampling the colours drifting behind, and only a masked hairline carries the gradient.</p>
    <div class="glz-25b__foot"><b>mask-composite: exclude</b><span>core untouched</span></div>
  </article>
</section>
</div>
```
## CSS
```css
.glz-25-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.glz-25-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.glz-25a,
.glz-25a *,
.glz-25a *::before,
.glz-25a *::after {
  box-sizing: border-box;
  margin: 0;
}

.glz-25a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(110% 100% at 50% 0%,#12162a,#0a0c16 60%);
  font-family: 'Space Grotesk',system-ui,sans-serif;
}

.glz-25a__card {
  position: relative;
  width: min(350px,100%);
  padding: 32px 30px;
  border-radius: 24px;
  color: #eef1fd;
  border: 1.5px solid transparent;
  background: linear-gradient(rgba(19,24,42,.9),rgba(19,24,42,.9)) padding-box,linear-gradient(135deg,oklch(0.83 0.11 220),oklch(0.75 0.15 290),oklch(0.8 0.13 350)) border-box;
  box-shadow: 0 30px 60px -26px rgba(0,0,0,.85),inset 0 1px 0 rgba(255,255,255,.14);
}

.glz-25a__card::before {
  content: "";
  position: absolute;
  inset: 8% -4% -6%;
  z-index: -1;
  border-radius: inherit;
  background: linear-gradient(135deg,oklch(0.83 0.11 220),oklch(0.75 0.15 290),oklch(0.8 0.13 350));
  filter: blur(28px);
  opacity: .4;
}

.glz-25a__ic {
  width: 46px;
  height: 46px;
  display: grid;
  place-items: center;
  font-size: 20px;
  border-radius: 15px;
  color: #0d1220;
  background: linear-gradient(135deg,oklch(0.83 0.11 220),oklch(0.8 0.13 350));
}

.glz-25a__card h3 {
  margin-top: 18px;
  font-size: 22px;
  font-weight: 600;
  letter-spacing: -.02em;
}

.glz-25a__card p {
  margin-top: 10px;
  font-size: 13.5px;
  line-height: 1.65;
  color: rgba(238,241,253,.62);
  text-wrap: pretty;
}

.glz-25a__meta {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  margin-top: 22px;
  padding-top: 16px;
  border-top: 1px solid rgba(255,255,255,.12);
  font-size: 11px;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: rgba(238,241,253,.45);
}

.glz-25a__meta b {
  font-size: 11.5px;
  color: oklch(0.83 0.11 220);
  letter-spacing: .04em;
  text-transform: none;
}

.glz-25b,
.glz-25b *,
.glz-25b *::before,
.glz-25b *::after {
  box-sizing: border-box;
  margin: 0;
}

.glz-25b {
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #0b0a14;
  font-family: 'Space Grotesk',system-ui,sans-serif;
}

.glz-25b::before,
.glz-25b::after {
  content: "";
  position: absolute;
  width: 52vmin;
  height: 52vmin;
  border-radius: 50%;
  filter: blur(80px);
  animation: glz-25b-drift 18s ease-in-out infinite alternate;
}

.glz-25b::before {
  background: oklch(0.6 0.21 310/.75);
  top: -10%;
  left: 6%;
}

.glz-25b::after {
  background: oklch(0.7 0.16 180/.65);
  bottom: -12%;
  right: 4%;
  animation-delay: -9s;
}

.glz-25b__card {
  position: relative;
  z-index: 1;
  width: min(360px,100%);
  padding: 32px 30px;
  border-radius: 24px;
  color: #f2effb;
  background: rgba(255,255,255,.06);
  backdrop-filter: blur(22px) saturate(180%);
  -webkit-backdrop-filter: blur(22px) saturate(180%);
  box-shadow: 0 30px 62px -26px rgba(0,0,0,.85),inset 0 1px 0 rgba(255,255,255,.18);
}

.glz-25b__card::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
  padding: 1px;
  background: linear-gradient(135deg,oklch(0.85 0.1 200),oklch(0.78 0.14 300) 45%,oklch(0.85 0.12 350) 80%,oklch(0.88 0.1 90));
  -webkit-mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
  mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  mask-composite: exclude;
  pointer-events: none;
}

.glz-25b__badge {
  display: inline-block;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: .22em;
  text-transform: uppercase;
  padding: 6px 11px;
  border-radius: 99px;
  color: oklch(0.85 0.1 200);
  background: oklch(0.85 0.1 200/.1);
  border: 1px solid oklch(0.85 0.1 200/.35);
}

.glz-25b__card h3 {
  margin-top: 16px;
  font-size: 22px;
  font-weight: 600;
  letter-spacing: -.02em;
}

.glz-25b__card p {
  margin-top: 10px;
  font-size: 13.5px;
  line-height: 1.65;
  color: rgba(242,239,251,.62);
  text-wrap: pretty;
}

.glz-25b__foot {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  margin-top: 22px;
  padding-top: 16px;
  border-top: 1px solid rgba(255,255,255,.12);
  font-size: 11.5px;
}

.glz-25b__foot b {
  color: oklch(0.78 0.14 300);
  font-weight: 700;
}

.glz-25b__foot span {
  color: rgba(242,239,251,.45);
  letter-spacing: .08em;
  text-transform: uppercase;
  font-size: 10px;
}

@keyframes glz-25b-drift {
  to {
    transform: translate(8vmin,-6vmin) scale(1.15);
  }
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-25b__card {
    background: rgba(20,18,34,.92);
  }
}

@media (prefers-reduced-motion: reduce) {
  .glz-25b::before,
    .glz-25b::after {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the ring is the border-box gradient showing through a transparent border; the halo is the same gradient on ::before, blurred and z-indexed behind. */

/* No JavaScript — a gradient-painted pseudo is masked down to a 1px ring (two mask layers, composite exclude), leaving the frosted core fully transparent. */
```
