---
source: "codefronts"
url: "https://codefronts.com/layouts/css-portfolio-layouts/bento-grid-portfolio-layout-html-css/"
title: "Bento Grid Portfolio Layout HTML CSS"
section: "layouts"
category: "css-portfolio-layouts"
category_name: "CSS Portfolio Layouts"
description: "The Apple-keynote bento: a 6-column grid where every tile buys the exact real estate its content deserves — a 4×2 statement tile, a 2×2 profile, single-row…"
has_js: "false"
---

Here's a working CSS Portfolio Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Bento Grid Portfolio Layout HTML CSS
Source: https://codefronts.com/layouts/css-portfolio-layouts/bento-grid-portfolio-layout-html-css/

The Apple-keynote bento: a 6-column grid where every tile buys the exact real estate its content deserves — a 4×2 statement tile, a 2×2 profile, single-row stat chips, twin project covers — all placed with nothing but grid-column/row spans. A sheen sweeps across tiles on hover, the availability dot pulses, and a container query re-deals the whole board into two columns when space runs out.
## HTML
```html
<section class="cpl-02" aria-label="Bento grid portfolio layout demo">
  <div class="cpl-02__stage">
    <div class="cpl-02__board">
      <article class="cpl-02__tile cpl-02__t-hero cpl-02__dark">
        <p class="cpl-02__kicker">Jules Aldana — Product Designer</p>
        <h2>Designing calm interfaces for loud problems.</h2>
        <a class="cpl-02__cta" href="#contact">Start a project<span aria-hidden="true">→</span></a>
      </article>
      <article class="cpl-02__tile cpl-02__t-face" aria-label="Portrait">
        <span class="cpl-02__face" role="img" aria-label="Portrait of Jules Aldana" style="--img:url('https://images.unsplash.com/photo-1494790108377-be9c29b29330?q=80&w=900&auto=format&fit=crop')"></span>
      </article>
      <article class="cpl-02__tile cpl-02__t-stat"><strong>48</strong><span>projects shipped</span></article>
      <article class="cpl-02__tile cpl-02__t-stat"><strong>9<i>yrs</i></strong><span>in product teams</span></article>
      <article class="cpl-02__tile cpl-02__t-stat cpl-02__avail"><strong><em aria-hidden="true"></em>Open</strong><span>for Q4 2026</span></article>
      <a class="cpl-02__tile cpl-02__t-work" href="#atlas" style="--img:url('https://images.unsplash.com/photo-1498050108023-c5249f4df085?q=80&w=900&auto=format&fit=crop');--a:oklch(0.75 0.13 300);--b:oklch(0.45 0.17 270)">
        <span class="cpl-02__chip">Fintech</span><h3>Atlas Wealth App</h3>
      </a>
      <a class="cpl-02__tile cpl-02__t-work" href="#ferra" style="--img:url('https://images.unsplash.com/photo-1523275335684-37898b6baf30?q=80&w=900&auto=format&fit=crop');--a:oklch(0.83 0.11 60);--b:oklch(0.55 0.16 30)">
        <span class="cpl-02__chip">E-commerce</span><h3>Ferra Storefront</h3>
      </a>
      <article class="cpl-02__tile cpl-02__t-strip">
        <span>Trusted by</span>
        <b>Linear</b><b>Vercel</b><b>Arc</b><b>Raycast</b>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
.cpl-02,
.cpl-02 *,
.cpl-02 *::before,
.cpl-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cpl-02 {
  --bg: oklch(0.96 0.005 90);
  --card: oklch(1 0 0);
  --ink: oklch(0.23 0.02 270);
  --mut: oklch(0.54 0.015 270);
  --line: oklch(0.89 0.008 270);
  --dark: oklch(0.2 0.03 280);
  --acc: oklch(0.72 0.17 55);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
}

.cpl-02__stage {
  width: 100%;
  container: cpl02/inline-size;
  background: var(--bg);
  padding: clamp(14px,3cqi,22px);
  min-height: 100vh;
  min-height: 100svh;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.cpl-02__board {
  display: grid;
  gap: 12px;
  grid-template-columns: repeat(6,1fr);
  grid-auto-rows: clamp(92px,11vh,132px);
}

.cpl-02__tile {
  position: relative;
  overflow: hidden;
  border-radius: 18px;
  background: var(--card);
  border: 1px solid var(--line);
  padding: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 6px;
  text-decoration: none;
  color: inherit;
  transition: translate .25s cubic-bezier(.2,.7,.2,1),box-shadow .25s;
}

.cpl-02__tile::after {
  content: "";
  position: absolute;
  inset: -40% auto;
  left: 0;
  width: 45%;
  background: linear-gradient(105deg,transparent,oklch(1 0 0/.14),transparent);
  transform: translateX(-150%) rotate(8deg);
  transition: transform .7s cubic-bezier(.4,0,.2,1);
  pointer-events: none;
}

.cpl-02__tile:hover {
  translate: 0 -3px;
  box-shadow: 0 16px 30px -18px oklch(0.3 0.04 280/.5);
}

.cpl-02__tile:hover::after {
  transform: translateX(280%) rotate(8deg);
}

a.cpl-02__tile:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.cpl-02__t-hero {
  grid-column: span 4;
  grid-row: span 2;
  justify-content: space-between;
  padding: 24px;
}

.cpl-02__dark {
  background: radial-gradient(120% 130% at 15% 0%,oklch(0.3 0.06 290/.9),transparent 55%),var(--dark);
  border-color: oklch(0.32 0.04 285);
  color: oklch(0.96 0.008 90);
}

.cpl-02__kicker {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: oklch(0.75 0.1 55);
}

.cpl-02__t-hero h2 {
  font-size: clamp(20px,3.4cqi,30px);
  line-height: 1.12;
  letter-spacing: -.025em;
  font-weight: 700;
  max-width: 14em;
  text-wrap: balance;
}

.cpl-02__cta {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  align-self: start;
  min-height: 40px;
  padding: 0 16px;
  border-radius: 99px;
  font-size: 13px;
  font-weight: 700;
  text-decoration: none;
  color: var(--dark);
  background: var(--acc);
  transition: gap .25s,background .25s;
}

.cpl-02__cta:hover,
.cpl-02__cta:focus-visible {
  gap: 13px;
  background: oklch(0.78 0.17 55);
}

.cpl-02__cta:focus-visible {
  outline: 2px solid oklch(0.96 0.008 90);
  outline-offset: 2px;
}

.cpl-02__t-face {
  grid-column: span 2;
  grid-row: span 2;
  padding: 0;
}

.cpl-02__face {
  position: absolute;
  inset: 0;
  background-image: var(--img,none),linear-gradient(160deg,oklch(0.88 0.04 90),oklch(0.7 0.09 60));
  background-size: cover;
  background-position: center;
}

.cpl-02__t-stat {
  grid-column: span 2;
}

.cpl-02__t-stat strong {
  font-size: 26px;
  letter-spacing: -.02em;
  font-variant-numeric: tabular-nums;
  display: flex;
  align-items: baseline;
  gap: 6px;
}

.cpl-02__t-stat strong i {
  font-size: 13px;
  font-style: normal;
  color: var(--mut);
}

.cpl-02__t-stat span {
  font-size: 12px;
  color: var(--mut);
}

.cpl-02__avail strong {
  font-size: 16px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.cpl-02__avail em {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: oklch(0.72 0.19 150);
  animation: cpl02-pulse 2s infinite;
}

@keyframes cpl02-pulse {
  0% {
    box-shadow: 0 0 0 0 oklch(0.72 0.19 150/.5);
  }

  70% {
    box-shadow: 0 0 0 9px oklch(0.72 0.19 150/0);
  }

  100% {
    box-shadow: 0 0 0 0 oklch(0.72 0.19 150/0);
  }
}

.cpl-02__t-work {
  grid-column: span 3;
  grid-row: span 2;
  justify-content: flex-end;
  background-image: var(--img,none),linear-gradient(150deg,var(--a),var(--b));
  background-size: cover;
  background-position: center;
  border: none;
  color: oklch(0.98 0.005 90);
}

.cpl-02__t-work h3 {
  font-size: 19px;
  letter-spacing: -.015em;
}

.cpl-02__chip {
  align-self: start;
  padding: 4px 10px;
  border-radius: 99px;
  font-size: 11px;
  font-weight: 700;
  background: oklch(1 0 0/.2);
  backdrop-filter: blur(4px);
  margin-bottom: auto;
}

.cpl-02__t-strip {
  grid-column: span 6;
  flex-direction: row;
  align-items: center;
  gap: 22px;
  padding: 0 24px;
}

.cpl-02__t-strip span {
  font-size: 11.5px;
  font-weight: 600;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--mut);
}

.cpl-02__t-strip b {
  font-size: 14.5px;
  letter-spacing: -.01em;
  opacity: .75;
}

@container cpl02 (width < 560px) {
  .cpl-02__board {
    grid-template-columns: repeat(2,1fr);
    grid-auto-rows: 88px;
  }

  .cpl-02__t-hero {
    grid-column: span 2;
    grid-row: span 2;
  }

  .cpl-02__t-face {
    grid-column: span 1;
    grid-row: span 1;
  }

  .cpl-02__t-stat {
    grid-column: span 1;
  }

  .cpl-02__t-work {
    grid-column: span 2;
  }

  .cpl-02__t-strip {
    grid-column: span 2;
    flex-wrap: wrap;
    gap: 12px;
    padding: 14px 18px;
  }
}

.cpl-02__t-work::before {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(to top,oklch(0.2 0.03 280/.72),transparent 55%);
}

.cpl-02__t-work .cpl-02__chip,
.cpl-02__t-work h3 {
  position: relative;
  z-index: 1;
}

@media (prefers-reduced-motion: reduce) {
  .cpl-02 *,
    .cpl-02 *::after {
    transition-duration: .01ms !important;
    animation: none !important;
  }
}
```
