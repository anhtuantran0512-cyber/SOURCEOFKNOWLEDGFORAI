---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-hover-effects/neon-glow-flicker-text-effect/"
title: "Neon Glow / Flicker Text Effect"
section: "motion"
category: "css-text-hover-effects"
category_name: "CSS Text Hover Effects"
description: "A bar sign that ignites on hover: five stacked text-shadows build the tube glow (white-hot core, tight halo, wide bloom), a steps(1) keyframe sputters…"
has_js: "false"
---

Here's a working CSS Text Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neon Glow / Flicker Text Effect
Source: https://codefronts.com/motion/css-text-hover-effects/neon-glow-flicker-text-effect/

A bar sign that ignites on hover: five stacked text-shadows build the tube glow (white-hot core, tight halo, wide bloom), a steps(1) keyframe sputters through the power-on like real gas catching, and one letter — the W, obviously — stays faulty, buzzing on its own clock even after ignition. Off-state isn't invisible: the tubes read as dim glass, the honest resting state of a real sign. Everything is color + text-shadow, so the markup is one anchor and the words stay words.
## HTML
```html
<section class="cth-07" aria-label="Neon flicker text demo">
  <div class="cth-07__stage">
    <div class="cth-07__scene">
      <a class="cth-07__sign" href="#cth07-top" id="cth07-top" aria-label="Night Owl — cocktails till 3 a.m.">
        <span class="cth-07__word" aria-hidden="true">NIGHT</span>
        <span class="cth-07__word cth-07__word--pink" aria-hidden="true">O<i class="cth-07__faulty">W</i>L</span>
        <span class="cth-07__pill" aria-hidden="true">cocktails &middot; til 3 a.m.</span>
      </a>
      <p class="cth-07__hint">Hover the sign and hold &mdash; ignition is a <code>steps(1)</code> sputter, the glow is five stacked <code>text-shadow</code> layers, and the W was always going to be the problem.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.cth-07,
.cth-07 *,
.cth-07 *::before,
.cth-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cth-07 {
  --wall: oklch(0.16 0.012 310);
  --tube: oklch(0.83 0.14 195);
  --tube2: oklch(0.73 0.21 350);
  --off: oklch(0.42 0.03 220);
  --off2: oklch(0.42 0.06 350);
  --mut: oklch(0.6 0.02 300);
  font-family: ui-rounded,'SF Pro Rounded','Segoe UI',system-ui,sans-serif;
  color: oklch(0.93 0.01 300);
}

.cth-07__stage {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  background: radial-gradient(80% 60% at 50% 38%,oklch(0.2 0.02 310),var(--wall) 72%);
  padding: clamp(20px,4vw,56px);
  container: cth07/inline-size;
}

.cth-07__scene {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: clamp(22px,4cqi,34px);
  text-align: center;
}

.cth-07__sign {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: clamp(8px,1.6cqi,14px);
  text-decoration: none;
  padding: clamp(20px,4cqi,36px) clamp(26px,5cqi,52px);
  border-radius: 22px;
}

.cth-07__sign:focus-visible {
  outline: 2px solid var(--tube);
  outline-offset: 6px;
}

.cth-07__word {
  display: block;
  font-size: clamp(52px,12cqi,120px);
  font-weight: 800;
  letter-spacing: .06em;
  line-height: .95;
  color: var(--off);
  text-shadow: 0 0 .1em color-mix(in oklch,var(--tube) 18%,transparent);
  transition: color .45s ease,text-shadow .45s ease;
}

.cth-07__word--pink {
  color: var(--off2);
  text-shadow: 0 0 .1em color-mix(in oklch,var(--tube2) 18%,transparent);
}

.cth-07__sign:hover .cth-07__word,
.cth-07__sign:focus-visible .cth-07__word {
  color: oklch(0.97 0.03 195);
  text-shadow: 0 0 .03em oklch(1 0 0/.9),0 0 .12em var(--tube),0 0 .35em var(--tube),0 0 .85em color-mix(in oklch,var(--tube) 65%,transparent),0 0 1.6em color-mix(in oklch,var(--tube) 40%,transparent);
  animation: cth07-ignite .95s steps(1,end);
}

.cth-07__sign:hover .cth-07__word--pink,
.cth-07__sign:focus-visible .cth-07__word--pink {
  color: oklch(0.94 0.06 350);
  text-shadow: 0 0 .03em oklch(1 0 0/.9),0 0 .12em var(--tube2),0 0 .35em var(--tube2),0 0 .85em color-mix(in oklch,var(--tube2) 65%,transparent),0 0 1.6em color-mix(in oklch,var(--tube2) 40%,transparent);
  animation: cth07-ignite 1.15s steps(1,end);
}

@keyframes cth07-ignite {
  0%,
    9%,
    24%,
    56% {
    color: inherit;
    text-shadow: none;
    opacity: .4;
  }

  5%,
    12%,
    28%,
    54%,
    60%,
    100% {
    opacity: 1;
  }
}

.cth-07__faulty {
  font-style: normal;
  animation: cth07-buzz-off 5s steps(1,end) infinite;
}

.cth-07__sign:hover .cth-07__faulty,
.cth-07__sign:focus-visible .cth-07__faulty {
  animation: cth07-buzz-on 3.2s steps(1,end) infinite;
}

@keyframes cth07-buzz-off {
  0%,
    100% {
    opacity: 1;
  }

  7%,
    9.5%,
    42% {
    opacity: .55;
  }

  8%,
    43.5%,
    71% {
    opacity: 1;
  }

  70% {
    opacity: .7;
  }
}

@keyframes cth07-buzz-on {
  0%,
    100% {
    opacity: 1;
  }

  11%,
    13%,
    57%,
    58.6% {
    opacity: .5;
  }

  12%,
    14%,
    58%,
    60% {
    opacity: 1;
  }
}

.cth-07__pill {
  margin-top: 6px;
  font-size: clamp(13px,2cqi,17px);
  font-weight: 700;
  letter-spacing: .22em;
  text-transform: lowercase;
  color: var(--off2);
  border: 2px solid color-mix(in oklch,var(--off2) 60%,transparent);
  border-radius: 99px;
  padding: 10px 22px;
  transition: color .5s ease,border-color .5s ease,box-shadow .5s ease,text-shadow .5s ease;
}

.cth-07__sign:hover .cth-07__pill,
.cth-07__sign:focus-visible .cth-07__pill {
  color: oklch(0.94 0.06 350);
  border-color: var(--tube2);
  text-shadow: 0 0 .3em var(--tube2);
  box-shadow: 0 0 .6em color-mix(in oklch,var(--tube2) 55%,transparent),inset 0 0 .5em color-mix(in oklch,var(--tube2) 35%,transparent);
  transition-delay: .18s;
}

.cth-07__hint {
  font-size: 12.5px;
  line-height: 1.7;
  color: var(--mut);
  max-width: 52ch;
}

.cth-07__hint code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .92em;
  background: oklch(0.24 0.015 310);
  padding: 1px 6px;
  border-radius: 4px;
  color: var(--tube);
}

@media (prefers-reduced-motion: reduce) {
  .cth-07 * {
    animation: none !important;
    transition-duration: .25s !important;
  }
}
```
