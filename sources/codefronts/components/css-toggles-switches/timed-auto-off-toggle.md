---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/timed-auto-off-toggle/"
title: "Timed Auto-Off Toggle"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "A self-disarming switch for risky settings: flip it on and a conic countdown ring drains around the control for 8 seconds, then the toggle flips itself back…"
has_js: "true"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Timed Auto-Off Toggle
Source: https://codefronts.com/components/css-toggles-switches/timed-auto-off-toggle/

A self-disarming switch for risky settings: flip it on and a conic countdown ring drains around the control for 8 seconds, then the toggle flips itself back off — with the remaining time announced to screen readers. Think 'temporarily allow' permissions.
## HTML
```html
<section class="tgl-10" aria-label="Timed auto-off toggle">
  <div class="tgl-10__card">
    <div class="tgl-10__head"><b>Temporarily allow</b><span>USB debugging · auto-off in 8s</span></div>
    <span class="tgl-10__ringwrap" id="tgl-10-ring">
      <input type="checkbox" id="tgl-10-sw" class="tgl-10__sw" role="switch" aria-label="Temporarily allow USB debugging">
    </span>
    <p class="tgl-10__live" id="tgl-10-live" aria-live="polite"></p>
  </div>
</section>
```
## CSS
```css
@property --tgl-10-p {
  syntax: '<percentage>';
  inherits: false;
  initial-value: 100%;
}

.tgl-10,
.tgl-10 *,
.tgl-10 *::before,
.tgl-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tgl-10 {
  --warn: oklch(0.72 0.16 60);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background: #15171d;
}

.tgl-10__card {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 18px;
  background: #1d2028;
  border: 1px solid #2a2e3a;
  border-radius: 20px;
  padding: 30px 36px;
  width: min(340px,100%);
}

.tgl-10__head {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  text-align: center;
}

.tgl-10__head b {
  font-size: 17px;
  color: #e8eaf2;
}

.tgl-10__head span {
  font-size: 12.5px;
  color: #7d8494;
}

.tgl-10__ringwrap {
  --dur: 8s;
  position: relative;
  display: grid;
  place-items: center;
  width: 110px;
  height: 110px;
  border-radius: 50%;
  background: conic-gradient(var(--warn) var(--tgl-10-p),#2a2e3a 0);
}

.tgl-10__ringwrap::before {
  content: "";
  position: absolute;
  inset: 5px;
  border-radius: 50%;
  background: #1d2028;
}

.tgl-10__ringwrap.tgl-10--counting {
  animation: tgl-10-drain var(--dur) linear forwards;
}

@keyframes tgl-10-drain {
  from {
    --tgl-10-p: 100%;
  }

  to {
    --tgl-10-p: 0%;
  }
}

.tgl-10__sw {
  appearance: none;
  -webkit-appearance: none;
  position: relative;
  z-index: 1;
  width: 64px;
  height: 36px;
  border-radius: 20px;
  background: #2c3040;
  cursor: pointer;
  transition: background-color .3s;
}

.tgl-10__sw:checked {
  background: var(--warn);
}

.tgl-10__sw::before {
  content: "";
  position: absolute;
  top: 3px;
  left: 3px;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background: #fff;
  box-shadow: 0 2px 6px rgba(0,0,0,.5);
  transition: transform .3s cubic-bezier(.25,.9,.3,1.1);
}

.tgl-10__sw:checked::before {
  transform: translateX(28px);
}

.tgl-10__sw:focus-visible {
  outline: 3px solid var(--warn);
  outline-offset: 4px;
}

.tgl-10__live {
  font-size: 12.5px;
  color: #8f96a8;
  min-height: 1.2em;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .tgl-10__sw,
    .tgl-10__sw::before {
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  const DURATION = 8000;
  const sw = document.querySelector('#tgl-10-sw');
  const ring = document.querySelector('#tgl-10-ring');
  const live = document.querySelector('#tgl-10-live');
  let timer = null;
  sw.addEventListener('change', () => {
    clearTimeout(timer);
    if (sw.checked) {
      ring.classList.remove('tgl-10--counting');
      void ring.offsetWidth; // restart the CSS countdown animation
      ring.classList.add('tgl-10--counting');
      live.textContent = 'Enabled for 8 seconds';
      timer = setTimeout(() => {
        sw.checked = false;
        ring.classList.remove('tgl-10--counting');
        live.textContent = 'Auto-disabled';
      }, DURATION);
    } else {
      ring.classList.remove('tgl-10--counting');
      live.textContent = 'Disabled';
    }
  });
})();
```
