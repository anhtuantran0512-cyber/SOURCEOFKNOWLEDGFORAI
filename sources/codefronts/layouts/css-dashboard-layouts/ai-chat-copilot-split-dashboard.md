---
source: "codefronts"
url: "https://codefronts.com/layouts/css-dashboard-layouts/ai-chat-copilot-split-dashboard/"
title: "AI Chat / Copilot Split Dashboard"
section: "layouts"
category: "css-dashboard-layouts"
category_name: "CSS Dashboard Layouts"
description: "The 2026 SaaS signature: your data on the left, a resident AI copilot docked on the right."
has_js: "true"
---

Here's a working CSS Dashboard Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: AI Chat / Copilot Split Dashboard
Source: https://codefronts.com/layouts/css-dashboard-layouts/ai-chat-copilot-split-dashboard/

The 2026 SaaS signature: your data on the left, a resident AI copilot docked on the right. The panel collapses by animating grid-template-columns itself — 1fr 340px tweens to 1fr 0px and the dashboard reflows in the same motion, no transform hacks. Inside: message bubbles, streaming typing dots, suggestion chips, a conic-gradient avatar with a slow shimmer. Four lines of JS toggle the disclosure button; CSS owns everything that moves.
## HTML
```html
<section class="cdl-13" aria-label="AI copilot split dashboard demo">
  <div class="cdl-13__split">
    <div class="cdl-13__main">
      <header class="cdl-13__bar">
        <strong><span class="cdl-13__logo" aria-hidden="true"></span>Margin — Q3 board</strong>
        <button class="cdl-13__ask" type="button" aria-expanded="true" aria-controls="cdl13-panel"><i class="cdl-13__spark" aria-hidden="true"></i>Copilot</button>
      </header>
      <div class="cdl-13__cards">
        <article><h3>Gross margin</h3><p>61.4%</p><small class="cdl-13__up">▲ 2.1 pts QoQ</small></article>
        <article><h3>Burn multiple</h3><p>1.3×</p><small class="cdl-13__up">improving</small></article>
        <article><h3>Net revenue retention</h3><p>117%</p><small>flat QoQ</small></article>
        <article class="cdl-13__wide"><h3>Revenue vs. cost</h3><div class="cdl-13__chart" aria-hidden="true"><i style="--a:46%;--b:30%"></i><i style="--a:52%;--b:33%"></i><i style="--a:49%;--b:35%"></i><i style="--a:61%;--b:36%"></i><i style="--a:66%;--b:38%"></i><i style="--a:74%;--b:39%"></i><i style="--a:82%;--b:41%"></i><i style="--a:90%;--b:42%"></i></div></article>
      </div>
    </div>
    <aside class="cdl-13__copilot" id="cdl13-panel" aria-label="AI copilot">
      <div class="cdl-13__inner">
        <header class="cdl-13__phead"><span class="cdl-13__avatar" aria-hidden="true"></span><div><b>Copilot</b><small>grounded in this board</small></div><button class="cdl-13__close" type="button" aria-label="Close copilot">✕</button></header>
        <div class="cdl-13__thread">
          <p class="cdl-13__q">Why did gross margin jump this quarter?</p>
          <div class="cdl-13__a"><p>Two drivers: hosting costs fell <b>9%</b> after the CDN renegotiation, and the Pro tier (72% margin) grew to <b>44%</b> of revenue mix — worth ~1.6 of the 2.1 point gain.</p></div>
          <p class="cdl-13__q">Draft a one-line summary for the board deck.</p>
          <div class="cdl-13__a cdl-13__thinking"><span class="cdl-13__dots" aria-hidden="true"><i></i><i></i><i></i></span><span class="cdl-13__sr">Copilot is typing</span></div>
        </div>
        <div class="cdl-13__chips"><button type="button">Explain NRR dip risk</button><button type="button">Forecast Q4 margin</button></div>
        <footer class="cdl-13__input"><span>Ask about this board…</span><button type="button" aria-label="Send">↑</button></footer>
      </div>
    </aside>
  </div>
</section>
```
## CSS
```css
.cdl-13,
.cdl-13 *,
.cdl-13 *::before,
.cdl-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cdl-13 {
  background: var(--bg);
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
  --w: 340px;
  --bg: oklch(0.975 0.005 300);
  --panel: oklch(1 0 0);
  --edge: oklch(0.905 0.012 300);
  --ink: oklch(0.26 0.02 300);
  --mut: oklch(0.55 0.02 300);
  --ai: oklch(0.6 0.19 305);
  --ai2: oklch(0.7 0.15 220);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
}

@property --cdl13-spin {
  syntax: "<angle>";
  inherits: false;
  initial-value: 210deg;
}

.cdl-13__split {
  width: 100%;
  height: 100vh;
  display: grid;
  grid-template-columns: minmax(0,1fr) var(--w);
  border: 1px solid var(--edge);
  overflow: hidden;
  background: var(--bg);
  transition: grid-template-columns .35s cubic-bezier(.2,.7,.2,1);
}

.cdl-13__split[data-closed] {
  grid-template-columns: minmax(0,1fr) 0px;
}

.cdl-13__main {
  min-width: 0;
  display: flex;
  flex-direction: column;
}

.cdl-13__bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  height: 56px;
  padding: 0 16px;
  background: var(--panel);
  border-bottom: 1px solid var(--edge);
}

.cdl-13__bar strong {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 14.5px;
}

.cdl-13__logo {
  width: 19px;
  height: 19px;
  border-radius: 6px;
  background: conic-gradient(from 210deg,var(--ai),var(--ai2));
}

.cdl-13__ask {
  display: flex;
  align-items: center;
  gap: 8px;
  border: 1px solid color-mix(in oklch,var(--ai) 40%,var(--edge));
  border-radius: 999px;
  padding: 8px 15px;
  font: 600 12.5px 'Segoe UI',system-ui,sans-serif;
  color: color-mix(in oklch,var(--ai) 80%,black);
  background: linear-gradient(120deg,color-mix(in oklch,var(--ai) 10%,white),color-mix(in oklch,var(--ai2) 10%,white));
  cursor: pointer;
  transition: box-shadow .2s,translate .15s;
}

.cdl-13__ask:hover {
  box-shadow: 0 6px 18px -8px color-mix(in oklch,var(--ai) 60%,transparent);
  translate: 0 -1px;
}

.cdl-13__ask:focus-visible {
  outline: 2px solid var(--ai);
  outline-offset: 2px;
}

.cdl-13__spark {
  width: 14px;
  height: 14px;
  background: conic-gradient(from var(--cdl13-spin),var(--ai),var(--ai2),var(--ai));
  border-radius: 50%;
  animation: cdl13-spin 6s linear infinite;
}

@keyframes cdl13-spin {
  to {
    --cdl13-spin: 570deg;
  }
}

.cdl-13__cards {
  flex: 1;
  min-height: 0;
  overflow-y: auto;
  overscroll-behavior: contain;
  padding: 16px;
  display: grid;
  gap: 12px;
  grid-template-columns: repeat(auto-fit,minmax(min(170px,100%),1fr));
  align-content: start;
}

.cdl-13__cards article {
  background: var(--panel);
  border: 1px solid var(--edge);
  border-radius: 14px;
  padding: 15px 17px;
}

.cdl-13__cards h3 {
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--mut);
}

.cdl-13__cards p {
  font-size: 23px;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
  margin: 5px 0 2px;
}

.cdl-13__cards small {
  font-size: 11px;
  font-weight: 600;
  color: var(--mut);
}

.cdl-13__up {
  color: oklch(0.55 0.13 155) !important;
}

.cdl-13__wide {
  grid-column: 1/-1;
}

.cdl-13__chart {
  display: flex;
  align-items: flex-end;
  gap: 9px;
  height: 96px;
  margin-top: 12px;
}

.cdl-13__chart i {
  flex: 1;
  position: relative;
  height: 100%;
}

.cdl-13__chart i::before,
.cdl-13__chart i::after {
  content: "";
  position: absolute;
  bottom: 0;
  border-radius: 3px 3px 0 0;
}

.cdl-13__chart i::before {
  left: 0;
  width: 52%;
  height: var(--a);
  background: var(--ai);
}

.cdl-13__chart i::after {
  right: 0;
  width: 34%;
  height: var(--b);
  background: color-mix(in oklch,var(--ai2) 55%,white);
}

.cdl-13__copilot {
  min-width: 0;
  overflow: hidden;
  background: var(--panel);
  border-left: 1px solid var(--edge);
  visibility: visible;
  transition: visibility 0s linear 0s;
}

.cdl-13__split[data-closed] .cdl-13__copilot {
  visibility: hidden;
  transition-delay: .35s;
}

.cdl-13__inner {
  width: var(--w);
  height: 100%;
  display: flex;
  flex-direction: column;
}

.cdl-13__phead {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 14px 16px;
  border-bottom: 1px solid var(--edge);
}

.cdl-13__phead b {
  font-size: 13.5px;
  display: block;
}

.cdl-13__phead small {
  font-size: 11px;
  color: var(--mut);
}

.cdl-13__avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: conic-gradient(from var(--cdl13-spin),var(--ai),var(--ai2),oklch(0.75 0.12 350),var(--ai));
  animation: cdl13-spin 8s linear infinite;
  box-shadow: inset 0 0 0 3px var(--panel);
}

.cdl-13__close {
  margin-left: auto;
  width: 32px;
  height: 32px;
  border: none;
  border-radius: 8px;
  background: transparent;
  color: var(--mut);
  font-size: 13px;
  cursor: pointer;
}

.cdl-13__close:hover {
  background: var(--bg);
  color: var(--ink);
}

.cdl-13__close:focus-visible {
  outline: 2px solid var(--ai);
  outline-offset: 2px;
}

.cdl-13__thread {
  flex: 1;
  min-height: 0;
  overflow-y: auto;
  overscroll-behavior: contain;
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.cdl-13__q {
  align-self: flex-end;
  max-width: 85%;
  font-size: 12.5px;
  line-height: 1.45;
  background: oklch(0.94 0.01 300);
  border-radius: 13px 13px 4px 13px;
  padding: 9px 13px;
}

.cdl-13__a {
  position: relative;
  max-width: 92%;
  font-size: 12.5px;
  line-height: 1.5;
  border-radius: 4px 13px 13px 13px;
  padding: 11px 14px;
  background: linear-gradient(var(--panel),var(--panel)) padding-box,linear-gradient(130deg,var(--ai),var(--ai2)) border-box;
  border: 1.5px solid transparent;
}

.cdl-13__a b {
  color: color-mix(in oklch,var(--ai) 80%,black);
}

.cdl-13__thinking {
  display: flex;
  align-items: center;
  min-height: 38px;
  background: linear-gradient(var(--panel),var(--panel)) padding-box,linear-gradient(130deg,var(--ai),var(--ai2),var(--ai)) border-box;
  background-size: 100%,200%;
  animation: cdl13-shimmer 2.2s linear infinite;
}

@keyframes cdl13-shimmer {
  to {
    background-position: 0 0,200% 0;
  }
}

.cdl-13__dots {
  display: flex;
  gap: 5px;
}

.cdl-13__dots i {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--ai);
  animation: cdl13-think 1.2s infinite;
}

.cdl-13__dots i:nth-child(2) {
  animation-delay: .15s;
}

.cdl-13__dots i:nth-child(3) {
  animation-delay: .3s;
}

@keyframes cdl13-think {
  0%,
    60%,
    100% {
    translate: 0 0;
    opacity: .4;
  }

  30% {
    translate: 0 -4px;
    opacity: 1;
  }
}

.cdl-13__chips {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  padding: 0 16px 12px;
}

.cdl-13__chips button {
  border: 1px solid var(--edge);
  background: var(--bg);
  border-radius: 999px;
  padding: 7px 12px;
  font: 600 11.5px 'Segoe UI',system-ui,sans-serif;
  color: var(--mut);
  cursor: pointer;
  transition: border-color .15s,color .15s;
}

.cdl-13__chips button:hover {
  border-color: color-mix(in oklch,var(--ai) 50%,var(--edge));
  color: color-mix(in oklch,var(--ai) 75%,black);
}

.cdl-13__chips button:focus-visible {
  outline: 2px solid var(--ai);
  outline-offset: 2px;
}

.cdl-13__input {
  display: flex;
  align-items: center;
  gap: 10px;
  margin: 0 16px 16px;
  padding: 7px 7px 7px 14px;
  border: 1px solid var(--edge);
  border-radius: 12px;
  background: var(--bg);
}

.cdl-13__input span {
  flex: 1;
  font-size: 12.5px;
  color: var(--mut);
}

.cdl-13__input button {
  width: 34px;
  height: 34px;
  border: none;
  border-radius: 9px;
  background: linear-gradient(130deg,var(--ai),var(--ai2));
  color: oklch(1 0 0);
  font-size: 15px;
  font-weight: 700;
  cursor: pointer;
  transition: scale .15s;
}

.cdl-13__input button:hover {
  scale: 1.07;
}

.cdl-13__input button:focus-visible {
  outline: 2px solid var(--ai);
  outline-offset: 2px;
}

.cdl-13__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

@container (max-width: 680px) {
  .cdl-13 {
    background: var(--bg);
    width: 100%;
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    box-sizing: border-box;
    --w: 280px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cdl-13 * {
    animation: none !important;
    transition-duration: .01s !important;
  }

  .cdl-13__dots i {
    opacity: .8;
  }
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.cdl-13__split').forEach(function (split) {
    if (split.dataset.bound) return; split.dataset.bound = '1';
    var ask = split.querySelector('.cdl-13__ask');
    function set(open) {
      split.toggleAttribute('data-closed', !open);
      ask.setAttribute('aria-expanded', String(open));
    }
    ask.addEventListener('click', function () { set(split.hasAttribute('data-closed')); });
    split.querySelector('.cdl-13__close').addEventListener('click', function () { set(false); });
  });
})();
```
