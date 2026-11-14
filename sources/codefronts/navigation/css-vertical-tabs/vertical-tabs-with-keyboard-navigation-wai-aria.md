---
source: "codefronts"
url: "https://codefronts.com/navigation/css-vertical-tabs/vertical-tabs-with-keyboard-navigation-wai-aria/"
title: "Vertical Tabs with Keyboard Navigation (WAI-ARIA)"
section: "navigation"
category: "css-vertical-tabs"
category_name: "CSS Vertical Tabs"
description: "The reference implementation: the complete WAI-ARIA Authoring Practices tabs pattern, vertical, in 28 lines of JavaScript."
has_js: "true"
---

Here's a working CSS Vertical Tab from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Vertical Tabs with Keyboard Navigation (WAI-ARIA)
Source: https://codefronts.com/navigation/css-vertical-tabs/vertical-tabs-with-keyboard-navigation-wai-aria/

The reference implementation: the complete WAI-ARIA Authoring Practices tabs pattern, vertical, in 28 lines of JavaScript. Roving tabindex, Up/Down/Home/End, automatic and manual activation modes you can switch live, and a visible key readout so you can watch the pattern work while you learn it.
## HTML
```html
<section class="vt-18" aria-label="WAI-ARIA keyboard navigation vertical tabs demo">
  <div class="vt-18__stage">
    <div class="vt-18__head">
      <p class="vt-18__eyebrow">WAI-ARIA APG · roving tabindex</p>
      <h2 class="vt-18__title">The reference implementation</h2>
      <div class="vt-18__mode">
        <span id="vt-18-modelabel">Activation</span>
        <div class="vt-18__seg" role="group" aria-labelledby="vt-18-modelabel">
          <button class="vt-18__segbtn" type="button" id="vt-18-auto" aria-pressed="true">Automatic</button>
          <button class="vt-18__segbtn" type="button" id="vt-18-manual" aria-pressed="false">Manual</button>
        </div>
      </div>
    </div>
    <div class="vt-18__card">
      <div class="vt-18__rail" id="vt-18-tablist" role="tablist" aria-orientation="vertical" aria-label="Accessibility topics">
        <button class="vt-18__tab" type="button" role="tab" id="vt-18-t1" aria-controls="vt-18-p1" aria-selected="true"><span class="vt-18__tabtext">Roving tabindex</span><kbd class="vt-18__kbd" aria-hidden="true">1</kbd></button>
        <button class="vt-18__tab" type="button" role="tab" id="vt-18-t2" aria-controls="vt-18-p2" aria-selected="false" tabindex="-1"><span class="vt-18__tabtext">Key bindings</span><kbd class="vt-18__kbd" aria-hidden="true">2</kbd></button>
        <button class="vt-18__tab" type="button" role="tab" id="vt-18-t3" aria-controls="vt-18-p3" aria-selected="false" tabindex="-1"><span class="vt-18__tabtext">Activation modes</span><kbd class="vt-18__kbd" aria-hidden="true">3</kbd></button>
        <button class="vt-18__tab" type="button" role="tab" id="vt-18-t4" aria-controls="vt-18-p4" aria-selected="false" tabindex="-1"><span class="vt-18__tabtext">Panel semantics</span><kbd class="vt-18__kbd" aria-hidden="true">4</kbd></button>
      </div>
      <div class="vt-18__panels">
        <div class="vt-18__panel" role="tabpanel" id="vt-18-p1" aria-labelledby="vt-18-t1" tabindex="0"><h3 class="vt-18__h">One tab stop, not four</h3><p class="vt-18__p">Exactly one tab carries <code>tabindex="0"</code>; the rest are <code>-1</code>. Tab moves past the widget, arrows move inside it.</p><p class="vt-18__chip">tabindex 0 · −1 · −1 · −1</p></div>
        <div class="vt-18__panel" role="tabpanel" id="vt-18-p2" aria-labelledby="vt-18-t2" tabindex="0" hidden><h3 class="vt-18__h">Up, Down, Home, End</h3><p class="vt-18__p">Movement wraps at both ends, and every handler calls <code>preventDefault()</code> so the page never scrolls out from under the focus ring.</p><p class="vt-18__chip">↑ ↓ Home End · wraps</p></div>
        <div class="vt-18__panel" role="tabpanel" id="vt-18-p3" aria-labelledby="vt-18-t3" tabindex="0" hidden><h3 class="vt-18__h">Automatic or manual</h3><p class="vt-18__p">Automatic selects on focus. Manual moves focus and waits for Enter or Space — mandatory when a panel fetches data. Switch modes above and arrow through the rail.</p><p class="vt-18__chip">Enter · Space activate in manual mode</p></div>
        <div class="vt-18__panel" role="tabpanel" id="vt-18-p4" aria-labelledby="vt-18-t4" tabindex="0" hidden><h3 class="vt-18__h">Panels are focusable</h3><p class="vt-18__p">Each panel is <code>tabindex="0"</code> with <code>aria-labelledby</code> pointing at its tab, so scrollable content is reachable and correctly announced.</p><p class="vt-18__chip">hidden attribute, never opacity:0</p></div>
      </div>
    </div>
    <p class="vt-18__keys" id="vt-18-keys" aria-live="polite">Focus a tab and press ↑ ↓ Home End</p>
  </div>
</section>
```
## CSS
```css
.vt-18 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--vt-18-bg);
  --vt-18-bg: oklch(0.96 0.008 240);
  --vt-18-card: oklch(1 0 0);
  --vt-18-rail: oklch(0.978 0.006 240);
  --vt-18-ink: oklch(0.22 0.024 245);
  --vt-18-mut: oklch(0.53 0.02 245);
  --vt-18-acc: oklch(0.52 0.17 258);
  --vt-18-line: oklch(0.22 0.024 245/.12);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--vt-18-ink);
}

.vt-18 *,
.vt-18 *::before,
.vt-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.vt-18__stage {
  min-height: 100svh;
  display: grid;
  place-content: center;
  justify-items: center;
  gap: clamp(14px,2.4vw,24px);
  padding: clamp(20px,5vw,60px);
  background: radial-gradient(85% 55% at 50% 0%,oklch(0.93 0.04 258/.7),transparent);
}

.vt-18__head {
  display: grid;
  justify-items: center;
  gap: 10px;
  text-align: center;
}

.vt-18__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--vt-18-acc);
}

.vt-18__title {
  font-size: clamp(24px,3.6vw,38px);
  line-height: 1.08;
  letter-spacing: -.028em;
  font-weight: 720;
  text-wrap: balance;
}

.vt-18__mode {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-block-start: 4px;
  font-size: 12px;
  font-weight: 650;
  letter-spacing: .05em;
  text-transform: uppercase;
  color: var(--vt-18-mut);
}

.vt-18__seg {
  display: flex;
  gap: 3px;
  padding: 3px;
  border-radius: 99px;
  background: oklch(0.22 0.024 245/.06);
  border: 1px solid var(--vt-18-line);
}

.vt-18__segbtn {
  min-height: 34px;
  padding: 0 15px;
  border: 0;
  border-radius: 99px;
  background: transparent;
  font: inherit;
  font-size: 12px;
  text-transform: none;
  letter-spacing: 0;
  color: var(--vt-18-mut);
  cursor: pointer;
  transition: color .18s ease,background .18s ease;
}

.vt-18__segbtn:hover {
  color: var(--vt-18-ink);
}

.vt-18__segbtn[aria-pressed="true"] {
  color: oklch(1 0 0);
  background: var(--vt-18-acc);
}

.vt-18__segbtn:focus-visible {
  outline: 2px solid var(--vt-18-acc);
  outline-offset: 2px;
}

.vt-18__card {
  width: min(94vw,860px);
  display: grid;
  grid-template-columns: minmax(160px,238px) minmax(0,1fr);
  background: var(--vt-18-card);
  border: 1px solid var(--vt-18-line);
  border-radius: 18px;
  box-shadow: 0 24px 62px -32px oklch(0.22 0.024 245/.4);
  overflow: hidden;
}

.vt-18__rail {
  display: grid;
  align-content: start;
  gap: 3px;
  padding: 12px 10px;
  background: var(--vt-18-rail);
  border-right: 1px solid var(--vt-18-line);
}

.vt-18__tab {
  position: relative;
  display: flex;
  align-items: center;
  gap: 10px;
  min-height: 44px;
  padding: 0 8px 0 14px;
  border: 1px solid transparent;
  border-radius: 10px;
  background: transparent;
  font-family: inherit;
  font-size: 14.2px;
  font-weight: 600;
  text-align: left;
  color: var(--vt-18-mut);
  cursor: pointer;
  transition: color .18s ease,background .18s ease,border-color .18s ease;
}

.vt-18__tabtext {
  flex: 1;
  min-inline-size: 0;
}

.vt-18__kbd {
  flex: none;
  display: grid;
  place-items: center;
  min-inline-size: 24px;
  block-size: 22px;
  padding: 0 6px;
  border: 1px solid var(--vt-18-line);
  border-block-end-width: 2px;
  border-radius: 5px;
  background: var(--vt-18-card);
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  font-weight: 700;
  color: var(--vt-18-mut);
  box-shadow: 0 1px 0 oklch(0.22 0.024 245/.06);
  transition: color .18s ease,border-color .18s ease,background .18s ease;
}

.vt-18__tab:hover {
  color: var(--vt-18-ink);
  background: oklch(0.22 0.024 245/.04);
}

.vt-18__tab:hover .vt-18__kbd {
  color: var(--vt-18-ink);
  border-color: color-mix(in oklch,var(--vt-18-acc) 30%,var(--vt-18-line));
}

.vt-18__tab:focus-visible {
  outline: 2px dashed var(--vt-18-acc);
  outline-offset: 3px;
}

.vt-18__tab[aria-selected="true"] {
  color: var(--vt-18-acc);
  background: transparent;
  border-color: color-mix(in oklch,var(--vt-18-acc) 60%,transparent);
  border-style: dashed;
}

.vt-18__tab[aria-selected="true"] .vt-18__kbd {
  color: oklch(1 0 0);
  background: var(--vt-18-acc);
  border-color: var(--vt-18-acc);
}

.vt-18__panels {
  display: grid;
  min-height: clamp(240px,30vw,286px);
  padding: clamp(22px,3.4vw,40px);
}

.vt-18__panel {
  grid-area: 1/1;
  align-content: center;
  display: grid;
  gap: 12px;
  justify-items: start;
}

.vt-18__panel[hidden] {
  display: none;
}

.vt-18__panel:not([hidden]) {
  animation: vt-18-in .3s cubic-bezier(.32,.72,.3,1) both;
}

@keyframes vt-18-in {
  from {
    opacity: 0;
    translate: 0 8px;
  }

  to {
    opacity: 1;
    translate: 0;
  }
}

.vt-18__panel:focus-visible {
  outline: 2px solid var(--vt-18-acc);
  outline-offset: -6px;
  border-radius: 12px;
}

.vt-18__h {
  font-size: clamp(19px,2.4vw,25px);
  line-height: 1.18;
  letter-spacing: -.024em;
  font-weight: 690;
  text-wrap: balance;
}

.vt-18__p {
  max-width: 48ch;
  font-size: 14.8px;
  line-height: 1.64;
  color: var(--vt-18-mut);
  text-wrap: pretty;
}

.vt-18__p code,
.vt-18__chip,
.vt-18__keys {
  font-family: ui-monospace,Menlo,Consolas,monospace;
}

.vt-18__p code {
  font-size: .85em;
  background: oklch(0.22 0.024 245/.07);
  padding: 2px 6px;
  border-radius: 5px;
}

.vt-18__chip {
  font-size: 11px;
  padding: 7px 13px;
  border-radius: 99px;
  color: var(--vt-18-acc);
  background: color-mix(in oklch,var(--vt-18-acc) 9%,transparent);
  border: 1px solid color-mix(in oklch,var(--vt-18-acc) 24%,transparent);
}

.vt-18__keys {
  min-height: 34px;
  display: grid;
  place-items: center;
  padding: 8px 16px;
  border-radius: 99px;
  background: oklch(0.22 0.024 245/.05);
  border: 1px solid var(--vt-18-line);
  font-size: 11.5px;
  letter-spacing: .04em;
  color: var(--vt-18-mut);
}

@media (max-width: 680px) {
  .vt-18__card {
    grid-template-columns: 1fr;
  }

  .vt-18__rail {
    border-right: 0;
    border-bottom: 1px solid var(--vt-18-line);
  }
}

@media (prefers-reduced-motion: reduce) {
  .vt-18 * {
    transition-duration: .01ms !important;
    animation: none !important;
  }
}
```

