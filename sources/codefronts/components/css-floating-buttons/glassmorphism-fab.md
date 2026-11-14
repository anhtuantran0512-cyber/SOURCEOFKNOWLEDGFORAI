---
source: "codefronts"
url: "https://codefronts.com/components/css-floating-buttons/glassmorphism-fab/"
title: "Glassmorphism Floating Action Button with Backdrop Blur"
section: "components"
category: "css-floating-buttons"
category_name: "CSS Floating Buttons"
description: "Glass done with physics in mind rather than a blur slider."
has_js: "false"
---

Here's a working CSS Floating Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Floating Action Button with Backdrop Blur
Source: https://codefronts.com/components/css-floating-buttons/glassmorphism-fab/

Glass done with physics in mind rather than a blur slider. Three ingredients make a translucent control read as glass: saturate() alongside the blur so colours behind stay alive, an asymmetric rim (bright top edge, dark bottom edge) that implies a thickness, and a shadow that sits closer to the surface than a solid button's would. Shown over a photograph, because glass over a flat colour proves nothing.
## HTML
```html
<section class="fb-17" aria-label="Glassmorphism floating action button demo">
  <div class="fb-17__photo" aria-hidden="true"></div>
  <div class="fb-17__stage">
    <p class="fb-17__eyebrow">blur · saturate · asymmetric rim</p>
    <h2 class="fb-17__title">Glass, not frosted plastic</h2>
    <p class="fb-17__sub">Saturation keeps the colour behind alive; a lit top edge and a shaded base imply thickness. Both are one line each and both are usually missing.</p>
    <div class="fb-17__row">
      <button class="fb-17__fab" type="button" aria-label="Add, clear glass">
        <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 5v14M5 12h14" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg>
      </button>
      <button class="fb-17__fab fb-17__fab--smoke" type="button" aria-label="Play, smoked glass">
        <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M8 5.5l11 6.5-11 6.5z" fill="currentColor"/></svg>
      </button>
      <button class="fb-17__fab fb-17__fab--pill" type="button">
        <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 3l2.2 5.8L20 11l-5.8 2.2L12 19l-2.2-5.8L4 11l5.8-2.2z" fill="currentColor"/></svg>
        <span>Enhance</span>
      </button>
    </div>
    <p class="fb-17__chip">saturate(190%) · inset rim ±1px · tinted for contrast</p>
  </div>
</section>
```
## CSS
```css
.fb-17 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: oklch(0.2 0.04 250);
  --fb-17-tint: oklch(1 0 0);
  --fb-17-ink: oklch(0.99 0.005 250);
  --fb-17-mut: oklch(0.9 0.01 250/.85);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--fb-17-ink);
  position: relative;
  display: grid;
  place-items: center;
  padding: clamp(20px,5vw,56px);
  isolation: isolate;
  overflow: hidden;
}

.fb-17 *,
.fb-17 *::before,
.fb-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fb-17__photo {
  position: absolute;
  inset: 0;
  z-index: -1;
  background: linear-gradient(140deg,oklch(0.55 0.19 25),oklch(0.35 0.16 285) 55%,oklch(0.42 0.14 200)),url("https://images.unsplash.com/photo-1502680390469-be75c86b636f?q=80&w=1600&auto=format&fit=crop") center/cover no-repeat;
  background-blend-mode: soft-light,normal;
  animation: fb-17-drift 34s ease-in-out infinite alternate;
}

@keyframes fb-17-drift {
  to {
    background-position: center,60% 40%;
    background-size: auto,112%;
  }
}

.fb-17__stage {
  width: min(100%,58ch);
  display: grid;
  gap: clamp(18px,3vw,28px);
  justify-items: center;
  text-align: center;
  text-shadow: 0 1px 14px oklch(0.15 0.04 250/.55);
}

.fb-17__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: oklch(0.94 0.07 90);
}

.fb-17__title {
  font-size: clamp(26px,4.8vw,46px);
  line-height: 1.04;
  letter-spacing: -.035em;
  font-weight: 700;
  text-wrap: balance;
}

.fb-17__sub {
  max-width: 50ch;
  font-size: clamp(13.5px,1.7vw,16.5px);
  line-height: 1.62;
  color: var(--fb-17-mut);
  text-wrap: pretty;
}

.fb-17__row {
  display: flex;
  flex-wrap: wrap;
  gap: clamp(14px,3vw,24px);
  justify-content: center;
  align-items: center;
}

.fb-17__fab {
  position: relative;
  isolation: isolate;
  display: grid;
  place-items: center;
  inline-size: 70px;
  block-size: 70px;
  border: 1px solid color-mix(in oklch,var(--fb-17-tint) 32%,transparent);
  border-radius: 24px;
  cursor: pointer;
  color: var(--fb-17-ink);
  background: color-mix(in oklch,var(--fb-17-tint) 15%,transparent);
  -webkit-backdrop-filter: blur(18px) saturate(190%) brightness(1.06);
  backdrop-filter: blur(18px) saturate(190%) brightness(1.06);
  box-shadow: inset 0 1px 0 oklch(1 0 0/.5),inset 0 -1px 0 oklch(0 0 0/.16),0 10px 26px -10px oklch(0.1 0.03 250/.6);
  transition: transform .3s cubic-bezier(.2,1.25,.4,1),background .3s ease,box-shadow .3s ease;
}

.fb-17__fab svg {
  width: 27px;
  height: 27px;
  filter: drop-shadow(0 1px 2px oklch(0.15 0.04 250/.6));
  position: relative;
  z-index: 2;
}

.fb-17__fab::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
  background: linear-gradient(145deg,oklch(1 0 0/.24),transparent 46%);
  z-index: 1;
  pointer-events: none;
}

.fb-17__fab:hover {
  transform: translateY(-3px);
  background: color-mix(in oklch,var(--fb-17-tint) 24%,transparent);
  box-shadow: inset 0 1px 0 oklch(1 0 0/.6),inset 0 -1px 0 oklch(0 0 0/.16),0 18px 38px -12px oklch(0.1 0.03 250/.7);
}

.fb-17__fab:active {
  transform: scale(.94);
}

.fb-17__fab:focus-visible {
  outline: 3px solid oklch(0.99 0.005 250);
  outline-offset: 4px;
}

.fb-17__fab--smoke {
  background: color-mix(in oklch,oklch(0.15 0.03 250) 34%,transparent);
  border-color: oklch(1 0 0/.22);
}

.fb-17__fab--smoke:hover {
  background: color-mix(in oklch,oklch(0.15 0.03 250) 46%,transparent);
}

.fb-17__fab--pill {
  inline-size: auto;
  block-size: 62px;
  border-radius: 99px;
  padding-inline: 24px;
  grid-auto-flow: column;
  gap: 11px;
  font-size: 15.5px;
  font-weight: 620;
  font-family: inherit;
  letter-spacing: -.01em;
}

.fb-17__fab--pill svg {
  width: 22px;
  height: 22px;
}

.fb-17__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--fb-17-mut);
  padding: 8px 14px;
  border: 1px solid oklch(1 0 0/.24);
  border-radius: 99px;
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
}

@media (prefers-reduced-motion: reduce) {
  .fb-17__photo {
    animation: none;
  }

  .fb-17__fab {
    transition: none;
  }
}
```
