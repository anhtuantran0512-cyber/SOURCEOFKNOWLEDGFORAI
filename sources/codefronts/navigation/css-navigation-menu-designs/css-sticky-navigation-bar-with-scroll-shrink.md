---
source: "codefronts"
url: "https://codefronts.com/navigation/css-navigation-menu-designs/css-sticky-navigation-bar-with-scroll-shrink/"
title: "CSS Sticky Navigation Bar with Scroll Shrink"
section: "navigation"
category: "css-navigation-menu-designs"
category_name: "CSS Navigation Menus"
description: "A sticky navigation bar that smoothly shrinks its height and adds a drop shadow as the user scrolls down, with a scroll-progress indicator bar at the top."
has_js: "true"
---

Here's a working CSS Navigation Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Sticky Navigation Bar with Scroll Shrink
Source: https://codefronts.com/navigation/css-navigation-menu-designs/css-sticky-navigation-bar-with-scroll-shrink/

A sticky navigation bar that smoothly shrinks its height and adds a drop shadow as the user scrolls down, with a scroll-progress indicator bar at the top. The shrink effect is driven by a CSS class toggled via a tiny IntersectionObserver-based scroll listener.
## HTML
```html
<div class="nav-06">
  <div class="nav-06__progress" id="nav-06-progress"></div>
  <nav class="nav-06__bar" id="nav-06-bar">
    <div class="nav-06__logo">
      <span class="nav-06__logo-leaf">
        <svg viewBox="0 0 24 24"><path d="M12 22s-8-4.5-8-11.8A8 8 0 0112 2a8 8 0 018 8.2c0 7.3-8 11.8-8 11.8z"/></svg>
      </span>
      Verdant
    </div>
    <ul class="nav-06__links">
      <li><a href="#" class="nav-06__active">Home</a></li>
      <li><a href="#">Features</a></li>
      <li><a href="#">Pricing</a></li>
      <li><a href="#">Blog</a></li>
    </ul>
    <div class="nav-06__actions">
      <a href="#" class="nav-06__btn nav-06__btn--ghost">Login</a>
      <a href="#" class="nav-06__btn nav-06__btn--fill">Try free</a>
    </div>
  </nav>
  <div class="nav-06__hero">
    <h1>Sticky nav that<br><span>shrinks on scroll</span></h1>
    <p>Scroll down to see the navbar compress from 72px to 52px. JavaScript reads <code>scrollY</code> and toggles a class. All visual transitions are pure CSS.</p>
    <div class="nav-06__scroll-hint">
      <svg viewBox="0 0 24 24"><path d="M12 5v14M5 12l7 7 7-7"/></svg>
      Scroll down to trigger
    </div>
  </div>
  <div class="nav-06__content">
    <div class="nav-06__card">
      <h3>How it works</h3>
      <p>A tiny scroll event listener adds <code>.nav-06--shrunk</code> once <code>scrollY > 60</code>. The navbar's <code>height</code>, logo scale, and button size all transition via CSS. The scroll progress bar width is updated in the same handler.</p>
    </div>
    <div class="nav-06__card">
      <h3>Performance</h3>
      <p>Only <code>height</code>, <code>transform</code>, and <code>box-shadow</code> animate — height is handled via CSS transition on a sticky element, transform stays on the compositor.</p>
    </div>
    <div class="nav-06__card">
      <h3>Accessibility</h3>
      <p>The navbar remains fully keyboard-navigable throughout. The shrink behaviour is a visual enhancement only and doesn't affect focus order or ARIA roles.</p>
    </div>
  </div>
</div>

```
## CSS
```css
.nav-06,
.nav-06 *,
.nav-06 *::before,
.nav-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.nav-06 ::selection {
  background: #059669;
  color: #fff;
}

.nav-06 {
  --bg: #f0fdf4;
  --surface: #fff;
  --text: #052e16;
  --muted: #6b7280;
  --accent: #059669;
  --accent2: #34d399;
  --border: #d1fae5;
  font-family: 'Inter',system-ui,sans-serif;
  background: var(--bg);
  min-height: 200vh;
}

.nav-06__bar {
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(255,255,255,.9);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border);
  padding: 0 48px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 72px;
  transition: height .3s ease,box-shadow .3s ease,border-color .3s;
}

.nav-06__bar.nav-06--shrunk {
  height: 52px;
  box-shadow: 0 4px 20px rgba(5,150,105,.1);
  border-color: rgba(5,150,105,.2);
}

.nav-06__logo {
  font-size: 1.2rem;
  font-weight: 700;
  color: var(--text);
  display: flex;
  align-items: center;
  gap: 8px;
  transition: transform .3s ease;
}

.nav-06__bar.nav-06--shrunk .nav-06__logo {
  transform: scale(.9);
}

.nav-06__logo-leaf {
  width: 28px;
  height: 28px;
  background: var(--accent);
  border-radius: 50% 0 50% 50%;
  display: grid;
  place-items: center;
  transition: width .3s,height .3s;
}

.nav-06__bar.nav-06--shrunk .nav-06__logo-leaf {
  width: 22px;
  height: 22px;
}

.nav-06__logo-leaf svg {
  width: 14px;
  height: 14px;
  stroke: #fff;
  fill: none;
  stroke-width: 2;
}

.nav-06__links {
  display: flex;
  align-items: center;
  gap: 4px;
  list-style: none;
}

.nav-06__links a {
  padding: 7px 13px;
  color: var(--muted);
  text-decoration: none;
  font-size: .875rem;
  font-weight: 500;
  border-radius: 6px;
  transition: color .18s,background .18s;
}

.nav-06__links a:hover {
  color: var(--text);
  background: var(--border);
}

.nav-06__links a.nav-06__active {
  color: var(--accent);
  background: #ecfdf5;
}

.nav-06__actions {
  display: flex;
  align-items: center;
  gap: 10px;
}

.nav-06__btn {
  padding: 7px 16px;
  border-radius: 6px;
  font-size: .875rem;
  font-weight: 600;
  text-decoration: none;
  cursor: pointer;
  transition: all .18s;
  display: inline-flex;
  align-items: center;
}

.nav-06__btn--ghost {
  color: var(--accent);
  background: transparent;
  border: 1.5px solid var(--border);
}

.nav-06__btn--ghost:hover {
  border-color: var(--accent2);
}

.nav-06__btn--fill {
  color: #fff;
  background: var(--accent);
  border: 1.5px solid var(--accent);
}

.nav-06__btn--fill:hover {
  opacity: .88;
}
/* shrink cta */

.nav-06__bar.nav-06--shrunk .nav-06__btn {
  padding: 5px 13px;
  font-size: .8125rem;
}
/* scroll indicator bar */

.nav-06__progress {
  position: fixed;
  top: 0;
  left: 0;
  height: 3px;
  z-index: 101;
  background: linear-gradient(90deg,var(--accent),var(--accent2));
  width: 0%;
  transition: width .1s linear;
}
/* sections */

.nav-06__hero {
  padding: 100px 48px;
  max-width: 800px;
  margin: 0 auto;
}

.nav-06__hero h1 {
  font-size: clamp(2.5rem,5vw,4rem);
  font-weight: 700;
  color: var(--text);
  letter-spacing: -.04em;
  line-height: 1.1;
  margin-bottom: 20px;
}

.nav-06__hero h1 span {
  color: var(--accent);
}

.nav-06__hero p {
  font-size: 1.0625rem;
  color: var(--muted);
  max-width: 520px;
  line-height: 1.7;
  margin-bottom: 32px;
}

.nav-06__scroll-hint {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  color: var(--accent);
  font-size: .875rem;
  font-weight: 600;
  animation: nav-06-bounce 1.5s ease-in-out infinite;
}

.nav-06__scroll-hint svg {
  width: 18px;
  height: 18px;
  stroke: currentColor;
  fill: none;
  stroke-width: 2;
}

@keyframes nav-06-bounce {
  0%,
    100% {
    transform: translateY(0);
  }

  50% {
    transform: translateY(5px);
  }
}

.nav-06__content {
  padding: 60px 48px;
  max-width: 800px;
  margin: 0 auto;
}

.nav-06__card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 28px;
  margin-bottom: 24px;
}

.nav-06__card h3 {
  font-size: 1.125rem;
  font-weight: 600;
  color: var(--text);
  margin-bottom: 8px;
}

.nav-06__card p {
  color: var(--muted);
  line-height: 1.65;
  font-size: .9375rem;
}

@media (max-width: 640px) {
  .nav-06__links,
    .nav-06__btn--ghost {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nav-06__bar,
    .nav-06__logo,
    .nav-06__logo-leaf,
    .nav-06__btn,
    .nav-06__scroll-hint {
    transition: none;
    animation: none;
  }
}
```

## JavaScript
```js
(function(){
  var bar=document.getElementById('nav-06-bar');
  var prog=document.getElementById('nav-06-progress');
  function onScroll(){
    var y=window.scrollY;
    bar.classList.toggle('nav-06--shrunk',y>60);
    var doc=document.documentElement;
    var pct=y/(doc.scrollHeight-doc.clientHeight)*100;
    prog.style.width=Math.min(pct,100)+'%';
  }
  window.addEventListener('scroll',onScroll,{passive:true});
}());
```
