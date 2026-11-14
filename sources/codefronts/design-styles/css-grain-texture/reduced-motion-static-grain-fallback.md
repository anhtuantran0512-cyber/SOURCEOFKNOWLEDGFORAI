---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-grain-texture/reduced-motion-static-grain-fallback/"
title: "Reduced Motion Static Grain Fallback"
section: "design-styles"
category: "css-grain-texture"
category_name: "CSS Grain and Noise Textures"
description: "Animated grain is the most convincing film effect on the web and the most likely thing in this collection to make somebody ill."
has_js: "false"
---

Here's a working CSS Grain and Noise Texture from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Reduced Motion Static Grain Fallback
Source: https://codefronts.com/design-styles/css-grain-texture/reduced-motion-static-grain-fallback/

Animated grain is the most convincing film effect on the web and the most likely thing in this collection to make somebody ill. This demo ships both halves properly: a real projector-gate animation built the performant way, and a static fallback that is a genuine design rather than a switched-off version — plus the reasoning for why flicker is the specific risk.
## HTML
```html
<section class="grn-20" aria-labelledby="grn-20-title">
  <div class="grn-20__theme">
    <input class="grn-20__theme-input" type="checkbox" id="grn-20-theme">
    <label class="grn-20__theme-label" for="grn-20-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="grn-20__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="grn-20__gate">
    <img class="grn-20__frame" src="https://picsum.photos/id/1016/2000/1200" alt="" aria-hidden="true" width="2000" height="1200">
    <span class="grn-20__weave" aria-hidden="true"></span>
    <span class="grn-20__grain" aria-hidden="true"></span>
    <span class="grn-20__vignette" aria-hidden="true"></span>

    <div class="grn-20__copy">
      <p class="grn-20__mode">
        <span class="grn-20__mode-anim">Projector running · animated grain</span>
        <span class="grn-20__mode-still">Reduced motion · static frame held</span>
      </p>
      <h1 class="grn-20__h1" id="grn-20-title">Reel four, gate check</h1>
      <p class="grn-20__lede">The grain layer translates on the compositor in eight discrete steps. If your system asks for reduced motion, it stops — and a heavier, deliberately composed static treatment takes over.</p>
    </div>
  </div>

  <main class="grn-20__shell">
    <section class="grn-20__cards" aria-labelledby="grn-20-h-rules">
      <h2 class="grn-20__h2" id="grn-20-h-rules">Four rules for animated texture</h2>
      <ul class="grn-20__list">
        <li class="grn-20__card">
          <span class="grn-20__num">01</span>
          <b>Translate, never background-position</b>
          <span>One is a compositor transform. The other repaints a viewport-sized background every frame.</span>
        </li>
        <li class="grn-20__card">
          <span class="grn-20__num">02</span>
          <b>steps(), never linear</b>
          <span>Film grain jumps between frames. A smooth slide reads as sandpaper being dragged.</span>
        </li>
        <li class="grn-20__card">
          <span class="grn-20__num">03</span>
          <b>Never animate filter: url()</b>
          <span>The turbulence re-evaluates every frame. Animate a static texture layer instead.</span>
        </li>
        <li class="grn-20__card">
          <span class="grn-20__num">04</span>
          <b>Design the fallback</b>
          <span>Not <code>animation: none</code>. Heavier grain, a vignette, one composed frame — a real design.</span>
        </li>
      </ul>
    </section>

    <aside class="grn-20__close">
      <h2 class="grn-20__h3">Why flicker is the specific risk</h2>
      <p class="grn-20__close-b">Vestibular disorders, migraine and photosensitivity respond to rapid luminance change over large areas more reliably than to movement. Animated grain is precisely that. If it flickers across a large surface, honour <code>prefers-reduced-motion</code> without exception — and give those users a treatment you would be happy to ship as the only one.</p>
    </aside>
  </main>
</section>
```
## CSS
```css
.grn-20 {
  --grn-20-noise: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cfilter id='grn20n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.82' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='200' height='200' filter='url(%23grn20n)'/%3E%3C/svg%3E");
  --grn-20-bg: #0b0b0c;
  --grn-20-surf: #16161a;
  --grn-20-line: #292930;
  --grn-20-ink: #f2f1ee;
  --grn-20-mut: #9b988f;
  --grn-20-acc: #e5c07b;
  --grn-20-acc: oklch(83% 0.11 88);
  --grn-20-gate: 0.9s;
  --grn-20-anim: 0.11;
  --grn-20-static: 0.17;
  --grn-20-font-display: "Space Grotesk", "Inter Tight", ui-sans-serif, system-ui, sans-serif;
  --grn-20-font-mono: ui-monospace, "SFMono-Regular", "JetBrains Mono", Menlo, monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--grn-20-bg);
  color: var(--grn-20-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.grn-20 *,
.grn-20 *::before,
.grn-20 *::after {
  box-sizing: border-box;
}

.grn-20 :focus-visible {
  outline: 2px solid var(--grn-20-acc);
  outline-offset: 3px;
}

.grn-20 code {
  font-family: var(--grn-20-font-mono);
  font-size: 0.9em;
}

.grn-20__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.grn-20:has(.grn-20__theme-input:checked) {
  --grn-20-bg: #f3f2ef;
  --grn-20-surf: #ffffff;
  --grn-20-line: #dedbd4;
  --grn-20-ink: #0b0b0c;
  --grn-20-mut: #615e57;
  --grn-20-acc: #8a6314;
  --grn-20-acc: oklch(50% 0.1 78);
}

@media (prefers-color-scheme: light) {
  .grn-20 {
    --grn-20-bg: #f3f2ef;
    --grn-20-surf: #ffffff;
    --grn-20-line: #dedbd4;
    --grn-20-ink: #0b0b0c;
    --grn-20-mut: #615e57;
    --grn-20-acc: #8a6314;
    --grn-20-acc: oklch(50% 0.1 78);
  }

  .grn-20:has(.grn-20__theme-input:checked) {
    --grn-20-bg: #0b0b0c;
    --grn-20-surf: #16161a;
    --grn-20-line: #292930;
    --grn-20-ink: #f2f1ee;
    --grn-20-mut: #9b988f;
    --grn-20-acc: #e5c07b;
    --grn-20-acc: oklch(83% 0.11 88);
  }
}

@media (prefers-color-scheme: dark) {
  .grn-20:has(.grn-20__theme-input:checked) {
    --grn-20-bg: #f3f2ef;
    --grn-20-surf: #ffffff;
    --grn-20-line: #dedbd4;
    --grn-20-ink: #0b0b0c;
    --grn-20-mut: #615e57;
    --grn-20-acc: #8a6314;
    --grn-20-acc: oklch(50% 0.1 78);
  }
}

.grn-20__theme {
  position: absolute;
  inset-block-start: clamp(1rem, 3vw, 1.75rem);
  inset-inline-end: clamp(0.85rem, 3vw, 1.75rem);
  z-index: 60;
}

.grn-20__theme-input {
  position: absolute;
  inset: 0;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.grn-20__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 999px;
  background: rgba(10, 10, 12, 0.5);
  color: #f2f1ee;
  cursor: pointer;
  backdrop-filter: blur(8px);
}

.grn-20__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.grn-20__gate {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  display: grid;
  align-items: end;
  min-block-size: min(82svh, 42rem);
  background: #0b0b0c;
}

.grn-20__frame {
  position: absolute;
  inset: 0;
  z-index: 0;
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
  filter: grayscale(0.55) contrast(1.12) brightness(0.86) sepia(0.12);
}

.grn-20__weave {
  position: absolute;
  inset: 0;
  z-index: 1;
  pointer-events: none;
  background-image: repeating-linear-gradient(0deg, rgba(255, 255, 255, 0.035) 0 1px, transparent 1px 3px);
  opacity: 0.7;
}

.grn-20__grain {
  position: absolute;
  inset: -25%;
  z-index: 2;
  pointer-events: none;
  background-image: var(--grn-20-noise);
  opacity: var(--grn-20-anim);
  mix-blend-mode: overlay;
  animation: grn-20-gate var(--grn-20-gate) steps(8) infinite;
  will-change: transform;
}

.grn-20__vignette {
  position: absolute;
  inset: 0;
  z-index: 3;
  pointer-events: none;
  background: radial-gradient(122% 100% at 50% 44%, transparent 42%, rgba(4, 4, 5, 0.35) 78%, rgba(4, 4, 5, 0.66) 100%);
}

@keyframes grn-20-gate {
  0% {
    transform: translate3d(0, 0, 0);
  }

  12% {
    transform: translate3d(-3%, 2%, 0);
  }

  25% {
    transform: translate3d(4%, -3%, 0);
  }

  37% {
    transform: translate3d(-5%, -1%, 0);
  }

  50% {
    transform: translate3d(2%, 4%, 0);
  }

  62% {
    transform: translate3d(-2%, -4%, 0);
  }

  75% {
    transform: translate3d(5%, 1%, 0);
  }

  87% {
    transform: translate3d(-4%, 3%, 0);
  }

  100% {
    transform: translate3d(0, 0, 0);
  }
}

.grn-20__copy {
  position: relative;
  z-index: 5;
  inline-size: min(72rem, calc(100% - clamp(1.5rem, 5vw, 4rem)));
  margin-inline: auto;
  display: grid;
  gap: 0.8rem;
  max-inline-size: 42rem;
  padding-block: clamp(2.5rem, 8vw, 4.5rem);
  color: #f6f4f0;
}

.grn-20__mode {
  margin: 0;
  justify-self: start;
  padding: 0.35rem 0.75rem;
  border: 1px solid rgba(255, 255, 255, 0.26);
  border-radius: 999px;
  background: rgba(8, 8, 10, 0.45);
  font: 500 0.72rem/1.4 var(--grn-20-font-mono);
  letter-spacing: 0.1em;
  text-transform: uppercase;
  backdrop-filter: blur(5px);
}

.grn-20__mode-still {
  display: none;
}

.grn-20__h1 {
  margin: 0;
  font: 600 clamp(2.2rem, 7vw, 4.4rem)/0.98 var(--grn-20-font-display);
  letter-spacing: -0.04em;
  text-wrap: balance;
}

.grn-20__lede {
  margin: 0;
  max-inline-size: 34rem;
  color: rgba(246, 244, 240, 0.86);
  font-size: clamp(0.96rem, 2vw, 1.11rem);
  text-wrap: pretty;
}

.grn-20__shell {
  inline-size: min(72rem, calc(100% - clamp(1.5rem, 5vw, 4rem)));
  margin-inline: auto;
  padding-block: clamp(2.5rem, 7vw, 4rem);
  display: grid;
  gap: clamp(1.6rem, 4vw, 2.4rem);
}

.grn-20__cards {
  display: grid;
  gap: 1rem;
}

.grn-20__h2 {
  margin: 0;
  padding-block-end: 0.7rem;
  border-block-end: 1px solid var(--grn-20-line);
  font: 600 clamp(1.2rem, 3vw, 1.6rem)/1.2 var(--grn-20-font-display);
  letter-spacing: -0.025em;
}

.grn-20__list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: clamp(0.7rem, 1.8vw, 1.1rem);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 15rem), 1fr));
}

.grn-20__card {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  display: grid;
  gap: 0.3rem;
  align-content: start;
  padding: clamp(1rem, 2.4vw, 1.4rem);
  border: 1px solid var(--grn-20-line);
  border-radius: 14px;
  background: var(--grn-20-surf);
  min-inline-size: 0;
}

.grn-20__card::after {
  content: "";
  position: absolute;
  inset: 0;
  z-index: -1;
  pointer-events: none;
  background-image: var(--grn-20-noise);
  opacity: 0.05;
  mix-blend-mode: overlay;
}

.grn-20__num {
  font: 500 0.7rem/1 var(--grn-20-font-mono);
  letter-spacing: 0.14em;
  color: var(--grn-20-acc);
}

.grn-20__card b {
  font: 600 0.98rem/1.25 var(--grn-20-font-display);
  letter-spacing: -0.01em;
  text-wrap: balance;
}

.grn-20__card span:last-child {
  color: var(--grn-20-mut);
  font-size: 0.85rem;
  text-wrap: pretty;
}

.grn-20__close {
  display: grid;
  gap: 0.5rem;
  padding: clamp(1.2rem, 3vw, 1.8rem);
  border: 1px solid var(--grn-20-line);
  border-radius: 14px;
  background: color-mix(in oklab, var(--grn-20-acc) 8%, transparent);
}

.grn-20__h3 {
  margin: 0;
  font: 600 1.05rem/1.2 var(--grn-20-font-display);
}

.grn-20__close-b {
  margin: 0;
  max-inline-size: 52rem;
  color: var(--grn-20-mut);
  font-size: 0.92rem;
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .grn-20__grain {
    animation: none;
    inset: 0;
    opacity: var(--grn-20-static);
    mix-blend-mode: soft-light;
    will-change: auto;
  }

  .grn-20__weave {
    opacity: 0.45;
  }

  .grn-20__vignette {
    background: radial-gradient(118% 100% at 50% 42%, transparent 34%, rgba(4, 4, 5, 0.44) 74%, rgba(4, 4, 5, 0.78) 100%);
  }

  .grn-20__frame {
    filter: grayscale(0.7) contrast(1.18) brightness(0.82) sepia(0.16);
  }

  .grn-20__mode-anim {
    display: none;
  }

  .grn-20__mode-still {
    display: inline;
  }

  .grn-20 * {
    transition-duration: 1ms !important;
  }
}
```
