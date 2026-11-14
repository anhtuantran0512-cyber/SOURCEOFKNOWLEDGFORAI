---
source: "codefronts"
url: "https://codefronts.com/navigation/css-side-menu/glassmorphism-blurred-sidebar/"
title: "Glassmorphism Blurred Sidebar"
section: "navigation"
category: "css-side-menu"
category_name: "CSS Side Menus"
description: "A frosted-glass sidebar panel using backdrop-filter blur over animated gradient colour blobs, with a semi-transparent border and layered glass card components."
has_js: "false"
---

Here's a working CSS Side Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Blurred Sidebar
Source: https://codefronts.com/navigation/css-side-menu/glassmorphism-blurred-sidebar/

A frosted-glass sidebar panel using backdrop-filter blur over animated gradient colour blobs, with a semi-transparent border and layered glass card components.
## HTML
```html
<div class="sm-10">
  <div class="sm-10__bg">
    <div class="sm-10__blob sm-10__blob--a"></div>
    <div class="sm-10__blob sm-10__blob--b"></div>
    <div class="sm-10__blob sm-10__blob--c"></div>
  </div>
  <nav class="sm-10__nav">
    <div class="sm-10__brand">
      <div class="sm-10__logo">◇</div>
      <div class="sm-10__brand-name">Crystal</div>
    </div>
    <div class="sm-10__links">
      <a class="sm-10__link sm-10__link--active" href="#"><span class="sm-10__link-icon">⬡</span> Home</a>
      <a class="sm-10__link" href="#"><span class="sm-10__link-icon">◈</span> Explore</a>
      <a class="sm-10__link" href="#"><span class="sm-10__link-icon">▦</span> Library <span class="sm-10__badge">7</span></a>
      <a class="sm-10__link" href="#"><span class="sm-10__link-icon">◉</span> Messages <span class="sm-10__badge">3</span></a>
      <div class="sm-10__divider"></div>
      <a class="sm-10__link" href="#"><span class="sm-10__link-icon">◬</span> Account</a>
      <a class="sm-10__link" href="#"><span class="sm-10__link-icon">⬙</span> Settings</a>
    </div>
    <div class="sm-10__user">
      <div class="sm-10__avatar">LM</div>
      <div>
        <div class="sm-10__uname">Lena M.</div>
        <div class="sm-10__urole">Creator</div>
      </div>
    </div>
  </nav>
  <div class="sm-10__main">
    <div class="sm-10__heading">Home Feed</div>
    <div class="sm-10__sub">Frosted glass sidebar using <code>backdrop-filter:blur(20px)</code> over animated gradient blobs. The glass blurs whatever colour passes behind it.</div>
    <div class="sm-10__cards">
      <div class="sm-10__card"><div class="sm-10__card-val">12.4k</div><div class="sm-10__card-lbl">Followers</div></div>
      <div class="sm-10__card"><div class="sm-10__card-val">892</div><div class="sm-10__card-lbl">Likes today</div></div>
      <div class="sm-10__card"><div class="sm-10__card-val">47</div><div class="sm-10__card-lbl">Published</div></div>
      <div class="sm-10__card"><div class="sm-10__card-val">3.2k</div><div class="sm-10__card-lbl">Views</div></div>
    </div>
  </div>
</div>
```
## CSS
```css
.sm-10,
.sm-10 *,
.sm-10 *::before,
.sm-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sm-10 ::selection {
  background: rgba(255,255,255,0.3);
  color: #fff;
}

.sm-10 {
  --font: 'Space Grotesk', system-ui, sans-serif;
  font-family: var(--font);
  min-height: 100vh;
  display: flex;
  border-radius: 12px;
  overflow: hidden;
  position: relative;
}
/* Vivid gradient background blobs (what passes THROUGH the glass) */

.sm-10__bg {
  position: absolute;
  inset: 0;
  background: #0d0d1a;
  z-index: 0;
  overflow: hidden;
}

.sm-10__blob {
  position: absolute;
  border-radius: 50%;
  filter: blur(60px);
  opacity: 0.6;
}

.sm-10__blob--a {
  width: 280px;
  height: 280px;
  background: #7c3aed;
  top: -60px;
  left: 20px;
  animation: sm-10-drift1 12s ease-in-out infinite alternate;
}

.sm-10__blob--b {
  width: 220px;
  height: 220px;
  background: #0ea5e9;
  bottom: -40px;
  left: 100px;
  animation: sm-10-drift2 14s ease-in-out infinite alternate;
}

.sm-10__blob--c {
  width: 200px;
  height: 200px;
  background: #10b981;
  top: 40%;
  right: 5%;
  animation: sm-10-drift3 10s ease-in-out infinite alternate;
}

@keyframes sm-10-drift1 {
  to {
    transform: translate(30px, 40px) scale(1.1);
  }
}

@keyframes sm-10-drift2 {
  to {
    transform: translate(-20px, -30px) scale(0.9);
  }
}

@keyframes sm-10-drift3 {
  to {
    transform: translate(10px, 20px) scale(1.05);
  }
}
/* Glass sidebar */

.sm-10__nav {
  position: relative;
  z-index: 10;
  width: 230px;
  background: rgba(255,255,255,0.06);
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  border-right: 1px solid rgba(255,255,255,0.1);
  display: flex;
  flex-direction: column;
  padding: 22px 0;
  flex-shrink: 0;
  box-shadow: 4px 0 40px rgba(0,0,0,0.3);
}

.sm-10__brand {
  padding: 0 18px 18px;
  border-bottom: 1px solid rgba(255,255,255,0.07);
  margin-bottom: 16px;
  display: flex;
  align-items: center;
  gap: 11px;
}

.sm-10__logo {
  width: 36px;
  height: 36px;
  background: rgba(255,255,255,0.12);
  border: 1px solid rgba(255,255,255,0.2);
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 16px;
  color: #fff;
  backdrop-filter: blur(10px);
}

.sm-10__brand-name {
  font-size: 15px;
  font-weight: 700;
  color: #fff;
}

.sm-10__links {
  flex: 1;
  padding: 0 10px;
}

.sm-10__link {
  display: flex;
  align-items: center;
  gap: 11px;
  padding: 11px 14px;
  border-radius: 10px;
  color: rgba(255,255,255,0.5);
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  text-decoration: none;
  transition: all 0.25s;
  margin-bottom: 3px;
  border: 1px solid transparent;
}

.sm-10__link:hover {
  color: rgba(255,255,255,0.9);
  background: rgba(255,255,255,0.09);
  border-color: rgba(255,255,255,0.12);
}

.sm-10__link--active {
  color: #fff;
  background: rgba(255,255,255,0.12);
  border-color: rgba(255,255,255,0.18);
  box-shadow: 0 0 20px rgba(255,255,255,0.05);
}

.sm-10__link-icon {
  font-size: 16px;
}

.sm-10__badge {
  margin-left: auto;
  background: rgba(255,255,255,0.15);
  color: #fff;
  font-size: 10px;
  font-weight: 700;
  padding: 2px 7px;
  border-radius: 99px;
}

.sm-10__divider {
  height: 1px;
  background: rgba(255,255,255,0.07);
  margin: 8px 10px;
}
/* Glass user footer */

.sm-10__user {
  margin: 8px 10px 0;
  padding: 12px;
  background: rgba(255,255,255,0.07);
  border: 1px solid rgba(255,255,255,0.1);
  border-radius: 12px;
  display: flex;
  align-items: center;
  gap: 10px;
  backdrop-filter: blur(8px);
}

.sm-10__avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: linear-gradient(135deg, #7c3aed, #0ea5e9);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
  font-weight: 700;
  color: #fff;
  flex-shrink: 0;
}

.sm-10__uname {
  font-size: 12px;
  font-weight: 700;
  color: #fff;
}

.sm-10__urole {
  font-size: 10px;
  color: rgba(255,255,255,0.5);
}
/* Main content */

.sm-10__main {
  flex: 1;
  position: relative;
  z-index: 10;
  padding: 24px;
  color: #fff;
}

.sm-10__heading {
  font-size: 20px;
  font-weight: 700;
  margin-bottom: 6px;
}

.sm-10__sub {
  font-size: 13px;
  color: rgba(255,255,255,0.55);
  line-height: 1.7;
  margin-bottom: 22px;
}
/* Glass cards */

.sm-10__cards {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}

.sm-10__card {
  background: rgba(255,255,255,0.07);
  border: 1px solid rgba(255,255,255,0.1);
  border-radius: 12px;
  padding: 16px;
  backdrop-filter: blur(10px);
}

.sm-10__card-val {
  font-size: 22px;
  font-weight: 700;
  color: #fff;
}

.sm-10__card-lbl {
  font-size: 12px;
  color: rgba(255,255,255,0.5);
  margin-top: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .sm-10__blob {
    animation: none;
  }

  .sm-10__link {
    transition: none;
  }
}
```
