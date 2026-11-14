---
source: "codefronts"
url: "https://codefronts.com/motion/css-image-hover-effects/circular-team-profile-avatar-hover-css/"
title: "Circular Team Profile Avatar Hover CSS"
section: "motion"
category: "css-image-hover-effects"
category_name: "CSS Image Hover Effects"
description: "About-page avatar hover with a conic-gradient spinning border trail and slide-up social icon reveal driven by CSS animation-play-state."
has_js: "false"
---

Here's a working CSS Image Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Circular Team Profile Avatar Hover CSS
Source: https://codefronts.com/motion/css-image-hover-effects/circular-team-profile-avatar-hover-css/

About-page avatar hover with a conic-gradient spinning border trail and slide-up social icon reveal driven by CSS animation-play-state.
## HTML
```html
<div class="ih-16">
  <div class="ih-16__grid">
    <div class="ih-16__item">
      <div class="ih-16__wrap">
        <div class="ih-16__avatar ih-16__avatar--1">👩‍💻</div>
      </div>
      <p class="ih-16__name">Yuki Tanaka</p>
      <p class="ih-16__role">Frontend Eng.</p>
      <div class="ih-16__socials"><span class="ih-16__s">𝕏</span><span class="ih-16__s">gh</span></div>
    </div>
    <div class="ih-16__item">
      <div class="ih-16__wrap">
        <div class="ih-16__avatar ih-16__avatar--2">👨‍🎨</div>
      </div>
      <p class="ih-16__name">Amara Diallo</p>
      <p class="ih-16__role">UX Designer</p>
      <div class="ih-16__socials"><span class="ih-16__s">𝕏</span><span class="ih-16__s">be</span></div>
    </div>
    <div class="ih-16__item">
      <div class="ih-16__wrap">
        <div class="ih-16__avatar ih-16__avatar--3">🧑‍🔬</div>
      </div>
      <p class="ih-16__name">Ravi Patel</p>
      <p class="ih-16__role">Data Scientist</p>
      <div class="ih-16__socials"><span class="ih-16__s">𝕏</span><span class="ih-16__s">in</span></div>
    </div>
    <div class="ih-16__item">
      <div class="ih-16__wrap">
        <div class="ih-16__avatar ih-16__avatar--4">👩‍🚀</div>
      </div>
      <p class="ih-16__name">Zoe Mercer</p>
      <p class="ih-16__role">DevOps Lead</p>
      <div class="ih-16__socials"><span class="ih-16__s">gh</span><span class="ih-16__s">in</span></div>
    </div>
  </div>
</div>
```
## CSS
```css
.ih-16,
.ih-16 *,
.ih-16 *::before,
.ih-16 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ih-16 ::selection {
  background: #a78bfa;
  color: #000;
}

.ih-16 {
  --accent: #a78bfa;
  --accent2: #34d399;
  --bg: #080812;
  --text: #f1f5f9;
  --muted: #64748b;
  font-family: system-ui,sans-serif;
  background: var(--bg);
  padding: 40px 24px;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.ih-16__grid {
  display: grid;
  grid-template-columns: repeat(4,1fr);
  gap: 20px;
  max-width: 780px;
  width: 100%;
}

.ih-16__item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  cursor: pointer;
}
/* Conic gradient spinning ring via pseudo-element */

.ih-16__wrap {
  position: relative;
  width: 80px;
  height: 80px;
}

.ih-16__wrap::before {
  content: '';
  position: absolute;
  inset: -3px;
  border-radius: 50%;
  background: conic-gradient(from 0deg, transparent 0deg 270deg, var(--ring-color,var(--accent)) 270deg 360deg);
  opacity: 0;
  transition: opacity 0.3s ease;
  animation: ih-16-spin 1.2s linear infinite paused;
}

.ih-16__item:hover .ih-16__wrap::before {
  opacity: 1;
  animation-play-state: running;
}

@keyframes ih-16-spin {
  to {
    transform: rotate(360deg);
  }
}
/* The avatar itself */

.ih-16__avatar {
  position: relative;
  z-index: 1;
  width: 74px;
  height: 74px;
  border-radius: 50%;
  margin: 3px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 34px;
  transition: transform 0.35s cubic-bezier(0.34,1.56,0.64,1);
}

.ih-16__item:hover .ih-16__avatar {
  transform: scale(1.06);
}

.ih-16__avatar--1 {
  background: radial-gradient(circle at 30% 30%,#4c1d95,#0f172a);
}

.ih-16__avatar--2 {
  background: radial-gradient(circle at 30% 30%,#065f46,#0f172a);
}

.ih-16__avatar--3 {
  background: radial-gradient(circle at 30% 30%,#92400e,#0f172a);
}

.ih-16__avatar--4 {
  background: radial-gradient(circle at 30% 30%,#1e3a5f,#0f172a);
}
/* Individual ring colours */

.ih-16__item:nth-child(1) .ih-16__wrap {
  --ring-color: #a78bfa;
}

.ih-16__item:nth-child(2) .ih-16__wrap {
  --ring-color: #34d399;
}

.ih-16__item:nth-child(3) .ih-16__wrap {
  --ring-color: #fb923c;
}

.ih-16__item:nth-child(4) .ih-16__wrap {
  --ring-color: #60a5fa;
}
/* Social icons slide up on hover */

.ih-16__socials {
  display: flex;
  gap: 6px;
  margin-top: 2px;
  transform: translateY(6px);
  opacity: 0;
  transition: transform 0.3s cubic-bezier(0.16,1,0.3,1),opacity 0.3s ease;
}

.ih-16__item:hover .ih-16__socials {
  transform: none;
  opacity: 1;
}

.ih-16__s {
  font-size: 12px;
  background: rgba(255,255,255,0.07);
  border-radius: 4px;
  padding: 2px 5px;
  color: var(--muted);
}

.ih-16__name {
  font-size: 12px;
  font-weight: 700;
  color: var(--text);
  text-align: center;
}

.ih-16__role {
  font-size: 10px;
  color: var(--muted);
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .ih-16__wrap::before {
    animation: none;
  }

  .ih-16__avatar,
    .ih-16__socials {
    transition: none;
  }

  .ih-16__item:hover .ih-16__wrap::before {
    opacity: 1;
  }

  .ih-16__item:hover .ih-16__socials {
    opacity: 1;
    transform: none;
  }
}
```
