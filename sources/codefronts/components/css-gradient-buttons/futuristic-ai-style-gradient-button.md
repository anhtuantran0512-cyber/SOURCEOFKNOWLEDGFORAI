---
source: "codefronts"
url: "https://codefronts.com/components/css-gradient-buttons/futuristic-ai-style-gradient-button/"
title: "Futuristic AI Style Gradient Button"
section: "components"
category: "css-gradient-buttons"
category_name: "CSS Gradient Buttons"
description: "A 2027-grade AI console Generate button where every color derives from one @property-registered OKLCH hue that drifts through the full wheel, plus a JS…"
has_js: "true"
---

Here's a working CSS Gradient Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Futuristic AI Style Gradient Button
Source: https://codefronts.com/components/css-gradient-buttons/futuristic-ai-style-gradient-button/

A 2027-grade AI console Generate button where every color derives from one @property-registered OKLCH hue that drifts through the full wheel, plus a JS generating state with scanline acceleration and a hairline progress rail.
## HTML
```html
<div class="gb-13">
  <div class="gb-13__term">
    <div class="gb-13__bar">
      <span class="gb-13__dot" aria-hidden="true"></span>
      <span class="gb-13__dot" aria-hidden="true"></span>
      <span class="gb-13__dot" aria-hidden="true"></span>
      <span class="gb-13__title">Model · lumen-2</span>
    </div>
    <p class="gb-13__prompt"><b>&gt;</b> Render a photoreal glass sculpture of a hummingbird, studio lighting, 8k</p>
    <button class="gb-13__btn" id="gb-13-generate" type="button"><span class="gb-13__spark" aria-hidden="true">✦</span><span class="gb-13__label">Generate</span></button>
    <p class="gb-13__status" id="gb-13-status" role="status" aria-live="polite"></p>
  </div>
</div>
```
## CSS
```css
.gb-13,
.gb-13 *,
.gb-13 *::before,
.gb-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gb-13 ::selection {
  background: oklch(80% .18 300);
  color: #05060d;
}

@property --gb-13-hue {
  syntax: "<number>";
  initial-value: 280;
  inherits: true;
}

.gb-13 {
  --gb-13-hue: 280;
  --line: oklch(70% .2 var(--gb-13-hue));
  --line2: oklch(75% .19 calc(var(--gb-13-hue) + 80));
  --bg: #05060d;
  font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
  background: radial-gradient(600px 300px at 50% 120%,oklch(30% .1 var(--gb-13-hue) / .35),transparent 70%), var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 24px;
  animation: gb-13-huedrift 12s linear infinite;
}
/* The whole scene slowly rotates through OKLCH hue space — every
   colour below derives from one animated custom property. */

@keyframes gb-13-huedrift {
  from {
    --gb-13-hue: 280;
  }

  to {
    --gb-13-hue: 640;
  }
}

.gb-13__term {
  width: 100%;
  max-width: 440px;
  border: 1px solid oklch(35% .06 var(--gb-13-hue) / .8);
  border-radius: 18px;
  background: rgba(10,12,22,.85);
  padding: 26px 26px 30px;
}

.gb-13__bar {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 22px;
}

.gb-13__dot {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: oklch(60% .15 var(--gb-13-hue) / .5);
}

.gb-13__title {
  margin-left: auto;
  font-size: 11px;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: oklch(70% .05 var(--gb-13-hue));
}

.gb-13__prompt {
  font-family: ui-monospace,SFMono-Regular,Menlo,monospace;
  font-size: 13.5px;
  line-height: 1.7;
  color: #c9cfe8;
  background: rgba(255,255,255,.03);
  border: 1px solid rgba(255,255,255,.06);
  border-radius: 12px;
  padding: 16px 18px;
  margin-bottom: 24px;
}

.gb-13__prompt b {
  color: var(--line);
}

.gb-13__btn {
  position: relative;
  width: 100%;
  padding: 16px 30px;
  border: 1px solid transparent;
  border-radius: 14px;
  font-family: inherit;
  font-size: 15.5px;
  font-weight: 700;
  letter-spacing: .4px;
  color: #eef0ff;
  cursor: pointer;
  isolation: isolate;
  overflow: hidden;
  background: linear-gradient(rgba(10,12,22,.6),rgba(10,12,22,.6)) padding-box, linear-gradient(100deg,var(--line),var(--line2)) border-box;
  box-shadow: 0 0 0 1px oklch(70% .2 var(--gb-13-hue) / .1),0 14px 34px -16px oklch(60% .2 var(--gb-13-hue) / .7);
  transition: transform .25s ease,box-shadow .35s ease;
  -webkit-tap-highlight-color: transparent;
}
/* Ultra-fine scanline sweep inside the button */

.gb-13__btn::before {
  content: "";
  position: absolute;
  inset: 0;
  z-index: -1;
  background: linear-gradient(100deg,transparent 30%,oklch(80% .18 var(--gb-13-hue) / .18) 50%,transparent 70%);
  background-size: 250% 100%;
  animation: gb-13-scan 3s linear infinite;
}

@keyframes gb-13-scan {
  from {
    background-position: 200% 0;
  }

  to {
    background-position: -100% 0;
  }
}

.gb-13__btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 0 0 1px oklch(75% .2 var(--gb-13-hue) / .35),0 18px 44px -16px oklch(65% .22 var(--gb-13-hue) / .85);
}

.gb-13__btn:active {
  transform: translateY(0) scale(.99);
}

.gb-13__btn:focus-visible {
  outline: 2px solid var(--line);
  outline-offset: 4px;
}

.gb-13__spark {
  display: inline-block;
  margin-right: 8px;
}
/* Generating state (toggled by JS) — text swaps, sweep accelerates,
   a hairline progress rail lights along the bottom border */

.gb-13__btn.is-busy {
  pointer-events: none;
  color: oklch(85% .08 var(--gb-13-hue));
}

.gb-13__btn.is-busy::before {
  animation-duration: .9s;
}

.gb-13__btn::after {
  content: "";
  position: absolute;
  left: 8%;
  right: 92%;
  bottom: 0;
  height: 2px;
  border-radius: 2px;
  background: linear-gradient(90deg,var(--line),var(--line2));
  opacity: 0;
  transition: right 2.4s cubic-bezier(.3,.6,.3,1),opacity .3s ease;
}

.gb-13__btn.is-busy::after {
  right: 8%;
  opacity: 1;
}

.gb-13__status {
  margin-top: 16px;
  font-family: ui-monospace,SFMono-Regular,Menlo,monospace;
  font-size: 12px;
  min-height: 16px;
  color: oklch(65% .1 var(--gb-13-hue));
  transition: opacity .3s ease;
}

@media (prefers-reduced-motion: reduce) {
  .gb-13 {
    animation: none;
  }

  .gb-13__btn::before {
    animation: none;
  }

  .gb-13__btn,
    .gb-13__btn::after {
    transition: none;
  }

  .gb-13__btn:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(function () {
  var btn = document.getElementById('gb-13-generate');
  var status = document.getElementById('gb-13-status');
  if (!btn || !status) return;
  var label = btn.querySelector('.gb-13__label');
  var timers = [];
  btn.addEventListener('click', function () {
    if (btn.classList.contains('is-busy')) return;
    btn.classList.add('is-busy');
    label.textContent = 'Generating…';
    status.textContent = 'Sampling latents · step 1/24';
    timers.push(setTimeout(function () {
      status.textContent = 'Refining detail · step 18/24';
    }, 1100));
    timers.push(setTimeout(function () {
      btn.classList.remove('is-busy');
      label.textContent = 'Generate';
      status.textContent = 'Done in 2.4s · seed 90210';
    }, 2500));
    timers.push(setTimeout(function () {
      status.textContent = '';
    }, 5200));
  });
})();
```
