---
source: "codefronts"
url: "https://codefronts.com/components/css-glassmorphism-cards/glassmorphism-card-with-animated-glowing-border/"
title: "Glassmorphism Card with Animated Glowing Border"
section: "components"
category: "css-glassmorphism-cards"
category_name: "CSS Glassmorphism Cards"
description: "Two energy signatures: a rotating conic border whose blurred twin bleeds glow into the page (the double-pseudo trick), and a border-beam comet — a glowing…"
has_js: "false"
---

Here's a working CSS Glassmorphism Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Card with Animated Glowing Border
Source: https://codefronts.com/components/css-glassmorphism-cards/glassmorphism-card-with-animated-glowing-border/

Two energy signatures: a rotating conic border whose blurred twin bleeds glow into the page (the double-pseudo trick), and a border-beam comet — a glowing head that orbits the card's rounded rectangle on offset-path, 2027's favourite flex.
## HTML
```html
<div class="glz-22-group">
<link href="https://fonts.googleapis.com/css2?family=Sora:[email protected]&display=swap" rel="stylesheet">
<section class="glz-22a" aria-label="Card with rotating glowing border">
  <article class="glz-22a__card">
    <span class="glz-22a__badge">PRO</span>
    <h3>Aurora Compute</h3>
    <p>Burst to 512 vCPUs when the queue spikes. Pay for the minutes, keep the glow.</p>
    <button type="button">Upgrade — $29/mo</button>
  </article>
</section>
<link href="https://fonts.googleapis.com/css2?family=Sora:[email protected]&family=JetBrains+Mono:[email protected]&display=swap" rel="stylesheet">
<section class="glz-22b" aria-label="Card with orbiting border beam">
  <article class="glz-22b__card">
    <i class="glz-22b__beam" aria-hidden="true"></i>
    <i class="glz-22b__beam glz-22b__beam--2" aria-hidden="true"></i>
    <p class="glz-22b__eyebrow">// new in v4.2</p>
    <h3>Edge Functions</h3>
    <p class="glz-22b__body">Deploy to 119 cities before your linter finishes. The beam is offset-path tracing the card's own border-box.</p>
    <code class="glz-22b__cmd">$ glass deploy --edge</code>
  </article>
</section>
</div>
```
## CSS
```css
.glz-22-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.glz-22-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.glz-22a,
.glz-22a *,
.glz-22a *::before,
.glz-22a *::after {
  box-sizing: border-box;
  margin: 0;
}

@property --glz-22a-a {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

.glz-22a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #07080d;
  font-family: 'Sora',system-ui,sans-serif;
}

.glz-22a__card {
  position: relative;
  width: min(350px,100%);
  padding: 32px 30px;
  border-radius: 24px;
  color: #edf1fb;
  text-align: left;
  background: linear-gradient(165deg,rgba(255,255,255,.09),rgba(255,255,255,.03));
  backdrop-filter: blur(20px) saturate(160%);
  -webkit-backdrop-filter: blur(20px) saturate(160%);
  box-shadow: 0 30px 60px -26px rgba(0,0,0,.9),inset 0 1px 0 rgba(255,255,255,.16);
}

.glz-22a__card::before,
.glz-22a__card::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
  padding: 1.5px;
  background: conic-gradient(from var(--glz-22a-a),oklch(0.82 0.14 200),oklch(0.72 0.18 300),oklch(0.78 0.17 350),oklch(0.82 0.14 200));
  -webkit-mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
  mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  mask-composite: exclude;
  animation: glz-22a-rot 4s linear infinite;
  pointer-events: none;
}

.glz-22a__card::after {
  filter: blur(18px);
  opacity: .55;
}

.glz-22a__badge {
  display: inline-block;
  font-size: 10px;
  font-weight: 800;
  letter-spacing: .26em;
  padding: 6px 12px;
  border-radius: 99px;
  color: #0a0c14;
  background: linear-gradient(120deg,oklch(0.82 0.14 200),oklch(0.78 0.17 330));
}

.glz-22a__card h3 {
  margin-top: 18px;
  font-size: 23px;
  font-weight: 700;
  letter-spacing: -.02em;
}

.glz-22a__card p {
  margin-top: 10px;
  font-size: 13.5px;
  line-height: 1.65;
  color: rgba(237,241,251,.6);
  text-wrap: pretty;
}

.glz-22a__card button {
  margin-top: 22px;
  width: 100%;
  padding: 14px;
  border: 1px solid rgba(255,255,255,.22);
  border-radius: 13px;
  background: rgba(255,255,255,.08);
  color: #fff;
  font: 700 14px 'Sora',sans-serif;
  cursor: pointer;
  transition: background .25s ease,transform .2s ease;
}

.glz-22a__card button:hover {
  background: rgba(255,255,255,.16);
  transform: translateY(-2px);
}

.glz-22a__card button:focus-visible {
  outline: 2px solid oklch(0.82 0.14 200);
  outline-offset: 3px;
}

@keyframes glz-22a-rot {
  to {
    --glz-22a-a: 360deg;
  }
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-22a__card {
    background: rgba(14,16,26,.94);
  }
}

@media (prefers-reduced-motion: reduce) {
  .glz-22a__card::before,
    .glz-22a__card::after {
    animation: none;
  }
}

.glz-22b,
.glz-22b *,
.glz-22b *::before,
.glz-22b *::after {
  box-sizing: border-box;
  margin: 0;
}

.glz-22b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  position: relative;
  overflow: hidden;
  background: radial-gradient(100% 90% at 50% 110%,#101c2e,#080b12 60%);
}

.glz-22b::before {
  content: "";
  position: absolute;
  inset: 0;
  background: radial-gradient(40% 34% at 76% 20%,oklch(0.6 0.15 230/.35),transparent 70%);
}

.glz-22b__card {
  position: relative;
  z-index: 1;
  width: min(370px,100%);
  padding: 30px;
  border-radius: 22px;
  color: #e9f2fd;
  font-family: 'Sora',system-ui,sans-serif;
  background: linear-gradient(165deg,rgba(255,255,255,.1),rgba(255,255,255,.03));
  backdrop-filter: blur(20px) saturate(165%);
  -webkit-backdrop-filter: blur(20px) saturate(165%);
  border: 1px solid rgba(150,190,255,.22);
  box-shadow: 0 30px 62px -26px rgba(0,0,0,.9),inset 0 1px 0 rgba(255,255,255,.18);
}

.glz-22b__beam {
  position: absolute;
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: oklch(0.85 0.14 220);
  box-shadow: 0 0 12px 3px oklch(0.85 0.14 220/.9),0 0 34px 10px oklch(0.75 0.16 260/.45);
  offset-path: border-box;
  offset-distance: 0%;
  animation: glz-22b-orbit 5.5s linear infinite;
  pointer-events: none;
}

.glz-22b__beam--2 {
  background: oklch(0.8 0.17 320);
  box-shadow: 0 0 12px 3px oklch(0.8 0.17 320/.9),0 0 34px 10px oklch(0.7 0.19 330/.45);
  animation-delay: -2.75s;
}

@supports not (offset-path: border-box) {
  .glz-22b__beam {
    offset-path: inset(0 round 22px);
  }
}

.glz-22b__eyebrow {
  font: 600 11px 'JetBrains Mono',monospace;
  letter-spacing: .08em;
  color: oklch(0.8 0.13 220);
}

.glz-22b__card h3 {
  margin-top: 12px;
  font-size: 24px;
  font-weight: 700;
  letter-spacing: -.02em;
}

.glz-22b__body {
  margin-top: 10px;
  font-size: 13.5px;
  line-height: 1.65;
  color: rgba(233,242,253,.6);
  text-wrap: pretty;
}

.glz-22b__cmd {
  display: block;
  margin-top: 20px;
  padding: 13px 16px;
  border-radius: 12px;
  font: 600 12.5px 'JetBrains Mono',monospace;
  color: oklch(0.87 0.12 160);
  background: rgba(6,10,18,.6);
  border: 1px solid rgba(150,190,255,.18);
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-22b__card {
    background: rgba(13,19,32,.94);
  }
}

@keyframes glz-22b-orbit {
  to {
    offset-distance: 100%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .glz-22b__beam {
    animation: none;
    opacity: .5;
  }
}
```

## JavaScript
```js
/* No JavaScript — one @property angle rotates two identical conic pseudos: the crisp masked 1.5px ring, and its blurred twin providing the halo. */

/* No JavaScript — two glowing dots ride offset-path:border-box (offset-distance 0→100%), a half-cycle apart; the browser rounds the corners for free. */
```
