---
source: "codefronts"
url: "https://codefronts.com/components/css-profile-cards/retro-90s-cyberpunk-profile-card/"
title: "Retro / 90s Cyberpunk Profile Card"
section: "components"
category: "css-profile-cards"
category_name: "CSS Profile Cards"
description: "A brutalist neon card with hard offset shadows, a clip-path notched avatar, a scanning line and a glitch-split name effect — pure CSS, no JS."
has_js: "false"
---

Here's a working CSS Profile Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Retro / 90s Cyberpunk Profile Card
Source: https://codefronts.com/components/css-profile-cards/retro-90s-cyberpunk-profile-card/

A brutalist neon card with hard offset shadows, a clip-path notched avatar, a scanning line and a glitch-split name effect — pure CSS, no JS.
## HTML
```html
<div class="pc-11">
  <div class="pc-11__card">
    <div class="pc-11__scan"></div>
    <div class="pc-11__pfp">
      <span>V0</span>
    </div>
    <h3 class="pc-11__name" data-text="VECTOR_09">VECTOR_09</h3>
    <p class="pc-11__role">// NETRUNNER · CLASS-A</p>
    <div class="pc-11__stats">
      <div class="pc-11__stat"><b>1337</b><span>REP</span></div>
      <div class="pc-11__stat"><b>404</b><span>RAIDS</span></div>
      <div class="pc-11__stat"><b>&#8734;</b><span>CRED</span></div>
    </div>
    <button class="pc-11__jack">&gt; JACK IN</button>
  </div>
</div>
```
## CSS
```css
.pc-11,
.pc-11 *,
.pc-11 *::before,
.pc-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pc-11 ::selection {
  background: #f0f;
  color: #000;
}

.pc-11 {
  font-family: 'Courier New',monospace;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 20px;
  background: #0a0012;
  color: #0ff;
}

.pc-11__card {
  position: relative;
  width: 300px;
  padding: 28px;
  overflow: hidden;
  background: #12001f;
  border: 2px solid #f0f;
  box-shadow: 8px 8px 0 #0ff,0 0 30px rgba(255,0,255,.4);
  text-align: center;
}

.pc-11__scan {
  position: absolute;
  left: 0;
  right: 0;
  height: 3px;
  top: 0;
  background: linear-gradient(90deg,transparent,#0ff,transparent);
  opacity: .6;
  animation: pc-11-scan 3s linear infinite;
}

@keyframes pc-11-scan {
  0% {
    top: 0;
  }

  100% {
    top: 100%;
  }
}

.pc-11__pfp {
  width: 90px;
  height: 90px;
  margin: 0 auto 18px;
  display: grid;
  place-items: center;
  font-weight: 800;
  font-size: 1.8rem;
  color: #0a0012;
  background: linear-gradient(135deg,#0ff,#f0f);
  border: 2px solid #0ff;
  box-shadow: 4px 4px 0 #f0f;
  clip-path: polygon(0 12%,12% 0,100% 0,100% 88%,88% 100%,0 100%);
}

.pc-11__name {
  position: relative;
  font-size: 1.6rem;
  font-weight: 800;
  letter-spacing: .06em;
  color: #0ff;
}

.pc-11__name::before,
.pc-11__name::after {
  content: attr(data-text);
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
}

.pc-11__name::before {
  color: #f0f;
  animation: pc-11-g1 2.6s infinite steps(2);
  clip-path: inset(0 0 55% 0);
}

.pc-11__name::after {
  color: #0ff;
  animation: pc-11-g2 3.1s infinite steps(2);
  clip-path: inset(55% 0 0 0);
}

@keyframes pc-11-g1 {
  0%,
    90%,
    100% {
    transform: translate(0);
  }

  92% {
    transform: translate(-3px,-1px);
  }

  96% {
    transform: translate(3px,1px);
  }
}

@keyframes pc-11-g2 {
  0%,
    88%,
    100% {
    transform: translate(0);
  }

  91% {
    transform: translate(3px,1px);
  }

  95% {
    transform: translate(-3px,-1px);
  }
}

.pc-11__role {
  color: #f0f;
  font-size: .8rem;
  margin-top: 8px;
  letter-spacing: .14em;
}

.pc-11__stats {
  display: flex;
  justify-content: space-between;
  margin: 22px 0;
  border-top: 1px dashed #f0f;
  border-bottom: 1px dashed #f0f;
  padding: 14px 0;
}

.pc-11__stat b {
  display: block;
  font-size: 1.2rem;
  color: #0ff;
}

.pc-11__stat span {
  font-size: .66rem;
  color: #f0f;
  letter-spacing: .1em;
}

.pc-11__jack {
  width: 100%;
  padding: 12px;
  cursor: pointer;
  font-family: inherit;
  font-weight: 800;
  font-size: .9rem;
  letter-spacing: .1em;
  color: #0a0012;
  background: #0ff;
  border: none;
  box-shadow: 4px 4px 0 #f0f;
  transition: transform .1s,box-shadow .1s;
}

.pc-11__jack:hover {
  background: #f0f;
  color: #0ff;
  box-shadow: 4px 4px 0 #0ff;
}

.pc-11__jack:active {
  transform: translate(4px,4px);
  box-shadow: 0 0 0 #f0f;
}

@media (prefers-reduced-motion: reduce) {
  .pc-11 * {
    animation: none!important;
  }
}
```
