---
source: "codefronts"
url: "https://codefronts.com/navigation/css-sticky-navigation/mobile-bottom-tab-bar-with-safe-area-inset-padding/"
title: "Mobile Bottom Tab Bar with Safe-Area Inset Padding"
section: "navigation"
category: "css-sticky-navigation"
category_name: "CSS Sticky Navigations"
description: "The thumb-zone navigation that mobile web apps and PWAs are judged on: five destinations pinned to the bottom of the scroll port, spaced above the home…"
has_js: "true"
---

Here's a working CSS Sticky Navigation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Mobile Bottom Tab Bar with Safe-Area Inset Padding
Source: https://codefronts.com/navigation/css-sticky-navigation/mobile-bottom-tab-bar-with-safe-area-inset-padding/

The thumb-zone navigation that mobile web apps and PWAs are judged on: five destinations pinned to the bottom of the scroll port, spaced above the home indicator instead of underneath it, with hit targets that survive a moving bus. Toggle the simulated inset in the demo to see exactly what breaks on a notched device.
## HTML
```html
<section class="sn-22" aria-label="Mobile bottom tab bar with safe area demo">
  <div class="sn-22__stage">
    <div class="sn-22__head">
      <p class="sn-22__eyebrow">position: sticky · bottom: 0 · env()</p>
      <h2 class="sn-22__title">Bottom tabs that clear the home indicator</h2>
      <p class="sn-22__sub">Scroll the feed, switch tabs, then toggle the simulated device inset.</p>
      <button class="sn-22__toggle" id="sn-22-toggle" type="button" aria-pressed="true">
        <span class="sn-22__dotled" aria-hidden="true"></span>Simulated home indicator
      </button>
    </div>
    <div class="sn-22__phone">
      <div class="sn-22__screen">
        <div class="sn-22__status" aria-hidden="true"><span>9:41</span><span class="sn-22__statusr"><span class="sn-22__sig"></span><span class="sn-22__bat"></span></span></div>
        <div class="sn-22__scroll" id="sn-22-scroll" role="region" aria-label="Trail feed, scrollable" tabindex="0">
          <header class="sn-22__top">
            <h3 class="sn-22__apptitle" id="sn-22-title">Nearby trails</h3>
            <p class="sn-22__appsub">Peak District · 12 routes</p>
          </header>
          <main class="sn-22__feed" id="sn-22-panel" aria-labelledby="sn-22-title">
            <article class="sn-22__card">
              <img class="sn-22__img" src="https://images.unsplash.com/photo-1441974231531-c6227db76b6e?q=80&w=800&auto=format&fit=crop" alt="Sunlight falling through a dense forest of tall trees" width="800" height="500" loading="lazy" decoding="async">
              <div class="sn-22__cbody"><h4 class="sn-22__ch">Beech Hollow Loop</h4><p class="sn-22__cp">6.4 km · easy · 1h 40m</p></div>
            </article>
            <article class="sn-22__card">
              <img class="sn-22__img" src="https://images.unsplash.com/photo-1506744038136-46273834b3fb?q=80&w=800&auto=format&fit=crop" alt="A still lake reflecting mountains at dusk" width="800" height="500" loading="lazy" decoding="async">
              <div class="sn-22__cbody"><h4 class="sn-22__ch">Still Water Circuit</h4><p class="sn-22__cp">11.2 km · moderate · 3h 05m</p></div>
            </article>
            <article class="sn-22__card">
              <img class="sn-22__img" src="https://images.unsplash.com/photo-1519681393784-d120267933ba?q=80&w=800&auto=format&fit=crop" alt="A mountain range under a clear night sky" width="800" height="500" loading="lazy" decoding="async">
              <div class="sn-22__cbody"><h4 class="sn-22__ch">Ridge Line Traverse</h4><p class="sn-22__cp">18.9 km · hard · 5h 20m</p></div>
            </article>
            <article class="sn-22__card">
              <img class="sn-22__img" src="https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?q=80&w=800&auto=format&fit=crop" alt="Mist drifting between pine trees on a hillside" width="800" height="500" loading="lazy" decoding="async">
              <div class="sn-22__cbody"><h4 class="sn-22__ch">Low Cloud Path</h4><p class="sn-22__cp">4.1 km · easy · 55m</p></div>
            </article>
          </main>
          <nav class="sn-22__tabs" aria-label="Primary">
            <button class="sn-22__tab" type="button" aria-current="page" data-label="Explore">
              <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M3 11.5 12 4l9 7.5M6 10v9h12v-9" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
              <span class="sn-22__tlabel">Explore</span>
            </button>
            <button class="sn-22__tab" type="button" data-label="Map">
              <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M9 4 3 6.5v13L9 17l6 2.5 6-2.5v-13L15 6.5 9 4Zm0 0v13m6-10.5V20" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
              <span class="sn-22__tlabel">Map</span>
            </button>
            <button class="sn-22__tab" type="button" data-label="Saved">
              <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M7 4h10v16l-5-3.6L7 20V4Z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
              <span class="sn-22__tlabel">Saved</span>
            </button>
            <button class="sn-22__tab" type="button" data-label="Inbox" aria-label="Inbox, 3 unread">
              <span class="sn-22__badgewrap">
                <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M3 6.5h18v11H3v-11Zm0 .5 9 6 9-6" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
                <span class="sn-22__badge" aria-hidden="true">3</span>
              </span>
              <span class="sn-22__tlabel">Inbox</span>
            </button>
            <button class="sn-22__tab" type="button" data-label="Profile">
              <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="8.5" r="3.6" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="M4.8 20a7.2 7.2 0 0 1 14.4 0" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
              <span class="sn-22__tlabel">Profile</span>
            </button>
          </nav>
        </div>
        <div class="sn-22__indicator" aria-hidden="true"></div>
      </div>
    </div>
    <p class="sn-22__live" id="sn-22-live" role="status"></p>
  </div>
</section>
```
## CSS
```css
.sn-22 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--sn-22-bg);
  --sn-22-bg: oklch(0.955 0.012 155);
  --sn-22-surface: oklch(0.995 0.003 155);
  --sn-22-ink: oklch(0.21 0.024 165);
  --sn-22-mut: oklch(0.52 0.02 165);
  --sn-22-acc: oklch(0.52 0.14 162);
  --sn-22-line: oklch(0.21 0.024 165/.12);
  --sn-22-safe: 26px;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--sn-22-ink);
  -webkit-font-smoothing: antialiased;
}

.sn-22[data-safe="off"] {
  --sn-22-safe: 0px;
}

.sn-22 *,
.sn-22 *::before,
.sn-22 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sn-22__stage {
  min-height: 100svh;
  display: grid;
  place-content: center;
  justify-items: center;
  gap: clamp(14px,2.4vw,22px);
  padding: clamp(16px,4vw,48px);
  background: radial-gradient(78% 50% at 50% 0%,oklch(0.98 0.03 160),transparent);
}

.sn-22__head {
  display: grid;
  justify-items: center;
  gap: 8px;
  text-align: center;
  max-width: 48ch;
}

.sn-22__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--sn-22-acc);
}

.sn-22__title {
  font-size: clamp(22px,3.3vw,34px);
  line-height: 1.07;
  letter-spacing: -.03em;
  font-weight: 700;
  text-wrap: balance;
}

.sn-22__sub {
  font-size: 14.2px;
  line-height: 1.58;
  color: var(--sn-22-mut);
  text-wrap: pretty;
}

.sn-22__toggle {
  display: inline-flex;
  align-items: center;
  gap: 9px;
  min-height: 42px;
  margin-block-start: 4px;
  padding: 0 16px;
  border: 1px solid var(--sn-22-line);
  border-radius: 99px;
  background: var(--sn-22-surface);
  font-family: inherit;
  font-size: 13px;
  font-weight: 620;
  color: var(--sn-22-ink);
  cursor: pointer;
  transition: border-color .2s ease,background .2s ease;
}

.sn-22__toggle:hover {
  border-color: color-mix(in oklch,var(--sn-22-acc) 45%,transparent);
}

.sn-22__toggle:focus-visible,
.sn-22__tab:focus-visible,
.sn-22__scroll:focus-visible {
  outline: 2px solid var(--sn-22-acc);
  outline-offset: 2px;
}

.sn-22__dotled {
  inline-size: 9px;
  block-size: 9px;
  border-radius: 50%;
  background: oklch(0.21 0.024 165/.22);
  transition: background .2s ease,box-shadow .2s ease;
}

.sn-22__toggle[aria-pressed="true"] .sn-22__dotled {
  background: var(--sn-22-acc);
  box-shadow: 0 0 0 4px color-mix(in oklch,var(--sn-22-acc) 20%,transparent);
}

.sn-22__phone {
  inline-size: min(90vw,330px);
  block-size: min(70svh,640px);
  padding: 11px;
  border-radius: 44px;
  background: linear-gradient(160deg,oklch(0.34 0.012 165),oklch(0.2 0.014 165));
  box-shadow: 0 32px 70px -30px oklch(0.21 0.024 165/.6),inset 0 0 0 1.5px oklch(1 0 0/.14);
}

.sn-22__screen {
  position: relative;
  block-size: 100%;
  border-radius: 34px;
  overflow: hidden;
  background: var(--sn-22-surface);
  display: grid;
  grid-template-rows: auto minmax(0,1fr);
}

.sn-22__status {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 9px 20px 3px;
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .02em;
}

.sn-22__statusr {
  display: flex;
  align-items: center;
  gap: 5px;
}

.sn-22__sig {
  inline-size: 16px;
  block-size: 9px;
  border-radius: 2px;
  background: var(--sn-22-ink);
  clip-path: polygon(0 60%,22% 60%,22% 100%,0 100%,0 60%,33% 30%,55% 30%,55% 100%,33% 100%,33% 30%,66% 0,100% 0,100% 100%,66% 100%);
}

.sn-22__bat {
  inline-size: 20px;
  block-size: 10px;
  border-radius: 3px;
  border: 1.4px solid var(--sn-22-ink);
  position: relative;
}

.sn-22__bat::after {
  content: '';
  position: absolute;
  inset: 1.6px;
  inline-size: 64%;
  border-radius: 1px;
  background: var(--sn-22-ink);
}

.sn-22__scroll {
  position: relative;
  overflow-y: auto;
  overscroll-behavior: contain;
  scroll-behavior: smooth;
  scroll-padding-block-end: calc(66px + var(--sn-22-safe));
  display: grid;
  grid-template-rows: auto 1fr auto;
  align-content: start;
}

.sn-22__top {
  padding: 10px 18px 12px;
  display: grid;
  gap: 2px;
}

.sn-22__apptitle {
  font-size: 22px;
  line-height: 1.1;
  letter-spacing: -.03em;
  font-weight: 730;
}

.sn-22__appsub {
  font-size: 12.6px;
  color: var(--sn-22-mut);
}

.sn-22__feed {
  display: grid;
  gap: 12px;
  padding: 0 14px calc(18px + var(--sn-22-safe));
}

.sn-22__card {
  border: 1px solid var(--sn-22-line);
  border-radius: 16px;
  overflow: hidden;
  background: var(--sn-22-surface);
  box-shadow: 0 10px 26px -22px oklch(0.21 0.024 165/.7);
}

.sn-22__img {
  inline-size: 100%;
  block-size: 118px;
  object-fit: cover;
  display: block;
  background: linear-gradient(140deg,oklch(0.78 0.08 160),oklch(0.55 0.1 190));
}

.sn-22__cbody {
  padding: 11px 13px 13px;
  display: grid;
  gap: 3px;
}

.sn-22__ch {
  font-size: 14.6px;
  line-height: 1.2;
  letter-spacing: -.02em;
  font-weight: 670;
}

.sn-22__cp {
  font-size: 12.4px;
  color: var(--sn-22-mut);
}

.sn-22__tabs {
  position: sticky;
  bottom: 0;
  z-index: 10;
  display: grid;
  grid-auto-flow: column;
  grid-auto-columns: 1fr;
  gap: 2px;
  padding: 6px 6px 0;
  padding-block-end: max(6px,var(--sn-22-safe));
  background: color-mix(in oklch,var(--sn-22-surface) 82%,transparent);
  backdrop-filter: blur(20px) saturate(1.6);
  -webkit-backdrop-filter: blur(20px) saturate(1.6);
  border-top: 1px solid var(--sn-22-line);
  transition: padding-block-end .32s cubic-bezier(.32,.72,.3,1);
}

.sn-22__tab {
  display: grid;
  justify-items: center;
  align-content: center;
  gap: 3px;
  min-block-size: 48px;
  padding: 6px 2px;
  border: 0;
  border-radius: 12px;
  background: transparent;
  font-family: inherit;
  color: var(--sn-22-mut);
  cursor: pointer;
  transition: color .2s ease,background .2s ease;
}

.sn-22__tab svg {
  inline-size: 21px;
  block-size: 21px;
  transition: transform .28s cubic-bezier(.34,1.56,.64,1);
}

.sn-22__tab:hover {
  color: var(--sn-22-ink);
  background: oklch(0.21 0.024 165/.05);
}

.sn-22__tab[aria-current="page"] {
  color: var(--sn-22-acc);
}

.sn-22__tab[aria-current="page"] svg {
  transform: translateY(-1px) scale(1.08);
}

.sn-22__tlabel {
  font-size: 10.4px;
  font-weight: 640;
  letter-spacing: .01em;
}

.sn-22__badgewrap {
  position: relative;
  display: grid;
  place-items: center;
}

.sn-22__badge {
  position: absolute;
  inset-block-start: -4px;
  inset-inline-start: 11px;
  min-inline-size: 16px;
  block-size: 16px;
  padding-inline: 4px;
  display: grid;
  place-items: center;
  border-radius: 99px;
  background: oklch(0.55 0.2 25);
  color: oklch(1 0 0);
  font-size: 10px;
  font-weight: 700;
  border: 1.5px solid var(--sn-22-surface);
}

.sn-22__indicator {
  position: absolute;
  inset-block-end: 8px;
  inset-inline-start: 50%;
  translate: -50% 0;
  inline-size: 106px;
  block-size: 5px;
  border-radius: 99px;
  background: oklch(0.21 0.024 165/.45);
  opacity: 0;
  transition: opacity .3s ease;
}

.sn-22[data-safe="on"] .sn-22__indicator {
  opacity: 1;
}

.sn-22__live {
  min-height: 20px;
  font-size: 12.6px;
  color: var(--sn-22-mut);
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .sn-22__scroll {
    scroll-behavior: auto;
  }

  .sn-22 * {
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sn-22');
  if (!root || root.dataset.snWired) return;
  root.dataset.snWired = '1';
  root.dataset.safe = 'on';
  const tabs = [...root.querySelectorAll('.sn-22__tab')];
  const title = root.querySelector('#sn-22-title');
  const sub = root.querySelector('.sn-22__appsub');
  const copy = { Explore: ['Nearby trails', 'Peak District · 12 routes'], Map: ['Live map', 'Following your position'], Saved: ['Saved routes', '5 offline · 2 shared'], Inbox: ['Inbox', '3 unread messages'], Profile: ['Ida Okonkwo', '148 km this month'] };
  tabs.forEach((tab) => tab.addEventListener('click', () => {
    tabs.forEach((t) => t === tab ? t.setAttribute('aria-current', 'page') : t.removeAttribute('aria-current'));
    const [h, s] = copy[tab.dataset.label] || [];
    if (h) { title.textContent = h; sub.textContent = s; }
    root.querySelector('#sn-22-scroll').scrollTop = 0;
  }));
  const toggle = root.querySelector('#sn-22-toggle');
  const live = root.querySelector('#sn-22-live');
  toggle.addEventListener('click', () => {
    const on = root.dataset.safe !== 'on';
    root.dataset.safe = on ? 'on' : 'off';
    toggle.setAttribute('aria-pressed', String(on));
    live.textContent = on ? 'Inset active — padding-block-end resolves to 26px, clearing the home indicator.' : 'Inset removed — max() holds the 6px floor so the bar keeps its spacing.';
  });
})();
```
