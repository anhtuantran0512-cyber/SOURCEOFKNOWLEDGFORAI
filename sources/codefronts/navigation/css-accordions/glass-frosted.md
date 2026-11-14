---
source: "codefronts"
url: "https://codefronts.com/navigation/css-accordions/glass-frosted/"
title: "Glassmorphism Frosted Accordion with backdrop-filter Blur"
section: "navigation"
category: "css-accordions"
category_name: "CSS Accordions — Vertical & Horizontal"
description: "Frosted-glass panels floating over a colorful gradient scene: each item is a translucent card with backdrop-filter blur, a 1px inner light edge and a glow…"
has_js: "false"
---

Here's a working CSS Accordions — Vertical & Horizontal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Frosted Accordion with backdrop-filter Blur
Source: https://codefronts.com/navigation/css-accordions/glass-frosted/

Frosted-glass panels floating over a colorful gradient scene: each item is a translucent card with backdrop-filter blur, a 1px inner light edge and a glow that brightens on open — the 'iOS control center' aesthetic developers want for hero FAQs on gradient-heavy landing pages.
## HTML
```html
<section class="acc-12" aria-label="Glassmorphism frosted accordion demo">
  <div class="acc-12__wrap">
    <h3 class="acc-12__title">Aurora — Ambient sound engine</h3>
    <details class="acc-12__item" open>
      <summary class="acc-12__sum">What does Aurora listen to?<span class="acc-12__chev"></span></summary>
      <div class="acc-12__body"><p>Nothing. All processing happens on-device: the engine reacts to time of day, weather and your calendar density — no microphone access, ever.</p></div>
    </details>
    <details class="acc-12__item">
      <summary class="acc-12__sum">Which platforms are supported?<span class="acc-12__chev"></span></summary>
      <div class="acc-12__body"><p>macOS, iOS and iPadOS today, with handoff between them. Windows is in private beta — join from the settings pane.</p></div>
    </details>
    <details class="acc-12__item">
      <summary class="acc-12__sum">Can I import my own soundscapes?<span class="acc-12__chev"></span></summary>
      <div class="acc-12__body"><p>Drop in any lossless file and Aurora will loop-point, EQ-match and weather-blend it automatically. Creators can publish packs to the gallery.</p></div>
    </details>
  </div>
</section>
```
## CSS
```css
.acc-12,
.acc-12 *,
.acc-12 *::before,
.acc-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.acc-12 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 44px 24px;
  background-color: #191430;
  background-image: radial-gradient(560px 420px at 18% 12%,oklch(0.62 0.23 310 / .55),transparent 65%),radial-gradient(620px 480px at 85% 88%,oklch(0.68 0.19 220 / .5),transparent 65%);
}

.acc-12__wrap {
  width: min(560px,100%);
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.acc-12__title {
  font-size: 24px;
  font-weight: 750;
  color: #fff;
  letter-spacing: -.01em;
  margin-bottom: 6px;
  text-shadow: 0 2px 20px rgba(0,0,0,.3);
}

.acc-12__item {
  background: rgba(255,255,255,.08);
  border: 1px solid rgba(255,255,255,.18);
  border-radius: 18px;
  backdrop-filter: blur(18px) saturate(1.4);
  -webkit-backdrop-filter: blur(18px) saturate(1.4);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.22),0 16px 40px -20px rgba(0,0,0,.55);
  transition: background .3s,border-color .3s;
}

.acc-12__item[open] {
  background: rgba(255,255,255,.14);
  border-color: rgba(255,255,255,.32);
}

@supports not (backdrop-filter: blur(1px)) {
  .acc-12__item {
    background: rgba(30,24,58,.88);
  }

  .acc-12__item[open] {
    background: rgba(38,31,70,.92);
  }
}

.acc-12__sum {
  list-style: none;
  display: flex;
  align-items: center;
  gap: 14px;
  min-height: 60px;
  padding: 8px 20px;
  font-size: 15.5px;
  font-weight: 650;
  color: #fff;
  cursor: pointer;
}

.acc-12__sum::-webkit-details-marker {
  display: none;
}

.acc-12__sum::marker {
  content: "";
}

.acc-12__chev {
  margin-left: auto;
  width: 9px;
  height: 9px;
  border-right: 2px solid rgba(255,255,255,.75);
  border-bottom: 2px solid rgba(255,255,255,.75);
  rotate: 45deg;
  translate: 0 -2px;
  transition: rotate .3s,translate .3s;
  flex: none;
}

.acc-12__item[open] .acc-12__chev {
  rotate: 225deg;
  translate: 0 2px;
}

.acc-12__body {
  padding: 0 24px 20px;
  font-size: 14.5px;
  line-height: 1.65;
  color: rgba(255,255,255,.82);
}

.acc-12__item[open] .acc-12__body {
  animation: acc-12-in .35s ease-out;
}

@keyframes acc-12-in {
  from {
    opacity: 0;
    translate: 0 -5px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.acc-12__sum:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 3px;
  border-radius: 14px;
}

@media (prefers-reduced-motion: reduce) {
  .acc-12__item,
    .acc-12__chev {
    transition: none;
  }

  .acc-12__item[open] .acc-12__body {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — frosted panes are backdrop-filter: blur() saturate() over gradient orbs; details[open] brightens the pane, and an @supports block swaps solid fills where backdrop-filter is missing. */
```
