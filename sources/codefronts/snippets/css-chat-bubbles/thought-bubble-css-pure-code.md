---
source: "codefronts"
url: "https://codefronts.com/snippets/css-chat-bubbles/thought-bubble-css-pure-code/"
title: "Thought Bubble CSS Pure Code"
section: "snippets"
category: "css-chat-bubbles"
category_name: "CSS Chat Bubbles"
description: "A cloud-shaped thought bubble with descending circles, built three ways: gradient cloud (the whole shape painted with layered radial-gradients), masked cloud…"
has_js: "false"
---

Here's a working CSS Chat Bubble from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Thought Bubble CSS Pure Code
Source: https://codefronts.com/snippets/css-chat-bubbles/thought-bubble-css-pure-code/

A cloud-shaped thought bubble with descending circles, built three ways: gradient cloud (the whole shape painted with layered radial-gradients), masked cloud (the same geometry used as a mask so the bubble can be filled with a photo or gradient), and outline cloud (the masked shape stroked with drop-shadow). The bubble and its trailing circles drift on independent, staggered loops.
## HTML
```html
<div class="cb-14">
  <input class="cb-14__sr" type="radio" name="cb-14-kind" id="cb-14-solid" checked>
  <input class="cb-14__sr" type="radio" name="cb-14-kind" id="cb-14-mask">
  <input class="cb-14__sr" type="radio" name="cb-14-kind" id="cb-14-outline">

  <div class="cb-14__stage">
    <div class="cb-14__scene">
      <div class="cb-14__thought">
        <div class="cb-14__cloud">
          <p class="cb-14__text">What if the whole thing is just four circles and a rectangle?</p>
        </div>
        <span class="cb-14__puff" style="--i:0" aria-hidden="true"></span>
        <span class="cb-14__puff" style="--i:1" aria-hidden="true"></span>
        <span class="cb-14__puff" style="--i:2" aria-hidden="true"></span>
      </div>
      <img class="cb-14__who" src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?auto=format&fit=facearea&facepad=2.6&w=320&h=320&q=70" width="120" height="120" alt="Theo Almeida, mid-thought" loading="lazy" decoding="async">
    </div>

    <div class="cb-14__switch" role="radiogroup" aria-label="Cloud technique">
      <label class="cb-14__chip" for="cb-14-solid">Gradient</label>
      <label class="cb-14__chip" for="cb-14-mask">Masked fill</label>
      <label class="cb-14__chip" for="cb-14-outline">Outline</label>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@500;600;700&display=swap');

@property --cb-14-lift {
  syntax: '<length>';
  inherits: false;
  initial-value: 0px;
}

.cb-14 {
  --bg: #eef0fb;
  --fill: #ffffff;
  --ink: #181a2e;
  --muted: #5f6484;
  --a: #8b7bff;
  --b: #57d2ff;
  --line: #dfe2f2;
  --shadow: rgba(24,26,46,.16);
  --sans: "Quicksand",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
  background: radial-gradient(70% 50% at 30% 10%, color-mix(in oklab,var(--a) 22%,transparent), transparent 62%), radial-gradient(60% 45% at 85% 80%, color-mix(in oklab,var(--b) 22%,transparent), transparent 60%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.cb-14,
.cb-14 *,
.cb-14 *::before,
.cb-14 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .cb-14 {
    --bg: oklch(95% .015 275);
    --ink: oklch(22% .04 280);
    --muted: oklch(50% .04 280);
    --a: oklch(68% .17 290);
    --b: oklch(82% .13 225);
    --line: oklch(90% .02 280);
  }
}

.cb-14__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  opacity: 0;
}

.cb-14__stage {
  inline-size: min(100%,42rem);
  display: grid;
  gap: clamp(1.5rem,4vw,2.5rem);
  justify-items: center;
}

.cb-14__scene {
  position: relative;
  inline-size: 100%;
  display: grid;
  justify-items: center;
  gap: 0;
  padding-block-end: 1rem;
}
/* ── the thought ── */

.cb-14__thought {
  position: relative;
  inline-size: min(100%,26rem);
  justify-self: center;
}

.cb-14__cloud {
  position: relative;
  aspect-ratio: 16/9;
  display: grid;
  place-items: center;
  padding: 14% 17% 16%;
  background-color: transparent;
  background-image: radial-gradient(circle at 50% 50%, var(--fill) 70%, transparent 71%), radial-gradient(circle at 50% 50%, var(--fill) 70%, transparent 71%), radial-gradient(circle at 50% 50%, var(--fill) 70%, transparent 71%), radial-gradient(circle at 50% 50%, var(--fill) 70%, transparent 71%), linear-gradient(var(--fill) 0 0);
  background-size: 44% 74%, 40% 64%, 50% 60%, 34% 52%, 72% 54%;
  background-position: 1% 30%, 99% 40%, 42% 0%, 76% 8%, 50% 66%;
  background-repeat: no-repeat;
  filter: drop-shadow(0 18px 30px color-mix(in oklab,var(--shadow) 70%,transparent));
  animation: cb-14-float 6.5s ease-in-out infinite;
}

.cb-14__text {
  margin: 0;
  text-align: center;
  text-wrap: balance;
  font-size: clamp(1rem,3.2vw,1.35rem);
  font-weight: 600;
  line-height: 1.35;
  letter-spacing: -.015em;
  color: var(--ink);
}

@keyframes cb-14-float {
  0%,
    100% {
    translate: 0 0;
  }

  50% {
    translate: 0 -10px;
  }
}

.cb-14__puff {
  position: absolute;
  border-radius: 50%;
  background: var(--fill);
  filter: drop-shadow(0 6px 12px color-mix(in oklab,var(--shadow) 60%,transparent));
  animation: cb-14-drift 4.2s ease-in-out infinite;
  animation-delay: calc(var(--i) * -700ms);
}

.cb-14__puff:nth-of-type(1) {
  inline-size: 2.6rem;
  block-size: 2.6rem;
  inset-block-end: -1.1rem;
  inset-inline-start: 22%;
}

.cb-14__puff:nth-of-type(2) {
  inline-size: 1.6rem;
  block-size: 1.6rem;
  inset-block-end: -3rem;
  inset-inline-start: 15%;
}

.cb-14__puff:nth-of-type(3) {
  inline-size: .95rem;
  block-size: .95rem;
  inset-block-end: -4.4rem;
  inset-inline-start: 10%;
}

@keyframes cb-14-drift {
  0%,
    100% {
    translate: 0 0;
    scale: 1;
  }

  50% {
    translate: -4px -6px;
    scale: 1.07;
  }
}

.cb-14__who {
  position: relative;
  z-index: 1;
  margin-block-start: 2.75rem;
  inline-size: clamp(5rem,18vw,7.5rem);
  block-size: clamp(5rem,18vw,7.5rem);
  border-radius: 50%;
  object-fit: cover;
  object-position: 50% 25%;
  border: 5px solid var(--fill);
  background: var(--line);
  box-shadow: 0 20px 40px -22px var(--shadow);
}
/* ═══ MASKED FILL ═══ */

.cb-14:has(#cb-14-mask:checked) .cb-14__cloud,
.cb-14:has(#cb-14-outline:checked) .cb-14__cloud {
  background-image: linear-gradient(140deg, var(--a), var(--b));
  background-size: 100% 100%;
  background-position: 0 0;
  -webkit-mask-image: radial-gradient(circle at 50% 50%, #000 70%, transparent 71%), radial-gradient(circle at 50% 50%, #000 70%, transparent 71%), radial-gradient(circle at 50% 50%, #000 70%, transparent 71%), radial-gradient(circle at 50% 50%, #000 70%, transparent 71%), linear-gradient(#000 0 0);
  mask-image: radial-gradient(circle at 50% 50%, #000 70%, transparent 71%), radial-gradient(circle at 50% 50%, #000 70%, transparent 71%), radial-gradient(circle at 50% 50%, #000 70%, transparent 71%), radial-gradient(circle at 50% 50%, #000 70%, transparent 71%), linear-gradient(#000 0 0);
  -webkit-mask-size: 44% 74%, 40% 64%, 50% 60%, 34% 52%, 72% 54%;
  mask-size: 44% 74%, 40% 64%, 50% 60%, 34% 52%, 72% 54%;
  -webkit-mask-position: 1% 30%, 99% 40%, 42% 0%, 76% 8%, 50% 66%;
  mask-position: 1% 30%, 99% 40%, 42% 0%, 76% 8%, 50% 66%;
  -webkit-mask-repeat: no-repeat;
  mask-repeat: no-repeat;
}

.cb-14:has(#cb-14-mask:checked) .cb-14__text,
.cb-14:has(#cb-14-outline:checked) .cb-14__text {
  color: #fff;
}

.cb-14:has(#cb-14-mask:checked) .cb-14__puff,
.cb-14:has(#cb-14-outline:checked) .cb-14__puff {
  background: linear-gradient(140deg, var(--a), var(--b));
}
/* ═══ OUTLINE ═══ */

.cb-14:has(#cb-14-outline:checked) .cb-14__cloud {
  background-image: linear-gradient(140deg, color-mix(in oklab,var(--a) 14%,var(--fill)), color-mix(in oklab,var(--b) 16%,var(--fill)));
  filter: drop-shadow(2px 0 0 var(--ink)) drop-shadow(-2px 0 0 var(--ink)) drop-shadow(0 2px 0 var(--ink)) drop-shadow(0 -2px 0 var(--ink));
}

.cb-14:has(#cb-14-outline:checked) .cb-14__text {
  color: var(--ink);
}

.cb-14:has(#cb-14-outline:checked) .cb-14__puff {
  background: color-mix(in oklab,var(--a) 14%,var(--fill));
  filter: drop-shadow(2px 0 0 var(--ink)) drop-shadow(-2px 0 0 var(--ink)) drop-shadow(0 2px 0 var(--ink)) drop-shadow(0 -2px 0 var(--ink));
}

.cb-14:has(#cb-14-outline:checked) .cb-14__who {
  border-color: var(--ink);
}
/* ── switch ── */

.cb-14__switch {
  display: flex;
  flex-wrap: wrap;
  gap: .4rem;
  justify-content: center;
  padding: .4rem;
  border-radius: 1.1rem;
  border: 1px solid var(--line);
  background: color-mix(in oklab,var(--fill) 72%,transparent);
  backdrop-filter: blur(12px);
}

.cb-14__chip {
  min-block-size: 44px;
  display: grid;
  place-items: center;
  padding: .5rem 1.1rem;
  cursor: pointer;
  border-radius: .8rem;
  color: var(--muted);
  font-size: .86rem;
  font-weight: 700;
  letter-spacing: -.01em;
  transition: background .22s, color .22s, transform .22s cubic-bezier(.16,1,.3,1);
}

.cb-14__chip:hover {
  color: var(--ink);
  transform: translateY(-1px);
}

#cb-14-solid:checked ~ .cb-14__stage .cb-14__chip[for="cb-14-solid"],
#cb-14-mask:checked ~ .cb-14__stage .cb-14__chip[for="cb-14-mask"],
#cb-14-outline:checked ~ .cb-14__stage .cb-14__chip[for="cb-14-outline"] {
  background: linear-gradient(120deg,var(--a),var(--b));
  color: #fff;
}

#cb-14-solid:focus-visible ~ .cb-14__stage .cb-14__chip[for="cb-14-solid"],
#cb-14-mask:focus-visible ~ .cb-14__stage .cb-14__chip[for="cb-14-mask"],
#cb-14-outline:focus-visible ~ .cb-14__stage .cb-14__chip[for="cb-14-outline"] {
  outline: 2px solid var(--a);
  outline-offset: 2px;
}

@media (prefers-color-scheme: dark) {
  .cb-14 {
    --bg: #0b0c16;
    --fill: #171a2b;
    --ink: #eceefb;
    --muted: #9aa0c0;
    --line: #232741;
    --shadow: rgba(0,0,0,.7);
  }

  .cb-14:has(#cb-14-outline:checked) {
    --ink: #eceefb;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cb-14 *,
    .cb-14 *::before,
    .cb-14 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .cb-14__cloud {
    filter: none;
    background: Canvas;
    border: 2px solid CanvasText;
    border-radius: 2rem;
  }

  .cb-14__puff {
    background: CanvasText;
    filter: none;
  }
}
```
