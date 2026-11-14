---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-liquid-glass-effects/liquid-glass-theme-switcher/"
title: "Liquid Glass Theme Switcher"
section: "design-styles"
category: "css-liquid-glass-effects"
category_name: "CSS Liquid Glass Effects"
description: "A dark/light toggle with wow-factor: tapping it releases a liquid glass ripple that sweeps across a card and flips the whole scene's theme mid-wave."
has_js: "true"
---

Here's a working CSS Liquid Glass Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Liquid Glass Theme Switcher
Source: https://codefronts.com/design-styles/css-liquid-glass-effects/liquid-glass-theme-switcher/

A dark/light toggle with wow-factor: tapping it releases a liquid glass ripple that sweeps across a card and flips the whole scene's theme mid-wave. A sun/moon glass knob slides inside a frosted capsule. Uses the View-Transitions-style circular reveal, hand-rolled for broad support.
## HTML
```html
<section class="lg-06" id="lg-06-root" data-theme="dark" aria-label="Liquid glass theme switcher">
  <div class="lg-06__card">
    <h3 class="lg-06__title">Good evening</h3>
    <p class="lg-06__text">Toggle the switch — a liquid glass ripple sweeps the new theme across the scene.</p>
    <button class="lg-06__switch" id="lg-06-switch" type="button" role="switch" aria-checked="true" aria-label="Toggle dark mode">
      <span class="lg-06__knob" id="lg-06-knob"><span class="lg-06__ico lg-06__ico--moon">☾</span><span class="lg-06__ico lg-06__ico--sun">☀</span></span>
    </button>
  </div>
</section>
```
## CSS
```css
.lg-06,
.lg-06 *,
.lg-06 *::before,
.lg-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lg-06 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  transition: background .1s;
}

.lg-06[data-theme=dark] {
  --bg: radial-gradient(circle at 30% 20%,#241f3a,#0e0b1a);
  --surface: color-mix(in oklab,white 12%,transparent);
  --fg: #f2f0fa;
  --muted: rgba(255,255,255,.75);
  --rim: rgba(255,255,255,.35);
  --track: rgba(120,110,160,.5);
}

.lg-06[data-theme=light] {
  --bg: radial-gradient(circle at 70% 10%,#eaf1ff,#cdd8f0);
  --surface: color-mix(in oklab,white 55%,transparent);
  --fg: #161425;
  --muted: rgba(30,28,50,.7);
  --rim: rgba(255,255,255,.8);
  --track: rgba(255,255,255,.6);
}

.lg-06 {
  background: var(--bg);
}

.lg-06__card {
  position: relative;
  width: min(400px,92vw);
  padding: 34px;
  border-radius: 26px;
  color: var(--fg);
  background: var(--surface);
  border: 1px solid var(--rim);
  box-shadow: inset 0 1px 0 var(--rim),0 30px 60px -30px rgba(0,0,0,.5);
  backdrop-filter: blur(20px) saturate(170%);
  -webkit-backdrop-filter: blur(20px) saturate(170%);
}

.lg-06__title {
  font-size: 26px;
  font-weight: 800;
  margin-bottom: 8px;
}

.lg-06__text {
  font-size: 15px;
  line-height: 1.6;
  color: var(--muted);
  margin-bottom: 22px;
}

.lg-06__switch {
  position: relative;
  width: 76px;
  height: 38px;
  border-radius: 999px;
  border: 1px solid var(--rim);
  background: var(--track);
  cursor: pointer;
  padding: 0;
  box-shadow: inset 0 2px 8px rgba(0,0,0,.3);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
}

.lg-06__switch:focus-visible {
  outline: 3px solid var(--fg);
  outline-offset: 3px;
}

.lg-06__knob {
  position: absolute;
  top: 3px;
  left: 3px;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  background: linear-gradient(180deg,rgba(255,255,255,.95),rgba(255,255,255,.7));
  box-shadow: 0 4px 10px rgba(0,0,0,.35),inset 0 1px 0 #fff;
  transition: left .4s cubic-bezier(.5,-.3,.4,1.4);
}

.lg-06[data-theme=light] .lg-06__knob {
  left: 41px;
}

.lg-06__ico {
  position: absolute;
  font-size: 16px;
  transition: opacity .3s;
}

.lg-06__ico--moon {
  color: #3a3560;
}

.lg-06__ico--sun {
  color: #e0a020;
}

.lg-06[data-theme=dark] .lg-06__ico--sun {
  opacity: 0;
}

.lg-06[data-theme=light] .lg-06__ico--moon {
  opacity: 0;
}

.lg-06__ripple {
  position: fixed;
  border-radius: 50%;
  pointer-events: none;
  z-index: 9999;
  background: var(--surface);
  border: 1px solid var(--rim);
  backdrop-filter: blur(26px) saturate(180%);
  -webkit-backdrop-filter: blur(26px) saturate(180%);
  animation: lg-06-ripple .6s ease-out forwards;
}

@keyframes lg-06-ripple {
  from {
    transform: scale(0);
    opacity: .9;
  }

  to {
    transform: scale(1);
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .lg-06__knob {
    transition: none;
  }

  .lg-06__ripple {
    display: none;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('#lg-06-root');
  const sw = root.querySelector('#lg-06-switch');
  const knob = root.querySelector('#lg-06-knob');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  function apply(){ const next = root.dataset.theme === 'dark' ? 'light' : 'dark'; root.dataset.theme = next; sw.setAttribute('aria-checked', next === 'light'); root.querySelector('.lg-06__title').textContent = next === 'light' ? 'Good morning' : 'Good evening'; }
  function ripple(){
    const r = knob.getBoundingClientRect();
    const cx = r.left + r.width/2, cy = r.top + r.height/2;
    const far = Math.hypot(Math.max(cx, innerWidth-cx), Math.max(cy, innerHeight-cy));
    const el = document.createElement('span');
    el.className = 'lg-06__ripple';
    el.style.left = (cx-far)+'px'; el.style.top = (cy-far)+'px'; el.style.width = el.style.height = (far*2)+'px';
    document.body.appendChild(el);
    el.addEventListener('animationend', () => el.remove(), {once:true});
  }
  sw.addEventListener('click', () => {
    if (reduce){ apply(); return; }
    ripple(); setTimeout(apply, 180);
  });
})();
```
