---
source: "codefronts"
url: "https://codefronts.com/components/css-profile-cards/glassmorphism-2-0-profile-card/"
title: "Glassmorphism 2.0 Profile Card"
section: "components"
category: "css-profile-cards"
category_name: "CSS Profile Cards"
description: "An evolved frosted-glass card with an ultra-thin gradient border, subtle SVG grain overlay and a drifting light orb behind lightly blurred glass."
has_js: "false"
---

Here's a working CSS Profile Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism 2.0 Profile Card
Source: https://codefronts.com/components/css-profile-cards/glassmorphism-2-0-profile-card/

An evolved frosted-glass card with an ultra-thin gradient border, subtle SVG grain overlay and a drifting light orb behind lightly blurred glass.
## HTML
```html
<div class="pc-02">
  <div class="pc-02__card">
    <div class="pc-02__noise"></div>
    <div class="pc-02__glow"></div>
    <div class="pc-02__inner">
      <div class="pc-02__top">
        <div class="pc-02__avatar"><span>NK</span></div>
        <span class="pc-02__badge">PRO</span>
      </div>
      <h3 class="pc-02__name">Noor Kapadia</h3>
      <p class="pc-02__role">Frontend Architect · Berlin</p>
      <p class="pc-02__bio">Building spatial UIs with the platform. Obsessed with depth, light and 8&nbsp;px grids.</p>
      <div class="pc-02__meta">
        <div class="pc-02__m"><strong>12k</strong><span>Followers</span></div>
        <div class="pc-02__div"></div>
        <div class="pc-02__m"><strong>340</strong><span>Posts</span></div>
        <div class="pc-02__div"></div>
        <div class="pc-02__m"><strong>98%</strong><span>Positive</span></div>
      </div>
      <div class="pc-02__actions">
        <button class="pc-02__btn">Connect</button>
        <button class="pc-02__icon" aria-label="Bookmark">&#9734;</button>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.pc-02,
.pc-02 *,
.pc-02 *::before,
.pc-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pc-02 ::selection {
  background: rgba(255,255,255,.85);
  color: #111;
}

.pc-02 {
  --ink: #f5f7ff;
  --dim: rgba(245,247,255,.6);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 20px;
  background: radial-gradient(600px 400px at 20% 10%,#3b1c7a,transparent 60%), radial-gradient(500px 500px at 90% 90%,#0e5a6b,transparent 60%), #070710;
  color: var(--ink);
}

.pc-02__card {
  position: relative;
  width: 100%;
  max-width: 340px;
  border-radius: 26px;
  padding: 1px;
  background: linear-gradient(145deg,rgba(255,255,255,.28),rgba(255,255,255,.04) 40%,transparent 70%);
  box-shadow: 0 30px 80px -30px rgba(0,0,0,.8);
  isolation: isolate;
}

.pc-02__inner {
  position: relative;
  z-index: 2;
  border-radius: 25px;
  padding: 26px;
  background: rgba(255,255,255,.06);
  -webkit-backdrop-filter: blur(8px) saturate(140%);
  backdrop-filter: blur(8px) saturate(140%);
  border: 1px solid rgba(255,255,255,.12);
  overflow: hidden;
}

.pc-02__noise {
  position: absolute;
  inset: 0;
  z-index: 1;
  border-radius: 26px;
  opacity: .5;
  mix-blend-mode: overlay;
  pointer-events: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='120'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.5'/%3E%3C/svg%3E");
}

.pc-02__glow {
  position: absolute;
  width: 180px;
  height: 180px;
  border-radius: 50%;
  top: -40px;
  right: -30px;
  z-index: 0;
  background: radial-gradient(circle,rgba(148,120,255,.55),transparent 70%);
  filter: blur(20px);
  animation: pc-02-float 7s ease-in-out infinite;
}

@keyframes pc-02-float {
  0%,
    100% {
    transform: translate(0,0);
  }

  50% {
    transform: translate(-24px,20px);
  }
}

.pc-02__top {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
}

.pc-02__avatar {
  width: 66px;
  height: 66px;
  border-radius: 20px;
  display: grid;
  place-items: center;
  font-weight: 800;
  font-size: 1.3rem;
  background: linear-gradient(145deg,#9478ff,#4cc9f0);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.4),0 8px 24px -8px #4cc9f0;
}

.pc-02__badge {
  font-size: .62rem;
  letter-spacing: .18em;
  font-weight: 800;
  padding: 5px 9px;
  border-radius: 8px;
  background: rgba(255,255,255,.14);
  border: 1px solid rgba(255,255,255,.2);
}

.pc-02__name {
  font-size: 1.35rem;
  font-weight: 800;
  margin-top: 18px;
  letter-spacing: -.01em;
}

.pc-02__role {
  color: var(--dim);
  font-size: .85rem;
  margin-top: 3px;
}

.pc-02__bio {
  font-size: .85rem;
  line-height: 1.55;
  color: rgba(245,247,255,.82);
  margin-top: 14px;
  text-wrap: balance;
}

.pc-02__meta {
  display: flex;
  align-items: center;
  gap: 14px;
  margin-top: 20px;
}

.pc-02__m {
  display: flex;
  flex-direction: column;
}

.pc-02__m strong {
  font-size: 1.1rem;
  font-weight: 800;
  font-variant-numeric: tabular-nums;
}

.pc-02__m span {
  font-size: .68rem;
  color: var(--dim);
  letter-spacing: .03em;
}

.pc-02__div {
  width: 1px;
  height: 26px;
  background: rgba(255,255,255,.14);
}

.pc-02__actions {
  display: flex;
  gap: 10px;
  margin-top: 22px;
}

.pc-02__btn {
  flex: 1;
  padding: 12px;
  border: none;
  border-radius: 13px;
  font-weight: 700;
  cursor: pointer;
  font-size: .88rem;
  background: linear-gradient(145deg,#9478ff,#6c4cff);
  color: #fff;
  box-shadow: 0 8px 22px -8px #6c4cff;
  transition: transform .2s,filter .25s;
}

.pc-02__btn:hover {
  filter: brightness(1.1);
}

.pc-02__btn:active {
  transform: scale(.97);
}

.pc-02__icon {
  width: 46px;
  border: 1px solid rgba(255,255,255,.18);
  border-radius: 13px;
  cursor: pointer;
  background: rgba(255,255,255,.06);
  color: var(--ink);
  font-size: 1.1rem;
  transition: background .25s;
}

.pc-02__icon:hover {
  background: rgba(255,255,255,.14);
}

@media (prefers-reduced-motion: reduce) {
  .pc-02 * {
    animation: none!important;
  }
}
```
