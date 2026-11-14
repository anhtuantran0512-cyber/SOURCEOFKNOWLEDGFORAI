---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/neon-cyberpunk-toggle/"
title: "Neon Cyberpunk Toggle"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "A clipped-corner, neon-tube toggle for dark dashboards and game UIs: magenta standby glow snaps to cyan when engaged, the status text flickers to life like a…"
has_js: "false"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neon Cyberpunk Toggle
Source: https://codefronts.com/components/css-toggles-switches/neon-cyberpunk-toggle/

A clipped-corner, neon-tube toggle for dark dashboards and game UIs: magenta standby glow snaps to cyan when engaged, the status text flickers to life like a striplight warming up, and every glow is pure layered box-shadow and text-shadow.
## HTML
```html
<section class="tgl-16" aria-label="Neon cyberpunk toggle">
  <label class="tgl-16__unit" for="tgl-16-sw">
    <span class="tgl-16__word" aria-hidden="true">PWR</span>
    <span class="tgl-16__frame">
      <input type="checkbox" id="tgl-16-sw" class="tgl-16__sw" role="switch" aria-label="Power">
      <span class="tgl-16__thumb" aria-hidden="true"></span>
    </span>
    <span class="tgl-16__status" aria-hidden="true"><i class="tgl-16__stby">STBY</i><i class="tgl-16__live">LIVE</i></span>
  </label>
  <p class="tgl-16__cap">Magenta standby → cyan engage</p>
</section>
```
## CSS
```css
.tgl-16,
.tgl-16 *,
.tgl-16 *::before,
.tgl-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tgl-16 {
  --off-neon: oklch(0.7 0.24 340);
  --on-neon: oklch(0.82 0.15 200);
  font-family: ui-monospace,'SF Mono',Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 28px;
  padding: 60px 20px;
  background: #0a0812;
}

.tgl-16__unit {
  display: flex;
  align-items: center;
  gap: 22px;
  cursor: pointer;
  padding: 20px 26px;
  background: #120f1d;
  clip-path: polygon(10px 0,100% 0,100% calc(100% - 10px),calc(100% - 10px) 100%,0 100%,0 10px);
}

.tgl-16__word {
  font-size: 14px;
  font-weight: 700;
  letter-spacing: .3em;
  color: #4c4761;
}

.tgl-16__frame {
  position: relative;
  width: 92px;
  height: 40px;
  background: #0c0a15;
  border: 1px solid var(--off-neon);
  box-shadow: 0 0 1px var(--off-neon),0 0 8px color-mix(in oklab,var(--off-neon) 60%,transparent),inset 0 0 10px color-mix(in oklab,var(--off-neon) 25%,transparent);
  clip-path: polygon(8px 0,100% 0,100% calc(100% - 8px),calc(100% - 8px) 100%,0 100%,0 8px);
  transition: border-color .3s,box-shadow .3s;
}

.tgl-16__frame:has(.tgl-16__sw:checked) {
  border-color: var(--on-neon);
  box-shadow: 0 0 1px var(--on-neon),0 0 10px color-mix(in oklab,var(--on-neon) 65%,transparent),inset 0 0 12px color-mix(in oklab,var(--on-neon) 30%,transparent);
}

.tgl-16__sw {
  appearance: none;
  -webkit-appearance: none;
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  cursor: pointer;
  z-index: 1;
  background: transparent;
}

.tgl-16__thumb {
  position: absolute;
  top: 6px;
  left: 6px;
  width: 28px;
  height: 26px;
  background: var(--off-neon);
  box-shadow: 0 0 8px var(--off-neon);
  clip-path: polygon(5px 0,100% 0,100% calc(100% - 5px),calc(100% - 5px) 100%,0 100%,0 5px);
  transition: transform .3s cubic-bezier(.6,0,.3,1.2),background-color .3s,box-shadow .3s;
  pointer-events: none;
}

.tgl-16__sw:checked ~ .tgl-16__thumb {
  transform: translateX(50px);
  background: var(--on-neon);
  box-shadow: 0 0 10px var(--on-neon);
}

.tgl-16__status {
  position: relative;
  width: 52px;
  height: 18px;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: .18em;
}

.tgl-16__status i {
  position: absolute;
  inset: 0;
  font-style: normal;
  transition: opacity .25s;
}

.tgl-16__stby {
  color: var(--off-neon);
  text-shadow: 0 0 6px var(--off-neon),0 0 16px color-mix(in oklab,var(--off-neon) 55%,transparent);
}

.tgl-16__live {
  color: var(--on-neon);
  text-shadow: 0 0 6px var(--on-neon),0 0 16px color-mix(in oklab,var(--on-neon) 55%,transparent);
  opacity: 0;
}

.tgl-16__unit:has(.tgl-16__sw:checked) .tgl-16__stby {
  opacity: 0;
}

.tgl-16__unit:has(.tgl-16__sw:checked) .tgl-16__live {
  opacity: 1;
  animation: tgl-16-strike .5s steps(1,end);
}

@keyframes tgl-16-strike {
  0% {
    opacity: 0;
  }

  20% {
    opacity: 1;
  }

  30% {
    opacity: .2;
  }

  45% {
    opacity: 1;
  }

  55% {
    opacity: .4;
  }

  70% {
    opacity: 1;
  }
}

.tgl-16__sw:focus-visible ~ .tgl-16__thumb {
  outline: 3px solid #fff;
  outline-offset: 6px;
}

.tgl-16__cap {
  font-size: 11px;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: #3f3a52;
}

@media (prefers-reduced-motion: reduce) {
  .tgl-16__unit:has(.tgl-16__sw:checked) .tgl-16__live {
    animation: none;
  }

  .tgl-16__thumb {
    transition: transform .15s,background-color .15s;
  }
}
```

## JavaScript
```js
/* No JavaScript — layered box/text shadows build the neon bloom, one custom-property swap rehues the tube, and a steps() opacity keyframe strikes the LIVE text. */
```
