---
source: "codefronts"
url: "https://codefronts.com/navigation/css-vertical-tabs/vertical-tabs-with-view-transitions-api/"
title: "Vertical Tabs with View Transitions API"
section: "navigation"
category: "css-vertical-tabs"
category_name: "CSS Vertical Tabs"
description: "Shared-element transitions without a framework: the active indicator morphs between tabs, the panel image scales from its old position to its new one, and…"
has_js: "true"
---

Here's a working CSS Vertical Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Vertical Tabs with View Transitions API
Source: https://codefronts.com/navigation/css-vertical-tabs/vertical-tabs-with-view-transitions-api/

Shared-element transitions without a framework: the active indicator morphs between tabs, the panel image scales from its old position to its new one, and the text cross-fades — all from four lines of JavaScript and a handful of view-transition-name declarations. The browser does the work it used to take FLIP libraries to fake.
## HTML
```html
<section class="vt-14" aria-label="View Transitions API vertical tabs demo">
  <div class="vt-14__stage">
    <div class="vt-14__card" id="vt-14-card">
      <div class="vt-14__rail" id="vt-14-tablist" role="tablist" aria-orientation="vertical" aria-label="Destinations">
        <p class="vt-14__railhead">Field guide</p>
        <button class="vt-14__tab" type="button" role="tab" id="vt-14-tab1" aria-controls="vt-14-p1" aria-selected="true">Coastline</button>
        <button class="vt-14__tab" type="button" role="tab" id="vt-14-tab2" aria-controls="vt-14-p2" aria-selected="false" tabindex="-1">Highlands</button>
        <button class="vt-14__tab" type="button" role="tab" id="vt-14-tab3" aria-controls="vt-14-p3" aria-selected="false" tabindex="-1">Deep forest</button>
      </div>
      <div class="vt-14__panels">
        <article class="vt-14__panel" role="tabpanel" id="vt-14-p1" aria-labelledby="vt-14-tab1" tabindex="0">
          <img src="https://images.unsplash.com/photo-1505142468610-359e7d316be0?q=80&w=1200&auto=format&fit=crop" alt="Waves breaking on a rocky coastline at dusk" width="1200" height="800" loading="lazy">
          <div class="vt-14__copy"><h3 class="vt-14__h">The browser owns the morph</h3><p class="vt-14__p">One <code>view-transition-name</code> on the image and it scales from its old box to its new one. No FLIP maths, no library.</p></div>
        </article>
        <article class="vt-14__panel" role="tabpanel" id="vt-14-p2" aria-labelledby="vt-14-tab2" tabindex="0" hidden>
          <img src="https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?q=80&w=1200&auto=format&fit=crop" alt="Mist rolling over green highland peaks" width="1200" height="800" loading="lazy">
          <div class="vt-14__copy"><h3 class="vt-14__h">Names must be unique</h3><p class="vt-14__p">Two rendered elements sharing a name abort the whole transition. That is why only the selected tab's pill carries one.</p></div>
        </article>
        <article class="vt-14__panel" role="tabpanel" id="vt-14-p3" aria-labelledby="vt-14-tab3" tabindex="0" hidden>
          <img src="https://images.unsplash.com/photo-1441974231531-c6227db76b6e?q=80&w=1200&auto=format&fit=crop" alt="Sunlight through the canopy of a dense forest" width="1200" height="800" loading="lazy">
          <div class="vt-14__copy"><h3 class="vt-14__h">Feature-detect, always</h3><p class="vt-14__p">Where <code>startViewTransition</code> is missing, the swap happens instantly and a CSS cross-fade covers it. Nobody sees a broken state.</p></div>
        </article>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.vt-14 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--vt-14-bg);
  --vt-14-bg: oklch(0.19 0.018 240);
  --vt-14-card: oklch(0.235 0.022 240);
  --vt-14-ink: oklch(0.97 0.007 240);
  --vt-14-mut: oklch(0.72 0.016 240);
  --vt-14-acc: oklch(0.8 0.14 82);
  --vt-14-line: oklch(1 0 0/.11);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--vt-14-ink);
}

.vt-14 *,
.vt-14 *::before,
.vt-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.vt-14__stage {
  min-height: 100svh;
  display: grid;
  place-content: center;
  justify-items: center;
  padding: clamp(18px,4vw,60px);
  background: radial-gradient(70% 50% at 30% 0%,oklch(0.3 0.06 220/.6),transparent);
}

.vt-14__card {
  width: min(96vw,900px);
  display: grid;
  grid-template-columns: minmax(150px,214px) minmax(0,1fr);
  background: var(--vt-14-card);
  border: 1px solid var(--vt-14-line);
  border-radius: 20px;
  box-shadow: 0 30px 80px -40px oklch(0 0 0/.85);
  overflow: hidden;
}

.vt-14__rail {
  display: grid;
  align-content: start;
  gap: 4px;
  padding: 14px 10px;
  background: oklch(0 0 0/.16);
  border-right: 1px solid var(--vt-14-line);
}

.vt-14__railhead {
  padding: 4px 10px 10px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: color-mix(in oklch,var(--vt-14-mut) 78%,transparent);
}

.vt-14__tab {
  position: relative;
  display: flex;
  align-items: center;
  min-height: 48px;
  padding: 0 14px;
  border: 0;
  border-radius: 12px;
  background: transparent;
  font-family: inherit;
  font-size: 14.5px;
  font-weight: 640;
  text-align: left;
  color: var(--vt-14-mut);
  cursor: pointer;
  transition: color .2s ease;
}

.vt-14__tab::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 12px;
  background: color-mix(in oklch,var(--vt-14-acc) 16%,transparent);
  border: 1px solid color-mix(in oklch,var(--vt-14-acc) 38%,transparent);
  opacity: 0;
}

.vt-14__tab:hover {
  color: var(--vt-14-ink);
}

.vt-14__tab:focus-visible {
  outline: 2px solid var(--vt-14-acc);
  outline-offset: 2px;
}

.vt-14__tab[aria-selected="true"] {
  color: var(--vt-14-acc);
}

.vt-14__tab[aria-selected="true"]::before {
  opacity: 1;
  view-transition-name: vt-14-pill;
}

.vt-14__panels {
  display: grid;
  block-size: clamp(280px,34vw,340px);
}

.vt-14__panel {
  grid-area: 1/1;
  display: grid;
  grid-template-columns: minmax(0,1fr) minmax(0,1.1fr);
  align-items: stretch;
  min-block-size: 0;
}

.vt-14__panel[hidden] {
  display: none;
}

.vt-14__panel img {
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
  display: block;
  background: linear-gradient(150deg,oklch(0.34 0.06 230),oklch(0.24 0.05 260));
  view-transition-name: vt-14-hero;
}

.vt-14__copy {
  display: grid;
  align-content: center;
  gap: 11px;
  padding: clamp(20px,3vw,34px);
}

.vt-14__h {
  font-size: clamp(18px,2.3vw,24px);
  line-height: 1.18;
  letter-spacing: -.024em;
  font-weight: 690;
  text-wrap: balance;
  view-transition-name: vt-14-title;
}

.vt-14__p {
  max-width: 40ch;
  font-size: 14.4px;
  line-height: 1.62;
  color: var(--vt-14-mut);
  text-wrap: pretty;
}

.vt-14__p code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .85em;
  background: oklch(1 0 0/.09);
  padding: 2px 6px;
  border-radius: 5px;
}

.vt-14__panel:focus-visible {
  outline: 2px solid var(--vt-14-acc);
  outline-offset: -4px;
}

::view-transition-group(vt-14-pill) {
  animation-duration: .42s;
  animation-timing-function: cubic-bezier(.34,1.28,.44,1);
}

::view-transition-group(vt-14-hero) {
  animation-duration: .46s;
  animation-timing-function: cubic-bezier(.32,.72,.3,1);
}

::view-transition-old(vt-14-title),
::view-transition-new(vt-14-title) {
  animation-duration: .34s;
}

@media (max-width: 680px) {
  .vt-14__card {
    grid-template-columns: 1fr;
  }

  .vt-14__rail {
    border-right: 0;
    border-bottom: 1px solid var(--vt-14-line);
  }

  .vt-14__panels {
    block-size: auto;
  }

  .vt-14__panel {
    grid-template-columns: 1fr;
    grid-template-rows: 180px auto;
  }
}

@media (prefers-reduced-motion: reduce) {
  ::view-transition-group(*),
    ::view-transition-old(*),
    ::view-transition-new(*) {
    animation: none !important;
  }

  .vt-14 * {
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const list = document.getElementById('vt-14-tablist');
  if (!list || list.dataset.vtWired) return;
  list.dataset.vtWired = '1';
  const tabs = [...list.querySelectorAll('[role="tab"]')];
  const calm = matchMedia('(prefers-reduced-motion: reduce)');
  const swap = (tab) => tabs.forEach((t) => {
    const on = t === tab;
    t.setAttribute('aria-selected', String(on));
    t.tabIndex = on ? 0 : -1;
    document.getElementById(t.getAttribute('aria-controls')).hidden = !on;
  });
  const activate = (tab) => {
    if (!tab || tab.ariaSelected === 'true') return;
    if (!document.startViewTransition || calm.matches) return swap(tab);
    document.startViewTransition(() => swap(tab));
  };
  list.addEventListener('click', (e) => activate(e.target.closest('[role="tab"]')));
  list.addEventListener('keydown', (e) => {
    const map = { ArrowDown: 1, ArrowUp: -1, Home: 'first', End: 'last' };
    if (!(e.key in map)) return;
    e.preventDefault();
    const i = tabs.indexOf(document.activeElement);
    const to = map[e.key] === 'first' ? 0 : map[e.key] === 'last' ? tabs.length - 1
      : (i + map[e.key] + tabs.length) % tabs.length;
    tabs[to].focus(); activate(tabs[to]);
  });
})();
```
