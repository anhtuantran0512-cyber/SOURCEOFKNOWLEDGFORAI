---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/waveform-mute-toggle/"
title: "Waveform Mute Toggle"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "A mute switch that shows sound instead of describing it: five equalizer bars dance inside the pill while audio is live, then collapse to a flatline the…"
has_js: "false"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Waveform Mute Toggle
Source: https://codefronts.com/components/css-toggles-switches/waveform-mute-toggle/

A mute switch that shows sound instead of describing it: five equalizer bars dance inside the pill while audio is live, then collapse to a flatline the instant you mute — state you can read from across the room, no thumb required.
## HTML
```html
<section class="tgl-09" aria-label="Waveform mute toggle">
  <label class="tgl-09__row" for="tgl-09-sw">
    <span class="tgl-09__lbl">Studio monitor</span>
    <span class="tgl-09__pill">
      <input type="checkbox" id="tgl-09-sw" class="tgl-09__sw" role="switch" checked>
      <span class="tgl-09__wave" aria-hidden="true"><i style="--d:0s"></i><i style="--d:.14s"></i><i style="--d:.28s"></i><i style="--d:.07s"></i><i style="--d:.21s"></i></span>
    </span>
  </label>
  <p class="tgl-09__cap">Live = dancing bars · muted = flatline</p>
</section>
```
## CSS
```css
.tgl-09,
.tgl-09 *,
.tgl-09 *::before,
.tgl-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tgl-09 {
  --live: oklch(0.78 0.16 160);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 24px;
  padding: 60px 20px;
  background: #101318;
}

.tgl-09__row {
  display: flex;
  align-items: center;
  gap: 28px;
  cursor: pointer;
}

.tgl-09__lbl {
  font-size: 16px;
  font-weight: 600;
  color: #c4ccd8;
}

.tgl-09__pill {
  position: relative;
  width: 96px;
  height: 46px;
  border-radius: 26px;
  background: #1b2028;
  box-shadow: inset 0 2px 6px rgba(0,0,0,.6),inset 0 0 0 1px #262d38;
  transition: box-shadow .35s;
}

.tgl-09__pill:has(.tgl-09__sw:checked) {
  box-shadow: inset 0 2px 6px rgba(0,0,0,.6),inset 0 0 0 1px color-mix(in oklab,var(--live) 55%,transparent),0 0 18px -4px color-mix(in oklab,var(--live) 50%,transparent);
}

.tgl-09__sw {
  appearance: none;
  -webkit-appearance: none;
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  border-radius: 26px;
  cursor: pointer;
  z-index: 1;
  background: transparent;
}

.tgl-09__wave {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 5px;
  pointer-events: none;
}

.tgl-09__wave i {
  width: 5px;
  height: 26px;
  border-radius: 3px;
  background: #3d4654;
  transform: scaleY(.12);
  transform-origin: center;
  transition: background-color .3s,transform .3s;
}

.tgl-09__sw:checked ~ .tgl-09__wave i {
  background: var(--live);
  animation: tgl-09-eq 0.9s ease-in-out var(--d) infinite alternate;
}

.tgl-09__sw:checked ~ .tgl-09__wave i:nth-child(2) {
  animation-duration: .75s;
}

.tgl-09__sw:checked ~ .tgl-09__wave i:nth-child(4) {
  animation-duration: 1.05s;
}

.tgl-09__sw:checked ~ .tgl-09__wave i:nth-child(5) {
  animation-duration: .8s;
}

@keyframes tgl-09-eq {
  0% {
    transform: scaleY(.25);
  }

  100% {
    transform: scaleY(1);
  }
}

.tgl-09__sw:focus-visible {
  outline: 3px solid var(--live);
  outline-offset: 4px;
}

.tgl-09__cap {
  font-size: 12px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: #525a68;
}

@media (prefers-reduced-motion: reduce) {
  .tgl-09__sw:checked ~ .tgl-09__wave i {
    animation: none;
    transform: scaleY(.7);
  }

  .tgl-09__sw:checked ~ .tgl-09__wave i:nth-child(odd) {
    transform: scaleY(.45);
  }
}
```

## JavaScript
```js
/* No JavaScript — five bars loop a staggered scaleY keyframe while checked and drop to a flatline via animation:none when muted. */
```
