---
source: "codefronts"
url: "https://codefronts.com/navigation/css-navigation-menu-designs/css-navigation-with-magnetic-hover-effect/"
title: "CSS Navigation with Magnetic Hover Effect"
section: "navigation"
category: "css-navigation-menu-designs"
category_name: "CSS Navigation Menus"
description: "An interactive navigation bar where menu items subtly attract to the cursor using a magnetic effect."
has_js: "true"
---

Here's a working CSS Navigation Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Navigation with Magnetic Hover Effect
Source: https://codefronts.com/navigation/css-navigation-menu-designs/css-navigation-with-magnetic-hover-effect/

An interactive navigation bar where menu items subtly attract to the cursor using a magnetic effect. CSS custom properties `--dx` and `--dy` are updated on mouse move via JavaScript, and CSS `translate` applies the offset — creating a fluid, physics-inspired hover interaction.
## HTML
```html
<div class="nav-13">
  <div class="nav-13__glow" id="nav-13-glow"></div>
  <div class="nav-13__ring"></div>
  <div class="nav-13__ring"></div>
  <nav class="nav-13__bar" role="navigation">
    <a href="#" class="nav-13__logo">Arp<span>.</span></a>
    <ul class="nav-13__links">
      <li><a href="#" class="nav-13__mag">Work</a></li>
      <li><a href="#" class="nav-13__mag">Studio</a></li>
      <li><a href="#" class="nav-13__mag">Process</a></li>
      <li><a href="#" class="nav-13__mag">Journal</a></li>
    </ul>
    <a href="#" class="nav-13__cta nav-13__mag">Let's talk →</a>
  </nav>
  <div class="nav-13__hero">
    <p class="nav-13__label">Creative Direction & Design</p>
    <h1>Move the cursor<br><span>near the nav</span></h1>
    <p>Navigation links react magnetically to the cursor — a CSS custom property trick where JS writes <code>--dx</code>/<code>--dy</code> values and CSS <code>transform: translate()</code> picks them up, keeping animation on the compositor.</p>
  </div>
</div>

```
## CSS
```css
.nav-13,
.nav-13 *,
.nav-13 *::before,
.nav-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.nav-13 ::selection {
  background: #fbbf24;
  color: #000;
}

.nav-13 {
  --bg: #070707;
  --text: #fafafa;
  --muted: #737373;
  --accent: #fbbf24;
  --border: rgba(255,255,255,.08);
  font-family: 'Space Grotesk',system-ui,sans-serif;
  background: var(--bg);
  min-height: 100vh;
  overflow: hidden;
}
/* cursor glow */

.nav-13__glow {
  position: fixed;
  width: 400px;
  height: 400px;
  border-radius: 50%;
  background: radial-gradient(circle,rgba(251,191,36,.06) 0%,transparent 70%);
  pointer-events: none;
  transform: translate(-50%,-50%);
  z-index: 0;
  transition: transform .12s ease;
  will-change: transform;
}
/* bar */

.nav-13__bar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 100;
  padding: 28px 48px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.nav-13__logo {
  font-size: 1.4rem;
  font-weight: 700;
  color: var(--text);
  letter-spacing: -.04em;
  position: relative;
  z-index: 1;
  text-decoration: none;
}

.nav-13__logo span {
  color: var(--accent);
}

.nav-13__links {
  display: flex;
  align-items: center;
  gap: 8px;
  list-style: none;
  position: relative;
  z-index: 1;
}

.nav-13__links li {
  position: relative;
}

.nav-13__links a {
  display: block;
  padding: 10px 16px;
  color: var(--muted);
  text-decoration: none;
  font-size: .9375rem;
  font-weight: 500;
  border-radius: 10px;
  transition: color .15s;
  position: relative;
  z-index: 1;
}
/* hover bg pill */

.nav-13__links a::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 10px;
  background: rgba(255,255,255,.05);
  transform: scale(.8);
  opacity: 0;
  transition: transform .22s cubic-bezier(.34,1.56,.64,1),opacity .2s;
  z-index: -1;
}

.nav-13__links a:hover {
  color: var(--text);
}

.nav-13__links a:hover::before {
  transform: scale(1);
  opacity: 1;
}
/* magnetic effect via CSS custom props set by JS */

.nav-13__links a {
  --dx: 0px;
  --dy: 0px;
  transform: translate(var(--dx),var(--dy));
  transition: color .15s,transform .3s cubic-bezier(.34,1.56,.64,1);
}
/* CTA button */

.nav-13__cta {
  position: relative;
  z-index: 1;
  padding: 10px 22px;
  border-radius: 10px;
  background: var(--accent);
  color: #000;
  text-decoration: none;
  font-weight: 700;
  font-size: .875rem;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: transform .3s cubic-bezier(.34,1.56,.64,1),box-shadow .2s;
  --dx: 0px;
  --dy: 0px;
  transform: translate(var(--dx),var(--dy));
}

.nav-13__cta:hover {
  box-shadow: 0 0 30px rgba(251,191,36,.3);
}
/* hero */

.nav-13__hero {
  position: relative;
  z-index: 1;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 120px 24px 60px;
}

.nav-13__label {
  font-size: .75rem;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 24px;
}

.nav-13__hero h1 {
  font-size: clamp(3rem,9vw,7rem);
  font-weight: 700;
  color: var(--text);
  letter-spacing: -.05em;
  line-height: .95;
  margin-bottom: 24px;
}

.nav-13__hero h1 span {
  color: transparent;
  -webkit-text-stroke: 1px rgba(255,255,255,.2);
}

.nav-13__hero p {
  font-size: 1rem;
  color: var(--muted);
  max-width: 420px;
  line-height: 1.65;
}
/* magnetic ring decoration */

.nav-13__ring {
  position: absolute;
  width: 600px;
  height: 600px;
  border: 1px solid rgba(255,255,255,.03);
  border-radius: 50%;
  pointer-events: none;
  z-index: 0;
}

.nav-13__ring:nth-child(2) {
  width: 900px;
  height: 900px;
  border-color: rgba(255,255,255,.02);
}

@media (max-width: 680px) {
  .nav-13__links {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nav-13__links a,
    .nav-13__cta {
    transition: none;
    transform: none!important;
  }

  .nav-13__glow {
    display: none;
  }
}
```

## JavaScript
```js
(function(){
  var glow=document.getElementById('nav-13-glow');
  var mags=document.querySelectorAll('.nav-13__mag');
  var strength=6;
  function onMove(e){
    var x=e.clientX,y=e.clientY;
    if(glow){glow.style.transform='translate(calc(-50% + '+x+'px),calc(-50% + '+y+'px)'}
    mags.forEach(function(el){
      var r=el.getBoundingClientRect();
      var cx=r.left+r.width/2,cy=r.top+r.height/2;
      var dx=x-cx,dy=y-cy;
      var dist=Math.sqrt(dx*dx+dy*dy);
      var radius=80;
      if(dist<radius){
        var f=(1-dist/radius)*strength;
        el.style.setProperty('--dx',(dx/dist*f)+'px');
        el.style.setProperty('--dy',(dy/dist*f)+'px');
      } else {
        el.style.setProperty('--dx','0px');
        el.style.setProperty('--dy','0px');
      }
    });
  }
  document.addEventListener('mousemove',onMove,{passive:true});
}());
```
