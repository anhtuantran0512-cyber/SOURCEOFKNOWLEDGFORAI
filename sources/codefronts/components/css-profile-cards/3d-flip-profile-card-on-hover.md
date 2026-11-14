---
source: "codefronts"
url: "https://codefronts.com/components/css-profile-cards/3d-flip-profile-card-on-hover/"
title: "3D Flip Profile Card on Hover"
section: "components"
category: "css-profile-cards"
category_name: "CSS Profile Cards"
description: "A card that rotates in 3D on hover to reveal a bio, quote and quick links on its back face, with a spinning conic gradient avatar ring on the front."
has_js: "false"
---

Here's a working CSS Profile Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: 3D Flip Profile Card on Hover
Source: https://codefronts.com/components/css-profile-cards/3d-flip-profile-card-on-hover/

A card that rotates in 3D on hover to reveal a bio, quote and quick links on its back face, with a spinning conic gradient avatar ring on the front.
## HTML
```html
<div class="pc-03">
  <div class="pc-03__scene">
    <div class="pc-03__flip">
      <div class="pc-03__face pc-03__front">
        <div class="pc-03__ring"><div class="pc-03__pfp">EL</div></div>
        <h3>Elena Vasquez</h3>
        <p class="pc-03__role">Motion Designer</p>
        <span class="pc-03__hint">Hover to flip &#8635;</span>
      </div>
      <div class="pc-03__face pc-03__back">
        <p class="pc-03__quote">&ldquo;Motion is meaning. Every ease curve is a decision.&rdquo;</p>
        <div class="pc-03__links">
          <a>Portfolio</a><a>Dribbble</a><a>Email</a>
        </div>
        <div class="pc-03__stats">
          <span><b>7</b> yrs</span><span><b>210</b> shots</span>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.pc-03,
.pc-03 *,
.pc-03 *::before,
.pc-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pc-03 ::selection {
  background: #ff5c8a;
  color: #fff;
}

.pc-03 {
  --front1: #1a1030;
  --front2: #3a1d6e;
  --back1: #0d2b2b;
  --back2: #0f4d4d;
  --ink: #f3f0ff;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 20px;
  background: #060510;
  color: var(--ink);
}

.pc-03__scene {
  width: 300px;
  height: 380px;
  perspective: 1400px;
}

.pc-03__flip {
  position: relative;
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
  transition: transform .9s cubic-bezier(.2,.8,.2,1);
}

.pc-03__scene:hover .pc-03__flip {
  transform: rotateY(180deg);
}

.pc-03__face {
  position: absolute;
  inset: 0;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
  border-radius: 24px;
  padding: 30px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 14px;
  text-align: center;
  border: 1px solid rgba(255,255,255,.1);
  box-shadow: 0 30px 70px -25px rgba(0,0,0,.8);
}

.pc-03__front {
  background: linear-gradient(160deg,var(--front1),var(--front2));
}

.pc-03__ring {
  width: 110px;
  height: 110px;
  border-radius: 50%;
  padding: 4px;
  background: conic-gradient(from 0deg,#ff5c8a,#ffbe5c,#5cffd4,#8a5cff,#ff5c8a);
  animation: pc-03-spin 6s linear infinite;
}

@keyframes pc-03-spin {
  to {
    transform: rotate(360deg);
  }
}

.pc-03__pfp {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  background: #1a1030;
  display: grid;
  place-items: center;
  font-weight: 800;
  font-size: 1.7rem;
}

.pc-03__front h3 {
  font-size: 1.4rem;
  font-weight: 800;
}

.pc-03__role {
  color: rgba(243,240,255,.6);
  font-size: .9rem;
}

.pc-03__hint {
  margin-top: 10px;
  font-size: .72rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: rgba(243,240,255,.4);
}

.pc-03__back {
  background: linear-gradient(160deg,var(--back1),var(--back2));
  transform: rotateY(180deg);
  gap: 20px;
}

.pc-03__quote {
  font-size: 1.05rem;
  line-height: 1.5;
  font-weight: 600;
  text-wrap: balance;
}

.pc-03__links {
  display: flex;
  flex-direction: column;
  gap: 8px;
  width: 100%;
}

.pc-03__links a {
  padding: 9px;
  border-radius: 11px;
  font-size: .82rem;
  font-weight: 600;
  cursor: pointer;
  background: rgba(255,255,255,.08);
  border: 1px solid rgba(255,255,255,.12);
  transition: background .25s,transform .2s;
}

.pc-03__links a:hover {
  background: rgba(255,255,255,.16);
  transform: translateX(3px);
}

.pc-03__stats {
  display: flex;
  gap: 20px;
  font-size: .82rem;
  color: rgba(243,240,255,.7);
}

.pc-03__stats b {
  color: #5cffd4;
}

@media (prefers-reduced-motion: reduce) {
  .pc-03__ring {
    animation: none;
  }

  .pc-03__flip {
    transition: none;
  }
}
```