## JavaScript
```js
(() => {
  const list = document.getElementById('vt-18-tablist');
  if (!list || list.dataset.vtWired) return;
  list.dataset.vtWired = '1';
  const tabs = [...list.querySelectorAll('[role="tab"]')];
  const keys = document.getElementById('vt-18-keys');
  const modes = ['vt-18-auto', 'vt-18-manual'].map((id) => document.getElementById(id));
  let automatic = true;
  const say = (k, what) => { keys.textContent = k + ' — ' + what; };
  const activate = (tab) => tabs.forEach((t) => {
    const on = t === tab;
    t.setAttribute('aria-selected', String(on));
    t.tabIndex = on ? 0 : -1;
    document.getElementById(t.getAttribute('aria-controls')).hidden = !on;
  });
  list.addEventListener('click', (e) => {
    const tab = e.target.closest('[role="tab"]');
    if (tab) { activate(tab); say('Click', 'selected ' + tab.textContent); }
  });
  list.addEventListener('keydown', (e) => {
    const i = tabs.indexOf(document.activeElement);
    const move = { ArrowDown: 1, ArrowUp: -1, Home: -i, End: tabs.length - 1 - i }[e.key];
    if (i < 0 || (move === undefined && e.key !== 'Enter' && e.key !== ' ')) return;
    e.preventDefault();
    if (move === undefined) { activate(tabs[i]); return say(e.key === ' ' ? 'Space' : 'Enter', 'activated'); }
    tabs[(i + move + tabs.length) % tabs.length].focus();
    if (automatic) activate(document.activeElement);
    say(e.key, automatic ? 'focus + select' : 'focus only');
  });
  modes.forEach((btn, idx) => btn.addEventListener('click', () => {
    automatic = idx === 0;
    modes.forEach((b, k) => b.setAttribute('aria-pressed', String((k === 0) === automatic)));
    say('Mode', automatic ? 'automatic activation' : 'manual activation');
  }));
})();
```
