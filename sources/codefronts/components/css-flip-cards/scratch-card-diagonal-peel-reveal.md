---
source: "codefronts"
url: "https://codefronts.com/components/css-flip-cards/scratch-card-diagonal-peel-reveal/"
title: "Scratch Card Diagonal Peel Reveal"
section: "components"
category: "css-flip-cards"
category_name: "CSS Flip Cards"
description: "A reward scratch card where the surface wipes away diagonally from top-left to bottom-right via an animated clip-path polygon — no rotateY, no rotateX, no 3D…"
has_js: "false"
---

Here's a working CSS Flip Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Scratch Card Diagonal Peel Reveal
Source: https://codefronts.com/components/css-flip-cards/scratch-card-diagonal-peel-reveal/

A reward scratch card where the surface wipes away diagonally from top-left to bottom-right via an animated clip-path polygon — no rotateY, no rotateX, no 3D transforms at all.
## HTML
```html
<div class="fc-23">
  <div class="fc-23__scene">

    <!-- Stars that appear after reveal -->
    <div class="fc-23__star"></div>
    <div class="fc-23__star"></div>
    <div class="fc-23__star"></div>
    <div class="fc-23__star"></div>
    <div class="fc-23__star"></div>
    <div class="fc-23__star"></div>

    <!-- BOTTOM — prize layer (always present, revealed by clip-path wiping top) -->
    <div class="fc-23__prize">
      <div class="fc-23__prize-icon">🏆</div>
      <div class="fc-23__prize-label">You Won!</div>
      <div class="fc-23__prize-amount">$250</div>
      <div class="fc-23__prize-sub">Store Credit · Valid 30 days</div>
      <button class="fc-23__prize-cta">Claim Reward →</button>
    </div>

    <!-- TOP — scratch surface (clip-path wipes this away on hover) -->
    <div class="fc-23__scratch">
      <div class="fc-23__scratch-bg"></div>
      <div class="fc-23__scratch-content">
        <div class="fc-23__scratch-logo">
          <span class="fc-23__logo-dot"></span>
          NovaPay Rewards
        </div>
        <div class="fc-23__scratch-title">Instant Win<br>Scratch Card</div>
        <div class="fc-23__scratch-sub">Hover to reveal your prize</div>
        <div class="fc-23__scratch-area">
          <span class="fc-23__scratch-icon">🪙</span>
          <span class="fc-23__scratch-cta-text">Scratch to reveal</span>
        </div>
      </div>
    </div>

    <div class="fc-23__reveal-label">Hover to peel →</div>
  </div>
</div>
```
## CSS
```css
.fc-23,
.fc-23 *,
.fc-23 *::before,
.fc-23 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fc-23 ::selection {
  background: #8b5cf6;
  color: #fff;
}

.fc-23 {
  --bg: #06040e;
  --violet: #8b5cf6;
  --purple: #a855f7;
  --gold: #f59e0b;
  --green: #22c55e;
  --white: #faf5ff;
  --card-w: 380px;
  --card-h: 240px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: radial-gradient(ellipse at 50% 40%,#100820,#06040e 65%);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  gap: 28px;
  color: var(--white);
}
/* ══════════════════════════════════════════
   SCRATCH / PEEL MECHANISM
   No rotateY or rotateX at all.

   The card has two layers stacked with position:absolute.
   The TOP layer (scratch surface) uses:
     clip-path: polygon(...)
   which starts as a full rectangle covering the card.
   On hover, the clip-path animates to a zero-width diagonal
   slice that vanishes from bottom-right to top-left —
   revealing the prize layer underneath.

   The peel curl is simulated by a ::before pseudo on the
   top layer that shows a curling shadow/gradient on the
   leading edge of the shrinking clip region.

   This is 100% clip-path + CSS custom property animation.
   Zero transform-style, zero backface-visibility, zero rotateY.
══════════════════════════════════════════ */

.fc-23__scene {
  width: var(--card-w);
  height: var(--card-h);
  position: relative;
  border-radius: 18px;
  overflow: hidden;
  cursor: pointer;
  box-shadow: 0 0 50px rgba(139,92,246,.12);
}
/* ── BOTTOM layer — the prize/reward ── */

.fc-23__prize {
  position: absolute;
  inset: 0;
  /* isolation:isolate creates a new stacking context so the z-index:1
       on prize-icon/amount/cta children stays confined to this layer.
       Without it those children would promote into the scene's stacking
       context and render ABOVE the scratch surface, defeating the whole
       "scratch reveals the prize underneath" mechanic. */
  isolation: isolate;
  background: linear-gradient(135deg,#0d0a20,#1a0d3a,#0a1a1a);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 12px;
  padding: 28px;
  border: 1px solid rgba(139,92,246,.3);
  border-radius: 18px;
}

.fc-23__prize::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 18px;
  background: radial-gradient(ellipse at 50% 50%,rgba(245,158,11,.08),transparent 70%);
  pointer-events: none;
}

.fc-23__prize-icon {
  width: 72px;
  height: 72px;
  border-radius: 50%;
  background: linear-gradient(135deg,rgba(245,158,11,.2),rgba(245,158,11,.05));
  border: 2px solid rgba(245,158,11,.4);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 32px;
  box-shadow: 0 0 30px rgba(245,158,11,.2);
  position: relative;
  z-index: 1;
}

.fc-23__prize-label {
  font-size: 11px;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: rgba(250,245,255,.4);
  font-weight: 700;
  position: relative;
  z-index: 1;
}

.fc-23__prize-amount {
  font-size: 42px;
  font-weight: 900;
  line-height: 1;
  background: linear-gradient(135deg,var(--gold),#fde68a,var(--gold));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  text-shadow: none;
  position: relative;
  z-index: 1;
}

.fc-23__prize-sub {
  font-size: 12px;
  color: rgba(250,245,255,.45);
  position: relative;
  z-index: 1;
}

.fc-23__prize-cta {
  margin-top: 4px;
  padding: 10px 28px;
  border-radius: 20px;
  border: none;
  cursor: pointer;
  background: linear-gradient(135deg,var(--gold),#d97706);
  color: #000;
  font-size: 13px;
  font-weight: 800;
  letter-spacing: .04em;
  position: relative;
  z-index: 1;
  transition: transform .15s;
}

.fc-23__prize-cta:hover {
  filter: brightness(1.08);
  box-shadow: 0 6px 18px rgba(245,158,11,.4);
}
/* ── TOP layer — the scratch surface ── */

.fc-23__scratch {
  position: absolute;
  inset: 0;
  border-radius: 18px;
  /*
      clip-path polygon at rest = full card rectangle:
        top-left(0% 0%) → top-right(100% 0%) → bottom-right(100% 100%) → bottom-left(0% 100%)
  
      On hover it animates to a collapsed diagonal line then zero:
        all four points converge to top-left corner
    */
  clip-path: polygon(0% 0%, 100% 0%, 100% 100%, 0% 100%);
  transition: clip-path .9s cubic-bezier(.4,0,.2,1);
  overflow: hidden;
}

.fc-23__scene:hover .fc-23__scratch {
  /* Wipe from bottom-right to top-left — all corners collapse to top-left */
  clip-path: polygon(0% 0%, 0% 0%, 0% 0%, 0% 0%);
}
/* Scratch surface texture */

.fc-23__scratch-bg {
  position: absolute;
  inset: 0;
  background: /* sparkle noise */ radial-gradient(circle at 20% 30%,rgba(139,92,246,.15) 0%,transparent 40%), radial-gradient(circle at 80% 70%,rgba(168,85,247,.12) 0%,transparent 40%), linear-gradient(135deg,#1a0d38,#250f4a,#12082a);
  border: 1px solid rgba(139,92,246,.3);
  border-radius: 18px;
}
/* Crosshatch scratch marks */

.fc-23__scratch-bg::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image: repeating-linear-gradient(
        45deg,
        rgba(255,255,255,.025) 0px,
        rgba(255,255,255,.025) 1px,
        transparent 1px,
        transparent 8px
      ), repeating-linear-gradient(
        -45deg,
        rgba(255,255,255,.015) 0px,
        rgba(255,255,255,.015) 1px,
        transparent 1px,
        transparent 8px
      );
  border-radius: 18px;
}
/* Content on the scratch layer */

.fc-23__scratch-content {
  position: relative;
  z-index: 1;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 12px;
  padding: 28px;
}

.fc-23__scratch-logo {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 15px;
  font-weight: 800;
  letter-spacing: .06em;
  color: rgba(250,245,255,.9);
}

.fc-23__logo-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--violet);
}

.fc-23__scratch-title {
  font-size: 22px;
  font-weight: 900;
  color: var(--white);
  text-align: center;
  line-height: 1.2;
}

.fc-23__scratch-sub {
  font-size: 12px;
  color: rgba(250,245,255,.45);
  text-align: center;
}

.fc-23__scratch-area {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 20px;
  border-radius: 12px;
  background: rgba(255,255,255,.06);
  border: 1px solid rgba(255,255,255,.1);
}

.fc-23__scratch-icon {
  font-size: 16px;
  animation: fc-23-wiggle 1.5s ease-in-out infinite;
}

@keyframes fc-23-wiggle {
  0%,
    100% {
    transform: rotate(-8deg);
  }

  50% {
    transform: rotate(8deg);
  }
}

.fc-23__scratch-cta-text {
  font-size: 12px;
  color: rgba(250,245,255,.6);
  font-weight: 600;
}
/* ── The peel curl edge — ::after on the scratch layer ──
   This is a narrow gradient strip that sits at the clip-path boundary,
   simulating the curling shadow of a peeling sticker.
   We animate its position in sync with the clip-path using the same timing.
*/

.fc-23__scratch::after {
  content: '';
  position: absolute;
  /* diagonal strip from bottom-right corner going to top-left */
  top: -20%;
  left: -20%;
  width: 60%;
  height: 60%;
  background: linear-gradient(
      135deg,
      transparent 40%,
      rgba(0,0,0,.35) 50%,
      rgba(139,92,246,.2) 55%,
      transparent 65%
    );
  transform: rotate(0deg);
  transition: transform .9s cubic-bezier(.4,0,.2,1),opacity .9s;
  pointer-events: none;
  border-radius: 0;
}

.fc-23__scene:hover .fc-23__scratch::after {
  transform: translate(-60%,-60%);
  opacity: 0;
}
/* Stars burst on the prize layer (pure CSS, no JS) */

.fc-23__star {
  position: absolute;
  width: 4px;
  height: 4px;
  border-radius: 50%;
  background: var(--gold);
  opacity: 0;
  transition: opacity .3s .8s;
}

.fc-23__scene:hover .fc-23__star {
  opacity: 1;
}

.fc-23__star:nth-child(1) {
  top: 15%;
  left: 12%;
  width: 6px;
  height: 6px;
  transition-delay: .8s;
}

.fc-23__star:nth-child(2) {
  top: 22%;
  right: 15%;
  width: 4px;
  height: 4px;
  transition-delay: .9s;
}

.fc-23__star:nth-child(3) {
  bottom: 20%;
  left: 18%;
  width: 5px;
  height: 5px;
  transition-delay: 1s;
}

.fc-23__star:nth-child(4) {
  bottom: 18%;
  right: 12%;
  width: 6px;
  height: 6px;
  transition-delay: .85s;
}

.fc-23__star:nth-child(5) {
  top: 50%;
  left: 8%;
  width: 3px;
  height: 3px;
  transition-delay: 1.1s;
}

.fc-23__star:nth-child(6) {
  top: 45%;
  right: 9%;
  width: 4px;
  height: 4px;
  transition-delay: .95s;
}
/* Reveal label */

.fc-23__reveal-label {
  position: absolute;
  bottom: 10px;
  right: 14px;
  font-size: 9px;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: rgba(250,245,255,.2);
  transition: opacity .3s .8s;
  pointer-events: none;
}

.fc-23__scene:hover .fc-23__reveal-label {
  opacity: 0;
}

@media (max-width: 440px) {
  .fc-23 {
    --card-w: 320px;
    --card-h: 210px;
  }

  .fc-23__prize-amount {
    font-size: 34px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .fc-23__scratch {
    transition: none;
  }

  .fc-23__scratch::after {
    transition: none;
  }

  .fc-23__scratch-icon {
    animation: none;
  }

  .fc-23__star {
    transition: none;
  }
}
```
