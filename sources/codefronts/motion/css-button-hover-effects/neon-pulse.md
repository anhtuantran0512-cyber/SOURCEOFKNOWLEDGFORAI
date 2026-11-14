---
source: "codefronts"
url: "https://codefronts.com/motion/css-button-hover-effects/neon-pulse/"
title: "Neon Pulse"
section: "motion"
category: "css-button-hover-effects"
category_name: "CSS Button Hover Effects"
description: "A glowing CTA whose neon halo breathes: on hover a heavy blurred glow scales gently in and out on a loop, so the button looks like a live light source (the…"
has_js: "false"
---

Here's a working CSS Button Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neon Pulse
Source: https://codefronts.com/motion/css-button-hover-effects/neon-pulse/

A glowing CTA whose neon halo breathes: on hover a heavy blurred glow scales gently in and out on a loop, so the button looks like a live light source (the soft looping counterpart to topic 11's hard snap).
## HTML
```html
<div class="bhe-18-group">
<section class="bhe-18a" aria-label="Neon pulse button">
  <button class="bhe-18a__btn" type="button">Go live</button>
</section>
<section class="bhe-18b" aria-label="Neon flicker button">
  <button class="bhe-18b__btn" type="button">Open bar</button>
</section>
</div>
```
## CSS
```css
.bhe-18-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-wrap: wrap;
}

.bhe-18-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.bhe-18a,
.bhe-18a *,
.bhe-18a *::before,
.bhe-18a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-18a {
  --neon: oklch(0.72 0.2 330);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #0a0710;
}

.bhe-18a__btn {
  font-size: 16px;
  font-weight: 800;
  letter-spacing: .05em;
  text-transform: uppercase;
  color: #fff;
  padding: 16px 40px;
  border: 2px solid var(--neon);
  border-radius: 9999px;
  cursor: pointer;
  background: color-mix(in oklab,var(--neon) 24%,#0a0710);
  box-shadow: 0 0 14px -2px color-mix(in oklab,var(--neon) 70%,transparent);
  transition: color .2s;
}

.bhe-18a__btn:hover,
.bhe-18a__btn:focus-visible {
  animation: bhe-18a-pulse 1.4s ease-in-out infinite;
}

.bhe-18a__btn:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 4px;
}

@keyframes bhe-18a-pulse {
  0%,
    100% {
    box-shadow: 0 0 12px -2px color-mix(in oklab,var(--neon) 65%,transparent);
    filter: brightness(1);
    text-shadow: 0 0 6px color-mix(in oklab,var(--neon) 60%,transparent);
  }

  50% {
    box-shadow: 0 0 34px 6px var(--neon),0 0 60px 12px color-mix(in oklab,var(--neon) 55%,transparent);
    filter: brightness(1.25);
    text-shadow: 0 0 16px var(--neon);
  }
}

@media (prefers-reduced-motion: reduce) {
  .bhe-18a__btn:hover,
    .bhe-18a__btn:focus-visible {
    animation: none;
    box-shadow: 0 0 24px 3px var(--neon);
  }
}

.bhe-18b,
.bhe-18b *,
.bhe-18b *::before,
.bhe-18b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-18b {
  --neon: oklch(0.78 0.16 195);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #04100f;
}

.bhe-18b__btn {
  font-size: 16px;
  font-weight: 800;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--neon);
  padding: 16px 42px;
  border: 2px solid var(--neon);
  border-radius: 8px;
  cursor: pointer;
  background: transparent;
  text-shadow: 0 0 8px var(--neon);
  box-shadow: 0 0 10px -2px var(--neon),inset 0 0 10px -4px var(--neon);
  transition: color .2s;
}

.bhe-18b__btn:hover,
.bhe-18b__btn:focus-visible {
  animation: bhe-18b-flick 2.2s steps(1) infinite;
}

.bhe-18b__btn:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 4px;
}

@keyframes bhe-18b-flick {
  0%,
    19%,
    21%,
    23%,
    80%,
    100% {
    opacity: 1;
    box-shadow: 0 0 22px -2px var(--neon),inset 0 0 14px -4px var(--neon);
  }

  20%,
    22% {
    opacity: .5;
    box-shadow: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bhe-18b__btn:hover,
    .bhe-18b__btn:focus-visible {
    animation: none;
    box-shadow: 0 0 22px -2px var(--neon),inset 0 0 14px -4px var(--neon);
  }
}
```

## JavaScript
```js
/* No JavaScript — pure CSS; all designs for this title are driven entirely by the css field. */
```
