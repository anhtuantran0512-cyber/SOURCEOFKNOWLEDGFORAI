---
source: "codefronts"
url: "https://codefronts.com/components/css-testimonials-reviews/brutalist-press/"
title: "Neo-Brutalist Review Card"
section: "components"
category: "css-testimonials-reviews"
category_name: "CSS Testimonials & Reviews"
description: "Neo-brutalism, done with restraint: 3 px ink borders, hard unblurred offset shadows, vivid flat fills and a press interaction where the card physically moves…"
has_js: "false"
---

Here's a working CSS Testimonials & Review from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neo-Brutalist Review Card
Source: https://codefronts.com/components/css-testimonials-reviews/brutalist-press/

Neo-brutalism, done with restraint: 3 px ink borders, hard unblurred offset shadows, vivid flat fills and a press interaction where the card physically moves into its own shadow. The whole aesthetic is four properties — the craft is in the interaction timing and in keeping the type legible against saturated backgrounds.
## HTML
```html
<section class="tr-12" aria-label="Neo-brutalist review card demo">
  <div class="tr-12__stage">
    <header class="tr-12__head">
      <h2 class="tr-12__title">REAL PEOPLE.<br>REAL LOUD.</h2>
      <span class="tr-12__sticker" aria-hidden="true">4.9★ avg</span>
    </header>

    <div class="tr-12__grid">
      <figure class="tr-12__card" style="--tr-12-h:95" tabindex="0">
        <div class="tr-12__rate"><span aria-hidden="true">★★★★★</span><b>5.0</b></div>
        <blockquote>Shipped our whole store in a weekend. Support answered on a Sunday. A SUNDAY.</blockquote>
        <figcaption>
          <img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?q=80&w=140&h=140&fit=crop&auto=format" alt="Portrait of Callum Doyle" width="44" height="44" loading="lazy" decoding="async">
          <span><b>Callum Doyle</b>Founder, Meridian Goods</span>
        </figcaption>
        <span class="tr-12__tag">E-COMMERCE</span>
      </figure>

      <figure class="tr-12__card" style="--tr-12-h:200" tabindex="0">
        <div class="tr-12__rate"><span aria-hidden="true">★★★★★</span><b>5.0</b></div>
        <blockquote>I have used six of these. This is the only one my co-founder stopped complaining about.</blockquote>
        <figcaption>
          <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?q=80&w=140&h=140&fit=crop&auto=format" alt="Portrait of Nia Osei" width="44" height="44" loading="lazy" decoding="async">
          <span><b>Nia Osei</b>CPO, Fieldwork</span>
        </figcaption>
        <span class="tr-12__tag">INDIE SAAS</span>
      </figure>

      <figure class="tr-12__card" style="--tr-12-h:320" tabindex="0">
        <div class="tr-12__rate"><span aria-hidden="true">★★★★<i>★</i></span><b>4.0</b></div>
        <blockquote>Docs could be shorter. Product could not be better. Net: I renewed for two years.</blockquote>
        <figcaption>
          <img src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?q=80&w=140&h=140&fit=crop&auto=format" alt="Portrait of Dan Reyes" width="44" height="44" loading="lazy" decoding="async">
          <span><b>Dan Reyes</b>CTO, Portside</span>
        </figcaption>
        <span class="tr-12__tag">INFRA</span>
      </figure>

      <figure class="tr-12__card" style="--tr-12-h:45" tabindex="0">
        <div class="tr-12__rate"><span aria-hidden="true">★★★★★</span><b>5.0</b></div>
        <blockquote>Cancelled three tools. Kept the budget. Told everyone. Here I am telling you.</blockquote>
        <figcaption>
          <img src="https://images.unsplash.com/photo-1517841905240-472988babdf9?q=80&w=140&h=140&fit=crop&auto=format" alt="Portrait of Grace Whitlock" width="44" height="44" loading="lazy" decoding="async">
          <span><b>Grace Whitlock</b>Design Lead, Auryn</span>
        </figcaption>
        <span class="tr-12__tag">DESIGN OPS</span>
      </figure>
    </div>
    <p class="tr-12__chip" aria-hidden="true">3px borders · box-shadow 6px 6px 0 · :active press-to-flush · per-card oklch hue token</p>
  </div>
</section>
```
## CSS
```css
.tr-12,
.tr-12 *,
.tr-12 *::before,
.tr-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tr-12 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --tr-12-bg: oklch(0.93 0.05 100);
  --tr-12-ink: oklch(0.16 0.02 60);
  --tr-12-mut: oklch(0.36 0.02 60);
  background: var(--tr-12-bg);
  color: var(--tr-12-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
  background-image: radial-gradient(oklch(0.16 0.02 60/.14) 1px,transparent 1px);
  background-size: 16px 16px;
}

.tr-12__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(20px,3vw,30px);
  padding: clamp(22px,5vw,56px);
}

.tr-12__head {
  position: relative;
  display: grid;
  justify-items: center;
  gap: 8px;
}

.tr-12__title {
  font-size: clamp(30px,6vw,60px);
  font-weight: 900;
  line-height: .96;
  letter-spacing: -.045em;
  text-align: center;
  text-transform: uppercase;
  -webkit-text-stroke: 0;
  text-shadow: 4px 4px 0 oklch(0.85 0.19 55);
}

.tr-12__sticker {
  display: inline-block;
  padding: 8px 16px;
  border: 3px solid var(--tr-12-ink);
  border-radius: 10px;
  background: oklch(0.86 0.19 145);
  font-size: 14px;
  font-weight: 800;
  rotate: -4deg;
  box-shadow: 4px 4px 0 var(--tr-12-ink);
}

.tr-12__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(min(100%,258px),1fr));
  gap: clamp(18px,2.4vw,26px);
  width: min(100%,1060px);
}

.tr-12__card {
  position: relative;
  display: grid;
  align-content: start;
  gap: 14px;
  padding: 22px 20px 24px;
  border: 3px solid var(--tr-12-ink);
  border-radius: 14px;
  background: oklch(0.9 0.14 var(--tr-12-h,95));
  box-shadow: 6px 6px 0 var(--tr-12-ink);
  transition: translate .16s ease,box-shadow .16s ease;
  cursor: pointer;
  animation: tr-12-drop .55s cubic-bezier(.16,1,.3,1) both;
}

.tr-12__card:nth-child(2) {
  animation-delay: .07s;
}

.tr-12__card:nth-child(3) {
  animation-delay: .14s;
}

.tr-12__card:nth-child(4) {
  animation-delay: .21s;
}

@keyframes tr-12-drop {
  from {
    opacity: 0;
    translate: 0 -14px;
    rotate: -1.5deg;
  }

  to {
    opacity: 1;
    translate: 0 0;
    rotate: 0deg;
  }
}

.tr-12__card:hover {
  translate: -2px -2px;
  box-shadow: 9px 9px 0 var(--tr-12-ink);
}

.tr-12__card:active {
  translate: 6px 6px;
  box-shadow: 0 0 0 var(--tr-12-ink);
}

.tr-12__card:focus-visible {
  outline: 3px solid var(--tr-12-ink);
  outline-offset: 5px;
}

.tr-12__rate {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 16px;
  letter-spacing: 1px;
  color: var(--tr-12-ink);
}

.tr-12__rate i {
  opacity: .24;
  font-style: normal;
}

.tr-12__rate b {
  font-size: 13px;
  font-weight: 800;
  padding: 2px 8px;
  border: 2px solid var(--tr-12-ink);
  border-radius: 6px;
  background: oklch(1 0 0/.55);
  font-variant-numeric: tabular-nums;
}

.tr-12__card blockquote {
  font-size: 16.5px;
  line-height: 1.42;
  font-weight: 620;
  letter-spacing: -.02em;
  text-wrap: pretty;
  color: oklch(0.2 0.02 60);
}

.tr-12__card figcaption {
  display: flex;
  align-items: center;
  gap: 11px;
  padding-top: 14px;
  border-top: 3px solid var(--tr-12-ink);
}

.tr-12__card figcaption img {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  object-fit: cover;
  flex: none;
  border: 3px solid var(--tr-12-ink);
  background: oklch(0.95 0.04 60);
}

.tr-12__card figcaption span {
  display: grid;
  font-size: 11.5px;
  line-height: 1.35;
  color: var(--tr-12-mut);
  font-weight: 600;
}

.tr-12__card figcaption b {
  font-size: 14px;
  font-weight: 800;
  color: var(--tr-12-ink);
  letter-spacing: -.015em;
}

.tr-12__tag {
  position: absolute;
  inset-block-start: -12px;
  inset-inline-end: 14px;
  padding: 4px 10px;
  border: 2.5px solid var(--tr-12-ink);
  border-radius: 8px;
  background: oklch(0.16 0.02 60);
  color: oklch(0.97 0.02 100);
  font-size: 10.5px;
  font-weight: 800;
  letter-spacing: .08em;
  rotate: 2.5deg;
}

.tr-12__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--tr-12-ink);
  padding: 9px 15px;
  border: 2.5px solid var(--tr-12-ink);
  border-radius: 10px;
  background: oklch(1 0 0/.6);
  text-align: center;
  font-weight: 600;
}

@media (prefers-reduced-motion: reduce) {
  .tr-12__card {
    animation: none;
    transition: none;
  }
}
```
