---
source: "codefronts"
url: "https://codefronts.com/motion/css-link-effects/heartbeat-pulse/"
title: "CSS Pulse / Heartbeat Link Hover Effect"
section: "motion"
category: "css-link-effects"
category_name: "CSS Link Effects"
description: "Three tempos of alive: a radar ping that radiates rings from a notification link, an anatomically-timed heartbeat (lub-DUB, then rest — not a metronome sine…"
has_js: "false"
---

Here's a working CSS Link Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Pulse / Heartbeat Link Hover Effect
Source: https://codefronts.com/motion/css-link-effects/heartbeat-pulse/

Three tempos of alive: a radar ping that radiates rings from a notification link, an anatomically-timed heartbeat (lub-DUB, then rest — not a metronome sine wave) on a like chip, and a slow breathing glow for a primary CTA. Each maps to a different UI job: attention, affection, invitation.
## HTML
```html
<section class="cle-14" aria-label="Pulse and heartbeat hover demo">
  <div class="cle-14__stage">
    <div class="cle-14__var"><a href="#a" class="cle-14__ping"><span class="cle-14__dot" aria-hidden="true"></span>3 new reviews</a><small class="cle-14__cap">A · radar ping</small></div>
    <div class="cle-14__var"><a href="#b" class="cle-14__beat"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 20.3 4.6 13a4.9 4.9 0 0 1 0-7 4.9 4.9 0 0 1 7 0l.4.4.4-.4a4.9 4.9 0 0 1 7 0 4.9 4.9 0 0 1 0 7z"/></svg>Save to favorites</a><small class="cle-14__cap">B · lub-dub heartbeat</small></div>
    <div class="cle-14__var"><a href="#c" class="cle-14__breathe">Start free trial</a><small class="cle-14__cap">C · breathing glow</small></div>
  </div>
</section>
```
## CSS
```css
.cle-14,
.cle-14 *,
.cle-14 *::before,
.cle-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cle-14 {
  width: 100%;
  min-height: 100vh;
  --ink: oklch(0.25 0.02 20);
  --brand: oklch(0.62 0.21 20);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.cle-14__stage {
  width: 100%;
  height: 100vh;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  gap: 44px 56px;
  border: 1px solid oklch(0.91 0.015 30);
  background: linear-gradient(170deg,oklch(0.98 0.008 40),oklch(0.95 0.018 25));
  padding: 44px 36px;
}

.cle-14__var {
  display: grid;
  gap: 14px;
  justify-items: center;
}

.cle-14__cap {
  font-size: 10.5px;
  font-weight: 600;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: oklch(0.55 0.04 25);
}

.cle-14 a {
  position: relative;
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 14px 26px;
  border-radius: 999px;
  background: oklch(1 0 0 / .85);
  border: 1.5px solid oklch(0.88 0.03 25);
  color: var(--ink);
  text-decoration: none;
  font-size: 15.5px;
  font-weight: 650;
  transition: border-color .3s,color .3s;
  box-shadow: 0 10px 26px -20px oklch(0.4 0.1 20 / .7);
}

.cle-14 a:hover,
.cle-14 a:focus-visible {
  border-color: var(--brand);
  color: oklch(0.45 0.19 20);
}

.cle-14 a:focus-visible {
  outline: 3px solid var(--brand);
  outline-offset: 3px;
}

.cle-14__dot {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: var(--brand);
}

.cle-14__ping::after {
  content: "";
  position: absolute;
  inset: -2px;
  border-radius: inherit;
  border: 2px solid var(--brand);
  opacity: 0;
  pointer-events: none;
}

.cle-14__ping:hover::after,
.cle-14__ping:focus-visible::after {
  animation: clh14-ping 1.1s cubic-bezier(0,.5,.4,1) infinite;
}

@keyframes clh14-ping {
  from {
    scale: 1;
    opacity: .8;
  }

  to {
    scale: 1.45;
    opacity: 0;
  }
}

.cle-14__beat svg {
  width: 19px;
  height: 19px;
  fill: var(--brand);
  stroke: none;
}

.cle-14__beat:hover svg,
.cle-14__beat:focus-visible svg {
  animation: clh14-beat 1.3s ease-in-out infinite;
}

@keyframes clh14-beat {
  0% {
    scale: 1;
  }

  12% {
    scale: 1.22;
  }

  24% {
    scale: 1;
  }

  34% {
    scale: 1.14;
  }

  45%,
    100% {
    scale: 1;
  }
}

.cle-14__breathe {
  background: linear-gradient(150deg,var(--brand),oklch(0.5 0.2 350));
  border-color: transparent;
  color: oklch(0.99 0.005 20);
}

.cle-14__breathe:hover,
.cle-14__breathe:focus-visible {
  color: #fff;
  animation: clh14-breathe 1.8s ease-in-out infinite alternate;
}

@keyframes clh14-breathe {
  from {
    box-shadow: 0 6px 18px -8px color-mix(in oklch,var(--brand),transparent 30%);
    scale: 1;
  }

  to {
    box-shadow: 0 10px 34px -6px color-mix(in oklch,var(--brand),transparent 12%);
    scale: 1.015;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cle-14 * {
    animation: none !important;
    transition-duration: .01s !important;
  }

  .cle-14__breathe:hover {
    box-shadow: 0 10px 30px -8px color-mix(in oklch,var(--brand),transparent 20%);
  }
}
```
