---
source: "codefronts"
url: "https://codefronts.com/motion/css-neon-text-effect/css-variables-dynamic-neon-colour/"
title: "CSS Variables Dynamic Neon Colour"
section: "motion"
category: "css-neon-text-effect"
category_name: "CSS Neon Text Effects"
description: "One registered @property --hue drives the entire glow spectrum — text colour and every shadow layer — so a single slider retints the whole sign live."
has_js: "true"
---

Here's a working CSS Neon Text Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Variables Dynamic Neon Colour
Source: https://codefronts.com/motion/css-neon-text-effect/css-variables-dynamic-neon-colour/

One registered @property --hue drives the entire glow spectrum — text colour and every shadow layer — so a single slider retints the whole sign live. The clean-token setup front-end engineers search for.
## HTML
```html
<div class="cnt-14">
  <div class="cnt-14__stack">
    <h2 class="cnt-14__h" id="cnt-14-sign">SPECTRUM</h2>
    <label class="cnt-14__ctrl">hue
      <input id="cnt-14-range" type="range" min="0" max="360" value="200" aria-label="Neon hue">
    </label>
  </div>
</div>
```
## CSS
```css
.cnt-14,
.cnt-14 *,
.cnt-14 *::before,
.cnt-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cnt-14 ::selection {
  background: #fff;
  color: #000;
}

@property --hue {
  syntax: '<angle>';
  inherits: true;
  initial-value: 200deg;
}

.cnt-14 {
  --hue: 200deg;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background: radial-gradient(120% 120% at 50% 30%,#0a0a0e,#050506);
}

.cnt-14__stack {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 34px;
}

.cnt-14__h {
  --c: oklch(0.82 0.19 var(--hue));
  font-size: clamp(46px,12vw,116px);
  font-weight: 900;
  letter-spacing: .05em;
  color: var(--c);
  text-shadow: 0 0 5px #fff,0 0 14px var(--c),0 0 34px var(--c),0 0 72px color-mix(in oklch,var(--c) 55%,transparent);
  animation: cnt-14-cycle 12s linear infinite;
}

@keyframes cnt-14-cycle {
  to {
    --hue: 560deg;
  }
}

.cnt-14__ctrl {
  display: flex;
  align-items: center;
  gap: 14px;
  font: 12px ui-monospace,Menlo,monospace;
  letter-spacing: .24em;
  text-transform: uppercase;
  color: #8a8a95;
}

.cnt-14__ctrl input {
  width: 220px;
  accent-color: oklch(0.82 0.19 var(--hue));
}

@media (prefers-reduced-motion: reduce) {
  .cnt-14__h {
    animation: none;
  }
}
```

## JavaScript
```js
(function(){
  var r = document.getElementById('cnt-14-range');
  var sign = document.getElementById('cnt-14-sign');
  if(!r || !sign) return;
  r.addEventListener('input', function(){
    // scrubbing overrides the idle cycle with an explicit hue
    sign.style.animation = 'none';
    sign.style.setProperty('--hue', r.value + 'deg');
  });
})();
```
