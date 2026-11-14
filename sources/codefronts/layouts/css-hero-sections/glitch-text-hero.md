---
source: "codefronts"
url: "https://codefronts.com/layouts/css-hero-sections/glitch-text-hero/"
title: "Glitch Text Hero"
section: "layouts"
category: "css-hero-sections"
category_name: "CSS Hero Sections"
description: "VHS-glitch hero — RGB-channel offsets create a tape-static glitch effect."
has_js: "false"
---

Here's a working CSS Hero Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glitch Text Hero
Source: https://codefronts.com/layouts/css-hero-sections/glitch-text-hero/

VHS-glitch hero — RGB-channel offsets create a tape-static glitch effect. VHS red and tape blue against a static-gray background, the analogue cyberpunk treatment.
## HTML
```html
<section class="hs-29" aria-label="Hero">
  <span class="hs-29__static" aria-hidden="true"></span>
  <span class="hs-29__scan" aria-hidden="true"></span>
  <div class="hs-29__inner">
    <span class="hs-29__eye">REC ● 00:42:18</span>
    <h2 data-text="LOST &amp; FOUND" class="hs-29__h">LOST &amp; FOUND</h2>
    <p>
      A search engine for VHS-era ephemera. Public-access TV, mall demos, regional news. The
      forgotten internet of the 80s.
    </p>
    <a class="hs-29__cta" href="#search">Search the tapes →</a>
  </div>
</section>
```
## CSS
```css
.hs-29 {
  position: relative;
  overflow: hidden;
  display: grid;
  place-items: center;
  width: 100%;
  min-height: 100vh;
  padding: clamp(28px, 5vw, 64px) clamp(20px, 5vw, 56px);
  background: #1a1818;
  font-family: 'JetBrains Mono', monospace;
  color: #d8d4c8;
  box-sizing: border-box;
  contain: layout paint;
}

.hs-29__static {
  position: absolute;
  inset: 0;
  background-image: radial-gradient(rgba(255,255,255,0.04) 1px, transparent 1px), radial-gradient(rgba(255,255,255,0.03) 1px, transparent 1px);
  background-size: 3px 3px, 5px 5px;
  background-position: 0 0, 1px 1px;
  pointer-events: none;
  animation: hs-29-jit 0.2s steps(2) infinite;
}

.hs-29__scan {
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(180deg, transparent 0 2px, rgba(0,0,0,0.18) 2px 3px);
  pointer-events: none;
}

@keyframes hs-29-jit {
  0% {
    transform: translate(0,0);
  }

  50% {
    transform: translate(-1px,1px);
  }

  100% {
    transform: translate(1px,-1px);
  }
}

.hs-29__inner {
  position: relative;
  z-index: 1;
  max-width: 640px;
  text-align: center;
}

.hs-29__eye {
  display: inline-block;
  padding: 4px 10px;
  background: #d63838;
  color: #fff;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.18em;
  margin-bottom: 22px;
  animation: hs-29-blink 1.4s steps(2) infinite;
}

@keyframes hs-29-blink {
  to {
    opacity: 0.5;
  }
}

.hs-29__h {
  position: relative;
  margin: 0 0 18px;
  font-family: 'Inter', sans-serif;
  font-size: clamp(48px, 9vw, 100px);
  font-weight: 900;
  letter-spacing: -0.04em;
  line-height: 0.92;
  color: #f0eee0;
}

.hs-29__h::before,
.hs-29__h::after {
  content: attr(data-text);
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  pointer-events: none;
  text-align: center;
}

.hs-29__h::before {
  color: #d63838;
  transform: translate(-3px,0);
  clip-path: polygon(0 12%, 100% 12%, 100% 38%, 0 38%);
  animation: hs-29-rgb 2.4s ease-in-out infinite;
}

.hs-29__h::after {
  color: #38b8d6;
  transform: translate(3px,0);
  clip-path: polygon(0 56%, 100% 56%, 100% 88%, 0 88%);
  animation: hs-29-rgb 2.4s ease-in-out infinite reverse;
}

@keyframes hs-29-rgb {
  0%,
    100% {
    transform: translate(-3px,0);
  }

  50% {
    transform: translate(3px,2px);
  }
}

.hs-29 p {
  margin: 0 auto 24px;
  font-size: 14px;
  line-height: 1.6;
  color: #98948c;
  max-width: 460px;
}

.hs-29__cta {
  display: inline-block;
  padding: 12px 22px;
  background: #38b8d6;
  color: #1a1818;
  border-radius: 0;
  text-decoration: none;
  font-weight: 800;
  font-size: 13px;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  transition: background 0.15s, color 0.15s;
}

.hs-29__cta:hover {
  background: #d63838;
  color: #fff;
}

@media (prefers-reduced-motion: reduce) {
  .hs-29__static,
    .hs-29__eye,
    .hs-29__h::before,
    .hs-29__h::after {
    animation: none;
  }

  .hs-29__cta {
    transition: none;
  }
}
```
