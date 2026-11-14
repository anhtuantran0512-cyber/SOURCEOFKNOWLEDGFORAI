---
source: "codefronts"
url: "https://codefronts.com/navigation/css-responsive-navbar/css-gradient-border-animated-navbar/"
title: "CSS Gradient Border Animated Navbar"
section: "navigation"
category: "css-responsive-navbar"
category_name: "CSS Responsive Navbars"
description: "Transparent navbar with a rotating conic-gradient animated bottom border and shimmer hover effects on links."
has_js: "false"
---

Here's a working CSS Responsive Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Gradient Border Animated Navbar
Source: https://codefronts.com/navigation/css-responsive-navbar/css-gradient-border-animated-navbar/

Transparent navbar with a rotating conic-gradient animated bottom border and shimmer hover effects on links.
## HTML
```html
<div class="nav-11">
  <input type="checkbox" id="nav-11-toggle">
  <div class="nav-11__bar">
    <a href="#" class="nav-11__logo"><em>Violet</em>Lab</a>
    <ul class="nav-11__links">
      <li><a href="#" class="is-active">Home</a></li>
      <li><a href="#">Products</a></li>
      <li><a href="#">Docs</a></li>
      <li><a href="#">Pricing</a></li>
      <li><a href="#">Blog</a></li>
    </ul>
    <button class="nav-11__btn">Get started</button>
    <label for="nav-11-toggle" class="nav-11__hamburger" aria-label="Toggle menu">
      <span></span><span></span><span></span>
    </label>
  </div>
  <div class="nav-11__mobile">
    <a href="#">Home</a><a href="#">Products</a><a href="#">Docs</a><a href="#">Pricing</a><a href="#">Blog</a>
    <a href="#" style="color:#a78bfa; font-weight:700;">Get started →</a>
  </div>
</div>
<div style="padding:4rem 2rem; color:#f5f0ff; max-width:700px; margin:0 auto;">
  <h1 style="font-size:2.5rem; font-weight:800; letter-spacing:-0.03em; margin-bottom:1rem; background:linear-gradient(90deg,#c026d3,#7c3aed,#2563eb); -webkit-background-clip:text; -webkit-text-fill-color:transparent;">Gradient Border Navbar</h1>
  <p style="color:rgba(245,240,255,0.55); font-size:1.1rem; line-height:1.7;">The animated gradient border uses an <code>::before</code> pseudo-element positioned 1px outside the card with a <code>border-radius</code> that's 1px larger. The card itself sits on top with a dark semi-transparent background.</p>
</div>
```
## CSS
```css
.nav-11,
.nav-11 *,
.nav-11 *::before,
.nav-11 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.nav-11 {
  --text: #f5f0ff;
  --muted: rgba(245,240,255,0.5);
  --grad-a: #c026d3;
  --grad-b: #7c3aed;
  --grad-c: #2563eb;
  font-family: 'Raleway', sans-serif;
  padding: 1.25rem 2rem;
  position: sticky;
  top: 0;
  z-index: 100;
}

.nav-11__bar {
  max-width: 1100px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  gap: 1.5rem;
  background: rgba(10,0,22,0.6);
  backdrop-filter: blur(20px);
  border-radius: 16px;
  padding: 0.5rem 0.5rem 0.5rem 1.5rem;
  position: relative;
}
/* Gradient border via pseudo-element */

.nav-11__bar::before {
  content: '';
  position: absolute;
  inset: -1px;
  border-radius: 17px;
  background: linear-gradient(135deg, var(--grad-a), var(--grad-b), var(--grad-c));
  z-index: -1;
  animation: nav-11-rotategrad 4s linear infinite;
}

@keyframes nav-11-rotategrad {
  0% {
    background: linear-gradient(135deg, #c026d3, #7c3aed, #2563eb);
  }

  25% {
    background: linear-gradient(225deg, #c026d3, #7c3aed, #2563eb);
  }

  50% {
    background: linear-gradient(315deg, #c026d3, #7c3aed, #2563eb);
  }

  75% {
    background: linear-gradient(45deg, #c026d3, #7c3aed, #2563eb);
  }

  100% {
    background: linear-gradient(135deg, #c026d3, #7c3aed, #2563eb);
  }
}

.nav-11__logo {
  font-weight: 800;
  font-size: 1.2rem;
  color: var(--text);
  text-decoration: none;
  letter-spacing: -0.02em;
  flex-shrink: 0;
}

.nav-11__logo em {
  font-style: normal;
  background: linear-gradient(90deg, #c026d3, #7c3aed);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.nav-11__links {
  display: flex;
  list-style: none;
  gap: 0.25rem;
  flex: 1;
}

.nav-11__links a {
  display: block;
  color: var(--muted);
  text-decoration: none;
  font-size: 0.875rem;
  font-weight: 600;
  padding: 0.45rem 0.9rem;
  border-radius: 10px;
  transition: color 0.2s, background 0.2s;
}

.nav-11__links a:hover {
  color: var(--text);
  background: rgba(255,255,255,0.07);
}

.nav-11__links a.is-active {
  color: var(--text);
}

.nav-11__btn {
  padding: 0.55rem 1.3rem;
  border-radius: 10px;
  font-size: 0.875rem;
  font-weight: 700;
  cursor: pointer;
  border: none;
  font-family: inherit;
  background: linear-gradient(135deg, #c026d3, #7c3aed);
  color: #fff;
  flex-shrink: 0;
  box-shadow: 0 4px 20px rgba(124,58,237,0.4);
  transition: opacity 0.2s, transform 0.15s, box-shadow 0.2s;
}

.nav-11__btn:hover {
  opacity: 0.85;
  transform: translateY(-1px);
  box-shadow: 0 8px 28px rgba(124,58,237,0.55);
}
/* Mobile */

#nav-11-toggle {
  display: none;
}

.nav-11__hamburger {
  display: none;
  flex-direction: column;
  gap: 5px;
  cursor: pointer;
  padding: 8px;
  border: none;
  background: transparent;
}

.nav-11__hamburger span {
  display: block;
  width: 20px;
  height: 1.5px;
  background: var(--text);
  border-radius: 2px;
  transition: transform 0.3s, opacity 0.3s;
}

#nav-11-toggle:checked ~ .nav-11__bar .nav-11__hamburger span:nth-child(1) {
  transform: translateY(6.5px) rotate(45deg);
}

#nav-11-toggle:checked ~ .nav-11__bar .nav-11__hamburger span:nth-child(2) {
  opacity: 0;
}

#nav-11-toggle:checked ~ .nav-11__bar .nav-11__hamburger span:nth-child(3) {
  transform: translateY(-6.5px) rotate(-45deg);
}

.nav-11__mobile {
  display: none;
  flex-direction: column;
  gap: 0.25rem;
  background: rgba(15,5,30,0.95);
  backdrop-filter: blur(20px);
  padding: 0.75rem 1rem 1rem;
  border-radius: 0 0 12px 12px;
  margin-top: -8px;
  position: relative;
  z-index: -1;
  border: 1px solid rgba(124,58,237,0.2);
  border-top: none;
}

.nav-11__mobile a {
  display: block;
  color: rgba(245,240,255,0.7);
  text-decoration: none;
  font-size: 0.9rem;
  font-weight: 600;
  padding: 0.6rem 0.75rem;
  border-radius: 8px;
  transition: background 0.15s, color 0.15s;
}

.nav-11__mobile a:hover {
  background: rgba(124,58,237,0.15);
  color: var(--text);
}

#nav-11-toggle:checked ~ .nav-11__mobile {
  display: flex;
}

@media (max-width: 640px) {
  .nav-11__links,
    .nav-11__btn {
    display: none;
  }

  .nav-11__hamburger {
    display: flex;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nav-11__bar::before {
    animation: none;
    background: linear-gradient(135deg, #c026d3, #7c3aed, #2563eb);
  }

  .nav-11__btn,
    .nav-11__hamburger span {
    transition: none;
  }
}
```
