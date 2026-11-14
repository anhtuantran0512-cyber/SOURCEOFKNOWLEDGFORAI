---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-gradient-ui/neon-dark-mode-glow-card/"
title: "Neon / Dark Mode Glow Card"
section: "design-styles"
category: "css-gradient-ui"
category_name: "CSS Gradient UI"
description: "Three arcade-grade neon cards on true black — cyan, magenta and lime — each glowing through a blurred gradient twin behind the card, with hover surging the…"
has_js: "false"
---

Here's a working CSS Gradient UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neon / Dark Mode Glow Card
Source: https://codefronts.com/design-styles/css-gradient-ui/neon-dark-mode-glow-card/

Three arcade-grade neon cards on true black — cyan, magenta and lime — each glowing through a blurred gradient twin behind the card, with hover surging the glow and a flickering "OPEN" sign easter egg. Built for dark-mode product pages and gaming UIs.
## HTML
```html
<div class="cgu-11-group">
<section class="cgu-11" aria-label="Neon dark mode glow card demos">
  <div class="cgu-11__inner">
    <header class="cgu-11__head">
      <p class="cgu-11__eyebrow">11 · Neon glow</p>
      <h2 class="cgu-11__title">The glow is the gradient</h2>
      <p class="cgu-11__sub">Each halo is the card's own background, duplicated and blurred behind it — retint the card and the light follows. Hover to surge.</p>
      <span class="cgu-11__sign" aria-hidden="true">OPEN</span>
    </header>
    <div class="cgu-11__grid">
      <article class="cgu-11__card" style="--n1:#22d3ee;--n2:#0ea5e9">
        <p class="cgu-11__tier">Arcade</p>
        <p class="cgu-11__price">$0<span>/mo</span></p>
        <ul class="cgu-11__list"><li>3 projects</li><li>Community themes</li><li>CRT scanline pack</li></ul>
        <button class="cgu-11__btn" type="button">Insert coin</button>
      </article>
      <article class="cgu-11__card is-featured" style="--n1:#e879f9;--n2:#a855f7">
        <p class="cgu-11__tier">High score</p>
        <p class="cgu-11__price">$16<span>/mo</span></p>
        <ul class="cgu-11__list"><li>Unlimited projects</li><li>Neon token editor</li><li>Priority render queue</li><li>1v1 support duels</li></ul>
        <button class="cgu-11__btn" type="button">Go pro</button>
      </article>
      <article class="cgu-11__card" style="--n1:#a3e635;--n2:#34d399">
        <p class="cgu-11__tier">Guild</p>
        <p class="cgu-11__price">$49<span>/mo</span></p>
        <ul class="cgu-11__list"><li>Team leaderboards</li><li>SSO + audit log</li><li>Custom cabinets</li></ul>
        <button class="cgu-11__btn" type="button">Assemble team</button>
      </article>
    </div>
    <p class="cgu-11__foot">Face stays near-black; only the border and halo carry color — that's what reads as neon.</p>
  </div>
</section>
</div>
```
## CSS
```css
.cgu-11-group {
  display: block;
  width: 100%;
}

.cgu-11,
.cgu-11 *,
.cgu-11 *::before,
.cgu-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cgu-11 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 64px 24px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: #f0fdff;
  background: radial-gradient(80% 60% at 50% 0%,#0a0f18 0%,#030407 60%);
}

.cgu-11__inner {
  width: min(1040px,100%);
  display: grid;
  gap: 40px;
}

.cgu-11__head {
  position: relative;
  text-align: center;
  display: grid;
  gap: 13px;
  justify-items: center;
}

.cgu-11__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .28em;
  text-transform: uppercase;
  color: #67e8f9;
}

.cgu-11__title {
  font-size: clamp(28px,4.4vw,50px);
  font-weight: 850;
  letter-spacing: -.02em;
  line-height: 1.06;
  text-wrap: balance;
}

.cgu-11__sub {
  max-width: 56ch;
  font-size: 15.5px;
  line-height: 1.6;
  color: #93a3b8;
  text-wrap: pretty;
}

.cgu-11__sign {
  position: absolute;
  top: -6px;
  right: max(0px,calc(50% - 420px));
  font-family: ui-monospace,Menlo,monospace;
  font-size: 13px;
  font-weight: 800;
  letter-spacing: .34em;
  color: #fecdd3;
  padding: 8px 16px 8px 20px;
  border: 2px solid #fb7185;
  border-radius: 12px;
  text-shadow: 0 0 8px #fb7185,0 0 22px #f43f5e;
  box-shadow: 0 0 14px -2px #fb7185,inset 0 0 12px -6px #fb7185;
  animation: cgu11-flicker 4.2s linear infinite;
  transform: rotate(4deg);
}

.cgu-11__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(250px,1fr));
  gap: 26px;
  align-items: stretch;
}

.cgu-11__card {
  --n1: #22d3ee;
  --n2: #0ea5e9;
  position: relative;
  isolation: isolate;
  display: grid;
  gap: 14px;
  align-content: start;
  padding: 30px 28px;
  border-radius: 20px;
  background: linear-gradient(170deg,#0b0f16,#05070c);
  transition: transform .35s cubic-bezier(.2,.9,.3,1.2);
}

.cgu-11__card::before {
  content: "";
  position: absolute;
  inset: -2px;
  border-radius: inherit;
  background: linear-gradient(140deg,var(--n1),var(--n2));
  filter: blur(24px);
  opacity: .28;
  z-index: -2;
  transition: opacity .35s,filter .35s;
}

.cgu-11__card::after {
  content: "";
  position: absolute;
  inset: 0;
  padding: 1.5px;
  border-radius: inherit;
  background: linear-gradient(140deg,var(--n1),var(--n2));
  -webkit-mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  z-index: -1;
}

.cgu-11__card:hover,
.cgu-11__card:focus-within {
  transform: translateY(-6px);
}

.cgu-11__card:hover::before,
.cgu-11__card:focus-within::before {
  opacity: .6;
  filter: blur(32px);
}

.cgu-11__card.is-featured::before {
  opacity: .42;
}

.cgu-11__tier {
  font-size: 12px;
  font-weight: 800;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: color-mix(in oklab,var(--n1) 75%,white);
}

.cgu-11__price {
  font-size: 44px;
  font-weight: 850;
  letter-spacing: -.03em;
}

.cgu-11__price span {
  font-size: 15px;
  font-weight: 600;
  color: #93a3b8;
  letter-spacing: 0;
}

.cgu-11__list {
  list-style: none;
  display: grid;
  gap: 9px;
}

.cgu-11__list li {
  position: relative;
  padding-left: 22px;
  font-size: 14px;
  color: #c3cede;
}

.cgu-11__list li::before {
  content: "▸";
  position: absolute;
  left: 0;
  color: var(--n1);
}

.cgu-11__btn {
  margin-top: 10px;
  font: inherit;
  font-size: 14.5px;
  font-weight: 750;
  color: #02060b;
  padding: 13px;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  background: linear-gradient(140deg,var(--n1),var(--n2));
  box-shadow: 0 10px 26px -12px var(--n1);
  transition: box-shadow .3s,transform .2s;
}

.cgu-11__btn:hover,
.cgu-11__btn:focus-visible {
  box-shadow: 0 14px 34px -12px var(--n1);
  transform: translateY(-1px);
}

.cgu-11__btn:focus-visible {
  outline: 3px solid color-mix(in oklab,var(--n1) 70%,white);
  outline-offset: 3px;
}

.cgu-11__foot {
  text-align: center;
  font-size: 13px;
  color: #64748b;
}

@keyframes cgu11-flicker {
  0%,
    7%,
    9%,
    100% {
    opacity: 1;
  }

  8% {
    opacity: .4;
  }

  42%,
    44% {
    opacity: 1;
  }

  43% {
    opacity: .55;
  }

  80% {
    opacity: 1;
  }

  81% {
    opacity: .7;
  }

  82% {
    opacity: 1;
  }
}

@media (max-width: 560px) {
  .cgu-11__sign {
    position: static;
    transform: rotate(0);
    justify-self: center;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cgu-11__sign {
    animation: none;
  }

  .cgu-11__card {
    transition: none;
  }

  .cgu-11__card:hover {
    transform: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — each halo is the card's gradient duplicated on a blurred ::before (background uses the same --n1/--n2 pair), border via mask-composite. */
```
