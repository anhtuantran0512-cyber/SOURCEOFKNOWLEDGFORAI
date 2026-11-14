---
source: "codefronts"
url: "https://codefronts.com/motion/css-neon-text-effect/interactive-neon-on-off-sign-switch/"
title: "Interactive Neon On/Off Sign Switch"
section: "motion"
category: "css-neon-text-effect"
category_name: "CSS Neon Text Effects"
description: "A neon sign with a physical pull-switch: dark and dead until you flip it, then it strikes to life with a realistic warm-up stutter."
has_js: "true"
---

Here's a working CSS Neon Text Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Interactive Neon On/Off Sign Switch
Source: https://codefronts.com/motion/css-neon-text-effect/interactive-neon-on-off-sign-switch/

A neon sign with a physical pull-switch: dark and dead until you flip it, then it strikes to life with a realistic warm-up stutter. The interactive 'turn the sign on' pattern gap that plain glow demos miss.
## HTML
```html
<div class="cnt-18 is-off" id="cnt-18">
  <div class="cnt-18__sign">
    <span class="cnt-18__tube">MOTEL</span>
    <span class="cnt-18__tube cnt-18__sub">no vacancy</span>
  </div>
  <button class="cnt-18__switch" type="button" id="cnt-18-switch" aria-pressed="false">
    <span class="cnt-18__knob"></span><span class="cnt-18__stext">flip the switch</span>
  </button>
</div>
```
## CSS
```css
.cnt-18,
.cnt-18 *,
.cnt-18 *::before,
.cnt-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cnt-18 ::selection {
  background: oklch(0.78 0.19 25);
  color: #fff;
}

.cnt-18 {
  --accent: oklch(0.78 0.2 25);
  --off: color-mix(in oklch,var(--accent) 16%,#241417);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  gap: 44px;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background: radial-gradient(90% 90% at 50% 40%,#130d0f,#060405);
}

.cnt-18__sign {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}

.cnt-18__tube {
  font-size: clamp(48px,12vw,110px);
  font-weight: 900;
  letter-spacing: .08em;
  line-height: 1;
  color: var(--off);
  text-shadow: none;
  transition: color .3s;
}

.cnt-18__sub {
  font-size: clamp(18px,4vw,32px);
  letter-spacing: .32em;
}

.cnt-18.is-on .cnt-18__tube {
  color: var(--accent);
  animation: cnt-18-strike 1.1s ease both;
}

.cnt-18.is-on .cnt-18__sub {
  animation-delay: .35s;
}

@keyframes cnt-18-strike {
  0% {
    color: var(--off);
    text-shadow: none;
  }

  12% {
    color: #fff;
    text-shadow: 0 0 6px #fff,0 0 16px var(--accent);
  }

  16% {
    color: var(--off);
    text-shadow: none;
  }

  28% {
    color: #fff;
    text-shadow: 0 0 6px #fff,0 0 18px var(--accent);
  }

  33% {
    color: var(--off);
    text-shadow: none;
  }

  45% {
    color: var(--accent);
    text-shadow: 0 0 6px #fff,0 0 18px var(--accent),0 0 40px var(--accent);
  }

  100% {
    color: var(--accent);
    text-shadow: 0 0 5px #fff,0 0 15px var(--accent),0 0 36px var(--accent),0 0 72px var(--accent);
  }
}

.cnt-18.is-on .cnt-18__tube {
  text-shadow: 0 0 5px #fff,0 0 15px var(--accent),0 0 36px var(--accent),0 0 72px var(--accent);
}

.cnt-18__switch {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  cursor: pointer;
  padding: 8px 18px 8px 8px;
  border-radius: 999px;
  border: 1px solid #2c1e21;
  background: #120c0e;
  font: 12px ui-monospace,Menlo,monospace;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: #9a7f84;
}

.cnt-18__knob {
  width: 44px;
  height: 24px;
  border-radius: 999px;
  background: #241417;
  position: relative;
  transition: background .25s;
}

.cnt-18__knob::after {
  content: "";
  position: absolute;
  top: 3px;
  left: 3px;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: #6b5257;
  transition: transform .25s,background .25s;
}

.cnt-18.is-on .cnt-18__knob {
  background: color-mix(in oklch,var(--accent) 40%,#241417);
}

.cnt-18.is-on .cnt-18__knob::after {
  transform: translateX(20px);
  background: var(--accent);
  box-shadow: 0 0 12px var(--accent);
}

@media (prefers-reduced-motion: reduce) {
  .cnt-18.is-on .cnt-18__tube {
    animation: none;
  }
}
```

## JavaScript
```js
(function(){
  var root = document.getElementById('cnt-18');
  var btn = document.getElementById('cnt-18-switch');
  if(!root || !btn) return;
  btn.addEventListener('click', function(){
    var on = root.classList.toggle('is-on');
    root.classList.toggle('is-off', !on);
    btn.setAttribute('aria-pressed', String(on));
  });
})();
```
