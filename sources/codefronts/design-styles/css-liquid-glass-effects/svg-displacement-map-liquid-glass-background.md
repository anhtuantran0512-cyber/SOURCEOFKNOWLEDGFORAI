---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-liquid-glass-effects/svg-displacement-map-liquid-glass-background/"
title: "SVG Displacement Map Liquid Glass Background"
section: "design-styles"
category: "css-liquid-glass-effects"
category_name: "CSS Liquid Glass Effects"
description: "The real thing: true organic refraction that CSS blur can't do."
has_js: "true"
---

Here's a working CSS Liquid Glass Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: SVG Displacement Map Liquid Glass Background
Source: https://codefronts.com/design-styles/css-liquid-glass-effects/svg-displacement-map-liquid-glass-background/

The real thing: true organic refraction that CSS blur can't do. An SVG feTurbulence + feDisplacementMap filter physically warps and bends the background image beneath a glass panel, and the warp intensity follows your cursor — recreating Apple's physics-based light-through-glass distortion.
## HTML
```html
<section class="lg-08" id="lg-08-root" aria-label="SVG displacement map liquid glass background">
  <svg class="lg-08__svg" viewBox="0 0 600 380" width="600" height="380" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
    <defs>
      <filter id="lg-08-warp" x="-20%" y="-20%" width="140%" height="140%">
        <feTurbulence id="lg-08-turb" type="fractalNoise" baseFrequency="0.012 0.02" numOctaves="2" seed="7" result="noise"/>
        <feDisplacementMap id="lg-08-disp" in="SourceGraphic" in2="noise" scale="14" xChannelSelector="R" yChannelSelector="G"/>
      </filter>
    </defs>
    <image href="https://picsum.photos/seed/lgwarp/600/380" x="0" y="0" width="600" height="380" preserveAspectRatio="xMidYMid slice" filter="url(#lg-08-warp)"/>
  </svg>
  <div class="lg-08__panel">
    <span class="lg-08__tag">SVG feDisplacementMap</span>
    <h3 class="lg-08__title">Real refraction</h3>
    <p class="lg-08__text">Move your cursor — the image bends through the glass. This is displacement, not blur.</p>
  </div>
</section>
```
## CSS
```css
.lg-08,
.lg-08 *,
.lg-08 *::before,
.lg-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lg-08 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background: #0c0a16;
}

.lg-08 {
  position: relative;
}

.lg-08__svg {
  position: absolute;
  width: min(720px,94vw);
  height: auto;
  border-radius: 26px;
  overflow: hidden;
  box-shadow: 0 40px 80px -34px rgba(0,0,0,.8);
  filter: saturate(120%);
}

.lg-08__panel {
  position: relative;
  z-index: 2;
  width: min(360px,84vw);
  padding: 28px;
  border-radius: 22px;
  color: #fff;
  background: color-mix(in oklab,white 10%,transparent);
  border: 1px solid rgba(255,255,255,.32);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.45),0 20px 50px -26px rgba(0,0,0,.6);
  backdrop-filter: blur(6px) saturate(150%);
  -webkit-backdrop-filter: blur(6px) saturate(150%);
}

.lg-08__tag {
  display: inline-block;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  padding: 5px 11px;
  border-radius: 999px;
  background: rgba(255,255,255,.2);
  border: 1px solid rgba(255,255,255,.35);
}

.lg-08__title {
  font-size: 28px;
  font-weight: 800;
  margin: 14px 0 8px;
  letter-spacing: -.02em;
}

.lg-08__text {
  font-size: 15px;
  line-height: 1.6;
  color: rgba(255,255,255,.9);
  text-shadow: 0 1px 8px rgba(0,0,0,.4);
}

@media (prefers-reduced-motion: reduce) {
  .lg-08__svg {
    filter: none;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('#lg-08-root');
  const disp = root.querySelector('#lg-08-disp');
  const turb = root.querySelector('#lg-08-turb');
  const svg = root.querySelector('.lg-08__svg');
  if (!disp) return;
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const BASE = 14, MAX = 40;
  let target = BASE, current = BASE, raf = null;
  function tick(){
    current += (target - current) * 0.12;
    disp.setAttribute('scale', current.toFixed(2));
    if (Math.abs(target - current) > 0.2){ raf = requestAnimationFrame(tick); } else { disp.setAttribute('scale', target.toFixed(2)); raf = null; }
  }
  function kick(){ if (!raf) raf = requestAnimationFrame(tick); }
  root.addEventListener('pointermove', e => {
    if (reduce) return;
    const r = svg.getBoundingClientRect();
    const dx = Math.abs((e.clientX - (r.left+r.width/2)) / (r.width/2));
    const dy = Math.abs((e.clientY - (r.top+r.height/2)) / (r.height/2));
    target = BASE + Math.min(1, (dx+dy)/2) * (MAX - BASE);
    const f = 0.012 + Math.min(1,(dx+dy)/2)*0.02;
    turb.setAttribute('baseFrequency', f.toFixed(4) + ' ' + (f*1.6).toFixed(4));
    kick();
  });
  root.addEventListener('pointerleave', () => { target = BASE; kick(); });
})();
```
