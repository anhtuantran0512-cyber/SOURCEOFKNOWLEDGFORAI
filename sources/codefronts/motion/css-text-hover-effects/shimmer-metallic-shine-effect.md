---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-hover-effects/shimmer-metallic-shine-effect/"
title: "Shimmer / Metallic Shine Effect"
section: "motion"
category: "css-text-hover-effects"
category_name: "CSS Text Hover Effects"
description: "Gold you can grade: a members-card wordmark set in a five-stop metallic gradient (shadow gold → base → near-white highlight band → base → shadow) clipped…"
has_js: "false"
---

Here's a working CSS Text Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Shimmer / Metallic Shine Effect
Source: https://codefronts.com/motion/css-text-hover-effects/shimmer-metallic-shine-effect/

Gold you can grade: a members-card wordmark set in a five-stop metallic gradient (shadow gold → base → near-white highlight band → base → shadow) clipped into the glyphs, with the light sweep done by sliding background-position across a 250%-wide canvas on hover — the gradient never changes, the LIGHT moves. The eyebrow line runs a slow 6s ambient shimmer so the card glints even untouched, the way foil does under ceiling light; the big mark saves its full sweep for your cursor.
## HTML
```html
<section class="cth-08" aria-label="Metallic shimmer text demo">
  <div class="cth-08__stage">
    <a class="cth-08__card" href="#cth08-top" id="cth08-top">
      <p class="cth-08__eyebrow"><span class="cth-08__gold cth-08__gold--ambient">Est. MMXXVI &middot; by invitation</span></p>
      <h1 class="cth-08__mark"><span class="cth-08__gold cth-08__gold--sweep">AURUM<br>RESERVE</span></h1>
      <div class="cth-08__foot">
        <span class="cth-08__tier">Founding member &mdash; No. 047</span>
        <span class="cth-08__price"><b class="cth-08__gold cth-08__gold--sweep">$890</b><small>/year</small></span>
      </div>
      <p class="cth-08__hint">Hover the card: the gradient never changes &mdash; <code>background-position</code> slides the glint band through the glyphs.</p>
    </a>
  </div>
</section>
```
## CSS
```css
.cth-08,
.cth-08 *,
.cth-08 *::before,
.cth-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cth-08 {
  --bg: oklch(0.15 0.008 70);
  --card: oklch(0.19 0.01 75);
  --line: oklch(0.34 0.03 85);
  --mut: oklch(0.62 0.03 80);
  --gold-1: oklch(0.88 0.09 92);
  --gold-2: oklch(0.72 0.11 85);
  --gold-3: oklch(0.5 0.09 78);
  font-family: Georgia,'Times New Roman',serif;
  color: oklch(0.9 0.02 85);
}

.cth-08__stage {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  background: radial-gradient(100% 80% at 50% 0%,oklch(0.19 0.012 75),var(--bg) 70%);
  padding: clamp(20px,4vw,56px);
  container: cth08/inline-size;
}

.cth-08__card {
  display: flex;
  flex-direction: column;
  gap: clamp(18px,3.4cqi,30px);
  width: min(100%,560px);
  padding: clamp(26px,5cqi,46px);
  background: linear-gradient(160deg,var(--card),oklch(0.16 0.009 72));
  border: 1px solid var(--line);
  border-radius: 20px;
  text-decoration: none;
  color: inherit;
  box-shadow: 0 30px 80px oklch(0.05 0.01 70/.6),inset 0 1px 0 oklch(1 0 0/.06);
  transition: border-color .5s ease,translate .5s cubic-bezier(.22,1,.36,1);
}

.cth-08__card:hover,
.cth-08__card:focus-visible {
  border-color: color-mix(in oklch,var(--gold-2) 55%,var(--line));
  translate: 0 -4px;
}

.cth-08__card:focus-visible {
  outline: 2px solid var(--gold-1);
  outline-offset: 4px;
}

.cth-08__gold {
  background-image: linear-gradient(105deg,var(--gold-3) 0%,var(--gold-2) 34%,oklch(0.97 0.05 95) 49%,var(--gold-2) 64%,var(--gold-3) 100%);
  background-size: 250% 100%;
  background-position: 97% 0;
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.cth-08__gold--sweep {
  transition: background-position 1.1s cubic-bezier(.25,.66,.15,1);
}

.cth-08__card:hover .cth-08__gold--sweep,
.cth-08__card:focus-visible .cth-08__gold--sweep {
  background-position: 3% 0;
}

.cth-08__gold--ambient {
  animation: cth08-glint 6s ease-in-out infinite;
}

@keyframes cth08-glint {
  0%,
    100% {
    background-position: 97% 0;
  }

  50% {
    background-position: 3% 0;
  }
}

.cth-08__eyebrow {
  font-size: 12.5px;
  letter-spacing: .3em;
  text-transform: uppercase;
}

.cth-08__mark {
  font-size: clamp(44px,9.4cqi,84px);
  font-weight: 700;
  letter-spacing: .045em;
  line-height: 1.04;
  filter: drop-shadow(0 3px 10px oklch(0.05 0.01 70/.7));
}

.cth-08__foot {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 14px;
  border-top: 1px solid var(--line);
  padding-top: clamp(14px,2.6cqi,20px);
}

.cth-08__tier {
  font-size: 12.5px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--mut);
}

.cth-08__price {
  display: flex;
  align-items: baseline;
  gap: 5px;
}

.cth-08__price b {
  font-size: clamp(24px,4cqi,32px);
  font-weight: 700;
}

.cth-08__price small {
  font-size: 12px;
  color: var(--mut);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.cth-08__hint {
  font-size: 12px;
  line-height: 1.7;
  color: var(--mut);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.cth-08__hint code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .92em;
  background: oklch(0.26 0.015 75);
  padding: 1px 6px;
  border-radius: 4px;
  color: var(--gold-1);
}

@media (prefers-reduced-motion: reduce) {
  .cth-08 * {
    animation: none !important;
    transition-duration: .01ms !important;
  }
}
```
