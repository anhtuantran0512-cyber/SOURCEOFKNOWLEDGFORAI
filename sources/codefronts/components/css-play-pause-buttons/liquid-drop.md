---
source: "codefronts"
url: "https://codefronts.com/components/css-play-pause-buttons/liquid-drop/"
title: "Organic Blob Morph Play Button CSS"
section: "components"
category: "css-play-pause-buttons"
category_name: "CSS Play / Pause Buttons"
description: "A button that never sits still: the eight-value border-radius drifts through four keyframes, so the shape breathes like a liquid droplet instead of a circle."
has_js: "false"
---

Here's a working CSS Play / Pause Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Organic Blob Morph Play Button CSS
Source: https://codefronts.com/components/css-play-pause-buttons/liquid-drop/

A button that never sits still: the eight-value border-radius drifts through four keyframes, so the shape breathes like a liquid droplet instead of a circle. On play the blob calms and tightens toward a circle — motion that means something. Zero SVG, zero filters, one keyframe, and it stays perfectly crisp at every size.
## HTML
```html
<section class="pp-22" aria-label="Organic blob morph play button demo">
  <div class="pp-22__stage">
    <div class="pp-22__wrap">
      <input class="pp-22-chk" type="checkbox" id="pp-22-toggle" aria-label="Play or pause the ambient set">
      <label class="pp-22__btn" for="pp-22-toggle">
        <span class="pp-22__ghost" aria-hidden="true"></span>
        <span class="pp-22__blob" aria-hidden="true"></span>
        <svg class="pp-22__icon" viewBox="0 0 24 24" width="32" height="32" aria-hidden="true">
          <path class="pp-22__p" d="M9.2 5.6v12.8L19 12z" fill="currentColor"/>
          <path class="pp-22__q" d="M8.8 5.6h3.2v12.8H8.8zM13 5.6h3.2v12.8H13z" fill="currentColor"/>
        </svg>
      </label>
      <p class="pp-22__cap">Ambient set<span>8-value border-radius drift</span></p>
    </div>
    <p class="pp-22__chip" aria-hidden="true">border-radius: a b c d / e f g h · reversed second layer · calm on play</p>
  </div>
</section>
```
## CSS
```css
.pp-22,
.pp-22 *,
.pp-22 *::before,
.pp-22 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pp-22 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--pp-22-bg);
  --pp-22-bg: oklch(0.96 0.02 40);
  --pp-22-ink: oklch(0.26 0.03 30);
  --pp-22-mut: oklch(0.55 0.03 30);
  --pp-22-c1: oklch(0.75 0.16 30);
  --pp-22-c2: oklch(0.72 0.15 350);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--pp-22-ink);
}

.pp-22__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 26px;
  padding: clamp(20px,5vw,56px);
  background: radial-gradient(70% 55% at 50% 45%,oklch(0.93 0.06 35/.9),transparent 72%);
}

.pp-22__wrap {
  display: grid;
  justify-items: center;
  gap: 26px;
}

.pp-22-chk {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.pp-22__btn {
  position: relative;
  display: grid;
  place-items: center;
  width: 170px;
  height: 170px;
  color: oklch(0.99 0 0);
  cursor: pointer;
  transition: scale .3s cubic-bezier(.34,1.4,.5,1);
}

.pp-22__btn:hover {
  scale: 1.05;
}

.pp-22-chk:focus-visible+.pp-22__btn .pp-22__blob {
  outline: 3px solid var(--pp-22-ink);
  outline-offset: 6px;
}

.pp-22__blob,
.pp-22__ghost {
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg,var(--pp-22-c1),var(--pp-22-c2));
  border-radius: 58% 42% 47% 53%/44% 52% 48% 56%;
  animation: pp-22-blob 9s ease-in-out infinite;
  transition: border-radius .8s ease,animation-duration .6s;
}

.pp-22__ghost {
  inset: -14px;
  opacity: .32;
  filter: blur(10px);
  animation-duration: 13s;
  animation-direction: reverse;
}

.pp-22__icon {
  position: relative;
  z-index: 1;
  filter: drop-shadow(0 2px 6px oklch(0.4 0.1 30/.4));
}

.pp-22__q {
  display: none;
}

.pp-22-chk:checked+.pp-22__btn .pp-22__blob {
  border-radius: 50%;
  animation-duration: 22s;
}

.pp-22-chk:checked+.pp-22__btn .pp-22__ghost {
  border-radius: 50%;
  animation-duration: 26s;
  opacity: .45;
}

.pp-22-chk:checked+.pp-22__btn .pp-22__p {
  display: none;
}

.pp-22-chk:checked+.pp-22__btn .pp-22__q {
  display: block;
}

@keyframes pp-22-blob {
  0%,
    100% {
    border-radius: 58% 42% 47% 53%/44% 52% 48% 56%;
  }

  25% {
    border-radius: 44% 56% 62% 38%/56% 40% 60% 44%;
  }

  50% {
    border-radius: 52% 48% 38% 62%/62% 56% 44% 38%;
  }

  75% {
    border-radius: 38% 62% 55% 45%/40% 46% 54% 60%;
  }
}

.pp-22__cap {
  text-align: center;
  font-size: 15px;
  font-weight: 640;
}

.pp-22__cap span {
  display: block;
  margin-top: 4px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  font-weight: 400;
  color: var(--pp-22-mut);
}

.pp-22__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--pp-22-mut);
  padding: 7px 14px;
  border: 1px solid oklch(0.26 0.03 30/.16);
  border-radius: 99px;
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .pp-22__blob,
    .pp-22__ghost {
    animation: none;
    border-radius: 52% 48% 44% 56%/48% 52% 48% 52%;
  }
}
```
