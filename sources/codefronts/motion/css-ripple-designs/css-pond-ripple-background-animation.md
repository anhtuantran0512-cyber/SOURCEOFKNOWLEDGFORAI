---
source: "codefronts"
url: "https://codefronts.com/motion/css-ripple-designs/css-pond-ripple-background-animation/"
title: "Pond Background with Drifting Ripples"
section: "motion"
category: "css-ripple-designs"
category_name: "CSS Ripple Effects"
description: "Nine rings surface at scattered positions on a slow, uneven cycle, so the field never reads as a grid or a pulse."
has_js: "false"
---

Here's a working CSS Ripple Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pond Background with Drifting Ripples
Source: https://codefronts.com/motion/css-ripple-designs/css-pond-ripple-background-animation/

Nine rings surface at scattered positions on a slow, uneven cycle, so the field never reads as a grid or a pulse. No interaction and no script: the origins are authored per ring as custom properties. It also covers what an always-on background animation actually costs, and why it has to stop under reduced motion.
## HTML
```html
<section class="rpl-11" aria-labelledby="rpl-11-title">
  <input class="rpl-11__theme-input" type="checkbox" id="rpl-11-theme">
  <label class="rpl-11__theme" for="rpl-11-theme">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="rpl-11__theme-sr">Switch between dark and light theme</span>
  </label>
  <div class="rpl-11__pond" aria-hidden="true">
    <span class="rpl-11__r" style="--rpl-11-x: 14%; --rpl-11-y: 22%; --rpl-11-d: 0s;   --rpl-11-s: 1.15"></span>
    <span class="rpl-11__r" style="--rpl-11-x: 68%; --rpl-11-y: 12%; --rpl-11-d: 1.4s; --rpl-11-s: 0.8"></span>
    <span class="rpl-11__r" style="--rpl-11-x: 82%; --rpl-11-y: 44%; --rpl-11-d: 2.6s; --rpl-11-s: 1.35"></span>
    <span class="rpl-11__r" style="--rpl-11-x: 30%; --rpl-11-y: 58%; --rpl-11-d: 3.9s; --rpl-11-s: 0.95"></span>
    <span class="rpl-11__r" style="--rpl-11-x: 55%; --rpl-11-y: 78%; --rpl-11-d: 5.1s; --rpl-11-s: 1.2"></span>
    <span class="rpl-11__r" style="--rpl-11-x: 9%;  --rpl-11-y: 86%; --rpl-11-d: 6.4s; --rpl-11-s: 0.85"></span>
    <span class="rpl-11__r" style="--rpl-11-x: 92%; --rpl-11-y: 88%; --rpl-11-d: 7.6s; --rpl-11-s: 1.05"></span>
    <span class="rpl-11__lily" style="--rpl-11-x: 22%; --rpl-11-y: 70%"></span>
    <span class="rpl-11__lily rpl-11__lily--b" style="--rpl-11-x: 74%; --rpl-11-y: 28%"></span>
  </div>
  <div class="rpl-11__panel">
    <span class="rpl-11__mark" aria-hidden="true"></span>
    <h1 class="rpl-11__h1" id="rpl-11-title">Welcome back to Marsh</h1>
    <p class="rpl-11__sub">Sign in to your field notebook.</p>
    <label class="rpl-11__label" for="rpl-11-email">Email</label>
    <input class="rpl-11__input" id="rpl-11-email" type="email" autocomplete="email" placeholder="[email protected]">
    <label class="rpl-11__label" for="rpl-11-pass">Password</label>
    <input class="rpl-11__input" id="rpl-11-pass" type="password" autocomplete="current-password" placeholder="••••••••••">
    <button class="rpl-11__btn" type="button">Sign in</button>
    <p class="rpl-11__alt">New here? <a class="rpl-11__link" href="#rpl-11">Create an account</a></p>
  </div>
</section>
```
## CSS
```css
.rpl-11 {
  --rpl-11-deep: #0a1f18;
  --rpl-11-deep: oklch(0.24 0.040 165);
  --rpl-11-mid: #16382a;
  --rpl-11-mid: oklch(0.33 0.052 160);
  --rpl-11-fg: #edf7f1;
  --rpl-11-fg: oklch(0.97 0.014 160);
  --rpl-11-muted: #a3c2b1;
  --rpl-11-muted: oklch(0.795 0.035 158);
  --rpl-11-accent: #8fe0a8;
  --rpl-11-accent: oklch(0.86 0.115 155);
  --rpl-11-glass: rgba(10, 31, 24, 0.55);
  --rpl-11-glass: oklch(0.24 0.040 165 / 0.55);
  --rpl-11-cycle: 9s;
  position: relative;
  display: grid;
  place-items: center;
  min-block-size: 100vh;
  min-block-size: 100svh;
  padding: clamp(18px, 4vw, 56px);
  background: radial-gradient(110% 80% at 30% 0%, oklch(0.40 0.06 150 / 0.85), transparent 68%), linear-gradient(160deg, var(--rpl-11-mid), var(--rpl-11-deep));
  color: var(--rpl-11-fg);
  font-family: ui-serif, Georgia, "Times New Roman", serif;
  overflow: hidden;
  isolation: isolate;
  box-sizing: border-box;
}

.rpl-11 *,
.rpl-11 *::before,
.rpl-11 *::after {
  box-sizing: border-box;
}

.rpl-11__pond {
  position: absolute;
  inset: 0;
  z-index: 0;
  pointer-events: none;
}

.rpl-11__pond::after {
  content: "";
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(96deg, oklch(1 0 0 / 0.03) 0 2px, transparent 2px 30px);
  mix-blend-mode: soft-light;
}

.rpl-11__r {
  position: absolute;
  left: var(--rpl-11-x);
  top: var(--rpl-11-y);
  inline-size: clamp(120px, 22vw, 240px);
  aspect-ratio: 1;
  border-radius: 50%;
  border: 1px solid oklch(0.95 0.03 160 / 0.5);
  box-shadow: inset 0 0 0 6px oklch(0.95 0.03 160 / 0.10);
  mix-blend-mode: screen;
  animation: rpl-11-drift var(--rpl-11-cycle) cubic-bezier(0.08, 0.7, 0.26, 1) infinite;
  animation-delay: var(--rpl-11-d);
}

@keyframes rpl-11-drift {
  from {
    transform: translate(-50%, -50%) scale(0.05);
    opacity: 0;
  }

  8% {
    opacity: 0.7;
  }

  to {
    transform: translate(-50%, -50%) scale(var(--rpl-11-s, 1));
    opacity: 0;
  }
}

.rpl-11__lily {
  position: absolute;
  left: var(--rpl-11-x);
  top: var(--rpl-11-y);
  inline-size: 68px;
  aspect-ratio: 1;
  translate: -50% -50%;
  border-radius: 50% 50% 50% 6%;
  background: oklch(0.42 0.075 150 / 0.75);
  box-shadow: inset -8px -10px 18px oklch(0.20 0.04 160 / 0.6);
}

.rpl-11__lily--b {
  inline-size: 44px;
  rotate: 128deg;
  background: oklch(0.38 0.07 145 / 0.7);
}

.rpl-11__panel {
  position: relative;
  z-index: 2;
  inline-size: 100%;
  max-inline-size: 400px;
  display: flex;
  flex-direction: column;
  padding: clamp(24px, 4vw, 36px);
  border: 1px solid oklch(0.95 0.03 160 / 0.16);
  border-radius: 26px;
  background: var(--rpl-11-glass);
  backdrop-filter: blur(18px) saturate(1.1);
  box-shadow: 0 40px 90px -50px oklch(0 0 0 / 0.9);
}

.rpl-11__mark {
  inline-size: 32px;
  block-size: 32px;
  margin-block-end: 20px;
  border-radius: 50% 50% 50% 8%;
  background: var(--rpl-11-accent);
}

.rpl-11__h1 {
  margin: 0 0 8px;
  font-size: clamp(26px, 4.4vw, 34px);
  font-weight: 500;
  letter-spacing: -0.02em;
  line-height: 1.12;
}

.rpl-11__sub {
  margin: 0 0 26px;
  font-family: ui-sans-serif, system-ui, sans-serif;
  font-size: 14px;
  color: var(--rpl-11-muted);
}

.rpl-11__label {
  font-family: ui-sans-serif, system-ui, sans-serif;
  font-size: 11.5px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--rpl-11-muted);
  margin-block-end: 7px;
}

.rpl-11__input {
  min-block-size: 48px;
  margin-block-end: 16px;
  padding: 0 15px;
  border: 1px solid oklch(0.95 0.03 160 / 0.2);
  border-radius: 12px;
  background: oklch(0.18 0.03 165 / 0.6);
  color: var(--rpl-11-fg);
  font-family: ui-sans-serif, system-ui, sans-serif;
  font-size: 15px;
}

.rpl-11__input::placeholder {
  color: oklch(0.70 0.03 158 / 0.7);
}

.rpl-11__input:focus-visible {
  outline: 2px solid var(--rpl-11-accent);
  outline-offset: 1px;
  border-color: transparent;
}

.rpl-11__btn {
  position: relative;
  min-block-size: 50px;
  margin-block-start: 8px;
  border: 0;
  border-radius: 12px;
  background: var(--rpl-11-accent);
  color: oklch(0.24 0.04 160);
  font-family: ui-sans-serif, system-ui, sans-serif;
  font-size: 15px;
  font-weight: 650;
  cursor: pointer;
  overflow: hidden;
  isolation: isolate;
}

.rpl-11__btn::after {
  content: "";
  position: absolute;
  inset-block-start: 50%;
  inset-inline-start: 50%;
  inline-size: 170%;
  aspect-ratio: 1;
  border-radius: 50%;
  background: oklch(0.24 0.04 160 / 0.24);
  transform: translate(-50%, -50%) scale(0);
  opacity: 0;
  transition: transform 620ms cubic-bezier(0.1, 0.7, 0.3, 1), opacity 620ms linear;
  pointer-events: none;
  z-index: -1;
}

.rpl-11__btn:active::after {
  transform: translate(-50%, -50%) scale(1);
  opacity: 1;
  transition: none;
}

.rpl-11__btn:focus-visible {
  outline: 2px solid var(--rpl-11-fg);
  outline-offset: 3px;
}

.rpl-11__alt {
  margin: 18px 0 0;
  font-family: ui-sans-serif, system-ui, sans-serif;
  font-size: 13px;
  color: var(--rpl-11-muted);
  text-align: center;
}

.rpl-11__link {
  color: var(--rpl-11-accent);
  text-decoration: none;
  border-block-end: 1px solid color-mix(in oklab, var(--rpl-11-accent) 45%, transparent);
}

.rpl-11__link:hover {
  color: var(--rpl-11-fg);
  border-color: var(--rpl-11-fg);
}

@media (prefers-reduced-motion: reduce) {
  .rpl-11__r {
    animation: none;
    opacity: 0.16;
    transform: translate(-50%, -50%) scale(0.6);
  }

  .rpl-11__btn::after {
    display: none;
  }

  .rpl-11__btn:active {
    filter: brightness(0.94);
  }
}
/* Counter-scheme (toggle): every colour declaration re-declared — oklch lightness mirrored, var()/color-mix() carried over so variant rules keep their own text colour, lightening blends flipped to darkening. */

.rpl-11:has(#rpl-11-theme:checked) {
  --rpl-11-deep: oklch(0.762 0.040 165);
  --rpl-11-mid: oklch(0.678 0.052 160);
  --rpl-11-fg: oklch(0.140 0.014 160);
  --rpl-11-muted: oklch(0.246 0.035 158);
  --rpl-11-accent: oklch(0.185 0.115 155);
  --rpl-11-glass: oklch(0.762 0.040 165 / 0.55);
  background: radial-gradient(110% 80% at 30% 0%, oklch(0.613 0.06 150 / 0.85), transparent 68%), linear-gradient(160deg, var(--rpl-11-mid), var(--rpl-11-deep));
  color: var(--rpl-11-fg);
}

.rpl-11:has(#rpl-11-theme:checked) .rpl-11__pond::after {
  background: repeating-linear-gradient(96deg, oklch(0.140 0 0 / 0.03) 0 2px, transparent 2px 30px);
}

.rpl-11:has(#rpl-11-theme:checked) .rpl-11__r {
  border: 1px solid oklch(0.140 0.03 160 / 0.5);
  box-shadow: inset 0 0 0 6px oklch(0.140 0.03 160 / 0.10);
  mix-blend-mode: multiply;
}

.rpl-11:has(#rpl-11-theme:checked) .rpl-11__lily {
  background: oklch(0.594 0.075 150 / 0.75);
  box-shadow: inset -8px -10px 18px oklch(0.799 0.04 160 / 0.6);
}

.rpl-11:has(#rpl-11-theme:checked) .rpl-11__lily--b {
  background: oklch(0.632 0.07 145 / 0.7);
}

.rpl-11:has(#rpl-11-theme:checked) .rpl-11__panel {
  border: 1px solid oklch(0.140 0.03 160 / 0.16);
  background: var(--rpl-11-glass);
  box-shadow: 0 40px 90px -50px oklch(0.985 0 0 / 0.9);
}

.rpl-11:has(#rpl-11-theme:checked) .rpl-11__mark {
  background: var(--rpl-11-accent);
}

.rpl-11:has(#rpl-11-theme:checked) .rpl-11__sub {
  color: var(--rpl-11-muted);
}

.rpl-11:has(#rpl-11-theme:checked) .rpl-11__label {
  color: var(--rpl-11-muted);
}

.rpl-11:has(#rpl-11-theme:checked) .rpl-11__input {
  border: 1px solid oklch(0.140 0.03 160 / 0.2);
  background: oklch(0.818 0.03 165 / 0.6);
  color: var(--rpl-11-fg);
}

.rpl-11:has(#rpl-11-theme:checked) .rpl-11__input::placeholder {
  color: oklch(0.334 0.03 158 / 0.7);
}

.rpl-11:has(#rpl-11-theme:checked) .rpl-11__input:focus-visible {
  outline: 2px solid var(--rpl-11-accent);
}

.rpl-11:has(#rpl-11-theme:checked) .rpl-11__btn {
  background: var(--rpl-11-accent);
  color: oklch(0.762 0.04 160);
}

.rpl-11:has(#rpl-11-theme:checked) .rpl-11__btn::after {
  background: oklch(0.762 0.04 160 / 0.24);
}

.rpl-11:has(#rpl-11-theme:checked) .rpl-11__btn:focus-visible {
  outline: 2px solid var(--rpl-11-fg);
}

.rpl-11:has(#rpl-11-theme:checked) .rpl-11__alt {
  color: var(--rpl-11-muted);
}

.rpl-11:has(#rpl-11-theme:checked) .rpl-11__link {
  color: var(--rpl-11-accent);
}

.rpl-11:has(#rpl-11-theme:checked) .rpl-11__link:hover {
  color: var(--rpl-11-fg);
  border-color: var(--rpl-11-fg);
}

.rpl-11 {
  position: relative;
}

.rpl-11__theme-input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.rpl-11__theme {
  position: absolute;
  z-index: 60;
  inset-block-start: 14px;
  inset-inline-end: 14px;
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border-radius: 999px;
  border: 1px solid color-mix(in oklab, currentColor 22%, transparent);
  background: color-mix(in oklab, currentColor 8%, transparent);
  color: inherit;
  cursor: pointer;
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  transition: background 160ms ease, border-color 160ms ease, transform 160ms ease;
}

.rpl-11__theme:hover {
  background: color-mix(in oklab, currentColor 15%, transparent);
  border-color: color-mix(in oklab, currentColor 38%, transparent);
}

.rpl-11__theme:active {
  transform: scale(0.94);
}

.rpl-11__theme svg {
  inline-size: 19px;
  block-size: 19px;
  display: block;
  transition: transform 320ms cubic-bezier(0.2, 0.7, 0.3, 1);
}

.rpl-11__theme-input:checked + .rpl-11__theme svg {
  transform: rotate(180deg);
}

.rpl-11__theme-input:focus-visible + .rpl-11__theme {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.rpl-11__theme-sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

@media (prefers-reduced-motion: reduce) {
  .rpl-11__theme,
    .rpl-11__theme svg {
    transition: none;
  }
}
```
