---
source: "codefronts"
url: "https://codefronts.com/navigation/css-vertical-tabs/product-feature-vertical-tabs-marketing-page/"
title: "Product Feature Vertical Tabs (Marketing Page)"
section: "navigation"
category: "css-vertical-tabs"
category_name: "CSS Vertical Tabs"
description: "The feature showcase every modern SaaS homepage runs: oversized type, a media panel that cross-fades, and tabs that advance themselves on a visible progress…"
has_js: "true"
---

Here's a working CSS Vertical Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Product Feature Vertical Tabs (Marketing Page)
Source: https://codefronts.com/navigation/css-vertical-tabs/product-feature-vertical-tabs-marketing-page/

The feature showcase every modern SaaS homepage runs: oversized type, a media panel that cross-fades, and tabs that advance themselves on a visible progress track. Autoplay is the part everyone gets wrong — this one pauses on hover, on keyboard focus, when the section scrolls out of view, and permanently the moment a visitor picks a tab themselves.
## HTML
```html
<section class="vt-12" aria-label="Product feature vertical tabs demo">
  <div class="vt-12__stage">
    <div class="vt-12__showcase" id="vt-12-showcase">
      <div class="vt-12__left">
        <p class="vt-12__eyebrow">Why teams switch</p>
        <h2 class="vt-12__title">Ship the whole pipeline, not just the demo</h2>
        <div class="vt-12__tabs" id="vt-12-tablist" role="tablist" aria-orientation="vertical" aria-label="Product features">
          <button class="vt-12__tab" type="button" role="tab" id="vt-12-tab1" aria-controls="vt-12-panel1" aria-selected="true"><span class="vt-12__tabtitle">Instant previews</span><span class="vt-12__tabdesc">Every branch gets a live URL in under nine seconds.</span><span class="vt-12__track"><i class="vt-12__fill"></i></span></button>
          <button class="vt-12__tab" type="button" role="tab" id="vt-12-tab2" aria-controls="vt-12-panel2" aria-selected="false" tabindex="-1"><span class="vt-12__tabtitle">Edge everywhere</span><span class="vt-12__tabdesc">318 regions, one deploy, no config file.</span><span class="vt-12__track"><i class="vt-12__fill"></i></span></button>
          <button class="vt-12__tab" type="button" role="tab" id="vt-12-tab3" aria-controls="vt-12-panel3" aria-selected="false" tabindex="-1"><span class="vt-12__tabtitle">Observability built in</span><span class="vt-12__tabdesc">Traces, logs and Core Web Vitals in one timeline.</span><span class="vt-12__track"><i class="vt-12__fill"></i></span></button>
        </div>
      </div>
      <div class="vt-12__media">
        <div class="vt-12__panel" role="tabpanel" id="vt-12-panel1" aria-labelledby="vt-12-tab1" tabindex="0"><img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=1200&auto=format&fit=crop" alt="Analytics dashboard showing deployment metrics" width="1200" height="800" loading="lazy"><p class="vt-12__cap">Preview URL ready · 8.4s</p></div>
        <div class="vt-12__panel" role="tabpanel" id="vt-12-panel2" aria-labelledby="vt-12-tab2" tabindex="0" hidden><img src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1200&auto=format&fit=crop" alt="Global network of connected nodes seen from orbit" width="1200" height="800" loading="lazy"><p class="vt-12__cap">318 edge regions · p95 41ms</p></div>
        <div class="vt-12__panel" role="tabpanel" id="vt-12-panel3" aria-labelledby="vt-12-tab3" tabindex="0" hidden><img src="https://images.unsplash.com/photo-1543286386-713bdd548da4?q=80&w=1200&auto=format&fit=crop" alt="Developer reviewing performance traces on a laptop" width="1200" height="800" loading="lazy"><p class="vt-12__cap">LCP 1.1s · CLS 0.00</p></div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.vt-12 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--vt-12-bg);
  --vt-12-bg: oklch(0.16 0.022 282);
  --vt-12-ink: oklch(0.97 0.008 282);
  --vt-12-mut: oklch(0.72 0.018 282);
  --vt-12-acc: oklch(0.78 0.16 196);
  --vt-12-line: oklch(1 0 0/.11);
  --vt-12-dwell: 6s;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--vt-12-ink);
}

.vt-12 *,
.vt-12 *::before,
.vt-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.vt-12__stage {
  min-height: 100svh;
  display: grid;
  place-content: center;
  padding: clamp(20px,5vw,68px);
  background: radial-gradient(60% 45% at 85% 15%,oklch(0.34 0.1 200/.45),transparent),radial-gradient(50% 40% at 5% 90%,oklch(0.3 0.09 300/.4),transparent);
}

.vt-12__showcase {
  width: min(96vw,1020px);
  display: grid;
  grid-template-columns: minmax(0,1fr) minmax(0,1.05fr);
  gap: clamp(24px,4vw,54px);
  align-items: center;
}

.vt-12__left {
  display: grid;
  gap: clamp(16px,2.4vw,24px);
}

.vt-12__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--vt-12-acc);
}

.vt-12__title {
  font-size: clamp(28px,4.4vw,46px);
  line-height: 1.04;
  letter-spacing: -.035em;
  font-weight: 750;
  text-wrap: balance;
}

.vt-12__tabs {
  display: grid;
  gap: 4px;
  margin-block-start: 6px;
}

.vt-12__tab {
  position: relative;
  display: grid;
  gap: 4px;
  padding: 16px 18px 18px;
  border: 0;
  border-radius: 14px;
  background: transparent;
  font-family: inherit;
  text-align: left;
  cursor: pointer;
  transition: background .24s ease;
}

.vt-12__tabtitle {
  font-size: 16.5px;
  font-weight: 680;
  letter-spacing: -.015em;
  color: var(--vt-12-mut);
  transition: color .24s ease;
}

.vt-12__tabdesc {
  font-size: 13.6px;
  line-height: 1.5;
  color: color-mix(in oklch,var(--vt-12-mut) 78%,transparent);
  max-width: 40ch;
  text-wrap: pretty;
}

.vt-12__track {
  position: absolute;
  inset-block-end: 0;
  inset-inline: 18px;
  block-size: 2px;
  border-radius: 99px;
  background: oklch(1 0 0/.1);
  overflow: hidden;
}

.vt-12__fill {
  display: block;
  block-size: 100%;
  border-radius: 99px;
  background: var(--vt-12-acc);
  scale: 0 1;
  transform-origin: left center;
}

.vt-12__tab:hover {
  background: oklch(1 0 0/.05);
}

.vt-12__tab:hover .vt-12__tabtitle {
  color: var(--vt-12-ink);
}

.vt-12__tab:focus-visible {
  outline: 2px solid var(--vt-12-acc);
  outline-offset: 2px;
}

.vt-12__tab[aria-selected="true"] {
  background: oklch(1 0 0/.07);
}

.vt-12__tab[aria-selected="true"] .vt-12__tabtitle {
  color: var(--vt-12-ink);
}

.vt-12__tab[aria-selected="true"] .vt-12__fill {
  animation: vt-12-grow var(--vt-12-dwell) linear forwards;
}

.vt-12__showcase[data-paused="true"] .vt-12__fill {
  animation-play-state: paused;
}

.vt-12__showcase[data-stopped="true"] .vt-12__tab[aria-selected="true"] .vt-12__fill {
  animation: none;
  scale: 1 1;
  opacity: .5;
}

@keyframes vt-12-grow {
  from {
    scale: 0 1;
  }

  to {
    scale: 1 1;
  }
}

.vt-12__media {
  display: grid;
  aspect-ratio: 4/3;
  border-radius: 20px;
  border: 1px solid var(--vt-12-line);
  background: linear-gradient(150deg,oklch(0.3 0.07 240),oklch(0.2 0.05 290));
  box-shadow: 0 40px 90px -44px oklch(0 0 0/.9);
  overflow: hidden;
}

.vt-12__panel {
  grid-area: 1/1;
  position: relative;
  display: grid;
}

.vt-12__panel[hidden] {
  display: none;
}

.vt-12__panel:not([hidden]) {
  animation: vt-12-fade .5s cubic-bezier(.32,.72,.3,1) both;
}

@keyframes vt-12-fade {
  from {
    opacity: 0;
    scale: 1.03;
  }

  to {
    opacity: 1;
    scale: 1;
  }
}

.vt-12__panel img {
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
  display: block;
}

.vt-12__cap {
  position: absolute;
  inset-block-end: 14px;
  inset-inline-start: 14px;
  padding: 8px 13px;
  border-radius: 99px;
  background: oklch(0.14 0.02 282/.72);
  backdrop-filter: blur(10px);
  border: 1px solid oklch(1 0 0/.14);
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .02em;
  color: var(--vt-12-ink);
}

.vt-12__panel:focus-visible {
  outline: 2px solid var(--vt-12-acc);
  outline-offset: -4px;
}

@media (max-width: 760px) {
  .vt-12__showcase {
    grid-template-columns: 1fr;
  }

  .vt-12__media {
    order: -1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .vt-12 * {
    animation: none !important;
    transition-duration: .01ms !important;
  }

  .vt-12__fill {
    scale: 1 1;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.getElementById('vt-12-showcase');
  if (!root || root.dataset.vtWired) return;
  root.dataset.vtWired = '1';
  const tabs = [...document.querySelectorAll('#vt-12-tablist [role="tab"]')];
  const calm = matchMedia('(prefers-reduced-motion: reduce)').matches;
  let timer = null, stopped = calm;
  const select = (tab) => tabs.forEach((t) => {
    const on = t === tab;
    t.setAttribute('aria-selected', String(on));
    t.tabIndex = on ? 0 : -1;
    document.getElementById(t.getAttribute('aria-controls')).hidden = !on;
  });
  const advance = () => select(tabs[(tabs.findIndex((t) => t.ariaSelected === 'true') + 1) % tabs.length]);
  const run = (on) => {
    clearInterval(timer);
    timer = on && !stopped ? setInterval(advance, 6000) : null;
    root.dataset.paused = String(!timer && !stopped);
  };
  root.addEventListener('click', (e) => {
    const tab = e.target.closest('[role="tab"]');
    if (!tab) return;
    stopped = true; root.dataset.stopped = 'true'; run(false); select(tab);
  });
  ['pointerenter', 'focusin'].forEach((ev) => root.addEventListener(ev, () => run(false)));
  ['pointerleave', 'focusout'].forEach((ev) => root.addEventListener(ev, () => run(true)));
  new IntersectionObserver((es) => es.forEach((e) => run(e.isIntersecting)), { threshold: 0.4 }).observe(root);
})();
```
