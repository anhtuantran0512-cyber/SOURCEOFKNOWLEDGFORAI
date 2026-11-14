---
source: "codefronts"
url: "https://codefronts.com/motion/css-link-effects/neon-sign-flicker/"
title: "CSS Neon Sign Flicker Text Hover"
section: "motion"
category: "css-link-effects"
category_name: "CSS Link Effects"
description: "Hover flips the power switch: a dead neon sign stutters to life with the irregular strike of a real gas tube, holds its glow while you stay, and goes dark…"
has_js: "false"
---

Here's a working CSS Link Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Neon Sign Flicker Text Hover
Source: https://codefronts.com/motion/css-link-effects/neon-sign-flicker/

Hover flips the power switch: a dead neon sign stutters to life with the irregular strike of a real gas tube, holds its glow while you stay, and goes dark when you leave. Includes the faulty-tube variant — the whole sign lights except one letter that keeps buzzing — and a full tube-border frame. Flicker cadence is kept under the WCAG three-flashes-per-second line.
## HTML
```html
<section class="cle-13" aria-label="Neon flicker hover demo">
  <div class="cle-13__stage">
    <div class="cle-13__var"><a href="#a" class="cle-13__sign">OPEN LATE</a><small class="cle-13__cap">A · strike on hover, hold lit</small></div>
    <div class="cle-13__var"><a href="#b" class="cle-13__faulty">DIN<span class="cle-13__bad">E</span>R</a><small class="cle-13__cap">B · one tube keeps buzzing</small></div>
    <div class="cle-13__var"><a href="#c" class="cle-13__tube">Reserve a booth</a><small class="cle-13__cap">C · tube-border frame</small></div>
  </div>
</section>
```
## CSS
```css
.cle-13,
.cle-13 *,
.cle-13 *::before,
.cle-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cle-13 {
  width: 100%;
  min-height: 100vh;
  --neon: oklch(0.72 0.23 350);
  --dead: oklch(0.6 0.05 350);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.cle-13__stage {
  width: 100%;
  height: 100vh;
  display: grid;
  align-content: center;
  justify-items: center;
  gap: 48px;
  background: radial-gradient(100% 130% at 50% -10%,oklch(0.24 0.04 330),oklch(0.15 0.02 320) 60%),oklch(0.15 0.02 320);
  padding: 44px 32px;
}

.cle-13__var {
  display: grid;
  gap: 14px;
  justify-items: center;
}

.cle-13__cap {
  font-size: 10.5px;
  font-weight: 600;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: oklch(0.55 0.04 340);
}

.cle-13 a {
  text-decoration: none;
  color: var(--dead);
  letter-spacing: .12em;
  font-weight: 800;
}

.cle-13 a:focus-visible {
  outline: 2px solid var(--neon);
  outline-offset: 6px;
  border-radius: 6px;
}

.cle-13__sign,
.cle-13__faulty {
  font-size: clamp(30px,4.6vw,42px);
}

.cle-13__sign:hover,
.cle-13__sign:focus-visible {
  animation: clh13-strike 1.1s steps(1) forwards;
}

.cle-13__faulty:hover,
.cle-13__faulty:focus-visible {
  animation: clh13-strike .7s steps(1) forwards;
}

.cle-13__bad {
  display: inline-block;
}

.cle-13__faulty:hover .cle-13__bad,
.cle-13__faulty:focus-visible .cle-13__bad {
  animation: clh13-buzz 3.4s linear .7s infinite;
}

.cle-13__tube {
  font-size: 19px;
  letter-spacing: .08em;
  padding: 16px 30px;
  border-radius: 999px;
  border: 2px solid oklch(0.4 0.04 350);
  transition: none;
}

.cle-13__tube:hover,
.cle-13__tube:focus-visible {
  animation: clh13-tube 1.1s steps(1) forwards;
}

@keyframes clh13-strike {
  0%,
    7%,
    12%,
    24%,
    29% {
    color: var(--dead);
    text-shadow: none;
  }

  9%,
    26%,
    38%,
    100% {
    color: oklch(0.97 0.03 350);
    text-shadow: 0 0 6px color-mix(in oklch,var(--neon),transparent 10%),0 0 24px color-mix(in oklch,var(--neon),transparent 35%),0 0 64px color-mix(in oklch,var(--neon),transparent 55%);
  }
}

@keyframes clh13-buzz {
  0%,
    88%,
    94%,
    100% {
    opacity: 1;
  }

  90%,
    96% {
    opacity: .55;
  }

  92% {
    opacity: .8;
  }
}

@keyframes clh13-tube {
  0%,
    7%,
    12%,
    24%,
    29% {
    color: var(--dead);
    border-color: oklch(0.4 0.04 350);
    box-shadow: none;
    text-shadow: none;
  }

  9%,
    26%,
    38%,
    100% {
    color: oklch(0.97 0.03 350);
    border-color: var(--neon);
    box-shadow: 0 0 10px color-mix(in oklch,var(--neon),transparent 45%),0 0 34px color-mix(in oklch,var(--neon),transparent 65%),inset 0 0 12px color-mix(in oklch,var(--neon),transparent 70%);
    text-shadow: 0 0 8px color-mix(in oklch,var(--neon),transparent 25%),0 0 28px color-mix(in oklch,var(--neon),transparent 55%);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cle-13 a,
    .cle-13 .cle-13__bad {
    animation: none !important;
    transition: color .3s,border-color .3s,box-shadow .3s,text-shadow .3s;
  }

  .cle-13 a:hover,
    .cle-13 a:focus-visible {
    color: oklch(0.97 0.03 350);
    text-shadow: 0 0 24px color-mix(in oklch,var(--neon),transparent 40%);
  }

  .cle-13__tube:hover,
    .cle-13__tube:focus-visible {
    border-color: var(--neon);
  }
}
```
