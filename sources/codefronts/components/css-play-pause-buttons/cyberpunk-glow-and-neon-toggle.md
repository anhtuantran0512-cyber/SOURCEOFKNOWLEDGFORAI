---
source: "codefronts"
url: "https://codefronts.com/components/css-play-pause-buttons/cyberpunk-glow-and-neon-toggle/"
title: "Cyberpunk Glow & Neon Toggle"
section: "components"
category: "css-play-pause-buttons"
category_name: "CSS Play / Pause Buttons"
description: "Synthwave HUD energy without a single image: the glow is stacked box-shadows, the halo is a blurred pseudo-element clone, the scanlines are a…"
has_js: "false"
---

Here's a working CSS Play / Pause Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Cyberpunk Glow & Neon Toggle
Source: https://codefronts.com/components/css-play-pause-buttons/cyberpunk-glow-and-neon-toggle/

Synthwave HUD energy without a single image: the glow is stacked box-shadows, the halo is a blurred pseudo-element clone, the scanlines are a repeating-linear-gradient, and the whole rig cranks up a stop when playback starts. The trick that keeps it from looking cheap is treating light like light — a tight inner bloom, a wide soft falloff, and a surface tint, all derived from one accent hue.
## HTML
```html
<section class="pp-06" aria-label="Cyberpunk neon glow play pause toggle demo">
  <div class="pp-06__stage">
    <div class="pp-06__rig">
      <p class="pp-06__hud" aria-hidden="true">SIG//7734 · BITRATE 320 · NEO-KYOTO FM</p>
      <input class="pp-06-chk" type="checkbox" id="pp-06-toggle" aria-label="Play or pause the stream">
      <label class="pp-06__btn" for="pp-06-toggle">
        <span class="pp-06__halo" aria-hidden="true"></span>
        <svg viewBox="0 0 24 24" width="30" height="30" aria-hidden="true">
          <path class="pp-06__p" d="M8.8 5.4v13.2L19 12z" fill="currentColor"/>
          <path class="pp-06__q" d="M8 5h3.2v14H8zM12.8 5H16v14h-3.2z" fill="currentColor"/>
        </svg>
      </label>
      <p class="pp-06__state" aria-hidden="true"><span class="pp-06__on">▮ STREAM LIVE</span><span class="pp-06__off">▷ STANDBY</span></p>
    </div>
    <p class="pp-06__chip" aria-hidden="true">stacked box-shadow bloom · blurred ::before halo · CRT scanlines</p>
  </div>
</section>
```
## CSS
```css
.pp-06,
.pp-06 *,
.pp-06 *::before,
.pp-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.pp-06 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--pp-06-bg);
  --pp-06-bg: oklch(0.14 0.03 285);
  --pp-06-ink: oklch(0.95 0.02 200);
  --pp-06-mut: oklch(0.68 0.05 285);
  --pp-06-neon: oklch(0.82 0.18 195);
  --pp-06-neon2: oklch(0.7 0.24 340);
  font-family: ui-monospace,'SFMono-Regular',Menlo,Consolas,monospace;
  color: var(--pp-06-ink);
}

.pp-06__stage {
  position: relative;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 30px;
  padding: clamp(20px,5vw,56px);
  background: radial-gradient(60% 45% at 50% 42%,oklch(0.26 0.1 300/.75),transparent 70%),linear-gradient(180deg,var(--pp-06-bg),oklch(0.1 0.03 290));
}

.pp-06__stage::after {
  content: '';
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: repeating-linear-gradient(to bottom,oklch(0 0 0/.28) 0 1px,transparent 1px 3px);
  mix-blend-mode: multiply;
}

.pp-06__rig {
  position: relative;
  display: grid;
  justify-items: center;
  gap: 26px;
  padding: 38px 44px;
  border: 1px solid color-mix(in oklch,var(--pp-06-neon) 34%,transparent);
  border-radius: 20px;
  background: oklch(0.17 0.04 288/.7);
  box-shadow: 0 0 0 1px oklch(0 0 0/.5),0 0 40px oklch(0.5 0.15 300/.25),inset 0 0 60px oklch(0.3 0.1 300/.25);
}

.pp-06__hud {
  font-size: 11px;
  letter-spacing: .24em;
  color: var(--pp-06-mut);
  text-shadow: 0 0 8px color-mix(in oklch,var(--pp-06-neon2) 60%,transparent);
}

.pp-06-chk {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.pp-06__btn {
  position: relative;
  display: grid;
  place-items: center;
  width: 120px;
  height: 120px;
  border: 2px solid var(--pp-06-neon);
  border-radius: 50%;
  color: var(--pp-06-neon);
  background: oklch(0.18 0.04 250/.5);
  cursor: pointer;
  box-shadow: 0 0 6px color-mix(in oklch,var(--pp-06-neon) 70%,transparent),0 0 22px color-mix(in oklch,var(--pp-06-neon) 45%,transparent),0 0 60px color-mix(in oklch,var(--pp-06-neon) 20%,transparent),inset 0 0 14px color-mix(in oklch,var(--pp-06-neon) 22%,transparent);
  transition: color .35s,border-color .35s,box-shadow .35s,transform .25s cubic-bezier(.34,1.4,.5,1);
}

.pp-06__btn:hover {
  transform: scale(1.05);
}

.pp-06__btn:active {
  transform: scale(.96);
}

.pp-06-chk:focus-visible+.pp-06__btn {
  outline: 2px dashed var(--pp-06-neon2);
  outline-offset: 8px;
}

.pp-06__halo {
  position: absolute;
  inset: -26%;
  z-index: -1;
  border-radius: 50%;
  background: radial-gradient(circle,color-mix(in oklch,var(--pp-06-neon) 55%,transparent),transparent 62%);
  filter: blur(26px);
  opacity: .7;
  transition: opacity .4s,scale .5s cubic-bezier(.34,1.3,.5,1);
}

.pp-06__q {
  display: none;
}

.pp-06-chk:checked+.pp-06__btn {
  color: var(--pp-06-neon2);
  border-color: var(--pp-06-neon2);
  box-shadow: 0 0 8px color-mix(in oklch,var(--pp-06-neon2) 75%,transparent),0 0 30px color-mix(in oklch,var(--pp-06-neon2) 50%,transparent),0 0 82px color-mix(in oklch,var(--pp-06-neon2) 28%,transparent),inset 0 0 20px color-mix(in oklch,var(--pp-06-neon2) 26%,transparent);
}

.pp-06-chk:checked+.pp-06__btn .pp-06__halo {
  opacity: 1;
  scale: 1.3;
  background: radial-gradient(circle,color-mix(in oklch,var(--pp-06-neon2) 60%,transparent),transparent 62%);
}

.pp-06-chk:checked+.pp-06__btn .pp-06__p {
  display: none;
}

.pp-06-chk:checked+.pp-06__btn .pp-06__q {
  display: block;
}

.pp-06__state {
  font-size: 12.5px;
  letter-spacing: .18em;
}

.pp-06__on {
  display: none;
  color: var(--pp-06-neon2);
  text-shadow: 0 0 12px currentColor;
  animation: pp-06-flicker 3.4s steps(1,end) infinite;
}

.pp-06__off {
  color: var(--pp-06-neon);
  text-shadow: 0 0 10px currentColor;
}

.pp-06__rig:has(.pp-06-chk:checked) .pp-06__on {
  display: inline;
}

.pp-06__rig:has(.pp-06-chk:checked) .pp-06__off {
  display: none;
}

@keyframes pp-06-flicker {
  0%,
    92%,
    100% {
    opacity: 1;
  }

  93% {
    opacity: .35;
  }

  94% {
    opacity: 1;
  }

  96% {
    opacity: .55;
  }

  97% {
    opacity: 1;
  }
}

.pp-06__chip {
  position: relative;
  font-size: 11.5px;
  color: var(--pp-06-mut);
  padding: 7px 14px;
  border: 1px solid color-mix(in oklch,var(--pp-06-neon) 25%,transparent);
  border-radius: 99px;
  text-align: center;
}

@media (forced-colors: active) {
  .pp-06__btn {
    border: 2px solid ButtonText;
    color: ButtonText;
  }
}

@media (prefers-reduced-motion: reduce) {
  .pp-06 * {
    animation: none !important;
    transition-duration: .01ms !important;
  }
}
```
