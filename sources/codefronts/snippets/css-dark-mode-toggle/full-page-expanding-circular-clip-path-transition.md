---
source: "codefronts"
url: "https://codefronts.com/snippets/css-dark-mode-toggle/full-page-expanding-circular-clip-path-transition/"
title: "Full-Page Expanding Circular Clip-Path Transition"
section: "snippets"
category: "css-dark-mode-toggle"
category_name: "CSS Dark Mode Toggles"
description: "A cinematic radial wipe where the dark theme expands as a growing circle from the exact pixel position of the button click — achieved with clip-path:…"
has_js: "true"
---

Here's a working CSS Dark Mode Toggle from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Full-Page Expanding Circular Clip-Path Transition
Source: https://codefronts.com/snippets/css-dark-mode-toggle/full-page-expanding-circular-clip-path-transition/

A cinematic radial wipe where the dark theme expands as a growing circle from the exact pixel position of the button click — achieved with clip-path: circle() and CSS custom properties for the origin point.
## HTML
```html
<div class="dm-08" id="dm-08-root">
  <!-- Light layer -->
  <div class="dm-08__layer dm-08__layer--light">
    <div class="dm-08__hero-l">
      <div class="dm-08__tag-l">✦ CSS clip-path wipe</div>
      <h2 class="dm-08__title-l">Radial Wipe<br>Transition</h2>
      <p class="dm-08__body-l">Click the button to trigger a radial clip-path expansion from the click origin — a cinematic full-page reveal built in pure CSS, no canvas required.</p>
    </div>
    <button class="dm-08__fab dm-08__fab--light" id="dm-08-btn-l" aria-label="Switch to dark mode">🌑</button>
    <span class="dm-08__hint dm-08__hint--light">Click anywhere on button to expand</span>
  </div>
  <!-- Dark layer -->
  <div class="dm-08__layer dm-08__layer--dark" id="dm-08-dark">
    <div class="dm-08__grid-d"></div>
    <div id="dm-08-particles"></div>
    <div class="dm-08__hero-d">
      <div class="dm-08__tag-d">◈ Cyberpunk mode</div>
      <h2 class="dm-08__title-d">System<br>Override</h2>
      <p class="dm-08__body-d">The dark layer expands via <code>clip-path: circle(0% → 160%)</code>, origin set to your click coordinates via CSS custom properties <code>--ox</code> and <code>--oy</code>.</p>
    </div>
    <button class="dm-08__fab dm-08__fab--dark" id="dm-08-btn-d" aria-label="Switch to light mode">☀️</button>
    <span class="dm-08__hint dm-08__hint--dark">Click to collapse the portal</span>
  </div>
</div>
```
## CSS
```css
.dm-08,
.dm-08 *,
.dm-08 *::before,
.dm-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.dm-08 ::selection {
  background: #f0abfc;
  color: #4a044e;
}

.dm-08 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  min-height: 100vh;
  position: relative;
  overflow: hidden;
}
/* Light layer */

.dm-08__layer {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  gap: 32px;
}

.dm-08__layer--light {
  background: linear-gradient(135deg,#fdf4ff,#f0e6ff,#e0f2fe);
  z-index: 1;
}

.dm-08__layer--dark {
  background: linear-gradient(135deg,#0d0014,#12002a,#001a2e);
  z-index: 2;
  clip-path: circle(0% at 50% 100%);
  transition: none;
}

.dm-08__layer--dark.is-expanding {
  transition: clip-path 0.9s cubic-bezier(0.76,0,0.24,1);
  clip-path: circle(160% at var(--ox,50%) var(--oy,100%));
}

.dm-08__layer--dark.is-done {
  clip-path: circle(160% at var(--ox,50%) var(--oy,100%));
  transition: none;
}

.dm-08__layer--dark.is-collapsing {
  transition: clip-path 0.9s cubic-bezier(0.76,0,0.24,1);
  clip-path: circle(0% at var(--ox,50%) var(--oy,100%));
}
/* Light layer content */

.dm-08__hero-l {
  text-align: center;
  max-width: 400px;
}

.dm-08__tag-l {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 4px 14px;
  border-radius: 99px;
  background: rgba(168,85,247,0.12);
  border: 1px solid rgba(168,85,247,0.25);
  color: #7e22ce;
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin-bottom: 16px;
}

.dm-08__title-l {
  font-size: clamp(1.8rem,5vw,2.8rem);
  font-weight: 900;
  letter-spacing: -0.04em;
  background: linear-gradient(135deg,#7e22ce,#be185d,#0891b2);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  line-height: 1.1;
  margin-bottom: 12px;
}

.dm-08__body-l {
  font-size: 0.88rem;
  line-height: 1.65;
  color: #6b7280;
  margin-bottom: 24px;
}
/* Dark layer content */

.dm-08__hero-d {
  text-align: center;
  max-width: 400px;
}

.dm-08__tag-d {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 4px 14px;
  border-radius: 99px;
  background: rgba(240,171,252,0.1);
  border: 1px solid rgba(240,171,252,0.2);
  color: #f0abfc;
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin-bottom: 16px;
}

.dm-08__title-d {
  font-size: clamp(1.8rem,5vw,2.8rem);
  font-weight: 900;
  letter-spacing: -0.04em;
  background: linear-gradient(135deg,#f0abfc,#818cf8,#67e8f9);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  line-height: 1.1;
  margin-bottom: 12px;
}

.dm-08__body-d {
  font-size: 0.88rem;
  line-height: 1.65;
  color: #9ca3af;
  margin-bottom: 24px;
}
/* Grid decoration */

.dm-08__grid-d {
  position: absolute;
  inset: 0;
  background-image: linear-gradient(rgba(240,171,252,0.04) 1px,transparent 1px), linear-gradient(90deg,rgba(240,171,252,0.04) 1px,transparent 1px);
  background-size: 40px 40px;
  pointer-events: none;
}
/* Floating particles in dark */

.dm-08__particle {
  position: absolute;
  border-radius: 50%;
  pointer-events: none;
  animation: dm-08-float linear infinite;
}

@keyframes dm-08-float {
  0% {
    transform: translateY(0) rotate(0deg);
    opacity: 0;
  }

  10% {
    opacity: 1;
  }

  90% {
    opacity: 1;
  }

  100% {
    transform: translateY(-100vh) rotate(720deg);
    opacity: 0;
  }
}
/* FAB button */

.dm-08__fab {
  width: 72px;
  height: 72px;
  border-radius: 50%;
  border: none;
  cursor: pointer;
  position: relative;
  overflow: visible;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 26px;
  transition: transform 0.2s ease,box-shadow 0.3s ease;
  z-index: 10;
}

.dm-08__fab:hover {
  transform: scale(1.1);
}

.dm-08__fab:active {
  transform: scale(0.93);
}

.dm-08__fab--light {
  background: linear-gradient(135deg,#7e22ce,#be185d);
  box-shadow: 0 6px 30px rgba(126,34,206,0.4),0 2px 8px rgba(0,0,0,0.2);
  color: #fff;
}

.dm-08__fab--dark {
  background: linear-gradient(135deg,#f0abfc,#818cf8);
  box-shadow: 0 6px 30px rgba(240,171,252,0.4),0 0 60px rgba(129,140,248,0.2);
  color: #1e0a3c;
}
/* Ripple ring animation */

.dm-08__ripple {
  position: fixed;
  border-radius: 50%;
  border: 2px solid rgba(168,85,247,0.4);
  pointer-events: none;
  z-index: 20;
  transform: translate(-50%,-50%) scale(0);
  animation: dm-08-ripple 0.6s ease-out forwards;
}

@keyframes dm-08-ripple {
  to {
    transform: translate(-50%,-50%) scale(6);
    opacity: 0;
  }
}
/* Instruction tooltip */

.dm-08__hint {
  padding: 10px 18px;
  border-radius: 99px;
  font-size: 0.75rem;
  font-weight: 600;
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
}

.dm-08__hint--light {
  background: rgba(255,255,255,0.7);
  border: 1px solid rgba(168,85,247,0.2);
  color: #7e22ce;
}

.dm-08__hint--dark {
  background: rgba(255,255,255,0.06);
  border: 1px solid rgba(240,171,252,0.15);
  color: #f0abfc;
}

@media (prefers-reduced-motion: reduce) {
  .dm-08__layer--dark {
    clip-path: circle(0%) !important;
    transition: none!important;
  }

  .dm-08__layer--dark.is-expanding,
    .dm-08__layer--dark.is-done {
    clip-path: circle(100%) !important;
  }

  .dm-08__particle {
    animation: none!important;
  }
}
```

