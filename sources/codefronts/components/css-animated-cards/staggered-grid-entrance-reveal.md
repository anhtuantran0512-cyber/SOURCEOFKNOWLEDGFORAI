---
source: "codefronts"
url: "https://codefronts.com/components/css-animated-cards/staggered-grid-entrance-reveal/"
title: "Staggered Grid Entrance Reveal"
section: "components"
category: "css-animated-cards"
category_name: "CSS Animated Cards"
description: "The cascade every editorial and product grid opens with — cards fading and lifting into place 90 ms apart so the page reads as choreographed rather than dumped."
has_js: "false"
---

Here's a working CSS Animated Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Staggered Grid Entrance Reveal
Source: https://codefronts.com/components/css-animated-cards/staggered-grid-entrance-reveal/

The cascade every editorial and product grid opens with — cards fading and lifting into place 90 ms apart so the page reads as choreographed rather than dumped. Built with a single keyframe and one custom property for the index, plus a pure-CSS replay switch that restarts the whole cascade by swapping the animation name — no JavaScript anywhere. Includes the 2026 one-liner (sibling-index()) alongside the universal nth-child fallback.
## HTML
```html
<section class="ac-01" aria-label="Staggered grid entrance reveal demo">
  <div class="ac-01__stage">
    <header class="ac-01__head">
      <p class="ac-01__eyebrow">Entrance choreography</p>
      <h2 class="ac-01__title">Six cards, one keyframe, ninety milliseconds apart</h2>
      <input class="ac-01__check" type="checkbox" id="ac-01-replay">
      <label class="ac-01__btn" for="ac-01-replay">
        <svg viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M3 12a9 9 0 1 0 3-6.7"/><path d="M3 4v5h5"/></svg>
        Replay cascade
      </label>
    </header>
    <ul class="ac-01__grid" role="list">
      <li class="ac-01__card"><a class="ac-01__link" href="#ac-01-replay">
        <span class="ac-01__media"><img src="https://images.unsplash.com/photo-1441974231531-c6227db76b6e?q=80&w=600&auto=format&fit=crop" alt="Sunlight through a dense forest canopy" loading="lazy" decoding="async" width="600" height="400"></span>
        <span class="ac-01__kicker">Field notes</span>
        <span class="ac-01__name">Designing for the fold that no longer exists</span>
      </a></li>
      <li class="ac-01__card"><a class="ac-01__link" href="#ac-01-replay">
        <span class="ac-01__media"><img src="https://images.unsplash.com/photo-1498050108023-c5249f4df085?q=80&w=600&auto=format&fit=crop" alt="Code editor open on a laptop screen" loading="lazy" decoding="async" width="600" height="400"></span>
        <span class="ac-01__kicker">Engineering</span>
        <span class="ac-01__name">Nine CSS features that replaced a library</span>
      </a></li>
      <li class="ac-01__card"><a class="ac-01__link" href="#ac-01-replay">
        <span class="ac-01__media"><img src="https://images.unsplash.com/photo-1483058712412-4245e9b90334?q=80&w=600&auto=format&fit=crop" alt="Tidy desk with notebook and laptop" loading="lazy" decoding="async" width="600" height="400"></span>
        <span class="ac-01__kicker">Process</span>
        <span class="ac-01__name">A design system audit in one afternoon</span>
      </a></li>
      <li class="ac-01__card"><a class="ac-01__link" href="#ac-01-replay">
        <span class="ac-01__media"><img src="https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?q=80&w=600&auto=format&fit=crop" alt="Abstract blue data streams" loading="lazy" decoding="async" width="600" height="400"></span>
        <span class="ac-01__kicker">Performance</span>
        <span class="ac-01__name">Why your grid janks on the second paint</span>
      </a></li>
      <li class="ac-01__card"><a class="ac-01__link" href="#ac-01-replay">
        <span class="ac-01__media"><img src="https://images.unsplash.com/photo-1493246507139-91e8fad9978e?q=80&w=600&auto=format&fit=crop" alt="Mountain range under soft morning light" loading="lazy" decoding="async" width="600" height="400"></span>
        <span class="ac-01__kicker">Craft</span>
        <span class="ac-01__name">Easing curves, ranked by how they feel</span>
      </a></li>
      <li class="ac-01__card"><a class="ac-01__link" href="#ac-01-replay">
        <span class="ac-01__media"><img src="https://images.unsplash.com/photo-1519389950473-47ba0277781c?q=80&w=600&auto=format&fit=crop" alt="Team collaborating around a table of laptops" loading="lazy" decoding="async" width="600" height="400"></span>
        <span class="ac-01__kicker">Teams</span>
        <span class="ac-01__name">Shipping motion without a motion designer</span>
      </a></li>
    </ul>
    <p class="ac-01__chip" aria-hidden="true">--i custom property · calc() animation-delay · animation-fill-mode:both · sibling-index() progressive enhancement</p>
  </div>
</section>
```
## CSS
```css
.ac-01,
.ac-01 *,
.ac-01 *::before,
.ac-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ac-01 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --ac-01-bg: oklch(0.16 0.018 265);
  --ac-01-card: oklch(0.21 0.021 265);
  --ac-01-ink: oklch(0.97 0.004 260);
  --ac-01-mut: oklch(0.70 0.02 265);
  --ac-01-acc: oklch(0.80 0.16 82);
  --ac-01-line: oklch(1 0 0/.11);
  background: var(--ac-01-bg);
  color: var(--ac-01-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.ac-01__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(18px,3vw,30px);
  padding: clamp(22px,5vw,64px);
  background: radial-gradient(120% 80% at 50% -10%,color-mix(in oklch,var(--ac-01-acc) 13%,transparent),transparent 62%);
}

.ac-01__head {
  display: grid;
  justify-items: center;
  gap: 12px;
  text-align: center;
  max-width: 56ch;
}

.ac-01__eyebrow {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--ac-01-acc);
}

.ac-01__title {
  font-size: clamp(23px,3.4vw,38px);
  font-weight: 650;
  line-height: 1.12;
  letter-spacing: -.03em;
  text-wrap: balance;
}

.ac-01__check {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.ac-01__btn {
  display: inline-flex;
  align-items: center;
  gap: 9px;
  min-height: 44px;
  padding: 0 20px;
  margin-top: 4px;
  border: 1px solid var(--ac-01-line);
  border-radius: 99px;
  background: oklch(1 0 0/.04);
  color: var(--ac-01-ink);
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: background .2s,border-color .2s,transform .2s;
}

.ac-01__btn:hover {
  background: oklch(1 0 0/.09);
  border-color: color-mix(in oklch,var(--ac-01-acc) 45%,transparent);
  transform: translateY(-1px);
}

.ac-01__check:focus-visible+.ac-01__btn {
  outline: 2px solid var(--ac-01-acc);
  outline-offset: 3px;
}

.ac-01__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(230px,1fr));
  gap: clamp(14px,1.8vw,20px);
  width: min(100%,1060px);
  list-style: none;
}

.ac-01__link {
  display: grid;
  gap: 10px;
  height: 100%;
  padding: 12px 12px 18px;
  border: 1px solid var(--ac-01-line);
  border-radius: 18px;
  background: var(--ac-01-card);
  color: inherit;
  text-decoration: none;
  transition: transform .35s cubic-bezier(.16,1,.3,1),border-color .35s,background .35s;
}

.ac-01__link:hover,
.ac-01__link:focus-visible {
  transform: translateY(-4px);
  border-color: color-mix(in oklch,var(--ac-01-acc) 40%,transparent);
  background: color-mix(in oklch,var(--ac-01-card) 88%,var(--ac-01-acc));
}

.ac-01__link:focus-visible {
  outline: 2px solid var(--ac-01-acc);
  outline-offset: 3px;
}

.ac-01__media {
  display: block;
  aspect-ratio: 16/10;
  border-radius: 11px;
  overflow: hidden;
  background: linear-gradient(135deg,oklch(0.34 0.06 265),oklch(0.26 0.04 300));
}

.ac-01__media img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: scale .5s cubic-bezier(.16,1,.3,1);
}

.ac-01__link:hover .ac-01__media img {
  scale: 1.05;
}

.ac-01__kicker {
  padding-inline: 4px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--ac-01-acc);
}

.ac-01__name {
  padding-inline: 4px;
  font-size: 15.5px;
  font-weight: 600;
  line-height: 1.32;
  letter-spacing: -.015em;
  text-wrap: pretty;
}

.ac-01__card {
  --ac-01-i: 0;
  --ac-01-kf: ac-01-rise-a;
  animation: var(--ac-01-kf) .9s cubic-bezier(.16,1,.3,1) both;
  animation-delay: calc(var(--ac-01-i) * 90ms);
}

.ac-01__card:nth-child(2) {
  --ac-01-i: 1;
}

.ac-01__card:nth-child(3) {
  --ac-01-i: 2;
}

.ac-01__card:nth-child(4) {
  --ac-01-i: 3;
}

.ac-01__card:nth-child(5) {
  --ac-01-i: 4;
}

.ac-01__card:nth-child(6) {
  --ac-01-i: 5;
}

@supports (animation-delay: calc(sibling-index() * 1ms)) {
  .ac-01__card {
    animation-delay: calc((sibling-index() - 1) * 90ms);
  }
}

.ac-01__stage:has(.ac-01__check:checked) .ac-01__card {
  --ac-01-kf: ac-01-rise-b;
}

@keyframes ac-01-rise-a {
  from {
    opacity: 0;
    transform: translateY(18px) scale(.97);
    filter: blur(6px);
  }

  to {
    opacity: 1;
    transform: none;
    filter: blur(0);
  }
}

@keyframes ac-01-rise-b {
  from {
    opacity: 0;
    transform: translateY(18px) scale(.97);
    filter: blur(6px);
  }

  to {
    opacity: 1;
    transform: none;
    filter: blur(0);
  }
}

.ac-01__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  line-height: 1.6;
  color: var(--ac-01-mut);
  padding: 8px 15px;
  border: 1px solid var(--ac-01-line);
  border-radius: 99px;
  text-align: center;
  max-width: min(100%,660px);
}

@media (prefers-reduced-motion: reduce) {
  .ac-01__card {
    animation: none;
  }

  .ac-01__link,
    .ac-01__media img {
    transition: none;
  }
}
```
