---
source: "codefronts"
url: "https://codefronts.com/components/css-glassmorphism-cards/glassmorphism-user-profile-card-html-css/"
title: "Glassmorphism User Profile Card HTML CSS"
section: "components"
category: "css-glassmorphism-cards"
category_name: "CSS Glassmorphism Cards"
description: "Two people-cards: a centred profile with a slow-spinning conic avatar ring, stat row and a follow button that fills on hover, and a cover-photo ID card where…"
has_js: "false"
---

Here's a working CSS Glassmorphism Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism User Profile Card HTML CSS
Source: https://codefronts.com/components/css-glassmorphism-cards/glassmorphism-user-profile-card-html-css/

Two people-cards: a centred profile with a slow-spinning conic avatar ring, stat row and a follow button that fills on hover, and a cover-photo ID card where the avatar overlaps the banner and skill chips wrap beneath — the two dominant profile layouts on the web.
## HTML
```html
<div class="glz-07-group">
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,[email protected],300..800&display=swap" rel="stylesheet">
<section class="glz-07a" aria-label="Glassmorphism user profile card demo">
  <article class="glz-07a__card">
    <div class="glz-07a__avatar"><img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?q=80&w=320&auto=format&fit=crop" alt="Portrait of Maya Okafor" loading="lazy"></div>
    <h3 class="glz-07a__name">Maya Okafor</h3>
    <p class="glz-07a__role">Product Designer · Toronto</p>
    <p class="glz-07a__bio">Designing calm interfaces for loud problems. Previously at Linear-ish startups.</p>
    <dl class="glz-07a__stats">
      <div><dt>Shots</dt><dd>214</dd></div>
      <div><dt>Followers</dt><dd>18.2k</dd></div>
      <div><dt>Following</dt><dd>312</dd></div>
    </dl>
    <div class="glz-07a__actions"><button type="button" class="glz-07a__follow">Follow</button><button type="button" class="glz-07a__msg" aria-label="Message Maya">✉</button></div>
  </article>
</section>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,[email protected],300..800&display=swap" rel="stylesheet">
<section class="glz-07b" aria-label="Cover photo profile card demo">
  <article class="glz-07b__card">
    <img class="glz-07b__cover" src="https://images.unsplash.com/photo-1519681393784-d120267933ba?q=80&w=760&auto=format&fit=crop" alt="" loading="lazy">
    <div class="glz-07b__body">
      <img class="glz-07b__avatar" src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=320&auto=format&fit=crop" alt="Portrait of Jonas Elm" loading="lazy">
      <div class="glz-07b__id"><h3>Jonas Elm <span class="glz-07b__ver" title="Verified" aria-label="Verified">✓</span></h3><p>Staff Frontend Engineer · Wellington</p></div>
      <div class="glz-07b__chips"><span>CSS architecture</span><span>Design systems</span><span>a11y</span><span>WebGL</span></div>
      <div class="glz-07b__foot"><span class="glz-07b__on">● Open to mentoring</span><button type="button">View profile</button></div>
    </div>
  </article>
</section>
</div>
```
## CSS
```css
.glz-07-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.glz-07-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.glz-07a,
.glz-07a *,
.glz-07a *::before,
.glz-07a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

@property --glz-07a-ring {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

.glz-07a {
  position: relative;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #0d0b16;
  font-family: 'Bricolage Grotesque',system-ui,sans-serif;
}

.glz-07a::before {
  content: "";
  position: absolute;
  width: 58vmin;
  height: 58vmin;
  border-radius: 50%;
  background: oklch(0.55 0.2 310);
  filter: blur(90px);
  opacity: .55;
  top: -12%;
  left: -4%;
}

.glz-07a::after {
  content: "";
  position: absolute;
  width: 46vmin;
  height: 46vmin;
  border-radius: 50%;
  background: oklch(0.7 0.15 170);
  filter: blur(90px);
  opacity: .4;
  bottom: -10%;
  right: -2%;
}

.glz-07a__card {
  position: relative;
  z-index: 1;
  width: min(330px,100%);
  padding: 32px 28px 28px;
  border-radius: 26px;
  text-align: center;
  color: #f0edfa;
  background: linear-gradient(165deg,rgba(255,255,255,.13),rgba(255,255,255,.04));
  backdrop-filter: blur(22px) saturate(170%);
  -webkit-backdrop-filter: blur(22px) saturate(170%);
  border: 1px solid rgba(255,255,255,.2);
  box-shadow: 0 32px 66px -26px rgba(0,0,0,.8),inset 0 1px 0 rgba(255,255,255,.24);
}

.glz-07a__avatar {
  width: 104px;
  height: 104px;
  margin: 0 auto;
  padding: 4px;
  border-radius: 50%;
  background: conic-gradient(from var(--glz-07a-ring),oklch(0.68 0.19 300),oklch(0.8 0.15 175),oklch(0.75 0.17 350),oklch(0.68 0.19 300));
  animation: glz-07a-spin 8s linear infinite;
}

.glz-07a__avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 50%;
  border: 3px solid #17131f;
  display: block;
}

.glz-07a__name {
  margin-top: 16px;
  font-size: 22px;
  font-weight: 700;
  letter-spacing: -.02em;
}

.glz-07a__role {
  margin-top: 4px;
  font-size: 12.5px;
  letter-spacing: .04em;
  color: oklch(0.8 0.12 300);
}

.glz-07a__bio {
  margin-top: 12px;
  font-size: 13.5px;
  line-height: 1.55;
  color: rgba(240,237,250,.6);
}

.glz-07a__stats {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  margin-top: 20px;
  border-block: 1px solid rgba(255,255,255,.14);
  padding: 14px 0;
}

.glz-07a__stats div+div {
  border-left: 1px solid rgba(255,255,255,.14);
}

.glz-07a__stats dt {
  font-size: 10px;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: rgba(240,237,250,.45);
}

.glz-07a__stats dd {
  margin-top: 3px;
  font-size: 17px;
  font-weight: 700;
}

.glz-07a__actions {
  display: flex;
  gap: 10px;
  margin-top: 20px;
}

.glz-07a__follow {
  flex: 1;
  padding: 13px;
  border-radius: 13px;
  border: 1.5px solid oklch(0.68 0.19 300);
  background: transparent;
  color: #f0edfa;
  font: 700 14px 'Bricolage Grotesque',sans-serif;
  cursor: pointer;
  transition: background .25s ease,color .25s ease,box-shadow .25s ease;
}

.glz-07a__follow:hover {
  background: oklch(0.68 0.19 300);
  color: #120c1c;
  box-shadow: 0 14px 30px -10px oklch(0.68 0.19 300/.8);
}

.glz-07a__msg {
  width: 48px;
  border-radius: 13px;
  border: 1px solid rgba(255,255,255,.22);
  background: rgba(255,255,255,.07);
  color: #f0edfa;
  font-size: 16px;
  cursor: pointer;
  transition: background .25s ease;
}

.glz-07a__msg:hover {
  background: rgba(255,255,255,.16);
}

.glz-07a__follow:focus-visible,
.glz-07a__msg:focus-visible {
  outline: 2px solid oklch(0.8 0.15 175);
  outline-offset: 3px;
}

@keyframes glz-07a-spin {
  to {
    --glz-07a-ring: 360deg;
  }
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-07a__card {
    background: rgba(21,17,32,.94);
  }
}

@media (prefers-reduced-motion: reduce) {
  .glz-07a__avatar {
    animation: none;
  }

  .glz-07a__follow,
    .glz-07a__msg {
    transition: none;
  }
}

.glz-07b,
.glz-07b *,
.glz-07b *::before,
.glz-07b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.glz-07b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(110% 90% at 15% 10%,oklch(0.82 0.1 250),transparent 60%),radial-gradient(100% 90% at 90% 90%,oklch(0.8 0.11 320),transparent 60%),#e9e9f2;
  font-family: 'Bricolage Grotesque',system-ui,sans-serif;
}

.glz-07b__card {
  width: min(360px,100%);
  border-radius: 26px;
  overflow: hidden;
  background: linear-gradient(165deg,rgba(255,255,255,.62),rgba(255,255,255,.34));
  backdrop-filter: blur(20px) saturate(160%);
  -webkit-backdrop-filter: blur(20px) saturate(160%);
  border: 1px solid rgba(255,255,255,.85);
  box-shadow: 0 32px 64px -28px rgba(60,60,120,.5),inset 0 1px 0 rgba(255,255,255,.95);
  transition: transform .35s ease,box-shadow .35s ease;
}

.glz-07b__card:hover {
  transform: translateY(-6px);
  box-shadow: 0 44px 80px -30px rgba(60,60,120,.55),inset 0 1px 0 rgba(255,255,255,.95);
}

.glz-07b__cover {
  width: 100%;
  height: 118px;
  object-fit: cover;
  display: block;
  background: linear-gradient(120deg,#3d4a7a,#6a4a8f);
}

.glz-07b__body {
  padding: 0 24px 24px;
  color: #242038;
}

.glz-07b__avatar {
  width: 88px;
  height: 88px;
  border-radius: 50%;
  object-fit: cover;
  display: block;
  margin-top: -44px;
  border: 4px solid rgba(255,255,255,.9);
  box-shadow: 0 12px 26px -10px rgba(36,32,56,.5);
  background: #cfd3e8;
}

.glz-07b__id h3 {
  margin-top: 12px;
  font-size: 20px;
  font-weight: 700;
  letter-spacing: -.02em;
  display: flex;
  align-items: center;
  gap: 7px;
}

.glz-07b__ver {
  width: 18px;
  height: 18px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  font-size: 10px;
  font-weight: 900;
  color: #fff;
  background: oklch(0.62 0.19 255);
}

.glz-07b__id p {
  margin-top: 4px;
  font-size: 13px;
  color: rgba(36,32,56,.6);
}

.glz-07b__chips {
  display: flex;
  flex-wrap: wrap;
  gap: 7px;
  margin-top: 16px;
}

.glz-07b__chips span {
  font-size: 11.5px;
  font-weight: 600;
  padding: 6px 11px;
  border-radius: 99px;
  color: #3a3060;
  background: rgba(255,255,255,.55);
  border: 1px solid rgba(90,80,140,.2);
}

.glz-07b__foot {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 20px;
  padding-top: 16px;
  border-top: 1px solid rgba(36,32,56,.12);
}

.glz-07b__on {
  font-size: 11.5px;
  font-weight: 700;
  color: oklch(0.55 0.16 155);
}

.glz-07b__foot button {
  padding: 11px 16px;
  border: none;
  border-radius: 12px;
  background: #242038;
  color: #f4f2fc;
  font: 700 12.5px 'Bricolage Grotesque',sans-serif;
  cursor: pointer;
  transition: transform .2s ease,box-shadow .2s ease;
}

.glz-07b__foot button:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 24px -10px rgba(36,32,56,.6);
}

.glz-07b__foot button:focus-visible {
  outline: 2px solid oklch(0.62 0.19 255);
  outline-offset: 3px;
}

@supports not ((backdrop-filter: blur(2px)) or (-webkit-backdrop-filter: blur(2px))) {
  .glz-07b__card {
    background: rgba(255,255,255,.94);
  }
}

@media (prefers-reduced-motion: reduce) {
  .glz-07b__card,
    .glz-07b__foot button {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the avatar ring is a conic gradient whose @property-registered from-angle animates; the photo itself never rotates. */

/* No JavaScript — banner + negative-margin avatar with a glass-matched border; chips wrap naturally under the identity block. */
```
