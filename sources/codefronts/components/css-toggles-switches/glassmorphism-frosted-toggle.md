---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/glassmorphism-frosted-toggle/"
title: "Glassmorphism Frosted Toggle"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "A frosted-glass switch floating over a vivid gradient scene: the track is translucent, blurred glass (backdrop-filter) with a hairline light border, the…"
has_js: "false"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Frosted Toggle
Source: https://codefronts.com/components/css-toggles-switches/glassmorphism-frosted-toggle/

A frosted-glass switch floating over a vivid gradient scene: the track is translucent, blurred glass (backdrop-filter) with a hairline light border, the thumb a denser frost puck — and the colorful blobs behind it visibly refract through both as it slides.
## HTML
```html
<section class="tgl-21" aria-label="Glassmorphism frosted toggle">
  <span class="tgl-21__blob tgl-21__blob--a" aria-hidden="true"></span>
  <span class="tgl-21__blob tgl-21__blob--b" aria-hidden="true"></span>
  <label class="tgl-21__panel" for="tgl-21-sw">
    <span class="tgl-21__txt"><b>Ambient blur</b><small>Frost the dock &amp; sidebar</small></span>
    <input type="checkbox" id="tgl-21-sw" class="tgl-21__sw" role="switch" checked>
  </label>
</section>
```
## CSS
```css
.tgl-21,
.tgl-21 *,
.tgl-21 *::before,
.tgl-21 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tgl-21 {
  position: relative;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background: linear-gradient(135deg,#1b1035,#0d2436);
  overflow: hidden;
}

.tgl-21__blob {
  position: absolute;
  width: 340px;
  height: 340px;
  border-radius: 50%;
  filter: blur(60px);
  opacity: .85;
  animation: tgl-21-drift 9s ease-in-out infinite alternate;
}

.tgl-21__blob--a {
  top: 6%;
  left: 14%;
  background: radial-gradient(circle,oklch(0.68 0.24 330),transparent 70%);
}

.tgl-21__blob--b {
  bottom: 4%;
  right: 12%;
  background: radial-gradient(circle,oklch(0.75 0.16 200),transparent 70%);
  animation-delay: -4.5s;
}

@keyframes tgl-21-drift {
  from {
    transform: translate(0,0);
  }

  to {
    transform: translate(46px,-30px);
  }
}

.tgl-21__panel {
  position: relative;
  z-index: 1;
  display: flex;
  align-items: center;
  gap: 36px;
  padding: 22px 26px;
  border-radius: 20px;
  background: rgba(255,255,255,.1);
  border: 1px solid rgba(255,255,255,.28);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.35),0 24px 50px -24px rgba(0,0,0,.7);
  backdrop-filter: blur(14px) saturate(1.4);
  -webkit-backdrop-filter: blur(14px) saturate(1.4);
  cursor: pointer;
}

.tgl-21__txt {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.tgl-21__txt b {
  font-size: 16px;
  color: #fff;
}

.tgl-21__txt small {
  font-size: 12.5px;
  color: rgba(255,255,255,.65);
}

.tgl-21__sw {
  appearance: none;
  -webkit-appearance: none;
  flex: none;
  width: 76px;
  height: 40px;
  border-radius: 22px;
  background: rgba(255,255,255,.14);
  border: 1px solid rgba(255,255,255,.35);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.3);
  position: relative;
  cursor: pointer;
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  transition: background-color .35s;
}

.tgl-21__sw:checked {
  background: rgba(120,235,170,.22);
}

.tgl-21__sw::before {
  content: "";
  position: absolute;
  top: 4px;
  left: 4px;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background: rgba(255,255,255,.75);
  box-shadow: 0 3px 10px rgba(0,0,0,.35),inset 0 1px 0 #fff;
  transition: transform .35s cubic-bezier(.3,1,.35,1.05);
}

.tgl-21__sw:checked::before {
  transform: translateX(36px);
}

.tgl-21__sw:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .tgl-21__panel {
    background: rgba(30,26,60,.85);
  }

  .tgl-21__sw {
    background: rgba(255,255,255,.12);
  }
}

@media (prefers-reduced-motion: reduce) {
  .tgl-21__blob {
    animation: none;
  }

  .tgl-21__sw,
    .tgl-21__sw::before {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — backdrop-filter frosts the track and thumb over drifting gradient blobs; a gentle alpha tint marks the on state. */
```
