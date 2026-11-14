---
source: "codefronts"
url: "https://codefronts.com/components/css-profile-cards/social-icons-slide-up-overlay-card/"
title: "Social Icons Slide-up Overlay Card"
section: "components"
category: "css-profile-cards"
category_name: "CSS Profile Cards"
description: "A portrait card whose avatar fills the frame, with social icons that stagger up from the bottom edge and a gentle image zoom on hover."
has_js: "false"
---

Here's a working CSS Profile Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Social Icons Slide-up Overlay Card
Source: https://codefronts.com/components/css-profile-cards/social-icons-slide-up-overlay-card/

A portrait card whose avatar fills the frame, with social icons that stagger up from the bottom edge and a gentle image zoom on hover.
## HTML
```html
<div class="pc-04">
  <div class="pc-04__card">
    <div class="pc-04__portrait">
      <div class="pc-04__pfp">JM</div>
      <div class="pc-04__grad"></div>
      <div class="pc-04__overlay">
        <a class="pc-04__soc" style="--i:0" aria-label="Twitter">&#120143;</a>
        <a class="pc-04__soc" style="--i:1" aria-label="GitHub">&#9670;</a>
        <a class="pc-04__soc" style="--i:2" aria-label="Site">&#8734;</a>
        <a class="pc-04__soc" style="--i:3" aria-label="Mail">&#9993;</a>
      </div>
    </div>
    <div class="pc-04__body">
      <h3>Jonas Meyer</h3>
      <p>Creative Technologist</p>
    </div>
  </div>
</div>
```
## CSS
```css
.pc-04,
.pc-04 *,
.pc-04 *::before,
.pc-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pc-04 ::selection {
  background: #ff7a45;
  color: #fff;
}

.pc-04 {
  --ink: #fff;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 20px;
  background: #0d0d12;
  color: var(--ink);
}

.pc-04__card {
  width: 290px;
  border-radius: 24px;
  overflow: hidden;
  background: #15151d;
  border: 1px solid rgba(255,255,255,.08);
  box-shadow: 0 30px 70px -28px rgba(0,0,0,.8);
}

.pc-04__portrait {
  position: relative;
  aspect-ratio: 1;
  overflow: hidden;
}

.pc-04__pfp {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  font-size: 4rem;
  font-weight: 800;
  letter-spacing: .02em;
  color: rgba(255,255,255,.92);
  background: radial-gradient(circle at 30% 30%,#ff7a45,transparent 55%), radial-gradient(circle at 75% 70%,#a445ff,transparent 55%), linear-gradient(145deg,#2a1840,#401f2f);
  transition: transform .6s cubic-bezier(.2,.8,.2,1);
}

.pc-04__card:hover .pc-04__pfp {
  transform: scale(1.08);
}

.pc-04__grad {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top,rgba(13,13,18,.95) 0%,transparent 55%);
}

.pc-04__overlay {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: flex-end;
  justify-content: center;
  gap: 12px;
  padding-bottom: 24px;
}

.pc-04__soc {
  width: 44px;
  height: 44px;
  border-radius: 13px;
  display: grid;
  place-items: center;
  cursor: pointer;
  font-size: 1.05rem;
  background: rgba(255,255,255,.12);
  border: 1px solid rgba(255,255,255,.18);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
  transform: translateY(80px);
  opacity: 0;
  transition: transform .5s cubic-bezier(.2,.9,.2,1),opacity .4s,background .25s;
  transition-delay: calc(var(--i) * .06s);
}

.pc-04__card:hover .pc-04__soc {
  transform: translateY(0);
  opacity: 1;
}

.pc-04__soc:hover {
  background: rgba(255,255,255,.26);
}

.pc-04__body {
  padding: 20px 22px;
  text-align: center;
}

.pc-04__body h3 {
  font-size: 1.3rem;
  font-weight: 800;
}

.pc-04__body p {
  color: rgba(255,255,255,.55);
  font-size: .86rem;
  margin-top: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .pc-04__soc {
    transition: opacity .3s;
  }

  .pc-04__card:hover .pc-04__pfp {
    transform: none;
  }
}
```