## JavaScript
```js
(()=>{
  const root=document.getElementById('dm-08-root');
  const dark=document.getElementById('dm-08-dark');
  const btnL=document.getElementById('dm-08-btn-l');
  const btnD=document.getElementById('dm-08-btn-d');
  const particles=document.getElementById('dm-08-particles');
  let isDark=false;
  function spawnParticles(){
    particles.innerHTML='';
    const colors=['#f0abfc','#818cf8','#67e8f9','#a78bfa','#fbbf24'];
    for(let i=0;i<12;i++){
      const p=document.createElement('div');
      p.className='dm-08__particle';
      const size=Math.random()*4+2;
      p.style.cssText=`
        width:${size}px;height:${size}px;
        background:${colors[Math.floor(Math.random()*colors.length)]};
        left:${Math.random()*100}%;
        bottom:-20px;
        animation-duration:${4+Math.random()*6}s;
        animation-delay:${Math.random()*4}s;
        opacity:0.6;
      `;
      particles.appendChild(p);
    }
  }
  function createRipple(e,el){
    const rect=el.getBoundingClientRect();
    const r=document.createElement('div');
    r.className='dm-08__ripple';
    r.style.left=(rect.left+rect.width/2)+'px';
    r.style.top=(rect.top+rect.height/2)+'px';
    r.style.width='60px';r.style.height='60px';
    document.body.appendChild(r);
    setTimeout(()=>r.remove(),600);
  }
  btnL.addEventListener('click',(e)=>{
    if(isDark)return;
    createRipple(e,btnL);
    const rect=btnL.getBoundingClientRect();
    const ox=((rect.left+rect.width/2)/window.innerWidth*100).toFixed(1)+'%';
    const oy=((rect.top+rect.height/2)/window.innerHeight*100).toFixed(1)+'%';
    dark.style.setProperty('--ox',ox);
    dark.style.setProperty('--oy',oy);
    dark.classList.remove('is-done','is-collapsing');
    dark.classList.add('is-expanding');
    spawnParticles();
    isDark=true;
    setTimeout(()=>{ dark.classList.remove('is-expanding');dark.classList.add('is-done'); },920);
  });
  btnD.addEventListener('click',(e)=>{
    if(!isDark)return;
    createRipple(e,btnD);
    dark.classList.remove('is-done','is-expanding');
    dark.classList.add('is-collapsing');
    isDark=false;
    setTimeout(()=>{ dark.classList.remove('is-collapsing');particles.innerHTML=''; },920);
  });
})();
```
