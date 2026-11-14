---
source: "codefronts"
url: "https://codefronts.com/navigation/css-accordions/holographic-slot/"
title: "Holographic Slot Accordion — @property Rotating Border Sheen"
section: "navigation"
category: "css-accordions"
category_name: "CSS Accordions — Vertical & Horizontal"
description: "Each closed item is a dark slot ringed by a faint conic seam; the open one ignites — a holographic gradient beam orbits its border continuously while an…"
has_js: "false"
---

Here's a working CSS Accordions — Vertical & Horizontal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Holographic Slot Accordion — @property Rotating Border Sheen
Source: https://codefronts.com/navigation/css-accordions/holographic-slot/

Each closed item is a dark slot ringed by a faint conic seam; the open one ignites — a holographic gradient beam orbits its border continuously while an iridescent sheen sweeps the header text. The 'animated gradient border' effect done properly with a registered @property angle and mask-composited ring, for AI products, gaming and dev-tool launches.
## HTML
```html
<section class="acc-31" aria-label="Holographic slot accordion demo">
  <div class="acc-31__wrap">
    <p class="acc-31__kicker">Nova Runtime</p>
    <h3 class="acc-31__title">What's inside the beta</h3>
    <details class="acc-31__item" open>
      <summary class="acc-31__sum">Instant cold starts<span class="acc-31__chev"></span></summary>
      <div class="acc-31__body"><p>Snapshots of your initialized runtime resume in under 5ms — the function is warm before the request finishes its TLS handshake.</p></div>
    </details>
    <details class="acc-31__item">
      <summary class="acc-31__sum">Typed edge storage<span class="acc-31__chev"></span></summary>
      <div class="acc-31__body"><p>A schema-checked KV replicated to every region. Reads are local everywhere; writes converge in ~80ms worldwide.</p></div>
    </details>
    <details class="acc-31__item">
      <summary class="acc-31__sum">Time-travel debugging<span class="acc-31__chev"></span></summary>
      <div class="acc-31__body"><p>Every production request is replayable locally with its exact inputs, clock and network responses. Heisenbugs lose their superpower.</p></div>
    </details>
  </div>
</section>
```
## CSS
```css
@property --acc-31-a {
  syntax: "<angle>";
  inherits: false;
  initial-value: 0deg;
}

.acc-31,
.acc-31 *,
.acc-31 *::before,
.acc-31 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.acc-31 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #0c0d12;
  padding: 44px 24px;
}

.acc-31__wrap {
  width: min(560px,100%);
}

.acc-31__kicker {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: #7c8398;
}

.acc-31__title {
  font-size: 25px;
  font-weight: 800;
  color: #eef0f8;
  letter-spacing: -.02em;
  margin: 6px 0 18px;
}

.acc-31__item {
  position: relative;
  background: #13151d;
  border-radius: 14px;
  margin-bottom: 12px;
}

.acc-31__item::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 14px;
  padding: 1.5px;
  background: conic-gradient(from var(--acc-31-a),#ff6ad5,#8f6aff,#6ad5ff,#6affb0,#ff6ad5);
  -webkit-mask: linear-gradient(#fff 0 0) content-box,linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor;
  mask: linear-gradient(#fff 0 0) content-box,linear-gradient(#fff 0 0);
  mask-composite: exclude;
  opacity: .12;
  transition: opacity .4s;
  pointer-events: none;
}

.acc-31__item:hover::before {
  opacity: .4;
}

.acc-31__item[open]::before {
  opacity: 1;
  animation: acc-31-orbit 3.5s linear infinite;
}

@keyframes acc-31-orbit {
  to {
    --acc-31-a: 360deg;
  }
}

.acc-31__sum {
  list-style: none;
  display: flex;
  align-items: center;
  gap: 14px;
  min-height: 60px;
  padding: 8px 20px;
  font-size: 16px;
  font-weight: 700;
  color: #d8dcea;
  cursor: pointer;
}

.acc-31__sum::-webkit-details-marker {
  display: none;
}

.acc-31__sum::marker {
  content: "";
}

.acc-31__item[open] .acc-31__sum {
  background: linear-gradient(100deg,#ff6ad5,#8f6aff,#6ad5ff,#6affb0) 0 0/300% 100%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: acc-31-sheen 3s ease-in-out infinite alternate;
}

@keyframes acc-31-sheen {
  to {
    background-position: 100% 0;
  }
}

.acc-31__chev {
  margin-left: auto;
  width: 8px;
  height: 8px;
  border-right: 2px solid #7c8398;
  border-bottom: 2px solid #7c8398;
  rotate: 45deg;
  translate: 0 -1.5px;
  transition: rotate .3s;
  flex: none;
}

.acc-31__item[open] .acc-31__chev {
  rotate: 225deg;
  translate: 0 1.5px;
}

.acc-31__body {
  padding: 0 20px 20px;
  font-size: 14.5px;
  line-height: 1.65;
  color: #9ba3ba;
}

.acc-31__item[open] .acc-31__body {
  animation: acc-31-in .35s ease-out;
}

@keyframes acc-31-in {
  from {
    opacity: 0;
    translate: 0 -5px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.acc-31__sum:focus-visible {
  outline: 3px solid #8f6aff;
  outline-offset: 3px;
  border-radius: 10px;
}

@media (prefers-reduced-motion: reduce) {
  .acc-31__item[open]::before {
    animation: none;
  }

  .acc-31__item[open] .acc-31__sum {
    animation: none;
  }

  .acc-31__item[open] .acc-31__body {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a registered @property angle rotates a conic gradient hollowed into a 1.5px ring via mask-composite:exclude; the orbit and text sheen run only while details[open]. */
```
