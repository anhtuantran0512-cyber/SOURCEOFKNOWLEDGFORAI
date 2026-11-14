---
source: "codefronts"
url: "https://codefronts.com/layouts/css-aspect-ratio/css-aspect-ratio-ad-banner-container/"
title: "CSS Aspect Ratio Ad Banner Container"
section: "layouts"
category: "css-aspect-ratio"
category_name: "CSS Aspect Ratio Demos"
description: "Publisher-grade ad slots that reserve their exact space before a single ad byte arrives: aspect-ratio: 728/90 for the leaderboard, 300/250 for the rectangle,…"
has_js: "false"
---

Here's a working CSS Aspect Ratio Demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Aspect Ratio Ad Banner Container
Source: https://codefronts.com/layouts/css-aspect-ratio/css-aspect-ratio-ad-banner-container/

Publisher-grade ad slots that reserve their exact space before a single ad byte arrives: aspect-ratio: 728/90 for the leaderboard, 300/250 for the rectangle, 300/600 for the half-page — the raw IAB dimensions written straight into CSS, no decimal maths. Each slot shimmers as a labeled placeholder, the 'ad' arrives on a CSS delay to prove the page doesn't flinch, and a container query swaps the leaderboard for a 320/50 mobile banner when the column gets narrow. Ads pay the bills; this is how they stop costing you CLS.
## HTML
```html
<section class="car-10" aria-label="Ad banner container demo">
  <div class="car-10__stage" id="car10-top">
    <header class="car-10__bar">
      <a class="car-10__brand" href="#car10-top">The Morning Brief</a>
      <nav class="car-10__nav" aria-label="Sections"><a href="#car10-top">Media</a><a href="#car10-top">Adtech</a><a href="#car10-top">Metrics</a></nav>
      <a class="car-10__sub" href="#car10-top">Subscribe</a>
    </header>
    <div class="car-10__slotzone">
      <p class="car-10__adlabel">Advertisement · leaderboard 728×90 (320×50 when narrow)</p>
      <div class="car-10__slot car-10__slot--leader">
        <a class="car-10__ad car-10__ad--leader" href="#car10-top" aria-label="House ad: Fjell boots">
          <b>FJELL</b><span>Boots that outlast the trail. Guaranteed for a decade.</span><em>Shop now →</em>
        </a>
      </div>
    </div>
    <main class="car-10__main">
      <article class="car-10__article">
        <p class="car-10__kicker">Adtech · CLS</p>
        <h1>The cheapest ranking win in publishing is an empty box</h1>
        <p class="car-10__meta">By Harriet Cole · August 3, 2026</p>
        <p>Every slot on this page was full-size before the auction returned. The leaderboard above, the rectangle below, the half-page in the sidebar — each is an <code>aspect-ratio</code> reservation wearing a skeleton, which is why the paragraph you are reading has not moved since first paint.</p>
        <p>Watch the creatives arrive (they're on a deliberate 1.4–2.2s delay). The boxes don't grow, the article doesn't lurch, and the CLS report stays at zero — the exact failure mode that used to cost publishers a Core Web Vitals grade every time a bid resolved late.</p>
        <div class="car-10__slotzone car-10__slotzone--inline">
          <p class="car-10__adlabel">Advertisement · medium rectangle 300×250</p>
          <div class="car-10__slot car-10__slot--mrec">
            <a class="car-10__ad car-10__ad--mrec" href="#car10-top" aria-label="House ad: Mono focus app" style="--img:url('https://images.unsplash.com/photo-1553062407-98eeb64c6a62?q=80&w=600&h=500&auto=format&fit=crop')">
              <i aria-hidden="true"></i><b>Mono</b><span>One task at a time. The focus app for deadline weeks.</span><em>Try free →</em>
            </a>
          </div>
        </div>
        <p>The trick bears repeating because it's so unglamorous: write the IAB size into the ratio — <code>aspect-ratio: 728/90</code>, <code>300/250</code>, <code>300/600</code> — cap it with <code>max-width</code>, and let the box scale proportionally in narrow columns. When the column can't honor a leaderboard at all, a container query swaps the slot for the 320×50 mobile unit. The column is the breakpoint, not the screen.</p>
        <p>Unfilled inventory keeps the box too. A reserved slot that stays a quiet skeleton costs a few hundred square pixels; a collapsing slot costs a layout shift on every page where the auction passes. Publishers who measured both stopped collapsing years ago.</p>
      </article>
      <aside class="car-10__side" aria-label="Sidebar">
        <p class="car-10__adlabel">Advertisement · half page 300×600</p>
        <div class="car-10__slot car-10__slot--half">
          <a class="car-10__ad car-10__ad--half" href="#car10-top" aria-label="House ad: Meridian data">
            <b>Meridian&nbsp;Data</b><span>Your dashboards, minus the 40 tabs. Warehouse-native analytics for newsrooms.</span><i aria-hidden="true"></i><em>Book a demo →</em>
          </a>
        </div>
        <div class="car-10__widget">
          <h2>Most read</h2>
          <ol><li><a href="#car10-top">Ratio maths for ad ops: the one-page cheat sheet</a></li><li><a href="#car10-top">Why the 320×50 still rules mobile</a></li><li><a href="#car10-top">Skeletons that convert better than spinners</a></li></ol>
        </div>
      </aside>
    </main>
    <footer class="car-10__foot">Slots reserve with <code>aspect-ratio</code> + <code>max-width</code>; creatives arrive whenever they like. A demo from the CodeFronts aspect-ratio collection.</footer>
  </div>
</section>
```
## CSS
```css
.car-10,
.car-10 *,
.car-10 *::before,
.car-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.car-10 {
  --bg: oklch(0.97 0.004 250);
  --ink: oklch(0.22 0.015 260);
  --mut: oklch(0.5 0.012 260);
  --line: oklch(0.89 0.008 255);
  --acc: oklch(0.55 0.17 255);
  --skeleton: oklch(0.93 0.006 255);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
  display: block;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: var(--bg);
}

.car-10__stage {
  width: 100%;
  container: car10/inline-size;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  background: var(--bg);
}

.car-10__bar {
  display: flex;
  align-items: center;
  gap: 18px;
  padding: 14px clamp(16px,4cqi,44px);
  border-bottom: 1px solid var(--line);
  background: oklch(1 0 0);
}

.car-10__brand {
  font-size: 17px;
  font-weight: 800;
  letter-spacing: -.02em;
  color: inherit;
  text-decoration: none;
}

.car-10__nav {
  display: flex;
  gap: 2px;
  margin-inline: auto;
}

.car-10__nav a {
  display: grid;
  place-items: center;
  min-height: 44px;
  padding: 0 12px;
  border-radius: 9px;
  font-size: 13px;
  font-weight: 600;
  color: var(--mut);
  text-decoration: none;
  transition: color .2s,background .2s;
}

.car-10__nav a:hover,
.car-10__nav a:focus-visible {
  color: var(--ink);
  background: oklch(0.94 0.006 255);
}

.car-10__nav a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
}

.car-10__sub {
  display: grid;
  place-items: center;
  min-height: 40px;
  padding: 0 16px;
  border-radius: 99px;
  background: var(--ink);
  color: oklch(0.98 0 0);
  font-size: 12.5px;
  font-weight: 700;
  text-decoration: none;
  transition: background .2s;
}

.car-10__sub:hover,
.car-10__sub:focus-visible {
  background: var(--acc);
}

.car-10__sub:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.car-10__slotzone {
  padding: 16px clamp(16px,4cqi,44px) 4px;
  text-align: center;
}

.car-10__slotzone--inline {
  padding: 18px 0 6px;
}

.car-10__adlabel {
  font-size: 9.5px;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: oklch(0.62 0.01 260);
  margin-bottom: 6px;
}

.car-10__slot {
  position: relative;
  margin-inline: auto;
  border: 1px dashed oklch(0.82 0.01 255);
  border-radius: 8px;
  overflow: hidden;
  background: linear-gradient(110deg,var(--skeleton) 30%,oklch(0.96 0.004 255) 45%,var(--skeleton) 60%) 0 0/200% 100%;
  animation: car10-shimmer 1.6s linear infinite;
}

@keyframes car10-shimmer {
  to {
    background-position: -200% 0;
  }
}

.car-10__slot--leader {
  aspect-ratio: 728/90;
  max-width: 728px;
}

.car-10__slot--mrec {
  aspect-ratio: 300/250;
  max-width: 300px;
}

.car-10__slot--half {
  aspect-ratio: 300/600;
  max-width: 300px;
}

.car-10__ad {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 12px 18px;
  text-decoration: none;
  color: oklch(0.98 0 0);
  opacity: 0;
  animation: car10-arrive .5s ease 1.4s both;
}

@keyframes car10-arrive {
  from {
    opacity: 0;
  }

  to {
    opacity: 1;
  }
}

.car-10__ad--leader {
  background: linear-gradient(100deg,oklch(0.35 0.08 150),oklch(0.5 0.11 130));
  justify-content: center;
  text-align: left;
}

.car-10__ad--leader b {
  font-size: clamp(14px,2.4cqi,19px);
  letter-spacing: .22em;
}

.car-10__ad--leader span {
  font-size: clamp(10px,1.8cqi,13px);
  opacity: .92;
  max-width: 46ch;
}

.car-10__ad--leader em {
  font-style: normal;
  font-size: clamp(10px,1.7cqi,12.5px);
  font-weight: 700;
  padding: 7px 12px;
  border-radius: 99px;
  background: oklch(0.98 0 0/.16);
  border: 1px solid oklch(0.98 0 0/.4);
  white-space: nowrap;
}

.car-10__ad--mrec {
  flex-direction: column;
  justify-content: flex-end;
  align-items: flex-start;
  gap: 4px;
  padding: 14px;
  background: oklch(0.3 0.05 280);
  animation-delay: 2s;
}

.car-10__ad--mrec i {
  position: absolute;
  inset: 0;
  background: linear-gradient(oklch(0.2 0.04 280/.15),oklch(0.14 0.04 280/.85)),var(--img);
  background-size: cover;
  background-position: center;
  z-index: -1;
  margin: 0;
}

.car-10__ad--mrec b {
  font-size: 17px;
  letter-spacing: -.01em;
}

.car-10__ad--mrec span {
  font-size: 11.5px;
  line-height: 1.45;
  opacity: .92;
}

.car-10__ad--mrec em {
  font-style: normal;
  font-size: 11.5px;
  font-weight: 700;
  margin-top: 6px;
  padding: 8px 12px;
  border-radius: 8px;
  background: oklch(0.98 0 0);
  color: oklch(0.3 0.05 280);
}

.car-10__ad--half {
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
  gap: 8px;
  padding: 22px;
  background: linear-gradient(170deg,oklch(0.28 0.06 255),oklch(0.42 0.12 285));
  animation-delay: 2.2s;
}

.car-10__ad--half b {
  font-size: 19px;
  letter-spacing: -.01em;
}

.car-10__ad--half span {
  font-size: 12.5px;
  line-height: 1.55;
  opacity: .92;
}

.car-10__ad--half i {
  width: 100%;
  aspect-ratio: 1;
  border-radius: 12px;
  margin: 8px 0;
  background: radial-gradient(60% 60% at 35% 30%,oklch(0.85 0.1 285/.5),transparent 70%),conic-gradient(from 200deg,oklch(0.5 0.14 285),oklch(0.65 0.16 255),oklch(0.5 0.14 285));
  border: 1px solid oklch(0.98 0 0/.25);
}

.car-10__ad--half em {
  font-style: normal;
  font-size: 12px;
  font-weight: 700;
  padding: 9px 14px;
  border-radius: 9px;
  background: oklch(0.98 0 0);
  color: oklch(0.32 0.08 270);
}

.car-10__ad:hover em,
.car-10__ad:focus-visible em {
  translate: 2px 0;
}

.car-10__ad em {
  transition: translate .2s;
}

.car-10__ad:focus-visible {
  outline: 3px solid var(--acc);
  outline-offset: -3px;
}

.car-10__main {
  display: grid;
  grid-template-columns: minmax(0,1fr) 332px;
  gap: clamp(20px,3.5cqi,40px);
  max-width: 1120px;
  margin-inline: auto;
  padding: clamp(18px,3cqi,32px) clamp(16px,4cqi,44px);
  align-items: start;
}

.car-10__kicker {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: var(--acc);
}

.car-10__article h1 {
  font-size: clamp(24px,3.6cqi,36px);
  line-height: 1.12;
  letter-spacing: -.025em;
  font-weight: 800;
  margin-top: 8px;
  text-wrap: balance;
}

.car-10__meta {
  font-size: 12.5px;
  color: var(--mut);
  margin: 8px 0 4px;
}

.car-10__article > p {
  font-size: 15px;
  line-height: 1.7;
  margin-top: 16px;
  max-width: 66ch;
}

.car-10__article code,
.car-10__foot code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .88em;
  background: oklch(0.92 0.008 255);
  padding: 2px 6px;
  border-radius: 5px;
  color: oklch(0.42 0.12 255);
}

.car-10__side {
  display: flex;
  flex-direction: column;
  gap: 18px;
  text-align: center;
}

.car-10__widget {
  text-align: left;
  border: 1px solid var(--line);
  border-radius: 14px;
  padding: 16px;
  background: oklch(1 0 0);
}

.car-10__widget h2 {
  font-size: 12px;
  font-weight: 800;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--mut);
  margin-bottom: 10px;
}

.car-10__widget ol {
  list-style: none;
  counter-reset: mr;
}

.car-10__widget li {
  counter-increment: mr;
  display: flex;
  gap: 10px;
  padding: 9px 0;
  border-top: 1px solid var(--line);
}

.car-10__widget li::before {
  content: counter(mr,decimal-leading-zero);
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  font-weight: 700;
  color: var(--acc);
  padding-top: 2px;
}

.car-10__widget a {
  font-size: 13px;
  font-weight: 600;
  line-height: 1.4;
  color: inherit;
  text-decoration: none;
}

.car-10__widget a:hover,
.car-10__widget a:focus-visible {
  color: var(--acc);
  text-decoration: underline;
  text-underline-offset: 3px;
}

.car-10__widget a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
  border-radius: 2px;
}

.car-10__foot {
  max-width: 1120px;
  margin-inline: auto;
  padding: 16px clamp(16px,4cqi,44px) 32px;
  border-top: 1px solid var(--line);
  font-size: 12.5px;
  line-height: 1.7;
  color: var(--mut);
}

@container car10 (width < 560px) {
  .car-10__slot--leader {
    aspect-ratio: 320/50;
    max-width: 320px;
  }

  .car-10__ad--leader span {
    display: none;
  }
}

@container car10 (width < 880px) {
  .car-10__main {
    grid-template-columns: 1fr;
  }

  .car-10__nav {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .car-10__slot {
    animation: none;
  }

  .car-10__ad {
    animation-duration: .01ms;
    animation-delay: .5s;
  }

  .car-10 * {
    transition-duration: .01ms !important;
  }
}
```
