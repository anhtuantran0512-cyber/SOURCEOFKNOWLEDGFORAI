---
source: "codefronts"
url: "https://codefronts.com/snippets/css-dividers/cyber-dividers/"
title: "Cyberpunk Neon Glow Divider CSS"
section: "snippets"
category: "css-dividers"
category_name: "CSS Dividers"
description: "Real neon is a bright core wrapped in progressively wider, dimmer halos — so this divider stacks four box-shadows at increasing blur and decreasing opacity…"
has_js: "false"
---

Here's a working CSS Divider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Cyberpunk Neon Glow Divider CSS
Source: https://codefronts.com/snippets/css-dividers/cyber-dividers/

Real neon is a bright core wrapped in progressively wider, dimmer halos — so this divider stacks four box-shadows at increasing blur and decreasing opacity instead of one big fuzzy glow, which is what separates convincing neon from a blurry line. Add a scanline overlay, a physically plausible flicker curve, and a glitch-offset label, and you have a dark-mode divider that earns its brightness.
## HTML
```html
<section class="div-13" aria-label="Cyberpunk neon glow divider demo">
  <div class="div-13__stage">
    <div class="div-13__scan" aria-hidden="true"></div>
    <p class="div-13__eyebrow">SECTOR 07 // NIGHT MARKET</p>
    <h2 class="div-13__title" data-txt="NEON RULE">NEON RULE</h2>
    <hr class="div-13__neon">
    <div class="div-13__labelled" role="separator" aria-label="Access divider">
      <span class="div-13__chipneon">ACCESS</span>
    </div>
    <hr class="div-13__neon div-13__neon--alt">
    <p class="div-13__sub">Four stacked shadows. One near-white core. A flicker that isn't a metronome.</p>
    <p class="div-13__chip">box-shadow ×4 falloff · clustered flicker keyframes · scanline overlay</p>
  </div>
</section>
```
## CSS
```css
.div-13 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--div-13-bg);
  --div-13-bg: oklch(0.13 0.03 285);
  --div-13-ink: oklch(0.94 0.02 290);
  --div-13-mut: oklch(0.66 0.04 290);
  --div-13-hue: oklch(0.82 0.17 200);
  --div-13-hue2: oklch(0.72 0.24 350);
  --div-13-core: oklch(0.99 0.03 200);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--div-13-ink);
  position: relative;
  overflow: hidden;
}

.div-13 *,
.div-13 *::before,
.div-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.div-13__stage {
  position: relative;
  min-height: 100svh;
  display: grid;
  place-content: center;
  justify-items: center;
  gap: clamp(16px,3vw,28px);
  text-align: center;
  padding: clamp(30px,6vw,72px) clamp(20px,5vw,56px);
  background: radial-gradient(70% 50% at 50% 46%,oklch(0.22 0.08 290/.85),transparent);
}

.div-13__scan {
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: repeating-linear-gradient(0deg,oklch(0 0 0/.34) 0 1px,transparent 1px 3px);
  mix-blend-mode: overlay;
  opacity: .6;
}

.div-13__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .3em;
  color: var(--div-13-hue2);
  text-shadow: 0 0 10px oklch(0.72 0.24 350/.7);
}

.div-13__title {
  position: relative;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: clamp(30px,7.4vw,76px);
  line-height: 1;
  letter-spacing: .06em;
  font-weight: 800;
  color: var(--div-13-core);
  text-shadow: 0 0 6px var(--div-13-hue),0 0 22px var(--div-13-hue),0 0 56px oklch(0.6 0.16 200/.75);
  animation: div-13-flicker 6.5s steps(1,end) infinite;
}

.div-13__title::before,
.div-13__title::after {
  content: attr(data-txt);
  position: absolute;
  inset: 0;
  opacity: .55;
}

.div-13__title::before {
  color: var(--div-13-hue2);
  translate: -2px 0;
  clip-path: inset(0 0 58% 0);
  text-shadow: none;
}

.div-13__title::after {
  color: var(--div-13-hue);
  translate: 2px 0;
  clip-path: inset(56% 0 0 0);
  text-shadow: none;
}

@keyframes div-13-flicker {
  0%,
    18%,
    20.5%,
    22%,
    24.5%,
    53%,
    55.5%,
    100% {
    opacity: 1;
  }

  19.5%,
    23%,
    54.5% {
    opacity: .4;
    filter: brightness(.65);
  }
}

.div-13__neon {
  width: min(90vw,560px);
  border: 0;
  height: 2px;
  border-radius: 99px;
  background: var(--div-13-core);
  box-shadow: 0 0 4px var(--div-13-hue),0 0 12px var(--div-13-hue),0 0 32px var(--div-13-hue),0 0 72px oklch(0.55 0.15 200/.7);
}

.div-13__neon--alt {
  background: oklch(0.99 0.02 350);
  box-shadow: 0 0 4px var(--div-13-hue2),0 0 12px var(--div-13-hue2),0 0 30px var(--div-13-hue2),0 0 66px oklch(0.5 0.2 350/.7);
}

.div-13__labelled {
  width: min(90vw,560px);
  display: flex;
  align-items: center;
  gap: 16px;
}

.div-13__labelled::before,
.div-13__labelled::after {
  content: '';
  flex: 1 1 0;
  height: 1px;
  background: var(--div-13-hue);
  box-shadow: 0 0 6px var(--div-13-hue),0 0 18px oklch(0.6 0.16 200/.6);
}

.div-13__chipneon {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .24em;
  color: var(--div-13-hue);
  padding: 7px 14px;
  border: 1px solid var(--div-13-hue);
  border-radius: 4px;
  box-shadow: 0 0 10px oklch(0.6 0.16 200/.5),inset 0 0 12px oklch(0.6 0.16 200/.25);
}

.div-13__sub {
  max-width: 46ch;
  font-size: clamp(14px,1.8vw,17px);
  line-height: 1.6;
  color: var(--div-13-mut);
  text-wrap: pretty;
}

.div-13__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--div-13-mut);
  padding: 8px 14px;
  border: 1px solid oklch(1 0 0/.16);
  border-radius: 99px;
  max-width: 92vw;
}

@media (prefers-reduced-motion: reduce) {
  .div-13__title {
    animation: none;
  }
}
```
