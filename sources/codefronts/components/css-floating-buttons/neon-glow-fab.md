---
source: "codefronts"
url: "https://codefronts.com/components/css-floating-buttons/neon-glow-fab/"
title: "Cyberpunk Neon Glow Floating Button CSS"
section: "components"
category: "css-floating-buttons"
category_name: "CSS Floating Buttons"
description: "Neon that looks like a gas tube rather than a coloured box-shadow: a bright near-white core, a saturated mid-glow, and a wide dim halo — three layers with…"
has_js: "false"
---

Here's a working CSS Floating Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Cyberpunk Neon Glow Floating Button CSS
Source: https://codefronts.com/components/css-floating-buttons/neon-glow-fab/

Neon that looks like a gas tube rather than a coloured box-shadow: a bright near-white core, a saturated mid-glow, and a wide dim halo — three layers with different blur radii, exactly how a real sign photographs. Plus a restrained startup flicker, a scanline sweep, and a hover that ramps the current up instead of just changing colour.
## HTML
```html
<section class="fb-18" aria-label="Cyberpunk neon floating button demo">
  <div class="fb-18__grid" aria-hidden="true"></div>
  <div class="fb-18__stage">
    <p class="fb-18__eyebrow">three-layer falloff · 400ms warm-up</p>
    <h2 class="fb-18__title">Neon<span class="fb-18__flick">_</span>district</h2>
    <p class="fb-18__sub">A hot near-white core, a saturated mid glow and a wide dim halo. Same three layers a real sign shows on camera.</p>
    <div class="fb-18__row">
      <button class="fb-18__fab" type="button" aria-label="Execute command">
        <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M13 2L4.5 13.5H11l-1 8.5 8.5-11.5H12z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>
      </button>
      <button class="fb-18__fab fb-18__fab--cyan" type="button" aria-label="Scan network">
        <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.6" fill="none" stroke="currentColor" stroke-width="1.9"/><path d="M15.8 15.8L21 21" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>
      </button>
      <button class="fb-18__fab fb-18__fab--amber fb-18__fab--off" type="button" aria-label="Power, unlit until hover">
        <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 3v9" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><path d="M6.6 6.8a7.5 7.5 0 1 0 10.8 0" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
      </button>
    </div>
    <p class="fb-18__chip">0 0 6px core · 0 0 22px glow · 0 0 60px halo</p>
  </div>
</section>
```
## CSS
```css
.fb-18 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--fb-18-bg);
  --fb-18-bg: radial-gradient(120% 90% at 50% 110%,oklch(0.24 0.09 320),oklch(0.13 0.03 275) 62%);
  --fb-18-c: oklch(0.72 0.28 330);
  --fb-18-ink: oklch(0.97 0.02 320);
  --fb-18-mut: oklch(0.76 0.04 320);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--fb-18-ink);
  position: relative;
  display: grid;
  place-items: center;
  padding: clamp(20px,5vw,56px);
  overflow: hidden;
}

.fb-18 *,
.fb-18 *::before,
.fb-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fb-18__grid {
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(90deg,oklch(0.72 0.28 330/.07) 0 1px,transparent 1px 54px),repeating-linear-gradient(0deg,oklch(0.7 0.2 200/.06) 0 1px,transparent 1px 54px);
  mask-image: radial-gradient(90% 70% at 50% 60%,black,transparent);
  -webkit-mask-image: radial-gradient(90% 70% at 50% 60%,black,transparent);
}

.fb-18__stage {
  position: relative;
  width: min(100%,58ch);
  display: grid;
  gap: clamp(18px,3vw,28px);
  justify-items: center;
  text-align: center;
}

.fb-18__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: oklch(0.82 0.16 200);
  text-shadow: 0 0 12px oklch(0.7 0.2 200/.8);
}

.fb-18__title {
  font-size: clamp(30px,6.4vw,62px);
  line-height: 1;
  letter-spacing: -.02em;
  font-weight: 800;
  text-transform: lowercase;
  color: oklch(0.98 0.03 330);
  text-shadow: 0 0 6px oklch(0.95 0.08 330),0 0 22px var(--fb-18-c),0 0 62px color-mix(in oklch,var(--fb-18-c) 60%,transparent);
}

.fb-18__flick {
  animation: fb-18-blink 1.2s steps(1) infinite;
  color: oklch(0.85 0.2 200);
  text-shadow: 0 0 8px oklch(0.85 0.2 200),0 0 26px oklch(0.7 0.2 200);
}

@keyframes fb-18-blink {
  0%,
    49% {
    opacity: 1;
  }

  50%,
    100% {
    opacity: .12;
  }
}

.fb-18__sub {
  max-width: 48ch;
  font-size: clamp(13.5px,1.7vw,16.5px);
  line-height: 1.62;
  color: var(--fb-18-mut);
  text-wrap: pretty;
}

.fb-18__row {
  display: flex;
  flex-wrap: wrap;
  gap: clamp(20px,5vw,42px);
  justify-content: center;
}

.fb-18__fab {
  position: relative;
  display: grid;
  place-items: center;
  inline-size: 72px;
  block-size: 72px;
  border: 2px solid var(--fb-18-c);
  border-radius: 50%;
  cursor: pointer;
  color: oklch(0.98 0.04 330);
  background: oklch(0.16 0.04 320/.7);
  box-shadow: 0 0 6px color-mix(in oklch,white 60%,var(--fb-18-c)),0 0 22px var(--fb-18-c),0 0 60px color-mix(in oklch,var(--fb-18-c) 60%,transparent),inset 0 0 16px color-mix(in oklch,var(--fb-18-c) 40%,transparent);
  animation: fb-18-warm .55s steps(1,end) 1;
  transition: transform .26s cubic-bezier(.2,1.3,.4,1),box-shadow .3s ease,background .3s ease;
}

.fb-18__fab svg {
  width: 27px;
  height: 27px;
  filter: drop-shadow(0 0 5px var(--fb-18-c)) drop-shadow(0 0 14px color-mix(in oklch,var(--fb-18-c) 70%,transparent));
}

@keyframes fb-18-warm {
  0%,
    8% {
    opacity: .2;
  }

  9%,
    14% {
    opacity: 1;
  }

  15%,
    22% {
    opacity: .25;
  }

  23%,
    38% {
    opacity: 1;
  }

  39%,
    44% {
    opacity: .4;
  }

  45%,
    100% {
    opacity: 1;
  }
}

.fb-18__fab:hover {
  transform: translateY(-3px) scale(1.04);
  background: oklch(0.22 0.08 320/.8);
  box-shadow: 0 0 9px color-mix(in oklch,white 70%,var(--fb-18-c)),0 0 34px var(--fb-18-c),0 0 90px color-mix(in oklch,var(--fb-18-c) 70%,transparent),inset 0 0 26px color-mix(in oklch,var(--fb-18-c) 55%,transparent);
}

.fb-18__fab:active {
  transform: scale(.93);
}

.fb-18__fab:focus-visible {
  outline: 3px solid oklch(0.98 0.02 320);
  outline-offset: 6px;
}

.fb-18__fab--cyan {
  --fb-18-c: oklch(0.8 0.19 200);
  color: oklch(0.98 0.03 200);
  animation-delay: .12s;
}

.fb-18__fab--amber {
  --fb-18-c: oklch(0.83 0.18 78);
  color: oklch(0.98 0.04 78);
  animation-delay: .24s;
}

.fb-18__fab--off {
  border-color: color-mix(in oklch,var(--fb-18-c) 40%,oklch(0.3 0.02 78));
  color: oklch(0.62 0.06 78);
  box-shadow: inset 0 0 14px oklch(0 0 0/.5);
  animation: none;
}

.fb-18__fab--off svg {
  filter: none;
}

.fb-18__fab--off:hover {
  border-color: var(--fb-18-c);
  color: oklch(0.98 0.04 78);
  box-shadow: 0 0 9px color-mix(in oklch,white 70%,var(--fb-18-c)),0 0 34px var(--fb-18-c),0 0 90px color-mix(in oklch,var(--fb-18-c) 70%,transparent);
}

.fb-18__fab--off:hover svg {
  filter: drop-shadow(0 0 5px var(--fb-18-c)) drop-shadow(0 0 14px color-mix(in oklch,var(--fb-18-c) 70%,transparent));
}

.fb-18__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--fb-18-mut);
  padding: 8px 14px;
  border: 1px solid oklch(0.72 0.28 330/.35);
  border-radius: 99px;
  box-shadow: 0 0 18px oklch(0.72 0.28 330/.18);
}

@media (prefers-reduced-motion: reduce) {
  .fb-18 * {
    animation: none !important;
    transition: none !important;
  }
}
```
